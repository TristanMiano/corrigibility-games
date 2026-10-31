# CG-R001: main research recurrence

This is the project's single repeatable substantive research task. Each explicit invocation runs one research increment and produces a durable handoff. It is not a scheduled automation and does not authorize an endless series of unattended runs.

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

## Count research honestly

Count active derivation, construction of models and counterexamples, proof attempts, proof audit, focused scientific literature analysis, and necessary research computation. Classify work as `theory`, `literature`, or `computation`. Only mathematical work counts toward the theory fraction; merely reading a paper or writing a status report does not. A proof derivation prompted by a paper can count as theory when the artifact records the actual derivation.

Exclude repository setup, generic coding infrastructure, ordinary formatting, handoff preparation, idle waits, tool latency without simultaneous active work, and unattended compute. Count concurrent work only once toward the lead run's duration; record helper-agent effort separately rather than summing overlapping worker-hours into four elapsed research hours.

Use observed start/end timestamps and active segments when the environment permits. Record actual uncertainties instead of fabricated precision. Do not infer four hours from an instruction or output length. If a runtime limit or interruption prevents the floor or allocation from being met, publish `PARTIAL`, state the shortfall, and leave a resumption point. Do not silently override the owner's floor, pad time, promise background continuation, or mark the run complete. The owner can explicitly waive or change a requirement.

## Research loop within an invocation

1. **Choose a substantive target.** Select one central unresolved claim and the closest existing positive and negative results. Briefly record why it advances the charter. Avoid an early lock-in to a minor candidate just because it is easy to publish.
2. **Derive before scaling.** Work through explicit definitions, equations, proofs, and small exact examples. Keep physical transitions and utility semantics visible. Pursue alternative constructions when the current one fails. Spend most of the run here.
3. **Attack the claim.** Search for minimal counterexamples, missing deviations, hidden commitment assumptions, utility-rescaling problems, and mismatch between current utility and founder welfare. Remove or weaken one assumption at a time and test informative interactions.
4. **Compare mechanisms.** Where relevant, give unchanged-utility bargaining or commitment the same information, physical resources, and implementation capabilities. Classify equivalence honestly. A reduction to an existing method can settle a meaningful question.
5. **Use targeted support.** Check primary literature as needed. Use exact arithmetic, symbolic tools, or small reproducible experiments to test boundaries, not replace proofs. Avoid building a large simulator before knowing what claim it is testing.
6. **Consolidate and explain the result.** State what was proved, refuted, or left open; identify the assumption dependency and next most informative test. Update ledgers, then write a readable findings report and concise handoff outside the research clock.

These steps recur within a run as useful; they are not separate project milestones or rigid time slices. A run focused on a difficult theorem can legitimately end with a sharply localized obstruction and a reproducible counterexample rather than a positive theorem. Administrative churn alone is not a successful research increment.

## Required artifacts

Use `research/runs/TEMPLATE.md` for a record under `research/runs/rNNNN.md`. Provide the input commit, settings, actual work accounting, substantive target, mathematical artifact paths, claim/assumption changes, tests performed, relevant literature additions, unsuccessful approaches worth preserving, and one next action.

Provide a reader-facing report under `research/reports/` and link it prominently from the run record and relevant model. Lead with the main headlines and conclusions, then explain why they hold with concrete examples and parameter boundaries. State informative positive conditionals: which values, settings and incentives favor combat, and which favor compromise. Prefer “under these conditions, this outcome follows” to a headline that only says one feature fails to imply another. Tie findings to the charter questions, including what utility modification adds and what drives freezing and prevalence. Explain the preference classes and game environments actually covered, how simple or specially constructed they are, and what broader conclusions remain unsupported. Keep bargain existence, adoption, selection, stability and population prevalence distinct. Link technical proofs without requiring the reader to decode a claim catalog to understand the conclusions. Scale the report to the findings; this is an explanation of the run, not final project synthesis. Its preparation receives no research-time credit.

Maintain research notes with explicit statements and proofs rather than only narrative summaries. Register new claims and assumption dependencies. Small scripts belong with tests or experiments and must document how to run them. Distinguish `PROVED-IN-MODEL` from independent verification, numerical evidence, or a conjecture.

End-state labels are `COMPLETE`, `PARTIAL`, `BLOCKED`, or `COMPLETE-WITH-EXPLICIT-OVERRIDE`. Completion requires the applicable floor and allocation, truthful accounting, substantive research artifacts, and the readable explanation. Meeting the time floor alone does not complete a recurrence. Do not guarantee a discovery quota or mislabel unsuccessful mathematics as success.

## Selection and stopping

Prioritize mathematical work that changes the answer to the owner's question: physical reachability or reconstruction bounds; adoption and attack incentives; whether changing preferences adds anything beyond commitments; finite versus hard freezing; and separate voluntary and evolutionary long-run behavior. Return periodically to underexamined fronts rather than optimizing indefinitely around one favorable example.

At the end of each invocation, evaluate the synthesis gate in `TODO.md`. Recommend another recurrence with a specific reason, or recommend synthesis only with an explicit coverage map establishing that the gate is met. A local example under each heading does not establish breadth across preferences, environments and parameter regions. Do not automatically launch the next run. If repeated runs only rediscover the same boundary, change the question; a bounded synthesis with unmet central obligations requires owner direction. Do not manufacture novelty or prolong the project for its own sake.
