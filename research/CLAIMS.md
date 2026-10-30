# Claim ledger

All substantive claims belong here. Status describes mathematical support; review status is separate. Initial seed proofs are elementary, author/agent-checked derivations, not independent or machine-checked verification and not claims of novelty.

| ID | Statement / question | Status | Assumptions and evidence |
| --- | --- | --- | --- |
| B01 | In the linear two-agent allocation benchmark, strictly mutually preferred peace exists iff P > W. | PROVED-IN-MODEL; seed, self-checked | A08, A10, A14, A16, zero relevant A17 penalties and A18 bonuses. [Proof](notes/000-baselines.md). P and W are given net resource amounts; no physical or equilibrium theorem. Standard bargaining-range benchmark related to L01. |
| B02 | A max-min successor objective implements a specified interior resource split. | PROVED-IN-MODEL; seed, self-checked | Expressive utility class, feasible resource simplex, optimization, atomic installation assumed. [Proof](notes/000-baselines.md). No verification, adoption, or successor-stability guarantee. |
| B03 | In the update-only benchmark with finite freezing penalties and combat bonuses, strict mutual preference requires and is implied by P-W exceeding their sum in the chosen resource-utility normalization. | PROVED-IN-MODEL; seed, self-checked | Linear common resource units; both updates incur specified penalties; combat incurs none. [Proof](notes/000-baselines.md). Does not imply all peaceful mechanisms fail. |
| B04 | A fixed positive per-period gain under discounting may or may not outweigh a finite one-time freezing penalty, even over arbitrarily long horizons. | PROVED-IN-MODEL; seed, self-checked | A15 convergent discounting, exogenous constant gain and one-time penalty. [Proof](notes/000-baselines.md). No endogenous repeated-game or evolutionary result. |
| Q01 | Which explicit physical mechanisms yield a larger implementable peaceful opportunity set? | OPEN | Derive from MODEL.md recovery frontier / kernels; do not assume P > W as the answer. |
| Q02 | When is peace adopted and dynamically stable with attacks still available? | OPEN | Formal bargaining protocol, beliefs, off-path deviations, changing power, rollback. |
| Q03 | What advantages of terminal-utility modification cannot be reproduced by matched ordinary commitments? | OPEN | A09–A13; equivalence is an admissible substantive answer. |
| Q04 | Which initial preferences make combat attractive against the full peaceful alternative set? | OPEN | Finite/hard freezing, process goals, relative outcomes, survival, control, and indivisibility. B03 alone is insufficient. |
| Q05 | When does the incumbent utility favor relaxing a freeze, including commitment benefits and future risks? | OPEN | Endogenous repeated interaction; separate from B04's exogenous-gain calculation. |
| Q06 | When do flexible types invade, coexist with, or lose to frozen types? | OPEN | A19–A20, payoff-to-fitness map, mutation/assortment/observation, and derived selection dynamics. |

## Additions and revisions

A new entry must give an exact quantified statement, model/version, assumption IDs, proof or reproducibility path, nearest prior result, review status, and failure boundary. Numerical evidence is `NUMERICAL`, not a proof. A proof sketch is labeled as such. Preserve superseded or refuted claims with correction links rather than erasing the history.

Do not promote Q01–Q06 to proved because a seed example works. At synthesis, attach a coverage map showing which owner's questions are answered, bounded, or still open, and whether each contribution is a theorem, counterexample, useful application, representation, comparison, or synthesis.
