# A welfare bound for ordinary signals, burns and payments

**R0004 mathematical derivation; contributing-agent self-check.** This strengthens
069's ordinary policy/payment comparison by allowing real, observable costly
signals. It also identifies a constructive region for goal-based information.
The bound is a mechanism frontier, not by itself an equilibrium-selection or
initial bargaining theorem.

## 1. A generous fixed-goal comparison class

Let theta be binary with P(theta=1)=p in (0,1), and original utilities

\[
u_S=X_S-(y-\theta-b)^2,\qquad u_R=X_R-(y-\theta)^2,
\quad 1\le b\le2,\quad 0\le y\le1.
\]

An ordinary mechanism preserves these goals. The sender can imitate either
type's complete strategy, and the physical policy/payment/cost law under an
imitation is the same as under that type. This permits arbitrary finite
communication, lotteries, binding policy/payment menus and type-independent
observable burns. It excludes a protected state sensor, a successor who
actually uses a different goal, and a combat outcome that reveals the real
state; those are consequential different information technologies.

Write m_t=E[Y|t], q_t=E[Y^2|t], C_t>=0 for real sender output destroyed or
spent in signaling, and t_t for a net payment from S to R. Let K_t=C_t+t_t.
Allow subsidies generously. Require only t_1<=B; enforcing a cap in both
states can further restrict the class. Sender incentive compatibility gives

\[
d:=K_1-K_0-2b(m_1-m_0)+(q_1-q_0)\ge0.
\tag{1}
\]

The actual original losses are

\[
L_S=(1-p)(q_0-2bm_0+b^2+K_0)
 +p(q_1-2(b+1)m_1+(b+1)^2+K_1),
\]

\[
L_R=(1-p)q_0+p(q_1-2m_1+1)-(1-p)t_0-p t_1.
\tag{2}
\]

Any real receiver execution expense is nonnegative and can only strengthen
the following lower bound. Providing binding authority for free is a
deliberately favorable control, not a claim that it is free in the game.

## 2. Exact supporting inequality

Set rho=p/(1-p). Direct substitution of (1) into (2) gives

\[
\boxed{L_S+\frac{L_R+pB}{1-p}
       \ge \frac{b^2}{2}+p(2b-1).}
\tag{3}
\]

The exact nonnegative remainder is

\[
\begin{aligned}
&L_S+\frac{L_R+pB}{1-p}
 -\left[\frac{b^2}{2}+p(2b-1)\right]\\
={}&2(q_0-m_0^2)+\rho(q_1-m_1^2)
 +2(m_0-b/2)^2\\
&+\rho(1-m_1)(3-2p-m_1)
 +C_0+\rho(B-t_1)+p d.
\end{aligned}
\tag{4}
\]

Each term is nonnegative on the stated domain. No assumption that the
ordinary sender cannot burn resources is used: C_1 may be arbitrarily large.
The proof uses low IC only and therefore also applies to the subset that
satisfies both types' IC and actual participation. For p=1/2,b=1 the bound
is simply L_S+2L_R+B>=1.

Suppose a bargain must leave R original loss at most r. Every ordinary
mechanism in this generous class then leaves S loss at least

\[
\frac{b^2}{2}+p(2b-1)-\frac{r+pB}{1-p}.
\tag{5}
\]

This is an informative cost boundary for *both* agents' objectives. The
earlier receiver-only payment bound cannot be applied once observable burns
are admitted: a burn can make a low type reject a profitable false report.

## 3. Sharpness and what it requires

Choose deterministic policies y_0=b/2, y_1=1, C_0=0 and t_1=B. To attain
L_R=r, set

\[
t_0=b^2/4-\frac{r+pB}{1-p},\qquad
C_1=-b^2/2+2b-1-\frac{r+B}{1-p}.
\tag{6}
\]

When C_1>=0 and the payments are actually funded, low IC binds; high IC
holds because the high policy benefit exceeds the low benefit by 2-b>=0.
This attains (3). Participation and binding execution remain separate
conditions. A cap in both states also needs t_0<=B. Nonnegative payments
further need t_0>=0; the bound itself generously permits negative t_0.

For b=1,p=1/2,B=.2,r=.005, the attaining menu has y_0=.5,y_1=1,
t_0=.04,t_1=.2,C_1=.09. Its losses are L_S=.79,L_R=.005. This control is
strictly stronger than ordinary cheap reporting, and it must not be omitted
when presenting a goal-change advantage.

## 4. Constructive room for negotiated goal-based information

Under perfect information, the efficient original-goal low policy is a=b/2
and the high policy is 1. Their total original quadratic loss is

\[
W_*=(1-p)b^2/2+p b^2=b^2(1+p)/2.
\]

Let a genuinely adopted goal/diagnostic package implement these decisions
approximately, with actual total extra original loss K>=0, so that total
loss is W_*+K. This K must include communication, verification, installation,
false positives, infrastructure and transaction costs. An enforceable
state-independent payment can leave R loss r and S loss W_*+K-r, *if*
its amount fits the real payment capacity. It strictly improves S's frontier
over all ordinary mechanisms (5) whenever

\[
\boxed{K<p\left[2b-1-b^2/2-\frac{B+r}{1-p}\right].}
\tag{7}
\]

In the zero-extra-cost limit the required payment is
T_*=(1-p)b^2/4-r. For each b in [1,2), there is a nonempty open interval

\[
(1-p)b^2/4-r < B
 < (1-p)(2b-1-b^2/2)-r
\tag{8}
\]

in which payment is feasible and (7) has a strictly positive right side.
Its width is (1-p)(-3b^2/4+2b-1)>0. Sufficiently small **positive** package
and payment costs retain strict margins. This is a robust conditional
opportunity for genuine goal change, or an equally capable matched delegate;
it is not evidence that either technology is generally cheap or available.

The staged C_a continuation in 073 supplies a candidate package, with actual
losses to be computed below. R's original adoption, current successor
choices, funded transfer, stage timing and the relevant outside option r
must all be implemented. In particular, r is not freely selectable by an
author: a receiver with a better available refusal/renegotiation option can
demand it. A beneficial frontier point alone does not establish proposal,
adoption, stability or prevalence.

## 5. Original receiver welfare in staged compromise

Use 073's peaceful assessment. Let Q_0=1, Q_i=product_{j<=i} q_j and define
the actual low-state false-positive frequency

\[
F=p\sum_{i=1}^N\frac{Q_{i-1}\mu_i(1-q_i)}{1-\mu_i}.
\tag{9}
\]

The current receiver's excess loss is m=pD mu_1/(1-mu_1). If V_paid is
the expected physical expense of its requests, then m=V_paid+D F.
Its original target theta instead loses 1-a^2 on a low false positive,
so archived original receiver loss, before the initial payment, is

\[
L_R^{old}=(1-p)a^2+m+2a(1-a)F+j_R,
\tag{10}
\]

where j_R is its actual initial implementation expense. Together with
073's sender loss, the total before a lossless transfer is

\[
W=(1-p)[(b-a)^2+a^2]+pb^2+pE+m+2a(1-a)F+j_R.
\tag{11}
\]

For a=b/2, this supplies K=pE+m+2a(1-a)F+j_R in (7), before any further
physical/escrow overhead. Original and current receiver welfare are thus
kept separate. An actual payment T reduces (10) and increases sender loss
by T; it does not create material or alter the conservation ledger.

## 6. Scope and next checks

The successful region (7)-(8) challenges the inference that permitting
ordinary transfers and costly signals automatically exhausts the gains from
goal-based information. The matching limiting region is concrete: a cheaper
matched delegate can displace goal change, and sufficient payment capacity
can replace a burn by an ordinary transfer. High package cost can consume
the entire improvement margin. These comparisons require the same actual
authority and funded resources, with stronger controls labeled.

Combat can reveal the real state and therefore violates the imitation
premise behind (1). A separate coupling/damage bound is needed for that
enlargement. Likewise, unrestricted later payments can induce renegotiation
of the low default. The contest and funded-refusal enlargements are addressed in 079–084,
including a stronger punitive control. Unrestricted circulating cash remains
open; the displayed ordinary-mechanism theorem retains its own narrower scope.
