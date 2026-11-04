# Cooperation that changes future partner opportunities

**R0005 dynamic extension.** Note 103 assumes installation does not change
the market-state transition. Productive work can instead change equipment,
access or qualification and hence future partners. This note gives the
correct stopping comparison for two implemented transition laws. It does
not infer those laws from a goal label or freeze the ordinary alternatives.

## 1. Switching changes the continuation kernel as well as current profit

Let the finite physical/market state s have actual implemented original
payoffs r_G(s),r_F(s) and transitions P_G,P_F. G denotes the proposed
reusable goal route; F denotes the best declared ordinary continuation
while retaining the option to adopt later. Both must include available
partners, controls, costs and live combat. The state and transition law
record actual resource renewal or accumulation and agency loss; an old
workshop's destroyed inputs cannot reappear merely by assigning a new label.

Let U be the original welfare of the installed route, k(s)>0 its setup
cost, V the pre-installation original value and 0<delta<1. Assume the
installed route is actually chosen by its then-current successors, with
the necessary goal/continuation certificate, rather than imposed on them
by the founder. The equations are

    U=r_G+delta P_G U,
    V=max(U-k, r_F+delta P_F V).                    (1)

If there are several ordinary actions with different transitions, the
second term is their Bellman maximum; the following single-P_F form
applies when its selected action law is fixed or already justified.

Define D=U-V and the effective advantage

    H=r_G-r_F+delta(P_G-P_F)U.                      (2)

Subtracting (1) gives

    D=min(k, H+delta P_F D).                        (3)

This is a contraction, so it has a unique bounded solution. Installation
is optimal at s exactly when

    k(s)<=H(s)+delta(P_F D)(s).                    (4)

The setup decision uses the original criterion. The new term in (2)
values the changed future opportunities at the installed continuation
value. Ignoring it can miss a beneficial change or credit an immediate
gain whose future consequences are worse. D can be negative when the
ordinary continuation is more valuable than the installed route; do not
import 103's nonnegative-loss interpretation without its stronger premises.

When r_G>=r_F and P_G U>=P_F U, H>=0. In that specialization the same
loss-of-delay and monotone-H arguments as 103 apply with P_F held fixed.
A physical capability improvement that alters both kernels or U requires
recomputation, not a claim that its sign follows from one row of P_G.

## 2. An exact qualification/access example

There are two states, low and high. In low, current net profit is zero
under both routes. In high, both routes earn R>0 per period and high is
absorbing. G moves from low to high with probability q_G per period;
ordinary continuation does so with q_F, where 0<q_F<q_G<=1. These are
implemented probabilities, for example from a specified productive trial
and subsequent access technology. Their actual derivation and expenses
must accompany any application. A goal name is not a qualification test.

Write z(q)=1-delta+delta q. The value of using route q from low is

    U_low(q)=delta q R/[(1-delta)z(q)],
    U_high=R/(1-delta).                             (5)

An installation in high buys no improvement and costs k, so it is refused.
In low, with constant one-time cost k, either immediate installation or
continued ordinary waiting is optimal, with indifference at

    k_crit=U_low(q_G)-U_low(q_F)
          =delta(q_G-q_F)R/[z(q_G)z(q_F)].          (6)

To check timing, compare immediate installation with one ordinary step
followed by installation if low persists. Immediate installation wins
when k z(q_F)<delta(q_G-q_F)(U_high-U_low(q_G)).
Since U_high-U_low(q_G)=R/z(q_G), this is exactly k<k_crit. Repeating
the comparison proves that delaying while still in the same low state
does not create another strictly better policy. Equation (3) gives the
same result and also permits arbitrary stopping times.

For delta=9/10,R=1,q_F=1/10,q_G=1/2,

    U_low(q_G)=90/11,  U_low(q_F)=90/19,
    k_crit=720/209.

At k=3 the original strictly prefers the implemented change, even though
the two routes have equal current profits in each state. The useful
difference is faster access to the productive future. This is genuine
adoption only when the proposed route actually includes a preference
change with its incentive certificate, rather than an ordinary purchase
arbitrarily named G. A priced ordinary method achieving q_G is a matched
alternative; equality permits either route and a cheaper method displaces G.

## 3. Changes in access and in the outside route have separate effects

At fixed other parameters in this example,

    d k_crit/d q_G = delta R/z(q_G)^2 >0,
    d k_crit/d q_F =-delta R/z(q_F)^2 <0.            (7)

Faster goal-enabled qualification increases the affordable installation
budget. Faster ordinary qualification decreases it while improving the
agent's ordinary welfare. If q_F rises to 2/5 with the other numerical
values fixed, k_crit becomes 90/253; the same k=3 update is displaced.
This is a better ordinary route, not evidence of reduced productive welfare.

A party considering a real access intervention at additional cost sigma
must compare the actual value improvement with sigma, and must account
for its effect on both q's, counterparties' choices and required resources.
Section 8 of 110 gives a funded advance that the already installed parties
can prefer; this note supplies the dynamic account when such productive
actions also change future access. The relation from an advance or goal
to the transition probabilities is still an application-specific proof
obligation.

The result separates three evidence levels: a transition parameter effect,
an affordable implemented route, and a route actually selected in a larger
market. Equations (3)-(7) establish the first and the conditional individual
choice once the second is supplied. They do not establish unrestricted
initial recognition, coalition selection or population prevalence.
