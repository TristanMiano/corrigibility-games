"""Exact output and deviation checks for E7 notes 136 and 137.

Run: python -m unittest discover -s tests -p test_e7_repair_and_asymmetry.py -v
These checks supplement self-reviewed proofs; they are not formal verification.
"""

from fractions import Fraction as F
from itertools import product
import unittest


def counts(xb, xr, ab, ar, hbr, hrb, cb, cr, kb=0, kr=0, transfer=0):
    return (ab*xb+hbr*xr-cb*xb*xb/2-kb-transfer,
            ar*xr+hrb*xb-cr*xr*xr/2-kr+transfer)


class RepairAndAsymmetryChecks(unittest.TestCase):
    def test_asymmetric_frontier_from_actual_counts(self):
        for hbr, hrb, cb, cr, z in product(
                (F(1), F(4)), (F(1, 2), F(1)),
                (F(1), F(2)), (F(1), F(2)),
                (F(1, 2), F(1), F(2))):
            ab, ar, kb, kr = F(1), F(2), F(1, 4), F(1, 8)
            base = counts(ab/cb, ar/cr, ab, ar, hbr, hrb, cb, cr)
            goal = counts((ab+z*hrb)/cb, (ar+hbr/z)/cr,
                          ab, ar, hbr, hrb, cb, cr, kb, kr)
            x, y = hrb*hrb/cb, hbr*hbr/cr
            self.assertEqual(goal[0]-base[0], y/z-x*z*z/2-kb)
            self.assertEqual(goal[1]-base[1], x*z-y/(2*z*z)-kr)

    def test_negotiating_weights_repairs_equal_weight_refusal(self):
        # X=1,Y=8: z0=2; equal weights hurt Red before any update expense.
        base = counts(F(1), F(1), F(1), F(2), F(4), F(1), F(1), F(2))
        equal = counts(F(2), F(3), F(1), F(2), F(4), F(1), F(1), F(2))
        changed = counts(F(3), F(2), F(1), F(2), F(4), F(1), F(1), F(2),
                         F(1, 4), F(1, 8))
        self.assertEqual(equal[1]-base[1], -3)
        self.assertEqual(changed[0]-base[0], F(7, 4))
        self.assertEqual(changed[1]-base[1], F(7, 8))

    def test_bargaining_first_order_condition_and_frontier_slopes(self):
        for alpha in (F(1, 5), F(1, 3), F(1, 2), F(4, 5)):
            t = (2-alpha)/(1+alpha)
            derivative = (1-alpha)/(2*t-1)-alpha/(2-t)
            self.assertEqual(derivative, 0)
            self.assertGreater(t, F(1, 2))
            self.assertLess(t, 2)
        for u in (F(4, 5), F(1), F(5, 4)):
            fb_prime, fr_prime = -1/(u*u)-u, 1+1/(u*u*u)
            self.assertEqual(fr_prime/fb_prime, -1/u)

    def test_one_way_paid_service_has_real_positive_gains(self):
        base = counts(F(1), F(1), F(1), F(2), F(2), F(0), F(1), F(2))
        changed = counts(F(1), F(2), F(1), F(2), F(2), F(0), F(1), F(2),
                         F(1, 4), F(1, 8), F(3, 2))
        gains = tuple(a-b for a, b in zip(changed, base))
        self.assertEqual(gains, (F(1, 4), F(3, 8)))
        self.assertEqual(sum(gains), F(1)-F(1, 4)-F(1, 8))

    def test_repair_fee_and_early_honesty_are_both_chosen(self):
        v, k, miss, bill, repair = F(1), F(1, 8), F(1, 4), F(3, 16), F(3, 8)
        accepted = []
        for fee_units in range(-8, 9):
            fee = F(fee_units, 16)
            gc, gd = v/2-repair+fee, v/2-repair-fee
            if gc > 0 and gd > 0:
                accepted.append((gc, gd, fee))
        gc, gd, fee = max(accepted)
        self.assertEqual((gc, gd, fee), (F(3, 16), F(1, 16), F(1, 16)))
        self.assertEqual(gc-k, F(1, 16))  # founder gain includes the sunk first K
        truthful = v/2-k
        fake = miss*v+(1-miss)*gd
        self.assertEqual(fake, F(19, 64))
        self.assertGreater(truthful, fake)
        self.assertGreater(truthful, gd)  # open refusal and selected repair
        self.assertEqual(truthful-bill, F(3, 16))
        self.assertGreater(truthful-bill, v/2-repair)
        self.assertEqual(truthful-bill, v-2*repair-F(1, 16))

    def test_cheap_symmetric_second_chance_rewards_waiting_to_change(self):
        for miss, k in product((F(1, 8), F(1, 2)), (F(1, 16), F(1, 4))):
            v = F(1)
            truthful = v/2-k
            repair_rent = (v-2*k)/2
            self.assertEqual(repair_rent, truthful)
            self.assertGreater(miss*v+(1-miss)*repair_rent, truthful)

    def test_positive_repair_rent_threshold(self):
        v, k, repair = F(1), F(1, 8), F(3, 8)
        truthful, surplus = v/2-k, v-2*repair
        for miss in (F(1, 8), F(1, 4), F(1, 2)):
            room = (truthful-miss*v)/(1-miss)
            if room > 0:
                d = min(room, surplus)/2
                self.assertGreater(d, 0)
                self.assertGreater(surplus-d, 0)
                self.assertLess(miss*v+(1-miss)*d, truthful)
            else:
                for d in (F(1, 100), F(1, 8)):
                    self.assertGreater(miss*v+(1-miss)*d, truthful)

    def test_protected_finished_stock_requires_remaining_delivery_check(self):
        # A bound on NEW war production is insufficient after Blue finishes first.
        peace_b, delivered_b, new_war_total, win = F(10), F(10), F(1), F(1, 2)
        self.assertLess(new_war_total, peace_b)
        self.assertGreater(delivered_b+win*new_war_total, peace_b)
        # Full-site material exposure bounds old and new surviving clips together.
        material, recovered = F(30), F(1, 4)
        self.assertLess(material*recovered, peace_b)
        # Alternatively, paced delivery preserves a strict remaining bargain.
        for tau in (F(0), F(1, 4), F(3, 4)):
            self.assertLess(tau*peace_b+(1-tau)*F(9), peace_b)


if __name__ == '__main__':
    unittest.main()
