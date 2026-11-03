"""Independent identities and interval certificates for funded accommodation."""
from fractions import Fraction as F
from itertools import permutations
import unittest

from experiments.r0004_funded_checks import (
    sqrt_bounds,small_root_bounds,continuous_outside,funded_package,
    ordinary_combat_bound,audit_funded_witness,captured_state_bound,
    full_budget_package,audit_renegotiated_family,audit_early_goal_repair,
    ordinary_frontier_at_receiver)
from experiments.r0004_staged_assessment import StagedTree


class FundedAccommodationChecks(unittest.TestCase):
    def test_full_cash_continuation_and_all_continuous_policy_deviations(self):
        tree=StagedTree(a=F(3,10),f=F(1,1000),costs=(F(1,150),)*3,
                        requests=(F(1,30000),)*3,late_cash=F(11,400),
                        trade_offset=F(1,50),
                        policies=(F(0),F(3,10),F(8,25),F(1,2),F(4,5),F(99,100),F(1)))
        result=tree.audit_limit()
        continuous=tree.audit_continuous_policies(result)
        package=funded_package()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(continuous['maximum_policy_regret'],0)
        self.assertTrue(continuous['quote_posteriors'])
        self.assertEqual(set(continuous['quote_posteriors']),{F(0)})
        self.assertEqual(result['values'][0]+package['transfer']+F(1,1000),
                         package['sender'])
        self.assertEqual(result['values'][3]-package['transfer']+F(11,1000),
                         package['receiver'])
        self.assertEqual(result['values'][2],package['current_receiver'])

    def test_continuous_disagreement_tree_matches_the_root_recursion(self):
        mus=(F(3,40000),F(2,40000),F(1,40000))
        ell=-F(899,5000); next_value=F(0); requests=[]
        for mu in reversed(mus):
            requests.insert(0,mu*(1-mu-ell)-(1-mu)*next_value)
            next_value=mu*(1-mu-ell)/(1-mu)
        tree=StagedTree(f=F(1,1000),costs=(F(1,150),)*3,requests=requests,
                        late_cash=F(1899,10000),trade_offset=F(1,10),
                        continuous_posteriors=mus)
        result=tree.audit_limit()
        bounds=continuous_outside(requests=requests)
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(tree.audit_continuous_policies(result)['maximum_policy_regret'],0)
        for field,index in (('sender',0),('receiver',2)):
            self.assertLessEqual(bounds[field][0],result['values'][index])
            self.assertGreaterEqual(bounds[field][1],result['values'][index])

    def test_root_enclosures_certify_the_polynomial_not_float_rounding(self):
        for value in (F(0),F(4,9),F(2),F(1,10**20)):
            lo,hi=sqrt_bounds(value,30)
            self.assertLessEqual(lo*lo,value)
            self.assertGreaterEqual(hi*hi,value)
            self.assertLessEqual(hi-lo,F(1,10**30))
        r,z,ell=F(1,30000),F(1,10000),-F(899,5000)
        lo,hi=small_root_bounds(r,z,ell)
        polynomial=lambda mu: mu*mu-(1-ell+z)*mu+r+z
        self.assertGreaterEqual(polynomial(lo),0)
        self.assertLessEqual(polynomial(hi),0)
        self.assertLess(hi,(1-ell+z)/2)

    def test_known_low_quotes_charge_both_fees_and_use_actual_cash(self):
        result=funded_package()
        self.assertEqual(result['delta'],F(11,400))
        self.assertEqual(result['transfer'],F(203,1250))
        self.assertEqual(result['delta']+result['transfer'],F(1899,10000))
        a,x,b=F(3,10),F(1,50),F(1)
        self.assertEqual((a+x-b)**2+result['delta']+F(1,10000),(a-b)**2)
        self.assertEqual(result['ell'],-F(27,1000))
        # With a receiver proposal, the full cash cap is on the increasing
        # part of 2*(b-a)*x-2*x^2-fees; larger policies only add loss at cap.
        self.assertLess(x,(b-a)/2)
        self.assertGreater(result['delta']-x*x-F(1,10000),0)

    def test_staged_cash_welfare_preserves_founder_and_current_losses(self):
        result=funded_package()
        self.assertEqual(result['sender'],F(9728042719,10588410000))
        self.assertEqual(result['receiver'],
                         -F(31228441730140144159,274296107960296638125))
        self.assertEqual(result['C_probability'],F(685415,1411788))
        self.assertNotEqual(result['receiver'],result['current_receiver'])
        self.assertLess(result['posteriors'][0],F(3,10))

    def test_continuous_outside_is_enclosed_and_prior_interval_certified(self):
        result=continuous_outside()
        for value in (result['sender'],result['receiver'],result['excess']):
            self.assertLess(value[1]-value[0],F(1,10**30))
        self.assertLess(result['posteriors'][2][1],result['posteriors'][1][0])
        self.assertLess(result['posteriors'][1][1],result['posteriors'][0][0])
        certificate=audit_funded_witness()
        self.assertGreater(certificate['uniform_gap_lower'],F(104,10000))

    def test_original_high_goal_and_installed_goal_reverse_lottery(self):
        probability=F(14,23)
        old=F(2); new=F(13,10)
        loss=lambda target: probability*(1-target)**2+(1-probability)*target**2
        self.assertLess(loss(old),(F(1,2)-old)**2)
        self.assertGreater(loss(new),(F(1,2)-new)**2)


class OrdinaryControlChecks(unittest.TestCase):
    def test_all_strengths_and_early_goal_repair_are_uniform_certificates(self):
        self.assertGreater(audit_renegotiated_family(F(0))['uniform_gap_lower'],F(649,100000))
        early=audit_early_goal_repair()
        self.assertGreater(early['uniform_gap_lower'],F(25,10000))
        self.assertLess(early['receiver_cost_upper'],F(64,10**6))
        self.assertGreater(audit_early_goal_repair(F(499,1000))['uniform_gap_lower'],F(244,100000))

    def test_ordering_real_installments_preserves_sender_welfare_and_improves_founder(self):
        costs=(F(1,200),F(1,150),F(1,120))
        results=[full_budget_package(costs=order) for order in permutations(costs)]
        best=full_budget_package(costs=costs)
        self.assertEqual(len({r['sender'] for r in results}),1)
        self.assertEqual(best['receiver'],min(r['receiver'] for r in results))
        self.assertEqual(best['C_probability'],max(r['C_probability'] for r in results))
        requests=(F(1,40000),F(1,30000),F(1,24000))
        results=[full_budget_package(requests=order) for order in permutations(requests)]
        best=full_budget_package(requests=tuple(reversed(requests)))
        self.assertEqual(best['receiver'],min(r['receiver'] for r in results))
        self.assertEqual(len({r['current_receiver'] for r in results}),1)

    def test_stable_threshold_and_pre_activation_counteroffer_use_current_values(self):
        a,q,k,fee,epsilon,B=F(1),F(2,5),F(1,50),F(1,10000),F(1,1000),F(1899,10000)
        W=q*q+2*fee+epsilon; price=W-fee
        self.assertLess(price,B)
        self.assertEqual((a-q)**2+price+fee+k,F(1353,2500))
        self.assertEqual(price-q*q-fee,epsilon)
        self.assertGreater(k,2*fee+epsilon+F(1,10**6))
        delta,remaining=F(1,200),k/2
        self.assertLess(price+delta,B)
        self.assertEqual(remaining-delta,delta)
        self.assertGreater(price+delta+fee,W)

    def test_full_capture_remainder_keeps_receiver_costs_and_original_offset(self):
        p,b,a,lam,eta,B=F(3,7),F(6,5),F(1,5),F(3),F(1,5),F(1,5)
        m0,q0,m1,q1=F(1,3),F(1,3),F(2,3),F(2,3)
        c0,c1,v0,v1,t0,t1=F(1,10),F(2,3),F(1,100),F(1,50),-F(1,50),B
        h=1-p; A0=h*(1+lam)+eta; L0=b*(h+eta)+lam*a*h
        A1=p*(1+lam)-eta; H=p*(b+lam*a)-(b-1)*eta
        d=c1+t1-c0-t0-2*b*(m1-m0)+q1-q0
        S=h*(q0-2*b*m0+b*b+c0+t0)+p*(q1-2*(b+1)*m1+(b+1)**2+c1+t1)
        R=h*(q0-2*a*m0+a*a+v0-t0)+p*(q1-2*(1+a)*m1+(1+a)**2+v1-t1)
        K=b*b+(2*b-1)*eta+lam*a*a-L0*L0/A0+(1-lam)*B
        remainder=(A0*(q0-m0*m0)+A1*(q1-m1*m1)+A0*(m0-L0/A0)**2
                   +(1-m1)*(A1*(1-m1)+2*H)+(h+eta)*c0+lam*h*v0
                   +(p-eta)*c1+lam*p*v1+eta*d
                   +(h*(lam-1)-eta)*(B-t0)+(p*(lam-1)+eta)*(B-t1))
        self.assertEqual(S+lam*R-K,remainder)

    def test_sharp_frontier_inverts_a_known_attaining_policy(self):
        p,x,B,D=F(1,2),F(11,25),F(1899,10000),F(101,5)
        r=(1-p)*x*x+p*F(1,100)*(1-x)**2/D-B
        s=p+B+(1-p+p*5/D)*(1-x)**2
        result=ordinary_frontier_at_receiver(r)
        self.assertLessEqual(result['policy'][0],x)
        self.assertGreaterEqual(result['policy'][1],x)
        self.assertLessEqual(result['sender'][0],s)
        self.assertGreaterEqual(result['sender'][1],s)
        self.assertLess(result['sender'][1]-result['sender'][0],F(1,10**30))

    def test_early_goal_and_successor_changes_use_different_incumbents(self):
        a,z,k=F(1,2),F(1,4),F(1,50)
        y=z/2; payment=3*z*z/4-F(1,10000)
        current_loss=(a-y)**2+payment+F(1,10000)+k
        founder_loss=(1-y)**2+payment+F(1,10000)+k
        self.assertEqual(a*a-current_loss,F(17,400))
        self.assertEqual(founder_loss-F(3,4),F(33,400))
        self.assertLess(z*z/4,k)
        stable=F(7,25)
        self.assertEqual(k-stable*stable/4,F(1,2500))

    def test_cash_allocation_identity_retains_both_fees_and_information_cost(self):
        p,a,x=F(1,2),F(3,10),F(1,50)
        result=funded_package()
        q=a+x
        total=(1+F(11,1000)+F(1,1000)+(1-p)*F(1,5000)
               +2*(1-p)*(q*q-q)+p*result['expense']+result['excess']
               +2*a*(1-a-x)*result['false_positive'])
        self.assertEqual(result['sender']+result['receiver'],total)

    def test_capture_bound_attained_with_actual_winner_law_and_finite_punishment(self):
        for a0,punishment in ((F(0),F(0)),(F(1,5),F(0)),(F(0),F(15))):
            p,b,B,ds,dr,s,lam=F(1,2),F(1),F(1899,10000),F(5),F(1,100),F(1,20),F(2)
            result=captured_state_bound(p=p,original_receiver=a0,punishment=punishment,
                                         weight=lam)
            x=result['low_policy']; M=result['M']
            gain=(b-x)**2-(b-1)**2
            w=gain/(ds+M)
            self.assertTrue(0 < w < 1)
            low_truth=(b-x)**2+B
            low_lie=(b-1)**2+B+w*(ds+(1-s)*((b-a0)**2-(b-1)**2+punishment))
            self.assertEqual(low_truth,low_lie)
            high_truth=b*b+B+w*ds
            high_lie=(b+1-x)**2+B
            self.assertLess(high_truth,high_lie)
            sender=(1-p)*low_truth+p*high_truth
            receiver=(1-p)*(x-a0)**2+p*a0*a0+p*w*dr-B
            self.assertEqual(sender+lam*receiver,result['bound'])

    def test_burn_attains_frontier_when_receiver_damage_is_too_expensive(self):
        p,ds,dr,s,lam,B=F(1,2),F(5),F(1),F(1,20),F(2),F(1899,10000)
        result=captured_state_bound(p=p,damage_r=dr,punishment=F(0),weight=lam)
        self.assertEqual(result['eta'],p)
        self.assertGreater(lam*dr,result['M'])
        x=result['low_policy']; burn=(1-x)**2
        sender=(1-p)*(1-x)**2+p*(1+burn)+B
        receiver=(1-p)*x*x-B
        self.assertEqual(sender+lam*receiver,result['bound'])

    def test_positive_cost_punisher_displaces_first_package(self):
        p,x,w,B,ds,dr,s,P=F(1,2),F(11,25),F(17,1000),F(1899,10000),F(5),F(1,100),F(1,20),F(14)
        slack=w*(ds+(1-s)*(1+P))-(1-x)**2
        self.assertEqual(slack,F(273,20000))
        sender=(1-p)*(1-x)**2+p*(1+w*ds)+B+F(1,200)
        receiver=(1-p)*x*x+p*w*dr-B+F(1,1000)
        self.assertEqual(sender,F(4471,5000))
        self.assertEqual(receiver,-F(18403,200000))
        self.assertLess(sender,funded_package()['sender'])
        self.assertLess(receiver,continuous_outside()['receiver'][0])
        self.assertLess(P+ds+F(1,200),20)

    def test_repaired_family_has_uniform_strict_margin_and_both_proposers(self):
        result=audit_renegotiated_family()
        self.assertGreater(result['uniform_gap_lower'],F(8,1000))
        self.assertLess(result['receiver_cost_upper'],F(61,10**6))
        self.assertEqual(result['sender_offer']['sender'],
                         F(23270576604997,26767049445000))
        self.assertEqual(result['receiver_offer']['receiver'],
                         -F(7634391991072827540595843,49365727306329402625410000))

    def test_full_budget_continuations_use_actual_successor_and_original_goals(self):
        for a in (F(21,50),F(11,50)):
            tree=StagedTree(a=a,f=F(1,1000),costs=(F(1,150),)*3,
                            requests=(F(1,30000),)*3)
            result=tree.audit_limit(); package=full_budget_package(a=a)
            self.assertEqual(result['maximum_regret'],0)
            self.assertEqual(tree.audit_continuous_policies(result)['maximum_policy_regret'],0)
            self.assertEqual(result['values'][0]+F(1899,10000)+F(1,1000),package['sender'])
            self.assertEqual(result['values'][3]-F(1899,10000)+F(11,1000),package['receiver'])
            self.assertEqual(result['values'][2],package['current_receiver'])

    def test_continuous_peace_uses_quadratic_combat_boundary(self):
        mu=F(53,5000); ell=-F(899,5000)
        self.assertGreater(mu,F(1,100)/(1-F(1,20)))
        self.assertLess(mu*(1-F(1,20)-mu),F(1,100))
        tree=StagedTree(f=F(1,1000),costs=(F(1,150),),
                        requests=(mu*(1-mu-ell),),late_cash=F(1899,10000),
                        trade_offset=F(1,10),continuous_posteriors=(mu,))
        result=tree.audit_limit()
        self.assertEqual(result['maximum_regret'],0)
        self.assertEqual(result['values'][5],0)
        self.assertEqual(tree.audit_continuous_policies(result)['maximum_policy_regret'],0)

    def test_two_cap_identity_with_slack_burns_and_lotteries(self):
        b,p,B,lam=F(6,5),F(3,7),F(1,5),F(3)
        m0,q0,m1,q1=F(1,3),F(1,3),F(2,3),F(2,3)
        c0,t0,t1,slack=F(1,10),-F(1,50),B,F(1,20)
        c1=c0+t0+2*b*(m1-m0)-(q1-q0)+slack-t1
        sender=(1-p)*(q0-2*b*m0+b*b+c0+t0)+p*(q1-2*(b+1)*m1+(b+1)**2+c1+t1)
        receiver=(1-p)*q0+p*(q1-2*m1+1)-(1-p)*t0-p*t1
        A=1+(1-p)*lam; x=b/A
        bound=b*b+p*(2*b-1)-b*b/A+(1-lam)*B
        remainder=(A*(q0-m0*m0)+p*lam*(q1-m1*m1)+A*(m0-x)**2+
                   p*(1-m1)*(2+lam*(1-m1))+c0+p*slack+
                   ((1-p)*lam-1)*(B-t0)+p*lam*(B-t1))
        self.assertEqual(sender+lam*receiver-bound,remainder)
        self.assertGreater(remainder,0)

    def test_two_cap_bound_is_attained_by_actual_ordinary_burn(self):
        b,p,B,lam=F(1),F(1,2),F(1,5),F(4)
        x=b/(1+(1-p)*lam)
        burn=(1-x)*(2*b-1-x)
        sender=(1-p)*((b-x)**2+B)+p*(b*b+B+burn)
        receiver=(1-p)*x*x-B
        bound=b*b+p*(2*b-1)-b*b/(1+(1-p)*lam)+(1-lam)*B
        self.assertEqual(sender+lam*receiver,bound)
        self.assertEqual(burn,F(4,9))

    def test_contest_information_can_violate_ordinary_ic_with_damage_paid(self):
        # High report invokes a .1 state-revealing contest and incurs .5
        # expected real damage. Low imitation then has a .1 policy loss.
        b,p,B=F(1),F(1,2),F(1,5)
        x,t0,t1,burn=F(1,5),F(4,25),B,F(1,2)
        d=burn+t1-t0-2*b*(1-x)+(1-x*x)
        self.assertEqual(d,-F(1,10))
        low=(b-x)**2+t0
        low_imitation=F(1,10)+burn+t1
        self.assertEqual(low,low_imitation)
        sender=(1-p)*low+p*(b*b+burn+t1)
        receiver=(1-p)*x*x-(1-p)*t0-p*t1
        bound=ordinary_combat_bound(p=p,B=B)
        self.assertEqual(bound,F(179,230))
        self.assertGreater(sender+2*receiver,bound)

    def test_offset_receiver_bound_uses_its_actual_original_goal(self):
        bound=ordinary_combat_bound(p=F(1,2),a=F(3,10),B=F(1,100),weight=F(12))
        self.assertEqual(bound,F(10953,8300))
        self.assertGreater(bound-12*F(9,200),F(77,100))


if __name__ == '__main__':
    unittest.main()
