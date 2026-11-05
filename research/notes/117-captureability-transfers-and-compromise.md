# Reusable assets, capture, transfers and compromise

R0006 exact two-color resource model. This supplies a different consequence
of common manufacturing steps: an asset can become more useful to a hostile
winner as well as to a peaceful trading partner. Originals still value only
their own final colors. There is no intrinsic reward for violence.

## 1. A complete peaceful transfer frontier

Blue and Red have prepared capacity bundles with native final yields
`r_B,r_R>0`. A unit used by its native line makes one clip of that color.
If transferred and converted to the other's process before the finite
deadline, it makes `lambda` clips of the other's color, `0<=lambda<=1`.
The lost yield represents incompatible equipment, conversion work and
delay, or unused raw material. It is not disappearing mass or energy.
Lambda is a cross-use coefficient, not a measure of intrinsic value overlap.

Allow every divisible allocation of both bundles between the two production
processes, not just the original allocation. The downward-closed feasible
output set F is exactly

`q_B+lambda q_R <= r_B+lambda r_R`,
`lambda q_B+q_R <= lambda r_B+r_R`,
`q_B,q_R >= 0`.                                          (1)

For lambda<1, the efficient boundary joins
`(0,r_R+lambda r_B)`, `(r_B,r_R)`, and
`(r_B+lambda r_R,0)`. Transferring Blue's bundle to Red traces the first
edge; transferring Red's bundle to Blue traces the second. Any dominated
output can leave material unprocessed. This proves both necessity and
sufficiency. At lambda=1 the frontier is the total-output simplex. At zero
cross-use it is the rectangle bounded by the two native yields.

The original autarkic outcome is `(r_B,r_R)`. This particular class contains
no setup-saving or knowledge-creation benefit beyond the prepared bundles;
no other point in F strictly improves both originals over autarky. Notes
112–116 supply the productive counterpart. Here the benefit of compromise
can instead be avoiding a contest that one party otherwise chooses.

## 2. The attack incentive and an exact bargaining margin

Combat is available. Blue wins with probability p in (0,1), determined by
the specified strengths. After finite material dispersion, converter damage,
ammunition expenditure, recovery work and delay, the winner can realize a
fraction `0<delta<1` of the corresponding fully captured own-color yield.
The loser loses the field actuator but still values its own color. With
both originals unmodified, expected combat counts are

`d_B=p delta(r_B+lambda r_R)`,
`d_R=(1-p)delta(r_R+lambda r_B)`.                         (2)

Delta is an effective recoverable production factor for this scalable
specialization. An explicit work/material/time bottleneck can determine it
as in note 115; it is not simultaneously an additional utility subtraction.
The limiting delta=1 calculations below isolate specialization losses, not
the baseline with positive damage. Which colors a *modified* winner makes
must be evaluated separately under its current goal.

Blue strictly prefers attacking an uncompensated autarkic arrangement iff

`p delta(r_B+lambda r_R)>r_B`,                            (3)

and analogously for Red. A rise in lambda raises both attack values. Since
`p delta<=1` and `(1-p)delta<=1`, no agent gains from attacking at lambda=0.
For equal bundles r, Blue's threshold is
`lambda>1/(p delta)-1`, when that threshold lies in [0,1].

Now compare with the **full** peaceful transfer set (1). Define its two
slacks above the combat vector:

`M_B=(1-delta)(r_B+lambda r_R)`
`     +delta(1-p)(1-lambda^2)r_B`,
`M_R=(1-delta)(r_R+lambda r_B)`
`     +delta p(1-lambda^2)r_R`.                            (4)

Substitution of (2) into (1) proves these expressions. The largest common
increment g such that `(d_B+g,d_R+g)` is feasible is exactly

`g_max=min(M_B,M_R)/(1+lambda)`.                          (5)

With positive bundles and delta<1 this is strictly positive. Thus a strong
agent's preference for attacking the original allocation coexists with a
strictly mutually better ordinary peaceful transfer. The transfer must be
implemented; existence alone is not an equilibrium selection claim.

For equal native bundles r, (5) reduces to

`g_max=r[(1-delta)+delta(1-lambda)min(p,1-p)]`.             (6)

At fixed damage and strength, making the assets more interchangeable
*reduces* this bargaining margin. It improves the winner's ability to use
the defeated factory, removing a specialization loss from combat. It also
improves peaceful transfer efficiency; (6) accounts for that improvement
instead of holding the peaceful alternative artificially fixed.

At delta=1 and lambda<1, the general expression becomes

`g_max=(1-lambda)min{(1-p)r_B,p r_R}`.

Both colors can be produced efficiently in peace, while a single-color
winner wastes some incompatible equipment. At lambda=1 that particular
source of surplus vanishes. For delta<1, avoided physical damage still
provides the positive first term in (6).

## 3. Actual implementation expense can select peace or war

Suppose a compensated agreement requires actual capacity expenses k_B,k_R,
paid from the two bundles, with `0<=k_i<r_i`. The net peaceful set is (1)
with r_i replaced by r_i-k_i. Comparing it to the initial combat vector
gives necessary and sufficient conditions for weak mutual participation:

`k_B+lambda k_R <= M_B`,
`lambda k_B+k_R <= M_R`.                                 (7)

Strict inequalities allow both to improve strictly. For equal expense k,
the exact boundary is `k<=g_max`. A verified ordinary transfer, a matched
delegate, or genuine common-goal installation may have different actual
expenses; evaluate each available route using its own feasible set. A
costless announcement is not a paid, executable transfer.

In a specified bargaining protocol where one party can accept a funded
allocation or initiate combat, (7), the offer rights, and the tie rule
determine whether that route is accepted. If (7) fails for every available
compensating route and some agent satisfies (3), uncompensated autarky is
also rejected by that agent. With no further productive, enforcement or
partner-choice option in the specified game, combat follows. This is an
explicit agreement-class condition, not a claim that trying one expensive
proposal establishes general failure. Cheaper transfers, alternative
finishing arrangements, pooling research and outside partners must be
included whenever feasible.

For example, take `r_B=r_R=5`, `p=4/5`, `delta=9/10`, `lambda=1`.
The original allocation yields (5,5); war yields expected (7.2,1.8).
The maximum common improvement over war is .5. A compensated route costing
.25 per bundle can give each strictly more than its war value. A route
costing .75 per bundle cannot satisfy both original reservations; if all
actual compensating routes have at least that expense, the strong Blue
prefers war to autarky and no accepted peaceful transfer in this class
exists. Positive combat losses and positive agreement costs both enter
the comparison. A cheaper feasible route repairs the latter case.

## 4. Where genuine goal change fits

Choose a mutually acceptable efficient point q* in the funded peaceful
frontier and the negotiated common criterion

`G(q)=min(q_B/q_B*,q_R/q_R*)`.                            (8)

It is a genuine ordering change for both originals. Since q* is Pareto
efficient, G has maximum 1 over that physical frontier. If battle leaves
a strictly contracted feasible resource set, neither common-goal successor
can improve G by initiating it, by retaining a different split, or by a
later preference revision whose physical result lies in the same set.
The loser may still receive valued-color clips from a modified winner;
do not substitute the original winner's all-own-color production into this
post-installation comparison. Use the physical frontier bound instead.

This gives the continuation certificate for a consensual modification
route. Initial staging still needs its actual protocol. A history-dependent
first goal can retain the original own-color ordering until the other
party has verifiably installed the agreed common criterion, as in note
114. Before activation, evaluate each original's current threat with the
actual work already spent. Proposal terms must be bound or observably
reopened *before* relevant participation opportunities are lost; note 020
shows why an unsecured offer is insufficient. Conditions (7) are a funded
opportunity result until those checkpoints and route costs are supplied.

When a matched ordinary controller can implement q* at the same cost,
genuine modification and unchanged-goal commitment can tie. A cheaper
available ordinary controller can displace the goal route; a cheaper
available verified goal route can extend the acceptable set. The cost
ordering is an implementation question, not a theorem about the labels.

## 5. Naturality and deliberate changes

Interchangeable equipment, concentrated stocks and finite recovery are
simple independent mechanisms. Equal bundle sizes simplify (6), while
(4)–(5) cover an open asymmetric class. None establishes how frequent such
environments are. The direction in (6) concerns captureability alone;
standardization may also reduce setup work or improve knowledge transfer,
which must be included as joint changes in the productive frontier.

An agent could invest in portable tooling to increase lambda, in modular
or dispersed equipment to reduce recoverable capture, or in lower-cost
transfer/inspection machinery to reduce k. These are candidate interventions,
not free parameter settings. Their cost, funding, authority, observation,
timing, current-goal benefit and the opponent's reaction remain to be
derived in a chosen-action extension. The exact margins here provide the
test: compare every resulting peaceful option and threat, and distinguish
an available repair from one both originals choose. Note 129 supplies a
chosen-action extension with paid conversion, protection and earlier bargaining.
