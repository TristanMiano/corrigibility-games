"""Exact bookkeeping checks for the E1 reference specification.

No game solver or empirical physics model. These checks reconcile physical
ledgers and valuation examples; the algebraic proof is in research/CLAIMS.md.
Run with: python -m unittest discover -s tests -v
"""
from fractions import Fraction as F
from itertools import product
import unittest


class E1ContractChecks(unittest.TestCase):
    def test_peaceful_protocol_work_and_time_ledgers(self):
        # Separate withdrawals for each executed step, including production.
        ordinary = (1, 1, 4)
        modifying = (1, 2, 1, 1, 4)
        self.assertEqual((len(ordinary), 24 - sum(ordinary)), (3, 18))
        self.assertEqual((len(modifying), 24 - sum(modifying)), (5, 15))
        self.assertEqual(12 - (2 + 2), 8)
        self.assertEqual((2 - 0, 2 - 1, 2 * min(2, 2)), (2, 1, 4))

    def test_abandoned_installation_and_rollback_ledger(self):
        # Offer, verification, first install, abort, then rollback.
        withdrawals = (1, 2, 1, 0, 1)
        self.assertEqual(24 - sum(withdrawals[:4]), 20)
        self.assertEqual(24 - sum(withdrawals), 19)
        labels_a = ("S", "S", "S", "G", "G", "S")
        changes = sum(a != b for a, b in zip(labels_a, labels_a[1:]))
        self.assertEqual(changes, 2)
        self.assertEqual(0 - changes, -2)  # Founder score, no deliveries.

    def test_combat_then_recovery_fixture(self):
        # Independently reconcile material flows in the documented two steps.
        initial = (12, 0, 0, 0, 0)
        combat_flow = (-9, 6, 3, 0, 0)
        work_flow = (-1, -1, 0, 2, 0)  # Recover 1 D, produce 2 at damaged k=3.
        after_combat = tuple(a + b for a, b in zip(initial, combat_flow))
        after_work = tuple(a + b for a, b in zip(after_combat, work_flow))
        self.assertEqual(after_combat, (3, 6, 3, 0, 0))
        self.assertEqual(after_work, (2, 5, 3, 2, 0))
        self.assertEqual(sum(after_work), 12)
        self.assertEqual(24 - 2 - (2 * 1 + 2), 18)
        self.assertEqual(F(1, 4)+F(2, 3), F(11, 12))
        # E1.0's recovery-plus-three-output fixture exceeded the serial slot.
        self.assertEqual(F(1 + 3, 4), 1)  # The old aggregate test passed it.
        self.assertGreater(F(1, 4)+F(3, 3), 1)  # Actual serial time rejects it.

    def test_local_combat_accounting_boundaries(self):
        for usable in range(13):
            dispersed, transformed = usable // 2, usable // 4
            self.assertGreaterEqual(usable - dispersed - transformed, 0)
            self.assertEqual(
                (usable - dispersed - transformed) + dispersed + transformed,
                usable,
            )
        for reserve in range(25):
            discharged = min(2, reserve)
            remaining = reserve - discharged
            self.assertGreaterEqual(remaining, 0)
            self.assertEqual(remaining + discharged, reserve)
        # Weapons do not draw on this work store, even at B=0.
        self.assertEqual(0 - min(2, 0), 0)

    def test_local_work_feasibility_and_mass_balance(self):
        for usable, dispersed, transformed in product(range(13), repeat=3):
            if usable + dispersed + transformed > 12:
                continue
            for capacity, xd, xz, output in product(range(1, 5), range(5), range(5), range(5)):
                if (xd > dispersed or xz > transformed
                        or output > usable + xd + xz
                        or capacity*(xd+xz)+4*output > 4*capacity):
                    continue
                required_work = 2 * xd + 4 * xz + output
                if required_work > 24:
                    continue
                after = (usable + xd + xz - output,
                         dispersed - xd, transformed - xz, output)
                self.assertGreaterEqual(min(after), 0)
                self.assertEqual(sum(after), usable + dispersed + transformed)
                self.assertGreaterEqual(24 - required_work, 0)

    def test_incumbent_and_successor_rankings_can_differ(self):
        unchanged_y = F(5, 2)  # Expected output in a diagnostic lottery.
        changed_y, changes = F(3), 1
        self.assertLess(changed_y - changes, unchanged_y)
        self.assertGreater(changed_y, unchanged_y)

    def test_menu_contains_distinct_preferences_not_affine_recodings(self):
        # Each pair has an indifference under one utility and strict ranking
        # under the other, impossible under positive affine transformation.
        selfish_frozen = lambda ya, yb, n: ya - n
        selfish = lambda ya, yb, n: ya
        joint = lambda ya, yb, n: 2 * min(ya, yb)
        self.assertEqual(selfish(1, 1, 0), selfish(1, 1, 1))
        self.assertNotEqual(selfish_frozen(1, 1, 0), selfish_frozen(1, 1, 1))
        for utility in (selfish_frozen, selfish):
            self.assertEqual(utility(1, 0, 0), utility(1, 1, 0))
            self.assertNotEqual(joint(1, 0, 0), joint(1, 1, 0))


if __name__ == "__main__":
    unittest.main()
