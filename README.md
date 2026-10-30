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

- [TODO](TODO.md): preparation, initial literature review, **one main repeatable research task**, then synthesis and publication.
- [AGENTS](AGENTS.md): instructions for ChatGPT, Codex, and other contributors.
- [Research charter](research/CHARTER.md): questions, scope, and contribution standards.
- [Recurrence protocol](research/RECURRENCE.md): the canonical `CG-R001` task; default **four-hour active-research floor**, with **at least 75% theory**, both overridable per invocation.

The remaining research files are added as the scaffold develops: a model contract, assumption register, literature map, claim ledger, mathematical notes, and run records. Research is not an automatically scheduled service; each recurrence is explicitly invoked and leaves a handoff.

## Status

Initialized on 2026-10-30. The initial commits establish the research workflow and seed elementary benchmarks; they do **not** constitute a completed four-hour recurrence or a completed literature review. `CG-01` and `CG-02` are the next preparation tasks. Most substantive work belongs inside `CG-R001`, not an expanding sequence of administrative milestones.

The existing [MIT license](LICENSE) is retained. References to third-party works do not relicense those works.
