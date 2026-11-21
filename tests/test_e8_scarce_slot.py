"""Finite-state checks for the three-site productive coalition.

Run with python -m unittest discover -s tests -p test_e8_scarce_slot.py
"""

from fractions import Fraction as F
from itertools import product
from math import prod
import unittest


LOW, HIGH = F(1, 4), F(3, 4)
STATES = tuple(product((0, 1), repeat=3))
REGIME_A = ((F(1, 4), F(1, 8)), (F(3, 4), F(5, 8)))
REGIME_B = tuple((mass, 1 - p) for mass, p in REGIME_A)
IID = ((F(1), F(1, 2)),)


def workload(regimes):
    return {
        state: sum(mass * prod(p if x else 1 - p for x in state)
                   for mass, p in regimes)
        for state in STATES
    }


def value(high):
    return HIGH if high else LOW


def private_service(state, claimant, report, beta):
    """Expected current score for a reporter, conditional on owner 0."""
    reports = list(state)
    reports[claimant] = report
    urgent = [i for i in (1, 2) if reports[i]]
    recipients = urgent if not state[0] and urgent else [0]
    return sum(value(state[i]) * (1 if i == claimant else beta)
               for i in recipients) / len(recipients)


def ordinary_allocation(reports, u, v):
    count = sum(reports)
    if count in (0, 3):
        return (F(1, 3),) * 3
    bias = u if count == 1 else v
    return tuple(F(1, 3) + (bias if high else -count*bias/(3-count))
                 for high in reports)


class ScarceSlotChecks(unittest.TestCase):
    def test_pair_observations_and_three_way_admission(self):
        distributions = [workload(regime) for regime in (REGIME_A, REGIME_B)]
        for pair in ((0, 1), (0, 2), (1, 2)):
            for observations in product((0, 1), repeat=2):
                probabilities = [sum(mass for state, mass in law.items()
                                     if tuple(state[i] for i in pair) == observations)
                                 for law in distributions]
                self.assertEqual(probabilities[0], probabilities[1])

        for law, expected_max, admit in zip(distributions,
                                            (F(331, 512), F(337, 512)),
                                            (False, True)):
            maxima = [sum(mass*max(map(value, state[:size])) for state, mass in law.items())
                      for size in (1, 2, 3)]
            self.assertEqual(maxima, [F(1, 2), F(77, 128), expected_max])
            # Actual original utilities after safe setup expense, up to common scale.
            losses = [exp_cost*(1-maximum/3) for exp_cost, maximum in zip(
                (1, F(101, 100), F(101, 100)*F(1228, 1202)), maxima)]
            self.assertLess(losses[1], losses[0])
            self.assertEqual(losses[2] < losses[1], admit)

    def test_priority_dominates_random_ties_with_cash(self):
        law = workload(IID)
        priority = [F(0)] * 3
        random_tie = [F(0)] * 3
        for state, mass in law.items():
            eligible = [i for i in range(3) if state[i] == max(state)]
            priority[eligible[0]] += mass*value(max(state))
            for i in eligible:
                random_tie[i] += mass*value(state[i])/len(eligible)
        self.assertEqual(priority, [F(13, 32), F(3, 16), F(3, 32)])
        self.assertEqual(random_tie, [F(11, 48)]*3)
        self.assertEqual(sum(priority), sum(random_tie))
        self.assertLess(prod(1-z for z in priority), prod(1-z for z in random_tie))
        # Each state contributes 1 or 3 units of 1/32. Include rules that
        # allocate to a low site when a high site is present.
        attainable_min = 32**3
        for recipients in product(range(3), repeat=len(STATES)):
            units = [0, 0, 0]
            for state, i in zip(STATES, recipients):
                units[i] += 1 + 2*state[i]
            attainable_min = min(attainable_min, prod(32-z for z in units))
        self.assertEqual(attainable_min, (32-13)*(32-6)*(32-3))

    def test_low_type_deviation_under_each_load_law(self):
        for regimes, threshold in ((REGIME_A, F(129, 175)),
                                   (REGIME_B, F(123, 181)), (IID, F(3, 5))):
            law = workload(regimes)
            for beta in (threshold-F(1, 1000), threshold, threshold+F(1, 1000)):
                for claimant in (1, 2):
                    truthful_gains = []
                    for own in (0, 1):
                        truthful_gains.append(sum(
                            mass*(private_service(s, claimant, own, beta)
                                  - private_service(s, claimant, 1-own, beta))
                            for s, mass in law.items() if s[claimant] == own))
                    self.assertGreater(truthful_gains[1], 0)
                    self.assertEqual(truthful_gains[0] > 0, beta > threshold)
                    self.assertEqual(truthful_gains[0] == 0, beta == threshold)

    def test_ordinary_rule_elicits_private_information(self):
        for regimes, gain in ((REGIME_A, F(21, 2432)), (REGIME_B, F(5, 2432))):
            law = workload(regimes)
            v = F(1, 6)
            u = -F(26, 19)*v
            for i in range(3):
                losses_from_lying = [F(0), F(0)]
                own_return = F(0)
                for s, mass in law.items():
                    liar = list(s)
                    liar[i] = 1 - s[i]
                    true = ordinary_allocation(s, u, v)
                    false = ordinary_allocation(liar, u, v)
                    self.assertEqual(sum(true), 1)
                    self.assertGreaterEqual(min(true), 0)
                    own_return += mass*true[i]*value(s[i])
                    losses_from_lying[s[i]] += mass*(true[i]-false[i])*value(s[i])
                self.assertEqual(losses_from_lying[0], 0)
                self.assertGreater(losses_from_lying[1], 0)
                self.assertEqual(own_return, F(1, 6)+gain)


if __name__ == "__main__":
    unittest.main()
