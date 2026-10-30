# CG-01 / CG-02 preparation handoff — 2026-10-30

**Status: both preparation tasks complete. No CG-R001 invocation.** Input commit: 4dc58b2103af430258a8a00abee1f57db5e52521. Work is on research branch `codex/cg-01-cg-02-preparation`; publication is through its pull request, not direct commits to main.

This is bounded preparation, not a four-hour research run. Active duration and theory percentage were not measured as recurrence accounting; no duration or recurrence credit is claimed. The observed validation checkpoint was 2026-10-30 23:55:49 UTC. No background or unattended work is claimed.

## Deliverables and completion evidence

| Task / exit condition | Artifact and evidence |
| --- | --- |
| CG-01: flexible formal contract | [C1](MODEL.md) declares histories, physics, agency, actions, kernels, observations/beliefs, utilities, implementation, and solution concepts. Instance assumptions remain replaceable. |
| CG-01: one fully defined tractable game | [E1.0](models/E1.md) specifies finite primitives, legal actions, all protocol phases, stochastic combat, resource accounting, successor/loser values, and current-self equilibrium. This is a witness, not a permanent baseline. |
| CG-01: invariants and assumptions | [Assumption register](ASSUMPTIONS.md) distinguishes C1 invariants from E1 choices and stronger delegation technology. [C01](CLAIMS.md) gives the local mass/nonnegativity proof and limits. |
| CG-01: first mechanism | Dispersion recovery work/time under a finite budget/deadline; derive the frontier before embedding it in a game. Continuous and integer formulations remain alternatives. |
| CG-02: compact primary-source map | [Literature map](LITERATURE.md) records twelve sources, actual versions/locators, selected audits, screened leads, access failures, and source-to-question mapping. |
| CG-02: comparison/contribution assessment | Separate overlap with bargaining, self-modification, program commitments, and preference evolution from possible physical/implementation contributions. No novelty claim. |
| CG-02: first targets and gaps | Q01 first; Q02/Q03 for adoption/stability and matched commitments; later Q05/Q06 with explicit repeated opportunities/fitness. Coalitions and several follow-up theorem audits remain scoped gaps. |

The owner's refinement was incorporated: C1 must accommodate variations during the recurrence. E1's numbers, utility menu, horizon, ownership, public information, and protocol are explicitly local. No new charter restriction or permanent recurrence default was introduced.

## Validation and limits

- `python -m unittest discover -s tests -v`: **18 checks passed**, consisting of 11 existing seed checks and 7 E1 ledger/preference checks. They do not solve equilibria, calibrate physics, or prove population claims.
- Inspected original-paper PDF passages and selected rendered pages to check equations/locators. The versioned L05 PDF uses different result numbering from the retrieved HTML; the record cites the PDF.
- Repository diff passed whitespace checks; all local Markdown links resolved; the license is unchanged.
- Audits are by the contributing AI agent only. No independent review, machine proof checking, or human endorsement is claimed.
- Existing seed artifacts and MIT license are preserved. Source PDFs/extractions were used as local temporary reading aids and are not redistributed in the repository.
- B01–B04 retain their original scope. Q01–Q06 remain open. C01 is elementary accounting, not a peace or thermodynamics result.

## Next action

Await an explicit CG-R001 invocation, then read [RECURRENCE.md](RECURRENCE.md). Start by deriving a dispersion-only recovery frontier in a named C1 instance and finding its binding/nonbinding regimes. Use that result to test bargaining incentives with attacks available; do not substitute a feasible split for an adoption/stability proof. Revise E1 or use a different small instance when it improves the argument.

The default four-hour active-research floor and 75% theory allocation remain intact for that later invocation. This preparation does not satisfy or reduce them.

Work was AI-assisted by OpenAI Codex. This handoff records artifacts and limits, not a claim of independent verification.
