"""Independent finite LP checks for notes 027/028.

Enumerating box vertices and intersections with the budget hyperplane checks
the stochastic allocation formula. Rational arithmetic checks the dated attack
and overlap examples. Continuous maximization and sensitivity checks support,
but do not replace, the analytical proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest

from test_e2_recovery_scheduling import serial_frontier


def knapsack_value(budgets, peace, war, strength, cap):
    rows = sorted(((1-strength*w/p, p*y) for y, p, w
                   in zip(budgets, peace, war) if p and p > strength*w),
                  reverse=True)
    remaining, value = cap, F(0)
    for rate, capacity in rows:
        take = min(capacity, remaining)
        value += rate*take
        remaining -= take
    return value


def allocation_vertices(budgets, peace, cap):
    """Vertices of a box cut by one halfspace, without sorting by the objective."""
    vertices = set()
    n = len(budgets)
    for mask in product((0, 1), repeat=n):
        x = tuple(flag*y for flag, y in zip(mask, budgets))
        if sum(p*m for p, m in zip(peace, x)) <= cap:
            vertices.add(x)
    for free in range(n):
        if not peace[free]:
            continue
        others = [j for j in range(n) if j != free]
        for mask in product((0, 1), repeat=n-1):
            x = [F(0)]*n
            for j, flag in zip(others, mask):
                x[j] = flag*budgets[j]
            x[free] = (cap-sum(p*m for p, m in zip(peace, x)))/peace[free]
            if 0 <= x[free] <= budgets[free]:
                vertices.add(tuple(x))
    return vertices


def quadratic_goal(x, y):
    return 2*x+F(61717, 32000)*y-(x+F(37, 40)*y)**2/2


def stochastic_schedule(y):
    if y <= F(1, 2):
        h, dh, d2h = F(3, 5), F(0), F(0)
    else:
        t, base, sign = (2*y-1, F(3, 5), 1) if y <= 1 else (2*y-2, F(1), -1)
        smooth = 6*t**5-15*t**4+10*t**3
        derivative = 30*t**2*(t-1)**2
        curvature = 60*t*(t-1)*(2*t-1)
        h = base+sign*F(2, 5)*smooth
        dh, d2h = sign*F(4, 5)*derivative, sign*F(8, 5)*curvature
    return y*h, h+y*dh, 2*dh+y*d2h


def stochastic_goal(x, y):
    total = x+y
    target, _, _ = stochastic_schedule(total)
    return 100*total-27*total**2-(x-target)**2


class StagingAndStochasticChecks(unittest.TestCase):
    def test_stochastic_frontier_against_all_lp_vertices(self):
        laws = [tuple(F(x, 4) for x in row) for row in
                [(4, 0, 0), (0, 4, 0), (0, 0, 4), (1, 1, 2),
                 (2, 1, 1), (1, 2, 1), (0, 2, 2), (2, 0, 2)]]
        budgets = (F(0), F(1, 2), F(3, 2))
        checked = 0
        for p, w, s in product(laws, laws, [F(1, 4), F(1, 2), F(3, 4)]):
            cap = sum(pj*y for pj, y in zip(p, budgets))-s*sum(wj*y for wj, y in zip(w, budgets))
            if cap <= 0:
                continue
            actual = max(sum((pj-s*wj)*mj for pj, wj, mj in zip(p, w, m))
                         for m in allocation_vertices(budgets, p, cap))
            self.assertEqual(knapsack_value(budgets, p, w, s, cap), actual)
            checked += 1
        self.assertGreater(checked, 100)

    def test_overlap_obstruction_and_strict_feasible_example(self):
        for theta in [F(7, 10), F(9, 10)]:
            s, p, w = F(1, 2), (F(0), F(1)), (1-theta, theta)
            cap = 1-s*theta
            result = knapsack_value((F(0), F(1)), p, w, s, cap)
            self.assertEqual(result, cap**2)
            self.assertEqual(result > (1-s)*theta, theta == F(7, 10))
        b, theta = F(3, 5), F(7, 10)
        self.assertGreater(1-b, theta/2)
        self.assertGreater(b-theta*b/2, theta/2)
        self.assertLess(F(1, 2)-theta/4, theta/2)  # proportional split fails

    def test_disjoint_support_restores_expected_surplus(self):
        budgets = (F(0), F(1, 2), F(1))
        p, w, s = (F(0), F(0), F(1)), (F(1, 4), F(3, 4), F(0)), F(2, 3)
        cap = 1-s*F(3, 8)
        self.assertEqual(knapsack_value(budgets, p, w, s, cap), cap)
        self.assertGreater(cap, (1-s)*F(3, 8))

    def test_physical_path_and_opposite_threat_maxima(self):
        for step in range(101):
            t = F(step, 100)
            actual = serial_frontier(F(0), F(1), F(8, 5)-t/10,
                                     9-t, F(1), F(1), F(1), F(1), F(1))
            self.assertEqual(actual, F(4, 5)-t/20)
            qa, qb = (1+2*t)/4, (3-2*t)/4
            self.assertLessEqual(qa*actual, F(9, 16))
            self.assertLessEqual(qb*actual, F(3, 5))
        self.assertGreater(F(9, 16)+F(3, 5), 1)

    def test_continuous_maximum_can_be_internal_or_at_a_frontier_knot(self):
        critical = sqrt(6)-2
        value = lambda t: (1+2*t)*(1-t/2)/(4+2*t)
        self.assertTrue(0 < critical < 1)
        self.assertGreater(value(critical), value(0))
        self.assertGreater(value(critical), value(1))
        self.assertAlmostEqual(4-8*critical-2*critical**2, 0., places=12)
        self.assertGreater(value(critical), value(critical-.01))
        self.assertGreater(value(critical), value(critical+.01))
        at_knot = F(5, 9)*F(39, 40)
        self.assertEqual(at_knot, F(13, 24))
        for j in range(101):
            t = F(j, 100)
            frontier = min(1-t/10, F(11, 10)-t/2)
            self.assertLessEqual((1+t)*frontier/(2+t), at_knot)

    def test_changed_current_goal_supports_the_declared_path(self):
        target = (F(7, 20), F(13, 20))
        self.assertGreater(target[0], F(17, 80))
        self.assertGreater(target[1], F(51, 80))
        peak = quadratic_goal(*target)
        rho, zp = F(37, 40), F(761, 800)
        self.assertEqual(target[0]+rho*target[1], zp)
        self.assertGreater(zp, F(17, 20))
        for j in range(101):
            t = F(j, 100)
            w, qa = F(4, 5)-t/20, (1+2*t)/4
            self.assertGreater(target[1], (1-qa)*w)
            self.assertGreater(peak, qa*quadratic_goal(w, 0)+(1-qa)*quadratic_goal(0, w))
        self.assertLess(target[0], F(9, 16))  # original A would attack late

    def test_limited_sensitivity_boundary(self):
        p, w, s = F(1), F(49, 50), F(1, 2)
        delta, cap = p-w, p-s*w
        threshold = (1-s)*(s*w-delta)/(s*delta)
        self.assertEqual(threshold, F(47, 2))
        for lip in [F(20), threshold, F(24)]:
            best = min(cap, (1-s)*cap+s*lip*delta)
            self.assertEqual(best > (1-s)*w, lip > threshold)
        # An explicit strict schedule just above the threshold.
        b, cw = F(509, 1000), F(29, 1000)
        self.assertLess(b, cap)
        self.assertGreater(b-s*cw, (1-s)*w)
        self.assertEqual((b-cw)/delta, 24)
        self.assertTrue(0 <= cw <= w and 0 <= b <= p)

    def test_average_deterrence_does_not_imply_conditional_deterrence(self):
        # Bad peaceful capacity is revealed while an intact combat route remains.
        chance_good, b_good, war = F(4, 5), F(1, 2), F(1, 2)
        self.assertGreater(chance_good*b_good, war/2)
        self.assertLess(F(0), war/2)

    def test_smooth_schedule_without_stochastic_dominance_and_signal_failure(self):
        # Peace: budgets 1/2 or 3/2, equally likely. A wins: 1. B wins: 1/2.
        self.assertEqual(stochastic_schedule(F(1, 2))[0], F(3, 10))
        self.assertEqual(stochastic_schedule(F(1))[0], F(1))
        self.assertEqual(stochastic_schedule(F(3, 2))[0], F(9, 10))
        peace = (stochastic_goal(F(3, 10), F(1, 5))
                 + stochastic_goal(F(9, 10), F(3, 5)))/2
        fight = (stochastic_goal(F(1), F(0))+stochastic_goal(F(0), F(1, 2)))/2
        self.assertEqual(peace, F(265, 4))
        self.assertEqual(fight, F(1452, 25))
        self.assertEqual(peace-fight, F(817, 100))
        self.assertGreater(F(3, 5), F(1, 2))  # founder A
        self.assertGreater(F(2, 5), F(1, 4))  # B, since m(1)=0
        self.assertLess(stochastic_goal(F(3, 10), F(1, 5)), fight)
        self.assertLess(F(1, 5), F(1, 4))  # both attack after the low signal
        for j in range(31):
            y = F(j, 20)
            target, slope, curvature = stochastic_schedule(y)
            self.assertTrue(0 <= target <= y)
            for portion in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
                x, d = portion*y, portion*y-target
                grad_b = 100-54*y+2*d*slope
                grad_a = 100-54*y+2*d*(slope-1)
                self.assertGreater(min(grad_a, grad_b), 0)
                self.assertLess(-54+2*d*curvature, 0)  # Hessian Schur complement
                self.assertEqual(stochastic_goal(target, y-target)-stochastic_goal(x, y-x), d*d)


if __name__ == '__main__':
    unittest.main()
