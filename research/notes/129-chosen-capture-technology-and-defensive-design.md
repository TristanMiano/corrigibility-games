# Chosen capture technology, defensive design and bargaining timing

R0006 intervention analysis extending notes 117 and 121. This supplies
actors, funded actions and actual choices for changes in asset reuse. It
separates an intervention causing combat from a feasible defensive repair,
then tests the repair against an earlier agreement. The productive research
and goal-change mechanisms of 114–128 remain separate available technologies
when specified; none is assumed to arise from asset convertibility alone.

## 1. Asymmetric physical conversion and the bargaining frontier

Let native useful-work bundles be r_B,r_R. Blue can turn one unit of Red's
bundle into alpha Blue clips, and Red can turn one unit of Blue's into beta
Red clips, with alpha,beta in [0,1]. Native conversion yields one own-color
clip per unit. Costs and capacities are in final-clip equivalents through
these declared converters; they are not conserved energy or utility.

The downward-complete peaceful frontier is

`q_B+alpha q_R<=r_B+alpha r_R`,
`beta q_B+q_R<=beta r_B+r_R`, `q_i>=0`.                  (1)

It follows by allocating each native bundle between its two possible uses.
Equivalently the efficient boundary consists of the two line segments
joining (r_B+alpha r_R,0), (r_B,r_R) and (0,beta r_B+r_R).
For alpha beta=1 they collapse to the ordinary total-budget line.

A fight destroys a fraction 1-delta of recoverable production, where
0<delta<1 incorporates material loss, finite work consumed, damaged
infrastructure, recovery effort and the remaining time window. Blue wins
with probability p determined by the specified strengths. Actual expected
original outputs after a fight are

`d_B=p delta(r_B+alpha r_R)`,
`d_R=(1-p)delta(r_R+beta r_B)`.                          (2)

The two frontier slacks at that vector are

`M_B=(1-delta)(r_B+alpha r_R)`
`      +(1-p)delta(1-alpha beta)r_B`,
`M_R=(1-delta)(beta r_B+r_R)`
`      +p delta(1-alpha beta)r_R`.                      (3)

Expansion verifies (3). Funded peaceful implementation consuming native
work k_B,k_R is individually rational exactly when
`k_B+alpha k_R<=M_B` and `beta k_B+k_R<=M_R`. A rise in alpha changes
both capture value and peaceful transfer efficiency, not just one side
of a bargaining comparison. Zero implementation costs leave a weakly
dominating peaceful allocation in this particular technology.

**Execution condition.** An affordable allocation is not by itself a
stable sequence of deliveries. For the peaceful executions below, let the
paid controller consume the two native stocks in common fractions tau and
produce tau of each promised final color, with adequate simultaneous
throughput. It retains production authority; each agent still has the
physical attack action. Already produced own-color clips count regardless
of who holds them. At fraction tau, remaining expected combat production
is bounded by `(1-tau)d_i`, using the pre-controller-cost threat d_i in
(2); paid implementation work and any additional recovery expense only
lower that bound. Then an offer q_i>=d_i satisfies
`tau q_i+(1-tau)d_i<=q_i` at every checkpoint. Thus initiating combat
cannot improve its original count during paced delivery. Exhausting the
finite useful work ends production and further recoloring capability.

This is an actual controller/capacity premise with cost included, not an
assumption that a verbal division binds future actions. Paying one side
fully first can violate the remaining inequality and needs a different
safeguard. The chosen-investment results below use this paced implementation
when calling an outcome peaceful agreement, and merely native production
when no cooperative implementation is selected. A different repair model
must recompute the checkpoint threat bound rather than reuse delta blindly.

## 2. A strong original chooses cross-use technology

Initially each has native capacity R>0. Red's cross-use coefficient is
beta=1. Blue can choose alpha in [0,1], consuming k alpha of its own
native capacity, where 0<k<R. This is a public investment in converters
that use the rival's material/equipment; r_B=R-k alpha, r_R=R. It need
not increase Blue's native production. All installation work is paid before
the later bargaining or fight. This is one specific dual-use intervention,
not an assertion that every shared research discovery has this effect.

Assume p delta>1/2. After the investment, Blue can offer an enforceable
peaceful allocation, attack, or retain native production. A completed
agreement uses H>=0 units of Blue's remaining native work for actual
communication, verification and execution; rejection does not incur that
execution expense. Any separately unavoidable proposal expense must also
be subtracted. Red accepts an offer at its actual rejection continuation;
ties accept. If Blue would attack after rejection, Red's reservation is
d_R. If Blue instead prefers native production, Red retains R and there
is no tribute bargain. Combat remains physically possible at that point.

In the threat region, the best offer to Red gives it d_R and leaves Blue

`P(alpha)=R+alpha[R-2(1-p)delta R-k]`
`          +(1-p)delta k alpha^2-H`.                    (4)

The first constraint of (1) binds since R>d_R. The other is satisfied.
When the expression is infeasible because H exhausts available work,
the peaceful route is absent, rather than evaluated at a negative budget.
The attack and native values are

`W(alpha)=p delta[R+(R-k)alpha]`,
`N(alpha)=R-k alpha`.                                   (5)

P is convex in alpha, W increasing and N decreasing. Therefore the maximum
over feasible choices is achieved by alpha=0 with native value R, or by
alpha=1 with the larger feasible peaceful/attack value. A spurious P in
the non-threat region cannot overturn this conclusion: when W<=N,
`R+alpha R-d_R alpha-r_B` is not a payment Red is forced to accept, and
the attainable no-threat allocation gives Blue at most N. At a threat
boundary P is no larger than the full-frontier upper envelope already
bounded by the endpoint values. Feasible endpoint P and W provide the
stated maximum. Weak equalities can yield additional tied choices.

At alpha=1 the two relevant values simplify to

`W_1=p delta(2R-k)`,
`P_1=[1-(1-p)delta](2R-k)-H`.                           (6)

Hence the following open conditions select full cross-use investment and
combat:

`k < 2R-R/(p delta)`,
`H > (1-delta)(2R-k)`.                                 (7)

The first makes W_1>R. The second makes W_1>P_1; no funded acceptable
peaceful offer in (1) improves Blue's attack value at the chosen technology.
Conversely H<(1-delta)(2R-k) and P_1>R select full investment followed by
ordinary peaceful agreement. A sufficiently costly converter selects no
investment if both endpoint gains are nonpositive. This classification
includes the other player's actual acceptance response and the outside
option of keeping native production.

For R=5, p=4/5, delta=9/10 and k=1, W_1=162/25=6.48.
At H=1, P_1=319/50=6.38, so the chosen outcome is combat. At H=1/2,
P_1=172/25=6.88, so the same conversion investment leads to ordinary
agreement. These originals value only their own clips. The difference is
recoverable prize value versus the real expense of executing a bargain.

## 3. A weak original can choose costly protective incompatibility

To examine the other causal direction, hold native Blue capacity at R,
initial alpha=beta=1, and let Red choose s in [0,1] before bargaining.
Its protective interface makes alpha=1-s and consumes c s of Red's native
capacity, where c>0 and the funded domain is `0<=s<=min{1,R/c}`.
Native Red production remains efficient apart from
that paid work. Protection is publicly observable, cannot be bypassed by a
converter outside the specified technology, and occurs before an attack.
These authority and timing conditions are substantive.

With r_R=R-cs, Blue's attack is deterred relative to native production
exactly when

`(1-s)(R-cs) <= R[1/(p delta)-1]`.                       (8)

On the funded domain the left side decreases strictly until its zero
endpoint, so the least deterring s_d is unique and leaves positive native
capacity remaining.
Writing z=c/R and h=1/(p delta)-1 in (0,1),

`s_d=[1+z-sqrt((1-z)^2+4zh)]/(2z)`.                     (9)

The costless limit is s_d=1-h. Take peaceful native production at the
attack-indifference boundary; an arbitrarily stronger defense makes that
comparison strict at an arbitrarily close extra cost.

With negligible successful-agreement expense and Blue having the offer
right, Red receives `(1-p)delta(2R-cs)` while the attack threat survives.
That value decreases with s. Once the threat is deterred, Red can reject
tribute and retain R-cs, also decreasing with s. Thus Red chooses either
s=0 or s=s_d, and strictly selects the safeguard exactly when

`c s_d < R[1-2(1-p)delta]`.                             (10)

The improvement is original own-color output, not a concern for the rival.
A parameter change that improves a bargaining slack but remains below the
deterrence threshold is not privately attractive in this offer-right model.
In contrast crossing the threshold can make the same kind of intervention
worth its full physical cost. Different bargaining rights change this
investment incentive and must not be inferred from the frontier alone.

The exact threshold can be stated in the primitive cost c. Put
`h=1/(p delta)-1`, `d_0=2(1-p)delta R`. The funded cost c s_d increases
strictly from zero to R(1-h) as c increases from zero to infinity. This
follows by writing w=c s_d and differentiating
`(1-w/c)(R-w)=Rh`: its derivative with respect to c is positive and its
derivative with respect to w is negative. If d_0<=Rh, defense is chosen
for every finite c. If d_0>Rh, it is chosen strictly exactly when

`c < c_crit=d_0(R-d_0)/(d_0-Rh)`.                       (11)

Substitute w=R-d_0 into the same equation to obtain (11). Above that
threshold Red strictly chooses no safeguard, despite the existence of a
funded deterring action. For p=4/5 and delta=99/100, h=26/99 and
d_0/R=99/250. A cost coefficient c=R induces defense; c=3R does not.
The expensive action remains feasible by selecting s<R/c. This supplies
both chosen protection and chosen refusal inside the funded action class.

## 4. Strategic repair and earlier bargaining

If section 2's conversion investment is followed by an available defensive
move before the bargaining/attack stage, it is incorrect to retain (7)
without recomputing the response. For any positive alpha, suppose Red can
fully protect at expense at most c_max, with

`c_max < R-2(1-p)delta R`.                              (12)

Then obtaining native Red output at least R-c_max strictly beats the
unprotected threat payoff. With defense chosen before offers, Red chooses
some deterring defense whenever otherwise threatened: every non-deterring
defense only reduces its threat-based reservation, whereas a full defense
strictly improves it. Blue then keeps R-k alpha. Anticipating this response,
it chooses alpha=0 rather than paying for a threat that will be neutralized.
This conclusion assumes the defensive action is available after the
conversion investment and before any attack; surprise or faster weapons
change the game. The full-protection comparison can be sharpened using the
least deterring action and asymmetric native capacities.

Allowing an agreement *before* Red pays for defense repairs the waste but
can preserve the incentive to create a threat. If the credible defensive
fallback leaves Blue r_B=R-k alpha and Red R-c_d, a fully transferable
pre-defense stock totals r_B+R. An executable early bargain costing H_e
can leave Red its fallback and Blue

`r_B+c_d-H_e`.                                         (13)

Thus avoiding defense creates a real surplus c_d-H_e when positive. Blue
can recover its conversion expense and profit relative to its initial R
when `c_d>k alpha+H_e`, provided the allocation and the early binding
agreement are actually available. With incomplete cross-use, replace (13)
by frontier (1). This is a conditional earlier-offer construction, not a
claim that all defensive responses eliminate investment. The chosen
continuation can still be peaceful: the credible safeguard changes the
terms, and negotiation saves its unused physical expense.

## 5. Utility change, controls and scope of the combat claim

Sections 2–4 establish ordinary bargaining and combat choices. A genuinely
changed goal that implements an accepted allocation is another execution
route; its real expense replaces H only if the entire staged installation
and continued incentives have been established. Notes 119 and 128 give
candidate common goals and a protected launch in their stated physical
classes. If such a route is cheaper than the frontier slack in (7), it can
repair the costly-agreement combat region. A matched ordinary delegate can
do so as well. A costly route yielding only the same already implementable
allocation is displaced. Actual adoption is not inferred from peace.

Consequently (7) is a combat result for the complete agreement menu stated
there, or for a larger menu after verifying that each added route still
fails its participation/expense boundary. The repair checks identify what
must survive before broadening it: feasible protection, earlier settlement,
productive surplus, a different partner, and cheaper genuine or ordinary
execution. They also give positive causal conditions for deliberately
creating peaceful incentives. Technology authority, expense and order of
action matter as much as the amount of overlap in the production diagram.
