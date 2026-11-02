"""Exact supporting checks for r0003's analytic constructions.

Branch enumeration, finite lottery searches and rational interval certificates
are deliberately separate from the paper formulas. They do not certify the
unfinished physical/authority implementation or constitute independent review.
Run: python -m unittest discover -s tests -p 'test_r0003*.py'
"""
from fractions import Fraction as F
from itertools import combinations, product
import unittest


def inspection_branches(p, alpha, audit, *, bias=F(1), packet=F(1, 100),
                        update=F(9, 20), probe=F(1, 100), unchecked=F(1)):
    """Enumerate the actual state/claim/check tree, retaining old welfare."""
    result = []
    for state, prior in ((0, 1-p), (1, p)):
        claim_probability = F(1) if state else alpha
        for claim, signal_probability in ((False, 1-claim_probability),
                                          (True, claim_probability)):
            if not signal_probability:
                continue
            checks = ((False, 1-audit), (True, audit)) if claim else ((False, F(1)),)
            for checked, check_probability in checks:
                changed = bool(claim and checked and state)
                action = F(state) if checked else unchecked if claim else F(0)
                sender_cost = packet*claim + update*changed
                receiver_cost = probe*checked
                result.append({
                    "probability": prior*signal_probability*check_probability,
                    "state": state, "claim": claim, "checked": checked,
                    "changed": changed, "action": action,
                    "sender_loss": sender_cost+(action-state-bias)**2,
                    "receiver_loss": receiver_cost+(action-state)**2,
                    "sender_material_cost": sender_cost,
                    "receiver_material_cost": receiver_cost,
                })
    return result


def mean(branches, field):
    return sum((row["probability"]*row[field] for row in branches), F(0))


def lottery_moments(weights, policies):
    return (sum(w*y for w, y in zip(weights, policies)),
            sum(w*y*y for w, y in zip(weights, policies)))


def upper_lottery_gain(policies, budget, bias):
    """Enumerate the one/two-support vertices under E[Y^2] <= budget."""
    vertices = [(y, y*y) for y in policies if y*y <= budget]
    for a, b in combinations(policies, 2):
        if a*a <= budget <= b*b:
            weight_b = (budget-a*a)/(b*b-a*a)
            vertices.append(((1-weight_b)*a+weight_b*b, budget))
    return max(2*bias*m-q for m, q in vertices)


class InspectionCore(unittest.TestCase):
    def test_branch_payoffs_and_distinct_outcome_measures(self):
        rows = inspection_branches(F(1, 2), F(1, 99), F(99, 100))
        self.assertEqual(sum(r["probability"] for r in rows), 1)
        self.assertEqual(mean(rows, "sender_loss"), F(4911, 4000))
        self.assertEqual(mean(rows, "receiver_loss"), F(1, 198))
        self.assertEqual(mean(rows, "changed"), F(99, 200))
        self.assertEqual(mean(rows, "checked"), F(1, 2))
        false_claims = sum(r["probability"] for r in rows if r["claim"] and not r["state"])
        wrong = sum(r["probability"] for r in rows if r["action"] != r["state"])
        self.assertEqual(false_claims, F(1, 198))
        self.assertEqual(wrong, F(1, 19800))
        self.assertEqual(mean(rows, "receiver_material_cost"), F(1, 200))
        self.assertGreater(mean(rows, "sender_material_cost"), F(1, 2)*(F(1, 100)+F(99, 100)*F(9, 20)))

    def test_low_claim_indifference_is_actual_costed_welfare(self):
        rows = inspection_branches(F(1, 2), F(1, 99), F(99, 100))
        low = [r for r in rows if r["state"] == 0]
        for claim in (False, True):
            selected = [r for r in low if r["claim"] == claim]
            mass = sum(r["probability"] for r in selected)
            loss = sum(r["probability"]*r["sender_loss"] for r in selected)/mass
            self.assertEqual(loss, 1)

    def test_receiver_all_policy_choices_and_combat(self):
        mu, v, s, damage = F(1, 100), F(1, 100), F(1, 20), F(1, 100)
        losses = {y: mu*y*y+(1-mu)*(y-1)**2 for y in (F(0), F(1, 2), F(1))}
        self.assertEqual(losses[F(1)], v)
        self.assertGreater(losses[F(0)], v)
        self.assertGreater(losses[F(1, 2)], v)
        self.assertEqual(s*mu+damage-v, F(1, 2000))
        self.assertLess(F(1, 198), s*F(1, 2)+damage)

    def test_prechange_evaluator_and_staged_abort(self):
        # k=2 is deliberately above the successor's decision-loss range 1.
        # The original high type still benefits: old losses are 4 versus 1+k.
        k = F(2)
        self.assertLess(1+k, 4)
        for remaining in (k, 2*k/3, k/3):
            self.assertLess(1+remaining, 4)  # High original continues.
            self.assertGreater(1+remaining, 1)  # Low original aborts.
        self.assertLess(F(0)**2, F(1)**2)  # Actual low C reports low.

    def test_high_state_change_reverses_lottery_preferences(self):
        for bias in (F(1), F(101, 100), F(2)):
            sure_old = (F(1, 2)-1-bias)**2
            gamble_old = F(7, 10)*bias*bias+F(3, 10)*(1+bias)**2
            self.assertLess(gamble_old, sure_old)
        self.assertLess(F(1, 4), F(3, 10))

    def test_on_demand_installation_saves_real_expected_cost(self):
        p, audit, k = F(1, 2), F(99, 100), F(9, 20)
        self.assertEqual(p*k-p*audit*k, F(9, 4000))

    def test_commitment_controls_include_destructive_screening(self):
        p, v, f, k, ds, dr, s = map(F, [F(1, 2), F(1, 100), F(1, 100), F(9, 20), 5, F(1, 100), F(1, 20)])
        q, uncommitted = 1-f, p*v/(1-v)
        self.assertEqual(uncommitted-p*v, F(1, 19800))
        self.assertEqual(uncommitted-p*q*v, F(199, 1980000))
        tau = (1-f)/(ds+1-s)
        self.assertEqual(tau, F(99, 595))
        self.assertEqual(p*tau*dr, F(99, 119000))
        self.assertLess(p*tau*dr, uncommitted)
        self.assertLess(f+tau*ds, 3)
        self.assertEqual(1-f-tau*(ds+1-s), 0)
        # A genuine cost for installing any receiver commitment can reverse it.
        self.assertGreater(F(1, 100)+p*tau*dr, uncommitted)


class ContinuousPolicyCore(unittest.TestCase):
    def test_continuous_combat_regime_from_winner_branches(self):
        p, mu, s, ds, b, f = F(1, 2), F(1, 100), F(1, 20), F(5), F(1), F(1, 100)
        z, g, h = 1-mu, 2*b-1, 2*b+1
        dr = mu*(1-s-mu)
        threshold = z*mu
        gz = 2*b*z-z*z
        war = (gz-f)/(ds+gz-s*g)
        alpha = p*mu/((1-p)*z)
        totals = {"sender": F(0), "receiver": F(0), "war": F(0)}
        conditional_claim = {}
        for theta, prior in ((0, 1-p), (1, p)):
            claim = alpha if not theta else F(1)
            claim_sender = F(0)
            for fought, mass, y in ((False, 1-war, z),
                                    (True, war*s, F(1)),
                                    (True, war*(1-s), F(theta))):
                sl = f+ds*fought+(y-theta-b)**2
                rl = dr*fought+(y-theta)**2
                claim_sender += mass*sl
                totals["sender"] += prior*claim*mass*sl
                totals["receiver"] += prior*claim*mass*rl
                totals["war"] += prior*claim*mass*fought
            totals["sender"] += prior*(1-claim)*(theta+b)**2
            totals["receiver"] += prior*(1-claim)*theta**2
            conditional_claim[theta] = claim_sender
        self.assertEqual(conditional_claim[0], b*b)
        self.assertLess(conditional_claim[1], (b+1)**2)
        self.assertEqual(totals["receiver"], p*mu)
        self.assertEqual(totals["war"], p*war/z)
        self.assertEqual(threshold, s*mu+dr)
        self.assertLess(threshold, F(3, 250))
        self.assertLess(totals["receiver"], s*(1-p)+dr)

    def test_verification_improvement_benefits_both_with_more_changes(self):
        # Reconstruct losses from state/claim/probe branches, rather than
        # testing the derivative formula against its own implementation.
        for b, k in product((F(1), F(3, 2), F(2)), (F(9, 20), F(2))):
            previous = None
            for z in (F(4, 5), F(9, 10), F(19, 20), F(99, 100)):
                p, f, v = F(1, 2), F(1, 100), z*(1-z)
                audit = 1-f/(2*b*z-z*z)
                alpha = p*(1-z)/((1-p)*z)
                rows = inspection_branches(p, alpha, audit, bias=b, packet=f,
                                           update=k, probe=v, unchecked=z)
                current = (mean(rows, "sender_loss"), mean(rows, "receiver_loss"),
                           mean(rows, "changed"))
                if previous is not None:
                    self.assertLess(current[0], previous[0])
                    self.assertLess(current[1], previous[1])
                    self.assertGreater(current[2], previous[2])
                previous = current

    def test_continuous_box_certificate(self):
        u = F(10103, 1000000)
        self.assertGreater(u*(1-u), F(1, 100))
        self.assertGreater(1-u*u, F(99, 100))
        self.assertLess(F(1, 100)/(1-u*u), F(11, 1000))
        self.assertLess(u*(F(202, 100)+u), F(21, 1000))
        self.assertLess(F(47, 100)+F(11, 1000)*F(21, 1000), F(49, 100))
        self.assertLess(F(952, 1000)*u, F(1, 100))
        self.assertLess(F(51, 100)*u, F(229, 5100))

    def test_rational_posterior_witness_from_actual_branches(self):
        # Choose a rational z, then set v=z(1-z); no floating-point root.
        z, p, b, f, k = F(99, 100), F(1, 2), F(1), F(1, 100), F(9, 20)
        mu, v = 1-z, z*(1-z)
        g_z = 2*b*z-z*z
        audit = 1-f/g_z
        alpha = p*mu/((1-p)*z)
        rows = inspection_branches(p, alpha, audit, bias=b, packet=f,
                                   update=k, probe=v, unchecked=z)
        self.assertEqual(mean(rows, "receiver_loss"), p*mu)
        excess = mu*(2*b+mu)
        self.assertEqual(mean(rows, "sender_loss"), b*b+p*(f+audit*k+(1-audit)*excess))
        # Every extra policy is checked, including ones absent from 067's grid.
        for action in (F(i, 100) for i in range(101)):
            self.assertGreaterEqual(mu*action**2+z*(action-1)**2, v)

    def test_committed_audit_benefits_both_before_setup_cost(self):
        for b, z, k in product((F(1), F(3, 2), F(2)),
                               (F(4, 5), F(9, 10), F(99, 100)),
                               (F(1, 10), F(9, 20), F(2))):
            g, h, f, p = 2*b-1, 2*b+1, F(1, 100), F(1, 2)
            self.assertLess(k, h)
            gz, mu = 2*b*z-z*z, 1-z
            rho, qd = 1-f/gz, 1-f/g
            delta_s = p*((1-rho)*mu*(2*b+mu)-(qd-rho)*k)
            self.assertGreater(delta_s, 0)
            self.assertEqual(g*(2*b+mu)-h*(2*b-2+mu), 2*z)
            self.assertGreater(p*mu-p*qd*z*mu, 0)

    def test_public_erasure_probability_preserves_effective_incentives(self):
        z, f, a = F(99, 100), F(1, 100), F(999, 1000)
        effective_cost = z*(1-z)
        actual_cost = a*effective_cost
        effective_inspection = 1-f/(2*z-z*z)
        attempt = effective_inspection/a
        self.assertLess(attempt, 1)
        self.assertEqual(actual_cost+(1-a)*effective_cost, effective_cost)
        self.assertEqual((1-attempt*a)*(2*z-z*z), f)


class EnlargedControlComparisons(unittest.TestCase):
    def test_low_belief_bound_cannot_be_reused_for_high_continuation(self):
        s, dr, ds, k = F(1, 20), F(1, 100), F(5), F(9, 20)
        receiver_losses = {}
        for offered in (F(0), F(1, 2), F(1)):
            # Low H attacks, then changes its winner policy with the offer.
            winner_policy = F(0) if offered == 1 else F(1)
            receiver_losses[offered] = dr+s*winner_policy**2
        self.assertEqual(min(receiver_losses, key=receiver_losses.get), F(1))
        self.assertLess(receiver_losses[F(1)], s+dr)
        low_final_moment, high_final_moment = F(0), F(1)
        self.assertLessEqual(low_final_moment, s+dr)
        self.assertGreater(high_final_moment, s+dr)
        high_alternative_loss = k+(1-1-1)**2
        high_diagnostic_loss = 1+F(1, 100)+F(99, 100)*k
        self.assertLess(high_alternative_loss, high_diagnostic_loss)
        self.assertGreater(k+ds+1, 1)  # Low adoption is unattractive.
        self.assertGreater(1+F(46, 100), high_diagnostic_loss)

    def test_prior_robust_payment_bound_against_lottery_menus(self):
        policies = (F(0), F(1, 2), F(1))
        weights = [(F(i, 4), F(j, 4), F(4-i-j, 4))
                   for i in range(5) for j in range(5-i)]
        moments = [lottery_moments(w, policies) for w in weights]
        budget = F(1, 5)
        for b, p in product((F(1), F(101, 100), F(2)),
                            (F(1, 10), F(49, 100), F(1, 2), F(51, 100), F(9, 10))):
            bound = (p-1/(8*(1-p)) if p < F(1, 2) else (1-p)/2)-budget
            for (m0, q0), (m1, q1) in product(moments, repeat=2):
                if m1 < m0:
                    continue
                # Maximize receipts at the cap and the low type's binding IC.
                t1 = budget
                t0 = t1-2*b*(m1-m0)+(q1-q0)
                self.assertLessEqual(t1-t0, 2*(b+1)*(m1-m0)-(q1-q0))
                loss = (1-p)*(q0-t0)+p*(q1-2*m1+1-t1)
                self.assertGreaterEqual(loss, bound)

    def test_payment_bound_attainment_and_resource_asymmetry(self):
        for p in (F(1, 10), F(49, 100), F(1, 2), F(51, 100), F(9, 10)):
            budget = F(1, 5)
            if p < F(1, 2):
                m0 = m1 = 1/(4*(1-p))
                q0, q1 = m0*m0, m1
                t0, t1 = budget+m0-m0*m0, budget
                bound = p-1/(8*(1-p))-budget
                self.assertGreater(t0, budget)  # Only t1 is capped.
            else:
                m0, q0, m1, q1 = F(1, 2), F(1, 4), F(1), F(1)
                t0, t1 = budget-F(1, 4), budget
                bound = (1-p)/2-budget
            loss = (1-p)*(q0-t0)+p*(q1-2*m1+1-t1)
            self.assertEqual(loss, bound)
            for theta in (0, 1):
                own = (q0-2*(theta+1)*m0+(theta+1)**2+t0,
                       q1-2*(theta+1)*m1+(theta+1)**2+t1)
                self.assertLessEqual(own[theta], own[1-theta])

    def test_all_small_lottery_menus_obey_receiver_screening_bound(self):
        policies = (F(0), F(1, 2), F(1))
        weights = [(F(i, 8), F(j, 8), F(8-i-j, 8))
                   for i in range(9) for j in range(9-i)]
        moments = [lottery_moments(w, policies) for w in weights]
        checked = 0
        for bias, prior in product((F(1), F(5, 4), F(2)),
                                   (F(1, 4), F(1, 2), F(3, 4))):
            for (m0, q0), (m1, q1) in product(moments, repeat=2):
                dm, dq = m1-m0, q1-q0
                if 2*bias*dm <= dq <= 2*(bias+1)*dm:
                    checked += 1
                    receiver = (1-prior)*q0+prior*(q1-2*m1+1)
                    self.assertGreaterEqual(receiver, prior*(1-prior))
        self.assertGreater(checked, 100)

    def test_signal_lottery_attains_bound_and_benefits_sender(self):
        self.assertEqual(F(1, 2)*F(1, 4)+F(1, 2)*F(1, 4), F(1, 4))
        self.assertEqual(F(1, 2)*F(1, 4)+F(1, 2)*(4-3*F(3, 4)), 1)

    def test_threat_frontier_from_exhaustive_lottery_vertices(self):
        grid = (F(0), F(1, 2), F(1))
        for bias, budget in product((F(1), F(3, 2), F(2)),
                                     (F(i, 40) for i in range(41))):
            expected = ((4*bias-1)*budget if budget <= F(1, 4)
                        else 2*bias/3+(4*bias/3-1)*budget)
            self.assertEqual(upper_lottery_gain(grid, budget, bias), expected)
        # Additional intermediate policies actually enlarge the threat frontier.
        self.assertGreater(upper_lottery_gain((F(0), F(1, 5), F(1, 2), F(1)), F(3, 50), F(1)),
                           upper_lottery_gain(grid, F(3, 50), F(1)))

    def test_open_region_has_exact_strict_margins(self):
        pmax, vmax = F(51, 100), F(1, 100)
        max_receiver_loss = pmax*vmax/(1-vmax)
        self.assertLess(max_receiver_loss, F(3, 500))
        self.assertLess(vmax, F(11, 1000))  # Late conditional controls too.
        self.assertLess(max_receiver_loss, F(48, 1000)*(1-pmax)+F(1, 100))
        self.assertLess(F(1, 100)+F(46, 100), 1-pmax)
        self.assertLess(vmax*(1-F(48, 1000)), F(1, 100))
        k, r, b = F(9, 20), F(63, 1000), F(101, 100)
        self.assertEqual((k+r)**2-4*b*b*r, F(30519, 5000000))
        self.assertGreater((k+r)**2, 4*b*b*r)


class ReactorRepairChecks(unittest.TestCase):
    def test_negotiated_proposal_lottery_minimizes_both_thresholds(self):
        for t in (F(1, 5), F(9, 20), F(1, 2), F(4, 5)):
            table = lambda r: (
                max(F(8, 5)-3*t+F(7, 5)*r, F(8, 5)-t-F(3, 5)*r),
                max(3*t-F(7, 5)*r, t+F(3, 5)*r))
            optimum = table(t)
            self.assertEqual(optimum, (F(8, 5)*(1-t), F(8, 5)*t))
            for r in (F(i, 100) for i in range(101)):
                self.assertGreaterEqual(table(r)[0], optimum[0])
                self.assertGreaterEqual(table(r)[1], optimum[1])

    def test_state_blind_repair_exceeds_physical_frontier(self):
        for t in (F(i, 200) for i in range(201)):
            states = ((F(27, 20)+4*t, F(107, 20)-4*t),
                      (F(59, 20)+t, F(47, 20)-t),
                      (F(27, 20)+t, F(79, 20)-t),
                      (F(59, 20), F(59, 20)))
            floor_sum = max(a for a, _ in states)+max(b for _, b in states)
            self.assertGreaterEqual(floor_sum-F(67, 10), F(1, 5))
        self.assertEqual(max(F(63, 20), F(17, 5), F(9, 5), F(59, 20))
                         +max(F(71, 20), F(19, 10), F(7, 2), F(59, 20))
                         -F(67, 10), F(1, 4))

    def test_promised_floor_restoration_uses_current_consent(self):
        target = (F(63, 20), F(71, 20))
        for fallback in ((F(17, 5), F(19, 10)), (F(9, 5), F(7, 2)),
                         (F(59, 20), F(59, 20))):
            da, db = (x-y for x, y in zip(target, fallback))
            self.assertGreater(da+F(2, 3)*db, 0)
            self.assertGreater(db+F(2, 3)*da, 0)
        # In the first state A's original coordinate falls despite consent.
        self.assertLess(target[0], F(17, 5))


if __name__ == "__main__":
    unittest.main()
