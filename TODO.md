# Research TODO

This queue is executable by ChatGPT, Codex, or another research agent. There is **one main recurring research task**, `CG-R001`. Its internal research fronts are not a long sequence of mandatory mini-projects. Most project effort belongs there.

Status: scaffold initialized 2026-10-30. No full recurrence has yet been completed.

## CG-00 — Initialize the project

**Status: DONE for workflow initialization.** Preserve the existing license; establish the charter, agent instructions, task queue, and recurrence protocol. Seed model/literature/claim files and elementary checks are initialization aids, not completed substantive research milestones.

## CG-01 — Establish the minimal formal contract

**Status: TODO; draft supplied in `research/MODEL.md`.**

Read the owner's research brief as reflected in the charter. Specify a minimal two-agent dynamic game: histories, physical states, power, legal actions, timing, beliefs, stochastic transitions, utility evaluation, update semantics, and solution concept. Give combat, ordinary compromise, and utility-modifying compromise explicit transition rules. Specify what the loser, survivors, and successor agents value.

Exit when one tractable model is fully defined, units and accounting are coherent, always-available combat and the old/new-utility distinction are checked, and assumptions are indexed. Select one minimal physical mechanism to derive first. Do not delay theory for a general simulator, exhaustive ontology, or polished paper. Leave substantive theorems and successive model extensions inside `CG-R001`.

## CG-02 — Initial literature and comparison map

**Status: TODO; screened leads supplied in `research/LITERATURE.md`.**

Review primary work on bargaining with costly conflict and commitment failures; strategic self-modification; delegation and program games; safe Pareto improvements; useful work and irreversible physical processes; and indirect evolution of preferences. Include repeated bargaining, changing power, coalitions, and preference observability as needed.

Exit with a compact source-to-question table, checked theorem assumptions for the closest results, an explicit overlap/possible-contribution assessment, and the first tractable research targets. Label unread or inaccessible sources. This is an initial map, not an exhaustive review. Continue targeted literature work during the recurrence.

## CG-R001 — Main recurrence: physical conflict, compromise, and preference evolution

**Status: OPEN / REPEATABLE.** Start after CG-01 and CG-02, or an explicit owner override. Execute the detailed [recurrence protocol](research/RECURRENCE.md).

**Defaults per invocation:** minimum four hours of active research; at least 75% of counted research time on substantial mathematical work. Both are overridable. Record the actual override, duration, time split, and completion status. Never silently shorten the floor.

An invocation should advance the most important unresolved mathematical question, not merely repeat a parameter sweep. These are connected research fronts inside the same task:

- **Physical advantage and its limits.** Derive how dispersion, thermal degradation, infrastructure damage, restoration work, and delay change achievable outcomes. Compare state-dependent mechanisms with a scalar conflict-cost surrogate. Test when the extra physical detail changes a prediction rather than just renames a parameter. Match nonphysical consequences where possible. Seek sufficient conditions, necessity boundaries, and counterexamples.
- **Bargaining under persistent conflict options.** Establish when a mutually acceptable peace exists, can be selected, and remains incentive-compatible against attack, rollback, renegotiation, and power shifts. Do not assume away preemption. Extend from pairs to coalitions when analytically useful.
- **What utility modification adds.** Construct actual successor objectives and implementation protocols. Compare them with unchanged utilities plus flexible policies, contracts, delegation, and conditional commitments. Isolate expressivity, verification, atomicity, and durability rather than crediting them all to preference change.
- **Preferences that restore combat's appeal.** Characterize finite and lexicographic freezing preferences, direct preferences for conflict or destruction, status/relative power, incompatible thresholds, nontransferable goals, and process or identity preferences. Identify which merely rule out one update mechanism and which rule out the full peaceful alternative set.
- **Long-run freezing.** Analyze voluntary relaxation under the incumbent utility, including discounted opportunity costs and strategic commitment benefits. Separately derive evolutionary or competitive invasion conditions, coexistence, and persistence using an explicit fitness map. Include mutation/innovation, observability, assortment, and exploitation; do not build extinction of freezing into the update rule.
- **Assumption dependence.** Pair positive results with minimal failures; relax assumptions individually and jointly. Distinguish generic claims, distributions over types, worst cases, and illustrative examples. Maintain the assumption register and claim ledger.

A recurrence can primarily pursue one front, but the accumulated portfolio must answer all the owner's central questions. Use the substantive stopping gate below, not arbitrary numbers of runs or candidate families.

### Gate from recurrence to synthesis

Recommend CG-03 when the portfolio contains: (a) an explicit physical-model result, not only an assumed cheaper peace; (b) clear existence/adoption/stability boundaries with combat retained; (c) a matched assessment of utility modification against ordinary commitments; (d) characterized pro-combat preferences including freezing; (e) distinct long-run voluntary and population analyses, including a persistence counterexample or theorem boundary; and (f) an assumption-dependence map and honest literature/contribution assessment.

Each item needs a proof, counterexample, or precisely bounded unresolved conclusion with evidence explaining the limit. Do not require a universal positive theorem, convergence of all agents, or a solution of every open question. Do not promote an elementary bargain-existence lemma as the whole project. If progress stalls, diagnose and redirect within CG-R001; do not fill the time with paperwork. Obtain owner direction for a major scope change or proceeding to synthesis with unmet central obligations.

## CG-03 — Synthesize and audit the research

**Status: BLOCKED on the synthesis gate or explicit owner instruction.**

Select a coherent contribution, freeze its model version, audit every main proof and counterexample, verify citations and comparisons, reproduce supporting calculations, and map every headline to a claim ID. Seek an independent agent review when available and label its scope. Separate results, limitations, and remaining conjectures. Additional mathematical repairs return to CG-R001 rather than spawning a second research loop.

## CG-04 — Write the paper and presentation

**Status: BLOCKED on CG-03.**

Produce a readable GitHub Markdown research paper and a matching LaTeX/arXiv-style PDF with rendered equations, proof appendices, references, and reproducible source. Include an expository summary suitable for the originating essay's audience and a compact presentation outline; create slides only when requested. State which conclusions are conditional, what thermodynamics contributes, and whether modification itself is essential.

Check notation, figures, links, citations, proof dependencies, rendering, and claim strength. Report AI contributions accurately. Do not submit to arXiv or another external venue without explicit authorization.

## Next-agent handoff

The next substantive task is **CG-01**, then **CG-02**, then an explicitly invoked **CG-R001** run. A useful instruction is: `Complete CG-01 and CG-02, then run CG-R001 with its default four-hour active-research floor and 75% minimum theory allocation.` Preparation does not consume that recurrence floor. If runtime prevents completion, checkpoint the unfinished work honestly.
