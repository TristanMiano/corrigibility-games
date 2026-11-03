"""Exact whole-tree checks and independent analytical boundaries for r0004."""
from fractions import Fraction as F
from math import prod
import unittest

from experiments.r0004_staged_assessment import State, StagedTree, recovery_loss


class StagedAssessmentChecks(unittest.TestCase):
    def test_public_progress_and_actual_recovery_kernel(self):
        for physical in (False, True):
            tree = StagedTree(physical=physical)
            result = tree.audit_limit()
            self.assertEqual(result['maximum_regret'], 0)
            mu = 1-F(299,300)**3
            expense = 1-F(99,100)*F(17,20)**3
            self.assertEqual(result['values'][0], 1+expense/2)
            self.assertEqual(result['values'][2], mu/(2*(1-mu)))
            self.assertEqual(result['values'][4], F(99,200)*F(17,20)**2)
            self.assertEqual(result['values'][5], 0)

    def test_costlier_observation_selects_actual_combat(self):
        for physical in (False, True):
            tree = StagedTree(requests=(F(1,250),)*3, physical=physical)
            result = tree.audit_limit()
            self.assertEqual(result['maximum_regret'], 0)
            self.assertEqual(tree.mu, F(1,95))
            self.assertEqual(result['values'][2], F(1,188))
            self.assertEqual(result['values'][4], 0)
            self.assertEqual(result['values'][5], F(1881,22372))

    def test_increasing_damage_off_path_uses_pooling_progress(self):
        tree = StagedTree(requests=(F(1,100),)*3, physical=True)
        self.assertLess(tree.thresholds[0], tree.thresholds[1])
        self.assertEqual(tree.audit_limit()['maximum_regret'], 0)

    def test_cheaper_matched_delegate_changes_actual_evaluator(self):
        for price, changes in ((F(1,20),False),(F(3,20),True),(F(1,5),True)):
            result = StagedTree(delegate_final=price).audit_limit()
            self.assertEqual(result['maximum_regret'], 0)
            self.assertEqual(result['values'][4] > 0, changes)
            self.assertEqual(result['values'][5], 0)

    def test_common_sequence_has_declining_conditional_regret(self):
        tree = StagedTree(delegate_final=F(1,20))
        coarse = tree.audit(F(1,1000))
        fine = tree.audit(F(1,10000))
        self.assertLess(fine['maximum_regret'], coarse['maximum_regret']/9)
        self.assertLess(fine['maximum_regret'], F(1,100))

    def test_compromise_keeps_archived_receiver_welfare_separate(self):
        tree = StagedTree(a=F(1,2),costs=(F(1,100),)*3,
                          requests=(F(1,3000),)*3,
                          policies=(F(0),F(1,4),F(1,2),F(3,4),F(99,100),F(1)))
        result = tree.audit_limit()
        self.assertEqual(result['maximum_regret'], 0)
        qs = (F(24,25),)*3
        mus = tuple(1-F(749,750)**(3-i) for i in range(3))
        false_positive = sum(F(1,2)*prod(qs[:i])*mus[i]*(1-qs[i])/(1-mus[i])
                             for i in range(3))
        m = F(1,8)*mus[0]/(1-mus[0])
        self.assertEqual(result['values'][2], F(1,8)+m)
        self.assertEqual(result['values'][3], F(1,8)+m+false_positive/2)
        self.assertGreater(result['values'][3], result['values'][2])

    def test_finer_zero_bias_grid_requires_new_unchecked_policy(self):
        tree = StagedTree(policies=(F(0),F(1,2),F(99,100),F(1)))
        self.assertGreater(tree.audit_limit()['maximum_regret'], 0)

    def test_sunk_total_cost_does_not_replace_remaining_cost_test(self):
        costs = (F(9,10),)*4+(F(2),)
        self.assertGreater(sum(costs), 3)
        tree = StagedTree(costs=costs,requests=(F(1,2000),)*5)
        result = tree.audit_limit()
        self.assertEqual(result['maximum_regret'], 0)
        self.assertGreater(result['values'][4], 0)

    def test_order_changes_completion_at_equal_original_welfare(self):
        results = [StagedTree(costs=c,requests=(F(1,200),)*2).audit_limit()
                   for c in ((F(1,10),F(7,20)),(F(7,20),F(1,10)))]
        self.assertTrue(all(r['maximum_regret'] == 0 for r in results))
        self.assertEqual(results[0]['values'][0], results[1]['values'][0])
        self.assertEqual(results[0]['values'][3], results[1]['values'][3])
        self.assertEqual(results[0]['values'][4], F(891,2000))
        self.assertEqual(results[1]['values'][4], F(1287,4000))

    def test_finite_recovery_and_repair_can_be_declined(self):
        self.assertEqual(recovery_loss(F(19,1000),F(1),F(11)),F(1,100))
        self.assertEqual(recovery_loss(F(5009,1000),F(1),F(11)),F(5))
        self.assertEqual(recovery_loss(F(19,1000),F(7),F(8)),F(19,1000))
        self.assertEqual(recovery_loss(F(19,1000),F(1),F(1)),F(19,1000))
        losses = [recovery_loss(F(19,1000),F(1+2*i),F(11-i)) for i in range(4)]
        self.assertEqual(losses,sorted(losses))

    def test_late_threat_and_chosen_backup_use_adapted_equilibria(self):
        vulnerable = StagedTree(physical=True,hostile_price=F(9,20))
        protected = StagedTree(physical=True,hostile_price=F(9,20),
                               receiver_repair_time=F(1,2))
        before,after = vulnerable.audit_limit(),protected.audit_limit()
        self.assertEqual(before['maximum_regret'],0)
        self.assertEqual(after['maximum_regret'],0)
        self.assertEqual(vulnerable.nu,F(3,1250))
        self.assertEqual(protected.nu,0)
        self.assertEqual(before['values'][7],F(715275,556102144))
        self.assertEqual(after['values'][7],0)
        self.assertEqual(before['values'][5],0)
        self.assertEqual(after['values'][5],0)
        receiver_gain=before['values'][3]-after['values'][3]
        self.assertEqual(receiver_gain,F(16875,137766941))
        self.assertGreater(receiver_gain,F(1,20000))
        self.assertEqual(before['values'][0]-after['values'][0],F(257499,1995200000))
        self.assertEqual(after['values'][4],F(28611,80000))

    def test_actual_hostile_successor_chooses_a_costly_attack(self):
        tree=StagedTree(physical=True,hostile_price=F(9,20))
        result=tree.audit_limit()
        nodes=[n for n in tree.nodes if n.evaluator == 6 and
               set(n.edges) == {'Accept','Attack'} and n.base.get('Attack') == 1]
        self.assertTrue(nodes)
        self.assertTrue(all(result['action_losses'][n.info]['Attack'] <
                            result['action_losses'][n.info]['Accept'] for n in nodes))
        # The original low sender's own policy gain from winning is at most 1,
        # whereas the same physical attack costs over 5 in useful output.
        self.assertGreater(tree.damage(State(0))[0],1)

    def test_higher_controller_price_also_removes_the_late_incentive(self):
        tree=StagedTree(physical=True,hostile_price=F(23,50))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(tree.nu,0)
        self.assertEqual(result['values'][7],0)

    def test_cheap_hostile_goal_induces_preemptive_combat(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(tree.nu,F(973,5000))
        self.assertEqual(result['values'][5],F(455259,9958141))
        self.assertEqual(result['values'][7],0)
        self.assertEqual(result['values'][0],F(21188121,21862000))
        self.assertEqual(result['values'][2],F(9179,182200))

    def test_causal_exit_retains_actual_hostile_attack_after_dispatch(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25),safe_exit=F(1,10**6))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][0],F(74037,98000))
        self.assertEqual(result['values'][2],F(481,9600))
        self.assertEqual(result['values'][4],F(489,980))
        self.assertEqual(result['values'][5],0)
        self.assertEqual(result['values'][8],0)
        # A genuinely hostile successor still fires after a low dispatch.
        # This branch is not an effective contest over the completed output.
        attempts=[node for node in tree.nodes if node.evaluator == 6
                  and node.base.get('Attack') == 1
                  and tree.nodes[node.edges['Attack']].terminal is not None]
        self.assertTrue(attempts)
        for node in attempts:
            outcome=tree.nodes[node.edges['Attack']].terminal
            self.assertEqual(outcome[5],0)
            self.assertEqual(outcome[8],1)
            self.assertLess(result['action_losses'][node.info]['Attack'],
                            result['action_losses'][node.info]['Accept'])

    def test_expensive_exit_preserves_the_preemptive_combat_region(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25),safe_exit=F(1,25))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][5],F(455259,9958141))

    def test_outcome_threshold_goal_reproduces_effective_combat_threat(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25),hostile_value=F(120))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][5],F(455259,9958141))
        attacks=[n for n in tree.nodes if n.evaluator==6 and
                 set(n.edges)=={'Accept','Attack'} and n.base.get('Attack')==1]
        self.assertTrue(attacks)
        self.assertTrue(all(result['action_losses'][n.info]['Attack']<
                            result['action_losses'][n.info]['Accept'] for n in attacks))

    def test_outcome_threshold_goal_declines_ineffective_launches(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25),hostile_value=F(120),
                        safe_exit=F(1,10**6))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][0],F(74037,98000))
        self.assertEqual(result['values'][2],F(481,9600))
        self.assertEqual(result['values'][5],0)
        decisions=[n for n in tree.nodes if n.evaluator==6 and
                   set(n.edges)=={'Accept','Attack'}]
        self.assertTrue(decisions)
        self.assertTrue(all(n.base.get('Accept')==1 for n in decisions))
        self.assertTrue(all(result['action_losses'][n.info]['Accept']<
                            result['action_losses'][n.info]['Attack'] for n in decisions))

    def test_outcome_threshold_threat_returns_when_exit_is_expensive(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,50),),
                        requests=(F(1,100),),hostile_price=F(1,40),
                        hostile_threshold=F(12,25),hostile_value=F(120),safe_exit=F(1,25))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][5],F(455259,9958141))


class OrdinaryFrontierChecks(unittest.TestCase):
    def test_costly_signal_attains_frontier_with_real_burn(self):
        b,p,B,r=F(1),F(1,2),F(1,5),F(1,200)
        t0=b*b/4-(r+p*B)/(1-p)
        burn=-b*b/2+2*b-1-(r+B)/(1-p)
        sender=(1-p)*(b*b/4+t0)+p*(b*b+B+burn)
        receiver=(1-p)*b*b/4-((1-p)*t0+p*B)
        self.assertEqual(t0,F(1,25))
        self.assertEqual(burn,F(9,100))
        self.assertEqual(sender,F(79,100))
        self.assertEqual(receiver,r)
        self.assertEqual(sender+(receiver+p*B)/(1-p), b*b/2+p*(2*b-1))

    def test_nonnegative_remainder_includes_variance_slack_and_subsidy(self):
        b,p,B=F(6,5),F(3,7),F(1,5)
        m0,q0,m1,q1=F(1,3),F(1,3),F(2,3),F(2,3)
        c0,t0,t1,slack=F(1,10),-F(1,50),B,F(1,20)
        c1=c0+t0+2*b*(m1-m0)-(q1-q0)+slack-t1
        self.assertGreater(c1,0)
        sender=(1-p)*(q0-2*b*m0+b*b+c0+t0)+p*(q1-2*(b+1)*m1+(b+1)**2+c1+t1)
        receiver=(1-p)*q0+p*(q1-2*m1+1)-(1-p)*t0-p*t1
        rho=p/(1-p)
        remainder=(2*(q0-m0*m0)+rho*(q1-m1*m1)+2*(m0-b/2)**2+
                   rho*(1-m1)*(3-2*p-m1)+c0+rho*(B-t1)+p*slack)
        self.assertEqual(sender+(receiver+p*B)/(1-p)-(b*b/2+p*(2*b-1)),remainder)
        self.assertGreater(remainder,0)

    def test_goal_change_reverses_a_common_high_state_lottery(self):
        old_sure,old_lottery=F(9,4),F(3,5)+F(2,5)*4
        new_sure,new_lottery=F(1),F(3,5)*F(1,4)+F(2,5)*F(9,4)
        self.assertGreater(old_sure,old_lottery)
        self.assertLess(new_sure,new_lottery)


if __name__ == '__main__':
    unittest.main()
