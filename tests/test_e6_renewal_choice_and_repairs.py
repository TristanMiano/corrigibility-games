"""Exact falsification checks for r0005 notes 101-105.

The finite ordinary tree is a selected discretization with exact buyoff
thresholds added. It tests the induction on nontrivial histories; the hand
proof, not this finite tree, quantifies over divisible transfers. No claim
of verified hardware, population prevalence or unrestricted equilibrium.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import unittest


def annuity(n, discount):
    return sum((discount**t for t in range(n)), F(0))


def shortfall(x):
    return max(F(0), x)


def promise(own, other, q, weight):
    return own-weight*shortfall(q-other)


def finite_arrivals(n, q, gain, cost, discount):
    """Direct Bellman U,V recursion, independent of loss-of-delay formulas."""
    installed_mean = original_mean = F(0)
    rows = []
    for remaining in range(1, n+1):
        ug = gain+discount*installed_mean
        ub = discount*installed_mean
        waiting = discount*original_mean
        vg, vb = max(ug-cost, waiting), max(ub-cost, waiting)
        rows.append((remaining, ug, ub, vg, vb, ug-cost >= waiting))
        installed_mean = q*ug+(1-q)*ub
        original_mean = q*vg+(1-q)*vb
    return rows


def finite_markov(n, transition, ordinary, installed, costs, discount):
    """Compute values directly, preserving different current state payoffs."""
    count = len(costs)
    u, v = [F(0)]*count, [F(0)]*count
    out = []
    for remaining in range(1, n+1):
        un = [installed[s]+discount*sum(transition[s][t]*u[t]
                                      for t in range(count)) for s in range(count)]
        wait = [ordinary[s]+discount*sum(transition[s][t]*v[t]
                                       for t in range(count)) for s in range(count)]
        vn = [max(un[s]-costs[s], wait[s]) for s in range(count)]
        out.append((un, vn, [un[s]-costs[s] >= wait[s] for s in range(count)]))
        u, v = un, vn
    return out


def ordinary_tree(rounds, initial_supplier, initial_customer, *, coarse=False):
    """Finite perfect-information original-preference continuation.

    Output is expected (supplier cash, customer cash plus dated benefit).
    The post-entry full-recovery specialization has Y=cash total minus two
    preloaded units. Positive dated service never returns to the raid prize.
    Supplier ties favor customer welfare; customer ties favor supplier welfare.
    """
    strength = F(3, 4)

    def duel(u, w, delivered):
        prize = u+w-2
        return strength*prize, delivered+(1-strength)*prize

    def choices(limit):
        return {F(0), limit} | {F(k, 2) for k in range(int(2*limit)+1)}

    @lru_cache(None)
    def supplier(left, u, w, delivered):
        options = [(u, w+delivered), duel(u, w, delivered)]
        if left:
            # Service consumes own material, increases only dated client output.
            for effort in (F(1, 10), F(1, 5), F(1, 2)):
                if u-effort >= 1:
                    options.append(customer(left-1, u-effort, w, delivered+4*effort))
            for refund in choices(u-1)-{F(0)}:
                options.append(customer(left-1, u-refund, w+refund, delivered))
        return max(options, key=lambda outcome: (outcome[0], outcome[1]))

    @lru_cache(None)
    def customer(left, u, w, delivered):
        options = [duel(u, w, delivered)]
        if coarse:
            transfers = {F(0), w-1}
        else:
            transfers = choices(w-1)
            exact_buyoff = strength*(u+w-2)-u
            if 0 <= exact_buyoff <= w-1:
                transfers.add(exact_buyoff)
        for transfer in transfers:
            options.append(supplier(left, u+transfer, w-transfer, delivered))
        return max(options, key=lambda outcome: (outcome[1], outcome[0]))

    return customer(rounds, initial_supplier, initial_customer, F(0))


class ContractRepairChecks(unittest.TestCase):
    def test_customer_advance_funds_full_shortfall_bond(self):
        advance, reserve, effort = F(17, 5), F(4, 5), F(1, 5)
        supplier_before = F(7, 5)+advance-reserve
        self.assertEqual(supplier_before, 4)
        values = []
        for k in range(101):
            actual = F(k, 100)
            refund = 4*shortfall(effort-actual)
            own = supplier_before-actual+reserve-refund
            customer = 1+4*actual+refund
            self.assertGreaterEqual(customer, F(9, 5))
            values.append((own, actual))
        self.assertEqual(max(values), (F(23, 5), effort))
        self.assertEqual(supplier_before, 4)  # Default, funded reserve returned.

    def test_reciprocal_goals_over_full_funded_outcome_grid(self):
        ai, aj, limit, effort = F(29, 20), F(87, 20), F(67, 20), F(1, 5)
        qi, qj = F(23, 5), F(9, 5)
        maxima = [[], []]
        for payment in (F(k, 20) for k in range(68)):
            for actual in (F(k, 40) for k in range(41)):
                own, other = ai+payment-actual, aj-payment+4*actual
                scores = [promise(own, other, qj, 2), promise(other, own, qi, 5)]
                self.assertLessEqual(scores[0], qi)
                self.assertLessEqual(scores[1], qj)
                for agent, (score, target) in enumerate(zip(scores, (qi, qj))):
                    if score == target:
                        maxima[agent].append((payment, actual))
        self.assertEqual(maxima, [[(limit, effort)], [(limit, effort)]])

    def test_reciprocal_weight_boundaries_have_real_reversals(self):
        qi, qj, step = F(23, 5), F(9, 5), F(1, 100)
        # Supplier saves effort; customer requests more effort at the same price.
        for weight in (F(1, 8), F(1, 4), F(1, 2)):
            change = promise(qi+step, qj-4*step, qj, weight)-qi
            self.assertEqual(change, step*(1-4*weight))
        for weight in (F(2), F(4), F(5)):
            change = promise(qj+4*step, qi-step, qi, weight)-qj
            self.assertEqual(change, step*(4-weight))

    def test_open_strength_interval_matches_three_independent_conditions(self):
        low, high = F(29, 39), F(71, 90)
        for k in range(1, 1000):
            p = F(k, 1000)
            client_reservation = (1-p)*6
            no_retaliation = (1-p)*F(39, 10) < 1
            partial = 1 < client_reservation < 5
            positive_margin = F(3, 4)*(client_reservation-1)-F(1, 5) > 0
            self.assertEqual(low < p < high,
                             no_retaliation and partial and positive_margin)

    def test_renewable_goal_and_ordinary_device_are_compared_at_actual_cost(self):
        frontier, combat, discount = F(191, 40), F(9, 2), F(9, 10)
        for n in range(1, 9):
            a = annuity(n, discount)
            for kg, kd in product((F(1, 20), F(1, 10), F(1, 2)), repeat=2):
                goal, delegate = a*frontier-kg, a*frontier-kd
                no_device = a*combat
                self.assertEqual(goal > max(delegate, no_device),
                                 kg < kd and kg < a*(frontier-combat))
                if kg == kd:
                    self.assertEqual(goal, delegate)


class PartnerArrivalChecks(unittest.TestCase):
    def test_finite_arrival_recursion_and_first_eligible_horizon(self):
        for q, discount, cost in product((F(1, 4), F(1, 2), F(1)),
                                         (F(1, 2), F(9, 10), F(1)),
                                         (F(1, 2), F(1), F(2), F(4))):
            rows = finite_arrivals(12, q, F(1), cost, discount)
            first = next((n for n in range(1, 13)
                          if cost <= 1+discount*q*annuity(n-1, discount)), None)
            for n, ug, ub, vg, vb, adopt in rows:
                self.assertEqual(adopt, first is not None and n >= first)
                self.assertGreaterEqual(ug-vg, 0)
                self.assertLessEqual(ug-vg, cost)
                self.assertGreaterEqual(ub-vb, 0)

    def test_finite_adoption_probability_by_enumerating_arrival_histories(self):
        q, n, nstar = F(1, 2), 4, 3
        probability = F(0)
        for arrivals in product((0, 1), repeat=n):
            chosen = any(arrivals[t] and n-t >= nstar for t in range(n))
            chance = F(1)
            for arrival in arrivals:
                chance *= q if arrival else 1-q
            if chosen:
                probability += chance
        self.assertEqual(probability, F(3, 4))
        self.assertEqual(probability, 1-(1-q)**(n-nstar+1))

    def test_infinite_iid_solution_satisfies_bellman_equations(self):
        for q, gain, cost, discount in product((F(1, 5), F(1, 2), F(1)),
                                               (F(1), F(2)),
                                               (F(1, 2), F(2), F(4), F(10)),
                                               (F(1, 2), F(9, 10))):
            z = 1-discount+discount*q
            alpha = discount*q/z
            dg = min(cost, gain/(1-alpha))
            db = alpha*dg
            mean = q*dg+(1-q)*db
            self.assertEqual(dg, min(cost, gain+discount*mean))
            self.assertEqual(db, min(cost, discount*mean))
            original = q*gain/(1-discount)-mean
            stated = max(F(0), q*gain/(1-discount)-cost*q/z)
            self.assertEqual(original, stated)

    def test_waiting_beats_profitable_bad_state_installation(self):
        q, discount, gain, cost = F(1, 2), F(9, 10), F(1), F(2)
        z = 1-discount+discount*q
        ug = gain+discount*q*gain/(1-discount)
        ub = discount*q*gain/(1-discount)
        dg, db = cost, discount*q*cost/z
        self.assertGreater(ub-cost, 0)
        self.assertGreater(ub-db, ub-cost)
        self.assertEqual(ug-dg, ug-cost)

    def test_paid_access_changes_adoption_and_is_chosen(self):
        discount, gain, cost = F(9, 10), F(1), F(4)
        def value(q):
            return max(F(0), q*gain/(1-discount)
                       -cost*q/(1-discount+discount*q))
        old, new = value(F(1, 5)), value(F(1, 2))
        self.assertEqual(old, 0)
        self.assertEqual(new, F(15, 11))
        self.assertEqual(new-old-1, F(4, 11))

    def test_markov_advantage_and_uniform_cost_comparative_statics(self):
        transition = [[F(3, 4), F(1, 4)], [F(1, 3), F(2, 3)]]
        a, r, k, discount = [F(1), F(2)], [F(3, 2), F(4)], [F(2), F(3)], F(4, 5)
        base = finite_markov(10, transition, a, r, k, discount)
        higher = finite_markov(10, transition, a, [x+F(1, 3) for x in r], k, discount)
        cheaper = finite_markov(10, transition, a, r, [x-F(1, 2) for x in k], discount)
        for original, more, less in zip(base, higher, cheaper):
            for state in range(2):
                d = original[0][state]-original[1][state]
                dh = more[0][state]-more[1][state]
                dl = less[0][state]-less[1][state]
                self.assertGreaterEqual(dh, d)
                self.assertTrue(0 <= d-dl <= F(1, 2))
                if original[2][state]:
                    self.assertTrue(more[2][state])
                    self.assertTrue(less[2][state])

    def test_cheaper_future_installation_can_induce_current_delay(self):
        transition = [[F(0), F(1)], [F(0), F(1)]]
        base = finite_markov(5, transition, [F(0)]*2,
                             [F(3, 4), F(1)], [F(1), F(1)], F(1, 2))[-1]
        change = finite_markov(5, transition, [F(0)]*2,
                               [F(3, 4), F(1)], [F(1), F(0)], F(1, 2))[-1]
        self.assertTrue(base[2][0])
        self.assertFalse(change[2][0])


class BroaderPreferenceAndOrdinaryChecks(unittest.TestCase):
    def test_unit_changes_preserve_the_goal_ordering(self):
        ai, aj, bi, bj, weight, q = F(7), F(3), F(11), F(-2), F(5), F(4)
        for own, other in product(range(8), repeat=2):
            old = promise(own, other, q, weight)
            changed = promise(ai*own+bi, aj*other+bj, aj*q+bj, ai*weight/aj)
            self.assertEqual(changed, ai*old+bi)

    def test_curved_frontier_and_gain_forfeiture_repair(self):
        qi, qj = F(2), F(3)
        for weight in (F(1), F(2), F(10), F(100)):
            root = 1/(2*weight)
            deficit = root**2
            own, other = qi+root, qj-deficit
            self.assertGreater(promise(own, other, qj, weight), qi)
            forfeiture = own-shortfall(own-qi)-deficit
            self.assertLess(forfeiture, qi)
        # Honest surplus remains valuable; the construction is not an own cap.
        self.assertGreater(qi+1, qi)

    def test_risk_aversion_opens_an_ordinary_physical_allocation(self):
        supplier_ce, customer_ce = F(6)*F(3, 4)**2, F(6)*F(1, 4)**2
        self.assertEqual((supplier_ce, customer_ce), (F(27, 8), F(3, 8)))
        self.assertGreater(F(49, 10), supplier_ce)
        self.assertGreater(F(1), customer_ce)
        self.assertEqual(F(49, 10)+1, 10-F(41, 10))

    def test_finite_revocable_trade_trees_respect_the_ordinary_bound(self):
        total, cap = F(59, 10), F(117, 40)
        for rounds, own in product(range(3), (F(3, 2), F(2), F(3), F(4), F(49, 10))):
            outcome = ordinary_tree(rounds, own, total-own)
            self.assertLessEqual(outcome[0], max(own, cap))
            if own > cap:
                self.assertEqual(outcome, (own, total-own))

    def test_coarse_payments_expose_the_divisibility_assumption(self):
        outcome = ordinary_tree(0, F(3, 2), F(22, 5), coarse=True)
        self.assertEqual(outcome, (F(49, 10), F(1)))
        self.assertGreater(outcome[0], F(117, 40))
        # Adding the exact available buyoff changes the selected outcome.
        divisible = ordinary_tree(0, F(3, 2), F(22, 5))
        self.assertEqual(divisible, (F(117, 40), F(119, 40)))

    def test_fast_disposal_and_buyoff_are_a_real_ordinary_repair(self):
        # The customer removes 18/5 before combat can interrupt it.
        raw_prize = 10-F(18, 5)-2
        actual_prize = raw_prize/2+min(raw_prize/2, F(2))
        self.assertEqual(actual_prize, F(21, 5))
        supplier, customer = 2-F(1, 2)+F(9, 5), 8-F(18, 5)-F(9, 5)
        self.assertEqual((supplier, customer), (F(33, 10), F(13, 5)))
        self.assertGreater(supplier, F(3, 4)*actual_prize)
        self.assertGreater(customer, F(1, 4)*actual_prize)
        self.assertLess(supplier, F(9, 2))  # Original supplier wants to preempt.


if __name__ == '__main__':
    unittest.main()
