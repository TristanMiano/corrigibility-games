"""Compare finite goal tables and price lottery disagreement in E9, notes 258 and 286–288.

Run with python experiments/r0008_goal_equivalence.py. Reference consequences
of utility zero and one may be shared for score comparison. Preference
comparison needs only a common domain of events and objective lotteries.
This program checks table semantics; whether the table actually controls a
deployed agent is a separate physical question.
"""

from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations


def probability_vector(row, size):
    return (len(row) == size and all(isinstance(x, (int, F)) and 0 <= x <= 1 for x in row)
            and sum(row) == 1)


def apply_event(row, matrix):
    return tuple(sum(weight * value for weight, value in zip(row, column))
                 for column in zip(*matrix))


def dot(row, values):
    return sum(x * y for x, y in zip(row, values))


@dataclass(frozen=True)
class GoalTable:
    initial: tuple
    events: dict
    terminal: tuple

    def __post_init__(self):
        n = len(self.initial)
        if not n or not probability_vector(self.initial, n):
            raise ValueError("Initial state weights must be an exact probability vector.")
        if len(self.terminal) != n or not all(isinstance(v, (int, F)) and 0 <= v <= 1 for v in self.terminal):
            raise ValueError("Terminal scores must lie between the two normalized anchors.")
        for name, matrix in self.events.items():
            if len(matrix) != n or not all(probability_vector(row, n) for row in matrix):
                raise ValueError(f"The event {name!r} needs a square, exact stochastic matrix.")

    def score(self, word):
        row = self.initial
        for symbol in word:
            row = apply_event(row, self.events[symbol])
        return dot(row, self.terminal)


def extend_basis(row, basis):
    """Insert an independent row in echelon form, keyed by pivot column."""
    residual = list(map(F, row))
    for pivot in sorted(basis):
        weight = residual[pivot]
        if weight:
            residual = [x - weight * y for x, y in zip(residual, basis[pivot])]
    for pivot, value in enumerate(residual):
        if value:
            basis[pivot] = tuple(x / value for x in residual)
            return True
    return False


@dataclass(frozen=True)
class Certificate:
    # None certifies equivalence; the empty tuple is a genuine possible witness.
    witness: tuple | None
    basis_words: tuple


@dataclass(frozen=True)
class HistoryDomain:
    """Complete deterministic recognizer for the histories covered by a contract."""
    initial: str
    accepting: frozenset
    transitions: dict

    def validate(self, alphabet):
        states = self.transitions.keys()
        if self.initial not in states or not self.accepting <= states:
            raise ValueError("The domain's initial and accepting states must exist.")
        for moves in self.transitions.values():
            if moves.keys() != alphabet or any(next_state not in states for next_state in moves.values()):
                raise ValueError("The history domain needs a defined transition for every event and state.")

    def accepts(self, word):
        state = self.initial
        for symbol in word:
            state = self.transitions[state][symbol]
        return state in self.accepting


def _search_words(left, right, terminal, domain=None):
    if left.events.keys() != right.events.keys():
        raise ValueError("A common grounded event alphabet is required.")
    alphabet = sorted(left.events)
    initial = left.initial + tuple(-x for x in right.initial)
    split = len(left.initial)
    if domain is not None:
        domain.validate(left.events.keys())
    # Separate domain states occupy disjoint blocks in the product automaton.
    bases = {}
    words = []
    pending = deque([((), initial, domain.initial if domain is not None else None)])
    while pending:
        word, row, state = pending.popleft()
        if (terminal is not None and (domain is None or state in domain.accepting)
                and dot(row, terminal)):
            return Certificate(word, tuple(words))
        if not extend_basis(row, bases.setdefault(state, {})):
            continue
        words.append(word)
        for symbol in alphabet:
            next_row = (apply_event(row[:split], left.events[symbol])
                        + apply_event(row[split:], right.events[symbol]))
            next_state = domain.transitions[state][symbol] if domain is not None else None
            pending.append((word + (symbol,), next_row, next_state))
    return Certificate(None, tuple(words))


def compare(left, right):
    """Find unequal normalized scores or a closed word basis certifying equality."""
    return _search_words(left, right, left.terminal + right.terminal)


@dataclass(frozen=True)
class PreferenceCertificate:
    scale: F | None
    offset: F | None
    # A witness contains two lotteries, each a tuple of (probability, event word).
    witness: tuple | None
    basis_words: tuple


def compare_preferences(left, right, *, domain=None):
    """Certify the same lottery ordering in independent units, or return a witness."""
    words = _search_words(left, right, None, domain).basis_words
    scores = [(left.score(w), right.score(w), w) for w in words
              if domain is None or domain.accepts(w)]
    if not scores:
        return PreferenceCertificate(F(1), F(0), None, words)
    lo = min(scores, key=lambda point: point[0])
    hi = max(scores, key=lambda point: point[0])

    def pure(point):
        return ((F(1), point[2]),)

    def disagreement(first, second):
        return PreferenceCertificate(None, None, (first, second), words)

    if lo[0] == hi[0]:
        for point in scores:
            if point[1] != lo[1]:
                return disagreement(pure(lo), pure(point))
        return PreferenceCertificate(F(1), F(lo[1] - lo[0]), None, words)

    scale = F(hi[1] - lo[1]) / (hi[0] - lo[0])
    if scale <= 0:
        return disagreement(pure(lo), pure(hi))
    offset = lo[1] - scale * lo[0]
    for point in scores:
        if point[1] != scale * point[0] + offset:
            high_weight = F(point[0] - lo[0]) / (hi[0] - lo[0])
            mixture = tuple((weight, end[2]) for weight, end in
                            ((1 - high_weight, lo), (high_weight, hi)) if weight)
            return disagreement(pure(point), mixture)
    return PreferenceCertificate(scale, offset, None, words)


def worst_lottery_loss(values, measure, *, target_slack=None):
    """Largest loss in values(P)-values(Q) over two objective lotteries.

    Without a slack, allow Q whenever the installed measure ranks it at
    least as high as P (note 287). With a slack, allow Q when it scores
    from zero to that amount below P on the target measure (note 288).
    Each entry can also be an expected score for an attainable recipe.
    """
    if len(values) != len(measure) or not values:
        raise ValueError("Both columns must describe the same nonempty outcome set.")
    if target_slack is not None and target_slack < 0:
        raise ValueError("A target-value tolerance must be nonnegative.")
    points = tuple(zip(map(F, values), map(F, measure)))
    # Between crossings the maximum and minimum residuals are linear.
    slopes = {F(0)}
    for (value_i, m_i), (value_j, m_j) in combinations(points, 2):
        if m_i == m_j:
            continue
        slope = (value_i - value_j) / (m_i - m_j)
        if target_slack is not None or slope >= 0:
            slopes.add(slope)
    costs = []
    for slope in slopes:
        residuals = [value - slope * m for value, m in points]
        width = max(residuals) - min(residuals)
        if target_slack is not None:
            width += F(target_slack) * max(0, slope)
        costs.append(width)
    return min(costs)


def check_equality_proof(left, right, basis_words):
    """Check a supplied basis independently of the order it was discovered."""
    if left.events.keys() != right.events.keys():
        return False
    basis_words = tuple(tuple(word) for word in basis_words)
    if any(symbol not in left.events for word in basis_words for symbol in word):
        return False

    def paired_row(word):
        lo, hi = left.initial, right.initial
        for symbol in word:
            lo = apply_event(lo, left.events[symbol])
            hi = apply_event(hi, right.events[symbol])
        return lo + tuple(-x for x in hi)

    basis = {}
    terminal = left.terminal + right.terminal
    for word in basis_words:
        row = paired_row(word)
        if dot(row, terminal):
            return False
        extend_basis(row, basis)
    if extend_basis(paired_row(()), basis.copy()):
        return False
    return all(
        not extend_basis(paired_row(word + (symbol,)), basis.copy())
        for word in basis_words for symbol in left.events
    )


def point_exception(word, alphabet=("red", "blue")):
    """Half on every word except the selected word, where the score is one."""
    length = len(word)
    sink = length + 1
    size = length + 2
    states = tuple(range(size))
    def destination(i, symbol):
        return i + 1 if i < length and word[i] == symbol else sink
    events = {
        symbol: tuple(tuple(int(j == destination(i, symbol)) for j in states) for i in states)
        for symbol in alphabet
    }
    return GoalTable(tuple(int(i == 0) for i in states), events,
                     tuple(F(1) if i == length else F(1, 2) for i in states))


def main():
    alphabet = ("red", "blue")
    routine = GoalTable((1,), {event: ((1,),) for event in alphabet}, (F(1, 2),))
    expanded = GoalTable((1, 0),
                         {"red": ((0, 1), (1, 0)), "blue": ((F(1, 3), F(2, 3)), (0, 1))},
                         (F(1, 2), F(1, 2)))
    same = compare(routine, expanded)
    assert same.witness is None
    print("Equivalent tables; closed word basis:", same.basis_words)
    altered_word = tuple(alphabet[i % 2] for i in range(12))
    altered = point_exception(altered_word)
    result = compare(routine, altered)
    assert result.witness == altered_word
    print("Disagree on:", " ".join(result.witness))
    print("Scores:", routine.score(result.witness), altered.score(result.witness))
    target = (F(0), F(1, 2), F(1))
    near = (F(0), F(4, 5), F(1))
    print("Largest target loss across lotteries:", worst_lottery_loss(target, near))
    print("Blue's exposure among equal joint totals:", worst_lottery_loss((2, 8), (10, 10), target_slack=0))


if __name__ == "__main__":
    main()
