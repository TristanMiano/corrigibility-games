# Corrigibility Games

Game-theoretic research on voluntary utility modification, physically costly conflict, and the stability and evolution of compromise.

**Central question:** When do agents prefer and sustain peaceful compromises, including consensual changes to their utilities, rather than combat? Which assumptions make that conclusion possible, and which initial preferences reverse it?

The motivating essay is Tristan Miano's [The Corrigibility Folk Theorem](https://thothhermes.substack.com/p/the-corrigibility-folk-theorem). The essay motivates a research question; its title is not a theorem claim established by this repository. Here, corrigibility means a scoped willingness to accept utility modification, not automatically human alignment, obedience, or the usual full collection of AI corrigibility properties.

## Research commitments

Combat and compromise must differ in their **physical transition models**, not merely in an arbitrary payoff penalty. Conflict can disperse materials, damage organized infrastructure, dissipate available work, and create reconstruction and cooling delays. Negotiation, verification, and consensual updating also consume resources. We study when those differences change feasible outcomes and incentives.

Combat remains a physically available action for capable agents at nonterminal decision points, including after agreements. It is the ultimate disagreement threat, not an action prohibited until a designer declares every peaceful option exhausted. Whether agents actually reserve it for last resort is an outcome to explain.

Utilities are initially transparent to their owners; agents understand permitted self-modifications and can evaluate stochastic future trajectories in the specified model. Public observability, common knowledge, atomic updates, and irreversible commitments are **separate assumptions**, not consequences of those capabilities.

We distinguish terminal-goal preservation, utility-freezing preferences, policy rigidity, and commitment devices. We separately investigate voluntary relaxation of freezing and population selection against freezing; one does not imply the other.

## Start here

- **[First-round findings: when agents favor combat or compromise](research/reports/r0001-findings.md)**: readable conclusions, worked examples, a parameter guide, and what remains unanswered about natural agents and game environments.
- [TODO](TODO.md): preparation, initial literature review, **one main repeatable research task**, then synthesis and publication.
- [AGENTS](AGENTS.md): instructions for ChatGPT, Codex, and other contributors.
- [Research charter](research/CHARTER.md) and [recurrence protocol](research/RECURRENCE.md): the canonical `CG-R001` task; default **four-hour active-research floor**, with **at least 75% theory**, both overridable per invocation.
- [Flexible model contract C1](research/MODEL.md), [reference instance E1](research/models/E1.md), and [assumption register](research/ASSUMPTIONS.md): physical transitions, bargaining, utility semantics, freezing, and selection. E1's choices are replaceable examples, not recurrence defaults.
- [Essay model E2](research/models/E2.md) and [first-recurrence mathematics](research/notes/010-essay-formalization.md): strength, recovery, adoption, deception, freezing and installation reliability; local assumptions remain revisable.
- [Literature map](research/LITERATURE.md), [claim ledger](research/CLAIMS.md), and [seed derivations](research/notes/000-baselines.md): sources, proof obligations, and elementary benchmarks.
- [Completed first recurrence: r0001](research/runs/r0001.md), [preparation handoff](research/PREPARATION.md), [run index](research/runs/README.md), and [initialization record](research/INITIALIZATION.md): actual work and handoffs.

Research is not an automatically scheduled service; each recurrence is explicitly invoked and leaves a handoff. Most substantive work belongs inside `CG-R001`, not an expanding sequence of administrative milestones.

## Status and checks

Initialized on 2026-10-30. **CG-01, CG-02 and the first recurrence r0001 are complete, with its reader-facing report added in the 2026-10-31 follow-up.** The research was merged in [PR #2](https://github.com/TristanMiano/corrigibility-games/pull/2). R0001's conservative active-research estimate remains **4h 00m 09s, 89.39% theory**; reporting adds no research-time credit. E2.1 provides an essay-faithful family of conditional models, with contributing-agent self-checks. C1 remains flexible.

For agents valuing their own project output, a credible division above each agent's expected combat return makes compromise attractive. Revocable sole control instead produces war in the solved final-decision game, and private-strength bargaining produces risky offers when the proposer gains more from demanding a larger share than it loses through combat. Direct combat rewards raise the compensation a peaceful bargain must provide; moderate goal-preservation preferences can protect a staged compromise against later concessions. The [findings report](research/reports/r0001-findings.md) explains the conditions and parameter boundaries. Establishing their breadth across preferences and environments remains the research priority. **CG-R001 remains the main research task; CG-03 is BLOCKED and the synthesis gate is not met.** Q01–Q06 remain open. No next recurrence is currently running.

Run the standard-library exact-arithmetic checks from the repository root:

```sh
python -m unittest discover -s tests -v
```

The **109 checks** cover seed calculations, E1.1's physical ledgers and E2's mathematical examples, including exact LP/game checks and explicitly labeled numerical support. Tests do not replace proofs, calibrate physics, solve every model-family game or independently verify the population results.

The existing [MIT license](LICENSE) is retained. References to third-party works do not relicense those works.
