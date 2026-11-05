"""Scientific checks for notes 127--133; exact where the model permits.

Run: python -m unittest discover -s tests -p test_e7_horizons_and_implementation.py -v
Floating-point CES/defense checks are numerical audits, not proof certificates.
"""

from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest

from test_e7_overlap_and_adoption import outputs


def horizon_gain(duration, rho):
    original = min(duration, F(1))
    common = min(duration*(1+rho), F(1))
    value = lambda x: duration*(1+rho)*x-x*x/2
    return value(common)-value(original)


def investment_value(alpha, k, overhead, p=F(4, 5), delta=F(9, 10)):
    blue = 1-k*alpha
    war_blue = p*delta*(blue+alpha)
    war_red = (1-p)*delta*(blue+1)
    value = max(blue, war_blue)
    if war_blue > blue and overhead <= blue:
        offer = blue-overhead+alpha*(1-war_red)
        value = max(value, offer)
    return value


def defense_threshold(c, p=.8, delta=.99, resource=1.):
    z = c/resource
    h = 1/(p*delta)-1
    # Rationalized form avoids cancellation at small cost.
    return 2*(1-h)/(1+z+sqrt((1-z)**2+4*z*h))


def public_club_output(n, size, power_ratio, member, cost=F(0)):
    """rho=a=c=1, nu=r/(r-1); evaluate actual counts at known efforts."""
    r = power_ratio
    nu = F(r, r-1)
    effort = F(size**(r-1)) if member else F(1)
    research_cost = F(size**r)/nu if member else 1/nu
    aggregate = F(size*size**(r-1)+n-size)
    return 100000+aggregate-research_cost-(cost if member else 0)


def ces(x, y, r):
    if min(x, y) == 0 and r <= 0:
        return 0.
    if r == 0:
        return sqrt(x*y)
    return ((x**r+y**r)/2)**(1/r)


def ces_efforts(beta, other, r):
    k, h = 1+beta, 1+other
    z = (k/h)**(1/(2-r))
    g = sqrt(z) if r == 0 else ((1+z**r)/2)**(1/r)
    y = h*g/(1+z**r)
    return z*y, y


def ces_output(beta, other, r):
    x, y = ces_efforts(beta, other, r)
    return ces(x, y, r)-x*x/2


class HorizonAndEntryChecks(unittest.TestCase):
    def test_horizon_pieces_against_direct_output(self):
        for duration, rho in product((F(i, 24) for i in range(49)),
                                     (F(0), F(1, 4), F(1, 2), F(1))):
            if duration <= 1/(1+rho):
                claimed = rho*rho*duration*duration/2
            elif duration <= 1:
                claimed = (1-duration)*((1+2*rho)*duration-1)/2
            else:
                claimed = F(0)
            self.assertEqual(horizon_gain(duration, rho), claimed)

    def test_horizon_cost_interval_and_peak(self):
        self.assertEqual(horizon_gain(F(1, 2), F(1)), F(1, 8))
        self.assertEqual(horizon_gain(F(5, 6), F(1)), F(1, 8))
        self.assertEqual(horizon_gain(F(2, 3), F(1)), F(1, 6))
        for i in range(37):
            duration = F(i, 36)
            self.assertEqual(horizon_gain(duration, F(1)) > F(1, 8),
                             F(1, 2) < duration < F(5, 6))

    def test_paid_expandable_capacity_includes_construction(self):
        for duration, rho, kappa in product((F(1), F(3)),
                                           (F(1, 4), F(1)),
                                           (F(1, 2), F(2))):
            original = duration/(1+kappa)
            common = duration*(1+rho)/(1+kappa)
            value = lambda x: duration*(1+rho)*x-(1+kappa)*x*x/2
            self.assertEqual(value(common)-value(original),
                             (duration*rho)**2/(2*(1+kappa)))

    def test_entry_reservation_rejects_a_harmful_counteroffer(self):
        target, eta, epsilon = F(175, 8), F(1, 100), F(1, 10000)
        score = lambda b, r: b+r-eta*(b-r)**2
        reservation = 2*target-epsilon
        self.assertGreater(score(target, target), reservation)
        self.assertLess(score(target-F(1, 5), target+F(1, 5)), reservation)
        loss_bound = float(epsilon)/2+sqrt(float(epsilon/eta))/2
        self.assertLess(loss_bound, 3/8)

    def test_expected_common_score_controls_original_counts(self):
        target, eta = F(10), F(1, 100)
        for left, right, probability in product(
                ((F(10), F(10)), (F(19, 2), F(21, 2)), (F(9), F(10))),
                ((F(10), F(10)), (F(11), F(9))),
                (F(1, 4), F(1, 2), F(3, 4))):
            score = lambda q: sum(q)-eta*(q[0]-q[1])**2
            gap = 2*target-probability*score(left)-(1-probability)*score(right)
            loss = float(gap)/2+sqrt(float(gap/eta))/2
            for i in range(2):
                count = probability*left[i]+(1-probability)*right[i]
                self.assertGreaterEqual(float(count)+1e-12, float(target)-loss)


class CaptureAndDefenseChecks(unittest.TestCase):
    def test_investment_endpoint_solution_against_complete_grid(self):
        for k, overhead in product((F(1, 10), F(1, 2), F(9, 10)),
                                   (F(1, 100), F(1, 10), F(1, 2), F(1))):
            endpoint = max(F(1), investment_value(F(1), k, overhead))
            for tick in range(101):
                self.assertLessEqual(investment_value(F(tick, 100), k, overhead),
                                     endpoint)

    def test_capture_investment_war_and_agreement_fixtures(self):
        self.assertEqual(5*investment_value(F(1), F(1, 5), F(1, 5)), F(162, 25))
        self.assertEqual(5*investment_value(F(1), F(1, 5), F(1, 10)), F(172, 25))

    def test_paced_delivery_keeps_attack_inferior(self):
        promised = (F(172, 25), F(81, 50))
        post_cost_war = (F(153, 25), F(153, 100))
        self.assertEqual(sum(promised), F(17, 2))
        for fraction in (F(i, 20) for i in range(21)):
            for goal, attack in zip(promised, post_cost_war):
                self.assertLessEqual(fraction*goal+(1-fraction)*attack, goal)
        # Receiving all Red output first can leave a profitable extra attack.
        self.assertGreater(promised[1]+F(9, 50)*promised[0], promised[1])

    def test_funded_defense_can_be_chosen_or_declined(self):
        initial_red = 2*.2*.99
        for cost, chosen in ((1., True), (3., False)):
            threshold = defense_threshold(cost)
            self.assertLess(threshold, min(1., 1/cost))
            self.assertAlmostEqual(.8*.99*(1+(1-threshold)*(1-cost*threshold)), 1.)
            protected = 1-cost*threshold
            self.assertEqual(protected > initial_red, chosen)
            best = max(initial_red, protected)
            for tick in range(501):
                s = min(1., 1/cost)*tick/500
                value = (.2*.99*(2-cost*s) if s < threshold else 1-cost*s)
                self.assertLessEqual(value, best+1e-12)

    def test_defense_primitive_cost_boundary(self):
        h = F(26, 99)
        outside = F(99, 250)
        critical = outside*(1-outside)/(outside-h)
        self.assertGreater(critical, 1)
        self.assertLess(critical, 3)
        s = defense_threshold(float(critical))
        self.assertAlmostEqual(1-float(critical)*s, float(outside))

    def test_conditional_defense_uses_current_goal(self):
        resource, cost, p, delta, beta = F(5), F(1), F(4, 5), F(99, 100), F(1)
        def values(disabled):
            stock = resource+(1-disabled)*(resource-cost)
            return ((1-p)*delta*stock,
                    ((1-p)-beta*p)*delta*stock)
        old_keep, current_keep = values(F(0))
        old_burn, current_burn = values(F(1))
        self.assertGreater(old_keep, old_burn)
        self.assertGreater(current_burn, current_keep)
        self.assertLess(p*delta*resource, resource)
        self.assertGreater(resource-cost, 2*(1-p)*delta*resource)

    def test_calibrated_attack_value_and_original_welfare_differ(self):
        p, delta, resource, cost, epsilon, beta = (
            F(4, 5), F(99, 100), F(5), F(1), F(1, 4), F(1))
        bonus = resource-cost-epsilon-delta*resource*((1-p)-beta*p)
        current = bonus+delta*resource*((1-p)-beta*p)
        original = (1-p)*delta*resource
        self.assertEqual(current, F(15, 4))
        self.assertEqual(original, F(99, 100))
        self.assertGreater(current, (1-p)*delta*(2*resource-cost))

    def test_consensual_replacement_and_share_selecting_goal(self):
        total, alpha = 9.5, 21/38
        goal = lambda blue: blue**alpha*(total-blue)**(1-alpha)
        chosen = goal(5.25)
        for tick in range(191):
            self.assertLessEqual(goal(tick/20), chosen+1e-12)
        self.assertGreater(5.25, 5)
        self.assertGreater(total-5.25, 4)
        # A higher Blue count can be worse for the actually installed goal.
        self.assertLess(goal(5.5), chosen)


class BroadProductionChecks(unittest.TestCase):
    def test_unilateral_commitment_bound_and_reciprocal_margin(self):
        for s, rho in product((F(-2, 5), F(-1, 4), F(0), F(1, 4), F(2, 5)),
                              (F(0), F(1, 2), F(1))):
            ordinary = 1/(1-s)
            leader = (1+s*(1+rho))/(1-2*s*s)
            follower = 1+s*leader
            benchmark = outputs(ordinary, ordinary, s, rho)[0]
            best = outputs(leader, follower, s, rho)[0]
            ell = rho*(1-s)+s
            gain = s*s*ell*ell/(2*(1-2*s*s)*(1-s)**2)
            self.assertEqual(best-benchmark, gain)
            common = (1+rho)/(1-2*s)
            reciprocal = outputs(common, common, s, rho)[0]-benchmark
            self.assertEqual(reciprocal-gain,
                             ell*ell*(1+2*s)/(2*(1-2*s)*(1-2*s*s)))
            cap = common if s >= 0 else 1+rho
            for tick in range(81):
                own = cap*F(tick, 80)
                self.assertLessEqual(outputs(own, 1+s*own, s, rho)[0], best)

    def test_random_commitments_do_not_exceed_the_bound(self):
        for s in (F(-1, 4), F(1, 4)):
            rho, probability = F(1, 2), F(2, 3)
            samples = (F(1, 4), F(5, 4))
            mean = probability*samples[0]+(1-probability)*samples[1]
            follower = 1+s*mean
            actual = probability*outputs(samples[0], follower, s, rho)[0]
            actual += (1-probability)*outputs(samples[1], follower, s, rho)[0]
            leader = (1+s*(1+rho))/(1-2*s*s)
            self.assertLessEqual(actual, outputs(leader, 1+s*leader, s, rho)[0])

    def test_power_cost_club_participation_from_actual_counts(self):
        for r, size in product((2, 3, 7, 10), range(2, 6)):
            actual = public_club_output(6, size, r, True)
            actual -= public_club_output(6, size-1, r, False)
            claimed = F(size**r-1, r)-(size-1)**r
            self.assertEqual(actual, claimed)
        self.assertEqual(F(3**3-1, 3)-2**3, F(2, 3))
        self.assertEqual(F(4**7-1, 7)-3**7, F(1074, 7))

    def test_quadratic_caps_keep_large_clubs_unprofitable(self):
        for size, rho, cap in product(range(3, 9),
                                      (F(1, 4), F(1)),
                                      (F(i, 4) for i in range(33))):
            own = min((size-1)*rho, cap)
            remaining = min((size-2)*rho, cap)
            advantage = (size-1)*rho*(own-remaining)-own*own/2-F(1, 100)
            self.assertLess(advantage, 0)

    def test_ces_efforts_are_actual_goal_best_responses(self):
        for r, beta, other in product((-10., -2., 0., .5, .9, 1.),
                                      (0., 1/3, 1.), (0., 1/2, 1.)):
            x, y = ces_efforts(beta, other, r)
            self.assertLessEqual(max(x, y), 1+1e-12)
            score = lambda own: (1+beta)*ces(own, y, r)-own*own/2-beta*y*y/2
            for tick in range(51):
                self.assertLessEqual(score(tick/50), score(x)+1e-11)

    def test_ces_goal_equilibrium_against_dense_deviations(self):
        for r in (-30., -10., -2., 0., .5, .9, 1.):
            beta = (1-r)/(3-r)
            value = ces_output(beta, beta, r)
            self.assertAlmostEqual(value-3/8, (1-4/(3-r)**2)/8)
            for tick in range(101):
                self.assertLessEqual(ces_output(tick/100, beta, r), value+1e-11)

    def test_essential_process_has_zero_equilibrium(self):
        for r in (-10., -2., 0.):
            for tick in range(1, 21):
                x = tick/20
                self.assertLess(2*ces(x, 0., r)-x*x/2, 0.)
        for r in (.25, .5, 1.):
            x = 2**(-1/r)
            self.assertGreater(ces(x, 0., r)-x*x/2, 0.)

    def test_cobb_sequential_control_and_common_repair(self):
        leader = .5*(4/3)**.75
        follower = .5*(4/3)**.25
        ordinary_blue = ces(leader, follower, 0.)-leader*leader/2
        ordinary_red = ces(leader, follower, 0.)-follower*follower/2
        self.assertAlmostEqual(ordinary_blue, 2/(3*sqrt(3)))
        self.assertAlmostEqual(ordinary_red, sqrt(3)/4)
        for tick in range(101):
            x = tick/100
            response = .5**(2/3)*x**(1/3)
            self.assertLessEqual(ces(x, response, 0.)-x*x/2, ordinary_blue+1e-12)
            common_response = x**(1/3)
            total = 2*ces(x, common_response, 0.)-(x*x+common_response**2)/2
            self.assertLessEqual(total, 1+1e-12)
        self.assertGreater(.5-ordinary_blue, (2-sqrt(3))/4)
        self.assertAlmostEqual(.5-ordinary_red, (2-sqrt(3))/4)


if __name__ == '__main__':
    unittest.main()
