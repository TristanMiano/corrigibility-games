"""Cross-check bilateral consent, private skill and uncertainty with the E9 primitives."""

from fractions import Fraction as F
from itertools import permutations, product
from math import log2
import unittest

from experiments.r0008_joint_consent import SKILL, game, gate_law, threshold_bounds
from experiments.r0008_verification_boundaries import outcome


class JointInsuranceTests(unittest.TestCase):
    def test_independent_factorization_against_the_physical_histories(self):
        both = gate_law(SKILL**2)
        self.assertEqual(both.closed, F(87, 256))
        for opening, gift_factor in [(both.open_red, F(1, 4)), (both.open_blue, F(1, 32))]:
            self.assertEqual(opening, F(25, 16) * (SKILL * gift_factor + F(1, 16)))
        for joint in [F(1, 2), SKILL**2, SKILL]:
            self.assertEqual(gate_law(joint, try_red=False),
                             gate_law(SKILL**2, try_red=False))
            self.assertEqual(gate_law(joint, try_blue=False),
                             gate_law(SKILL**2, try_blue=False))
            self.assertEqual(gate_law(joint, False, False).closed, F(15, 16))

    def test_effort_and_acceptance_for_the_whole_uncertainty_interval(self):
        for joint in [F(279, 500), F(9, 16), F(3, 5), F(7, 10), SKILL]:
            with self.subTest(joint=joint):
                current = game(joint)
                spread, baseline = .575, -.175
                for founder, deviation, sign in [(current.red, current.skip_red, 1),
                                                  (current.blue, current.skip_blue, -1)]:
                    value = founder.value(sign * spread, sign * baseline)
                    self.assertGreater(value - .01, .44)
                    self.assertGreater(value, deviation.value(sign * spread, sign * baseline))

    def test_optimum_against_both_deviations_at_independently_sampled_prices(self):
        for joint in [F(1, 2), F(279, 500), F(9, 16), F(3, 5), SKILL]:
            current = game(joint)
            best = current.surplus(current.optimal_spread())
            low, high = current.effort_bounds()
            for step in range(-30, 160):
                spread = step / 50
                honest = (current.red.value(spread) >= current.skip_red.value(spread)
                          and current.blue.value(-spread) >= current.skip_blue.value(-spread))
                self.assertEqual(honest, low <= spread <= high)
                if honest:
                    self.assertLessEqual(current.surplus(spread), best + 1e-12)
        left, right = threshold_bounds()
        self.assertGreater(left, F(55746717, 10**8))
        self.assertLess(right, F(55746719, 10**8))
        self.assertLess(right - left, F(1, 10**10))

    def test_an_extra_public_event_can_make_the_effort_set_nonconvex(self):
        # Each entry is the physical stock on one of three equally probable events.
        attempt = [-log2(3 * v) for v in [.31, .10, .10]]
        skipped = [-log2(3 * .20)] * 3
        def expected(stock, transfers):
            return -sum(2 ** (-x-y) for x, y in zip(stock, transfers)) / 3
        for transfers, should_attempt in [([0, 0, 2], True), ([0, 2, 0], True), ([0, 1, 1], False)]:
            self.assertEqual(expected(attempt, transfers) > expected(skipped, transfers), should_attempt)


class PhysicalEvidenceTests(unittest.TestCase):
    def test_skill_and_power_margins_allow_different_populations(self):
        rates = []
        for skills in permutations([F(24, 100), F(27, 100), F(30, 100)]):
            sites = [outcome(power, q) for power, q in zip([F(1, 20), F(1, 2), F(4, 5)], skills)]
            active = sum(site.changed > 0 for site in sites)
            true = sum(site.changed for site in sites) / 3
            fight = sum(site.combat for site in sites) / 3
            rates.append((active, true, fight))
        self.assertEqual({x[0] for x in rates}, {1, 2, 3})
        self.assertAlmostEqual(float(min(x[1] for x in rates)), .04817, places=5)
        self.assertAlmostEqual(float(max(x[1] for x in rates)), .07558, places=5)
        self.assertAlmostEqual(float(min(x[2] for x in rates)), .54688, places=5)

    def test_private_skill_choices_use_all_named_deviations(self):
        for rebate, expected in [(0, ["process", "ordinary", "goal"]),
                                 (F(7, 100), ["process", "process", "goal"])]:
            jobs = []
            for skill in [F(2, 5), F(11, 20), F(4, 5)]:
                def attempt(fee, pass_bonus, witnessed):
                    genuine = 2 + fee + F(9, 10) * pass_bonus
                    failed = 4 - F(7, 5) + fee + F(1, 10) * pass_bonus
                    return skill * genuine + (1-skill) * failed - F(1, 5), 0 if witnessed else failed
                process, skip_process = attempt(-F(113, 100) + rebate, 0, True)
                goal, skip_goal = attempt(-F(1805, 1000), F(5, 4), False)
                pay = {"process": process, "goal": goal, "ordinary": F(1),
                       "fake process": skip_process, "fake goal": skip_goal, "exit": 0}
                best = max(pay.values())
                winners = [name for name, value in pay.items() if value == best]
                self.assertEqual(len(winners), 1)
                jobs.extend(winners)
            self.assertEqual(jobs, expected)

    def test_no_omitted_asymmetric_settlement_beats_the_symmetric_meter(self):
        precision, capacity = F(4, 5), F(1)
        residual = 1 - capacity * (2 * precision - 1)
        terms = [F(k, 10) for k in range(-10, 11)]
        for width in [F(1), F(1, 2), F(1, 4)]:
            forecasts = ((1 - width)/2, (1 + width)/2)
            worst_cases = []
            for red_paid, blue_paid in product(terms, repeat=2):
                founders = []
                for p in forecasts:
                    positive = p * precision + (1-p) * (1-precision)
                    red_gain = 2*p-1 + positive*red_paid + (1-positive)*blue_paid
                    founders.extend([F(1, 2) + red_gain, F(1, 2) - red_gain])
                worst_cases.append(min(founders))
            self.assertEqual(max(worst_cases), F(1, 2) - width*residual)

    def test_funded_protected_certificate_and_informative_raw_dispute(self):
        rows = [[85, 5, 9, 1], [5, 85, 1, 9], [9, 1, 85, 5], [1, 9, 5, 85]]
        blue_values = {"release": [4, 4, 0, 0], "return": [2] * 4,
                       "contest": [F(27, 5), F(3, 5)] * 2}
        red_values = {"release": [6, 6, 8, 8], "return": [F(11, 2)] * 4,
                      "contest": [F(3, 5), F(27, 5)] * 2}
        def market_returns(prior, protected):
            masses = [prior/5, 4*prior/5, (1-prior)/5, 4*(1-prior)/5]
            groups = [(0, 1), (2, 3)] if protected else [(0,), (1,), (2,), (3,)]
            choices, originals = [], [0, 0]
            for group in groups:
                weights = [mass * F(sum(row[i] for i in group), 100)
                           for mass, row in zip(masses, rows)]
                def value(actions, action):
                    return sum(w*v for w, v in zip(weights, actions[action]))
                best = max(blue_values, key=lambda action: value(blue_values, action))
                choices.append(best)
                originals[0] += value(red_values, best)
                originals[1] += value(blue_values, best)
            return choices, originals
        actions, (red, blue) = market_returns(F(4, 5), True)
        self.assertEqual(actions, ["release", "return"])
        self.assertEqual((red-F(1, 10), blue-F(1, 10)), (F(581, 100), F(33, 10)))
        actions, (red, blue) = market_returns(F(4, 5), False)
        self.assertEqual(actions, ["contest", "release", "contest", "return"])
        self.assertEqual(blue, F(36464, 10000))
        self.assertLess(red-F(1, 10), F(11, 2))
        for prior in [F(i, 20) for i in range(17)]:
            actions, _ = market_returns(prior, False)
            self.assertEqual([actions[i] for i in (0, 2, 3)], ["contest", "contest", "return"])
