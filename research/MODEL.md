# Formal contract C1 — a family of corrigibility games

Version C1, 2026-10-30. **CG-01 complete.** This contract fixes accounting and interpretation, not one favored game's substantive assumptions. [Reference instance E1](models/E1.md) supplies one fully specified finite two-agent game. Its numbers, horizon, information structure, utility menu, and bargaining protocol are **local examples, not recurrence defaults**. A recurrence may replace them without amending the charter.

## 1. A model is a declared tuple

Specify an instance by

$$\mathcal G=(I,\mathcal H,Z,L,A,\mathcal K,\mathcal O,\mathcal B,\mathcal U,\mathcal M,\mathcal T,\mathcal S).$$

| Component | Required declaration | Open choices |
| --- | --- | --- |
| I, H | Agent identities, histories, initial conditions, horizon/termination | Begin with two agents; later coalitions, entrants, mergers; finite, discounted, or other well-posed evaluation |
| Z | Physical state, units, system boundary, resource balances | Spatial/material/thermal detail, recovery networks, capacity, multiple outputs |
| L | Agency and physical capability at each history; identity/successor map | Survival, incapacity, capture, repair, delegation, merger |
| A | Physical actions and who can decide when, including attack | Simultaneous, sequential, continuous/event time; preemption and interruption |
| K | Joint stochastic kernels for state, agency, elapsed time, and implementation | Endogenous power, asymmetric destruction, uncertain updates and external hazards |
| O, B | Observation maps, information sets, beliefs and updating | Public/private preferences, noisy observation, common or differing priors |
| U | Current preferences over a declared common outcome/history domain | Linear, nonlinear, threshold, process, identity, freezing, lexicographic classes |
| M | Permitted changes, execution steps, verification, rollback, successor behavior | Restricted or rich utility/program menus; atomic/sequential; reversible/durable |
| T | Peaceful mechanisms and implementation technology | Trade, flexible policies, contracts, delegation, voluntary modification |
| S | Solution concept and result being sought | Feasibility, adoption, dynamic equilibrium, coalition stability, population selection |

An instance must fill these entries sufficiently to determine legal histories, transition probabilities, and the evaluation of every decision, including deviations. The tuple is a specification checklist, not a requirement to build a general simulator or supply every conceivable extension. For infinite/continuous spaces state measurability and existence/integrability conditions actually needed.

Separate **invariants** (the repository's interpretation/accounting rules) from **instance assumptions** (which may change) and **comparison technologies** (which may be stronger). Give each result a model/version and assumption IDs. A changed protocol or utility domain can change a theorem; do not transfer claims just because both instances implement C1.

## 2. Histories, identity, and current-utility evaluation

A full history records physical states, actions/messages, elapsed time, chance outcomes, implementation events, installed objectives, and agency/control changes. An agent may observe only a projection of this history. Current utility self-knowledge is not public observation, semantic verification, common knowledge, or commitment.

For expected-utility instances, the agent deciding at information set J with current criterion U_i^J evaluates a candidate action or modification m by

$$V_i^J(m;\sigma)=\mathbb E_{\mathcal B_i,\mathcal K,\sigma}[U_i^J(H)\mid J,\operatorname{do}(m)].$$

Subsequent selves use their then-current criteria; the expectation models those policies rather than assigning the founder perpetual control. Report founder welfare E[U_i^0(H)] separately. A new utility's approval of its own installation is not an adoption argument. For lexicographic or hard-admissibility variants, replace this numerical maximization by the specified preference relation; do not import expected-utility results automatically.

Define utility change on a declared common domain of outcomes or lotteries. Under expected-utility assumptions, positive affine transforms represent the same preference ordering. Code identity, beliefs, representation, observed policy, and preferences are different coordinates. Specify whether freezing penalizes each change, departure from a reference preference, capture, successor creation, or a route to an outcome. Rollback need not undo a historical penalty.

For every death, defeat, merger, or delegation state, identify who can still act and what each surviving or original criterion values. A defeated agent can value its project after losing control. A merger can terminate separate agency without erasing original welfare assessments. These are kernel/utility choices, not consequences of winning probabilities.

## 3. Physical mechanisms and accounting

A useful expandable state interface is

$$z=(\mathbf m,\ell,\chi,\Theta,B,K,t),$$

where m is material inventory/composition, ell location, chi organization, Theta thermal state, B available work relative to a declared environment, and K infrastructure/capacity. An instance need retain only sufficient coordinates for its mechanism. If B is derived from the rest, do not also treat it as an independent free resource. If it is only a battery/work reserve, say so rather than calling it total system exergy.

Give combat, ordinary compromise, and utility-modifying compromise explicit kernels (possibly compositions of implementation steps):

$$K_j(dz',dL',d\mathbf U',d\mathbf a',d\tau\mid h,\text{actions}),\quad j\in\{C,P,M\}.$$

Account for material flows, transformations, unavailable work, damage, restoration effort, delay, and negotiation/verification/computation/install costs within those transitions. Matter can change categories without disappearing; energy dissipation is not energy destruction. Useful output, available work, conserved energy, and utility must remain distinct. No identification of Shannon with thermodynamic entropy is licensed. [L07 and L11](LITERATURE.md) delimit the physical background and its access limits.

Derive both the region where avoided damage leaves a larger implementable peaceful opportunity set after negotiation costs and the region where that margin disappears or reverses. Scarce recovery work, infrastructure loss and delay can favor compromise; expensive verification, cheap recovery or goals valuing combat can favor another route. Test each through the declared physical kernels and current utilities, with no uniform ordering imposed. A constructive region and an adverse region each retain their conditional scope.

The initialization's recovery frontier remains a useful **optional continuous submodel**:

$$Y(O,D,Z,B,k;T)=\max y$$

subject to

$$0\le x_D\le D,\quad0\le x_Z\le Z,\quad0\le y\le O+x_D+x_Z,$$
$$w_Dx_D+w_Zx_Z+w_y y\le B,$$
$$t_Dx_D+t_Zx_Z+t_y y\le T,\qquad y\le kT.$$

Material units, work/unit, time/unit, and output/time must match. Additive processing-workload time, divisibility, single output, fixed coefficients, and the separate aggregate capacity bound are assumptions of this LP, not C1 invariants. A literal serial line whose production rate is k needs the coupled time condition with production duration max(t_y,1/k) per unit; [note 024](notes/024-recovery-scheduling-and-infrastructure.md) supplies that correction and other scheduling models. Parallel lines, integer batches, spatial transport, cooling, endogenous repair, and vector outputs can replace the aggregate LP. An aggregate LP is not automatically equivalent to a dynamic scheduling problem.

## 4. Timing, information, and persistent combat

At relevant nonterminal histories, every capable agent must have a physical route to initiate combat. Specify opportunities for non-proposers, attacks during verification/installations, and attacks following agreement. An agreement or favorable utility cannot itself delete attack. A delegate may choose never to attack while retaining the physical action; disarmament and externally imposed last-resort rules are separately labeled controls.

An instance must define collision/priority rules when attack coincides with another action, the time resolution within which no new decision occurs, and what survives an interruption. Terminal states, incapacity, and loss of separate agency must be explained physically or by the chosen task horizon. A deadline does not establish peace beyond that deadline.

A contest function such as q_A=a_A^r/(a_A^r+a_B^r) is optional. If used, handle a zero denominator, specify the units/meaning of power, and supply casualty, control, material, and recovery kernels conditional on each outcome. The victory probability alone is not a combat model.

Specify rejection, inaction, ordinary work/trade, exit if feasible, and further offers. Rejection is not defined to mean war unless the particular protocol physically warrants that restriction. Perfect outcome modeling means knowledge of stochastic laws, not random realizations. Common probabilities, complete information, and preference observability require separate assumptions.

## 5. Mechanism comparison and solution concept

Compare the following, stating any differences in feasible actions, physical inputs, information, costs, horizon, and implementation:

1. Fixed terminal utility with flexible policies and ordinary peaceful allocations.
2. Fixed utility with enforceable contracts or delegation.
3. Voluntary utility modification, including future modification/rollback options.
4. Combat and noncombat disagreement continuations.

Do not grant the third verifiable, atomic, durable implementation while denying comparable technology to the second without labeling that difference. Likewise, irreversible delegation is not automatically a matched control for reversible utility changes. Preserve strong fixed-utility controls even when they reproduce modification's outcome, and preserve voluntary-change results when a matched delegate reproduces their benefit. Determine which devices are actually available, their costs and stability, and whether modification is strictly chosen, tied or displaced. Unique superiority to every equivalent device is a separate question from instrumental adoption.

Each instance must choose a solution concept. Ordinary SPE can describe fixed-utility complete-information games. With changing utilities, a finite **decision-self** formulation can require local best responses under the utility installed at each decision, given the actual policies of later selves; E1 defines this precisely. Private-information variants must specify information sets, belief consistency, and an appropriate sequential solution concept. Discounted/infinite variants must supply convergence and any equilibrium existence assumptions. No concept or equilibrium selection is mandated across all instances.

A finding must identify its level: feasible bargain; incentives to offer/accept; equilibrium selection; stability against attack, rollback, or renegotiation; coalition stability; or population prevalence. One level is not evidence for all others.

## 6. Extensions available to the recurrence

| Variation | Change explicitly | Recheck |
| --- | --- | --- |
| Changing power / preemption | Power state and investment/combat kernels; action order | Future attack values, credible transfers, first-strike incentives |
| Hidden preferences / imperfect updates | Observation map, beliefs, failure and verification kernels | Adoption under uncertainty, off-path beliefs, semantic vs syntactic evidence |
| Long-run freezing | Horizon and current preference relation; opportunity stream and commitment benefits | Well-defined values, voluntary relaxation vs mere selection |
| Coalitions / mergers | I, joint actions, agency map, coalition feasibility | Who consents, deviates, survives, and retains welfare claims |
| Rich physics | State/work boundary and recovery technology | Conservation, feasible outputs, delay and double charging |
| Population evolution | A separate demographic/fitness/transmission model | Fitness vs utility, matching, mutation, invasion/coexistence |

For population work an optional two-type equation is
\(\dot x=x(1-x)[F_M(x)-F_F(x)]\), but its fitness functions must be derived from specified interactions and a transmission process. Mutation and assortment require their own laws. Neither extinction of freezing nor voluntary acceptance is built in.

These variations can be combined; they are not a sequence of required mini-projects. Start with the smallest instance that can decide the chosen question.

## 7. CG-01 completion and first tractable target

[E1](models/E1.md) fills all components with a finite, dimensionally coherent example, explicit stochastic combat, peaceful fallback, sequential updates, and an equilibrium criterion. Its checks establish only that the specification is usable. Its discrete stock, three utilities, and public monitoring are replaceable choices.

The selected first physical mechanism is **dispersion requiring extra recovery work and time**. Derive a conditional production frontier with control held fixed; compare (O,D) with (O-d,D+d) at matched work/deadline/capacity, then embed the frontier in a bargaining continuation with attacks retained. Begin with the LP above or E1's integer processing technology as appropriate, explicitly naming which. Test boundaries before adding thermal, chemical, or coalition detail. A physical subproblem holding attacks fixed is not a baseline game that forbids them.

This is a research target, not a new proved result. Q01-Q06 remain open. The [literature map](LITERATURE.md) explains overlap and the closest assumptions to audit during CG-R001.
