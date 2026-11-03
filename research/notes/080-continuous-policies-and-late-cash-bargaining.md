# Continuous policies and actual post-refusal renegotiation

**R0004 mathematical construction; analytical and exact-arithmetic self-check.** This note
enlarges the staged game to continuous policies and a specified late
cash-bargaining window. It derives the changed signaling assessment rather
than retaining the old assessment after adding a profitable bargain.

## 1. What the late window permits

After an original sender publicly refuses the diagnostic/update route,
the receiver may quote a policy and a payment. The sender can accept,
reject or attack. Rejection leaves the receiver choosing its best policy
at the resulting belief; in the selected assessment that belief is low.
An accepted quote is a funded exchange of a dispatched policy command
for payment, with physical transaction expenses e_S,e_R>0. This is
binding current execution, not a free promise about every future action.

The sender's remaining transferable budget is delta>=0. Receiver cash
received earlier is at its remote project and cannot make the return trip
before this episode closes. Sender cash is escrowed and becomes available
for this window on the public refusal event. Before refusal, neither can
fund an additional on-the-spot payment. This event restriction is a
declared agreement/transport technology, not a consequence of utility
self-knowledge. More general live cash and preinstalled contingent menus
are a separate enlargement discussed in 081.

Let d=b-a. At a low belief, a quote y=a+x with payment delta leaves
the original sender indifferent to rejection at a if

\[
\delta+e_S=2d x-x^2,\qquad
x=d-\sqrt{d^2-\delta-e_S}.
\tag{1}
\]

Assume 0<x<=d/2, a+x<=1, delta+e_S<d^2, and that the receiver's net
gain delta-x^2-e_R is positive. With receiver proposal rights, using the
full budget is optimal: for any feasible x the largest acceptable payment
is 2d x-x^2-e_S, and its net benefit is
2d x-2x^2-e_S-e_R, increasing up to d/2. For x beyond the budget-binding
point, revenue remains capped while the receiver's policy cost rises.

Write

\[
\ell=x^2-\delta+e_R<0.
\]

The current receiver's low-state continuation loss is ell. The old
sender's continuation loss remains (b-a)^2: payment and transaction
cost exactly equal its policy gain. A high sender imitating this refusal
instead loses b^2+h-2x, where h=(1-a)(2b+1-a). It therefore prefers
sufficiently inexpensive completion at policy 1. A vanishing tremble
sequence can put low probability mass above high mass after a rejected
quote: low is indifferent at the quote, whereas high strictly prefers
acceptance to the low-belief rejection policy. The low rejection belief
must be supplied consistently; it is not an inference from rejection
alone.

The quote is an actual renegotiation of the previous low default. Its
receiver proposer extracts the sender's entire gain at the specified
tie-breaking equilibrium. Sender proposal rights instead leave it a
strict trade surplus and change the earlier signaling incentives. The
allocation of bargaining rights is therefore a substantive parameter.

## 2. A positive compromise offset admits continuous policy choices

Suppose a>0 and every on-path claim posterior mu_i=P(low|claim prefix)
is smaller than a. The receiver's best unchecked policy on the *entire*
interval [0,1] is then 1: its unconstrained quadratic optimum is
1-mu_i+a>1. This supplies a continuous-policy class for the earlier
upper-bound action, without relying on a coarse grid near 1.

Put D=(1-a)^2, G=D-ell, and mu_{N+1}=0. The receiver indifference
recursion becomes

\[
\mu_i=\mu_{i+1}+(1-\mu_{i+1})r_i/G
      =1-\prod_{j=i}^N(1-r_j/G).
\tag{2}
\]

Every refusal now obtains ell, so G replaces D at **every** stage.
Only changing the final-stage recursion, as for 078's final-only hostile
controller, would be incorrect here. Sender low indifference is unchanged:

\[
q_1=1-f/g,\quad q_i=1-c_{i-1}/g\ (i>1),\qquad
g=(1-a)(2b-1-a).
\tag{3}
\]

Low claim/progress probabilities follow the same Bayes ratios as 073.
Use 0<mu_1<min(a,1-p), positive costs below the applicable low gains,
and enough remaining high completion advantage. A simple sufficient high
condition is sum_j c_j<h-2x; less restrictive remaining-cost conditions
can also be used. Combat must be compared using the actual physical
payoffs. In particular its opportunity cost now includes the low-state
cash revenue forgone on a contest.

Let Q_0=1,Q_i=product_{j<=i}q_j, E=f+sum_i c_i Q_i, and

\[
F=p\sum_i\frac{Q_{i-1}\mu_i(1-q_i)}{1-\mu_i},\qquad
m=\frac{pG\mu_1}{1-\mu_1}.
\]

F is the actual low-state unchecked acceptance probability; m equals
physical request expense plus G*F. With an initial payment T and genuine
receiver installation expense j_R, the original losses are

\[
L_S=(1-p)(b-a)^2+p b^2+pE+T+e_S^{early},
\tag{4}
\]

\[
L_R=(1-p)[(a+x)^2-\delta+e_R]
 +m+2a(1-a-x)F-T+j_R+e_R^{early}.
\tag{5}
\]

The current receiver instead has policy/material loss
p a^2+(1-p)ell+m, less the sunk initial payment. The extra term in
(5) preserves the original receiver's evaluation of a successor goal.
The initial payment is already in (4)-(5); the late payment is already
included through (1) and ell. Neither is counted twice.

## 3. The original receiver's continuous-policy disagreement game

For a=0, setting every unchecked policy to 1 is not optimal on [0,1].
At posterior mu the receiver instead chooses y=1-mu. Keep the actual
known-low late bargain and let ell denote its loss. Define z_{N+1}=0.
For each stage, choose the smaller root

\[
\mu_i^2-(1-\ell+z_{i+1})\mu_i+(r_i+z_{i+1})=0,
\qquad
z_i=\frac{\mu_i(1-\mu_i-\ell)}{1-\mu_i}.
\tag{6}
\]

The root must lie in the increasing, small-posterior region and satisfy
the usual Bayes and combat inequalities. It exceeds mu_{i+1} when r_i>0.
To derive (6), subtract the typewise low continuation mu_i*ell from
both stopping and requesting losses. Requesting costs
r_i+(1-mu_i)z_{i+1}; stopping costs mu_i(1-mu_i-ell).

The low sender's unchecked gain is now

\[
g_i=2b(1-\mu_i)-(1-\mu_i)^2,
\quad q_i=1-e_{i-1}/g_i,
\]

with e_0=f,e_{i-1}=c_{i-1} thereafter. High unchecked acceptance has
extra loss B_i=2b mu_i+mu_i^2 above policy 1. Therefore

\[
L_S^{out}=b^2+p\left[f+
\sum_i Q_{i-1}(1-q_i)B_i+\sum_i Q_i c_i\right],
\quad L_R^{out}=(1-p)\ell+p z_1.
\tag{7}
\]

These formulas establish the disagreement values from a selected
continuous-policy continuation, including its actual late payment. They
do not assign an arbitrary reservation payoff to make a package succeed.

With no cash receipt on combat, the stopping-versus-combat comparison is
mu(1-s-mu)<=d_R. Its smaller boundary root, when real, is
[(1-s)-sqrt((1-s)^2-4d_R)]/2. Low sender mixing at a combat checkpoint
uses denominator d_S+g_i-s(2b-1). This identifies the corresponding
combat boundary; a globally complete mixed checking/combat assessment
for arbitrary parameters still requires the remaining stage checks.

## 4. Constructive use and remaining closure

Equations (1)-(7) describe an enlarged, parameterized continuation class
with actual low-state renegotiation and continuous policy choices. They
support an initial funded-adoption construction in 081. The information,
cash-release, available hardware and proposal-window assumptions must
be checked there; they are not supplied by these payoff equations.
Freer cash circulation or a cheap preinstalled binding menu can favor
ordinary trade, while a suitably priced genuine update or matched
delegate can supply information at lower cost than ordinary incentive
payments. Both comparisons remain part of the agreement-design question.
