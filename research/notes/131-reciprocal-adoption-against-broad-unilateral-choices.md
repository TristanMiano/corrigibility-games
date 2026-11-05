# Reciprocal adoption against broad unilateral production choices

R0006 mathematical strengthening of the two-factory result. This removes
the linear-weight restriction from the *unilateral deviation bound* in one
specified production episode. It then gives a reciprocal adoption equilibrium
with actual conditional installation. The communication and verification
premises are substantive; later public rounds or new physical opportunities
are not covered by the one-round theorem.

## 1. The best unilateral commitment against an original producer

Use note 116's physical counts

`q_i=Q+a x_i+rho a x_j+b x_i x_j-c x_i^2/2-K_i`,

with `s=b/c in (-1/2,1/2)`, `t=a/c`, `A=a^2/c`,
`ell=rho(1-s)+s`, and the stated finite caps and funding. Costs K_i are
paid work, not utility penalties. Original j's effort response to a known
x_i is `x_j=t+s x_i`.

Suppose i can choose any publicly known goal or production commitment,
including one that directly specifies an effort, while j's effective
production criterion remains q_j. The actual effort stage is simultaneous,
or j observes i's effort before choosing its own. Each admissible
continuation must preserve j's own best-response condition. Arbitrary new
sequential move rights that let i reward j *after* its action are another
game and are not smuggled into this bound.

Substitute j's response into original i's physical output, before its own
extra commitment expense:

`f(x)=Q+rho A+a[1+s(1+rho)]x-c(1-2s^2)x^2/2`.           (1)

This is strictly concave. Its maximum occurs at

`x_L=t[1+s(1+rho)]/(1-2s^2)`,                           (2)

which lies in the allowed effort interval. For s<0 this follows from
`1+s(1+rho)>0` and
`rho-s(1+rho)(1+2s)>=0`; for s>=0 the common efficient-effort cap is
at least x_L. Subtracting the original equilibrium value at x_F=t/(1-s)
gives the exact unilateral gain

`G_L=A s^2 ell^2/[2(1-2s^2)(1-s)^2]`.                   (3)

This upper bound covers nonlinear goals and direct effort commitments,
not just H_i=q_i+beta_i q_j. A direct effort controller attains it in this
ideal comparison. Every real cost weakens that deviation. If a proposed
goal has no actual continuation, an announced payoff is not a deviation.

The bound also covers appropriately timed random recommendations. Conditional
on original j's information, let m be its expectation of x_i. Strict
own-effort concavity gives x_j=t+s m. Then conditional expected q_i is
at most f(m), because E[x_i^2]>=m^2. Hence every such lottery has expected
original payoff at most max f. This argument requires that j's unilateral
action change does not itself change the conditional law of i's later
action. It is the stated simultaneous-action obedience condition, not an
assumption of independent information or perfect knowledge of realizations.

Combat remains an alternative deviation. Include the finite physical bound
of note 115 so every war lottery gives the deviating original fewer clips
than the relevant peaceful continuation. A successor with an arbitrary
hostile goal may still initiate a fight, but the initial own-color maximizer
then evaluates that actual poor outcome. With weaker physical protection,
add the true combat value to the maximum in (3).

## 2. A common objective has a strict surplus over that bound

Both agents' common total-count optimum gives gross per-original gain

`Delta=A ell^2/[2(1-2s)(1-s)^2]`.                        (4)

For ell!=0, direct cancellation yields

`Delta-G_L=A ell^2(1+2s)/[2(1-2s)(1-2s^2)] >0`.         (5)

Equivalently `G_L/Delta=s^2(1-2s)/(1-2s^2)<1`, because the difference
between denominator and numerator is `(1-s)^2(1+2s)>0`.
Thus a reciprocal common-goal route can leave each original strictly more
than its best unilateral commitment even when s<=0, where independent
positive other-regarding weights were unattractive. The agreement changes
both effective production criteria, and that joint response is its benefit.

The fixed-cost sufficient condition is

`K_i < Delta-G_L` for both i.                           (6)

It is deliberately conservative: unilateral alternatives are given zero
expense and the entire best-response frontier, while actual installation
expense is charged to the common route. At ell=0 there is no productive
gap to fund a positive-cost update. Inequalities with another outside
partner or a superior existing agreement must replace (6) when available.

## 3. Conditional installation without a simultaneous physical rewrite

Consider one explicit public-audit interface. Each original privately
prepares and pays for an effective production controller. Preparations and
installations occur physically in stages, with attacks and aborts available;
the finite physical comparison covers those checkpoints. Neither sees the
other's completed choice before the announced audit. A funded trusted audit
then publishes the actual effective controllers and relevant actuator
constraints. It issues a persistent Ready event exactly when both selected
the agreed conditional templates and possess the specified production
control. It verifies the absence of hidden mandatory rewrites or conflicting
actuator commitments that would invalidate the proposed continuation.

This is stronger than reading a utility variable or matching a code hash.
Its expense and reliability are explicit model premises. Template functions
refer to the public event, and the auditor recognizes their specified
implementation; no circular inference from a program's claimed honesty is
used. A secretly precommitted future controller that will overrule the
current evaluator fails this effective-control audit.

The installed template for i is the fixed terminal-history utility

`C_i(Hist)=q_B+q_R`, if the valid Ready event occurred;
`C_i(Hist)=q_i`,     otherwise.                         (7)

A smooth share-sensitive H from note 119 can replace the productive branch
if final allocation control is included and its common maximum is verified.
Ready is a past event: later program edits do not remove it from the acting
current criterion's evaluation. The templates are genuine changes of
preferences over histories and, in the productive branch, over feasible
output choices. A positive affine recoding of the original would not produce
these rankings.

After the audit there is a finite production window with no further public
commitment/negotiation round before simultaneous efforts. Agents can still
edit privately, choose any feasible effort and attack. An original-goal
branch gains nothing by a private change that induces a worse own-effort
choice without altering the other factory's information or available
responses. A common-goal branch reaches a global maximum and likewise gains
nothing from a later rewrite whose outcome stays in this opportunity set.
This is an incentive argument, not a prohibition on self-modification.

**Reciprocal adoption theorem.** Under these interface, continuation and
physical premises, and (6), both choosing the conditional templates is a
strict equilibrium against unilateral deviations that fail Ready. The
continuation after Ready is the unique common-goal effort optimum. No
unilateral deviation in the broad production-controller class beats it.

**Proof.** Given the other's template, choosing one's own makes Ready and
gives original i `q_F+Delta-K_i`. A different effective controller prevents
Ready, so the other's criterion is its original q_j. Equation (3) bounds
the deviator's expected output by q_F+G_L even if its own device is free.
Condition (6) makes the common route strictly better. After Ready, strict
joint concavity and the global maximum give the stated continuation and
the absence of a profitable private rollback. Attack is inferior by the
explicit physical comparison. QED.

An alternative audited device giving the same actual common continuation
can tie: strictness is against outcomes that fail the reciprocal condition,
not against harmless representations. If a matched ordinary conditional
delegate is recognized as an equally capable route at the same cost, it
can be a co-optimal choice. A cheaper actual joint controller can displace
genuine installation. The result does not require unique superiority over
such devices and must include them when choosing the actual mechanism.

## 4. What the larger agreement-space test establishes

This strengthens a binary accept/refuse example: changing one's nonlinear
goal, choosing a direct own-effort commitment, or using an appropriate
correlated recommendation is explicitly covered. It leaves important
restrictions visible. The final effective-control audit, protected private
preparation and one public commitment window are chosen implementation
features. A new public renegotiation round can alter the other's criterion
as well, invalidating the single-original response used in (1). Arbitrary
new partners or productive assets also change the benchmark.

Note 128 supplies a different repair for richer counteroffers: a protected
physical entry gate and a deliberately chosen current-goal reservation.
Its output guarantee can survive varied offers but does not by itself force
both parties to select genuine change over ordinary controls. The present
theorem instead gives strict reciprocal adoption against broad unilateral
production choices in one audited episode. Neither should be promoted to
the other's larger implementation scope without a proof.

The physical sufficient margin (5) is an open parameter region in a simple
production family. The exact audit and conditional preference are engineered
conditions requiring reliable technology. This separation preserves a
constructive answer—exclusive original ends can rationally fund genuine
reciprocal change—while showing which practical and future-game questions
remain before calling that outcome natural or prevalent.
