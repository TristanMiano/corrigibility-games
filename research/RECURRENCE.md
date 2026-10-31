# CG-R001: main research recurrence

This is the project's single repeatable substantive research task. Each explicit invocation runs one research increment and produces a durable handoff. It is not a scheduled automation and does not authorize an endless series of unattended runs.

Read and follow the charter's binding [Aim preservation and balanced research](AIM_BALANCE.md) before selecting work. Its local pairing rule and [end-of-task review](AIM_BALANCE.md#4-end-of-task-review) apply throughout this protocol, including to partial handoffs and reporting-only follow-ups. Positive constructions and scoped negative results receive equal explicit search and scrutiny; neither universal cooperation nor universal failure is the presumed answer.

## Invocation and defaults

Example: `Run the next CG-R001 recurrence.`

Canonical settings:

| Setting | Default | Meaning |
| --- | --- | --- |
| `research_time_floor` | `4h` | Minimum active research in this invocation, excluding administration and idle time |
| `theory_share_min` | `0.75` | Minimum fraction of counted research spent on mathematical theory |
| `focus` | highest-value unresolved charter question | Optional owner-specified emphasis |
| `run_id` | next unused `rNNNN` | A partial run is resumed, not relabeled completed |

An explicit instruction such as `time_floor=90m, theory_share_min=0.60` overrides only that invocation. A time floor is not a maximum. At the default floor, at least three hours must be substantial theory. If the run is longer, the 75% requirement applies to its actual counted duration, not merely the first four hours.

Before starting, inspect the latest repository state, TODO, ledgers, and run record; resolve any unfinished prior run and state the chosen settings. Do not silently overwrite another agent's changes. Preparation tasks CG-01/02 are outside the recurrence clock unless the owner explicitly changes the scope.

## Explanatory target

Use the [charter's core hypothesis](CHARTER.md#core-hypothesis-to-investigate): agents can instrumentally choose genuine preference changes when negotiated accommodation advances their current goals in a future that other agents still influence. Study the arrangements agents can choose, including revisions of the agreement itself. The primary target is an integrated conditional result over a defensible class, or an obstruction that survives serious attempts to repair the arrangement.

Prioritize **X implies greater cooperation**, **Z implies greater combat**, exact conditions, and parameter boundaries. For each such claim, specify the agent and environment class, the change or comparison being made, the outcome measure, and the equilibrium/selection assumptions. Cooperation may mean a mutually preferred bargain, actual peaceful play, stable accommodation or a population rate; report each separately. A counterexample is useful evidence for locating a boundary; use it to seek the sufficient conditions on either side. A succession of bare failures of implication is not the explanatory objective.

Assess the conditions themselves: which arise from simple goals or physical constraints, which are chosen by agents, which require tailored goals or restricted offer menus, and which depend on demanding information or implementation technology? State the independent motivation for the class and whether the conclusion holds across a parameter region or depends on special equalities and finely tuned choices. Test perturbations and relevant joint changes. Justify any prevalence claim by a population/distribution or structural result. Keep this assessment revisable rather than imposing a fixed taxonomy of natural agents.

## Count research honestly

Count active derivation, construction of models and counterexamples, proof attempts, proof audit, focused scientific literature analysis, and necessary research computation. Classify work as `theory`, `literature`, or `computation`. Only mathematical work counts toward the theory fraction; merely reading a paper or writing a status report does not. A proof derivation prompted by a paper can count as theory when the artifact records the actual derivation.

Exclude repository setup, generic coding infrastructure, ordinary formatting, handoff preparation, idle waits, tool latency without simultaneous active work, and unattended compute. Count concurrent work only once toward the lead run's duration; record helper-agent effort separately rather than summing overlapping worker-hours into four elapsed research hours.

Use observed start/end timestamps and active segments when the environment permits. Record actual uncertainties instead of fabricated precision. Do not infer four hours from an instruction or output length. If a runtime limit or interruption prevents the floor or allocation from being met, publish `PARTIAL`, state the shortfall, and leave a resumption point. Do not silently override the owner's floor, pad time, promise background continuation, or mark the run complete. The owner can explicitly waive or change a requirement.

## Research loop within an invocation

1. **Choose an integrated target.** Select a central conditional implication and the closest existing results. Restate the original constructive aim, its quantifier, and the positive and negative possibilities this task distinguishes. State the defensible class and the missing link from a beneficial opportunity through proposal, current-goal adoption, installation and continued incentives. A run may address one link; keep its contribution to the shared target explicit rather than collecting unrelated cases.
2. **Derive before scaling.** Work through explicit definitions, equations, proofs, and small exact examples. Keep physical transitions and utility semantics visible. Construct what agents can negotiate, including successor goals and safeguards, and account for their incentives to choose it. Spend most of the run here.
3. **Challenge and repair in both directions.** Test promising constructions for missing deviations, hidden commitments, utility-rescaling problems, and mismatch between current utility and founder welfare. Equally test claims of impossibility or general disadvantage by constructing successful arrangements and feasible repairs. When an arrangement fails, investigate how agents could repair it under the agreement-design requirements below. Use failures and successes to refine sufficient conditions, identify parameter regions, or establish an obstruction over the enlarged class.
4. **Compare mechanisms and adoption incentives.** Give controls matched information, physical resources and execution capabilities where feasible. Separate available alternatives from hypothetical stronger technologies. Explain when genuine preference change is attractive under the incumbent's goals, including ties, and what produces the benefit. A matching delegate identifies a shared mechanism and remains compatible with a successful explanation of voluntary change.
5. **Use targeted support.** Check primary literature for constructive mechanisms and enabling results as explicitly as for impossibility results and failure modes. Use exact arithmetic, symbolic tools, or small reproducible experiments to test successful regions and failure boundaries, not replace proofs. Avoid building a large simulator before knowing what claim it is testing.
6. **Consolidate, explain and review the result.** State what was proved, refuted, or left open; identify the assumption dependency and next most informative test. Update ledgers, then write a readable findings report and concise handoff outside the research clock. Perform and record the substantive end-of-task aim-preservation review, correcting both misleading wording and missing counterpart instructions before claiming completion.

These steps recur within a run as useful; they are not separate project milestones or rigid time slices. A sound positive construction, sufficient-condition theorem or successful repair is a legitimate research outcome. A sound negative result, sharply localized obstruction or reproducible counterexample is equally legitimate. Actively pursue and scrutinize both directions with equal seriousness, without imposing a quota of findings or substituting the failure of universal cooperation for the constructive question. Administrative churn alone is not a successful research increment.

## Agreement design and repair

For a central obstruction, record the original agreement space and the restriction causing failure. Try relevant feasible enlargements: renegotiated final objectives and shares; transfers or staged delivery; conditional commitments and delegation; counterparty choice or exit; and an agent's choice of future safeguards. These are candidate repairs, not assumed free capabilities. Carry communication, search, verification, execution and update costs, information, timing and retained attack options into the enlarged game. Recheck initial choice and later deviations, since repairing one stage can alter another agent's incentives.

Classify the result as a failure of the stated protocol, repaired by the enlargement, persistent over an explicitly described richer class, or unresolved after the attempted repairs. Give the reason for excluding a consequential repair. A claim about an entire feasible agreement class needs a quantifier and an argument covering that class; several unsuccessful proposals alone establish only those failures. Conversely, an integrated successful construction needs agents' incentives to propose, adopt and execute it, with the selected continuation and remaining stability scope stated.

[Sequential fusion](notes/012-sequential-fusion.md) illustrates the obligation: allowing negotiation over the final goal can repair a fixed-goal joining threshold, while initial adoption and protection against later concessions remain to be checked together. The [full-menu conditions](notes/026-preferences-and-the-full-peaceful-menu.md) supply possible starting classes, including increasing concave preferences and implementable pointwise improvements over combat. Connect such opportunities to actual choice and continuation; retain flexibility to choose another defensible class.

## Preference change, alternatives and capability

Record both the benefit relative to refusal/disagreement and the incentive relative to the alternatives actually available in the game. A genuine change that is an optimal available choice can be selected strictly or at indifference; distinguish these cases from a merely beneficial proposal displaced by a better available option. Demonstrating a unique advantage over every behaviorally equivalent device is not a requirement. A delegate that matches the continuation at matched cost explains the role of credible future behavior and others' responses. When both are available, each can be an optimal choice; their availability must be established under the agents' actual technology. State evidence or assumptions for the comparative feasibility and costs of each mechanism.

When studying increasing capability, vary explicit capabilities such as discovering agreements, representing successor preferences, verifying implementation or executing updates. Specify which costs and action sets change, and whether combat capability and outside options also change. Seek conditions for the resulting direction of cooperation or combat, with strategic adaptation included. Merely adding a favorable agreement proves an expansion of possibilities; an adoption or equilibrium claim also needs the corresponding incentives.

## Long-run accommodation and chosen safeguards

The long-run target is whether refusal remains advantageous when agents anticipate exploitation, negotiate alternative terms, choose counterparties and design their future commitments. Treat accommodation and protection as joint choices. The finite successor-preservation example is a constructive starting point: an agent can choose a compromise goal and safeguards because the package serves its current goals. Test that package against richer renegotiation and execution possibilities rather than using a freezing parameter as the whole explanation.

Separate continued choice by long-lived agents from reproduction of types. For claims extending to innovation or descendants, specify available goal innovation, encounter/counterparty selection, resource renewal and inherited information/preferences, plus what current agents value about descendants. Preserve current-self evaluation throughout. A finite template population is a diagnostic model; broader persistence or extinction claims need justified robustness to its consequential restrictions. These are cumulative research obligations for the relevant claim, not a demand to solve every extension in each invocation.

## Required artifacts

Use `research/runs/TEMPLATE.md` for a record under `research/runs/rNNNN.md`. Provide the input commit, settings, actual work accounting, substantive target, mathematical artifact paths, claim/assumption changes, tests performed, relevant literature additions, successful and unsuccessful approaches worth preserving, and one next action.

Include the integrated target and link advanced, the precise conditional implication or remaining proof obligation, the agreement-space repair assessment, the actual and hypothetical control comparisons, and the basis for calling the conditions simple, robust or specially constructed. Record these in the existing notes/ledgers and handoff; avoid creating administrative artifacts that displace mathematics.

Provide a reader-facing report under `research/reports/` and link it prominently from the run record and relevant model. Lead with the main headlines and conclusions, then explain why they hold with concrete examples and parameter boundaries. State informative positive conditionals: which values, settings and incentives favor combat, and which favor compromise. Prefer “under these conditions, this outcome follows” to a headline that only says one feature fails to imply another. Tie findings to the charter questions, including what utility modification adds and what drives freezing and prevalence. Explain the preference classes and game environments actually covered, how simple or specially constructed they are, and what broader conclusions remain unsupported. Keep bargain existence, adoption, selection, stability and population prevalence distinct. Preserve each achieved positive result at its supported level, and each negative result at its actual scope; unresolved stronger questions do not erase weaker established results. Link technical proofs without requiring the reader to decode a claim catalog to understand the conclusions. Scale the report to the findings; this is an explanation of the run, not final project synthesis. Its preparation receives no research-time credit.

Maintain research notes with explicit statements and proofs rather than only narrative summaries. Register new claims and assumption dependencies. Small scripts belong with tests or experiments and must document how to run them. Distinguish `PROVED-IN-MODEL` from independent verification, numerical evidence, or a conjecture.

Record the [end-of-task aim-preservation review](AIM_BALANCE.md#4-end-of-task-review) in the run template's dedicated section. Inspect the whole changed work and surrounding active instructions, compare the original aim with the question actually answered, identify missing counterpart directions and asymmetric standards, and review the headlines and next recommendation. Record actual constructive and limiting work, specific corrections, and remaining obligations. This review is also required for reporting-only tasks and partial handoffs; it does not require creating another research run or administrative document.

End-state labels are `COMPLETE`, `PARTIAL`, `BLOCKED`, or `COMPLETE-WITH-EXPLICIT-OVERRIDE`. Completion requires the applicable floor and allocation, truthful accounting, substantive research artifacts, the readable explanation, and the recorded aim-preservation review with identified framing defects corrected. Meeting the time floor alone does not complete a recurrence. Do not guarantee a discovery quota or mislabel unsuccessful mathematics as success.

## Selection and stopping

Prioritize mathematical work that explains when negotiated preference change advances current goals and what pushes actual choices toward cooperation or combat. Connect physical opportunities, agreement design, adoption, implementation and continuation within a defensible class; assess realistic alternatives and chosen safeguards. Return to underexamined links and environments while building this explanation, rather than optimizing indefinitely around one favorable example or accumulating disconnected cases.

At the end of each invocation, evaluate the synthesis gate in `TODO.md`. Recommend another recurrence that advances a specific missing link, or recommend synthesis only with evidence that the gate is met. Require an integrated class result or an obstruction tested against serious repairs, alongside the broader coverage obligations. A local example under each heading does not establish that explanation. Do not automatically launch the next run. If repeated runs only rediscover the same boundary, change the question; a bounded synthesis with unmet central obligations requires owner direction. Do not manufacture novelty or prolong the project for its own sake.
