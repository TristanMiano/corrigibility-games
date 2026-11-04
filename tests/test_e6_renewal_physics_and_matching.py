"""Exact resource, funding, renewal and matching checks for r0005.

Independent enumerations check the analytic boundaries in 098-100. The
matching checks assume the stated transferable-surplus implementation
interface; neither they nor the payoff grids certify arbitrary hardware.
"""

from fractions import Fraction as F
from itertools import combinations, product
import unittest


def recovery_choices(ready, dispersed, raw, work, time, *, wx=2, tx=1,
                     repair_material=1, repair_work=1, repair_time=1):
    """Indivisible recovery/processing, with exact feasibility arithmetic."""
    out = []
    for repair in (0, 1):
        for recovered in range(int(dispersed)+1):
            for processed in range(int(raw)+1):
                if processed > repair*raw:
                    continue
                if ready+recovered < repair*repair_material:
                    continue
                spent_work = wx*recovered+repair_work*repair+processed
                spent_time = tx*recovered+repair_time*repair+processed
                if spent_work <= work and spent_time <= time:
                    final = ready+recovered-repair_material*repair+processed
                    out.append((final, recovered, repair, processed))
    return out


def matchings(rows, cols):
    """All matchings of small labeled bipartite sets, including exit."""
    if not rows:
        yield ()
        return
    first, *rest = rows
    yield from matchings(rest, cols)
    for col in cols:
        for tail in matchings(rest, [j for j in cols if j != col]):
            yield ((first, col),)+tail


def annuity(n, delta):
    return sum((delta**t for t in range(n)), F(0))


class PhysicalAndFundingChecks(unittest.TestCase):
    def test_initial_combat_prize_and_material_balance(self):
        values = recovery_choices(4, 4, 1, 4, 3)
        self.assertEqual(max(v[0] for v in values), 6)
        self.assertIn((6, 2, 0, 0), values)
        for final, recovered, repair, processed in values:
            remaining_dispersion = 4-recovered
            spent_material = 2+repair  # Two preloaded combat units.
            remaining_raw = 4-processed
            self.assertEqual(final+remaining_dispersion+spent_material+remaining_raw,
                             2+8+4)

    def test_work_time_dispersion_and_repair_variations(self):
        for time in range(1, 7):
            maxima = [max(x[0] for x in recovery_choices(4, 4, 1, work, time))
                      for work in range(9)]
            self.assertEqual(maxima, sorted(maxima))
        for work in range(9):
            maxima = [max(x[0] for x in recovery_choices(4, 4, 1, work, time))
                      for time in range(7)]
            self.assertEqual(maxima, sorted(maxima))
        values = [max(x[0] for x in recovery_choices(8-d, d, 1, 4, 3))
                  for d in (0, 2, 4, 6, 8)]
        self.assertEqual(values, sorted(values, reverse=True))
        # A different declared technology makes repair strictly useful.
        choices = recovery_choices(4, 4, 3, 6, 5, wx=4)
        best = max(x[0] for x in choices)
        self.assertEqual(best, 6)
        self.assertTrue(all(x[2] == 1 for x in choices if x[0] == best))

    def test_ordinary_division_boundary_against_all_tenth_unit_shares(self):
        stock, prize, chance = F(10), F(6), F(3, 4)
        reservations = (chance*prize, (1-chance)*prize)
        for expense in (F(3), F(4), F(41, 10), F(5)):
            residual = stock-expense
            feasible = []
            for k in range(int(residual*10)+1):
                a = F(k, 10)
                b = residual-a
                if a >= reservations[0] and b >= reservations[1]:
                    feasible.append((a, b))
            self.assertEqual(bool(feasible), expense <= stock-prize)

    def test_original_full_service_fixture_is_funded_opportunity(self):
        ri, rj, hi, hj, setup, price, b, c = map(
            F, (2, 8, "1/2", "9/2", "1/2", "5/2", 4, 1))
        own = ri-hi-setup-c+price
        other = rj-hj-price+b
        self.assertEqual((own, other), (F(5, 2), F(5)))
        self.assertGreater(own, F(2, 5)*6)
        self.assertGreater(other, F(3, 5)*6)
        self.assertLessEqual(hi+setup, ri-1)
        self.assertLessEqual(price, rj-hj-1)
        # But a no-service branch with only one unit left invites retaliation.
        self.assertGreater(F(3, 5)*F(5, 2), 1)

    def test_repaired_partial_service_and_all_attack_upper_bounds(self):
        ri, rj = F(2), F(8)
        hi, hj, setup = F(1, 2), F(18, 5), F(1, 10)
        price, effort, b, c, chance = F(17, 5), F(1, 5), F(4), F(1), F(3, 4)
        own = ri-hi-setup+price-c*effort
        other_cash = rj-hj-price
        other = other_cash+b*effort
        self.assertEqual((own, other), (F(23, 5), F(9, 5)))
        self.assertGreater(own, chance*6)
        self.assertGreater(other, (1-chance)*6)
        self.assertLessEqual(hi+setup, ri-1)
        self.assertEqual(price, rj-hj-1)
        max_cash_prize = ri+rj-hi-hj-2  # Generous, before setup/effort.
        self.assertEqual((1-chance)*max_cash_prize, F(39, 40))
        self.assertLess((1-chance)*max_cash_prize, 1)
        for completed in (F(k, 100) for k in range(21)):
            prize = ri+rj-hi-hj-setup-c*completed-2
            self.assertLess(chance*prize, own)
            self.assertLess(b*completed+(1-chance)*prize, other)

    def test_continuous_quality_optimum_and_strict_offer_grid(self):
        base, limit, before_client, reservation = F(7, 5), F(17, 5), F(22, 5), F(3, 2)
        b, c = F(4), F(1)
        effort = F(1, 8)
        self.assertEqual(base+limit-c*effort, F(187, 40))
        self.assertEqual(before_client-limit+b*effort, reservation)
        # Enumerate every fixed quality/price offer on the declared tenth grid.
        strict = []
        for e_units, p_units in product(range(11), range(35)):
            e, p = F(e_units, 10), F(p_units, 10)
            client = before_client-p+b*e
            if client > reservation:
                strict.append((base+p-c*e, e, p, client))
        optimum = max(x[0] for x in strict)
        self.assertEqual(optimum, F(23, 5))
        self.assertEqual([x[1:] for x in strict if x[0] == optimum],
                         [(F(1, 5), F(17, 5), F(9, 5))])

    def test_current_contract_goal_over_refunds_prices_and_all_efforts(self):
        base, client_before = F(7, 5), F(22, 5)
        promise, weight = F(9, 5), F(2)
        best = []
        for e_units, p_units in product(range(101), range(341)):
            effort, net_payment = F(e_units, 100), F(p_units, 100)
            own = base+net_payment-effort
            client = client_before-net_payment+4*effort
            goal = own-weight*max(F(0), promise-client)
            self.assertLessEqual(goal, F(23, 5))
            if goal == F(23, 5):
                best.append((effort, net_payment))
        self.assertEqual(best, [(F(1, 5), F(17, 5))])


class RenewableChoiceChecks(unittest.TestCase):
    def test_all_installation_dates_against_immediate_boundary(self):
        for n, delta, a, r, setup in product(
            range(1, 8), (F(1, 2), F(9, 10), F(1)),
            (F(0), F(2, 5)), (F(1, 2), F(1)), (F(1, 10), F(1), F(3))
        ):
            permanent = annuity(n, delta)*a
            options = [permanent]
            for when in range(n):
                options.append(annuity(when, delta)*a
                               + delta**when*(annuity(n-when, delta)*r-setup))
            predicted = permanent+max(F(0), annuity(n, delta)*(r-a)-setup)
            self.assertEqual(max(options), predicted)

    def test_new_partner_can_increase_or_decrease_update_advantage(self):
        horizon, cost = F(4), F(1)
        target, old_alternative = F(1, 2), F(0)
        self.assertGreater(horizon*(target-old_alternative)-cost, 0)
        new_ordinary_alternative = F(2, 5)
        self.assertLess(horizon*(target-new_ordinary_alternative)-cost, 0)
        better_goal_partner = F(1)
        self.assertGreater(horizon*(better_goal_partner-new_ordinary_alternative)-cost, 0)


class VoluntaryAssignmentChecks(unittest.TestCase):
    def test_certificate_against_every_coalition_and_matching(self):
        values = ((6, 4), (3, 5))
        u, w = (3, 2), (3, 3)
        for count_i, count_j in product(range(3), repeat=2):
            for rows in combinations(range(2), count_i):
                for cols in combinations(range(2), count_j):
                    possible = [sum(values[i][j] for i, j in m)
                                for m in matchings(list(rows), list(cols))]
                    endowed = sum(u[i] for i in rows)+sum(w[j] for j in cols)
                    self.assertLessEqual(max(possible), endowed)
        self.assertEqual(sum(u)+sum(w), 11)

    def test_a_core_split_still_needs_funding_and_can_be_repaired(self):
        # Provider cost two, customer liquid budget four. The first abstract
        # core split needs price five; a second core split fits the budget.
        values = ((6, 4), (3, 5))
        u, w = (F(3), F(2)), (F(3), F(3))
        self.assertGreater(2+u[0], 4)
        repaired_u, repaired_w = (F(2), F(1)), (F(4), F(4))
        for i, j in product(range(2), repeat=2):
            self.assertGreaterEqual(repaired_u[i]+repaired_w[j], values[i][j])
        self.assertEqual(sum(repaired_u)+sum(repaired_w), 11)
        self.assertTrue(all(2+gain <= 4 for gain in repaired_u))


if __name__ == "__main__":
    unittest.main()
