"""Exact constraint and interval checks supporting notes 044 and 046–058.

These check witness inequalities and finite enlargements, rather than treating
numerical agreement as a proof of the entire strategic implementation.
"""
from fractions import Fraction as F
from math import comb
import unittest

from experiments.r0002_welfare_checks import (
    audit_three_partition_witness, log_bounds, welfare_bound,
)


def product_polynomials(a, b):
    result = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def shifted_power(shift, exponent):
    return [F(comb(exponent, j))*shift**(exponent-j)
            for j in range(exponent+1)]


def subtract_intervals(a, b):
    return a[0]-b[1], a[1]-b[0]


def divide_positive_intervals(a, b):
    assert 0 < a[0] <= a[1] and 0 < b[0] <= b[1]
    return a[0]/b[1], a[1]/b[0]


class GuardedMechanisms(unittest.TestCase):
    def test_correlated_control_satisfies_all_recommendation_constraints(self):
        c, a, b, output = F(8, 5), F(1, 10), F(2, 5), F(10)
        for reserve, floor in [(F(8), F(0)), (F(10), F(0)),
                               (F(10), F(3, 5)), (F(100), F(1))]:
            effective = reserve-floor
            collateral = effective-c
            t = F(5)/(5*effective-18)
            b0 = (40*effective+41)/(15*(5*effective-23))
            mechanisms = [
                ((0, 1), t, (collateral, -collateral,
                              -collateral, output+collateral)),
                ((1, 1), 1-t, (-b0, output-b0-F(14, 3),
                                b0, b0+F(14, 3))),
            ]
            payoff = [F(0), F(0)]
            obedience = {(i, rec): F(0) for i in range(2) for rec in range(2)}
            for efforts, mass, transfers in mechanisms:
                p = b if efforts == (1, 1) else a
                self.assertEqual(transfers[0]+transfers[2], 0)
                self.assertEqual(transfers[1]+transfers[3], output)
                for i in range(2):
                    g0, g1 = transfers[2*i:2*i+2]
                    # Enforce collateral even if a recommended shirker works.
                    self.assertGreaterEqual(reserve-c+min(g0, g1), floor)
                    marginal = b-a if efforts[1-i] else a
                    work_gain = marginal*(g1-g0)-c
                    obedience[i, efforts[i]] += mass*(2*efforts[i]-1)*work_gain
                    payoff[i] += mass*((1-p)*g0+p*g1-c*efforts[i])
            self.assertTrue(all(v >= 0 for v in obedience.values()))
            self.assertEqual(payoff[1], 0)
            self.assertEqual(payoff[0], F(4, 5)-F(7)/(5*effective-18))

    def test_guard_effort_margins_and_physical_slack(self):
        for own_share in [F(9, 20), F(11, 20)]:
            for concern in [F(0), F(9, 50), F(11, 50)]:
                for probability_increment in [F(1, 10), F(3, 10)]:
                    gain = (probability_increment*10*
                            (own_share+concern*(1-own_share))-F(8, 5)+F(3, 2))
                    self.assertGreater(gain, 0)
        self.assertLess(F(16)+F(5, 2)-20, 0)
        work = F(3, 50)+F(1, 50)+F(1, 50)+F(1, 10)+F(4, 125)+10+F(17, 100)
        self.assertEqual(work, F(5201, 500))
        self.assertLess(work+F(1, 10), 11)
        self.assertGreater(F(2, 5), F(4, 11))  # Insured failure vs all late spoils.
        self.assertGreater(F(133, 100), F(4, 11))  # Diversified failure.
        self.assertLessEqual(28, 32)  # Negotiated default output delivery.

    def test_logarithmic_threshold_and_shirk_polynomial(self):
        def adoption_polynomial(z):
            return (z-F(33, 20))**3*(z+F(67, 20))**2-z**5
        self.assertLess(adoption_polynomial(F(77391, 10000)), 0)
        self.assertGreater(adoption_polynomial(F(77392, 10000)), 0)
        self.assertLess(F(12, 5)**3*F(37, 5)**2, F(4)**5)
        work = [F(0)]*6+shifted_power(F(5), 4)
        shirk = product_polynomials(shifted_power(F(8, 5), 9),
                                     shifted_power(F(33, 5), 1))
        coefficients = [x-y for x, y in zip(work, shirk)]
        self.assertEqual(coefficients[-1], 0)
        self.assertTrue(all(x < 0 for x in coefficients[:-1]))
        self.assertEqual(coefficients[-4:-1], [-F(11308, 25), -F(186, 5), -1])

    def test_diversified_witness_and_open_cost_correlation_rectangle(self):
        audit_three_partition_witness()
        # Log welfare decreases in material setup cost; it is affine in rho.
        # These interval bounds therefore cover the whole displayed rectangle.
        lower = min(welfare_bound(3, 3, 0, partition_cost=F(11, 1000), rho=r)[0]
                    for r in [F(9, 100), F(11, 100)])
        self.assertGreater(lower, log_bounds(F(4))[1])
        for n in range(1, 4):
            for full in range(n+1):
                for solo in range(n-full+1):
                    if (n, full, solo) == (3, 3, 0):
                        continue
                    upper = max(welfare_bound(n, full, solo,
                                               partition_cost=F(9, 1000), rho=r)[1]
                                for r in [F(9, 100), F(11, 100)])
                    self.assertGreater(lower, upper, (n, full, solo))

    def test_correlation_boundaries_and_larger_plan_repair(self):
        stock = log_bounds(F(4))
        g = {(m, r): subtract_intervals(welfare_bound(3, m, 0, rho=F(r)), stock)
             for m in [2, 3] for r in [0, 1]}
        decay2 = subtract_intervals(g[2, 0], g[2, 1])
        decay3 = subtract_intervals(g[3, 0], g[3, 1])
        switch = divide_positive_intervals(subtract_intervals(g[3, 0], g[2, 0]),
                                           subtract_intervals(decay3, decay2))
        end = divide_positive_intervals(g[2, 0], decay2)
        self.assertGreater(switch[0], F(180070, 10**6))
        self.assertLess(switch[1], F(180071, 10**6))
        self.assertGreater(end[0], F(269548, 10**6))
        self.assertLess(end[1], F(269549, 10**6))
        # At rho=.24 the revised two-compartment plan still improves both
        # original utilities, while the unrevised full plan falls below stock.
        self.assertGreater(welfare_bound(3, 2, 0, rho=F(6, 25))[0], stock[1])
        self.assertLess(welfare_bound(3, 3, 0, rho=F(6, 25))[1], stock[0])

    def test_coalition_work_repair_and_coordination_shares(self):
        total, work, disposal = F(307, 100), F(27, 4), F(2, 5)
        pair_war = F(4, 5)*F(2, 5)*(work-disposal)
        self.assertEqual(pair_war, F(254, 125))
        self.assertLess(pair_war, 2*total/3)
        self.assertGreater(work-3*disposal, F(53, 10))
        C, K, ordinary = F(4, 5), F(1, 10), F(2, 5)
        threshold = (K+ordinary)/(C+ordinary)
        self.assertEqual(threshold, F(5, 12))
        shares = [F(17, 25), F(3, 25)]
        for share, outside in zip(shares, [F(2, 5), F(0)]):
            self.assertEqual((F(1, 20)+outside)/(share+outside), threshold)

    def test_public_conversion_combat_and_guarded_adoption_margins(self):
        epsilon, discount = F(1, 10), F(99, 100)
        launch, repair, conversion, preparation = 10, 2, 24, 13
        war = epsilon+(1-epsilon)*discount**(launch+repair+conversion)
        stable_cap = 2*epsilon+epsilon/discount**(repair+conversion)
        q = epsilon+(1-epsilon)*discount**(preparation+conversion)/2
        winner = epsilon+(1-epsilon)*discount**(preparation+conversion)
        later_war = epsilon+(1-epsilon)*discount**(preparation+launch+repair+conversion)
        self.assertGreater(war, stable_cap)
        self.assertGreater(q-war/2, F(4, 100))
        for concern in [F(7, 10), F(8, 10), F(9, 10)]:
            self.assertGreater(epsilon+concern*winner, (1+concern)*later_war/2)
            self.assertGreater((1+concern)*q, (1+concern)*war/2)
            self.assertLess(1+concern-3, 0)
        self.assertLess(2, launch)  # Staged activation precedes new remote events.
        self.assertLess(preparation+launch, preparation+conversion-launch)
        # Constructive ordinary control: a larger agency stake deters the loser.
        high_agency = F(1, 2)
        high_war = high_agency+(1-high_agency)*discount**(launch+repair+conversion)
        self.assertGreater(high_agency, high_war/2)

    def test_survivor_allocation_and_concave_outside_bounds(self):
        def defeated_log_output(concern, recovered):
            return max(F(0), (concern*(1+recovered)-1)/(1+concern))
        self.assertEqual(defeated_log_output(F(1, 5), F(4)), 0)
        self.assertEqual(defeated_log_output(F(3, 10), F(4)), F(5, 13))
        # Check the interior first-order condition under the actual current goal.
        other = defeated_log_output(F(3, 10), F(4))
        own = 4-other
        self.assertEqual(1/(1+own), F(3, 10)/(1+other))
        # Equal-strength original log payoff, including defeated-project output.
        self.assertLess(log_bounds(F(15))[1]/2, log_bounds(F(4))[0])
        productive = welfare_bound(3, 3, 0)[0]
        for concern in [F(1, 10), F(3, 10)]:
            self.assertGreater((1+concern)*productive,
                               (1+concern)*log_bounds(F(366, 100))[1])

    def test_power_preference_stock_bound_and_actual_utility_gain(self):
        mean, second = F(7, 20), F(2449, 400)
        self.assertGreater(F(679, 100), second)
        for curvature in [2, 3, 5, 10]:
            z = F(13*curvature)
            stock = z-1
            self.assertGreater(2*mean*(z-F(33, 20))**(curvature+1),
                               curvature*second*z**curvature)
            def utility(x):
                return ((1+x)**(1-curvature)-1)/(1-curvature)
            gain = (F(3, 5)*utility(stock-F(33, 20))+
                    F(2, 5)*utility(stock+F(67, 20))-utility(stock))
            self.assertGreater(gain, 0)
            self.assertGreater(stock-F(33, 20), 4)

    def test_uniform_rewards_cover_post_miss_continuations(self):
        # These are global base bounds, not just fixed-contract effort margins.
        rows = [
            (F(16), F(17), F(19), F(40)),
            (F(47, 10), F(6), F(6), F(12)),
            (F(17), F(18), F(18), F(40)),
            (F(13, 10)*log_bounds(F(31))[1], F(5), F(6), F(12)),
            (F(13, 10)*log_bounds(F(17))[1], F(4), F(5), F(10)),
        ]
        for base_upper, reward_lower, reward_upper, penalty in rows:
            self.assertGreater(reward_lower, base_upper)
            self.assertGreater(penalty, base_upper+reward_upper)
        self.assertGreater(log_bounds(F(4))[0]+F(4),
                           F(13, 10)*log_bounds(F(5))[1])

    def test_actual_cost_and_collateral_comparison(self):
        def ordinary(stock):
            return F(2, 5) if stock <= F(71, 10) else F(4, 5)-7/(5*stock-18)
        guarded = F(7, 10)
        self.assertEqual(guarded-ordinary(F(3)), F(3, 10))
        self.assertEqual(guarded-ordinary(F(10)), F(19, 160))
        self.assertEqual(guarded, ordinary(F(88, 5)))
        self.assertGreater(ordinary(F(20)), guarded)

    def test_costly_verification_and_concern_design_boundaries(self):
        def margin(layers, false_accept=F(1, 10)):
            return ((1-F(layers, 1000))*(F(79, 25)-F(layers, 100))
                    -3-26*false_accept**layers)
        margins = {n: margin(n) for n in range(1, 15)}
        self.assertEqual([n for n in margins if margins[n] > 0], list(range(3, 13)))
        self.assertEqual(max(margins, key=margins.get), 4)
        self.assertEqual(margin(2, F(1, 20)), F(6872, 100000))
        for n in margins:
            self.assertLessEqual(18+n, 32)
            self.assertLess(F(5201, 500)+F(2, 100)*(n-1), 11)
            self.assertGreater(F(34, 25)-F(n, 100), F(4, 11))
        temptation, damage, buffer, error = F(3, 10), F(1, 2), F(1, 5), F(1, 100)
        lower = temptation/(temptation+damage)
        critical_gap = (damage*buffer-error*(temptation+damage))/temptation
        self.assertEqual(lower, F(3, 8))
        self.assertEqual(critical_gap, F(23, 75))
        for gap in [F(1, 10), F(3, 10)]:
            self.assertLess(lower, (buffer-error)/(buffer+gap))
        self.assertGreater(lower, (buffer-error)/(buffer+F(2, 5)))

    def test_asymmetric_combat_condition_and_two_peaceful_routes(self):
        epsilon, discount = F(1, 10), F(99, 100)
        war = epsilon+(1-epsilon)*discount**36
        later_war = epsilon+(1-epsilon)*discount**49
        winner = epsilon+(1-epsilon)*discount**37
        recovery_discount = discount**26
        def combat_index(strength):
            a_cap = epsilon*strength/((1-strength)*recovery_discount)
            b_cap = epsilon*(1-strength)/(strength*recovery_discount)
            return (max(F(0), strength*war-epsilon)/a_cap+
                    max(F(0), (1-strength)*war-epsilon)/b_cap)
        self.assertLess(combat_index(F(147132, 10**6)), 1)
        self.assertGreater(combat_index(F(147134, 10**6)), 1)
        for strength in [F(3, 20), F(1, 2), F(4, 5), F(17, 20)]:
            self.assertGreater(combat_index(strength), 1)
        strength, share, concern = F(4, 5), F(17, 20), F(4, 5)
        for p, pi in [(strength, share), (1-strength, 1-share)]:
            q = epsilon+pi*(winner-epsilon)
            self.assertGreater(q, p*war)
            self.assertGreater(epsilon+concern*winner,
                               (p+concern*(1-p))*later_war)
        self.assertGreater(winner, F(9, 10)*war)
        self.assertGreater(epsilon, F(1, 10)*war)

    def test_private_offer_requires_statewise_or_correct_posterior_check(self):
        baseline = [(F(27, 20), F(27, 20)), (F(117, 20), F(137, 20))]
        proposed = [(F(0), F(27, 10)), (F(36, 5), F(11, 2))]
        prior = [F(3, 5), F(2, 5)]
        receiver_prior_gain = sum(p*(new[1]-old[1])
                                  for p, old, new in zip(prior, baseline, proposed))
        self.assertEqual(receiver_prior_gain, F(27, 100))
        sender_gains = [new[0]+F(1, 5)*new[1]-old[0]-F(1, 5)*old[1]
                        for old, new in zip(baseline, proposed)]
        self.assertEqual(sender_gains, [-F(27, 25), F(27, 25)])
        self.assertLess(proposed[1][1], baseline[1][1])
        self.assertFalse(all(new[1] >= old[1] for old, new in zip(baseline, proposed)))

    def test_curvature_counterpart_and_exact_gamma_two_threshold(self):
        # The gamma=1/2 comparison at R=3 reduces to this rational sign.
        self.assertGreater(144*6909, 989**2)
        def gamma_two_gain(stock):
            z = stock+1
            return 1/z-F(3, 5)/(z-F(33, 20))-F(2, 5)/(z+F(67, 20))
        boundary = F(2071, 140)
        self.assertEqual(gamma_two_gain(boundary), 0)
        self.assertLess(gamma_two_gain(F(10)), 0)
        self.assertGreater(gamma_two_gain(F(15)), 0)
        for stock in [F(3), F(10), F(15), F(1000)]:
            z = stock+1
            closed = (F(7, 20)*z-F(2211, 400))/(z*(z-F(33, 20))*(z+F(67, 20)))
            self.assertEqual(gamma_two_gain(stock), closed)

    def test_voluntary_exit_uses_the_survivors_actual_allocation(self):
        def defeated_allocation(total, powered_concern):
            return max(F(0), (powered_concern*(1+total)-1)/(1+powered_concern))
        # Actual maximum material includes possible input/control gifts.
        for stock in [F(3), F(10)]:
            total_bound = 2*stock+F(167, 20)
            self.assertLess(defeated_allocation(total_bound, F(3, 10)), stock)
        self.assertLess(defeated_allocation(6+F(167, 20), F(9, 100)), 3)
        # Conditional cheaper-exit module: even a positive 0.01 exit cost
        # can leave enough of the 0.05 installation saving to beat the default.
        concern, saved_material = F(999, 1000), F(1, 25)
        for default in [10-F(33, 20), 10+F(67, 20)]:
            self.assertGreater(
                defeated_allocation(2*default+saved_material, concern), default)
            self.assertLess(defeated_allocation(2*default, concern), default)

    def test_safe_abort_and_catastrophic_error_have_different_adoption_costs(self):
        stock, setup = F(1000), F(1, 20)
        def utility(x):
            return 1-1/(1+x)
        retained = utility(stock)
        success = (F(3, 5)*utility(stock-F(33, 20))+
                   F(2, 5)*utility(stock+F(67, 20)))
        abort = utility(stock-setup)
        gain = success-retained
        safe_threshold = gain/(success-abort)
        catastrophic_threshold = gain/success
        self.assertGreater(safe_threshold, F(7, 8)-F(1, 100))
        self.assertLess(safe_threshold, F(7, 8))
        self.assertLess(catastrophic_threshold, F(1, 10**6))
        self.assertGreater((success+abort)/2, retained)
        self.assertLess(F(999, 1000)*success, retained)


if __name__ == '__main__':
    unittest.main()
