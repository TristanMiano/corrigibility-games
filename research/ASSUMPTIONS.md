# Assumption register

Updated for CG-01/CG-02, 2026-10-30. These are indexed distinctions, not an empirical ranking of importance. [Contract C1](MODEL.md) leaves instance assumptions open; [E1](models/E1.md) makes local example choices only. Each substantive claim must name the assumptions it actually uses and link to a removal test, counterexample, or open proof obligation. Separate structural necessity from convenience in the current proof.

| ID | Assumption / setting | Role and removal test |
| --- | --- | --- |
| A01 | Agents know their own utilities | Owner's starting idealization; not knowledge of others. Later weaken to partial self-knowledge if informative. |
| A02 | Agents understand allowed self-modifications | Does not supply arbitrary objective expressivity, trusted execution, atomicity, or irreversibility. |
| A03 | Correct model of stochastic futures and evaluable expectations | Requires a defined game and well-posed horizon; compare approximation or uncertainty later. |
| A04 | Agent-dominated environment | Physical work, spatial structure, and resource constraints remain. Track any additional environmental hazards. |
| A05 | Combat remains physically available | Core main-model requirement. Do not remove attacks after agreement; label incapacity/terminal exceptions and disarmament controls. |
| A06 | Distinct physical transition mechanisms | Core main-model requirement. A scalar cost is a benchmark reduction, not the final physical analysis. |
| A07 | Resource/work monotonicity of goals | Potential heavy-lifting condition, not universal. Test destructive, relative, threshold, and process preferences. |
| A08 | Rich peaceful feasible set | Divisibility, transfers, lotteries, and enforceable allocations are separate sub-assumptions. Remove each without quietly retaining its substitute. |
| A09 | Public observability and common knowledge | Separate from A01. Vary private information, truthful reporting, semantic verification, and observed implementation. |
| A10 | Common beliefs about combat and dynamics | Separate from the ability to calculate expectations. Test disagreement and incompatible posteriors when relaxing correct common models. |
| A11 | Verifiable, durable implementation | Distinguish observed promises from real commitments; test rollback and successor incentives. |
| A12 | Atomic reciprocal updates | Compare sequential installation, hostage exposure, interruption, and attack during transition. |
| A13 | Matched policy/utility expressivity | Compare terminal changes with fixed-utility contracts and delegation under the same technology. |
| A14 | Linear resource utility / risk neutrality | Static seed convenience. Test nonlinear, multiobjective, and nontransferable utilities. |
| A15 | Finite or convergent discounted evaluation | Necessary for the selected expectation formulas; analyze average reward separately rather than subtract infinities. |
| A16 | Fixed power and no first-strike advantage | Seed convenience; vary endogenous power investment, asymmetric destruction, and preemption. |
| A17 | No or finite utility-freezing preference | Test positive finite costs, contingent commitments, hard constraints, and lexicographic preferences separately. |
| A18 | Outcome-only utility without combat/process bonus | Seed convenience; test direct preferences about conflict, identity, control, and the route to outcomes. |
| A19 | Specified fitness and transmission map | Required for population claims. Never equate fitness with utility by default. |
| A20 | Specified mixing, observation, and mutation | Required for evolutionary conclusions. Test assortment, rare invasion, exploitation, and inaccessible mutant types. |
| A21 | Time resolution and interruption opportunities | Declare simultaneous/sequential moves and collision priority. Vary slot size, attack during implementation, and first-move advantage. |
| A22 | Agency, ownership, and delivered-output boundary | Specify survival/incapacity, shared/private control, and whether past output can be seized or destroyed. Do not infer loser welfare from loss of control. |
| A23 | Recovery technology and resource boundary | Integer vs divisible stocks, sequential vs parallel processing, work store vs total exergy, imports, material conversion, infrastructure repair. Recheck feasibility and accounting on replacement. |
| A24 | Utility identity and admissible objective menu | Declare the common outcome domain and equivalence of representations. Menu restrictions and finite vs lexicographic preferences are instance assumptions. |
| A25 | Current-self solution concept and selection | Specify best responses of incumbents/successors, off-path behavior, beliefs, and any selection rule. Founder optimization is only an external welfare perspective after change. |
| A26 | Strength-weighted control and contest | E2 separates controllable policies from utility representations. Additive strength plus identity-neutral grouping forces linear weights (R102); nonlinear synergy is a different physical assumption. Control draws need not end the other's attack capability. |
| A27 | Goal aggregation and actual outcome domain | Deterministic mixed-color worlds, lotteries over exclusive worlds, and vectors of expected utility are distinct domains. R105 constructs a proportional deterministic objective; R114 obstructs unique interior lottery implementation. Weights do not automatically change when a founder loses agency. |
| A28 | Deception observation and credible response | Detection kernel, verification effort/cost, physical camouflage and postdetection choices must be specified. R110's restored-honesty example defeats an assumed punitive threat; R111 requires implementable branch payoffs. |
| A29 | Exclusive-control delegation versus retained attack | Note 010 section 13 grants a stronger control-transfer technology; E2-U section 14 retains both agents' attack capability after the operator draw. Neither comparison licenses silently removing attacks from the baseline. |
| A30 | Restricted sequential update menu and finite task | E2-U permits A then B one opportunity to install G, plus attacks, ordinary production and rejection. R117–R118 do not prove claims about arbitrary rollback, repeated encounters or physical fusion. Remove the restriction in a new protocol. |
| A31 | Locally peaceful continuation selection | E2-U selects peaceful last-stage equilibria where a G-agent is present. R118 specifies round-2 selection too. Weak war equilibria remain; changing off-path selections can alter adoption. No claim of generic/unique equilibrium selection. |
| A32 | Publicly recognized stochastic installation failure | R119–R120 use independent trials, success installs G, failure preserves the old goal, and either result pays the round's physical cost. Known probabilities are not known draws. Hidden corruption, correlated failures and costly verification require new continuations. |

## Scope of C1 and reference instance E1

C1's invariants concern physical availability, honest accounting, current-utility evaluation, and comparison/reporting. They do not require E1's public information, utility menu, horizon, or transition coefficients. A new instance may change any local choice below without changing C1, but must reassess affected claims.

| IDs | E1 setting | Status / informative variation |
| --- | --- | --- |
| A01–A04 | Own objective/menu known; specified stochastic model; agent choices dominate | Starting idealizations; correct modeling does not reveal chance draws |
| A05, A21 | Both capable agents may attack in every slot/phase; attack has priority | Core availability rule with local simultaneous timing; vary initiative/interruptions |
| A06, A23 | O/D/Z feedstock, finite battery work, recovery costs, capacity damage | Local engineering abstraction; no thermodynamic calibration or entropy theorem |
| A07, A14, A18 | S/F monotone in own delivery; G balanced joint output; no combat bonus | Menu convenience, not a restriction on C1; try destruction/status/threshold goals |
| A08, A22 | Integer shared stock, alternating access, ordinary Work and P; protected deliveries | Local property/control arrangement; vary divisibility, ownership, output vulnerability |
| A09–A10 | Complete information and public labels; common contest probabilities | Strong instance assumption; not implied by self-knowledge; compare hidden types |
| A11–A12 | Reliable individual installation; reciprocal installation sequential, reversible | No global atomicity/durability. E1-D separately grants durable delegation and protected installation |
| A13 | E1-F matches physics/info; E1-D has a larger contingent-policy menu and stronger execution | No modification/commitment equivalence assumed; match durability and verification before causal comparison |
| A15–A16 | Twelve-hour task; fixed equal power; no first-strike advantage | Finite witness only; repeated and endogenous-power instances remain available |
| A17, A24 | Three explicit utility classes; S has finite per-change penalty, F/G omit it | Positive affine recoding excluded from change; hard/lexicographic freezing remains open |
| A19–A20 | No population process in E1 | No prevalence, invasion, or reproductive-fitness result |
| A25 | Local stage best responses of current decision selves at every history; mixed actions allowed | No unique selection imposed; private information requires new belief consistency conditions |

Source assumptions and transfer limits are in [the literature audit](LITERATURE.md). In particular L02's modification independence, L04/L05's program implementation, and L08's private-type/matching assumptions are not silently inherited by C1.

## E2.0 / R0001 dependency and removal map

These are local alternatives, not new C1 invariants. [E2](models/E2.md) leaves its protocol and implementation parameters open; [note 010](notes/010-essay-formalization.md) states them separately for each result.

| Setting / dependencies | What follows locally | Removal or limitation |
| --- | --- | --- |
| A06, A23: divisible O/D material, finite work/time, fixed sequential coefficients | Exact recovery frontier and damage thresholds, R106 | Parallel processing, endogenous repair, multiple outputs and interruptions need a new feasibility proof; spare capacity can erase a dispersion loss |
| A07–A08, A14, A18: own-color linear utilities and feasible full-output splits | R107 bargaining interval and merger participation thresholds | Concavity versus convexity changes lottery comparisons; asymmetric winners defeat fixed proportional division; process goals need actual history payoffs |
| A24, A26–A27: preference classes, fixed strength weights, a declared physical domain | R101–R105, R114–R115 semantic and implementation boundaries | A raw utility vector is not a probability law; literal code-driven influence is a stronger behavioral assumption |
| A09–A13, A28–A29: observation, cost, durability and delegate expressivity | Conditional replication R113 and verification boundaries R110–R111 | Unverifiable goals, revocable programs or identity-dependent responses break equivalence; inspection need not supply credible sanctions |
| A05, A16, A21–A22, A25, A30–A31: finite E2-U protocol and selected continuations | Voluntary one-sided change R117; finite-freezing/preemption classification R118 | No population or unlimited self-modification claim; weak war equilibria and off-path selection remain; actual fusion is not dual goal adoption |
| A17: finite historical preference-change penalty kappa | R118 can reverse which agent changes; negotiation work changes the threat by date | This compares initial types only. Voluntarily rewriting kappa, hard freezing and transmission/fitness remain unresolved |

No fitness/transmission mechanism (A19–A20) has been added. R118 is not evidence of invasion or of voluntary adoption of a stronger freeze.

R119 varies A32 at zero freezing; R120 combines unequal success probabilities with finite initial freezing. Its strict-region classification is local to E2-U and the declared continuation selection. R119's nonmonotone combat probability comes from changing the number of attempts, not from worse reliability under a fixed protocol.

## Required comparison record

For a claimed peace advantage, record the model version, utility class, feasible mechanisms, physics, horizon, beliefs, and solution concept. State whether the result establishes feasibility, individual preference, adoption equilibrium, dynamic stability, coalition stability, or prevalence.

For every major positive result, seek a minimal negative instance. Try both one-at-a-time removals and meaningful interactions: e.g. reversibility plus changing power; finite freezing plus discounting; observability plus commitment benefits; physical recovery cost plus target-specific utility.

Do not rank assumptions by frequency of favorable simulations alone. Explain the proof dependency and how much the conclusion changes when an assumption is removed. At synthesis, classify each as essential in the model, a replaceable sufficient condition, a tractability choice, or unresolved.
