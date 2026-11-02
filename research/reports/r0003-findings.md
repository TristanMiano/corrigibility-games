# When credible information makes changing goals worthwhile—and when checking costs lead to combat

**Third recurrence findings.** The main result is a solved small game in
which agents choose genuine preference changes to make information credible.
Cheap checking supports peaceful play. Raising the checking price past an
explicit threshold supports a different equilibrium with actual combat.
The same original goals can therefore produce either outcome as the setting
changes. The results cover a parameter family, with ordinary contracts,
delegation and costed repairs compared explicitly.

The strongest conclusions are:

1. **An agent can prefer a genuine goal change because it makes a useful
   claim credible to someone who controls its future.** The choice is made
   using the agent's original goals. In the successful region, both original
   agents benefit and combat remains available throughout the live game.
2. **Checking above the receiver's combat threshold makes fighting an
   attractive way to resolve uncertainty.** In the worked example, raising
   the checking cost from .010 to .012 changes the selected outcome from
   zero combat to combat in about 8.4% of interactions. No prior commitment
   to punishment is needed for this result.
3. **Better verification and feasible agreement redesign can favor peaceful
   accommodation.** Improved verification benefits both original agents in
   the continuous-policy model. Usable transfers and a chosen checking
   commitment can repair the displayed combat incentive. A timely safe exit
   can protect accommodation even with symmetric combat damage.
4. **The productive model can use simpler obligations.** Rewarding actual
   delivery by the physical deadline avoids unnecessary early-effort reports
   and additional goal installations. Its full private-information equilibrium
   remains open; the completed equilibrium is the smaller information game.

These findings advance the project's constructive question: when does
accommodation serve an agent's existing goals? They identify successful and
combat-favoring conditions without assigning a prevalence to either among
natural agents. This is a recurrence report, not project synthesis.

## Why an agent would choose a new goal

Imagine a machine whose appropriate setting depends on a condition known
to one party, the sender. Another party, the receiver, controls the setting.
The receiver wants a setting suited to the actual condition. The sender
prefers a higher setting and also values its own project resources. Both
possible conditions give the unchanged sender a reason to ask for a high
setting, so an ordinary unsupported claim conveys little useful information.

The sender can instead adopt a goal that favors the state-appropriate
setting. A real checking procedure can recognize that active goal and
authenticate a fresh report chosen by it. The check recognizes a specified
procedure; it does not directly reveal the private condition. After changing,
the sender tells the truth because truth now serves its current goal.

In the high condition, the original sender benefits: a credible report gets
the favorable setting, and that gain exceeds the update's actual cost. In
the low condition, changing would produce the low setting and spend extra
resources, so the original sender declines. This difference supports
credible information and makes the high-state change instrumentally useful.

The change is genuine even though both the original and new high-state goals
favor the high deterministic setting. They disagree over lotteries involving
intermediate settings. The proof gives an explicit reversal of lottery
preferences, rather than counting a renamed program as a new utility.

The model also allows a protected truthful delegate that preserves the
sender's utility. At equal price it can tie with direct change; at a lower
price it replaces direct change. At a higher price the high sender strictly
prefers changing. The shared benefit is credible future behavior. A matched
delegate explains that benefit while preserving the finding that genuine
change can be an optimal voluntary choice.

## The same game has a precise peace/combat boundary

A claim consumes resources. After receiving one, the receiver can accept it,
pay for a diagnostic, or fight for control. Combat has finite physical damage
and a strength-dependent chance of victory. The winner learns the condition
and controls the machine. Neither original utility includes a reward for
violence or for being corrigible.

Let `s` be the sender's chance of winning combat, `d_R` the receiver's own
combat damage, and `v` the checking cost. At the relevant claim-stage
posterior, the finite-policy model's boundary is

\[
\boxed{v_*=d_R/(1-s).}
\]

Below that price, the selected equilibrium uses checks and voluntary goal
changes. Above it, the receiver mixes accepting claims with fighting.
Some low-state senders make false claims, leaving exactly enough uncertainty
that combat is a current best response. This differs from a threat that
would be abandoned once the receiver knew the claim was true.

The example uses equal prior probabilities, sender victory probability .05,
receiver combat damage .01, sender damage 5, claim cost .01 and goal-update
cost .45. Its threshold is 1/95, about .010526. Costs are normalized through
the assumed valuation of useful project output; they are not empirical
measurements or units of conserved energy.

| Outcome in the selected equilibrium | Checking costs .010 | Checking costs .012 |
| --- | ---: | ---: |
| Genuine goal changes | 49.5% | 0% |
| Actual combat | 0% | About 8.4% |
| Original sender's expected loss | 1.22775 | About 1.42097 |
| Original receiver's expected loss | About .00505 | About .00532 |

Losses include actual costs; lower is better. At the boundary there are
mixtures of checking and fighting, rather than a unique prediction. These
are rates within specified selected equilibria, not population statistics.
The exact finite-game check includes staged installation, refusal, stopping,
fresh reports, delegates, private information and off-path combat choices.

Allowing every intermediate machine setting preserves the transition. The
receiver then compromises at its posterior mean, and the threshold changes
to the explicit quadratic boundary in [the proof](../notes/072-verification-cost-and-uncommitted-combat.md).
Thus the result does not depend solely on having three available settings.

The parameters explain the incentive. A receiver that suffers little damage
and is likely to win can find combat a cheap source of information and
control. Greater damage to that receiver, or a stronger sender that is more
likely to retain control after combat, raises the checking cost the receiver
will tolerate. These statements hold the other costs and available actions
fixed. Increasing every capability together requires a different comparison.

## Which values and settings favor accommodation

The original agents need to value outcomes that credible interaction can
improve. Here that means useful project output and a preferred machine
setting. They need no original intrinsic preference for changing themselves.
The high sender's gain from credibility must cover its implementation cost,
and the receiver's information gain must justify checking at the time it
actually chooses whether to check.

| Condition | Established effect and scope |
| --- | --- |
| A cheap authenticated goal change is among the best available diagnostic responses | The high original sender voluntarily adopts it; an equally cheap protected delegate can tie. |
| Checking costs less than the live-claim combat threshold, with the stated initial participation conditions | The selected finite equilibrium is peaceful and uses genuine changes. |
| Checking exceeds that threshold | The selected equilibrium uses actual combat to screen uncertain claims. |
| Verification becomes more reliable at fixed attempt cost and other capabilities | In the continuous-policy diagnostic region, both original agents benefit, false claims fall, and genuine changes become more frequent. |
| A feasible transfer compensates the receiver for a credible peaceful checking commitment | Both original agents can prefer that package to the displayed combat continuation. |
| A timely safe exit preserves useful resources | It caps what a threatening controller can extract and can protect the accommodation mechanism. |
| Successor concern values the partner's preserved output in the reactor model | Sufficient concern makes continuing production preferable to combat even after pessimistic beliefs about private effort. |

The result about better verification is especially relevant to the charter's
capability hypothesis. It changes an explicit capability: successfully opening
an authenticated channel at a given real cost. Within the derived region,
the strategic response improves both original welfare coordinates. More
changes in that model accompany better outcomes. In a different timing
comparison, waiting until a real challenge saves installations while preserving
the information benefit. A count of modifications alone therefore needs an
outcome measure alongside it.

## What capable agents can repair

The diagnostic is paid for before the sender installs its goal, and the
installation takes three private stages. A first version let low senders
decline immediately. Their absence then revealed the high state before
installation finished, leaving the receiver indifferent about stopping
early. A simpler response schedule fixes that leak: low senders wait until
the response deadline, while high senders privately install. At every
checkpoint the receiver still values the remaining information and strictly
prefers finishing. Early refusal and combat remain available. This repair
uses zero incremental waiting cost; costly waiting needs further analysis.

Agents can also redesign the agreement. A receiver may choose a credible
partial-checking rule that deters false claims. Its setup and execution must
be paid for, and it can compete with a cheaper destructive screening rule.
When an actual transferable resource is available, the sender can compensate
the receiver for peaceful checking. At the .012 example, a checking setup
cost .001 and an enforceable ex ante payment .01 give both original agents
a strict gain over the uncommitted combat outcome. This is a constructive,
costed repair, conditional on real payment and commitment authority.

Ordinary mechanisms receive broader comparisons as well. Binding menus of
policies and lotteries are included. With usable payments capped as stated
in the proof, a whole class of ordinary report-selection contracts remains
more expensive to the receiver than the diagnostic, including priors near
50–50. Cheap observable sacrifices, direct state sensors or protected
delegation can instead displace the goal-based mechanism. Their availability
and actual costs determine the choice.

One attempted extension failed an audit: a bound justified by the receiver's
low-state belief was incorrectly being used to bound the high state's actual
payoff. A state-contingent goal can induce different later behavior in those
states. The counterexample can itself make an alternative genuine change
attractive. The corrected extension requires sufficient actual total costs
or an independently proved continuation restriction. The solved finite core
survives; a theorem covering equally cheap arbitrary early programs remains
open.

## What changed in the productive model

The earlier reactor model asks a related question: can agents choose goals
that make a mutually productive plan credible? This round found workable
repairs and clarified what still needs proof.

One guarded contributor can make an ordinary output contract sufficient for
the other. The ordinary agent saves its installation cost; the negotiated
division of that saving determines whether it keeps its utility, ties with
changing, or prefers changing. Genuine accommodation can therefore be useful
without both participants adopting the same kind of goal.

A second issue concerns renegotiation after a private breach. If the partner's
new-agreement reservation automatically falls to the damaged fallback, a
shirker can gain by changing goals late and demanding most of the recovered
surplus. Preserving the earlier registered promise blocks that displayed
rent. Current concern for the partner can still make restoring the promise
acceptable, even when one agent's conditional original material share falls.

The simplest execution repair is to reward actual input delivery by the
latest feasible physical date. Earlier preparation can remain optional.
Each party then pays for one calibration, without a fresh update merely
because an earlier window passed. This matters materially: the earlier
fresh-update proposal spent output that was already promised to the parties.
Spare computation or work capacity did not replace that missing material.

These local results preserve a promising productive construction. They do
not yet supply the reactor's full command, interruption and authority game.
That distinction is explicit in the [technical model](../models/E4.md).

## How natural are the conditions, and what remains open?

The original goals are simple quadratic disagreements plus own-output value;
the productive examples use linear own-output goals. Successful conditions
hold on parameter regions, including continuous intermediate policies and
nearby priors. They are stronger evidence of breadth than a single numerical
coincidence, while remaining model-specific.

The technology is demanding. Recognizing an active goal, protecting its
private-state input, authenticating a fresh report and enforcing a delegate
are separate capabilities. The initial information example also uses strong
asymmetry in combat exposure. A safe-exit variant supports the diagnostic
with equal combat damage and arbitrary interior strength shares, but timely
safe exit is itself a substantive physical assumption. Engineered process
rewards and guards in the reactor model require the same scrutiny as
engineered threatening goals. Neither class is established as typical.

The proved scope is selected adoption and execution in the finite diagnostic
game, its parameter boundaries, and the stated local repair/comparison
theorems. Global renegotiation stability, fully costed physical implementation
of the enlarged menu, indefinite innovation, coalition stability and
population prevalence remain open. The next useful step is to close one
causal physical implementation and renegotiation gap for this same diagnostic
class, seeking both adoptable accommodation and its combat/retention boundary
under the same capabilities. **CG-03 remains blocked.**

The run used **4h 5m 40s of conservatively estimated active research,
88.74% theory**. Report writing and review are excluded. The
[run record](../runs/r0003.md) links the proofs, source audits, exact checks
and accounting. This work uses conventional communication, inspection and
equilibrium machinery; no general novelty or independent verification claim
is made.

I performed the de-biasing self-review required by
[AIM_BALANCE](../AIM_BALANCE.md#4-end-of-task-review). The work reintroduced a risk of overprotecting the favorable protocol
through its initially closed menu. I also checked the standing risks of
treating matched delegation as a defeat for genuine change and letting
repeated gap-finding obscure successful repairs. I compared cheaper ordinary mechanisms, added late-control and
transfer options, preserved the staged adoption result, and replaced the
invalid cross-state payoff bound with a counterexample and narrower valid
conditions. I also paired the actual-combat regime with costed peaceful
repairs and assessed engineered threat and accommodation technologies by
the same standard. The review covers the changed artifacts and handoff;
it is a contributing-agent self-review, with full physical implementation,
broader stability and prevalence still unresolved.
