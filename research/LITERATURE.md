# Initial literature map

Screened on 2026-10-30. **CG-02 remains TODO.** These are verified leads with deliberately limited reading-status labels, not a completed review or an assertion that the project is novel. Use primary sources; inspect the actual theorem and its assumptions before relying on it.

## Motivation

The owner supplied [The Corrigibility Folk Theorem](https://thothhermes.substack.com/p/the-corrigibility-folk-theorem). Direct retrieval was unavailable during this initialization, so the charter uses the owner's explicit research brief rather than claiming a fresh textual audit of the essay. Obtain its text during preparation if needed; do not invent quotations or passage-level claims.

## Closest technical leads

| ID | Source | Relevance and reading status |
| --- | --- | --- |
| L01 | James D. Fearon (1995), *Rationalist explanations for war*, International Organization 49(3), 379–414. [Publisher/DOI](https://doi.org/10.1017/S0020818300033324) | Bargaining ranges, private information, and commitment failures. Publisher metadata/abstract checked; full theorem/argument audit pending. The seed bargain-existence calculation is a standard benchmark, not a novelty claim. |
| L02 | Tom Everitt, Daniel Filan, Mayank Daswani, Marcus Hutter (2016), *Self-Modification of Policy and Utility Function in Rational Agents*. [arXiv:1605.03142v1](https://arxiv.org/abs/1605.03142v1) | Pre-change evaluation and modeled consequences of self-modification. Metadata/abstract checked; inspect precise agent definitions and scope before importing results. |
| L03 | James D. Miller, Roman Yampolskiy, Olle Häggström (2020), *An AGI Modifying Its Utility Function in Violation of the Orthogonality Thesis*. [arXiv:2003.00812v1](https://arxiv.org/abs/2003.00812v1) | Strategic incentives to change observable preferences. Metadata/abstract checked. Evaluate formal support independently; do not adopt the title's orthogonality conclusion as an established result. |
| L04 | Caspar Oesterheld, Vincent Conitzer (2022), *Safe Pareto improvements for delegated game playing*, Autonomous Agents and Multi-Agent Systems 36, article 46. [Full text/DOI](https://doi.org/10.1007/s10458-022-09574-6) | Abstract, introduction, and selected definitions inspected; full proof audit pending. Particularly close: modified delegate utilities and conditional commitments. Check sections 3.2 and 6. Some constructions restrict available actions; compare carefully with this project's persistent-combat requirement. |
| L05 | Anthony DiGiovanni, Jesse Clifton, Nicolas Macé (2025 version), *Safe Pareto Improvements for Expected Utility Maximizers in Program Games*. [arXiv:2403.05103v5](https://arxiv.org/abs/2403.05103v5) | Renegotiation programs and incentives to use them. Abstract/version checked; arXiv records AAMAS-25 acceptance. Audit beliefs, code observability, guarantees, and negative bounds against our protocol. |
| L06 | Caspar Oesterheld, Vincent Conitzer (2025), *Choosing What Game to Play without Selecting Equilibria: Inferring Safe (Pareto) Improvements in Binary Constraint Structures*. [arXiv:2511.21262](https://arxiv.org/abs/2511.21262) | Outcome-correspondence reasoning without selecting one equilibrium. Metadata/abstract checked; proof audit pending. Relevant to separating efficient possibilities from guarantees. |
| L07 | Adrian Bejan (2002), *Fundamentals of exergy analysis, entropy generation minimization, and the generation of flow architecture*. [DOI](https://doi.org/10.1002/er.804), [author-institution record](https://scholars.duke.edu/publication/682006) | Physical accounting for irreversibility and available work. Author-institution abstract checked; full physical derivation pending. Do not use entropy as a universal proxy for arbitrary agents' utility or treat energy as destroyed. |
| L08 | Ingela Alger, Jörgen W. Weibull (2013), *Homo Moralis—Preference Evolution Under Incomplete Information and Assortative Matching*, Econometrica 81(6), 2269–2302. [Publisher/DOI](https://doi.org/10.3982/ECTA10637) | Indirect evolution, information, and matching assumptions. Publisher identity/metadata checked; theorem audit pending. Determine which preference-stability concepts transfer to self-modifying artificial agents. |
| L09 | Ingela Alger, Jörgen W. Weibull, Laurent Lehmann (2020), *Evolution of preferences in structured populations: Genes, guns, and culture*, Journal of Economic Theory 185, 104951. [Publisher/DOI](https://doi.org/10.1016/j.jet.2019.104951) | Structured populations, conflict, and fitness-based preference evolution. Publisher search-index metadata/abstract screened; direct full-page access failed. Obtain an author version and verify its assumptions before relying on results. |

## CG-02 deliverable

For each relied-on source record: version, exact section/theorem/page, primitives, information assumptions, commitment technology, physical resource treatment, utility evaluation semantics, solution/stability concept, and what it does **not** prove. Add a source-to-claim crosswalk and compare the proposed project with the nearest established result.

Fill gaps in bargaining with endogenous or changing power, contest-success functions, repeated/coalitional stability, physical reconstruction/separation costs, and preference commitments that benefit stubborn types. Search forward citations and recent primary work; the list above is not exhaustive or guaranteed to contain the latest relevant result.

Keep external bibliographic claims separate from new derivations. A paper's abstract is a discovery aid, not proof that our stronger claim follows. Log failed access and unresolved attribution rather than citing an unread source as verified.
