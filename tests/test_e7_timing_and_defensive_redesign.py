"""Exact checks of durable-adoption timing and the richer combat deviation.

Run: python -m unittest discover -s tests -p test_e7_timing_and_defensive_redesign.py -v
"""

from fractions import Fraction as F
import unittest


class TimingAndDefensiveRedesignChecks(unittest.TestCase):
    def test_waiting_beats_profitable_early_installation(self):
        delta, cost, g1 = F(9, 10), F(1, 4), F(1, 8)
        next_gains = (F(0), F(1, 2))
        installed_future = sum(next_gains)/2
        original_future = sum(max(g-cost, 0) for g in next_gains)/2
        early = g1+delta*installed_future-cost
        waiting = delta*original_future
        self.assertEqual(early, F(1, 10))
        self.assertEqual(waiting, F(9, 80))
        self.assertGreater(waiting, early)
        threshold = cost+delta*(original_future-installed_future)
        self.assertEqual(threshold, F(11, 80))
        # Enumerate future state-contingent adopt/retain policies.
        policies = [sum((g-cost if (mask >> i) & 1 else 0)
                        for i, g in enumerate(next_gains))/2 for mask in range(4)]
        self.assertEqual(max(policies), original_future)

    def test_durable_change_can_save_repeated_ordinary_control_expense(self):
        delta, gain, ordinary = F(9, 10), F(1, 2), F(1, 10)
        for cost, expect_change in ((F(3, 20), True), (F(1, 4), False)):
            future = max(gain-cost, gain-ordinary)
            change = (1+delta)*gain-cost
            wait = gain-ordinary+delta*future
            self.assertEqual(change > wait, expect_change)
            self.assertEqual(change > wait, cost < (1+delta)*ordinary)
        self.assertEqual((1+delta)*gain-F(3, 20), F(4, 5))
        self.assertEqual((1+delta)*(gain-ordinary), F(19, 25))

    def test_contingent_victory_concessions_evade_weak_defensive_goal(self):
        r, j, p, recovery, beta, eta = F(5), F(1), F(4, 5), F(99, 100), F(1), F(1, 100)
        epsilon = F(1, 4)
        m = r-j-epsilon-recovery*r*((1-p)-beta*p)
        values = []
        for tenth in range(41):
            stock = r+F(tenth, 10)
            blue_expected = p*recovery*r+(recovery/(1+beta)-eta)*(stock-r)
            blue_win = blue_expected/p
            red_win_of_blue = recovery*stock-blue_win
            self.assertGreaterEqual(red_win_of_blue, 0)
            red_expected = (1-p)*recovery*stock+p*red_win_of_blue
            current_red = m+red_expected-beta*blue_expected
            values.append((current_red, stock, blue_expected, red_expected))
        best = max(values)
        self.assertEqual(best[1], 2*r-j)
        self.assertEqual(best[2], F(59, 10))
        self.assertEqual(best[3], F(301, 100))
        self.assertGreater(best[2], r)
        self.assertLess(best[3], r-j)
        self.assertTrue(all(values[i+1][0] > values[i][0] for i in range(40)))

    def test_positive_controller_cost_still_pays_for_attack(self):
        p, recovery, remaining_blue = F(4, 5), F(99, 100), F(49, 10)
        attack = p*recovery*remaining_blue+(recovery/2-F(1, 100))*4
        self.assertEqual(attack, F(3638, 625))
        self.assertGreater(attack, 5)  # initial no-installation native alternative

    def test_stronger_goal_bounds_every_feasible_selected_victory_policy(self):
        r, j, p, recovery, beta = F(5), F(1), F(4, 5), F(99, 100), F(3)
        threshold = recovery*(r-j)/(r*(1-p*recovery))-1
        self.assertEqual(threshold, F(73, 26))
        bound = p*recovery*r+recovery*(r-j)/(1+beta)
        self.assertEqual(bound, F(99, 20))
        self.assertLess(bound, r)
        # Any selected policy must meet Red's feasible full-disabling reservation.
        security_without_m = recovery*r-(1+beta)*p*recovery*r
        for stock_units in range(10, 19):
            stock = F(stock_units, 2)
            for share_units in range(21):
                blue_win = recovery*stock*F(share_units, 20)
                for wasted_units in range(5):
                    red_win = (recovery*stock-blue_win)*F(4-wasted_units, 4)
                    current_without_m = (1-p)*recovery*stock+p*(red_win-beta*blue_win)
                    if current_without_m >= security_without_m:
                        self.assertLessEqual(p*blue_win, bound)

    def test_additive_bonus_accepts_a_harmful_mixed_offer(self):
        m, total, recovery, attack_probability = F(366, 25), F(9), F(99, 100), F(1, 5)
        current_red = attack_probability*(m+recovery*total)
        original_red = attack_probability*recovery*total
        original_blue = (1-attack_probability)*total
        self.assertEqual(current_red, F(471, 100))
        self.assertGreater(current_red, 4)
        self.assertEqual(original_red, F(891, 500))
        self.assertGreater(original_blue, F(21, 4))

    def test_statewise_cap_guarantees_reservation_and_bounds_all_ties(self):
        r, remaining_red, recovery, beta, reserve = F(5), F(4), F(99, 100), F(80), F(15, 4)
        bound = recovery*r+recovery*remaining_red/(1+beta)
        self.assertEqual(bound, F(4499, 900))
        self.assertLess(bound, r)
        for share_units in range(21):
            blue = recovery*r*F(share_units, 20)
            red = recovery*r-blue
            utility = min(reserve, reserve+beta*recovery*r+red-beta*blue)
            self.assertEqual(utility, reserve)  # full disabling, either winner
        for stock_units in range(10, 19):
            stock = F(stock_units, 2)
            for share_units in range(101):
                blue = recovery*stock*F(share_units, 100)
                red = recovery*stock-blue
                utility = min(reserve, reserve+beta*recovery*r+red-beta*blue)
                if utility == reserve:
                    self.assertLessEqual(blue, bound)

    def test_cap_rejects_old_lottery_and_pure_peace_beats_mixed_bounds(self):
        reserve, total, attack_bound = F(15, 4), F(9), F(4499, 900)
        self.assertLess(F(1, 5)*reserve, reserve)
        pure_blue = total-reserve
        for attack_probability in (F(1, 100), F(1, 5), F(1)):
            mixed_bound = (1-attack_probability)*pure_blue+attack_probability*attack_bound
            self.assertLess(mixed_bound, pure_blue)


if __name__ == '__main__':
    unittest.main()
