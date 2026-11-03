# Causal response frames and finite recovery costs

**R0004 physical construction; contributing-agent self-check.** This note supplies a concrete
resource/clock realization for the staged game. It does not identify output,
work, conserved energy and utility. The declared finite kernel is audited in 077; the larger agreement-space
implementation remains conditional.

## 1. Resource coordinates and deadline

For each party keep separate registers for usable project components U_i,
transformed/spent components Z_i, dispersed components D_i, available work
W_i, fuel energy E_i, dissipated heat H_i and repair-infrastructure status.
Take one kilogram of a party's specialized component to supply one unit of
that party's terminal project output; this is a chosen production coefficient,
not an identity between matter and utility. Initial usable stocks can be 20.

An implementation operation that costs c output units converts c kilograms
of usable components into spent controller/communication assembly. It moves
mass U_i to Z_i, preserving U_i+Z_i+D_i. Its work requirement is recorded
separately. With efficiency eta in (0,1), delivering work w consumes fuel
energy w/eta; work and inefficiency ultimately become heat or recorded
physical configuration changes. A consistent energy ledger tracks these
flows, rather than treating the destroyed *usefulness* of a component as
destroyed energy.

The project delivers at a fixed deadline H. Existing usable components are
already finished; spare work alone cannot create more of them before H.
Unused work can still support recovery after damage. Earlier policy selection
does not advance the delivery date. This explains why elapsed response time
need not itself be an additional utility charge beyond actual work, material
and lost recovery opportunity. A project with earlier productive alternatives
or time-discounted delivery needs those additional charges.

## 2. Requested frames and actual observation

A claim consumes f of sender components and prepares the diagnostic port:
it supplies the session data and physical alignment needed to authenticate
subsequent progress. Utility self-knowledge does not prepare that port.
A request without a prepared port returns no protected information. A
different direct sensor or a binding request/subsidy mechanism is an added
technology to compare, not a free consequence of knowing S exists.

Each requested stage lasts two elementary ticks. At its start R converts
r_i components into the stage's receiver assembly, irrecoverable before H.
Work may be supplied across the two ticks. S can refuse immediately or
start the next recognized stage. Starting consumes c_i/2 and half its work;
completion consumes the other half. A started prefix can be aborted; its
spent material is not refunded. An unstarted stage cannot complete in the
second tick alone at the hardware's specified maximum work rate.

Progress/refusal/report observations are released at the frame boundary.
One physical realization is a scheduled relay with no causal line of sight
from S's local workspace to R between those boundaries; a side channel
that can arrive earlier changes the game. R can still issue stop or attack
commands during a frame. It has the same posterior until the response
arrives; public progress at the *previous* boundary remains fully remembered.
The last frame releases activation evidence together with the fresh active
controller's report. Activation evidence arriving earlier than the report
is not this observation map.

Low refusal can be prepared and cached immediately, freeing its local work.
It is not required to keep paying an avoidable standby cost merely to mimic
high S. Publicly observable prefix advancement, by contrast, costs c_i and
can be mimicked by low S at that real price. These two physical facts yield
the staged mixing calculation in 073.

During a requested peaceful frame, R has already spent r_i. The expected
information benefit that justified the request is still available, while
that material expense is sunk. With no new observation, stopping or
launching a now-no-cheaper contest does not improve its current payoff.
Once low S has started an intermediate prefix, its remaining half-cost is
less than the continuation value c_i, so it completes; at the last stage
a low original controller instead aborts an accidental start. High S
completes when its derived remaining expense is below h. These are actual
interruption checks, not an assertion of atomic safe installation.

The finite clock defines priority: the first effective launch starts one
contest; simultaneous launches coalesce into that contest rather than
drawing independent victories. Pending installation work stops, and only
material/work actually spent is charged. A stopped but not activated
candidate never acquires authority. The contest apparatus is consumed in
the clash. The winner controls this project's actuator, not every future
choice of the loser throughout the universe.

## 3. Recoverable dispersion and infrastructure loss

A contest disperses d_i^disp components and disables recovery infrastructure.
It also consumes w_i^war of available work and takes tau_war time. Repair
requires work w_i^rep, time tau_i^rep and chi_i usable components. Recovery
then needs omega_i work per kilogram and has rate rho_i. At a contest
started at time t with available work W_i, let

\[
u_i=\min\left\{d_i^{disp},\
\frac{(W_i-w_i^{war}-w_i^{rep})_+}{\omega_i},\
\rho_i(H-t-\tau_{war}-\tau_i^{rep}-\tau_{ship})_+\right\}.
\tag{1}
\]

Repair is available only if its actual work/time/material prerequisites
are met. If there are enough intact components for chi_i, the optimal
net recovery is max(0,u_i-chi_i), giving effective project loss

\[
d_i(t,W_i)=d_i^{disp}-\max\{0,u_i-\chi_i\}.
\tag{2}
\]

If a prerequisite fails, effective loss is d_i^disp. Agents may decline
repair. Every goal considered in the core increases with its own X_i, so
repair maximizing net useful output is optimal after the actuator outcome;
the original and changed criteria agree on this physical choice. Material
is dispersed/transformed, not annihilated. Finite repair effort and time
can prevent its usefulness from being restored before H.

If no new work is acquired, later stages reduce W_i and remaining time.
Therefore d_i(t,W_i) is nondecreasing along a progression. This changes a
contest comparison without identifying energy, work or useful output.
Longer recovery time, more dispersion or less available recovery work can
make checking preferable; cheaper timely recovery can make destructive
state revelation preferable. The actual policy/incentive conditions must
still be checked, particularly if the sender's own attack loss falls below
the earlier restraint bound.

## 4. An exact dimensional witness

Set H=10 ticks. The claim finishes at t=1 and three two-tick frames finish
at t=3,5,7. Shipping takes one tick. Each requested receiver stage and each executed sender stage
uses one work unit. At the first checkpoint each party has W_i=11. A
contest uses one work unit and one tick; infrastructure repair uses one
work unit, two ticks and chi_i=.001 kilograms. Recovery requires 900 work
units per kilogram and has rate .01 kilograms per tick. Let

\[
d_S^{disp}=5.009,\qquad d_R^{disp}=.019.
\]

At t=1, u_i=.01, so effective losses are d_S=5 and d_R=.01 exactly. At
later public checkpoints work and time are smaller, hence these losses
weakly increase; at t=7 no recovery finishes and the dispersed amounts
are the effective losses. All quantities are finite. This is an asymmetric
exposure example, not a claim about typical installations or military power.
For s=1/20 use positive strengths in ratio 1:19; the outcome is random,
and neither party knows its realization before combat.

With f=.01, c_i=.15 and r_i=.01/3, the usable stocks remain positive on
every branch. Positive partial work and material costs are charged even
when a frame is interrupted. Other parameters can be realized by changing
actual component requirements and recovery capacities, subject to the
same resource/clock checks.

## 5. Early combat versus later combat

When effective contest costs rise along completed frames, the earliest
receiver threshold w_1=d_R(t_1,W_1)/(1-s) is the strongest restraint test:
the peaceful suffix excess T_i decreases with i, while w_i increases.
Thus V_eff<w_1 suffices for all peaceful checkpoint comparisons. Later
attacks remain physically available; they are more expensive relative to
the remaining information benefit.

An off-path request in a combat regime needs special care. A later
threshold can exceed the current posterior; Bayes' formula for a mixing
low type would then ask for an impossible advancement probability above
one. The repair is a pooling advancement continuation followed by policy 1
at the next checkpoint when its prior lies below that checkpoint's threshold.
The request remains costly and inferior at the earlier combat decision.
This continuation and all mid-frame information sets must be included in
the full assessment; a constant-damage recursion alone does not check them.

## 6. Enlargements still requiring actual implementation

**Terminal closure matters.** A received policy offer opens a final command
window of one quarter tick in which the incumbent can launch the existing
apparatus. If it does not, the actuator locks and the surviving useful
stocks leave in a one-tick dispatch. Launch travel takes one tick, and
simultaneous arrival has priority over dispatch. Even a half-installed
core candidate needs at least one full remaining installation tick before
it can issue a launch. Its earliest new-goal arrival is therefore at least
two ticks after the offer, strictly later than the 1.25-tick closure. A
fresh core module needs two installation ticks. This explicitly covers a
partial candidate at a midpoint interruption; a faster prepared authority
requires a different continuation rather than being silently discarded.

The incumbent's immediate launch is its cheapest launch in that window:
waiting supplies no new information or better policy opportunity and only
reduces recovery capacity. The finite tree represents that optimal launch
time; intermediate delays are weakly dominated under the core evaluators.
A quarter-tick incumbent response and the one-tick remaining-activation
floor are local hardware assumptions. Useful output is delivered at H.
After a contest the
apparatus is spent; rebuilding it takes more work/time than remain, while
recovery and shipment use their stated finite resources. This explains the
terminal control boundary instead of silently discarding later attacks on
still-exposed useful stocks. Common dispatch components/work are reserved
in both branches and normalized out of the reported *incremental* losses;
they must still be included in the full material/energy inventory.

This particular ten-tick witness supports three frames, not arbitrarily
many. Longer staged interfaces need a correspondingly checked horizon.

Physical escape, transfers, an early private controller, reused partial
assembly, a faster side channel, arbitrary-program attestation and a new
counterparty are distinct potential enlargements. Price and timing bounds
must be justified for each consequential alternative. Work on successful
accommodation and on its limiting/repair conditions should use the same
resources and information. The present kernel supplies neither a claim of
unrestricted renegotiation-proofness nor a ban on those alternatives.
