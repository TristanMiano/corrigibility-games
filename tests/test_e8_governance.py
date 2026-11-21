"""Exact checks of E8's participation and scope comparisons."""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb, log
import unittest


def subsets(sites):
    for count in range(1, len(sites)):
        yield from combinations(sites, count)


def ring_payoffs(fake, genuine_gate, fake_gate, n, benefit, cost, setup):
    """Compute private gains by summing scheduled edges, including the donor's cost."""
    payoff = [F(0) if site in fake else -setup for site in range(n)]
    for donor in range(n):
        recipient = (donor + 1) % n
        if donor not in fake:
            probability = (fake_gate if recipient in fake else genuine_gate) / n
            payoff[donor] -= cost * probability
            payoff[recipient] += benefit * probability
    return payoff


class GovernanceChecks(unittest.TestCase):
    def test_urgent_report_disposal(self):
        weights = (1, 4, 4, 1)
        for high in (F(3, 2), F(2), F(3)):
            returns = []
            for unanimous_delivery in (0, 1):
                s = F(unanimous_delivery)
                low = (F(1, 3), F(0), (7+2*s)/12)
                high_share = (1, (5-2*s)/24, s/3)
                gain = [a-b for a, b in zip(high_share, low)]
                self.assertEqual(sum(comb(2, i)*weights[i]*gain[i] for i in range(3)), 0)
                self.assertGreater(sum(comb(2, i)*weights[i+1]*gain[i] for i in range(3)), 0)
                value = F(0)
                for states in product((False, True), repeat=3):
                    count = sum(states)
                    if count:
                        value += weights[count] * count * high_share[count-1] * high / 26
                    if count < 3:
                        value += weights[count] * (3-count) * low[count] / 26
                returns.append(value)
            self.assertEqual(returns[0]-returns[1], (high-2)/26)

    def test_applicants_costed_date_certificate(self):
        law_a, law_b = (53, 23, 29, 47), (47, 29, 23, 53)
        for pair in product((0, 1), repeat=2):
            self.assertEqual(sum(law_a[sum(pair)+bit] for bit in (0, 1)),
                             sum(law_b[sum(pair)+bit] for bit in (0, 1)))
        good = [sum(F(comb(3, k)*law[k], 256) for k in (1, 3)) for law in (law_a, law_b)]
        self.assertEqual(good, [F(29, 64), F(35, 64)])
        prior_b = F(49, 100)
        for available_dates in (1, 4, 5):
            found_a, found_b = [1-(1-prob)**available_dates for prob in good]
            self.assertEqual(prior_b*found_b > (1-prior_b)*found_a, available_dates < 5)
        pair_loss, solo_loss, difference = F(31007, 38400), F(5, 6), F(3, 1202)
        acquire_loss = F(0)
        for prior, success, trio in ((1-prior_b, good[0], pair_loss*(1+difference)),
                                     (prior_b, good[1], pair_loss*(1-difference))):
            acquire_loss += prior*(success*trio+(1-success)*solo_loss)
        self.assertGreater(log(solo_loss/acquire_loss), 0.004)

    def test_ring_side_agreements_against_exhaustive_deviations(self):
        for n in range(3, 7):
            sites = tuple(range(n))
            for fraction in (F(35, 100), F(45, 100)):
                genuine = (1+fraction)/2
                false = F(1, 20) + F(19, 20)*fraction
                setup = F(66, 100*n)
                base = ring_payoffs((), genuine, false, n, 6, 1, setup)
                best = None
                for group in subsets(sites):
                    for size in range(1, len(group)+1):
                        for fakes in combinations(group, size):
                            deviating = ring_payoffs(fakes, genuine, false, n, 6, 1, setup)
                            gain = sum(deviating[i]-base[i] for i in group)
                            best = gain if best is None else max(best, gain)
                self.assertEqual(best > 0, fraction == F(45, 100))
                if fraction == F(45, 100):
                    theta = F(15, 100)
                    closed_pay = genuine*theta/(genuine-false)
                    open_pay = -(1-genuine)*theta/(genuine-false)
                    self.assertEqual((1-genuine)*closed_pay+genuine*open_pay, 0)
                    self.assertEqual((1-false)*closed_pay+false*open_pay, theta)
                    single = ring_payoffs((1,), genuine, false, n, 6, 1, setup)
                    self.assertGreater(single[0]-theta/n, base[0])
                    self.assertGreater(single[1]+theta/n, base[1])

    def test_future_partner_and_funded_release(self):
        outcomes = ((F(142, 100), F(1332, 1000)), (F(1592, 1000), F(6032, 10000)))
        delta = F(85, 100)
        b_reservation = 2*delta/(2-delta)
        a_fallback = delta*F(155, 100)/(2-delta)
        for price, predicted in ((F(1, 9), 2), (F(5, 13), 1), (F(2), 0)):
            values = [a_fallback] + [a-price*(b_reservation-b) for a, b in outcomes]
            route = max(range(3), key=values.__getitem__)
            self.assertEqual(route, predicted)
            if route:
                self.assertGreater(values[route], delta*(F(155, 100)+values[route])/2)
            self.assertEqual(b_reservation, delta*(2+b_reservation)/2)

    def test_funded_search_and_asymptotic_information_budget(self):
        loads = ((F(1, 2), F(3, 20)), (F(19, 20), F(17, 20)))
        all_low = [sum(weight*(1-load)**k for load, weight in loads) for k in range(9)]
        search = [1-all_low[m+1]-F(2, 25)*sum(all_low[:m]) for m in range(8)]
        ordinary = F(17, 20) + (1-F(17, 19))/2
        self.assertLess(search[1], search[0])
        self.assertEqual(max(range(8), key=search.__getitem__), 7)
        self.assertGreater((search[7]-ordinary)/8, F(15, 100000))

    def test_coalition_schedule_by_actual_recipient_probabilities(self):
        delta, x, q, cost = F(3, 4), F(1), F(19, 100), F(1, 10)
        values = (F(12, 100), F(16, 100), q, q, F(34, 100))
        self.assertEqual(sum(values), x)
        future = [F(0)]*5
        for winner, chance in ((1, F(7, 45)), (2, F(19, 45)), (3, F(19, 45))):
            next_values = [F(16, 100), q, q, q, F(12, 100)]
            next_values[winner] = F(34, 100)
            for i, value in enumerate(next_values):
                future[i] += chance*value
        self.assertEqual(tuple(delta*v + ((1-delta)*x if i == 4 else 0)
                               for i, v in enumerate(future)), values)
        for group in subsets(tuple(range(5))):
            sincere = sum(values[i] for i in group)
            initiating = (1-delta)*(len(group)*q-cost) + delta*sincere
            self.assertGreaterEqual(sincere, initiating)
        shorter = F(74, 100)
        lowest = x-(4*q-cost)/shorter
        self.assertGreaterEqual(lowest, q-cost)
        self.assertLess(lowest*(1+1/shorter), 2*q-cost)

    def test_partial_renewal_has_strict_obedience(self):
        x, q, d, delta = F(7, 10), F(1, 5), F(4, 25), F(11, 20)
        served, earlier, last = F(1681, 2550), F(97, 255), F(919, 2550)
        self.assertEqual(served, (x+q)/2+delta*earlier)
        self.assertEqual(earlier, q/2+delta*(served+last)/2)
        self.assertEqual(last, d/2+delta*(served+last)/2)
        self.assertGreater(delta*(served-last), d)
        self.assertGreater(earlier, d+delta*last)
        self.assertGreater(served, d+delta*last)
        contest_floor = (2*d-delta*(x-d))/(2*q-delta*(x-d))
        self.assertEqual(contest_floor, F(23, 103))
        self.assertGreater(contest_floor*(x-3*q+(q-d))/(3*(1-delta)), F(17, 1000))

    def test_known_changers_receive_service(self):
        x, d, delta = F(7, 10), F(4, 25), F(2, 5)
        z = F(17, 100)
        switch = z*(1-delta)/(delta*(x-z))
        self.assertLess(switch, 1)
        self.assertEqual(z, delta*((1-switch)*z+switch*x))
        self.assertGreater(z, (1-delta)*d+delta*z)
        initial = F(48, 53)
        self.assertEqual(initial*z+(1-initial)*x, F(22, 100))
        self.assertEqual(initial*(x-z)/2, F(24, 100))
        self.assertLess(delta*x, 2*d)

    def test_scoped_information_price(self):
        s = F(1, 2)
        cells = ((F(9, 10), F(1, 10)), (F(1, 10), F(9, 10)))
        guarantee = sum(max(0, (1-s)*F(2, 19)*regular - s*outside/8)
                        for regular, outside in cells)
        # Enumerate the four deterministic ways to use the reading at both job tiers.
        candidates = []
        for policy in product((0, 1), repeat=2):
            totals = [F(0), F(0)]
            for accept, (regular, outside) in zip(policy, cells):
                for probability, outputs in ((F(12, 19), (-1, F(3, 4))),
                                             (F(7, 19), (2, -1))):
                    for i, value in enumerate(outputs):
                        totals[i] += (1-s)*regular*probability*accept*value
                for i in range(2):
                    totals[i] -= s*outside*accept/8
            candidates.append(min(totals))
        self.assertEqual(guarantee, max(candidates))
        self.assertGreater(guarantee - F(12, 1000) - F(20, 1000), F(5, 1000))
        self.assertLessEqual((1-s)*F(2, 19)-s/8, 0)


class RenewalAndCapacityTests(unittest.TestCase):
    def test_noisy_reports_and_actual_configuration_choice(self):
        x, q, d = F(7, 10), F(1, 5), F(4, 25)
        reservation, price, setup = F(14, 75), F(1, 25), F(1, 2000)
        damage = x-3*q+(q-d)
        for accuracy, winner in ((F(3, 4), 0), (F(39, 50), 1),
                                 (F(4, 5), 2), (F(9, 10), 3)):
            stake_slope = d*accuracy+(x-d)*(1-accuracy)
            floor = (d*accuracy-price)/stake_slope
            for count in range(4):
                ordinary = 3-count
                shares = ordinary*max(floor, reservation/x)+count*(reservation+setup)/x
                if count == winner:
                    self.assertLess(shares, 1)
                excess = ordinary*floor+count*reservation/x-1
                necessary_conflict = max(0, excess/(ordinary*q/stake_slope+count*q/x))
                required = count*setup+damage*necessary_conflict
                if count != winner:
                    self.assertGreater(required, winner*setup)

    def test_public_diagnostic_and_alternative_release_costs(self):
        x, q, d = F(7, 10), F(1, 5), F(4, 25)
        price, outside = F(9, 100), F(14, 75)
        self.assertLess(1-price/d+2*outside/x, 1)
        certificate_bound = (1-price/q+2*outside/x-1)/(1+2*q/x)
        self.assertEqual(certificate_bound, F(7, 132))
        self.assertGreater((x-3*q+(q-d))*certificate_bound, F(5, 1000))
        self.assertGreater(q/(x-2*q+q-d), d/(x-2*q))

    def test_meter_and_restore_options_are_physically_funded(self):
        x, q, d, p = F(7, 10), F(1, 5), F(4, 25), F(2, 5)
        self.assertEqual((2*d-p*(x-d))/(1-p), F(13, 75))
        self.assertEqual(((q+d)-p*(x-d))/(1-p), F(6, 25))
        transfer = F(1, 10)
        risk = (2*d-(1-p)*transfer-p*(x-d))/((1-p)*(2*q-transfer)-p*(x-3*q+q-d))
        self.assertEqual(risk, F(11, 31))
        self.assertGreater(risk*(x-3*q+q-d)/(1-p), F(6, 100))
        conversion = F(6, 5)
        partial = F(65, 100)
        retention = d-F(2, 100)/(1-partial*conversion)
        self.assertEqual(retention, F(19, 275))
        self.assertLess((1-partial*conversion)*d, F(4, 100))
        self.assertLess(F(15, 1000), F(8, 1000)+(conversion-1)*retention)

    def test_downstream_private_draw_after_an_early_reading(self):
        x, q, d = F(7, 10), F(1, 5), F(4, 25)
        b, last, h = F(107, 570), F(10, 57), F(1, 25)
        contest = F(715, 2033)
        signal_mass = 3*contest/2
        first_loser = (b-contest*q)/x+contest*(1-d/x)
        last_loser = last/x
        self.assertGreater(first_loser, signal_mass*(1-d/x))
        self.assertGreater(last_loser, signal_mass*d/x)
        self.assertGreater((last-signal_mass*d)/(1-signal_mass), d)
        self.assertLess(F(2, 3)*q, d)
        self.assertEqual(d*(first_loser+last_loser)-q*contest, h)
        self.assertGreater((b+last-x*h/d)/(2*q), contest)

    def test_contingent_future_work_recovers_current_peace(self):
        x, q, d, h = F(7, 10), F(1, 5), F(4, 25), F(1, 25)
        b, last = F(107, 570), F(10, 57)
        denominator = q-d+d*(q+d)/x
        budget = d*(b+last)/x-h
        self.assertEqual(budget, F(143, 3325))
        for resource in (F(0), budget/3, budget):
            contest = (budget-resource)/denominator
            intact = ((b-contest*q)/x, (last-contest*d)/x)
            gains = (d*(intact[0]+contest)-q*contest, d*intact[1])
            bonuses = [resource*g/(h+resource) for g in gains]
            self.assertGreater(min(intact), 0)
            self.assertGreater(min(gains), 0)
            self.assertEqual(sum(bonuses), resource)
            self.assertEqual(sum(g-bonus for g, bonus in zip(gains, bonuses)), h)
            self.assertEqual(x*intact[0]+contest*q, b)
            self.assertEqual(x*intact[1]+contest*d, last)
        self.assertEqual(1+h/budget, F(276, 143))

    def test_multi_owner_full_service_and_partial_bounds(self):
        x, q, d = F(7, 10), F(1, 5), F(4, 25)
        base_share, fee, information = F(4, 15), F(5, 1000), F(7, 16)
        new_share = base_share+fee/x
        for equipped, minimum in ((0, 0), (1, 0), (2, 1), (3, 2)):
            feasible = []
            for count in range(equipped+1):
                needed = (equipped-count)*information + count*new_share + (3-equipped)*base_share
                if needed <= 1:
                    feasible.append(count)
            self.assertEqual(min(feasible), minimum)
        loss = x-3*q+(q-d)
        two = (2*information+base_share-1)/(2*q/d+q/x)
        self.assertEqual(two, F(119, 2340))
        self.assertGreater(loss*two, fee)
        self.assertGreater(loss*(3*information-1)/(3*q/d), 2*fee)

    def test_wealth_funded_risk_and_inspection(self):
        # One rational tick is exp(-gamma * 0.02). The same stock pays all bills.
        for tick, outcome in ((F(99, 100), "change"), (F(49, 50), "ordinary"),
                              (F(9, 10), "no read"), (F(4, 5), "no initiative")):
            intact = 1-tick**35
            passive = (1-tick**30)/3
            initiate = 1-(1-passive)/tick**2
            if outcome == "no initiative":
                self.assertLess(initiate, 0)
                continue
            expense = passive-initiate
            price = 1-tick**2
            share = F(1, 3)
            option = (1-share)*initiate-price*(1-share*intact)
            if outcome == "no read":
                self.assertGreater(initiate, 0)
                self.assertGreater(share*intact, initiate)
                self.assertLess(option, 0)
                continue
            later = option/((1-share)*passive+price*(share*intact-passive))
            early = (1-share)*(share*intact-initiate)/(share*intact-(1-share)*initiate)
            second = early*passive+(1-early)*(initiate+later*expense)
            third = early*passive+(1-early)*initiate
            loss = intact-3*passive+expense
            ordinary_contest = (initiate*(second+third)/intact-price*(1-intact+second+third)) / (
                expense+initiate*(passive+initiate)/intact+price*loss)
            second_mass = (second-ordinary_contest*passive)/intact
            third_mass = (third-ordinary_contest*initiate)/intact
            first_mass = 1-ordinary_contest-second_mass-third_mass
            self.assertGreater(min(first_mass, second_mass, third_mass, ordinary_contest), 0)
            ordinary = first_mass*intact+passive*ordinary_contest
            self.assertGreater(ordinary, initiate)
            self.assertLess(ordinary_contest/(ordinary_contest+second_mass), initiate/passive)
            # Compare the observational deviation at its actual stock expense.
            inspected_gross = first_mass*intact+(1-first_mass)*initiate
            self.assertEqual(1-(1-inspected_gross)/tick**2, ordinary)
            installed = 1-(1-intact+second+third)/tick**2
            self.assertEqual(installed > ordinary, outcome == "change")

    def test_equal_load_quota_cancellation(self):
        weights = [F(4**(6-k) + 4*4**k, 5**7) for k in range(7)]
        mass = [comb(6, k)*w for k, w in enumerate(weights)]

        def incentives(high, served):
            low = [s-h for s, h in zip(served, high)]
            high_mass = sum(p*h for p, h in zip(mass, high))
            low_mass = sum(p*l for p, l in zip(mass, low))
            false_high = sum(mass[k]*high[k]*weights[k-1]/weights[k] for k in range(1, 7))
            false_low = sum(mass[k]*low[k]*weights[k+1]/weights[k] for k in range(6))
            return low_mass-false_high, high_mass-false_low, low_mass+25*high_mass

        high = [0, 0, 1, F(5, 2), 4, 5, 5]
        served = [F(5)]*7
        self.assertEqual(incentives(high, served), (0, F(9, 5), F(11689, 125)))
        high[2:4] = [F(23, 39), 3]
        served[2] = 4+high[2]
        self.assertEqual(incentives(high, served), (0, F(79173, 40625), F(3813261, 40625)))

    def test_named_unequal_calendar_and_conditional_renewal(self):
        recovery = F(1, 5)
        survival = F(9, 20)
        claims = [F(34, 100), F(19, 100), 0]
        floors = [(1-survival)*d/(1-recovery) for d in claims]
        free = 1-sum(floors)
        states = [[v+free*(i==j) for i, v in enumerate(floors)] for j in range(3)]
        for j, state in enumerate(states):
            next_values = [(v-(1-survival)*(i==j))/survival for i, v in enumerate(state)]
            lottery = [(w-a)/free for w, a in zip(next_values, floors)]
            self.assertGreaterEqual(min(lottery), 0)
            self.assertEqual(sum(lottery), 1)
            for i, v in enumerate(state):
                self.assertEqual(v, (1-survival)*(i==j)
                                 + survival*sum(prob*s[i] for prob, s in zip(lottery, states)))
                self.assertGreaterEqual(v, (1-survival)*claims[i]+recovery*v)

    def test_fixed_configuration_partial_conflict_bound(self):
        probabilities = [F(i, 100) for i in (39, 24, 12)]
        cost, survival = F(1, 20), F(7, 20)
        reservations = [q-cost/3 for q in probabilities]
        dispute_loss = 1-sum(probabilities)+cost
        bounds = {}
        for size in range(4):
            for changed in combinations(range(3), size):
                floors = [0 if i in changed else q-cost for i, q in enumerate(probabilities)]
                lower = []
                for j, floor in enumerate(floors):
                    salvage = sum(q for i, q in enumerate(probabilities) if i != j and i not in changed)
                    shortfall = max(0, sum(floors)-floor-survival*(1-floor))
                    lower.append(shortfall/((1-survival)*salvage) if salvage else 0)
                bound = (sum(g*r for g, r in zip(lower, reservations))
                         / (1+sum(g*q for g, q in zip(lower, probabilities))))
                bounds[changed] = dispute_loss*bound
        self.assertEqual(bounds[()], dispute_loss*F(305908, 2004651))
        self.assertEqual(bounds[(1,)], dispute_loss*F(119803, 2715768))
        self.assertEqual(bounds[(2,)], dispute_loss*F(101357, 1177812))
        for strong_cost, expected in ((F(8, 1000), (0,)), (F(18, 1000), (1, 2))):
            quotes = [strong_cost, F(5, 1000), F(5, 1000)]
            total = {c: lost+sum(quotes[i] for i in c) for c, lost in bounds.items()}
            self.assertEqual([c for c in total if total[c] == min(total.values())], [expected])
            self.assertEqual(bounds[expected], 0)


if __name__ == "__main__":
    unittest.main()
