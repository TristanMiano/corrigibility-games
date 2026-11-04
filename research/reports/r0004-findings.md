# When negotiated goals, credible threats and protection change the bargain

**Fourth recurrence, 2026-11-02–03.** The main result is a class of games
in which both original agents benefit from a negotiated preference change,
choose it under explicit implementation assumptions, and then carry out
peaceful trade. The result survives stronger ordinary contracts, finite
punishment after a combat audit, a range of uncertainty, and any strength
split giving both sides a positive chance of victory. Allowing an attractive
early goal change alters the disagreement payoff; negotiating a different
shared goal repairs the agreement against that alternative too.

The explanation is economic and physical. **A preference change can be
worth buying when it makes useful information credible more cheaply than
the available payments, punishment or verification.** **A strong preference
for reaching a minimum outcome can make combat credible when the chance
of achieving it outweighs the material loss.** **Protection that removes
that opportunity can make peaceful accommodation preferable.** Continued
stability depends on how much additional joint benefit remains available
and what it costs to change the arrangement again.

These are conditional results, with important boundaries. Cheap protected
delegates can match the goal changes. Timely paid counteroffers can save
the update expense and produce compromise with unchanged goals. In a
fully informed control where ordinary trade already reaches the funded
Pareto frontier, a costly goal change cannot improve both original agents.
The work identifies reasons for each outcome; it does not estimate which
agents or technologies are common. [E5](../models/E5.md) contains the formal
model, and the [run record](../runs/r0004.md) records evidence and scope.

## 1. Credible information can make changing goals mutually advantageous

Imagine two agents with different preferred settings of a project. One
agent, the sender, privately knows which state the project is in. The
receiver controls its setting. Both value useful output and have simple
quadratic policy preferences: being farther from their preferred setting
is worse. Their original goals contain no reward for being corrigible.

The sender would like the receiver to choose a higher setting. That makes
an unsupported favorable report tempting to imitate. An ordinary contract
can demand payments, burn resources to separate reports, or use a costly
contest to acquire reliable information. A genuine successor goal can
instead make a fresh truthful report serve the successor's own interests.
The original sender agrees to that change only when the resulting bargain
is better according to its original goal.

This round makes the installation less idealized. It takes several paid
steps, completed progress is visible, either party can interrupt, and
attacks remain possible. The current evaluator changes only on actual
activation. Physical recovery depends on remaining work and time; fuel
energy, useful output and utility are distinct quantities.

The receiver can also adopt a negotiated goal before the private state
is drawn. A real initial payment compensates it under its original
preferences. The choice of target matters: moving it toward the sender
benefits the original sender and costs the original receiver over the
relevant bargaining range. This gives the negotiation a concrete tradeoff.

Here is one example. The numbers are **losses, so lower is better**;
a negative loss reflects net useful receipts after policy costs. They
compare each agent using its original utility.

| Arrangement | Original sender loss | Original receiver loss |
| --- | ---: | ---: |
| Actual disagreement, including ordinary late cash trade | 1.010424 | -0.089850 |
| Negotiated target .42 and full initial payment | .869374 | -.090648 |
| Receiver-proposer target .22 and full initial payment | 1.005475 | -.154650 |

Both originals gain in either negotiated example. Proposal rights affect
who receives most of the improvement. The receiver changes its goal in
advance; in the first package the sender completes its own genuine update
with probability about .479, when sufficiently challenged. Other branches
settle earlier. Actual combat is zero in the selected continuation.

The result covers state probabilities from .45 to .55, with the proposed
goal adjusted to the known environment. It also survives any sender win
probability strictly between zero and one while the specified damage,
cash and punishment limits are held fixed. The proof covers the interval;
it is not an extrapolation from a sample. Initial proposal and completion
are conditional on the priced recognition, custody and additional-controller
interface stated in [084](../notes/084-prestate-completion-and-scope-of-the-offer-game.md).

## 2. Stronger ordinary alternatives make renegotiation necessary

The first goal package failed a stronger comparison. A binding ordinary
controller could occasionally fight to verify a favorable report and
destroy additional sender assets if it caught a lie. A large credible
penalty made a small audit probability sufficient. With positive setup
expenses, this ordinary mechanism gave the sender a better outcome than
the initial proposed goal package while satisfying the receiver.

The useful response was to change the agreement. Paying the full available
budget earlier and negotiating a different target produced the .42 package
above. It beats every accepted ordinary mechanism in the specified
communication/payment/capture class, including punishment up to the
remaining finite stock. The comparison generously grants the ordinary
controller binding policy and launch authority without setup expense.
The goal package's advantage is therefore not obtained by omitting ordinary
trade or making ordinary commitment artificially costly.

There is a real boundary. In the worked environment, increasing usable
punishment capacity from 15 to about 23.87 makes the best ordinary audit
catch up with that *fixed* .42 package. Such punishment requires more
assets than the original physical inventory permits. It also needs actual
work, targeting and commitment. The crossing calls for another negotiation;
it does not prove that every possible goal package loses in the larger
environment. [083](../notes/083-costed-combat-information-and-renegotiated-goals.md)
and [085](../notes/085-sharp-choice-frontiers-and-goal-bargaining.md) give the
frontier and its assumptions.

An attractive early goal change provides another serious alternative.
By reducing its future willingness to pay, the sender can force the
receiver to offer a larger concession for a payment. That early option
improves the sender's disagreement payoff. Renegotiating the shared
target again produces packages preferred by both originals and better
for the proposer than the qualifying ordinary controls. This repair also
works with strictly truthful early reporting. Cheap repeated and
two-sided goal choice remains a broader game, rather than something
silently excluded from a claim about all agents.

## 3. Minimum-outcome priorities and unprotected exposure can favor combat

The clearest value condition is direct. If a contest gives policy 1 with
probability s and policy a otherwise, an agent with outcome value V fights
against an offer y when

\[
sV(1)+(1-s)V(a)-V(y) > \text{its effective material loss}.
\]

For an increasing concave value function, a sure offer above the contest's
mean policy is preferable. A threshold project creates a different
incentive. Suppose reaching at least z is worth W and falling short
obtains none of that project value. Then a subthreshold offer induces
combat when **sW exceeds the material cost**. Reaching the threshold
peacefully is preferable. The agent values a particular achievement;
violence is a means to obtain a chance at it.

An original agent with a smooth quadratic goal can choose such a successor
because its credible threshold induces a better concession. The receiver
can anticipate that move and fight *before* installing or verifying the
threatening controller. In the checked one-frame example, that produces
actual combat with probability about **4.57%**. The threatening successor
is off path: its feasible future behavior changes the earlier decision.

A prepared exit reverses the incentive if it can protect the relevant
stocks and dispatch the policy before an attack can affect them. The
threshold successor then gains no chance of achieving its project by
launching an ineffective attack, so it declines to do so. The original
sender consequently declines to buy that threatening goal. Peaceful
diagnosis and genuine cooperative updating return. The receiver buys the
safeguard when its setup cost is below about **.0002745** in this example.

That price is a willingness-to-pay result, not an engineering estimate.
Detection time, transport speed, valuable exposed infrastructure and the
actual setup work determine whether the safeguard exists at that cost.
A separate recovery-backup example reduces extortion and expense while
both compared regimes already avoid combat; those gains are not reported
as a reduction in fighting. [082](../notes/082-fast-exit-early-goals-and-negotiated-safeguards.md)
and [089](../notes/089-outcome-threshold-goals-and-combat.md) explain both sides.

## 4. Small remaining joint surplus can stabilize a chosen goal

A successor may find another preference change advantageous. In the simple
known-state pricing game, a current target a can gain by changing to a/2
when **a²/4 exceeds the update cost**, subject to the quote's feasibility.
A broader concave replacement family can obtain a²/3. The original
founder can dislike that later change even though the successor correctly
chooses it under its then-current preferences.

There is also a broad constructive stability condition. If the receiver
can physically protect a fallback of loss at most e, and no new outside
resources appear, the sender cannot obtain more than the available joint
surplus by installing another goal. For the quadratic known-state case,
an update costing more than **a²/2 + e** is inferior to retention,
regardless of the replacement criterion. A more accommodating target
reduces that remaining surplus. Protection and a chosen goal can therefore
support stability together without an intrinsic preference for freezing.

The round also constructs a threshold successor that is attractive to
its founder and has so little remaining joint surplus that every further
replacement in the stated physical class costs more than it can gain.
This is a known-state bargaining result with a protected fallback, not
yet a complete reusable-goal version of the private-information model.

Timing can instead favor ordinary compromise. If a funded counteroffer
arrives before activation, the agents can sometimes implement the same
policy with the incumbent goal and share the installation expense that
has not yet been spent. That can replace actual utility change with
unchanged-goal trade. After activation, the successor may reject the same
price. [091](../notes/091-joint-surplus-and-stable-outcome-goals.md) and
[092](../notes/092-paid-counteroffers-before-goal-activation.md) keep initial
choice, actual completion and later stability separate.

## 5. Which assumptions are simple, and which are demanding?

| Feature | What it explains | Assessment of its scope |
| --- | --- | --- |
| Quadratic policy disagreement and linear value for own output | Ordinary trade, signaling and the negotiated target | Simple preference class; no distribution over actual agents is assumed. |
| A valuable threshold project | Credible fighting below a minimum outcome | Short description with an explicit value/strength/cost boundary; the numerical weight is chosen, not measured. |
| Finite specialized stocks, work and delivery time | Limited punishment, costly recovery and meaningful exit timing | Physical mechanisms are explicit; the calibration and asymmetry of exposure are model choices. |
| Fresh recognized goal reports and protected delegation | Credible information and the control comparison | Demanding implementation technology, distinct from utility self-knowledge. |
| Cash custody, proposal order and available quote windows | Who can compensate whom, and when a cheaper ordinary bargain intervenes | Consequential protocol assumptions; several enlargements were tested, reusable two-sided bargaining remains open. |
| Endogenous mixed checking | Selected peace/combat frequencies | Consistent finite assessments are checked; no unique equilibrium, population prevalence or engineering precision theorem is claimed. |

The strongest joint result uses avoidable information costs. In a fully
informed control with the same cash limit, ordinary trade already reaches
the constrained Pareto frontier. A costly goal change cannot make both
original agents better there, even though it may improve one agent by
reducing the other's bargaining income. This is why it matters to ask
where the additional joint benefit comes from.

An equally priced protected delegate can reproduce the relevant goal
mechanism. Reproducing the whole two-party package with fixed utilities
also needs receiver policy authority. A cheaper equivalent device can
be selected instead; an equal-cost tie remains a valid voluntary genuine
change. The comparison identifies credible future behavior and its real
price as the source of the benefit.

The mathematical machinery overlaps established work on costly signaling,
stochastic verification and inspection. This round checked relevant primary
material, including [Townsend's verification model](https://economics.mit.edu/research/publications/optimal-contracts-and-competitive-markets-costly-state-verification),
[Kartik's burned-money analysis](https://navinkartik.com/Papers/burned_note.pdf)
and [von Stengel's recursive inspection games](https://arxiv.org/abs/1412.0129).
The [literature ledger](../LITERATURE.md) records versions and reading limits.
The contribution claimed here is the conditional integration, comparisons
and repairs, rather than priority for those established techniques.

The run's original next recommendation was one joint initial-offer and
continuation game with a priced reusable goal/safeguard menu and live funded
counteroffers. It should seek
stable mutually attractive accommodation and equally test obstructions
after changing goals, payments, delegates and protection. Repeated resource
renewal, counterparty choice and population prevalence remain open.
**CG-03 remains blocked; this report completes a recurrence, not synthesis.**

**2026-11-03 review update:** the [portfolio review](2026-11-03-scope-and-incentives-review.md)
redirects the next recommendation toward renewable productive cooperation
and partner choice, preserving the implementation questions above as open
backlog. It also gives consensual utility change modest research priority
and adds explicit assessment of which incentives parties can feasibly
create and would choose to create. This editorial update adds no theorem
or recurrence time; its separate aim review is recorded in the linked audit.

This report and its supporting work received the required [AIM_BALANCE](../AIM_BALANCE.md#4-end-of-task-review)
de-biasing self-review. The research risked favoring the initial goal package
through narrow ordinary controls and costly alternative programs; adding
finite captured-state punishment actually displaced that package, and
renegotiating its target and budget repaired it. Cheap early and further
goal changes, matched delegation and pre-activation paid counteroffers were
then tested rather than treating the first installation as permanent.
The review also separated unilateral bargaining gains from mutual original
improvement, effective contests from futile attacks, and proven local
stability from unresolved repeated bargaining. Those corrections preserve
the achieved constructive results and their limiting conditions; this is
an AI agent's self-review, not independent verification or a guarantee
against remaining bias, and the implementation and prevalence limits above
remain substantive.
