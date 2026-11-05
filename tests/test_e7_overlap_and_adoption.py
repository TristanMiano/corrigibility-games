"""Exact scientific checks for r0006 notes 112--121.

Run: python -m unittest discover -s tests -p test_e7_overlap_and_adoption.py -v
These check interior formulas against actual output/goal deviations and both
sides of the boundaries. They are not independent or machine-checked proofs.
"""

from fractions import Fraction as F
from itertools import product
import unittest


def outputs(x, y, s, rho=F(0), costs=(F(0), F(0)), q=F(20)):
    """Physical family, normalized a=c=1; expenses subtract clip production."""
    x, y, s, rho = map(F, (x, y, s, rho))
    return (q+x+rho*y+s*x*y-x*x/2-costs[0],
            q+y+rho*x+s*x*y-y*y/2-costs[1])


def efforts(beta, other, s, rho=F(0)):
    k, h = 1+beta, 1+other
    u, v = 1+rho*beta, 1+rho*other
    den = 1-s*s*k*h
    return ((u+s*k*v)/den, (v+s*h*u)/den)


def original_at(beta, other, s, rho=F(0), cost=F(0)):
    x, y = efforts(beta, other, s, rho)
    return outputs(x, y, s, rho, (cost if beta else 0, 0))[0]


def best_weight(other, s):
    k = 1+other
    return k*s*(1+s)/(1+k*s*(1-s))


def adoption_gain(k, s, rho):
    ell = rho*(1-s)+s
    return k*k*s*s*(1+s)**2*ell**2 / (
        2*(1-2*k*s*s)*(1-k*s*s)**2)


class ProductiveGoalChecks(unittest.TestCase):
    def test_continuation_best_responses(self):
        for s, rho, b, d in product(
                (F(-2, 5), F(-1, 5), F(0), F(1, 5), F(2, 5)),
                (F(0), F(1, 4), F(1)),
                (F(0), F(1, 3), F(1)),
                (F(0), F(2, 3), F(1))):
            x, y = efforts(b, d, s, rho)
            self.assertGreater(x, 0)
            self.assertGreater(y, 0)
            self.assertEqual(x, 1+rho*b+s*(1+b)*y)
            self.assertEqual(y, 1+rho*d+s*(1+d)*x)
            qb, qr = outputs(x, y, s, rho)
            for shift in (F(-1, 10), F(1, 10)):
                if x+shift >= 0:
                    alt = outputs(x+shift, y, s, rho)
                    self.assertLess(alt[0]+b*alt[1], qb+b*qr)

    def test_positive_complements_choose_weight_against_dense_deviation_grid(self):
        for s, rho, other in product(
                (F(1, 10), F(1, 4), F(2, 5)),
                (F(0), F(1, 2), F(1)),
                (F(0), F(1, 3), F(1))):
            best = best_weight(other, s)
            value = original_at(best, other, s, rho)
            for tick in range(41):
                self.assertGreaterEqual(value, original_at(F(tick, 40), other, s, rho))

    def test_additive_and_substitutable_retention_beats_all_positive_weights(self):
        for s, rho, other in product(
                (F(-2, 5), F(-1, 5), F(0)),
                (F(0), F(1, 4), F(1)),
                (F(0), F(1, 3), F(1))):
            ell = rho*(1-s)+s
            retained = original_at(0, other, s, rho)
            for tick in range(1, 21):
                actual = original_at(F(tick, 20), other, s, rho)
                if ell:
                    self.assertLess(actual, retained)
                else:
                    self.assertEqual(actual, retained)

    def test_cancelled_externality_leaves_efforts_unchanged(self):
        s, rho = F(-1, 3), F(1, 4)
        for b, d in product((F(0), F(1, 3), F(1)), repeat=2):
            self.assertEqual(efforts(b, d, s, rho), (F(3, 4), F(3, 4)))

    def test_adoption_gain_matches_direct_original_output_difference(self):
        for s, rho, other in product(
                (F(1, 10), F(1, 4), F(2, 5)),
                (F(0), F(1, 2), F(1)),
                (F(0), F(1, 3), F(1))):
            actual = original_at(best_weight(other, s), other, s, rho)
            actual -= original_at(0, other, s, rho)
            self.assertEqual(actual, adoption_gain(1+other, s, rho))

    def test_symmetric_weights_efforts_and_founder_gains(self):
        for s, rho in product((F(1, 10), F(1, 4), F(2, 5)),
                              (F(0), F(1, 2), F(1))):
            beta = s/(1-s)
            self.assertEqual(best_weight(beta, s), beta)
            x, y = efforts(beta, beta, s, rho)
            ordinary = 1/(1-s)
            efficient = (1+rho)/(1-2*s)
            self.assertEqual(x, y)
            self.assertEqual(x, ordinary+s*(efficient-ordinary))
            gain = outputs(x, y, s, rho)[0]-outputs(ordinary, ordinary, s, rho)[0]
            ell = rho*(1-s)+s
            full_gain = ell**2/(2*(1-2*s)*(1-s)**2)
            self.assertEqual(gain, s*(2-s)*full_gain)

    def test_cost_regions_include_coordination_and_retention(self):
        s, rho, beta = F(1, 4), F(0), F(1, 3)
        g0, gs = adoption_gain(1, s, rho), adoption_gain(1+beta, s, rho)
        self.assertEqual(g0, F(1, 252))
        self.assertEqual(gs, F(15, 1936))
        for cost, retain_eq, adopt_eq in (
                (F(1, 500), False, True),
                (F(1, 200), True, True),
                (F(1, 100), True, False)):
            self.assertEqual(original_at(0, 0, s) >=
                             original_at(best_weight(0, s), 0, s, cost=cost), retain_eq)
            self.assertEqual(original_at(beta, beta, s, cost=cost) >=
                             original_at(0, beta, s), adopt_eq)

    def test_common_package_can_pay_more_than_independent_stability_threshold(self):
        s, cost = F(1, 4), F(1, 50)
        retained = original_at(0, 0, s)
        common = original_at(1, 1, s, cost=cost)
        self.assertGreater(common, retained)
        self.assertGreater(cost, adoption_gain(F(4, 3), s, 0))

    def test_additive_negotiated_weights_against_actual_outputs(self):
        rho = F(1, 2)
        for z in (F(3, 4), F(1), F(4, 3)):
            x, y = 1+rho*z, 1+rho/z
            qb, qr = outputs(x, y, 0, rho)
            base = outputs(1, 1, 0, rho)[0]
            self.assertEqual(qb-base, rho*rho*(1/z-z*z/2))
            self.assertEqual(qr-base, rho*rho*(z-1/(2*z*z)))


class OrdinaryAndSmoothGoalChecks(unittest.TestCase):
    def test_temptation_and_trigger_threshold_both_sides(self):
        for s, rho in product((F(-1, 4), F(0), F(1, 4)),
                              (F(0), F(1, 2), F(1))):
            ell = rho*(1-s)+s
            if not ell:
                continue
            f, e = 1/(1-s), (1+rho)/(1-2*s)
            dev = 1+s*e
            nf = outputs(f, f, s, rho)[0]
            coop = outputs(e, e, s, rho)[0]
            cheat = outputs(dev, e, s, rho)[0]
            temptation = ell*ell/(2*(1-2*s)**2)
            self.assertEqual(cheat-coop, temptation)
            threshold = (1-s)**2/((1-s)**2+1-2*s)
            self.assertEqual(threshold, (cheat-coop)/(cheat-nf))
            for delta in (threshold-F(1, 100), threshold+F(1, 100)):
                self.assertEqual(coop/(1-delta) >= cheat+delta*nf/(1-delta),
                                 delta >= threshold)

    def test_balance_goal_reverses_founders_split_preference(self):
        eta = F(1, 100)
        h = lambda b, r: b+r-eta*(b-r)**2
        self.assertGreater(11, 10)
        self.assertLess(h(11, 9), h(10, 10))
        self.assertEqual(h(10, 10)-h(11, 9), 4*eta)

    def test_linear_blend_is_affine_on_a_fixed_total_frontier(self):
        beta, total = F(1, 3), F(20)
        for blue in range(21):
            self.assertEqual(blue+beta*(total-blue), (1-beta)*blue+beta*total)

    def test_actual_lottery_is_scored_before_expectation(self):
        eta = F(1, 100)
        h = lambda b, r: b+r-eta*(b-r)**2
        self.assertLess((h(12, 8)+h(8, 12))/2, h(10, 10))

    def test_chosen_standardization_fixture(self):
        kappa, rho0 = F(12), F(0)
        zf, zg = 1/kappa, 2*(1+rho0)/(kappa-4)
        rf, rg = rho0+2*zf, rho0+2*zg
        ordinary = outputs(1, 1, 0, rf)[0]-kappa*zf*zf/2
        changed = outputs(1+rg, 1+rg, 0, rg)[0]-kappa*zg*zg/2
        self.assertEqual((rf, rg), (F(1, 6), F(1, 2)))
        self.assertEqual(ordinary, 20+F(5, 8))
        self.assertEqual(changed, 20+F(3, 4))
        self.assertEqual(changed-ordinary, F(1, 8))
        # Check selected common design against actual nearby joint designs.
        def total(z, w, x, y):
            b, r = outputs(x, y, 0, rho0+z+w)
            return b+r-kappa*(z*z+w*w)/2
        target = total(zg, zg, 1+rg, 1+rg)
        for z, w, x, y in product((F(1, 5), F(1, 4), F(3, 10)),
                                  (F(1, 5), F(1, 4), F(3, 10)),
                                  (F(7, 5), F(3, 2), F(8, 5)),
                                  (F(7, 5), F(3, 2), F(8, 5))):
            self.assertGreaterEqual(target, total(z, w, x, y))


class CaptureAndSetupChecks(unittest.TestCase):
    def test_setup_threshold_and_binding_capacity(self):
        for theta in (F(0), F(1, 4), F(1, 2), F(1)):
            total = 24-(2-theta)*4-1
            self.assertEqual(total > 16, theta > F(1, 4))
            self.assertLess(min(15, total), 16)

    def test_capture_margin_and_cost_threshold(self):
        for rb, rr, p, damage, cross in product(
                (F(3), F(5)), (F(4), F(5)),
                (F(1, 5), F(1, 2), F(4, 5)),
                (F(4, 5), F(9, 10), F(1)),
                (F(0), F(1, 3), F(1))):
            db, dr = p*damage*(rb+cross*rr), (1-p)*damage*(rr+cross*rb)
            mb, mr = rb+cross*rr-db-cross*dr, rr+cross*rb-dr-cross*db
            g = min(mb, mr)/(1+cross)
            self.assertGreaterEqual(g, 0)
            if damage < 1:
                self.assertGreater(g, 0)
            self.assertLessEqual(db+g+cross*(dr+g), rb+cross*rr)
            self.assertLessEqual(cross*(db+g)+dr+g, cross*rb+rr)
            eps = F(1, 1000)
            self.assertTrue(db+g+eps+cross*(dr+g+eps) > rb+cross*rr or
                            cross*(db+g+eps)+dr+g+eps > cross*rb+rr)
            if rb == rr:
                self.assertEqual(g, rb*((1-damage)+damage*(1-cross)*min(p, 1-p)))

    def test_costly_route_and_cheaper_repair(self):
        rb, rr, p, damage, cross = F(5), F(5), F(4, 5), F(9, 10), F(1)
        db, dr = p*damage*(rb+cross*rr), (1-p)*damage*(rr+cross*rb)
        self.assertEqual((db, dr), (F(36, 5), F(9, 5)))
        self.assertGreater(db, rb)
        self.assertGreater(rb+rr-2*F(1, 4), db+dr)
        self.assertLess(rb+rr-2*F(3, 4), db+dr)

    def test_joint_overlap_path_thresholds(self):
        def prize(z):
            return F(99, 100)*12*(1+z)-4-F(1, 2)
        def peaceful(z, expense=F(1)):
            return 24-(2-z)*4-expense
        attack_at, margin_at = F(131, 594), F(381, 394)
        self.assertEqual(F(4, 5)*prize(attack_at), 8)
        self.assertEqual(prize(margin_at), peaceful(margin_at))
        self.assertLess(peaceful(1), prize(1))
        self.assertEqual(peaceful(1, F(2, 5))-prize(1), F(17, 50))


if __name__ == '__main__':
    unittest.main()
