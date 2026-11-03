# Sharp ordinary frontiers and the direction of goal bargaining

**R0004 derivation; analytical self-check.** This refines 083's supporting
inequality into an attained frontier on a stated range, and derives the
direction in which a negotiated goal changes both parties' original
welfare. The stronger ordinary authority remains explicitly a control;
its commitment is not silently supplied to the uncommitted staged game.

## 1. An attained frontier with the receiver's actual reservation value

Set b=1, a_0=0, h=1-p, D_c=d_S+M, beta=d_S/D_c and gamma=d_R/D_c.
Here D_c is a contest denominator, distinct from the staged D=(1-a)^2.
Assume D_c>=1, h>p gamma, and M>0. Put

\[
A=h+p\beta,\qquad c=p\gamma,\qquad
\lambda_{min}=A/(h-c),\qquad
x_c=\frac{1}{1+hM/d_R}.
\]

For d_R=0 use the limiting x_c=0. In the audit-dominant part of 083's
frontier, the ordinary menu has low policy x, both payments B, and
high contest probability w=(1-x)^2/D_c. Its losses are

\[
S(x)=p+B+A(1-x)^2,\qquad
R(x)=(h+c)x^2-2cx+c-B.
\tag{1}
\]

The multiplier supporting x is

\[
\lambda(x)=\frac{A(1-x)}{(h+c)x-c}.
\tag{2}
\]

It satisfies 083's payment-cap condition exactly when x<=1/2.
The combat-versus-burn condition lambda*d_R<=M is exactly x>=x_c.
For x in [x_c,1/2], all those bounds apply and the stated menu attains
them. Thus, for a reservation r with r=R(x) in that range, the minimum
accepted ordinary sender loss is S(x), where

\[
x(r)=\frac{c+\sqrt{(h+c)(r+B)-ch}}{h+c}.
\tag{3}
\]

The increasing root applies since x>c/(h+c); below that vertex this
parameterization is not the relevant Pareto branch. Equations (1)--(3)
are a constrained optimum, not just a menu that happened to work.

There is also a useful adjacent segment. Keep x=1/2 and t_1=B, but
reduce the low payment t_0 from B. Low IC then needs

\[
w=(1/4+t_0-B)/D_c.
\]

For B-1/4<=t_0<=B this is a probability, and high IC still holds.
Receiver loss rises while sender loss falls, with slope
dS/dR=-lambda_min. This attains the supporting line

\[
S\ge p+B+\frac{A}{h-c}(h/2-B-r)
\tag{4}
\]

for R(1/2)<=r<=h/2-B. Actual negative t_0, if any, requires receiver
funding; the generous upper comparison permits it, and the examples
used below have positive t_0. Richer reservations outside these two
segments require their own active constraints, not extrapolation.

## 2. Finite punishment and combat strength change this frontier

For fixed x, increasing M lowers w, both parties' expected audit damage,
and therefore both losses in (1), strictly when the relevant damage is
positive. Every previously feasible menu remains available, so the
optimal accepted sender loss is weakly decreasing in M. With a binding
receiver reservation in the interior of (3), it is strictly decreasing:
the saved receiver loss also permits a slightly higher x. This is a
conditional improvement of an ordinary control, with smaller actual
contest frequency at the fixed target. It is not a claim that greater
punishment causes greater realized violence.

Here M=(1-s)(1+P_max). Holding physical damage, inventories and the
disagreement continuation fixed, a greater sender win probability s
reduces the receiver's evidence-and-punishment advantage. It raises the
cost of that ordinary control relative to genuine information-bearing
accommodation. This conclusion concerns an inspection mechanism, not
every game in which strength changes.

For 083's p=.5, s=.05, d_S=5, d_R=.01 and original disagreement value,
the sharp ordinary minimum is about .88054438 at P_max=15. The a=.42
goal package costs S about .86937399. Raising usable punishment capacity
to 25 lowers the ordinary minimum to about .86841010, below that fixed
package. These are the same positive-cost policies, evaluated against the
same reservation; the crossing identifies a real repair obligation.

The crossing can be solved without a numerical optimizer. Write
Q=r+B, H=S_goal-p-B, t=d_R/d_S and u=1-x. At equality,

\[
h(1-t)u^2-2hu+h+tH-Q=0,
\quad
D_c^*=\frac{p d_Su^2}{H-hu^2},
\quad
P^*=\frac{D_c^*-d_S}{1-s}-1.
\tag{5}
\]

Use the root on the frontier and require H-hu^2>0. Here it gives
P^* approximately 23.87393. Such a punishment exceeds the original
20-unit stock after combat. It belongs to an enlarged material class;
its mechanism also needs actual targeting, work and binding authority.
The crossing alone does not show that all renegotiated goals lose there.

## 3. The negotiated target has a strict original-welfare tradeoff

Return to the full-budget staged package, b=1 and 0<a<1/2. Write
g=D=(1-a)^2 and e=(f,c_1,...,c_N). Positive e_j<D give

\[
E(D)=D\left[1-\prod_{j=0}^{N}(1-e_j/D)\right].
\tag{6}
\]

This is 073's telescoping expression for high-type implementation
expense. Its derivative is

\[
E'(D)=1-\prod_j(1-e_j/D)
-\sum_j(e_j/D)\prod_{k\ne j}(1-e_k/D)\ge0.
\]

The right side is the probability of at least two successes in
independent Bernoulli trials of probabilities e_j/D. Consequently

\[
\frac{dL_S}{da}=-2(1-a)\{(1-p)+pE'(D)\}<0.
\tag{7}
\]

The original receiver's loss is
h a^2+m(D)+2a(1-a)F(D)-B+J. It strictly increases in a on this interval.
For m=pD(P^{-1}-1), P=product_j(1-r_j/D), differentiation gives

\[
m'(D)=\frac pP\left[1-P-\sum_j\frac{r_j/D}{1-r_j/D}\right]<0.
\]

To check F without dropping its changing reach probabilities, couple
independent uniform variables for the first unchecked stop. Its hazards
are e_{i-1}/D. Lower D moves that stop weakly earlier. At a stop i its
value is the suffix odds mu_i/(1-mu_i), and at no stop its value is zero.
Those odds rise both when D falls and when i moves earlier. Thus F is
nondecreasing as D falls. Finally 2a(1-a) increases for a<1/2, and
h a^2 increases strictly. This proves the claimed receiver direction.

Within this fixed-transfer package family, the sender proposer therefore
selects the largest acceptable target, and the receiver proposer selects
the smallest target accepted by S, subject to the actual finite goal
bank. The interior witnesses in 083 are conservative feasible proposals;
they need not be the optimal targets. Proposal rights redistribute gains
along this tradeoff. An equally priced protected delegate implements the
same tradeoff while preserving the sender's terminal utility.

## 4. The repaired family survives every contest win probability

For P_max<=15 and any s in (0,1), M<=16. Use that common upper bound in
083's inequality, with eta=p(5+.016)/21 and lambda=8/5. The proof only
needs d>=-16w_1, so it remains valid when actual M is smaller. One must
not mechanically maximize eta separately at each s while retaining a
lambda that then violates the payment condition.

The same concavity proof in p gives endpoint gaps greater than
.0095600 and .0065032 before rational-goal rounding. The rounding cost
is at most .000011000055. The uniform strict gap thus exceeds .00649
for every p in [.45,.55] and every such s. The comparison bound also
holds at the degenerate limiting strengths; the finite assessment here
uses positive chances for both winners. Both disagreement and the
goal package stay peaceful throughout this strength comparison: their
small checking posteriors remain below even the s=0 contest threshold,
and sender damage 5 exceeds its possible policy gain.

This broadens the parameter result while holding the physical technology,
cash transport and priced recognition interface fixed. It gives no
population distribution over those technologies and no assertion that
strength can change in reality without correlated changes in damage,
information or control over infrastructure.
