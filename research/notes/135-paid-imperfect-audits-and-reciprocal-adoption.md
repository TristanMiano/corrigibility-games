# Paid imperfect audits and reciprocal adoption

R0006 implementation extension of the additive research class. This replaces
perfect recognition with a declared finite deceptive alternative and a
funded audit technology. It derives the incentives from the actual clip
outputs, then gives an audit choice and selected adoption equilibrium.
It does not claim that behavioral tests can recognize arbitrary utility
functions. Inspection-game machinery is conventional; compare note 013.

## 1. Genuine templates, retention and a false claim

Use note 114's production technology, with `v=A rho^2`, A=a^2/c.
Original production gives q_F. Each participant has three effective
controller choices before the public audit:

* C: pay actual update work K>0 and install a genuine conditional template
  that uses the common total goal if the audit issues Ready, and otherwise
  retains the own-color ordering.
* F: openly retain the original goal. This prevents Ready.
* D: claim the common template while retaining the own-color criterion.

Incremental deception cost is set to zero as a strong comparison; common
message and audit expenses are charged separately. Adding an actual
deception expense reduces that deviation's advantage. The shared process,
private finishing, retained attacks and one public production-controller
window are as in the specified physical class. Later unmodeled public
renegotiation must not be inserted into the effort equilibrium silently.

An actual audit always recognizes a genuine C, but lets a D pass with
probability epsilon. If one genuine C faces a false pass, the realized
production goals are (common, original), so their efforts are
`(t(1+rho),t)`. Substitution into actual outputs gives gains, before the
common audit/message bill,

| Own choice / other choice | C | D | F |
| --- | --- | --- | --- |
| C | v/2-K | -epsilon v/2-K | -K |
| D | epsilon v | 0 | 0 |
| F | 0 | 0 | 0 |

Rows report the original chooser's expected own-color gain. For C versus
D, detection returns both effective production goals to originals; a false
pass causes the loss v/2. For D versus C, false passage gains v. When both
retain, even a nominal Ready signal changes neither actual production goal.
No deceptive program is counted as genuine adoption.

Consequently mutual genuine C is a strict equilibrium against F and D
exactly when

`K < v(1/2-epsilon)`.                                  (1)

This requires epsilon<1/2 and v>2K. If the reverse inequality is strict,
D strictly dominates C against C and also against D or F. Therefore no
equilibrium then places positive probability on C. At equality there can
be weak adoption; this note uses strict margins for its construction.

The mechanism is a comparison of two gains: reciprocal concern produces
v/2 before update expense, while a fake claim earns epsilon v by taking
advantage of the other's changed criterion. Greater useful sharing v can
pay the fixed update expense, but it also raises the prize from deception.
The audit condition includes both effects.

## 2. Paying for an actual audit level

Suppose n independent funded inspections each miss the specified deceptive
controller with probability m in (0,1). Then epsilon_n=m^n. Each inspection
uses real work c>0 per participant; common communication/setup uses h>=0.
All funds are available before the audit and come from native useful-work
stocks. The inspections and their level are publicly observable. The paid
route includes actual execution of the promised inspections: a funded
audit controller or another verified continuation incentive must supply
this commitment. Merely announcing n and later choosing whether to save
its cost is the different inspection game examined in note 013.

This miss-rate model is a technology premise. It can describe inspections
of a known finite controller family whose deception affects a detectable
part of the implementation. It does not follow from a public claim, utility
self-knowledge or observing a few cooperative actions. A richer adversary
that can mimic all tested behavior requires a new miss-rate bound; an
arbitrary semantic verifier is not inferred.

For v>2K, the least integer level supporting strict mutual C is

`n_* = floor(log(1/2-K/v)/log m)+1`.                     (2)

At that level, the actual per-founder gain relative to opting out is

`V_C=v/2-K-h-c n_*`.                                   (3)

Larger audit levels cost more while, on the mutual genuine path, giving
the same production. Smaller levels fail the strict controller incentive.
Thus n_* is the least-cost audit for this strict-adoption implementation.
It is actually beneficial to fund when V_C>0.

One finite launch protocol is: offer the public audit level; both originals
authorize its bill conditionally on mutual participation; then privately
install their controllers; audit, reveal Ready and produce. Select mutual
C in the ensuing controller game when (1) is strict, and no C when it is
strictly dominated. Both initially authorize when (3) is positive. Refusing
the offered joint audit returns the original production continuation. The
offer and chosen continuation supply a subgame-perfect adoption path in
this specified protocol; the all-retain controller equilibrium can still
coexist after a high audit. Selection is not claimed to be unique.

Publicly reducing an agreed audit before controller choice changes the
subgame that the other original sees; it does not leave the other blindly
playing C against an unsafe audit. Secretly reducing paid inspection or
tampering with the public signal is an additional deception action whose
cost and detection would need inclusion. Agents can still attack; use the
finite physical dominance bound at these pre-production checkpoints.

## 3. An exact overlap-to-adoption threshold with nonzero expenses

Take A=1, K=1/8, m=1/2, h=c=1/16, so v=rho^2 in [0,1].
One inspection always fails (1), because epsilon=1/2. Two suffice exactly
when v>1/2. Their net gain is

`V_C=v/2-5/16`.

For v<=1/2, any sufficient audit needs at least three inspections, whose
bill makes its net gain negative. For v>1/2, more than two inspections
only increase cost. Hence the specified funded strict-adoption route is
chosen over opt-out exactly when

`rho > sqrt(5/8)`, with n_*=2.                          (4)

At rho=1 each original gains 3/16 after its update, message and inspection
expenses. The true controller gain before the sunk common bill is 3/8;
the fake-controller deviation gives 1/4. Both effective common goals are
genuinely installed, and the unique additive common-goal effort follows.
The no-audit controller game has no C in equilibrium. Perfect costless
recognition would have admitted a larger region, so it is not substituted
for this actual chosen capability.

Increasing overlap in this comparison raises useful shared research while
leaving the specified capture and audit technologies fixed. A design that
also makes fake controllers harder to detect or raises captured-asset value
needs those changes included. A matched conditional delegate facing the
same false claims and audit authority has the same calculation with its
actual controller-installation expense in place of K. A cheaper genuinely
available implementation can displace the modification route; labels alone
do not establish that cost ordering.

## 4. False rejection and the count of successful changes

Even with no false rejections, selection remains consequential. When (1)
holds and epsilon>0, the symmetric controller game also has a mixed
equilibrium with C probability

`p_C=(epsilon+2K/v)/(1-epsilon) in (0,1)`.

Subtracting D's expected payoff from C's gives
`(v/2)[p_C(1-epsilon)-epsilon]-K`; setting it to zero proves the formula.
F is strictly inferior at that mixture. The original expected gain before
the common bill is `p_C epsilon v`, and actual mutual C has probability
p_C^2. In the section 3 fixture, p_C=2/3 and the net gain after h+2c is
`1/6-3/16=-1/48`. Initial originals anticipating that selection would
decline to fund the audit. The constructive funded path therefore uses
the stated mutual-C selection; it is not an equilibrium-independent
prediction that buying the tests forces genuine adoption.

If each genuine controller is falsely rejected with probability tau,
independently across the two checks, mutual C activates with probability
`a_C=(1-tau)^2`. One D facing C receives a useful false Ready with probability
`a_D=epsilon(1-tau)`. The incentive condition becomes

`v[(1-tau)^2/2-epsilon(1-tau)] > K`,                    (5)

and the mutual original gain before the common bill is
`(1-tau)^2 v/2-K`. This is obtained by the same realized-output calculation,
not by applying a new utility to the initial decision. A weak audit can
waste real update work even if it deters false claims.

Report the events separately: a paid conditional template is a genuine
ordering change over the then-possible histories; successful activation
of two common production goals has probability a_C; a false Ready against
D activates only one genuine common production goal; a counterfeit has no
genuine update. After a failed audit permanently closes the Ready event,
the retained branch agrees with the original future ordering. These facts
must not be compressed into a single undifferentiated adoption rate.

The positive result is an affordable imperfect-audit region supporting
reciprocal change, with a chosen audit level and direct output accounting.
The limits are equally explicit: a detectable finite deceptive class,
funded observable inspection, a selected consent equilibrium and a specified
production window. Richer counterfeit strategies, correlated errors and
later bargaining remain actual implementation questions, not assumed
consequences of the agents' ability to understand their own goals.
