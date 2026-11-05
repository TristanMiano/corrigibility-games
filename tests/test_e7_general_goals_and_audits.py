"""Exact checks for the general-goal example and imperfect-audit game.

Run: python -m unittest discover -s tests -p test_e7_general_goals_and_audits.py -v
"""

from fractions import Fraction as F
from itertools import product
import unittest

from test_e7_overlap_and_adoption import outputs


def audit_table(v, cost, miss):
    return ((v/2-cost, -miss*v/2-cost, -cost),
            (miss*v, F(0), F(0)),
            (F(0), F(0), F(0)))


class GeneralGoalAndAuditChecks(unittest.TestCase):
    def test_audit_payoffs_come_from_real_production(self):
        for rho, cost, miss in product((F(1, 2), F(1)),
                                       (F(1, 16), F(1, 8)),
                                       (F(1, 4), F(1, 2), F(1))):
            baseline = outputs(F(1), F(1), F(0), rho)[0]
            common = outputs(1+rho, 1+rho, F(0), rho, (cost, cost))[0]
            fooled = outputs(1+rho, F(1), F(0), rho, (cost, 0))[0]
            fake = outputs(F(1), 1+rho, F(0), rho, (0, cost))[0]
            table = audit_table(rho*rho, cost, miss)
            self.assertEqual(common-baseline, table[0][0])
            self.assertEqual(miss*(fooled-baseline)+(1-miss)*(-cost), table[0][1])
            self.assertEqual(miss*(fake-baseline), table[1][0])

    def test_mutual_adoption_and_low_audit_dominance(self):
        for v, cost, miss in product((F(1, 4), F(1, 2), F(1)),
                                     (F(1, 16), F(1, 8)),
                                     (F(1, 8), F(1, 4), F(1, 2), F(1))):
            table = audit_table(v, cost, miss)
            strict = table[0][0] > max(table[1][0], table[2][0])
            self.assertEqual(strict, cost < v*(F(1, 2)-miss))
            if cost > v*(F(1, 2)-miss):
                for column in range(3):
                    self.assertGreater(table[1][column], table[0][column])

    def test_paid_integer_audit_threshold(self):
        cost, message, inspection = F(1, 8), F(1, 16), F(1, 16)
        for tick in range(65):
            v = F(tick, 64)
            routes = []
            for level in range(17):
                miss = F(1, 2)**level
                table = audit_table(v, cost, miss)
                if table[0][0] > table[1][0] and table[0][0] > 0:
                    net = table[0][0]-message-level*inspection
                    if net > 0:
                        routes.append((net, level))
            self.assertEqual(bool(routes), v > F(5, 8))
            if routes:
                self.assertEqual(max(routes)[1], 2)

    def test_mixed_selection_can_prevent_funding(self):
        v, cost, miss = F(1), F(1, 8), F(1, 4)
        probability = (miss+2*cost/v)/(1-miss)
        table = audit_table(v, cost, miss)
        cooperate = probability*table[0][0]+(1-probability)*table[0][1]
        deceive = probability*table[1][0]+(1-probability)*table[1][1]
        self.assertEqual(probability, F(2, 3))
        self.assertEqual(cooperate, deceive)
        self.assertGreater(cooperate, 0)
        self.assertEqual(cooperate-F(3, 16), F(-1, 48))
        self.assertEqual(table[0][0]-F(3, 16), F(3, 16))

    def test_false_rejection_includes_wasted_updates(self):
        v, cost, miss, rejection = F(1), F(1, 8), F(1, 4), F(1, 10)
        true_ready = (1-rejection)**2
        fake_ready = miss*(1-rejection)
        honest = true_ready*(v/2-cost)+(1-true_ready)*(-cost)
        fake = fake_ready*v
        self.assertEqual(honest-fake,
                         v*((1-rejection)**2/2-miss*(1-rejection))-cost)

    def test_asymmetric_common_goal_and_strict_preference_changes(self):
        weights = (F(1), F(11, 10), F(9, 10))
        chosen = (F(3), F(30, 11), F(10, 3))
        counts = lambda effort: tuple(20+sum(effort)-x*x/2-F(1, 10)
                                       for x in effort)
        target = counts(chosen)
        baseline = F(45, 2)
        self.assertEqual(min(x-baseline for x in target), F(448, 495))
        def goal(q):
            return sum(w*x-F(1, 1000)*(x-y)**2
                       for w, x, y in zip(weights, q, target))
        maximum = goal(target)
        for effort in product((F(i, 2) for i in range(11)), repeat=3):
            self.assertLessEqual(goal(counts(effort)), maximum)
        for i in range(3):
            altered = list(chosen)
            altered[i] -= F(1, 10)
            outcome = counts(altered)
            self.assertGreater(outcome[i], target[i])
            self.assertLess(goal(outcome), maximum)
            # Independent final idling changes an old indifference as well.
            omitted = list(target)
            omitted[(i+1) % 3] -= F(1, 10)
            self.assertEqual(omitted[i], target[i])
            self.assertLess(goal(omitted), maximum)


if __name__ == '__main__':
    unittest.main()
