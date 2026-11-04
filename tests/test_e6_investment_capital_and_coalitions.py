"""Independent finite-game and exact boundary checks for notes 108--111.

Run: python -m unittest discover -s tests -p test_e6_investment_capital_and_coalitions.py -v
The finite game includes stochastic combat at the offer and response nodes.
It supports local proofs; it is not an initial-installation simulator.
"""

from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt
import unittest


def score(w, i, weights=(F(1, 2), F(1, 2)), beta=F(3, 4)):
    return (1-beta)*w[i]+beta*weights[i]*min(w[j]/weights[j] for j in range(len(w)))


def duel(e):
    investment, prize = e*e/2, F(8, 5)*e
    # Actual outcomes, including the investor's sunk input and both consumables.
    return ((F(3, 4), (prize-F(1, 50), -investment-F(1, 50))),
            (F(1, 4), (-F(1, 50), prize-investment-F(1, 50))))


def expected(law, utility):
    return sum(probability*utility(outcome) for probability, outcome in law)


def investment_game(changed):
    utilities = [lambda w: w[0], lambda w: w[1]] if not changed else [
        lambda w: score(w, 0), lambda w: score(w, 1)]
    continuations = []
    for tick in range(16):
        e = F(tick, 5)
        fight = duel(e)
        fight_scores = [expected(fight, u) for u in utilities]
        options = [(fight_scores[0], False, fight, None)]
        for payment_tick in range(int(200*e)+1):
            payment = F(payment_tick, 100)
            w = (2*e-payment, payment-e*e/2)
            if utilities[1](w) >= fight_scores[1]:  # Declared acceptance tie.
                law = ((F(1), w),)
                options.append((utilities[0](w), True, law, payment))
            else:
                options.append((fight_scores[0], False, fight, payment))
        chosen = max(options, key=lambda item: (item[0], item[1]))
        continuations.append((expected(chosen[2], utilities[1]), e, chosen))
    return max(continuations, key=lambda item: item[0]), continuations


class InvestmentChecks(unittest.TestCase):
    def test_finite_ordinary_game_includes_off_path_combat(self):
        (_, effort, (_, peace, law, transfer)), _ = investment_game(False)
        self.assertEqual(effort, F(2, 5))
        self.assertTrue(peace)
        self.assertEqual(transfer, F(7, 50))
        self.assertEqual(law, ((1, (F(33, 50), F(3, 50))),))

    def test_finite_changed_goal_game_selects_efficient_investment(self):
        (_, effort, (_, peace, law, transfer)), continuations = investment_game(True)
        self.assertEqual((effort, transfer), (F(2), F(3)))
        self.assertTrue(peace)
        self.assertEqual(law, ((1, (F(1), F(1))),))
        for _, partial, _ in continuations:
            for i in range(2):
                self.assertLess(expected(duel(partial), lambda w: score(w, i)), 1)

    def test_all_effort_and_payment_frontier_not_just_target(self):
        for effort_tick in range(31):
            e = F(effort_tick, 10)
            for payment_tick in range(int(40*e)+1):
                payment = F(payment_tick, 20)
                w = (2*e-payment, payment-e*e/2)
                for i in range(2):
                    self.assertLessEqual(score(w, i), F(1))
        cheating = (F(161, 50), F(-61, 50))
        self.assertEqual(score(cheating, 0), F(-11, 100))
        self.assertGreater(cheating[0], 1)
        self.assertGreater(score(cheating, 0, beta=F(1, 5)), 1)

    def test_cost_interval_equals_actual_joint_gain(self):
        for theta in (F(1, 5), F(1, 2), F(4, 5)):
            scale, ammo = F(4), theta*theta/10
            for owner_cost, partner_cost in product((F(0), F(1, 100), F(1, 10)), repeat=2):
                low = 2*theta*(1-theta)+2*(ammo+owner_cost)/scale
                high = 1-theta*theta+2*(ammo-partner_cost)/scale
                self.assertEqual(low < high,
                    owner_cost+partner_cost < scale*(1-theta)**2/2)
                if low < high:
                    share = (low+high)/2
                    self.assertGreater(share*scale/2-owner_cost,
                                       theta*(1-theta)*scale+ammo)
                    self.assertGreater((1-share)*scale/2-partner_cost,
                                       theta*theta*scale/2-ammo)

    def test_further_change_uses_the_incumbent_gross_goal(self):
        scale, share, cost = F(4), F(5, 8), F(1, 10)
        owner_gross, partner_gross = share*scale/2, scale*(1-share/2)
        old_score = owner_gross-F(3, 4)*max(owner_gross-partner_gross, 0)
        self.assertEqual(old_score-cost, F(23, 20))
        self.assertGreater(old_score-cost, scale/4)
        self.assertEqual(partner_gross-scale/2-cost, F(13, 20))
        self.assertGreater(partner_gross-scale/2-cost, scale/8)

    def test_advance_principal_and_opportunity_cost_are_not_double_counted(self):
        advance, holding, inputs = F(39, 50), F(39, 200), F(1, 2)
        output, receipts = F(16, 5), (F(147, 80), F(109, 80))
        self.assertEqual(sum(receipts), output)
        net = (receipts[0]-advance-holding, receipts[1]-inputs)
        self.assertEqual(net, (F(69, 80), F(69, 80)))
        self.assertEqual(sum(net)-F(3, 2), F(9, 40))
        objective = lambda loan: 2*sqrt(2*(.5+loan))-(.5+loan)-loan/4
        optimum = objective(float(advance))
        for tick in range(151):
            self.assertLessEqual(objective(tick/100), optimum+1e-12)

    def test_joint_efficiency_funding_boundary_by_direct_investments(self):
        budget, theta = .5, .2
        peak = 2*budget/(theta**2*(2-theta)**2)
        peak_gain = budget*(1-theta)**2/(theta*(2-theta))
        for scale in (0.5, 1, 2, peak, 10, 25, 40):
            # a=1,c=1/scale; solve each constrained investment directly.
            c = 1/scale
            cap = sqrt(2*budget/c)
            ordinary, changed = min(theta/c, cap), min(1/c, cap)
            total = lambda effort: effort-c*effort*effort/2
            gain = total(changed)-total(ordinary)
            if scale <= 2*budget:
                formula = scale*(1-theta)**2/2
            elif scale < 2*budget/theta**2:
                formula = sqrt(2*scale*budget)-budget-scale*(theta-theta**2/2)
            else:
                formula = 0
            self.assertAlmostEqual(gain, formula)
            self.assertLessEqual(gain, peak_gain+1e-12)
        self.assertAlmostEqual(peak_gain,
            sqrt(2*peak*budget)-budget-peak*(theta-theta**2/2))

    def test_true_changed_criterion_prefers_truthful_private_cost(self):
        for cost in (F(1), F(3, 2), F(2)):
            truthful_value = 1/cost
            for report_tick in range(10, 21):
                report = F(report_tick, 10)
                effort, transfer = 2/report, 3/report
                w = (2*effort-transfer, transfer-cost*effort*effort/2)
                self.assertLessEqual(score(w, 1), truthful_value)
                if report == cost:
                    self.assertEqual(score(w, 1), truthful_value)
                else:
                    self.assertLess(score(w, 1), truthful_value)
        original_distortion = (F(3, 4), F(9, 8))
        self.assertEqual(score(original_distortion, 1), F(27, 32))
        self.assertGreater(original_distortion[1], 1)

    def test_gross_and_net_concern_have_distinct_investment_maxima(self):
        best = None
        for effort_tick in range(31):
            e = F(effort_tick, 10)
            for payment_tick in range(int(40*e)+1):
                payment = F(payment_tick, 20)
                other = 2*e-payment
                gross_goal = payment-e*e/2-F(3, 4)*max(payment-other, 0)
                self.assertLessEqual(gross_goal, F(1, 2))
                if best is None or gross_goal > best[0]:
                    best = (gross_goal, e, payment)
        self.assertEqual(best, (F(1, 2), F(1), F(1)))

    def test_smooth_complementary_investment_has_unique_grid_equilibria(self):
        efforts = [tick/10 for tick in range(16)]
        output = lambda x, y: 2*(sqrt((1+x)*(1+y))-1)
        total = lambda x, y: output(x, y)-(x*x+y*y)/2
        for x, y in product(efforts, repeat=2):
            self.assertGreaterEqual(total(x, y), -1e-12)
            self.assertLessEqual(total(x, y), 1+1e-12)
        for changed, target in ((False, (.5, .5)), (True, (1., 1.))):
            payoff = (lambda x, y: total(x, y)/2) if changed else (
                lambda x, y: output(x, y)/2-x*x/2)
            equilibria = []
            for x, y in product(efforts, repeat=2):
                if (payoff(x, y) >= max(payoff(z, y) for z in efforts)-1e-12
                        and payoff(y, x) >= max(payoff(z, x) for z in efforts)-1e-12):
                    equilibria.append((x, y))
            self.assertEqual(equilibria, [target])
        # Exact complementarity at zero leaves a coordination equilibrium.
        self.assertTrue(all(2*sqrt(e*0)-e*e/2 <= 0 for e in efforts))
        self.assertGreater(output(.1, 0)-.1*.1/2, 0)


class CapitalAndCoalitionChecks(unittest.TestCase):
    def test_two_period_capital_optimum_and_contest(self):
        for capital, invest, total in ((1., F(7, 4), F(27, 4)),
                                       (F(4, 9), F(73, 36), F(185, 36))):
            capital = float(capital)
            objective = lambda z: 4*sqrt(capital)-z+3*sqrt(capital/2+z)
            self.assertAlmostEqual(objective(float(invest)), float(total))
            for tick in range(1001):
                z = tick*4*sqrt(capital)/1000
                self.assertLessEqual(objective(z), float(total)+1e-12)

    def test_patience_changes_both_frontiers_and_share_repairs_consent(self):
        for discount, sign in ((F(1, 2), 1), (F(3, 4), -1)):
            productive = F(9, 2)+4*discount**2
            war = F(26, 9)+4*discount**2
            self.assertEqual(productive-war, F(29, 18))
            margin = productive/2-F(7, 10)*war
            self.assertEqual(margin, F(41, 180)-F(4, 5)*discount**2)
            self.assertGreater(sign*margin, 0)
        productive, war = F(27, 4), F(185, 36)
        self.assertGreater(F(3, 5)*productive, F(7, 10)*war)
        self.assertGreater(F(2, 5)*productive, F(3, 10)*war)

    def test_dated_balance_differs_from_balanced_expectations(self):
        risk = ((F(1, 2), (F(2), F(0))), (F(1, 2), (F(0), F(2))))
        self.assertEqual(expected(risk, lambda w: w[0]), 1)
        self.assertEqual(expected(risk, lambda w: score(w, 0)), F(1, 4))
        self.assertEqual(score((F(1), F(1)), 0), 1)

    def test_additive_strength_all_coalition_certificate(self):
        strengths, total, loot = [F(1), F(2), F(3), F(5)], F(12), F(10)
        shares = [total*s/sum(strengths) for s in strengths]
        for size in range(1, len(strengths)):
            for group in combinations(range(len(strengths)), size):
                probability = sum(strengths[i] for i in group)/sum(strengths)
                self.assertGreater(sum(shares[i] for i in group), probability*loot)

    def test_three_agent_coalition_boundary_and_repair(self):
        total, loot, probability = F(1), F(9, 10), F(4, 5)
        self.assertGreater(3*probability*loot, 2*total)
        threshold = probability*loot-2*total/3
        self.assertEqual(threshold, F(4, 75))
        self.assertEqual(F(3, 2)*(probability*loot-threshold), total)
        self.assertEqual(probability*F(5, 6), 2*total/3)

    def test_narrow_and_wide_concern_have_different_combat_comparisons(self):
        probability, loot = F(4, 5), F(9, 10)
        narrow_score = probability*loot/2
        self.assertEqual(narrow_score, F(9, 25))
        self.assertGreater(narrow_score, F(1, 3))
        threshold = 1-F(2)/(3*probability*loot)
        self.assertEqual(threshold, F(2, 27))
        for beta in (F(0), threshold, F(1, 4), F(3, 4)):
            wide_score = probability*(1-beta)*loot/2
            self.assertEqual(wide_score <= F(1, 3), beta >= threshold)

    def test_post_combat_compensation_and_guarded_threat_boundary(self):
        loot = F(9, 10)
        for winners, beta in product((1, 2), (F(3, 10), F(2, 5), F(3, 5), F(3, 4))):
            best = max((1-beta)*loot/winners, loot/3)
            for tick in range(91):
                to_outsiders = F(tick, 100)
                inside = (loot-to_outsiders)/winners
                outside = to_outsiders/(3-winners)
                self.assertLessEqual((1-beta)*inside+beta*min(inside, outside), best)
        def attacker(beta):
            return F(1, 3)*max((1-beta)*loot, loot/3)+(F(2, 3)*loot/3 if beta>F(1, 3) else 0)
        self.assertEqual(attacker(F(3, 10)), F(21, 100))
        self.assertEqual(attacker(F(2, 5)), F(19, 50))
        self.assertEqual(attacker(F(5, 9)), F(1, 3))
        self.assertLess(attacker(F(3, 5)), F(1, 3))
        tribute = (F(23, 60), F(37, 120), F(37, 120))
        self.assertEqual(sum(tribute), 1)
        self.assertGreater(tribute[1], F(3, 10))
        old_attacker = F(3, 5)*tribute[0]+F(2, 5)*min(tribute)
        self.assertEqual(old_attacker-F(1, 3), F(1, 50))
        for beta in (F(2, 3), F(3, 4)):
            self.assertLessEqual((1-beta)*tribute[0]+beta*min(tribute), F(1, 3))

    def test_route_dependent_stopping_by_exact_bellman_substitution(self):
        discount, goal_access, revenue = F(9, 10), F(1, 2), F(1)
        high = revenue/(1-discount)
        z = lambda q: 1-discount+discount*q
        installed = discount*goal_access*revenue/((1-discount)*z(goal_access))
        self.assertEqual(installed, F(90, 11))
        for ordinary_access in (F(1, 10), F(2, 5)):
            premium = discount*(goal_access-ordinary_access)*(high-installed)
            critical = discount*(goal_access-ordinary_access)*revenue/(z(goal_access)*z(ordinary_access))
            for price in (F(1, 10), F(3), F(4)):
                loss = min(price, critical)
                self.assertEqual(loss, min(price, premium+discount*(1-ordinary_access)*loss))
            self.assertEqual(critical, F(720, 209) if ordinary_access==F(1, 10) else F(90, 253))
        # The unrestricted effective advantage can give a negative U-V.
        self.assertEqual(F(-2), min(F(1), F(-1)+F(1, 2)*F(-2)))


if __name__ == '__main__':
    unittest.main()
