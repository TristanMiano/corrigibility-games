"""Exact adverse-lottery checks for note 031; run with unittest discovery.

On a full production frontier the constructed objective is piecewise affine.
Enumerating all breakpoints and every two-point lottery therefore solves each
one-constraint error LP independently of the derived closed forms. Under-
production is additionally sampled exactly; its general exclusion is proved
in the note by filling the color that is not the LP's objective.
"""
from fractions import Fraction as F
from itertools import combinations
import unittest


def lottery_extreme(points, allowance, maximize=False):
    values = [q for regret, q in points if regret <= allowance]
    for (e0, q0), (e1, q1) in combinations(points, 2):
        if e0 != e1 and min(e0, e1) <= allowance <= max(e0, e1):
            weight = (allowance-e0)/(e1-e0)
            values.append(q0+(q1-q0)*weight)
    return (max if maximize else min)(values)


def fixture(root_b, root_sr):
    b, s = root_b**2, 1-root_b**2
    r = root_sr**2/s
    t = root_sr/(root_b+root_sr)
    c = 1-t*s/r
    eta = min(s, b, (1-r)/2, c/(t/r+(1-t)/b))/4
    zeta = F(1, 100)
    def clip(x):
        return min(F(1), max(F(0), x))
    def raw(x, y):
        return t*min(x/r, 1)+c*clip((x-s+eta)/eta)*clip((y-b+eta)/eta)
    def goal(x, y):
        return (raw(x, y)+zeta*(x+y))/(1+zeta)
    return s, r, t, eta, zeta, raw, goal


CASES = ((F(1, 2), F(4, 5)),
         (F(4, 5), F(297, 500)),
         (F(3, 5), F(79, 100)))


class NonconcaveRobustnessTests(unittest.TestCase):
    def test_independent_frontier_lottery_lps_and_exact_failure(self):
        for root_b, root_sr in CASES:
            s, r, t, eta, zeta, raw, goal = fixture(root_b, root_sr)
            b, d = 1-s, 1-r
            eps_n = b*d/(root_b+root_sr)**2
            xs = sorted({F(0), s-eta, s, s+eta, r, F(1)})
            peace = [(x, 1-x) for x in xs]
            war = [(F(0), r), (r, F(0))]
            # Every affine frontier segment is represented by its endpoints.
            self.assertEqual(goal(s, b), 1)
            self.assertEqual(goal(0, 0), 0)
            for multiplier in (F(0), F(1, 3), F(9, 10), F(1), F(11, 10)):
                epsilon = multiplier*eps_n/(1+zeta)
                e = epsilon*(1+zeta)
                worst_a = lottery_extreme([(1-goal(x, y), x) for x, y in peace], epsilon)
                worst_b = lottery_extreme([(1-goal(x, y), y) for x, y in peace], epsilon)
                war_b = lottery_extreme([(goal(r, 0)-goal(x, y), y) for x, y in war], epsilon, True)
                self.assertEqual(worst_a, s*(1-e))
                self.assertEqual(worst_b, b*(1-e/(1-t)))
                self.assertEqual(war_b, r*e/t)
                gap = worst_b-(b*r+s*war_b)
                self.assertEqual(gap, b*d*(1-multiplier))
                if multiplier <= 1:
                    self.assertGreater(worst_a, s*r)
                    self.assertGreater(1-epsilon, s*goal(r, 0)+b*goal(0, r))

    def test_affine_certificates_include_underproduction(self):
        for root_b, root_sr in CASES:
            s, r, t, eta, zeta, raw, goal = fixture(root_b, root_sr)
            b = 1-s
            points = {(F(i, 20), F(j, 20)) for i in range(21) for j in range(21-i)}
            for da in (-eta, -eta/2, F(0), eta/2, eta):
                for db in (-eta, -eta/2, F(0), eta/2, eta):
                    if da+db <= 0:
                        points.add((s+da, b+db))
            for x, y in points:
                self.assertLessEqual(raw(x, y), x/s)
                self.assertLessEqual(raw(x, y), t+(1-t)*y/b)
                self.assertLessEqual(goal(x, y), 1)
                if (x, y) != (s, b):
                    self.assertLess(goal(x, y), 1)
            for i in range(21):
                for j in range(21-i):
                    x, y = r*F(i, 20), r*F(j, 20)
                    self.assertEqual(raw(x, y), t*x/r)
                    self.assertGreaterEqual((1+zeta)*(goal(r, 0)-goal(x, y)), t*y/r)

    def test_nonconcavity_is_substantive_and_constants_are_exact(self):
        for root_b, root_sr in CASES:
            s, r, t, eta, zeta, raw, goal = fixture(root_b, root_sr)
            # Concavity would require V(r*p) >= r*V(p)+(1-r)*V(0) = r.
            self.assertLess(goal(r*s, r*(1-s)), r)
        s, r, _, _, _, _, _ = fixture(*CASES[0])
        self.assertEqual((1-s)*(1-r)/(F(1, 2)+F(4, 5))**2, F(11, 507))
        self.assertEqual((1-r)**2/(1+F(4, 5))**2, F(121, 18225))

    def test_physical_stock_loss_defeats_exact_optimizers(self):
        s, r, t, eta, zeta, raw, goal = fixture(*CASES[0])
        y = 1-2*eta
        self.assertEqual(eta, F(11, 600))
        self.assertEqual(y, F(289, 300))
        self.assertGreater(y, r)
        self.assertLess(y-r, (1-s)*r)
        # On this full frontier the bonus is identically zero. Its entire
        # maximizer interval has A>=r, so even its largest B share fails.
        for j in range(101):
            x = y*F(j, 100)
            self.assertEqual(raw(x, y-x), t*min(x/r, 1))
        self.assertEqual(goal(r, y-r), goal(y, 0))
        # Independent serial physical bounds: O=y, B=1+2r, combat spends
        # one work unit and disperses O. Deadline/capacity bounds are slack.
        self.assertEqual(min(y, 1+2*r), y)
        self.assertEqual(min(y, (1+2*r-1)/2), r)


if __name__ == '__main__':
    unittest.main()
