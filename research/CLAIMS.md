# Claim ledger

All substantive claims belong here. Status describes mathematical support; review status is separate. Initial seed proofs are elementary, author/agent-checked derivations, not independent or machine-checked verification and not claims of novelty.

| ID | Statement / question | Status | Assumptions and evidence |
| --- | --- | --- | --- |
| B01 | In the linear two-agent allocation benchmark, strictly mutually preferred peace exists iff P > W. | PROVED-IN-MODEL; seed, self-checked | A08, A10, A14, A16, zero relevant A17 penalties and A18 bonuses. [Proof](notes/000-baselines.md). P and W are given net resource amounts; no physical or equilibrium theorem. Standard bargaining-range benchmark related to L01. |
| B02 | A max-min successor objective implements a specified interior resource split. | PROVED-IN-MODEL; seed, self-checked | Expressive utility class, feasible resource simplex, optimization, atomic installation assumed. [Proof](notes/000-baselines.md). No verification, adoption, or successor-stability guarantee. |
| B03 | In the update-only benchmark with finite freezing penalties and combat bonuses, strict mutual preference requires and is implied by P-W exceeding their sum in the chosen resource-utility normalization. | PROVED-IN-MODEL; seed, self-checked | Linear common resource units; both updates incur specified penalties; combat incurs none. [Proof](notes/000-baselines.md). Does not imply all peaceful mechanisms fail. |
| B04 | A fixed positive per-period gain under discounting may or may not outweigh a finite one-time freezing penalty, even over arbitrarily long horizons. | PROVED-IN-MODEL; seed, self-checked | A15 convergent discounting, exogenous constant gain and one-time penalty. [Proof](notes/000-baselines.md). No endogenous repeated-game or evolutionary result. |
| C01 | In E1.0, every feasible Work transition and either combat outcome preserve O+D+Z+y_A+y_B=12 and nonnegative feedstock/work reserves. | PROVED-IN-MODEL; local accounting only | A06, A22–A23, E1.0 sections 1–3. Substitution proof and failure boundaries below; [exact checks](../tests/test_e1_contract.py). Review: agent self-checked, not independently or machine verified. Nearest background L11; conservation bookkeeping is not novel. |
| Q01 | Which explicit physical mechanisms yield a larger implementable peaceful opportunity set? | OPEN | First target: dispersion recovery with finite work/deadline, using a named C1 instance. [Contract](MODEL.md), [E1 example](models/E1.md), L01/L07/L11 comparison. Do not assume P > W as the answer. |
| Q02 | When is peace adopted and dynamically stable with attacks still available? | OPEN | Formal bargaining protocol, beliefs, off-path deviations, changing power, rollback. |
| Q03 | What advantages of terminal-utility modification cannot be reproduced by matched ordinary commitments? | OPEN | A09–A13; equivalence is an admissible substantive answer. |
| Q04 | Which initial preferences make combat attractive against the full peaceful alternative set? | OPEN | Finite/hard freezing, process goals, relative outcomes, survival, control, and indivisibility. B03 alone is insufficient. |
| Q05 | When does the incumbent utility favor relaxing a freeze, including commitment benefits and future risks? | OPEN | Endogenous repeated interaction; separate from B04's exogenous-gain calculation. |
| Q06 | When do flexible types invade, coexist with, or lose to frozen types? | OPEN | A19–A20, payoff-to-fitness map, mutation/assortment/observation, and derived selection dynamics. |

## Additions and revisions

CG-01/CG-02 completion adds a flexible contract and a reference specification, not a solved dynamic game. B01–B04 retain their original static scope; Q01–Q06 remain open. The [source map](LITERATURE.md) audits selected external assumptions and distinguishes their results from repository claims.

**C01 proof and boundary.** For Work, summing the five new material coordinates cancels +x_D against -x_D, +x_Z against -x_Z, and -v against v_A+v_B. Feasibility gives D-x_D>=0, Z-x_Z>=0, O+x_D+x_Z-v>=0 and B-(2x_D+4x_Z+v)>=0. For combat, d+z<=O for integer O>=0, so moving those quantities from O to D/Z preserves mass and nonnegativity; B-min(2,B)>=0 and both R reserves become zero. Protocol costs require sufficient B and leave material alone until Execute, which is a Work action. These are stipulated closed-feedstock transitions, not thermodynamic or equilibrium claims. Unmodeled imports, vulnerable deliveries, harvesting extra work, or altered recovery yields require new balances. The code checks finite examples/local boundaries and is not a formal proof checker.

A new entry must give an exact quantified statement, model/version, assumption IDs, proof or reproducibility path, nearest prior result, review status, and failure boundary. Numerical evidence is `NUMERICAL`, not a proof. A proof sketch is labeled as such. Preserve superseded or refuted claims with correction links rather than erasing the history.

Do not promote Q01–Q06 to proved because a seed example works. At synthesis, attach a coverage map showing which owner's questions are answered, bounded, or still open, and whether each contribution is a theorem, counterexample, useful application, representation, comparison, or synthesis.
