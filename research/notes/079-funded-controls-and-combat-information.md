# Funded ordinary mechanisms and costly combat information

**R0004 derivation; analytical self-check with exact arithmetic support.** This
extends 074's control in two directions: both state-contingent payments obey
the same real liquidity cap, and a specified contest may reveal the state.
It supplies a stronger comparison for constructive accommodation, while
identifying the control and information technologies that can displace it.

## 1. The two-cap supporting family

Retain 074's binary state, probability p, original quadratic goals, policy
interval [0,1], b in [1,2], moments m_t,q_t and real signaling expense C_t.
Now impose t_0,t_1 <= B. Negative payments remain generously permitted; an
actual receiver budget only narrows this comparison class. Write

\[
d=C_1+t_1-C_0-t_0-2b(m_1-m_0)+(q_1-q_0).
\]

Ordinary imitation gives d>=0. For lambda>=1/(1-p), put

\[
A=1+(1-p)\lambda,\qquad x=b/A.
\]

Then

\[
\boxed{L_S+\lambda L_R\ge
b^2+p(2b-1)-b^2/A+(1-\lambda)B.}
\tag{1}
\]

The exact remainder is

\[
\begin{aligned}
&A(q_0-m_0^2)+p\lambda(q_1-m_1^2)+A(m_0-x)^2\\
&+p(1-m_1)\{2+\lambda(1-m_1)\}+C_0+p d\\
&+[(1-p)\lambda-1](B-t_0)+p\lambda(B-t_1).
\end{aligned}
\tag{2}
\]

Every term is nonnegative. Receiver execution losses add another
nonnegative lambda-weighted term. At lambda=1/(1-p), (1) reduces to 074's
one-cap bound. Larger lambda uses the low-state cap as well; a control
cannot extract an unfunded low-state payment merely because a supporting
inequality omitted that cap.

The bound is attained algebraically by y_0=x,y_1=1, payments B in both
states, C_0=0 and C_1=(1-x)(2b-1-x). Here x<=b/2<=1, so this burn is
nonnegative; high IC also holds. The losses are

\[
L_S=(b-x)^2+p(2b-1)+B,\qquad L_R=(1-p)x^2-B.
\tag{3}
\]

Actual proposal, authority, participation and payment delivery are still
required to implement this attaining menu. Giving them free to the
comparison makes a subsequent strict advantage more informative.

For b=1,p=1/2, a sender reservation loss L in the range where x<=1/2
permits the sharp algebraic receiver frontier

\[
x=1-\sqrt{L-1/2-B},\qquad L_R\ge x^2/2-B.
\tag{4}
\]

The receiver's bargaining rights matter: a Pareto improvement at one
reservation pair need not be chosen at another. This is a condition to
derive from the actual disagreement game, not a freely assigned welfare
target.

## 2. Allowing a specified information-revealing contest

Broaden the comparison to mechanisms with a first effective contest that
terminates policy bargaining. Before that contest, a low sender can
imitate the high sender's entire strategy. On a contest path, discovering
the real state may change the terminal policy. Require:

- terminal policy remains in [0,1];
- the financial and non-policy material law under imitation is the same
  as for the high type (for example, payments are already funded and
  locked to the same public pre-contest history);
- a contest costs the sender at least d_S>0 in real original output,
  including the actual best available recovery;
- there is no additional state-dependent confiscation, burn, transfer or
  protected sensor outside this stated contest law.

These are consequential coupling assumptions. A winner who can impose a
new state-contingent material punishment requires a different bound.

Let w_1 be the actual high-type probability of a contest. The old low
sender's policy loss ranges over an interval of length M=2b-1. A coupled
imitation therefore gives

\[
d\ge-M w_1,\qquad C_1\ge d_S w_1.
\tag{5}
\]

The inequality permits the strongest policy revelation after every
contest, rather than assuming that an ordinary mechanism cannot use
combat to obtain information. If only a receiver victory can change the
policy under imitation, M may be replaced by (1-s)(2b-1), provided that
stronger coupling is actually verified. We use the more generous M.

Choose

\[
0\le\eta\le\frac{p d_S}{d_S+M},\qquad
\lambda\ge1+\frac{\eta}{1-p}.
\]

Define A_0=(1-p)(1+lambda)+eta and L_0=(1-p)+eta. Then

\[
\boxed{L_S+\lambda L_R\ge
K_{\lambda,\eta}:=b^2+(2b-1)\eta
-\frac{b^2L_0^2}{A_0}+(1-\lambda)B.}
\tag{6}
\]

To check it, subtract eta*d from the objective before minimizing policy
moments. Low policy has coefficient A_0 and minimizer b L_0/A_0.
High policy has coefficient A_1=p(1+lambda)-eta and linear coefficient
-2P_1, where P_1=p(b+1+lambda)-b eta. Since
P_1-A_1=pb-(b-1)eta>0, its minimum on [0,1] is at 1. The remaining
cost-and-IC terms are

\[
[(1-p)+\eta]C_0+(p-\eta)C_1+\eta d\ge0,
\]

by (5) and (p-eta)d_S>=eta M. Payment remainders have coefficients
(1-p)(lambda-1)-eta and p(lambda-1)+eta, both nonnegative. Variance,
low-square and high-boundary remainders are nonnegative as in (2).
This proves (6), including stochastic policies and arbitrary finite
communication satisfying the coupling premises.

For b=1,p=1/2,B=1/5,d_S=5, choose lambda=2,eta=5/12. Then

\[
L_S+2L_R\ge179/230\approx .77826087.
\tag{7}
\]

The ordinary no-combat bound is .8. Finite destructive cost thus supplies
an explicit, slightly weaker control that allows information obtained by
combat. It neither deletes attacks nor presumes that every attack is
inferior to every compromise.

## 3. How to use the bound without overstating it

If a sequentially implementable goal package leaves R loss at most its
actual reservation r and S loss strictly below K_{lambda,eta}-lambda*r,
it beats all qualifying fixed-sender-goal mechanisms, even those using
funded ordinary signals and the specified contests. A matched protected
delegate can still reproduce the goal package: its type protection breaks
the imitation premise and is an informative separate control.

Large payment capacity, cheap protected state evidence, cheap matched
delegation or a costly goal package can favor those alternatives. Small
package costs and binding financial/resource limits can favor genuine
change. Neither comparison supplies a distribution over natural agents.
An initial bargaining and continuation construction must establish the
reservation pair and package before this frontier becomes an adoption
result; 080 investigates that link with explicit late renegotiation.

## 4. A receiver whose original target already has offset a

For original receiver loss (y-theta-a)^2, the same calculation gives

\[
L_S+\lambda L_{R_a}\ge b^2+(2b-1)\eta+\lambda a^2
-\frac{[b(1-p+\eta)+\lambda a(1-p)]^2}
       {(1-p)(1+\lambda)+\eta}+(1-\lambda)B.
\tag{8}
\]

Use the same payment/cost conditions and eta bound as above, and require
the displayed low-policy minimizer to lie in [0,1]. The high minimum is
still at 1 since its derivative numerator at that boundary is
p(b+lambda*a)-(b-1)eta>0. This treats a as an actual original preference
parameter, rather than silently substituting a successor's welfare for
its founder's welfare. For a=.3,b=1,p=.5,d_S=5,B=.01,lambda=12,eta=5/12,
the right side is 10953/8300. A matched protected delegate remains outside
the imitation class for the same reason as before.
