# Instructions for research agents

Applies to ChatGPT, Codex, and other contributors throughout this repository. Explicit owner instructions override project defaults. Read `README.md`, `TODO.md`, `research/CHARTER.md`, and the latest run handoff before selecting work. Read `research/RECURRENCE.md` before invoking `CG-R001`.

## Work allocation

This is a theory-first research project, not primarily a simulator-building project. Keep preparation bounded and put most substantive research in the single repeatable task `CG-R001`. Its defaults are a **four-hour floor of active research** and **at least 75% of counted research time on mathematical definitions, derivations, proofs, counterexamples, and proof checking**. The owner may override either setting for one invocation; overrides do not silently become permanent defaults.

Do not invent elapsed work, count idle waits, pad a session, or call a runtime-limited partial run complete. Use actual observed work intervals where available, identify estimates honestly, and preserve incomplete runs for resumption. A four-hour instruction is not permission to claim unattended or background work. Repository housekeeping and handoff writing are not mathematical research credit. See the recurrence protocol for accounting.

## Modeling invariants

1. Keep combat physically available to capable agents at relevant nonterminal histories. Explain terminal states, incapacity, merger, and loss of agency explicitly. Do not prove peace by deleting the action or imposing infinite combat cost. An externally imposed last-resort-only rule is a separately labeled comparison, not the baseline.
2. Represent physical mechanisms: material dispersion and transformation, infrastructure loss, available work, recovery effort and delay. Keep useful work distinct from conserved energy and from utility. Account for compromise's communication, verification, computation, and update costs too. Do not identify Shannon entropy with thermodynamic entropy without a physical model.
3. An agent deciding whether to change its utility evaluates that change using its **current, pre-change utility**. At later decisions the successor uses its then-current utility. Report original-agent welfare separately. Do not score the initial decision only by the newly installed utility, or silently force all descendants to maximize the founder's utility.
4. Utility self-knowledge is not public observability, semantic verification, common knowledge, or credible commitment. Knowing how to self-modify does not mean modifying atomically, safely, or irreversibly. Perfect outcome modeling means knowing the specified stochastic dynamics, not knowing random realizations.
5. Include peaceful options without terminal-utility modification. Compare fixed-utility flexible policies, enforceable commitments or delegation, voluntary utility modification, and combat under matched physical and informational assumptions. Label controls requiring stronger implementation technology. Never infer that freezing entails combat just because ordinary trade was omitted.
6. Define what counts as a utility change. Distinguish code identity, preference ordering over lotteries, policy behavior, beliefs, and representations. Positive affine rescaling alone is not a change of expected-utility preferences.
7. Distinguish a beneficial bargain's existence, incentives to propose and adopt it, equilibrium selection, ongoing stability, coalition stability, and population prevalence. A result at one level is not a result at the others.
8. Distinguish an agent's utility from its reproductive or competitive fitness. Selection can eliminate a type without making any member want to change. Conversely, freezing may confer commitment or anti-exploitation advantages. Treat both directions seriously.

## Evidence and contributions

Record claims in `research/CLAIMS.md` with precise statements, assumptions, proof locations, status, counterexamples, and nearest literature. Use statuses such as `PROVED-IN-MODEL`, `PROOF-SKETCH`, `CONJECTURE`, `NUMERICAL`, `COUNTEREXAMPLE`, `OPEN`, and `REFUTED`. State review status separately; a self-checked proof is not independently verified or machine checked.

Check primary sources before attributing theorems. Record actual versions, sections, and access limits. Abstract-level screening is not a theorem audit. Do not fabricate citations or novelty. Useful applications, representations, comparative classifications, and syntheses count as contributions even when the machinery is conventional. A fixed-utility control matching a modification mechanism is an informative result, not something to hide.

Try to break promising claims before broadening them. Prefer small exact models and analytical boundaries; use symbolic computation and experiments to assist rather than replace derivation. Preserve informative failures and counterexamples. Never use favorable parameter samples as a distribution-free statement about agents in general.

## Repository practice

Preserve existing work and the license. Use small, coherent commits. Check the current branch head before writing; do not force-push over concurrent changes. Unless the owner requests direct commits, work on a research branch and present a pull request. Initial scaffold commits are directly authorized by the owner.

Keep scratch work out of claims presented as results. Every completed recurrence leaves a concise public run record, substantive mathematical artifacts, updated assumption/claim ledgers, reproducible checks where useful, and one clear next step. It also requires a readable findings report: lead with headlines and conclusions, then explain mechanisms, examples and parameter boundaries in terms of the project's central questions. State which values, settings and incentives favor combat or compromise through positive conditional claims; avoid headlines that merely say “X does not imply Y.” Distinguish results about particular preferences and environments from claims about naturalness or prevalence. A technical artifact catalog alone does not complete the reporting obligation; report writing is outside the research clock. Redact private conversation details, credentials, and unrelated personal context. Record AI assistance accurately; do not invent human review or authorship endorsements.
