"""Scoped checks for notes 011-014 and 020.

Fractions check physical budgets and finite deviations; square-root comparisons
use numerical values with strict margins. These checks do not independently
verify the continuous proofs or certify a real goal-verification technology.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest

from test_e2_results import frontier, pure_equilibria
from test_e2_robustness import quadratic_goal, triangle


def g(a, b):
    return (sqrt(a)+sqrt(b))/sqrt(2)


class LateGoalAndFusionTests(unittest.TestCase):
    def test_actual_homothetic_survivor_changes_threat(self):
        for share, alpha, war in product((F(1, 4), F(1, 2), F(3, 4)),
                                         (F(1, 5), F(3, 5)), (F(1, 2), F(4, 5))):
            actual_b = share*(1-alpha)*war+(1-share)*war
            self.assertEqual(actual_b, war*(1-share*alpha))
            self.assertGreater(actual_b, (1-share)*war)

    def test_late_goal_interval_conditions_and_binding_date(self):
        for share, p, w0, ratio in product((F(1, 5), F(1, 2), F(4, 5)),
                                          (F(1), F(2)), (F(1, 2), F(1)),
                                          (F(1, 2), F(1))):
            w1 = w0*ratio
            if p <= w1:
                continue
            earlier = 1-(1-share)*w0/p
            later = (p-w1)/(p-share*w1)
            feasible = share*w0/p < min(earlier, later)
            self.assertEqual(feasible, p > w0 and p*(p-w1) > share*w0*(p-share*w1))
            self.assertEqual(earlier <= later, p*(w0-w1) >= share*w0*w1)

    def test_power_boundary_and_expected_share_bias(self):
        self.assertEqual(1-(1+F(2, 3))*F(3, 4)+F(2, 3)**2*F(3, 4)**2, 0)
        for share, ratio in product((F(1, 5), F(1, 2), F(4, 5)),
                                    (F(1, 3), F(1, 2), F(7, 10))):
            h = lambda s: (1-ratio)/(1-s*ratio)
            mean_a = share*h(share)+(1-share)*(1-h(1-share))
            bias = share*(1-share)*(1-2*share)*ratio**2 / \
                ((1-share*ratio)*(1-(1-share)*ratio))
            self.assertEqual(mean_a-share, bias)
            self.assertGreater(h(share), share*ratio)

    def test_fusion_finite_offers_and_founder_participation(self):
        outside = (1+1/sqrt(2))/2
        offers = (F(1, 16), F(1, 5), F(1, 4), F(1, 2))
        choices = {}
        for penalty in (0.0, 0.09):
            accepted = [b for b in offers if g(b, 1-b)-penalty > outside]
            choices[penalty] = max(accepted, key=lambda b: 1-b)
        self.assertEqual(choices[0.0], F(1, 16))
        self.assertEqual(choices[0.09], F(1, 5))
        self.assertLess(choices[0.0], F(27, 200))
        self.assertGreater(choices[0.09], F(27, 200))
        self.assertGreater(g(F(1, 5), F(4, 5))-0.09-outside, 0.005)

    def test_unsecured_prepayment_fails_control_transfer(self):
        delivered, left = F(15, 16), F(1, 16)
        b_without_handover = delivered+left/2
        self.assertEqual(b_without_handover, F(31, 32))
        self.assertGreater(b_without_handover, delivered)
        outside = (1+1/sqrt(2))/2
        self.assertLess((g(left, delivered)+1/sqrt(2))/2, outside)
        self.assertLess(F(11, 10)-delivered, F(14, 25))
        # If a separate mechanism actually secures handover, the retained
        # goal does choose all A from the remaining stock, without a change.
        for j in range(9):
            a = left*F(j, 8)
            self.assertGreaterEqual(g(left, delivered), g(a, 1-a))
        self.assertGreater(g(left, delivered), outside)

    def test_deterministic_threshold_does_not_protect_lottery_mean(self):
        q, penalty = F(1, 5), 0.3
        current = lambda a, b: g(a, b)-(penalty if a < q else 0)
        outside = (current(F(1, 2), F(1, 2))+current(F(0), F(1)))/2
        bad = F(1, 16)
        self.assertLess(current(bad, 1-bad), outside)
        lottery_value = (current(bad, 1-bad)+current(q, 1-q))/2
        self.assertGreater(lottery_value, outside)
        old_mean = (bad+q)/2
        self.assertEqual(old_mean, F(21, 160))
        self.assertLess(old_mean, F(27, 200))
        self.assertGreater(1-old_mean, 1-q)


class InspectionTests(unittest.TestCase):
    def test_detection_and_mixed_trade_from_actual_branches(self):
        honest, undetected, rejected = F(4, 5), F(15, 16), F(3, 4)
        delta, inspect = F(9, 10), F(22, 27)
        self.assertEqual(inspect*delta, F(11, 15))
        self.assertEqual((1-inspect*delta)*undetected+inspect*delta*rejected, honest)
        outside = (1+1/sqrt(2))/2
        h = g(F(1, 5), F(4, 5))-0.09-outside
        ell = outside-g(F(1, 16), F(15, 16))+0.09
        cost = 0.002
        cheat = cost/(float(delta)*ell)
        self.assertLess(cheat, h/(h+ell))
        # Columns: no-inspect/accept, no-inspect/reject, inspect/pass-accept,
        # inspect/reject-all. Values are gains over the rejection baseline.
        game = [[(honest-rejected, h), (F(0), 0.0),
                 (honest-rejected, h-cost), (F(0), -cost)],
                [(undetected-rejected, -ell), (F(0), 0.0),
                 ((1-delta)*(undetected-rejected), -(1-float(delta))*ell-cost),
                 (F(0), -cost)]]
        f_values = [(1-cheat)*game[0][j][1]+cheat*game[1][j][1] for j in range(4)]
        self.assertAlmostEqual(f_values[0], f_values[2])
        self.assertGreater(f_values[0], f_values[1])
        self.assertGreater(f_values[0], f_values[3])
        b_values = [(1-inspect)*row[0][0]+inspect*row[2][0] for row in game]
        self.assertEqual(b_values[0], b_values[1])
        self.assertIn((1, 1), pure_equilibria(game))

    def test_inspector_can_refuse_even_after_a_pass(self):
        h, ell, delta, cost = F(1, 100), F(1, 10), F(3, 4), F(1, 1000)
        za = cost/(delta*ell)
        z0 = h/(h+ell)
        zb = (h-cost)/(h+(1-delta)*ell)
        def values(z):
            return ((1-z)*h-z*ell, F(0), (1-z)*h-z*(1-delta)*ell-cost, -cost)
        for z, best in ((F(0), 0), ((za+z0)/2, 2), ((z0+zb)/2, 2), ((zb+1)/2, 1)):
            payoffs = values(z)
            self.assertEqual(max(range(4), key=lambda j: payoffs[j]), best)
        self.assertEqual(values(za)[0], values(za)[2])
        self.assertEqual(values(zb)[1], values(zb)[2])

    def test_repair_set_bound_beats_even_unpenalized_goal(self):
        outside = (1+1/sqrt(2))/2
        self.assertLess(g(F(1, 10), F(3, 4)), outside)
        self.assertLess(F(592, 707), F(17, 20))
        self.assertLess(F(17, 20), outside)
        self.assertEqual(F(107, 100)-F(22, 100), F(17, 20))
        for j in range(11):
            b = F(3, 4)+F(j, 100)
            self.assertLessEqual(g(F(17, 20)-b, b), g(F(1, 10), F(3, 4)))


class InstallerAndScheduleTests(unittest.TestCase):
    def test_sunk_cost_protocol_has_real_combat_frontiers(self):
        work, elapsed = F(11, 5), F(0)
        war_outputs = []
        for cost in (F(0), F(1, 100), F(19, 100), F(1, 5)):
            work -= cost
            elapsed += (1 if cost else 0)
            war_outputs.append(frontier(F(0), F(1), work-F(3, 5),
                                        10-elapsed-1, F(1), F(1), F(1), F(1), F(1)))
            self.assertGreaterEqual(work, F(3, 5))
        self.assertEqual(war_outputs, [F(4, 5), F(159, 200), F(7, 10), F(3, 5)])
        self.assertGreater(work, 1)

    def test_actual_installer_choice_revises_an_unsecured_proposal(self):
        targets = {'H': (F(11, 20), F(9, 20)), 'L': (F(16, 25), F(9, 25))}
        accepted_late = [name for name, x in targets.items() if x[1] > F(7, 20)]
        chosen = max(accepted_late, key=lambda name: targets[name][0])
        self.assertEqual(chosen, 'L')
        self.assertLess(targets[chosen][1], F(2, 5))
        self.assertTrue(all(value > F(2, 5) for value in targets['H']))
        locked_values = {name: (x[0] if x[1] > F(159, 400) else F(159, 400))
                         for name, x in targets.items()}
        self.assertEqual(max(locked_values, key=locked_values.get), 'H')
        for a, b in targets.values():
            utility, _, _ = quadratic_goal(F(1), F(3, 5), a, F(4, 5))
            for x, y in triangle(F(3, 5)):
                self.assertGreaterEqual(utility(F(3, 5), F(0)), utility(x, y))
            self.assertEqual(utility(a, b), 1)

    def test_installer_separation_survives_certified_errors(self):
        epsilon = F(1, 4000000)
        for target_a in (F(11, 20), F(16, 25)):
            utility, curvature, margin = quadratic_goal(F(1), F(3, 5), target_a, F(4, 5))
            self.assertLessEqual(2*epsilon/curvature, F(1, 200)**2)
            self.assertLessEqual(epsilon/margin, F(1, 124000))
            self.assertGreater(1-utility(F(3, 5), 0), epsilon)
        self.assertGreater(F(71, 200), F(7, 20))
        self.assertLess(F(73, 200), F(159, 400))
        self.assertGreater(F(89, 200), F(2, 5))
        self.assertGreater(F(127, 200), F(111, 200))

    def test_arbitrary_smooth_schedule_construction(self):
        # m(Y)=Y^2/(2 Pmax), epsilon=1, K=2, C=9 Pmax.
        for maximum in (F(1), F(3)):
            for x, y in triangle(maximum):
                total = x+y
                target = total*total/(2*maximum)
                error = x-target
                derivative = total/maximum
                va = 9*maximum-4*total+2*error*(derivative-1)
                vb = 9*maximum-4*total+2*error*derivative
                schur = -4+2*error/maximum
                self.assertGreater(va, 0)
                self.assertGreater(vb, 0)
                self.assertLess(schur, 0)
                fixed_budget = lambda a: 9*maximum*total-2*total**2-(a-target)**2
                self.assertGreaterEqual(fixed_budget(target), fixed_budget(x))


if __name__ == '__main__':
    unittest.main()
