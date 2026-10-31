"""Checks for notes 014, 017 and 018.

Exact finite-distribution LPs test the quadratic error envelopes, including
underproduction and lotteries. Smooth-goal checks are numerical examples;
general optimization and equilibrium arguments remain mathematical proofs in
the notes, self-checked only. No external numerical package is required.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import exp, log1p, sqrt
import unittest


def quadratic_goal(p, w, s, rho=None):
    pa, pb = s*p, (1-s)*p
    if rho is None:
        rho = (p+w)/(2*p)
    zp = pa+rho*pb
    b = 2*p-(1-rho)*zp
    def raw(a, c):
        return 2*p*a+b*c-(a+rho*c)**2/2
    scale = raw(pa, pb)
    return (lambda a, c: raw(a, c)/scale), (1-rho)**2/scale, \
        (1-rho)*(zp-w)/scale


def triangle(budget, denominator=8):
    return [(budget*F(i, denominator), budget*F(j, denominator))
            for i in range(denominator+1) for j in range(denominator+1-i)]


def one_constraint_lottery_extreme(points, allowance, maximize):
    # (regret, quantity) points; a finite probability LP has an optimum
    # at one world, or a two-world mixture on the regret boundary.
    candidates = [value for regret, value in points if regret <= allowance]
    for (r0, x0), (r1, x1) in combinations(points, 2):
        if r0 != r1 and min(r0, r1) <= allowance <= max(r0, r1):
            weight = (allowance-r0)/(r1-r0)
            candidates.append((1-weight)*x0+weight*x1)
    return (max if maximize else min)(candidates)


def smooth_goal(p, w, s):
    pa, pb = s*p, (1-s)*p
    gap = p-w
    c = 1+2*pb/gap
    e = 2*pa-(2-c)*p
    tau = min(s, 1-s)*gap/16
    def raw(a, b):
        y = a+b
        l1, l2 = c*y+a, 2*y-a+e
        soft = min(l1, l2)-tau*log1p(exp(-abs(l1-l2)/tau))
        return soft-y*y/(8*p)
    origin = raw(0, 0)
    scale = raw(pa, pb)-origin
    return lambda a, b: (raw(a, b)-origin)/scale


def last_feasible(loss, limit, allowance):
    if loss(limit) <= allowance:
        return limit
    lower, upper = 0.0, limit
    for _ in range(70):
        middle = (lower+upper)/2
        if loss(middle) <= allowance:
            lower = middle
        else:
            upper = middle
    return lower


def markov_value(kernel, reward, discount):
    a = 1-discount*kernel[0][0]
    b = -discount*kernel[0][1]
    c = -discount*kernel[1][0]
    d = 1-discount*kernel[1][1]
    determinant = a*d-b*c
    return ((d*reward[0]-b*reward[1])/determinant,
            (a*reward[1]-c*reward[0])/determinant)


class GoalRobustnessTests(unittest.TestCase):
    def test_quadratic_error_envelopes_against_lottery_lps(self):
        for p, ratio, s in product((F(1), F(3)), (F(1, 4), F(2, 3), F(9, 10)),
                                   (F(1, 5), F(1, 2), F(4, 5))):
            w = ratio*p
            utility, curvature, margin = quadratic_goal(p, w, s)
            pa, pb = s*p, (1-s)*p
            peaceful_error = pb/4
            epsilon = curvature*peaceful_error**2/2
            worlds = triangle(p)+[(pa, pb), (pa+peaceful_error, pb-peaceful_error)]
            points = [(1-utility(a, b), b) for a, b in worlds]
            self.assertEqual(one_constraint_lottery_extreme(points, epsilon, False),
                             pb-peaceful_error)
            war_error = w/3
            epsilon_w = margin*war_error+curvature*war_error**2/2
            worlds_w = triangle(w)+[(w-war_error, war_error)]
            points_w = [(utility(w, 0)-utility(a, b), b) for a, b in worlds_w]
            self.assertEqual(one_constraint_lottery_extreme(points_w, epsilon_w, True),
                             war_error)
            self.assertEqual(one_constraint_lottery_extreme(points_w, F(0), True), 0)

    def test_quadratic_normalized_necessity_witness(self):
        for s, ratio in product((F(1, 10), F(1, 2), F(9, 10)),
                                (F(1, 2), F(9, 10), F(99, 100))):
            p, w = F(1), ratio
            utility, curvature, margin = quadratic_goal(p, w, s)
            pb = 1-s
            self.assertLessEqual(curvature, 2*(p-w)**2/(p*p*pb*pb))
            bad_b = (1-s)*w
            regret = 1-utility(p-bad_b, bad_b)
            self.assertGreaterEqual(regret, 0)
            self.assertLessEqual(regret, ((p-w)/p)**4)
            self.assertGreater(margin, 0)

    def test_quadratic_sufficient_certificate_has_strict_margins(self):
        for s, gap in product((F(1, 10), F(1, 2), F(9, 10)),
                              (F(1, 100), F(1, 20), F(1, 10))):
            p, w = F(1), 1-gap
            pa, pb = s, 1-s
            utility, curvature, margin = quadratic_goal(p, w, s, 1-gap/(2*pb))
            m = min(s, 1-s)
            epsilon = m*m/(64*(1-s)**2)*gap**4
            # Square the nonnegative quantities to retain exact arithmetic.
            self.assertLessEqual(2*epsilon/curvature, (m*gap/2)**2)
            self.assertLessEqual(epsilon/margin, m*gap/8)
            self.assertGreater(pa-m*gap/2, s*w)
            self.assertGreater(pb-m*gap/2, (1-s)*w+s*m*gap/8)
            self.assertGreater(1-utility(w, 0), epsilon)

    def test_smooth_goal_optima_and_adverse_error_boundaries(self):
        for p, s, gap_fraction in product((1.0, 3.0), (0.1, 0.5, 0.9),
                                          (0.01, 0.05, 0.1)):
            w = p*(1-gap_fraction)
            pa, pb = s*p, (1-s)*p
            utility = smooth_goal(p, w, s)
            epsilon = min(s, 1-s)/(64*(1-s))*gap_fraction**2
            self.assertAlmostEqual(utility(0, 0), 0)
            self.assertAlmostEqual(utility(pa, pb), 1)
            for j in range(101):
                self.assertLessEqual(utility(p*j/100, p*(1-j/100)), 1+1e-12)
                self.assertLessEqual(utility(w*j/100, w*(1-j/100)),
                                     utility(w, 0)+1e-12)
            za = last_feasible(lambda z: 1-utility(pa-z, pb+z), pa, epsilon)
            zb = last_feasible(lambda z: 1-utility(pa+z, pb-z), pb, epsilon)
            zw = last_feasible(lambda z: utility(w, 0)-utility(w-z, z), w, epsilon)
            self.assertGreater(pa-za, s*w)
            self.assertGreater(pb-zb, (1-s)*w+s*zw)
            self.assertGreater(1-epsilon, utility(w, 0))

    def test_smooth_hessian_at_target_is_strictly_negative(self):
        # At the target the soft-min weights are exactly 1/2. Check the
        # full Hessian directly with fractions, including the Y-square term.
        for p, s, gap in product((F(1), F(3)), (F(1, 10), F(1, 2), F(9, 10)),
                                 (F(1, 100), F(1, 20))):
            pb = (1-s)*p
            c = 1+2*pb/gap
            tau = min(s, 1-s)*gap/16
            h11 = -c*c/(4*tau)-1/(4*p)
            h22 = -(c-2)**2/(4*tau)-1/(4*p)
            h12 = -c*(c-2)/(4*tau)-1/(4*p)
            self.assertLess(h11, 0)
            self.assertEqual(h11*h22-h12*h12, 1/(4*p*tau))

    def test_general_concave_reservation_witness(self):
        for s in (0.1, 0.5, 0.9):
            p, w = 1.0, 0.95
            utility = smooth_goal(p, w, s)
            bad_b = (1-s)*w
            self.assertLessEqual(1-utility(p-bad_b, bad_b), (p-w)**2+1e-12)
            r, d = w/p, 1-w/p
            epsilon = d*d/(1+sqrt(s*r))**2
            gamma = 1-utility(w, 0)
            eta = utility(w, 0)-utility(r*s*p, r*(1-s)*p)
            t, theta = min(epsilon/gamma, 1), min(epsilon/eta, 1)
            self.assertGreaterEqual(t+s*r*theta, d-1e-12)


class ModelErrorTests(unittest.TestCase):
    def test_discounted_kernel_bound_against_exact_linear_solve(self):
        original = ((F(3, 4), F(1, 4)), (F(1, 3), F(2, 3)))
        perturbed = ((F(19, 25), F(6, 25)), (F(8, 25), F(17, 25)))
        reward = (F(1, 10), F(9, 10))
        other_reward = (F(11, 100), F(89, 100))
        error_r = max(abs(x-y) for x, y in zip(reward, other_reward))
        error_k = max(sum(abs(x-y) for x, y in zip(row, other))/2
                      for row, other in zip(original, perturbed))
        for discount in (F(1, 10), F(1, 2), F(9, 10), F(99, 100)):
            actual = markov_value(original, reward, discount)
            changed = markov_value(perturbed, other_reward, discount)
            bound = error_r/(1-discount)+discount*error_k/(1-discount)**2
            self.assertLessEqual(max(abs(x-y) for x, y in zip(actual, changed)), bound)

    def test_inactive_founder_evaluation_is_retained(self):
        outcomes = [(F(2), F(0)), (F(0), F(3))]
        successor_choice = max(outcomes, key=lambda x: x[1])
        continuation = {'original': successor_choice[0], 'successor': successor_choice[1]}
        self.assertGreater(F(1), continuation['original'])
        self.assertLess(F(1), continuation['successor'])
        # Using the successor coordinate in the initial comparison reverses it.


if __name__ == '__main__':
    unittest.main()
