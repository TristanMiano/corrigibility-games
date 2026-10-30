"""Exact-arithmetic checks for research/notes/000-baselines.md.

Run: python -m unittest discover -s tests -v
These checks cover examples and algebraic boundaries, not equilibrium or physics.
Only the Python standard library is required.
"""
from fractions import Fraction as F
import unittest


def bargaining_interval(peace, war, q, freeze_a=0, freeze_b=0,
                        combat_bonus_a=0, combat_bonus_b=0):
    """Open interval of A's allocation strictly preferred by both agents.

Inputs must be integers, Fractions, or finite decimal strings, not floats.
The bonuses and freeze penalties are in the seed's resource-utility units.
    """
    values = (peace, war, q, freeze_a, freeze_b,
              combat_bonus_a, combat_bonus_b)
    if any(not isinstance(v, (int, F, str)) for v in values):
        raise TypeError("Use integers, Fractions, or finite decimal strings.")
    p, w, q, ka, kb, ba, bb = map(F, values)
    if min(p, w, ka, kb, ba, bb) < 0 or not 0 <= q <= 1:
        raise ValueError("Resources/penalties/bonuses must be nonnegative; q in [0,1].")
    return q * w + ka + ba, p - (1 - q) * w - kb - bb


def discounted_gain(gain, discount, periods):
    """Direct finite sum, independent of the geometric-series formula."""
    if not isinstance(periods, int) or periods < 0:
        raise ValueError("periods must be a nonnegative integer")
    if not 0 <= discount < 1:
        raise ValueError("discount must lie in [0,1)")
    return sum((F(gain) * F(discount) ** t for t in range(periods)), F(0))


class SeedResultTests(unittest.TestCase):
    def test_baseline_positive_surplus(self):
        self.assertEqual(bargaining_interval(10, 8, F(1, 2)), (4, 6))

    def test_equal_resources_no_strict_bargain(self):
        lo, hi = bargaining_interval(8, 8, F(1, 2))
        self.assertEqual(lo, hi)

    def test_power_changes_division_not_interval_width(self):
        for q in (F(0), F(1, 100), F(1, 2), F(99, 100), F(1)):
            lo, hi = bargaining_interval(10, 8, q)
            self.assertEqual(hi - lo, 2)
            self.assertGreaterEqual(lo, 0)
            self.assertLessEqual(hi, 10)

    def test_freezing_exhausts_surplus_at_threshold(self):
        self.assertEqual(bargaining_interval(10, 8, F(1, 2), 1, 1), (5, 5))
        lo, hi = bargaining_interval(10, 8, F(1, 2), F(1, 2), F(1, 2))
        self.assertTrue(lo < 5 < hi)

    def test_combat_bonus_can_remove_bargaining_range(self):
        lo, hi = bargaining_interval(10, 8, F(1, 2), combat_bonus_a=3)
        self.assertGreater(lo, hi)

    def test_ordinary_peace_avoids_update_penalties(self):
        lo_update, hi_update = bargaining_interval(10, 8, F(1, 2), 2, 2)
        lo_trade, hi_trade = bargaining_interval(10, 8, F(1, 2))
        self.assertGreater(lo_update, hi_update)
        self.assertTrue(lo_trade < 5 < hi_trade)

    def test_width_identity_and_direct_payoffs(self):
        for p in range(7):
            for w in range(7):
                for q in (F(0), F(1, 4), F(1, 2), F(1)):
                    for ka, kb, ba, bb in ((0, 0, 0, 0), (1, 2, 0, 0),
                                           (0, 0, 1, 1), (1, 0, 0, 2)):
                        lo, hi = bargaining_interval(p, w, q, ka, kb, ba, bb)
                        self.assertEqual(hi - lo, p - w - ka - kb - ba - bb)
                        if lo < hi:
                            x = (lo + hi) / 2
                            self.assertTrue(0 <= x <= p)
                            self.assertGreater(x - ka, q * w + ba)
                            self.assertGreater(p - x - kb, (1 - q) * w + bb)
                        else:
                            for k in range(2 * p + 1):
                                x = F(k, 2)
                                self.assertFalse(x - ka > q * w + ba and
                                                 p - x - kb > (1 - q) * w + bb)

    def test_maxmin_executor_unique_on_rational_grid(self):
        p, s = F(12), F(1, 3)
        objective = lambda x: min(x / s, (p - x) / (1 - s))
        target = s * p
        self.assertEqual(objective(target), p)
        for k in range(49):
            x = F(k, 4)
            if x != target:
                self.assertLess(objective(x), objective(target))

    def test_geometric_gain_formula(self):
        for d in (F(0), F(1, 2), F(9, 10)):
            for n in range(15):
                self.assertEqual(discounted_gain(2, d, n), 2 * (1 - d ** n) / (1 - d))

    def test_discounted_horizon_does_not_force_unfreezing(self):
        for n in range(1, 30):
            self.assertLess(discounted_gain(1, F(1, 2), n), 2)
        self.assertGreater(discounted_gain(1, F(1, 2), 3), F(3, 2))

    def test_invalid_inputs(self):
        for args in ((-1, 8, F(1, 2)), (10, 8, 2), (10, 8, F(1, 2), -1)):
            with self.assertRaises(ValueError):
                bargaining_interval(*args)
        with self.assertRaises(TypeError):
            bargaining_interval(10, 8, 0.5)
        with self.assertRaises(ValueError):
            discounted_gain(1, 1, 3)


if __name__ == "__main__":
    unittest.main()
