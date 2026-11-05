# Asymmetric shared processes and negotiated goal weights

R0006 strengthening of the additive production class. Blue and Red can
benefit very differently from each other's research. This note solves the
productive agreement frontier, rather than fixing equal common weights,
and distinguishes transfer-free reciprocity from a paid one-way service.
Convex optimization and bargaining machinery are conventional; the
application and its implementation distinctions are the contribution.

## 1. Separate final values and asymmetric intermediate benefits

Let actual final counts be

`q_B=Q_B+a_B x_B+h_BR x_R-c_B x_B^2/2-K_B`,
`q_R=Q_R+a_R x_R+h_RB x_B-c_R x_R^2/2-K_R`.              (1)

All a_i,c_i are positive, h_ij>=0, and originals value only q_i.
Finite work, materials and effort caps cover the profiles below as in
note 115. The expense K_i is actual foregone production under the chosen
implementation. In the original continuation, x_i^F=a_i/c_i. Additive
spillovers do not affect the other's own marginal effort incentive.

Suppose both adopt the common criterion `W_z=q_B+z q_R`, z>0. Strict
joint concavity gives its unique effort maximum

`x_B=(a_B+z h_RB)/c_B`,
`x_R=(a_R+h_BR/z)/c_R`.                                 (2)

Define `X=h_RB^2/c_B`, `Y=h_BR^2/c_R`. Before transfers, gains relative
to the actual original effort continuation are

`G_B=Y/z-X z^2/2-K_B`,
`G_R=X z-Y/(2z^2)-K_R`.                                (3)

Direct substitution proves these formulas. They exhibit the separate
effects: extra useful knowledge from the partner, extra own research
expense, and actual installation expense. An exclusive final preference
does not have to value the partner's output initially to prefer a
reciprocal change producing positive (3).

## 2. The entire positive-weight opportunity frontier

First let X,Y>0. Put

`z_0=(Y/X)^(1/3)`, `u=z/z_0`,
`B_0=X^(1/3)Y^(2/3)`, `R_0=X^(2/3)Y^(1/3)`.

Then

`G_B=B_0(1/u-u^2/2)-K_B`,
`G_R=R_0(u-1/(2u^2))-K_R`.                             (4)

At zero expenses both are strictly positive exactly when

`2^(-1/3)<u<2^(1/3)`.                                  (5)

Thus arbitrarily unequal but positive two-way useful sharing permits a
strictly beneficial negotiated common goal. Equal weights z=1 need not
lie in this interval. Setting u=1 always gives gross gains B_0/2 and R_0/2,
so `K_B<B_0/2`, `K_R<R_0/2` is a simple funded sufficient region.

The exact nonnegative-cost frontier is also given by (4). Define
`f_B(u)=1/u-u^2/2`, `f_R(u)=u-1/(2u^2)`. The former is strictly decreasing
and the latter strictly increasing. Let u_B solve f_B=K_B/B_0, and u_R
solve f_R=K_R/R_0 within the nonnegative-gain interval whenever such roots
exist. A strict mutually beneficial goal exists exactly when u_R<u_B.
Equivalently, some u in (5) satisfies both inequalities in (4).

For the exact interior classification, fund caps at least
`E_B=(a_B+z_high h_RB)/c_B` and
`E_R=(a_R+h_BR/z_low)/c_R`, where
`z_low=(Y/(2X))^(1/3)` and `z_high=(2Y/X)^(1/3)`.
Larger finite caps are permitted. Thus all potentially strictly beneficial
weighted optima above fit the physical technology.

This is a productive frontier, not just a menu of attractive goals. Every
W_z maximizes a positive weighted sum of counts over the physical effort
set. Its strict concavity supplies the unique target. Conversely, the
Pareto frontier supported by strictly positive weights is obtained by them;
supporting-hyperplane arguments apply to the downward complete concave
output set, as in note 134. At weights outside [z_low,z_high], clipping
effort to the stated caps creates no omitted mutual improvement. Above
z_high, Blue's received benefit Y/z decreases and its own extra research
expense increases until capped; its gain is already nonpositive at
z_high. Below z_low the symmetric argument applies to Red. Thus every
strictly beneficial supported point is on the interior frontier (4).
Along it,

`d G_R/d G_B = -R_0/(B_0 u)`,

and the second derivative is negative because f_B'<0. Thus the frontier
is strictly concave. Endpoints that maximize just one color are limiting
weights; strict mutual improvements considered here lie in the finite
interval (5), whose effort requirements can be funded by finite caps.

## 3. A bargaining calculation and its actual implementation scope

For a specified bargaining weight alpha in (0,1), maximize
`G_B^alpha G_R^(1-alpha)` on the strictly beneficial frontier. This is
an allocation-selection criterion, not an intrinsic utility assigned to
either original. Strict concavity gives a unique optimum when the feasible
positive-gain region exists. At zero expenses it has the exact solution

`u^3=(2-alpha)/(1+alpha)`.                              (6)

To prove it, write t=u^3. Apart from constants, the gains are
`(2-t)/(2t^(1/3))` and `(2t-1)/(2t^(2/3))`.
The first-order log derivative has the sign of
`(1-alpha)/(2t-1)-alpha/(2-t)`, giving (6) and its unique crossing.
At alpha=1/2, u=1. More Blue bargaining weight lowers z and favors Blue's
output. With positive expenses, the same frontier gives a unique interior
bargaining optimum, but (6) must be replaced by its actual first-order
condition. A larger K_B shifts the selected u downward, and a larger K_R
shifts it upward, while strict positive gains remain feasible.

An actual finite take-it-or-leave-it offer protocol can instead select
the smallest grid z that gives Red a strict improvement, since G_B is
strictly decreasing in z. Neither alpha nor that offer right is inferred
from physical overlap. They represent a selected bargaining procedure
whose timing and responses must be part of the game.

For initial installation, use note 131's reliable conditional controller
interface at the agreed z. On failed reciprocity the counterpart retains
its original effort. Since the additive counterpart does not change effort
in response to one's unilateral commitment, the best own-color output
against that original is precisely the ordinary baseline. Therefore
`G_B>0` and `G_R>0` support strict reciprocal installation against that
unilateral production-controller menu, after all actual expenses are
included. Once both change, strict common concavity gives (2), and the
global maximum supplies current-goal continuation stability. Combat and
intermediate execution still require note 115's all-history bound or an
actual remaining-delivery comparison. This connects the frontier to
selected actual adoption under a specified interface; it does not identify
an arbitrary bargaining criterion with an equilibrium of every game.

Matched binding ordinary controllers reach the same frontier with their
own implementation expenses. Equal costs permit both mechanisms to be
optimal; cheaper available ordinary control can displace genuine change.
An improved outside partner also raises the participation benchmark. The
ordinary effort baseline in (3) is not silently retained in those cases.

## 4. One-way sharing and a physically funded transfer repair

If X=0<Y, Blue benefits from Red's research but Red receives no reciprocal
productive benefit. Equation (3) gives a strict Red loss for every finite
positive z when K_R>=0. This transfer-free weighted-goal class therefore
needs a repair; merely declaring equal common goals does not fund consent.
The symmetric statement holds when Y=0<X.

Suppose the agents can transfer convertible useful work before finishing,
with one transferred unit costing Blue one blue clip and enabling one red
clip. At z=1 the gross gains are `Y-X/2` and `X-Y/2`. A net transfer T
from Blue to Red gives

`G_B=Y-X/2-K_B-T`,
`G_R=X-Y/2-K_R+T`.                                    (7)

Both gains can be made strictly positive exactly when

`K_B+K_R<(X+Y)/2`,                                    (8)

provided the actual transferable reserve covers the chosen T. The common
sum achieves the largest total output; the transfer only divides it.
For X=0, one can choose
`Y/2+K_R<T<Y-K_B`. The beneficiary pays for a service that is costly to
the provider, and both exclusive originals then favor the arrangement.
Actual escrow, delivery and verification expenses belong in K, and their
availability is substantive. Unit convertibility is not implied by
shared knowledge: with conversion losses, replace (7) by the actual rates.

At the exactly one-way endpoint, Blue's own productive effort already
maximizes the common sum, so its new other-color concern need not change
its effort. A cheaper mixed arrangement—Blue retains its utility and pays
a binding transfer while Red changes its goal—can displace an unnecessary
positive-cost Blue update. Ordinary service contracting can also implement
the gain. Thus (8) proves a funded cooperation opportunity and an available
two-change continuation, while the selected number of genuine changes
depends on the actual control costs. For strictly two-way sharing, both
productive incentives move under (2), and section 3 gives the reciprocal
adoption construction.

## 5. What increased overlap means in this asymmetric class

At zero expenses and fixed bargaining weight alpha, formula (6) keeps u
fixed. Raising either positive X or positive Y then raises both founders'
gains in (4), with the other parameters held fixed. The negotiated z adapts
to the new asymmetry. At a fixed old z, by contrast, raising X lowers
Blue's gain and raises Red's, because Blue bears the additional induced
research expense. A technology comparison with renegotiated weights is
therefore a different statement from the response of agents already
committed to one old goal.

After genuine common adoption, later decisions use that current common
criterion. Its agents need not redesign it to restore every founder's
previous share after an innovation. An initial contingent goal or later
available bargain can address that issue, but needs its own current-goal
proof. This note compares new agreements by initially exclusive agents.

Strict positive-gain regions survive small continuous changes of the
physical coefficients and costs. Reciprocity becomes demanding when one
direction nearly disappears: even with K_B=0, the largest Red gain without
harming Blue is `3*2^(-5/3) X^(2/3)Y^(1/3)`, which tends to zero with X.
Real transfers repair that disappearing transfer-free margin when (8)
holds. These are useful structural distinctions between amount, direction,
contractibility and convertibility of common processes, without treating
either special symmetry or one-way obstruction as a population claim.
