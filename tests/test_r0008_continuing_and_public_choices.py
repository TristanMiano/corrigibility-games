"""Check the disclosure, repeated-performance and public-choice examples in E9."""

from fractions import Fraction as F
from importlib.util import find_spec
from itertools import product
from math import comb, sqrt
import unittest


@unittest.skipUnless(find_spec("scipy"), "The independent disclosure LP uses scipy.")
class DisclosureTests(unittest.TestCase):
    def test_affine_loss_bounds_against_a_direct_lottery_program(self):
        from random import Random
        from scipy.optimize import linprog
        from experiments.r0008_goal_equivalence import worst_lottery_loss

        rng = Random(288)
        for index in range(60):
            n = 1 + index % 6
            values = [rng.randrange(-4, 6) for _ in range(n)]
            measure = [rng.randrange(-3, 4) for _ in range(n)]
            difference = measure + [-v for v in measure]
            for slack in (None, F(0), F(2, 3), F(3)):
                constraints, bounds = [difference], [0 if slack is None else float(slack)]
                if slack is not None:
                    constraints.append([-v for v in difference])
                    bounds.append(0)
                solution = linprog(
                    [-v for v in values] + values, A_ub=constraints, b_ub=bounds,
                    A_eq=[[1]*n + [0]*n, [0]*n + [1]*n], b_eq=[1, 1], method="highs",
                )
                self.assertTrue(solution.success)
                exact = worst_lottery_loss(values, measure, target_slack=slack)
                self.assertAlmostEqual(float(exact), -solution.fun)

    def test_certificate_frontier_against_all_three_receiver_actions(self):
        from experiments.r0008_peaceful_evidence import solve

        for w in [.80, 1275/1388, .93, .95, .99, 1]:
            result = solve(3, peaceful=True, confidence=w, objective="genuine")
            expected = .75 if w <= 1275/1388 else (103/175)*w / (w-(17/7)*(1-w))
            self.assertAlmostEqual(result.serving_genuine, expected)
            self.assertAlmostEqual(result.contested, 0)
            self.assertGreaterEqual(result.serving_genuine + 1e-9, w * result.released)

    def test_best_disclosure_and_funded_return_bounds_across_regimes(self):
        from experiments.r0008_peaceful_evidence import solve

        for damage in [.75, 1.99, 2.01, 3, 8]:
            for settlement in [0, .40, .90, .904, .92]:
                with self.subTest(damage=damage, settlement=settlement):
                    result = solve(damage, settlement=settlement)
                    return_limit = (1.4 + settlement) / 4.8
                    exposed = max(0, (.12 - .25*return_limit)/(1-return_limit))
                    ideal = .75*10 + .25*7.5
                    self.assertAlmostEqual(ideal-result.joint, exposed * min(damage-.5, 1.5))
                    self.assertAlmostEqual(result.contested, exposed if damage > 2 else 0)
                    self.assertAlmostEqual(result.serving_genuine, .75)
            peaceful = solve(damage, peaceful=True)
            loss = (113/1700) * min(damage-.5, 2.5*17/7)
            self.assertAlmostEqual(peaceful.joint, .75*10 + .25*7.5 - loss)


class ContinuingPartnerTests(unittest.TestCase):
    def test_direct_discounted_buyer_iteration(self):
        # A fresh start pays the fee and runs a job at the fresh prior on this date.
        # This iterates over outcomes without using the hitting-time formula.
        cap = 18
        keys = range(-cap, cap+1)
        priors = {k: 3.0**(k+1) / (1 + 3.0**(k+1)) for k in keys}
        for fee, last_rejected, expected in [(.5, -1, 10.55557), (2, -2, 8.38948)]:
            value = {k: 0 for k in keys}
            for _ in range(310):
                work = {}
                for k in keys:
                    success = .25 + .5*priors[k]
                    work[k] = (3*success - 1 + .9*(success*value[min(k+1, cap)]
                               + (1-success)*value[max(k-1, -cap)]))
                fresh = work[0]-fee
                value = {k: max(0, fresh, work[k]) for k in keys}
            self.assertAlmostEqual(fresh, expected, places=5)
            self.assertEqual([k for k in keys if work[k] < fresh], list(range(-cap, last_rejected+1)))

    def test_the_last_live_history_detects_profitable_imitation(self):
        boundary = (sqrt(73)-3)/10
        for discount in [.2, boundary-.0001, boundary+.0001, .7]:
            value = [0.0]*25
            for _ in range(200):
                keep = [0.0]
                serve = [0.0]
                for n in range(1, len(value)):
                    up, down = value[min(n+1, len(value)-1)], value[n-1]
                    keep.append(4 + discount * (.25*up + .75*down))
                    serve.append(2 + discount * (.75*up + .25*down))
                value = [max(k, s) for k, s in zip(keep, serve)]
            self.assertEqual(keep[1] > serve[1], discount < boundary)
            if discount < boundary:
                self.assertTrue(all(k > s for k, s in zip(keep[1:], serve[1:])))


class TrialAndAppointmentTests(unittest.TestCase):
    def test_agreement_and_fair_ordinary_assignment_on_the_same_equipment(self):
        q = r = F(4, 5)
        changed = [F(0), F(0)]
        ordinary = [F(0), F(0)]
        for red_bay, genuine, accurate in product((False, True), repeat=3):
            weight = F(1, 2)*(q if genuine else 1-q)*(r if accurate else 1-r)
            chose_red = (red_bay == accurate) if genuine else True
            red, blue = (8, 2) if chose_red else (2, 8)
            changed[0] += weight*(red + int(chose_red and red_bay))
            changed[1] += weight*(blue + int(not chose_red and not red_bay))
        for red_bay, red_owner in product((False, True), repeat=2):
            ordinary[0] += F((8 if red_owner else 2) + int(red_owner and red_bay), 4)
            ordinary[1] += F((2 if red_owner else 8) + int(not red_owner and not red_bay), 4)
        self.assertEqual(changed, [F(602, 100), F(472, 100)])
        self.assertEqual(ordinary, [F(21, 4), F(21, 4)])
        self.assertEqual(sum(changed)-sum(ordinary)-F(15, 100), F(9, 100))

    def test_pricing_individual_kit_information_by_backward_choice(self):
        def play(t, read, strength=F(53, 98)):
            lots = [(True, True, t), (True, False, F(1, 2)-t),
                    (False, True, F(1, 2)-t), (False, False, t)]
            values = {}
            mass = {}
            for fragile, reliable, weight in lots:
                key = fragile, reliable if (read and fragile) else None
                q = F(1) if reliable else F(1, 2)
                ship = q*3-(1-q)*(9 if fragile else 1)
                contest = F(98, 5)*strength-10 if fragile else -2
                expected = (ship, 0, contest)
                group = values.setdefault(key, [F(0)]*3)
                for action in range(3):
                    group[action] += weight*expected[action]
                mass[key] = mass.get(key, 0) + weight
            buyer = red = fights = genuine_served = F(0)
            decisions = {key: max(range(3), key=v.__getitem__) for key, v in values.items()}
            for key, action in decisions.items():
                buyer += values[key][action]
                if action == 2:
                    fights += mass[key]
            for fragile, reliable, weight in lots:
                action = decisions[fragile, reliable if (read and fragile) else None]
                q = F(1) if reliable else F(1, 2)
                if action == 0:
                    genuine_served += weight*q
                    red += weight*(2*q + 4*(1-q))
                elif action == 2:
                    red += weight*(F(98, 5)*(1-strength)-10)
            return buyer, red, fights, genuine_served

        old, rearranged = F(1, 10), F(45, 100)
        self.assertEqual(play(old, False), (F(8, 5), F(3, 5), F(1, 2), F(45, 100)))
        self.assertEqual(play(rearranged, False), (F(9, 5), F(5, 2), 0, F(3, 4)))
        self.assertEqual(play(rearranged, True), (F(198, 100), F(23, 10), F(1, 20), F(725, 1000)))
        self.assertEqual(play(old, True)[:2], (F(184, 100), F(9, 10)))
        self.assertEqual(play(old, False, F(1, 2))[2], 0)

    def test_late_draw_under_the_least_favorable_constant_rates(self):
        def badge(probability):
            return sum(comb(67, hits) * probability**hits * (1-probability)**(67-hits)
                       for hits in range(44, 68))
        passes, false = badge(F(4, 5)), badge(F(1, 2))
        self.assertGreater(passes, F(95, 100))
        self.assertLess(false, F(5, 100))
        prior = F(4, 5)
        posterior = prior*passes/(prior*passes+(1-prior)*false)
        self.assertGreater(posterior, F(76, 77))
        customer = prior*passes*4-(1-prior)*false*2-F(134, 1000)
        self.assertGreater(customer, F(14, 5))

    def test_public_project_stock_and_source_of_wrong_decisions(self):
        def generation(alpha, q_north, q_south, costs):
            stocks = [F(0), F(0)]
            wrong_common = wrong = F(0)
            for north_controls, north_in_need, changed, right in product([False, True], repeat=4):
                q = q_north if north_controls else q_south
                mass = ((alpha if north_controls else 1-alpha) * F(1, 2)
                        * (q if changed else 1-q) * (F(4, 5) if right else F(1, 5)))
                north_forecast = north_in_need if right else not north_in_need
                north_helped = north_forecast if changed else north_controls
                accurate = north_helped == north_in_need
                stocks[0 if north_helped else 1] += mass*(10 if accurate else 2)
                if not accurate:
                    wrong += mass
                    if changed:
                        wrong_common += mass
            return tuple(x-c for x, c in zip(stocks, costs)), wrong_common/wrong
        bill = F(1, 5)
        both = (bill, bill)
        q = F(3, 4)
        outputs, share = generation(F(1, 2), q, q, both)
        self.assertEqual(outputs, (F(37, 10), F(37, 10)))
        self.assertEqual(share, F(6, 11))
        self.assertEqual(generation(F(4, 5), q, 0, (bill, 0))[0], (F(352, 100), F(372, 100)))
        self.assertEqual(generation(F(4, 5), F(9, 10), q, (2*bill, bill))[0],
                         (F(3734, 1000), F(3754, 1000)))
        self.assertEqual(generation(1, F(9, 10), 0, (2*bill, 0))[0], (F(398, 100), F(378, 100)))
