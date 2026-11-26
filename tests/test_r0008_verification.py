"""Regression checks for the denominators, physical fallbacks and equilibrium feedback in E9."""

from fractions import Fraction as F
import unittest

from experiments.r0008_verification_boundaries import (
    COST_CEILING, FALSE_POSITIVE, SENSITIVITY, TEST_PRICE, market, outcome,
)
from experiments.r0008_sequential_evidence import Job, equilibrium_rates, threshold_rule


class CommissioningTests(unittest.TestCase):
    def test_exact_cases(self):
        central = outcome(F(1, 2), F(4, 5))
        self.assertEqual((central.attempt, central.changed, central.deliberate), (F(4, 5), F(16, 25), F(1, 5)))
        self.assertEqual((central.confidence, central.combat), (F(16, 17), 0))
        powerful = outcome(F(4, 5), F(4, 5))
        self.assertEqual((powerful.attempt, powerful.confidence, powerful.combat), (1, F(36, 37), F(13, 50)))
        weak = outcome(F(1, 20), F(4, 5))
        self.assertEqual(weak.changed, F(7, 107))
        self.assertEqual(outcome(F(1, 100), F(1)).combat, 1)
        self.assertIsNone(outcome(F(1, 100), F(1)).confidence)

    def test_strategies_optimize_against_each_other(self):
        for power_index in range(1, 40):
            power = F(power_index, 40)
            m = market(power)
            for skill_index in range(1, 21):
                q = F(skill_index, 20)
                o = outcome(power, q)
                if o.policy == "no trade":
                    self.assertEqual(o.changed, 0)
                    self.assertFalse(m.active_interval and q * min(1, q * m.red_edit_premium / COST_CEILING) >= m.lower_prior)
                    continue
                audit = o.changed * SENSITIVITY * m.blue_gain - (1 - o.changed) * FALSE_POSITIVE * m.blue_loss - TEST_PRICE
                trust = o.changed * m.blue_gain - (1 - o.changed) * m.blue_loss
                self.assertGreaterEqual(audit, max(0, trust))
                if o.test < 1:
                    self.assertEqual(audit, trust)
                premium = o.test * m.red_edit_premium - 2 * (1 - o.test)
                self.assertEqual(o.attempt, min(1, max(0, q * premium / COST_CEILING)))
                self.assertEqual(o.changed, q * o.attempt)
                self.assertGreaterEqual(1, o.release + o.combat)
                self.assertGreaterEqual(o.release, o.genuine_service)

    def test_reliability_changes_the_sample_receiving_the_order(self):
        before, after = (outcome(F(4, 5), q) for q in (F(17, 20), F(1)))
        self.assertEqual(before.changed, F(103, 126))
        self.assertEqual(after.changed, before.changed)
        self.assertGreater(after.deliberate, before.deliberate)
        self.assertGreater(after.genuine_service, before.genuine_service)
        self.assertLess(after.confidence, before.confidence)
        self.assertLess(after.combat, before.combat)

    def test_affordable_inspection_can_change_combat_in_either_direction(self):
        differences = []
        for q in (F(3, 5), F(4, 5)):
            original = outcome(F(1, 20), q)
            cheaper = outcome(F(1, 20), q, price=F(9, 100))
            self.assertEqual((original.changed, cheaper.changed), (F(7, 107), F(9, 107)))
            differences.append(cheaper.combat - original.combat)
        self.assertGreater(differences[0], 0)
        self.assertLess(differences[1], 0)

    def test_optimal_sequence_of_readings(self):
        job = Job()
        selected = threshold_rule(4, 2)
        rate = job.genuine_rate(selected)
        self.assertEqual((selected.accept_genuine, selected.accept_retained), (F(272, 273), F(17, 273)))
        self.assertEqual(rate, F(1088, 1365))
        self.assertIn(rate, equilibrium_rates(job))
