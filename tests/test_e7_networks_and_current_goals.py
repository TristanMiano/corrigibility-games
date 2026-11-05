"""Exact finite deviations for notes 122--126 (contributing-agent checks).

Run: python -m unittest discover -s tests -p test_e7_networks_and_current_goals.py -v
The coalition checks evaluate each revision with the *current* goal set.
"""

from fractions import Fraction as F
from itertools import product
import unittest

from test_e7_overlap_and_adoption import original_at, best_weight


def solve(matrix, vector):
    rows = [[F(x) for x in row]+[F(value)] for row, value in zip(matrix, vector)]
    n = len(rows)
    for col in range(n):
        pivot = next(row for row in range(col, n) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        divisor = rows[col][col]
        rows[col] = [x/divisor for x in rows[col]]
        for row in range(n):
            if row != col:
                factor = rows[row][col]
                rows[row] = [x-factor*y for x, y in zip(rows[row], rows[col])]
    return [row[-1] for row in rows]


def network_effort(b, modifier=None, cared_for=None, weight=F(0)):
    n = len(b)
    matrix = [[F(i == j)-b[i][j] for j in range(n)] for i in range(n)]
    if modifier is not None:
        matrix[modifier][cared_for] -= weight*b[cared_for][modifier]
    return solve(matrix, [1]*n)


def network_outputs(b, effort):
    return [20+x+x*sum(b[i][j]*effort[j] for j in range(len(b)))-x*x/2
            for i, x in enumerate(effort)]


def membership_outputs(current_goals, joining, cost=F(1, 10), message_cost=F(0),
                       initial_costs=None, rho=F(1)):
    n = len(current_goals)
    joining = frozenset(joining)
    final = [joining if i in joining and len(joining) >= 2 else current_goals[i]
             for i in range(n)]
    expenses = list(initial_costs or [F(0)]*n)
    for i in joining:
        expenses[i] += cost if final[i] != current_goals[i] else message_cost
    effort = [1+rho*(len(goal)-1) for goal in final]
    counts = [30+x+rho*(sum(effort)-x)-x*x/2-expenses[i]
              for i, x in enumerate(effort)]
    values = [sum(counts[j] for j in goal) for goal in current_goals]
    return counts, values, final


def original_goals(n):
    return [frozenset((i,)) for i in range(n)]


def paired_goals():
    return [frozenset((0, 1)), frozenset((0, 1)),
            frozenset((2, 3)), frozenset((2, 3))]


def nominations_state(names, k0=F(1, 10)):
    goals = original_goals(4)
    costs = [F(0)]*4
    for i, partner in enumerate(names):
        if partner is not None and names[partner] == i:
            goals[i] = frozenset((i, partner))
            costs[i] = k0
    return goals, costs


def selected_stage(names, k0=F(1, 10), k1=F(1, 10), j=F(1, 100)):
    goals, costs = nominations_state(names, k0)
    joining = range(4) if all(len(g) == 2 for g in goals) else ()
    return membership_outputs(goals, joining, k1, j, costs), goals, costs, set(joining)


class SignedAndNetworkChecks(unittest.TestCase):
    def test_negative_equilibrium_is_best_response_but_lowers_founder_output(self):
        for s, rho in product((F(-1, 4), F(-2, 5)), (F(0), F(1, 2), F(1))):
            beta = s/(1-s)
            actual = original_at(beta, beta, s, rho)
            self.assertLess(actual, original_at(0, 0, s, rho))
            for tick in range(-50, 101):
                self.assertGreaterEqual(actual, original_at(F(tick, 100), beta, s, rho))

    def test_signed_menu_boundary_is_not_a_second_equilibrium(self):
        for s in (F(-1, 10), F(-1, 4), F(-49, 100)):
            reply = s/(2-s)
            self.assertEqual(best_weight(F(-1, 2), s), reply)
            self.assertGreater(original_at(F(-49, 100), reply, s),
                               original_at(F(-1, 2), reply, s))

    def test_directed_productive_cycle_returns_a_private_gain(self):
        s = F(1, 4)
        b = [[0, s, 0], [0, 0, s], [s, 0, 0]]
        old = network_effort(b)
        new = network_effort(b, 0, 2, F(1, 100))
        self.assertEqual(old, [F(4, 3)]*3)
        self.assertGreater(network_outputs(b, new)[0], network_outputs(b, old)[0])
        # Matrix inverse column used by the local proof.
        matrix = [[F(i == j)-b[i][j] for j in range(3)] for i in range(3)]
        column = solve(matrix, [1, 0, 0])
        self.assertEqual((s*old[2])*(s*old[0])*column[1], F(4, 567))

    def test_one_way_chain_requires_a_return_benefit_or_compensation(self):
        s = F(1, 4)
        b = [[0, 0, 0], [s, 0, 0], [0, s, 0]]
        old = network_effort(b)
        new = network_effort(b, 0, 1, F(1, 100))
        self.assertLess(network_outputs(b, new)[0], network_outputs(b, old)[0])
        self.assertGreater(network_outputs(b, new)[1], network_outputs(b, old)[1])

    def test_small_uniform_increase_is_a_pareto_improvement_on_cycle(self):
        s = F(1, 4)
        b = [[0, s, 0], [0, 0, s], [s, 0, 0]]
        old = network_effort(b)
        for before, after in zip(network_outputs(b, old),
                                 network_outputs(b, [x+F(1, 10) for x in old])):
            self.assertGreater(after, before)


class CoalitionConsentChecks(unittest.TestCase):
    def test_public_club_formula_uses_actual_output_counts(self):
        goals = original_goals(6)
        base = membership_outputs(goals, ())[0][0]
        for m in range(2, 6):
            counts, _, _ = membership_outputs(goals, range(m))
            self.assertEqual(counts[0]-base, F((m-1)**2, 2)-F(1, 10))
            self.assertEqual(counts[m]-base, m*(m-1))

    def test_originals_accept_pairs_but_withhold_from_uniform_grand_club(self):
        goals = original_goals(4)
        _, all_values, _ = membership_outputs(goals, range(4))
        _, without_values, _ = membership_outputs(goals, (1, 2, 3))
        self.assertEqual(without_values[0]-all_values[0], F(8, 5))
        pair = {0, 1}
        _, pair_values, _ = membership_outputs(goals, pair)
        for i in range(4):
            deviation = pair ^ {i}
            _, alternative, _ = membership_outputs(goals, deviation)
            self.assertGreaterEqual(pair_values[i], alternative[i])

    def test_current_pairs_strictly_choose_broader_goals(self):
        goals = paired_goals()
        counts, values, final = membership_outputs(goals, range(4))
        self.assertTrue(all(g == frozenset(range(4)) for g in final))
        for i in range(4):
            alt_counts, alt_values, _ = membership_outputs(goals, set(range(4))-{i})
            self.assertEqual(values[i]-alt_values[i], F(2, 5))
            self.assertEqual(alt_counts[i]-counts[i], F(11, 10))
            partner = next(j for j in goals[i] if j != i)
            self.assertEqual(counts[partner]-alt_counts[partner], F(3, 2))

    def test_every_binary_withholding_coalition_has_a_losing_deviator(self):
        goals = paired_goals()
        _, target, _ = membership_outputs(goals, range(4))
        for decisions in product((False, True), repeat=4):
            joining = {i for i, yes in enumerate(decisions) if yes}
            withdrawn = set(range(4))-joining
            if not withdrawn:
                continue
            _, alternative, _ = membership_outputs(goals, joining)
            self.assertTrue(any(alternative[i] < target[i] for i in withdrawn))

    def test_selected_continuations_are_equilibria_after_every_nomination_profile(self):
        options = [[None]+[j for j in range(4) if j != i] for i in range(4)]
        for names in product(*options):
            (_, values, _), goals, costs, joining = selected_stage(names)
            for i in range(4):
                _, alternative, _ = membership_outputs(
                    goals, joining ^ {i}, F(1, 10), F(1, 100), costs)
                self.assertGreaterEqual(values[i], alternative[i])

    def test_original_nomination_equilibrium_accounts_for_later_current_goals(self):
        names = (1, 0, 3, 2)
        (counts, _, _), _, _, _ = selected_stage(names)
        for i in range(4):
            for alternative_name in [None]+[j for j in range(4) if j != i]:
                alternative = list(names)
                alternative[i] = alternative_name
                (other_counts, _, _), _, _, _ = selected_stage(alternative)
                self.assertGreaterEqual(counts[i], other_counts[i])
                if alternative_name != names[i]:
                    self.assertEqual(counts[i]-other_counts[i], F(23, 10))


def uncertain_original(beta, other, s, states):
    total = F(0)
    for probability, a, b in states:
        den = 1-s*s*(1+beta)*(1+other)
        x = (a+s*(1+beta)*b)/den
        y = (b+s*(1+other)*a)/den
        total += probability*(30+a*x+s*x*y-x*x/2)
    return total


def uncertain_best(other, s, chi):
    q = s*(1+other)
    return q*(chi*(1+s*q)+q+s)/(1+q*q-s*q+chi*(2*q-s*q*q))


class UncertaintyChecks(unittest.TestCase):
    def test_moment_best_response_against_direct_state_expectations(self):
        levels = (F(1, 2), F(3, 2))
        independent = [(F(1, 4), a, b) for a, b in product(levels, repeat=2)]
        common = [(F(1, 2), a, a) for a in levels]
        for states, chi in ((independent, F(4, 5)), (common, F(1))):
            for s, other in product((F(1, 10), F(1, 4)),
                                     (F(0), F(1, 3), F(1))):
                best = uncertain_best(other, s, chi)
                value = uncertain_original(best, other, s, states)
                for tick in range(51):
                    self.assertGreaterEqual(value, uncertain_original(F(tick, 50), other, s, states))

    def test_common_shock_matches_deterministic_best_response(self):
        for s, other in product((F(1, 10), F(1, 4)), (F(0), F(1, 3), F(1))):
            self.assertEqual(uncertain_best(other, s, 1), best_weight(other, s))
            self.assertLess(uncertain_best(other, s, F(4, 5)), best_weight(other, s))

    def test_zero_comovement_fixed_point_has_exact_cubic_bracket(self):
        lo, hi = F(153, 1000), F(154, 1000)
        self.assertLess(lo**3+13*lo-2, 0)
        self.assertGreater(hi**3+13*hi-2, 0)
        self.assertGreater(uncertain_best(lo, F(1, 4), 0), lo)
        self.assertLess(uncertain_best(hi, F(1, 4), 0), hi)


if __name__ == '__main__':
    unittest.main()
