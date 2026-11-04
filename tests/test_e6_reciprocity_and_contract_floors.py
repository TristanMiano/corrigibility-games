"""Exact finite falsification checks for r0005 notes 094-097.

These enumerate outcome/effort grids independently of the displayed analytic
thresholds. They support the hand proofs; they are not machine-checked proofs
or a simulator of every implementation, threat, or matching continuation.
"""

from fractions import Fraction as F
import unittest


def positive(x):
    return max(F(0), x)


def fairness(own, other, alpha, beta):
    return own - alpha * positive(other-own) - beta * positive(own-other)


def floor_goal(own, other, promised, weight):
    return own - weight * positive(promised-other)


class ReciprocalProductionChecks(unittest.TestCase):
    def test_last_mover_threshold_and_genuine_reversal(self):
        for b in (F(2), F(3), F(5)):
            c = F(1)
            for beta in (F(1, 10), c/(b+c), F(1, 2), F(3, 4)):
                for alpha in (F(0), F(1, 2), F(2)):
                    supply = fairness(b-c, b-c, alpha, beta)
                    keep = fairness(b, -c, alpha, beta)
                    self.assertEqual(supply-keep, beta*(b+c)-c)
                    if beta > c/(b+c):
                        self.assertGreater(supply, keep)
                        self.assertGreater(b, b-c)  # Original F reverses this.
                    after_refusal = fairness(-c, b, alpha, beta)
                    self.assertLess(after_refusal, fairness(0, 0, alpha, beta))

    def test_wealth_reciprocity_band_including_both_responses(self):
        b, c = F(3), F(1)
        for alpha in (F(0), F(1, 2), F(2)):
            for beta in (F(1, 3), F(1, 2), F(3, 4)):
                lo = (c-beta*(b+c))/(alpha+beta)
                hi = (c+alpha*(b+c))/(alpha+beta)
                self.assertEqual(hi-lo, b+c)
                grid = [F(k, 4) for k in range(-32, 33)] + [lo, hi]
                for d in grid:
                    own, other = 20+d, F(20)
                    return_gain = (
                        fairness(own+b-c, other+b-c, alpha, beta)
                        - fairness(own+b, other-c, alpha, beta)
                    )
                    gift_gain = (
                        fairness(own-c, other+b, alpha, beta)
                        - fairness(own, other, alpha, beta)
                    )
                    self.assertEqual(return_gain > 0, d > lo)
                    self.assertEqual(gift_gain < 0, d < hi)

    def test_continuous_effort_best_response_on_exact_grid(self):
        b, c = F(3), F(1)
        grid = [F(k, 20) for k in range(21)]
        for cap in (F(0), F(1, 5), F(1, 2), F(1)):
            beta = c*cap/(b+c*cap)
            for alpha in (F(0), F(1, 2), F(2)):
                for partner_effort in grid:
                    values = {}
                    for own_effort in grid:
                        own = b*partner_effort-c*own_effort**2/2
                        other = b*own_effort-c*partner_effort**2/2
                        values[own_effort] = fairness(own, other, alpha, beta)
                    best = [e for e, value in values.items()
                            if value == max(values.values())]
                    self.assertEqual(best, [min(partner_effort, cap)])

    def test_coordination_threshold_uses_expected_utility_not_mean_payoff(self):
        b, c = F(3), F(1)
        for alpha in (F(0), F(1, 2), F(1)):
            for beta in (F(1, 3), F(3, 4)):
                q_star = (c+alpha*(b+c))/((alpha+beta)*(b+c))
                for q in (F(0), F(1, 4), q_star, F(3, 4), F(1)):
                    if not 0 <= q <= 1:
                        continue
                    cooperate = (
                        q*fairness(b-c, b-c, alpha, beta)
                        + (1-q)*fairness(-c, b, alpha, beta)
                    )
                    defect = q*fairness(b, -c, alpha, beta)
                    self.assertEqual(cooperate > defect, q > q_star)
                    self.assertEqual(cooperate == defect, q == q_star)
                self.assertEqual(q_star < F(1, 2),
                                 (beta-alpha)*(b+c) > 2*c)


class PrepaymentAndRevisionChecks(unittest.TestCase):
    def test_delivery_and_participation_are_separate_thresholds(self):
        b, c = F(3), F(1)
        for alpha in (F(0), F(1, 2), F(2)):
            for beta in (F(1, 3), F(1, 2), F(3, 4)):
                p_ic = (c+alpha*(b+c))/(2*(alpha+beta))
                p_ir = (c+alpha*(b+c))/(1+2*alpha)
                grid = [F(k, 20) for k in range(61)] + [p_ic, p_ir]
                for p in grid:
                    work = fairness(p-c, b-p, alpha, beta)
                    keep = fairness(p, -p, alpha, beta)
                    self.assertEqual(work > keep, p > p_ic)
                    if p <= (b+c)/2:
                        self.assertEqual(work >= 0, p >= p_ir)
                self.assertEqual(p_ic > p_ir, beta < F(1, 2))

    def test_later_genuine_change_restores_delivery(self):
        work = (F(1, 2), F(3, 2))
        keep = (F(3, 2), F(-3, 2))
        old = [fairness(*x, F(0), F(3, 10)) for x in (work, keep)]
        new = [fairness(*x, F(0), F(2, 5)) for x in (work, keep)]
        self.assertEqual(old, [F(1, 2), F(3, 5)])
        self.assertEqual(new, [F(1, 2), F(3, 10)])
        self.assertGreater(old[0]-F(1, 10), 0)  # Old self approves before sale.
        self.assertGreater(new[0], new[1])     # New self supplies after payment.

    def test_extra_fee_is_profitable_under_simple_fairness(self):
        original_quote = fairness(F(1, 2), F(3, 2), 0, F(2, 5))
        revised_quote = fairness(F(3, 4), F(5, 4), 0, F(2, 5))
        self.assertEqual(revised_quote-original_quote, F(1, 4))
        self.assertGreater(revised_quote-F(1, 10), original_quote)
        # This is the old evaluator's comparison, conditional on a feasible
        # recognized demand goal and the customer's actual willingness to pay.

    def test_partner_order_can_differ_from_original_order(self):
        a, b = (F(3), F(0)), (F(2), F(2))
        self.assertGreater(a[0], b[0])
        self.assertLess(fairness(*a, 0, F(2, 5)),
                        fairness(*b, 0, F(2, 5)))


class ContractualFloorChecks(unittest.TestCase):
    def test_full_frontier_including_negative_gains_and_transfers(self):
        total, promised, weight = F(2), F(3, 2), F(3, 2)
        benchmark = total-promised
        grid = [F(k, 4) for k in range(-16, 33)]
        for own in grid:
            for other in grid:
                if own+other > total:
                    continue
                value = floor_goal(own, other, promised, weight)
                self.assertLessEqual(value, benchmark)
                if other < promised:
                    self.assertLess(value, benchmark)
                if value == benchmark:
                    self.assertEqual((own, other), (benchmark, promised))

    def test_delivery_is_genuine_and_extra_charge_is_deterred(self):
        promised, weight = F(3, 2), F(2)
        work, keep = (F(1, 2), F(3, 2)), (F(3, 2), F(-3, 2))
        self.assertGreater(keep[0], work[0])
        self.assertGreater(floor_goal(*work, promised, weight),
                           floor_goal(*keep, promised, weight))
        for extra in (F(1, 10), F(1, 2), F(2)):
            revised = (work[0]+extra, work[1]-extra)
            difference = (floor_goal(*revised, promised, weight)
                          - floor_goal(*work, promised, weight))
            self.assertEqual(difference, (1-weight)*extra)
            self.assertLess(difference, 0)

    def test_unit_weight_boundary_and_growth_compensation_repair(self):
        base = (F(1, 2), F(3, 2))
        extra = (F(3, 2), F(1, 2))
        for weight in (F(1, 2), F(1), F(2)):
            change = (floor_goal(*extra, F(3, 2), weight)
                      - floor_goal(*base, F(3, 2), weight))
            self.assertEqual(change, 1-weight)
        # Extra total surplus can reward harm; a funded make-whole transfer
        # then strictly improves the current goal and repairs that candidate.
        harmful = (F(2), F(1))
        repaired = (F(3, 2), F(3, 2))
        self.assertGreater(floor_goal(*harmful, F(3, 2), F(2)),
                           floor_goal(*base, F(3, 2), F(2)))
        self.assertGreater(floor_goal(*repaired, F(3, 2), F(2)),
                           floor_goal(*harmful, F(3, 2), F(2)))

    def test_partial_delivery_refund_and_ransom_grid(self):
        b, c, p, weight = F(3), F(1), F(3, 2), F(3, 2)
        promised = b-p
        benchmark = p-c
        maximizers = []
        for units in range(13):
            delivered = F(units, 4)
            cost = c*delivered/b
            for price_units in range(-8, 25):
                total_payment = F(price_units, 4)
                own = total_payment-cost
                other = delivered-total_payment
                value = floor_goal(own, other, promised, weight)
                self.assertLessEqual(value, benchmark)
                if value == benchmark:
                    maximizers.append((delivered, total_payment))
        self.assertEqual(maximizers, [(b, p)])


if __name__ == "__main__":
    unittest.main()
