"""Exact lottery-LP and numerical smoothing checks for note 023.

Finite LP extrema include underproduction and independently chosen peace/war
lotteries. The analytic proof, rather than these samples, establishes the
uniform result. Floating-point Hessians are checked at the calibrated target;
no assertion is made about representability of exponentially small weights.
"""
from fractions import Fraction as F
from math import exp, log
import unittest

from test_e2_robustness import triangle, one_constraint_lottery_extreme


def sharp_pieces(s, r, root):
    b, d = 1-s, 1-r
    gamma = d/(1+root)
    eta = root*gamma
    k, h, a = eta/(r*b), gamma/b, 1+eta/r
    def pieces(x, y):
        return (a*x+(a-k)*y, 1-gamma+h*y, x/s)
    return pieces, gamma, eta, k, h


def smooth_goal(s, r, root, allowance):
    pieces, gamma, _, k, _ = sharp_pieces(s, r, root)
    limit = gamma**2
    zeta = (limit-allowance)/20
    h = (gamma-zeta)/(1-s)
    wa, ww = h/(2*(h+1/s)), h/(2*(h+k))
    wb = 1-wa-ww
    weights = (ww, wb, wa)
    largest_log = log(1/min(weights))
    ratio = wb*h/(ww*k)
    tau = min(zeta/(2*log(2*ratio)), (limit-allowance)/(80*largest_log))
    def evaluate(x, y):
        raw = list(pieces(x, y))
        raw[1] = 1-gamma+zeta+h*y
        base = min(raw)
        terms = [weight*exp(-(value-base)/tau) for weight, value in zip(weights, raw)]
        total = sum(terms)
        return base-tau*log(total), tuple(term/total for term in terms)
    origin = evaluate(0., 0.)[0]
    def goal(x, y):
        return (evaluate(x, y)[0]-origin)/(1-origin)
    error = zeta+tau*largest_log/(1-tau*largest_log)
    return goal, evaluate, weights, k, h, tau, error


class SharpGoalChecks(unittest.TestCase):
    PARAMETERS = [(F(1, 2), F(49, 50), F(7, 10)),
                  (F(1, 4), F(81, 100), F(9, 20)),
                  (F(3, 4), F(64, 75), F(4, 5)),
                  (F(4, 5), F(4, 5), F(4, 5)),
                  (F(1, 10), F(961, 1000), F(31, 100))]

    def test_exact_independent_lottery_extrema(self):
        for s, r, root in self.PARAMETERS:
            pieces, gamma, eta, k, h = sharp_pieces(s, r, root)
            self.assertEqual(root**2, s*r)
            self.assertLessEqual(1-r, s*r)
            for multiplier in [F(1, 4), F(1, 2), F(1)]:
                allowance = multiplier*gamma**2
                peace_min_b = (s+allowance/h, 1-s-allowance/h)
                peace_min_a = (s*(1-allowance), 1-s*(1-allowance))
                war_max_b = (r-allowance/k, allowance/k)
                peace = triangle(F(1), 6)+[(s, 1-s), peace_min_b, peace_min_a]
                war = triangle(r, 6)+[(r, F(0)), (r*s, r*(1-s)), war_max_b]
                peace_b = [(1-min(pieces(x, y)), y) for x, y in peace]
                peace_a = [(1-min(pieces(x, y)), x) for x, y in peace]
                war_b = [(1-gamma-min(pieces(x, y)), y) for x, y in war]
                self.assertEqual(one_constraint_lottery_extreme(peace_b, allowance, False),
                                 1-s-allowance/h)
                self.assertEqual(one_constraint_lottery_extreme(peace_a, allowance, False),
                                 s*(1-allowance))
                self.assertEqual(one_constraint_lottery_extreme(war_b, allowance, True),
                                 allowance/k)
                deterrence = 1-s-allowance/h-((1-s)*r+s*allowance/k)
                self.assertEqual(deterrence, (1-s)*(1-r)*(1-multiplier))

    def test_omitting_founder_piece_can_break_adoption(self):
        s, r, root = self.PARAMETERS[-1]
        pieces, gamma, _, k, _ = sharp_pieces(s, r, root)
        allowance = gamma**2/2
        x = s-allowance/k
        y = 1-x
        self.assertGreater(x, 0)
        self.assertLess(x, s*r)
        self.assertEqual(1-min(pieces(x, y)[:2]), allowance)
        self.assertGreater(1-min(pieces(x, y)), allowance)

    def test_smoothing_preserves_optima_and_uniform_bound(self):
        for sf, rf, rootf in self.PARAMETERS:
            s, r, root = map(float, (sf, rf, rootf))
            pieces, gamma, _, _, _ = sharp_pieces(s, r, root)
            allowance = .8*gamma**2
            goal, evaluate, weights, k, h, tau, error = smooth_goal(s, r, root, allowance)
            self.assertLess(allowance+2*error, gamma**2)
            self.assertAlmostEqual(goal(0., 0.), 0.)
            self.assertAlmostEqual(goal(s, 1-s), 1.)
            target_weights = evaluate(s, 1-s)[1]
            target_slope = target_weights[0]*k-target_weights[1]*h+target_weights[2]/s
            self.assertAlmostEqual(target_slope, 0., places=10)
            war_weights = evaluate(r, 0.)[1]
            war_slope = -war_weights[0]*k+war_weights[1]*h-war_weights[2]/s
            self.assertLess(war_slope, 0.)
            for x, y in triangle(1., 20)+[(s, 1-s), (r, 0.)]:
                self.assertLessEqual(abs(goal(x, y)-min(pieces(x, y))), error+1e-12)
                self.assertLessEqual(goal(x, y), 1.+1e-12)
            for x, y in triangle(r, 20):
                self.assertLessEqual(goal(x, y), goal(r, 0.)+1e-12)

    def test_three_gradient_covariance_at_target_is_positive_definite(self):
        for sf, rf, rootf in self.PARAMETERS:
            s, r, root = map(float, (sf, rf, rootf))
            _, gamma, eta, _, _ = sharp_pieces(s, r, root)
            _, _, weights, k, h, _, _ = smooth_goal(s, r, root, .8*gamma**2)
            a = 1+eta/r
            gradients = [(a, a-k), (0., h), (1/s, 0.)]
            means = [sum(weight*g[j] for weight, g in zip(weights, gradients))
                     for j in [0, 1]]
            covariance = [[sum(weight*(g[i]-means[i])*(g[j]-means[j])
                               for weight, g in zip(weights, gradients))
                           for j in [0, 1]] for i in [0, 1]]
            self.assertGreater(covariance[0][0], 0.)
            self.assertGreater(covariance[0][0]*covariance[1][1]
                               -covariance[0][1]**2, 0.)


if __name__ == '__main__':
    unittest.main()
