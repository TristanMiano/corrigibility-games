"""Exact LP checks for note 026 and calibrated merger checks for note 025.

The hostile-preference classification is compared with a separately specified
three-variable margin LP, including zero budgets, equality cases and bonuses.
Primal lottery vertices and dual envelope intersections are independent checks.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isqrt, sqrt
from random import Random
import unittest

from test_e2_population import solve_three


def max_third_coordinate(constraints):
    candidates = []
    for active in combinations(constraints, 3):
        point = solve_three(active)
        if point is not None and all(sum(a*x for a, x in zip(row[:3], point)) <= row[3]
                                     for row in constraints):
            candidates.append(point[2])
    return max(candidates)


def hostile_margin(alpha, beta, s, war, peace, bonus_a=F(0), bonus_b=F(0)):
    da = s*war-alpha*(1-s)*war+bonus_a
    db = (1-s)*war-beta*s*war+bonus_b
    constraints = [(-1, 0, 0, 0), (0, -1, 0, 0), (1, 1, 0, peace),
                   (-1, alpha, 1, -da), (beta, -1, 1, -db)]
    return max_third_coordinate(constraints)


def hostile_classification(alpha, beta, s, war, peace, ba=F(0), bb=F(0)):
    determinant = 1-alpha*beta
    da, db = s*war-alpha*(1-s)*war+ba, (1-s)*war-beta*s*war+bb
    if determinant > 0:
        threshold = war+((1+beta)*ba+(1+alpha)*bb)/determinant
        return peace > threshold
    if determinant == 0:
        return False
    return (da+alpha*db < 0 and beta*da+db < 0 and
            (peace > max(F(0), da, db) or (peace == 0 and da < 0 and db < 0)))


def three_route_primal(gains):
    # Variables p_0,p_1,z, with p_2=1-p_0-p_1.
    constraints = [(-1, 0, 0, 0), (0, -1, 0, 0), (1, 1, 0, 1)]
    for i in [0, 1]:
        constraints.append((gains[2][i]-gains[0][i],
                            gains[2][i]-gains[1][i], 1, gains[2][i]))
    return max_third_coordinate(constraints)


def two_agent_dual(gains):
    # Minimize the upper envelope of payoff lines in lambda_A in [0,1].
    points = [F(0), F(1)]
    for left, right in combinations(gains, 2):
        denominator = left[0]-left[1]-right[0]+right[1]
        if denominator:
            crossing = (right[1]-left[1])/denominator
            if 0 <= crossing <= 1:
                points.append(crossing)
    return min(max(lam*a+(1-lam)*b for a, b in gains) for lam in points)


def rational_sqrt(value):
    n, d = isqrt(value.numerator), isqrt(value.denominator)
    assert n*n == value.numerator and d*d == value.denominator
    return F(n, d)


def calibrated_power_merge(left, right):
    a, u = left
    b, v = right
    return a+b, ((a*rational_sqrt(u)+b*rational_sqrt(v))/(a+b))**2


class PreferenceFrontierChecks(unittest.TestCase):
    def test_hostility_and_bonus_cases_against_exact_margin_lp(self):
        # Covers all three determinant signs and participation equality cases.
        for alpha, beta, s, peace, ba, bb in product(
                [F(0), F(1, 2), F(1), F(2)],
                [F(0), F(1, 2), F(1), F(2)],
                [F(1, 4), F(1, 2), F(3, 4)],
                [F(0), F(1, 2), F(1), F(2), F(4)],
                [F(0), F(3, 5)], [F(0), F(3, 5)]):
            self.assertEqual(hostile_margin(alpha, beta, s, F(1), peace, ba, bb) > 0,
                             hostile_classification(alpha, beta, s, F(1), peace, ba, bb))

    def test_underproduction_and_combat_bonus_counterexamples(self):
        self.assertEqual(hostile_margin(F(2), F(2), F(1, 2), F(1), F(0)), F(1, 2))
        self.assertEqual(hostile_margin(F(2), F(2), F(1, 2), F(1), F(100),
                                        F(3, 5), F(3, 5)), -F(1, 10))
        self.assertEqual(hostile_margin(F(1), F(1), F(1, 2), F(1), F(100)), 0)

    def test_primal_dual_and_positive_rescaling(self):
        rng = Random(2601)
        for _ in range(60):
            gains = [(F(rng.randrange(-4, 5)), F(rng.randrange(-4, 5))) for _ in range(3)]
            primal = three_route_primal(gains)
            self.assertEqual(primal, two_agent_dual(gains))
            recoded = [(3*a, F(1, 7)*b) for a, b in gains]
            transformed = three_route_primal(recoded)
            self.assertEqual(primal > 0, transformed > 0)
            self.assertEqual(primal < 0, transformed < 0)

    def test_randomization_is_a_real_additional_capability(self):
        gains = [(F(2), -F(1)), (-F(1), F(2)), (-F(1), -F(1))]
        self.assertEqual(max(min(gain) for gain in gains), -1)
        self.assertEqual(three_route_primal(gains), F(1, 2))

    def test_affine_calibration_and_power_mean_grouping(self):
        leaves = [(F(1), F(1, 25)), (F(2), F(4, 25)), (F(3), F(9, 25))]
        left = calibrated_power_merge(calibrated_power_merge(leaves[0], leaves[1]), leaves[2])
        right = calibrated_power_merge(leaves[0], calibrated_power_merge(leaves[1], leaves[2]))
        flat = (sum(a*rational_sqrt(u) for a, u in leaves)/sum(a for a, _ in leaves))**2
        self.assertEqual(left, right)
        self.assertEqual(left, (F(6), flat))
        # Displayed utility recoding cancels only after restoring its calibration.
        canonical_left, canonical_right = F(2, 5), F(3, 7)
        ua, ub = 3*canonical_left+8, F(1, 2)*canonical_right-4
        decoded = (2*(ua-8)/3+5*(ub+4)/F(1, 2))/7
        self.assertEqual(decoded, (2*canonical_left+5*canonical_right)/7)

    def test_naive_recursive_rule_target_and_risk_difference(self):
        def collapsed(z):
            return 2**.75*z**.25+sqrt(1-z)
        best = max(range(2001), key=lambda j: collapsed(j/2000))
        self.assertEqual(best, 1000)
        self.assertGreater(collapsed(.5), collapsed(F(2, 3)))
        self.assertGreater(1., sqrt(2)/2)  # Additive square-root criterion.
        self.assertEqual(F(1, 2), F(1, 2)*1+F(1, 2)*0)  # Quantity-equivalent criterion.


if __name__ == '__main__':
    unittest.main()
