# R0002 working derivation: voluntarily chosen guards with future goal variation

**Finite-guard lemma registered within R204; sequential adoption candidate remains scoped.** The productive certificate protects accepted outcomes while its efficient fallback remains available. This note investigates how agents could choose safeguards that preserve that fallback through later goal variation. It uses deliberately designed, history-sensitive preferences and strong, explicitly scoped verification. The parallel timing, grounded instruction relation and execution repairs in 046/049/056 support [E3](../models/E3.md)'s conditional result; they do not solve every earlier sequential commitment game. Review is contributing-agent self-check.

## 1. Why guarding future updates must itself be negotiated

In 037, changing B's goal within y+mu x, 0<=mu<1, preserves the productive default. Arbitrary hostile, contract-contingent or process-sensitive goals can instead erase it and change bargaining threats. Merely restricting the analyst's future type menu would leave the voluntary-choice question unanswered.

Suppose the agents can install a certified family of guarded goals. Original B need not initially value staying in that family. A therefore makes its own productive participation conditional on B voluntarily choosing a compatible guard. The hypothesis is constructive: can that condition make B's guard adoption advantageous under B's original project goal? Its limiting counterpart is whether feasible deception, randomization, transfers or guard removal defeats the condition.

## 2. A finite approval guard

Use absolute project outcomes X,Y>=0 on a bounded physical episode. In the 037 material ledger, X+Y<=16 pathwise. Let a goal's base criterion be X+lambda Y for A, or Y+mu X for B, with parameters below one. Each base value therefore lies in [0,16].

Let I_i be the indicator that, after the current evaluator's activation, agent i voluntarily approves a noncertified continuation mechanism. A guarded criterion is

$$G_i=\text{base}_i-K_i I_i,\qquad K_i>16.$$

Approval includes consenting to an unsafe goal replacement, an unsafe binding delegation or a public lottery/commitment with unsafe support. The event occurs at that approval, not only if a later random draw happens to install the unsafe goal. A privately randomized behavioral choice cannot profit from mixing in an individually dominated unsafe approval. For a publicly committed lottery, approving unsafe support is itself an unsafe approval and incurs the penalty with certainty. This distinction closes the randomized-event loophole of a penalty charged only on realized subsequent goal changes.

Every unsafe approval has continuation value at most 16-K_i<0. A safe refusal/retention continuation has nonnegative base value and no penalty. Therefore a current guarded agent strictly rejects every unsafe approval. The penalty is finite and does not charge combat. Physical attacks remain possible and are evaluated using actual output consequences.

This criterion is genuinely different from the base preference on complete histories, even when it induces the same behavior on a protected productive path. Positive affine recodings of the entire criterion, including K_i, are equivalent preferences; code changes alone are not the event. Certificates concern declared preference/behavioral properties of the active implementation, not a string label or an arbitrary semantic oracle.

## 3. A large safe family, with an explicit boundary

For the 037 default, let A's safe output parameters range over a closed interval [lambda_min,lambda_max] strictly inside (lambda_0,1); let B's range over [0,mu_max] with mu_max<1. Safe goal updates preserve the guard rule and its finite bound. They may change these parameters, representations and implementations with a valid certificate. All such output preferences keep mutual effort strictly incentive compatible under the existing default. The family contains a continuum of genuinely different lottery preferences rather than a single frozen objective.

The safe mechanism class also contains every consensual output contract or lottery satisfying the current-self participation conditions and physical resource bounds, as long as it does not silently remove the productive default before that comparison. Goal-preserving transfers are included. Their founder protection comes from the efficient-fallback certificate, not from counting them as goal-change events. A mechanism that would first erase the default without a replacement certificate is outside the safe class and can still be physically chosen, at its finite current-utility penalty.

A sound verifier for this parameterized family is an implementation assumption. Self-knowledge is insufficient. The model requires actual controller attestation and checks for the declared update/approval kernel, at a charged physical cost. Arbitrary unverified programs and unsound certificates remain enlarged-class tests. The class and verification technology are intentionally designed; their naturalness must be assessed separately from the simple original project goals.

**Physical-preservation correction.** Parameter preservation alone is insufficient: repeated updates, delay, sabotage or an outstanding binding timer can remove the productive fallback. A safe certificate must also cover the actual remaining work, time, allocator state and outstanding commitments. A deliberate noncombat reconfiguration or delay that removes the fallback without a certified replacement counts as an unsafe approval. Safe updates are allowed only while their charged costs leave a feasible certified continuation. Production and an accepted replacement may consume the fallback when their current-self participation certificates justify that transition. Attack is excluded from the penalty and requires its own physical incentive check. This makes the guard a demanding mechanism-level commitment; it is not merely a type restriction.

## 4. A sequential adoption construction

Initially both original agents value their own project output. A may first install a guarded goal with lambda in the safe interval and an additional rule: approving productive participation or a binding exchange with an unguarded counterparty is an unsafe approval. This rule includes A's own contribution to the default joint project while B remains unguarded. It permits refusal, ordinary retention, and combat; it does not prohibit them physically.

If B stays unguarded, A will not contribute or consent to an unsafe agreement. B's solitary production is unprofitable because aY<c_B. An unconditional gift cannot purchase A's later effort: with linear project values and a fixed effort cost it does not remove the approval condition, and B's lost project output must still be paid. Under the 037 low-combat physical instance, attacking also pays B less than retaining its stock. Thus B's best unguarded continuation is its stock fallback, net zero, within this declared mechanism class.

**Threat/gift correction.** That last conclusion needs the participation condition to cover voluntary outgoing concessions and gifts to an unguarded partner as well as signed exchanges. Otherwise B could choose an attack commitment and seek an unconditional payment. Passive receipt, retention and attack remain available; outgoing concessions require compatibility. A valid partner certificate must cover existing binding commitments and actual control, not only the newly installed goal string. An attack timer installed before certification cannot be ignored. These are explicit strengthening assumptions for the candidate guard, and their installation and verification costs remain to be integrated.

B can instead install the guarded goal Y-K_B I_B, retaining its original output ranking while genuinely changing its preferences over future approval histories. A's counterpart condition is then satisfied. The productive default yields B net r_B>0. Original B evaluates adopting the guard using Y and strictly prefers it to the unguarded fallback. Before activation B uses its original criterion; after activation it uses the guard. Both prefer the constructive continuation at the intermediate attack checks from 037.

Once B is guarded, A's actual base goal X+lambda Y induces its effort; B's base Y induces its effort. Mutual effort attains maximum expected net surplus C. Consensual safe renegotiations then preserve both expected project payoffs: each retains a strict own-project priority at a fixed total and each can reject to the efficient default. Neither a transfer nor a lottery can give one agent more without making the other reject. Unsafe proposals and unsafe support in public lotteries are rejected by the finite approval guard.

Original A anticipates net r_A>0 from installing this jointly enabling compromise/guard. In 037's B-proposer comparison, keeping the original goal yields net zero after B's optimal enlarged response. Hence A strictly prefers its first change. The two updates are evaluated by the two original project goals at their respective adoption decisions. A's concern for B and B's later-update guard are both chosen instrumentally; neither is silently inserted into the original agents' preferences.

This is a candidate complete sequential construction. The required physical step count, attestation semantics and counterparty condition must be integrated into a state table before registration. In particular, a feasible unguarded route that makes A contribute or supplies B more than its stock fallback would change B's adoption comparison and must be tested rather than excluded by wording.

**Initial-choice scope correction:** this sequential calculation establishes B's guard adoption conditional on A already choosing the displayed guarded controller, and compares A with Keep in the specified proposer game. It has not optimized A over arbitrary earlier aggressive commitments. The parallel pre-observation adoption construction in 046 addresses that initial deviation class under a different, explicit timing assumption. The sequential proposal is not promoted to a full arbitrary-goal equilibrium by that later result.

## 5. Future updates and evaluator memory

For any finite sequence of later update opportunities, current guarded agents strictly refuse the first unsafe approval. Safe updates activate a new guarded evaluator, whose own future-approval flag begins at zero. Archived criteria continue evaluating complete histories with their original reference times; they do not control the new evaluator. This is the epoch distinction in 029. Backward induction through the finite sequence establishes that no voluntary unsafe approval occurs on the selected continuation, while safe genuine parameter changes remain possible.

This argument needs a nonnegative safe continuation at each relevant decision and the common physical bound. If an unsafe event has already occurred, its penalty may be sunk, and the theorem does not claim the old guard restores itself. Forced replacement, false attestation, loss of agency and resource changes need their actual kernels. A longer or renewable horizon can exceed the bound used to set K_i. For a bounded discounted future a new finite bound may be available; for an unbounded undiscounted future this finite-episode calibration cannot be reused.

## 6. Limits and matched controls

The guard's selection of an entire approved mechanism class is more demanding than a penalty on a single code-change event. That strength is explicit. It does not eliminate the possibility of profitable accommodation: the safe family permits substantial changes and all participation-compatible transfers and lotteries, and the first guarded compromise is adopted because it increases original project output. Nor does it establish general long-run convergence or population prevalence.

A fixed-utility principal with a binding, publicly attested conditional delegate implementing the same participation and update policy can reproduce the result. Equal cost gives a tied alternative; cheaper or more reliable delegation can displace direct goal modification. This identifies shared commitment machinery and is compatible with voluntary genuine change. The nearest existing repository comparisons are L04–L05 on program/delegation mechanisms; their theorems are not automatically imported into this physical game.

Replication here holds for the same declared policy and compatible mechanism class. Adding unrestricted binding delegates also adds new threat commitments and can alter the other agent's best response. It is not valid to infer that the original full-game equilibrium survives such an enlarged technology merely because one delegate can reproduce its on-path actions. A guard must be checked against that enlarged space, or the equivalence must remain an implementation comparison.

Future tests should examine cheaper monitoring or transfer devices that repair ordinary production, and feasible guard-bypass or richer-goal mechanisms that change the chosen arrangement. Both successful repairs and persistent protected classes are evidence toward the charter question. The current construction remains explicitly scoped to its bounded physical episode, certified family and declared approval semantics.
