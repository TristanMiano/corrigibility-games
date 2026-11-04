"""Exact checks of scoped recognition menus and multi-partner certificates.

The confirmation test deliberately rejects the remediation-only assessment
when another audit is allowed after a pass. Enumerated cooperative games
test the stated complementarity class, not external-attack equilibria.
"""

from fractions import Fraction as F
from itertools import combinations, permutations, product
import unittest


def integral_linear(intercept, slope, low, high):
    return intercept*(high-low)+slope*(high*high-low*low)/2


def chosen_capacity_values(n, edges, costs):
    subsets = [frozenset(i for i in range(n) if mask & (1 << i))
               for mask in range(1 << n)]
    f = {s: sum((value for (i, j), value in edges.items() if i in s and j in s), F(0))
            -sum((costs[i] for i in s), F(0)) for s in subsets}
    return {s: max(f[a] for a in subsets if a <= s) for s in subsets}


class RecognitionChecks(unittest.TestCase):
    def test_one_check_assessment_and_distinct_outcomes(self):
        g, fraud, v, loss, error, cost_cap, audit = (
            F(1, 5), F(2, 5), F(3, 10), F(1, 2), F(1, 10), F(3, 10), F(1, 50))
        h = g-error*fraud
        adoption = h/cost_cap
        outcomes = adoption, (1-adoption)*error, (1-adoption)*(1-error)
        self.assertEqual(outcomes, (F(8, 15), F(7, 150), F(21, 50)))
        self.assertEqual(sum(outcomes), 1)
        checked = outcomes[0]*v-outcomes[1]*loss-audit
        trusted = adoption*v-(1-adoption)*loss
        self.assertEqual(checked, F(7, 60))
        self.assertEqual(trusted, -F(11, 150))
        self.assertGreater(checked, max(trusted, 0))
        posterior = adoption/(adoption+(1-adoption)*error)
        self.assertGreater(posterior, loss/(v+loss))
        self.assertEqual(error*fraud+h*h/(2*cost_cap), F(31, 375))

    def test_fixed_quality_accuracy_can_reduce_combat(self):
        def rates(error):
            adoption = (F(1, 5)-error*F(2, 5))/F(3, 10)
            return adoption, (1-adoption)*error, (1-adoption)*(1-error)
        before, after = rates(F(1, 10)), rates(F(1, 20))
        self.assertGreater(after[0], before[0])
        self.assertLess(after[1], before[1])
        self.assertLess(after[2], before[2])

    def test_mixed_checking_trusting_equations(self):
        g, fraud, k, error, loss, v = F(1), F(2), F(1), F(1, 10), F(1), F(4)
        previous = None
        for audit in (F(1, 5), F(19, 100)):
            adoption = 1-audit/((1-error)*loss)
            check_rate = (fraud-g+k*adoption)/((1-error)*fraud)
            self.assertTrue(0 < adoption < 1 and 0 < check_rate < 1)
            self.assertEqual(check_rate*(1-error)*fraud-(fraud-g), k*adoption)
            checked = adoption*v-(1-adoption)*error*loss-audit
            trusted = adoption*v-(1-adoption)*loss
            self.assertEqual(checked, trusted)
            self.assertGreater(trusted, 0)
            if previous is not None:
                self.assertGreater(adoption, previous)
            previous = adoption

    def test_late_change_repairs_the_restricted_one_check_menu(self):
        g, fraud, error = F(1, 5), F(2, 5), F(1, 10)
        for cost in (F(0), F(1, 20), F(1, 10), F(19, 100)):
            direct = g-cost
            delayed = error*fraud+(1-error)*(g-cost)
            self.assertGreater(delayed, direct)
            self.assertEqual(delayed-direct, error*(fraud-g+cost))

    def test_two_opportunity_remediation_strategies_and_exact_integrals(self):
        g, fraud, error, attempt, cap = F(1, 5), F(2, 5), F(1, 10), F(3, 100), F(3, 10)
        a, h = F(7, 100), F(4, 25)
        self.assertEqual(a, (1-error)*attempt/error-(fraud-g))
        self.assertEqual(h, g-error*fraud)
        for index in range(301):
            cost = F(index, 1000)
            last_g, last_f = g-cost-attempt, error*fraud-attempt
            direct = g-cost-attempt
            delayed = -attempt+error*fraud+(1-error)*max(last_g, last_f, 0)
            if cost < a:
                self.assertGreater(direct, max(delayed, 0))
            elif cost > a:
                self.assertGreater(delayed, max(direct, 0))
            if cost < h:
                self.assertGreater(last_g, last_f)
            elif cost > h:
                self.assertGreater(last_f, last_g)
        value = (integral_linear(g-attempt, -1, F(0), a)
                 +integral_linear(F(163, 1000), -F(9, 10), a, h)
                 +integral_linear(F(19, 1000), F(0), h, cap))/cap
        self.assertEqual(value, F(3493, 60000))
        genuine = a/cap+(1-error)*(h-a)/cap
        accepted_fraud = error*(cap-a)/cap+error*(1-error)*(cap-h)/cap
        combat = (1-error)**2*(cap-h)/cap
        checks = 1+(1-error)*(cap-a)/cap
        self.assertEqual((genuine, accepted_fraud, combat),
                         (F(151, 300), F(89, 750), F(189, 500)))
        self.assertEqual(sum((genuine, accepted_fraud, combat)), 1)
        self.assertEqual(checks, F(169, 100))
        buyer = genuine*F(3, 10)-accepted_fraud*F(1, 2)-checks*F(1, 50)
        self.assertEqual(buyer, F(217, 3750))

    def test_confirmation_is_a_profitable_deviation_from_remediation_only(self):
        first_pass = F(93, 1000)
        immediate = (F(7, 100)*F(3, 10)-F(23, 1000)*F(1, 2))/first_pass
        confirm = (F(79, 1000)*F(3, 10)-F(14, 10000)*F(1, 2))/first_pass-F(1, 50)
        self.assertEqual(immediate, F(95, 930))
        self.assertEqual(confirm, F(115, 465)-F(1, 50))
        self.assertEqual(confirm-immediate, F(97, 775))
        self.assertGreater(confirm, immediate)

    def test_quality_optimization_by_independent_grid_search(self):
        def optimize(error, audit):
            options = []
            for numerator in range(1601):
                effort_cost = F(numerator, 1600)
                g, fraud, loss = F(2, 5)-effort_cost, F(2, 5), F(1, 2)
                v = 4*effort_cost-loss
                adoption = min(F(1), max(F(0), (g-error*fraud)/F(3, 10)))
                checked = adoption*v-(1-adoption)*error*loss-audit
                trusted = adoption*v-(1-adoption)*loss
                if 0 < adoption < 1 and checked > max(trusted, 0):
                    options.append((checked, effort_cost, adoption))
            return max(options)
        old = optimize(F(1, 10), F(1, 50))
        new = optimize(F(1, 20), F(3, 100))
        self.assertEqual(old, (F(2147, 16000), F(189, 800), F(33, 80)))
        self.assertEqual(new, (F(33121, 192000), F(399, 1600), F(209, 480)))
        self.assertGreater(new[0], old[0])
        self.assertGreater(new[2], old[2])
        self.assertGreater((1-new[2])*F(19, 20), (1-old[2])*F(9, 10))
        self.assertLess((1-new[2])*F(1, 20), (1-old[2])*F(1, 10))


class SeveralPartnerChecks(unittest.TestCase):
    def test_optional_installation_preserves_complementarity(self):
        nodes = range(4)
        pairs = list(combinations(nodes, 2))
        for edge_values, costs in (
                ((2, 2, 2, 2, 2, 2), (1, 1, 1, 1)),
                ((0, 1, 4, 0, 3, 2), (1, 5, 2, 3)),
                ((0, 0, 0, 0, 0, 0), (1, 2, 3, 4)),
                ((1, 7, 2, 6, 0, 5), (9, 1, 8, 2))):
            values = chosen_capacity_values(4, dict(zip(pairs, edge_values)), costs)
            for a, b in product(values, repeat=2):
                self.assertLessEqual(values[a]+values[b], values[a | b]+values[a & b])
            for order in permutations(nodes):
                before = frozenset()
                shares = {}
                for node in order:
                    after = before | {node}
                    shares[node] = values[after]-values[before]
                    before = after
                self.assertEqual(sum(shares.values()), values[frozenset(nodes)])
                for coalition in values:
                    self.assertGreaterEqual(sum(shares[i] for i in coalition), values[coalition])

    def test_three_partner_reusable_setup_example_and_sunk_costs(self):
        nodes = range(3)
        values = chosen_capacity_values(3, {edge: F(2) for edge in combinations(nodes, 2)}, [F(1)]*3)
        self.assertEqual(values[frozenset(nodes)], 3)
        self.assertTrue(all(values[s] == 0 for s in values if len(s) < 3))
        net, setup = F(1), F(1)
        self.assertGreater(2*(net+setup), 2)  # Two agents' continuation receipts vs pair output.
        self.assertGreater(2*net, 2-2*setup)  # Same comparison in net original welfare.

    def test_weighted_minimum_goal_bound_and_genuine_reversal(self):
        weights = [F(1, 5), F(3, 10), F(1, 2)]
        references = [F(-1), F(2), F(4)]
        target = F(5)
        for normalized in product(range(-2, 11), repeat=3):
            if sum(weights[i]*normalized[i] for i in range(3)) > target:
                continue
            for i in range(3):
                beta = 1-weights[i]/2
                score = references[i]+weights[i]*((1-beta)*normalized[i]+beta*min(normalized))
                self.assertLessEqual(score, references[i]+weights[i]*target)
        original_preferred = (F(2), F(1, 2), F(1, 2))
        changed_score = F(1, 4)*original_preferred[0]+F(3, 4)*min(original_preferred)
        self.assertEqual(changed_score, F(7, 8))
        self.assertGreater(original_preferred[0], 1)
        self.assertLess(changed_score, 1)

    def test_weight_boundary_and_profitable_group_expansion(self):
        weight, target, increase = F(1, 3), F(3), F(1)
        own = target+increase
        others = (target-weight*own)/(1-weight)
        for beta in (F(1, 2), F(2, 3), F(3, 4)):
            score = (1-beta)*own+beta*others
            self.assertEqual(score-target, increase*(1-beta/(1-weight)))
        old, new, newcomer = F(4), F(9), F(1, 3)
        self.assertGreater((1-newcomer)*new, old)
        self.assertEqual(F(1, 2)*(1-newcomer)*new, 3)
        self.assertEqual(newcomer*new, 3)

    def test_exclusive_three_agent_obstruction_and_fourth_partner_repair(self):
        # Three pair constraints sum to 6, but twice total production is 4.
        self.assertGreater(3*2, 2*2)
        for size in range(5):
            self.assertGreaterEqual(size, 2*(size//2))
        self.assertEqual(4, 2*(4//2))

    def test_ordinary_reputation_threshold_and_bilateral_goal_bound(self):
        b, c = F(3), F(1)
        for discount in (F(1, 4), F(1, 3), F(1, 2), F(9, 10)):
            self.assertEqual((b-c)/(1-discount) >= b, discount >= c/b)
        for own, other in product((F(k, 4) for k in range(-8, 25)), repeat=2):
            if own+other > 4:
                continue
            for beta in (F(1, 2), F(3, 4)):
                goal = own-F(1, 3)*max(other-own, 0)-beta*max(own-other, 0)
                self.assertLessEqual(goal, 2)


if __name__ == '__main__':
    unittest.main()
