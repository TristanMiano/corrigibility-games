"""Finite checks for E8. Run with python -m unittest discover -s tests -p test_e8_formation.py."""
from fractions import Fraction as F
from itertools import product
from math import exp, prod, sqrt
import unittest


def gate_boundary(honest_masses, fake_masses, expense):
    """Enumerate vertices of the box subject to one incentive constraint."""
    gains = [F(5, 3) * h - 2 * f for h, f in zip(honest_masses, fake_masses)]
    best = F(-1)
    for bits in product((F(0), F(1)), repeat=len(gains)):
        margin = sum(a * g for a, g in zip(bits, gains))
        opening = sum(a * h for a, h in zip(bits, honest_masses))
        if margin >= expense:
            best = max(best, opening)
        for index, gain in enumerate(gains):
            if gain == 0:
                continue
            change = (expense - margin) / gain
            if 0 <= bits[index] + change <= 1:
                best = max(best, opening + change * honest_masses[index])
    return best


class FormationChecks(unittest.TestCase):
    def test_search_selects_an_agreement_type(self):
        mass = {0: F(1, 2), 1: F(3, 10), 2: F(1, 5)}
        for stop_at, prob_goal, num_checks in ((1, F(21, 40), F(7, 4)),
                                                (2, F(387, 1000), F(61, 25))):
            counts = [F(0)] * 3
            total_checks = F(0)
            for offers in product(mass, repeat=3):
                weight = prod(mass[offer] for offer in offers)
                best = 0
                for checks, offer in enumerate(offers, start=1):
                    best = max(best, offer)
                    if best >= stop_at:
                        break
                counts[best] += weight
                total_checks += checks * weight
            self.assertEqual(counts[0], F(1, 8))
            self.assertEqual(counts[1], prob_goal)
            self.assertEqual(total_checks, num_checks)

    def test_recipient_gate_and_role_blind_frontier(self):
        honest = [F(0)] * 4
        fake = [F(0)] * 4
        for readings in product((False, True), repeat=3):
            honest[sum(readings)] += F(1, 8)
            fake[sum(readings)] += (F(1, 20) if readings[0] else F(19, 20)) / 4
        bound = gate_boundary(honest, fake, F(22, 100))
        role_bound = gate_boundary((F(1, 2), F(1, 2)), (F(19, 20), F(1, 20)), F(22, 100))
        self.assertLess(bound, F(569, 1000))
        self.assertEqual(role_bound, F(237, 320))
        self.assertLess(bound, F(725, 1000))
        self.assertGreater(role_bound, F(725, 1000))

    def test_two_readings_induce_broader_genuine_coverage(self):
        x = (1 + sqrt(0.68)) / 2.4
        real_read = 0.2 + 0.6 * x
        original = 5 * x * real_read / 3 - 0.4 * x**3
        self.assertAlmostEqual(1.2 * x**2, x - 1/15)
        self.assertGreater(F(2, 3) - F(5, 1000), original)
        self.assertLess(F(2, 3) - F(2, 100), original)
        # Concavity of the two-probe marginal payoff makes these endpoint bounds global.
        for endpoint in (F(0), F(1)):
            passing = F(1, 5) + F(3, 5) * endpoint
            derivative = (12 * F(3, 5) * passing - F(4, 5)**2) / 3 - F(6, 5) * endpoint**2
            self.assertGreater(derivative, 0)

    def test_true_scope_and_metered_endpoint_prices(self):
        for change_work, meter_b, number_changed in (
                (F(1, 20), F(1, 5), 2),
                (F(1, 20), F(1, 25), 1),
                (F(2, 5), F(1, 25), 0)):
            target = (F(1, 3) + change_work) / F(3, 5)
            sent = min(F(1), target)
            residual_cash = target - sent
            b_work = F(4, 5) * sent / 3
            common_cost = F(1, 50) + F(4, 5) * residual_cash
            costs = {
                "both genuine": common_cost + F(1, 100) + F(4, 3) * (b_work + F(1, 20)),
                "meter B": common_cost + meter_b + b_work,
                "meter C": F(1, 3) + F(1, 100),
                "cash to changed C": F(1, 50) + F(4, 5) * target,
            }
            actual = min(costs, key=costs.get)
            self.assertEqual(number_changed, {"both genuine": 2, "meter B": 1, "meter C": 0}[actual])

    def test_reserve_failure_known_before_release(self):
        success = F(17, 20)
        gross = F(0)
        for statuses in product((False, True), repeat=2):
            weight = prod(success if yes else 1-success for yes in statuses)
            net_reserve = sum(int(yes) - F(3, 2) for yes in statuses)
            output = 4 if all(statuses) else 0
            gross += weight * (net_reserve + output)
        honest = F(9, 10) * gross / 3 - F(1, 10)
        fake = F(1, 10) * success**2 * 6 / 3
        self.assertEqual(honest, F(377, 1000))
        self.assertEqual(fake, F(289, 2000))
        self.assertGreater(honest - F(1, 20), fake)

    def test_two_resource_bargaining_responses(self):
        constraints = ((2, 1, 1), (1, 2, 1))
        for delta in (F(0), F(1, 2), F(9, 10), F(99, 100)):
            expected = [a / (6 - delta) for a in (1, 1, 2)]
            reserves = [delta * value for value in expected]
            offers = []
            for proposer in range(3):
                extra = min((1 - sum(x * a for x, a in zip(reserves, row))) / row[proposer]
                            for row in constraints)
                offered = list(reserves)
                offered[proposer] += extra
                offers.append(offered)
                self.assertTrue(any(sum(x * a for x, a in zip(offered, row)) == 1
                                    for row in constraints))
            self.assertEqual(expected, [sum(col) / 3 for col in zip(*offers)])

    def test_exact_ordinary_cara_peace_frontier(self):
        u = lambda x: 1 - exp(-x)
        free_contest = (2*u(0) + u(0.5))/3
        own_contest = (2*u(-0.003) + u(0.497))/3
        from math import log
        d = -log(1 - own_contest)
        cash = 0.19
        after_late_dispute = (2*u(cash) + u(cash+0.5))/3
        p = (after_late_dispute - own_contest)/(after_late_dispute-u(cash-d))
        self.assertGreater(free_contest, own_contest)
        self.assertGreater(p, 0.663)
        self.assertLess(p, 0.665)
        self.assertAlmostEqual(p*u(cash-d) + (1-p)*after_late_dispute, own_contest)

    def test_buyer_and_original_welfare_have_different_optima(self):
        candidates = (F(0), F(1, 5), F(5, 9), F(1))
        for price, expected_p in ((1, F(1)), (F(8, 5), F(5, 9)), (F(9, 5), F(0))):
            buyer = {}
            group = {}
            for p in candidates:
                paid = F(4, 25)*p + max(0, p/5 - F(1, 25))
                capacity = max(F(4, 25), paid) if p else F(0)
                buyer[p] = p/2 - paid - (price-1)*capacity
                group[p] = F(14, 25) + F(7, 50)*p - (price-1)*capacity
            self.assertEqual(max(buyer, key=buyer.get), expected_p)
            if price == F(8, 5):
                self.assertEqual(max(group.values()), F(14, 25))
                self.assertGreater(F(7, 10) - 3*F(3, 100), max(group.values()))


if __name__ == "__main__":
    unittest.main()
