"""Finite-state checks for the three-site productive coalition.

Run with python -m unittest discover -s tests -p test_e8_scarce_slot.py
"""

from fractions import Fraction as F
from itertools import product
from math import acos, cos, exp, log, prod, sin
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

    def test_funded_insurance_with_three_report_levels(self):
        # Physical levels 3 log(2), 6 log(2), 9 log(2). An equal
        # share is an integer multiple of log(2), so CARA is rational.
        levels = (1, 2, 3)
        for masses, truthful in (((F(1, 8), F(5, 8), F(1, 4)), True),
                                 ((F(1, 2), F(1, 8), F(3, 8)), False)):
            credible = True
            for own, lie in product(levels, repeat=2):
                if own == lie:
                    continue
                truth_loss = lie_loss = F(0)
                for a, b in product(levels, repeat=2):
                    mass = masses[a-1] * masses[b-1]
                    truth_loss += mass * F(2)**(-max(own, a, b))
                    reports = (lie, a, b)
                    largest = max(reports)
                    winners = [i for i, x in enumerate(reports) if x == largest]
                    lie_loss += mass * sum(
                        F(2)**(-largest - (3*(own-lie) if i == 0 else 0))
                        for i in winners) / len(winners)
                if lie_loss < truth_loss:
                    credible = False
            self.assertEqual(credible, truthful)

    def test_continuous_categories_are_best_responses(self):
        left, right = 0.25, 0.5
        for beta, count in ((0.5, 2), (0.8, 5)):
            role_ratio = (1 + beta**2) / (2*beta)
            angle = acos(1 / role_ratio)
            cutoff = acos(left/right * cos(angle/2))
            self.assertLess((count-0.5)*angle, cutoff)
            self.assertGreater((count+0.5)*angle, cutoff)
            bounds = [(left*sin((count-j)*angle) + right*sin(j*angle)) / sin(count*angle)
                      for j in range(count+1)]
            intervals = list(zip(bounds, bounds[1:]))
            for index, (lo, hi) in enumerate(intervals):
                self.assertLess(lo, hi)
                for own in (lo+(hi-lo)/100, (lo+hi)/2, hi-(hi-lo)/100):
                    losses = []
                    for report in range(count):
                        loss = 0.0
                        for rival, (a, b) in enumerate(intervals):
                            chance = 1 if report < rival else (0.5 if report == rival else 0)
                            loss += (b-a)*(chance*own + (1-chance)*role_ratio*(a+b)/2)
                        losses.append(loss)
                    self.assertEqual(min(range(count), key=losses.__getitem__), index)

    def test_deliberately_produced_collateral_and_mixed_contest(self):
        u = lambda income: 1-exp(-income)
        reserve = 0.045
        free_contest = -log((2+exp(-0.5))/3)
        reservation = free_contest-0.003
        required = 2*reservation-reserve
        for loss, extra_premium in ((0.6, 0.0), (0.8, 0.00170402), (1.5, 0.03144210)):
            chosen = max(0, (1-reserve/2-log(1+loss))/(1+loss+0.5))
            def cert_equiv(amount):
                winner = 1-(1+loss)*amount
                others = (reserve+amount)/2
                self.assertGreaterEqual(winner, others)
                return -log((exp(-winner)+2*exp(-others))/3)
            self.assertAlmostEqual(cert_equiv(chosen)-cert_equiv(max(chosen, required)),
                                   extra_premium, places=7)

        cash = 0.19
        critical = (u(reservation)-u(cash-reservation))/(u(cash+free_contest)-u(cash-reservation))
        mixed = (1+critical)/2
        self.assertLess(cash, 2*reservation)
        self.assertGreater(mixed*u(cash+free_contest)+(1-mixed)*u(cash-reservation),
                           u(reservation))
        self.assertGreater(1-mixed, 0.33)
        # Verify the two monotonic bound intervals in 152 independently.
        cash = 0.205
        pool_peace = u(cash/2)
        pool_fight = pool_peace/3 + (u(0.5)+u(cash))/3
        h = (pool_fight-u(reservation))/(pool_fight-pool_peace)
        self.assertLess(h, 0.757)
        self.assertLess(-log(1-0.757*u(0.256)-0.243*u(0.182)), 0.238)
        self.assertLess(-log((exp(-0.6)+2*exp(-0.205/2))/3), 0.243)


if __name__ == "__main__":
    unittest.main()
