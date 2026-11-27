"""Regression checks for the denominators, physical fallbacks and equilibrium feedback in E9."""

from fractions import Fraction as F
import unittest

from experiments.r0008_verification_boundaries import (
    COST_CEILING, FALSE_POSITIVE, SENSITIVITY, TEST_PRICE, market, outcome,
)
from experiments.r0008_sequential_evidence import Job, equilibrium_rates, threshold_rule


class CommissioningTests(unittest.TestCase):
    def test_exact_cases(self):
        central = outcome(F(1, 2), F(4, 5))
        self.assertEqual((central.attempt, central.changed, central.deliberate), (F(4, 5), F(16, 25), F(1, 5)))
        self.assertEqual((central.confidence, central.combat), (F(16, 17), 0))
        powerful = outcome(F(4, 5), F(4, 5))
        self.assertEqual((powerful.attempt, powerful.confidence, powerful.combat), (1, F(36, 37), F(13, 50)))
        weak = outcome(F(1, 20), F(4, 5))
        self.assertEqual(weak.changed, F(7, 107))
        self.assertEqual(outcome(F(1, 100), F(1)).combat, 1)
        self.assertIsNone(outcome(F(1, 100), F(1)).confidence)

    def test_strategies_optimize_against_each_other(self):
        for power_index in range(1, 40):
            power = F(power_index, 40)
            m = market(power)
            for skill_index in range(1, 21):
                q = F(skill_index, 20)
                o = outcome(power, q)
                if o.policy == "no trade":
                    self.assertEqual(o.changed, 0)
                    self.assertFalse(m.active_interval and q * min(1, q * m.red_edit_premium / COST_CEILING) >= m.lower_prior)
                    continue
                audit = o.changed * SENSITIVITY * m.blue_gain - (1 - o.changed) * FALSE_POSITIVE * m.blue_loss - TEST_PRICE
                trust = o.changed * m.blue_gain - (1 - o.changed) * m.blue_loss
                self.assertGreaterEqual(audit, max(0, trust))
                if o.test < 1:
                    self.assertEqual(audit, trust)
                premium = o.test * m.red_edit_premium - 2 * (1 - o.test)
                self.assertEqual(o.attempt, min(1, max(0, q * premium / COST_CEILING)))
                self.assertEqual(o.changed, q * o.attempt)
                self.assertGreaterEqual(1, o.release + o.combat)
                self.assertGreaterEqual(o.release, o.genuine_service)

    def test_reliability_changes_the_sample_receiving_the_order(self):
        before, after = (outcome(F(4, 5), q) for q in (F(17, 20), F(1)))
        self.assertEqual(before.changed, F(103, 126))
        self.assertEqual(after.changed, before.changed)
        self.assertGreater(after.deliberate, before.deliberate)
        self.assertGreater(after.genuine_service, before.genuine_service)
        self.assertLess(after.confidence, before.confidence)
        self.assertLess(after.combat, before.combat)

    def test_affordable_inspection_can_change_combat_in_either_direction(self):
        differences = []
        for q in (F(3, 5), F(4, 5)):
            original = outcome(F(1, 20), q)
            cheaper = outcome(F(1, 20), q, price=F(9, 100))
            self.assertEqual((original.changed, cheaper.changed), (F(7, 107), F(9, 107)))
            differences.append(cheaper.combat - original.combat)
        self.assertGreater(differences[0], 0)
        self.assertLess(differences[1], 0)

    def test_optimal_sequence_of_readings(self):
        job = Job()
        selected = threshold_rule(4, 2)
        rate = job.genuine_rate(selected)
        self.assertEqual((selected.accept_genuine, selected.accept_retained), (F(272, 273), F(17, 273)))
        self.assertEqual(rate, F(1088, 1365))
        self.assertIn(rate, equilibrium_rates(job))

class GoalCertificateTests(unittest.TestCase):
    def test_impossible_histories_leave_an_independent_offset_free(self):
        from experiments.r0008_goal_equivalence import GoalTable, HistoryDomain, compare_preferences

        events = {"tick": ((0, 1, 0), (0, 0, 1), (0, 0, 1))}
        left = GoalTable((1, 0, 0), events, (0, F(1, 4), F(1, 2)))
        right = GoalTable((1, 0, 0), events, (0, F(1, 2), F(3, 4)))
        moves = {"new": {"tick": "running"}, "running": {"tick": "running"}}
        admitted = HistoryDomain("new", frozenset({"running"}), moves)
        self.assertIsNotNone(compare_preferences(left, right).witness)
        cert = compare_preferences(left, right, domain=admitted)
        self.assertEqual((cert.scale, cert.offset), (1, F(1, 4)))
        self.assertIn((), cert.basis_words)
        empty = HistoryDomain("new", frozenset(), moves)
        self.assertIsNone(compare_preferences(left, right, domain=empty).witness)
        malformed = HistoryDomain("new", frozenset({"running"}), {"new": {"tick": "absent"}})
        with self.assertRaises(ValueError):
            compare_preferences(left, right, domain=malformed)

    def test_preference_proofs_and_short_lottery_witnesses(self):
        from itertools import product
        from experiments.r0008_goal_equivalence import GoalTable, compare_preferences

        def table(terminal):
            # All three terminal states can be reached within two ticks.
            return GoalTable((1, 0, 0), {"tick": ((0, 1, 0), (0, 0, 1), (0, 0, 1))},
                             tuple(terminal))

        def ordering(machine, lotteries):
            x, y = (sum(weight * machine.score(word) for weight, word in lottery)
                    for lottery in lotteries)
            return (x > y) - (x < y)

        cases = list(product((F(0), F(1, 2), F(1)), repeat=3))
        for f, g in product(cases, repeat=2):
            left, right = table(f), table(g)
            cert = compare_preferences(left, right)
            if cert.witness is None:
                self.assertGreater(cert.scale, 0)
                self.assertEqual(tuple(cert.scale*v + cert.offset for v in f), g)
            else:
                self.assertNotEqual(ordering(left, cert.witness), ordering(right, cert.witness))
                for lottery in cert.witness:
                    self.assertEqual(sum(weight for weight, _ in lottery), 1)
                    self.assertTrue(all(weight > 0 and len(word) <= 4 for weight, word in lottery))
        aligned = compare_preferences(table((0, F(1, 2), 1)), table((F(1, 4), F(1, 2), F(3, 4))))
        self.assertEqual((aligned.scale, aligned.offset), (F(1, 2), F(1, 4)))
        nonlinear = compare_preferences(table((0, F(1, 2), 1)), table((0, F(4, 5), 1)))
        self.assertEqual(sorted(map(len, nonlinear.witness)), [1, 2])

    def test_distinct_representations_and_incomplete_proofs(self):
        from experiments.r0008_goal_equivalence import GoalTable, check_equality_proof, compare
        small = GoalTable((1, 0), {"tick": ((0, 1), (0, 1)), "hold": ((1, 0), (0, 1))},
                          (F(1, 4), F(3, 4)))
        split = GoalTable((1, 0, 0),
                          {"tick": ((0, 0, 1),) * 3,
                           "hold": ((F(1, 3), F(2, 3), 0), (1, 0, 0), (0, 0, 1))},
                          (F(1, 4), F(1, 4), F(3, 4)))
        proof = compare(small, split)
        self.assertIsNone(proof.witness)
        self.assertTrue(check_equality_proof(small, split, reversed(proof.basis_words)))
        self.assertFalse(check_equality_proof(small, split, iter([()])))
        self.assertFalse(check_equality_proof(small, split, [("unknown",)]))

    def test_single_exception_including_empty_history(self):
        from itertools import product
        from experiments.r0008_goal_equivalence import GoalTable, compare, point_exception
        letters = ("a", "b")
        base = GoalTable((1,), {s: ((1,),) for s in letters}, (F(1, 2),))
        for k in range(5):
            for trigger in product(letters, repeat=k):
                other = point_exception(trigger, letters)
                proof = compare(base, other)
                self.assertEqual(proof.witness, trigger)
                self.assertEqual((base.score(trigger), other.score(trigger)), (F(1, 2), 1))

    def test_independent_exhaustion_to_stochastic_witness_bound(self):
        from itertools import combinations_with_replacement, product
        from experiments.r0008_goal_equivalence import GoalTable, compare
        transitions = (
            ((1, 0), (0, 1)), ((0, 1), (1, 0)), ((0, 1), (0, 1)),
            ((F(1, 3), F(2, 3)), (F(1, 2), F(1, 2))),
        )
        machines = [GoalTable((1, 0), {"a": a, "b": b}, (0, 1))
                    for a, b in product(transitions, repeat=2)]
        words = [w for n in range(3) for w in product(("a", "b"), repeat=n)]
        for left, right in combinations_with_replacement(machines, 2):
            brute = next((w for w in words if left.score(w) != right.score(w)), None)
            certificate = compare(left, right)
            self.assertEqual(certificate.witness, brute)

    def test_sharp_runtime_error_and_holding_threshold(self):
        from experiments.r0008_goal_equivalence import GoalTable
        for leak in (F(1, 100), F(1, 50)):
            rho = F(9, 10)
            table = GoalTable((1, 0), {"hold": ((1-leak, leak), (1-rho-leak, rho+leak))}, (F(3, 5), 0))
            for k in (0, 1, 10, 11, 80):
                score = table.score(("hold",) * k)
                expected = F(3, 5) * (1 - leak * (1 - rho**k) / (1-rho))
                self.assertEqual(score, expected)
                self.assertEqual(score > F(13, 25), leak == F(1, 100) or k <= 10)


class ReceiptGameTests(unittest.TestCase):
    def test_complete_strategies_recover_all_three_productive_rates(self):
        from experiments.r0008_receipt_game import complete_plans, equilibrium_intervals

        price = F(1, 5)
        rates = [F(0), F(5, 302), F(166, 375), F(10, 19), F(15, 26)]
        self.assertEqual(equilibrium_intervals(price), [(f, f) for f in rates])
        plans = complete_plans(price)
        values = [max(plan.buyer_value(f) for plan in plans) for f in rates]
        self.assertEqual(values, [0, 0, F(48257, 46875), F(117, 95), F(89, 65)])

    def test_price_branches_against_complete_plan_enumeration(self):
        from experiments.r0008_receipt_game import equilibrium_intervals

        a, e = F(166, 375), F(44, 75)
        def after_pass(f):
            return 9 * (5 - 4 * f) / (25 * (8 * f + 1))
        def after_failure(f):
            return (116 * f - 45) / (25 * (9 - 8 * f))

        prices = {F(k, 100) for k in range(31)}
        prices.update([after_failure(a), F(9, 50), after_failure(e), after_pass(a)])
        for c in prices:
            with self.subTest(price=c):
                productive = set()
                from_pass = (45 - 25*c) / (36 + 200*c)
                from_failure = (45 + 225*c) / (116 + 200*c)
                if c <= after_failure(a) or F(9, 50) <= c <= after_failure(e):
                    productive.add(from_failure)
                if after_failure(a) <= c <= after_pass(a):
                    productive.add(a)
                if F(9, 50) <= c <= after_pass(a):
                    productive.add(from_pass)
                if c >= after_failure(e):
                    productive.add(e)
                exact = [(lo, hi) for lo, hi in equilibrium_intervals(c) if hi > F(5, 68)]
                self.assertEqual(exact, [(f, f) for f in sorted(productive)])

    def test_full_disclosure_bond_against_raw_state_laws(self):
        from experiments.r0008_receipt_game import Q, SIGN_LAWS

        p_h = [(Q*g + (1-Q)*m) / 100 for g, m in zip(*SIGN_LAWS[:2])]
        p_d = [F(d, 100) for d in SIGN_LAWS[2]]
        old, new = (1, 1, 0, 0), (1, 1, 1, 0)
        transfer = [F(16, 100), F(16, 100), F(-1, 10), F(-1, 10)]
        f = F(44, 75)
        def payoffs(decisions, fees):
            founder = []
            buyer = []
            for i, law in enumerate(SIGN_LAWS):
                founder.append(sum(F(w, 100) * ((2 if i == 0 else 4)*r + t)
                                   for w, r, t in zip(law, decisions, fees)))
                buyer.append(sum(F(w, 100) * ((4 if i == 0 else -2)*r - t)
                                 for w, r, t in zip(law, decisions, fees)))
            cutoff = Q*founder[0] + (1-Q)*founder[1] - founder[2]
            value = f*(Q*buyer[0] + (1-Q)*buyer[1]) + (1-f)*buyer[2]
            return cutoff, founder[2], value
        d_old, base_old, value_old = payoffs(old, [0]*4)
        d_new, base_new, value_new = payoffs(new, transfer)
        self.assertEqual(d_old, d_new)
        self.assertEqual(base_new-base_old, F(143, 500))
        self.assertEqual(value_new-value_old, F(1657, 37500))
        for s, release in enumerate(new):
            mass = f*p_h[s] + (1-f)*p_d[s]
            posterior = f*Q*F(SIGN_LAWS[0][s], 100)/mass
            gain = 6*posterior-2
            temptation = max(0, -gain if release else gain)
            self.assertGreater(F(72, 100) - transfer[s], temptation)
