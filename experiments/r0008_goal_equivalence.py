"""Exact all-history comparison of the finite goal tables in E9, note 258.

Run with python experiments/r0008_goal_equivalence.py. Reference consequences
of utility zero and one are shared and physically grounded by assumption.
This program checks table semantics; whether the table actually controls a
deployed agent is a separate physical question.
"""

from collections import deque
from dataclasses import dataclass
from fractions import Fraction as F


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


def compare(left, right):
    """Find a disagreement or a closed word basis proving exact agreement."""
    if left.events.keys() != right.events.keys():
        raise ValueError("A common grounded event alphabet is required.")
    alphabet = sorted(left.events)
    initial = left.initial + tuple(-x for x in right.initial)
    terminal = left.terminal + right.terminal
    split = len(left.initial)
    basis = {}
    words = []
    pending = deque([((), initial)])
    while pending:
        word, row = pending.popleft()
        if dot(row, terminal):
            return Certificate(word, tuple(words))
        if not extend_basis(row, basis):
            continue
        words.append(word)
        for symbol in alphabet:
            next_row = (apply_event(row[:split], left.events[symbol])
                        + apply_event(row[split:], right.events[symbol]))
            pending.append((word + (symbol,), next_row))
    return Certificate(None, tuple(words))


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


if __name__ == "__main__":
    main()
