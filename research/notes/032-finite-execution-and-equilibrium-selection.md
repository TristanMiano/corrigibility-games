# R0001 working note: a finite execution refinement selects the local peace

The E2-U calculations in note 010 deliberately select peaceful checkpoint continuations when a compromise-goal agent is present. Weak mutual-attack equilibria also exist. This note asks whether a precise mistake model can select those continuations. It gives a positive result for a finite execution control, while retaining every attack action. The self-contained finite-game argument is self-checked only; it is not a new general equilibrium-refinement theorem.

## 1. Declare the perturbation and the finite control

Use E2-U's public finite horizon, two administrative rounds, attack priority, actual resource transitions and current criteria. Replace each continuous allocation simplex by a fixed finite menu containing the two own-color endpoints and the equal split at that route's output frontier. It may contain other feasible allocations, including underproduction. The original own-color controller and the balanced G controller must each have a unique maximizing physical allocation in the menu; duplicate action names with identical consequences can be consolidated. This is a finite execution comparison, not a restriction on C1 or every future E2 model.

At every simultaneous checkpoint, independently constrain each player's behavior to put probability at least eta>0 on every available action, with eta less than the reciprocal of the largest menu size. The remaining probability is chosen to maximize that decision maker's current expected utility. A finite public-history continuation is solved backward using these constrained action simplexes, recording every evaluator's utility on every branch. Each stage has a mixed equilibrium because it is a finite game on compact mixed-action polytopes. No founder substitutes a new utility's numerical score at installation.

Postwar production can receive the same finite-menu perturbation; its optimal allocation converges to the specified current-goal optimum as eta tends to zero. All combat and physical chance kernels otherwise remain fixed. Recognized installation failure with probability 1-p is distinct from the action tremble eta.

We study limits as eta tends to zero of these backward-solved behavioral profiles. This is an explicitly defined independent behavioral-perturbation refinement. We do not identify it without proof with every normal-form, correlated-error, continuous-action or evolutionary refinement. For positive eta there is a real positive risk of mistaken attack; the conclusion about certain local peace concerns the limit.

## 2. A last-checkpoint selection lemma

Suppose a selected operator has a finite production menu and a unique preferred peaceful allocation x*. The other capable agent chooses Continue or Attack. Either attack triggers a common continuation with current payoff vector c, independent of the unexecuted allocation. Suppose the operator strictly prefers x* to this combat continuation.

Against every fully mixed opponent, every alternative allocation yields less to the operator than x*: the payoff difference is its strictly positive production-utility gap multiplied by the positive probability of Continue. The same holds against the operator's own Attack action, by its strict preference over c. Thus its constrained best response puts all probability beyond the compulsory lower bounds on x*. This remains true even if the opponent's continuation probability tends to zero.

Consequently, if the nonoperator strictly prefers x* to c, its constrained best response concentrates on Continue for all sufficiently small eta. If it strictly prefers c to x*, it concentrates on Attack. These are the only possible limiting outcomes. Bounded postwar perturbations change c continuously and preserve the strict comparisons for small eta. The result is not obtained by deleting combat or pricing it infinitely.

In E2-U with common output P=1 and final W=1/4:

- With two original goals, the operator chooses its own-color endpoint, and the nonoperator strictly attacks. Every perturbed limit gives war.
- With at least one balanced G goal, the operator's unique maximizer is the equal split if it has G, or its own endpoint otherwise. The other agent strictly prefers continuation in both cases, by note 010 section 14's actual current-goal war comparisons. Every perturbed limit gives the selected peaceful production.

These limits give exactly the founder-welfare table used in E2-U. A separate reason for selecting that table is now available for this finite control; the original unrefined game still has its additional Nash equilibria.

## 3. Backward propagation through an administrative checkpoint

A useful general form has row actions j=1,...,m and Attack, column actions Wait and Attack. Against Wait, nonattack row j gives continuation vector v^j; any attack gives c. Suppose the row player's largest value among {v_A^j,c_A} is unique.

If its maximizer is a nonattack row j*, every positive probability of column restraint makes j* its unique best action. Under the constrained simplex it therefore receives all residual probability. As eta tends to zero, the column player's Wait-minus-Attack comparison tends to v_B^{j*}-c_B. If this difference is positive, the unique limiting initial outcome is j*/Wait. If negative, it is j*/Attack and combat. If the row player's unique maximizer is Attack, every limiting outcome is combat, although the column's behavior can remain undetermined because its action no longer affects the outcome. Ties require separate analysis.

The proof also applies when v^j(eta),c(eta) converge to these strict-region values: their finite set of strict comparisons persists for sufficiently small eta. The row comparison is always conditional on the positive probability of Wait, so a small unconditional payoff difference is not incorrectly treated as an exact tie.

Apply this argument backward after section 2. In zero-penalty, reliable E2-U, B installs G in round two if A kept, and keeps if A installed. Both choices have strict conditional advantages over its other rows and immediate combat. The passive controller strictly prefers waiting for the respective continuation. At the first round, A then strictly keeps and B strictly waits. Thus every backward perturbation limit has **A keep, B install G**, with founder outputs (3/4,1/4), in this finite control.

More generally, the strict-region classification of note 010 section 17 survives as the classification of limiting initial outcomes: use its K, M, J and initial combat vector. When the selected nonattack row is strictly better than immediate combat for both founders, the perturbation limit selects initial restraint. When its required strict comparison fails, the limiting initial outcome is combat. At a later subgame where Attack is the unique maximizing row, the continuation outcome is the same combat law regardless of the passive player's possibly undetermined behavior; this preserves the continuation values needed for backward propagation. Branches with ties are explicitly excluded as in note 010.

Action names with identical consequences can remain tied without changing this outcome conclusion. In particular, if p_B=0 after A already installed G, B's Keep and a recognized always-failed attempt have the same costs and resulting state in this witness. Consolidating those equivalent rows, or leaving their residual mixture unspecified, gives the same limiting continuation values. No uniqueness of their literal action labels is asserted.

## 4. Reliability and freezing remain substantive after this selection

For equal installation reliability p and zero penalties, the resulting limiting combat probabilities are still (1-p)^2 for 1/25<p<1/5 and 1-p for 1/5<p<=1; below 1/25 the limit starts combat. Therefore the increase from 6561/10000 at p=19/100 to 79/100 at p=21/100 is not solely an arbitrary choice between the local peace and mutual-attack Nash equilibria. It persists under this declared finite behavioral perturbation. It remains a comparison of two different installation technologies, not an increase in failure risk for a fixed protocol.

The welfare accounting identifies the externality at the switch. Approaching p=1/5 from below, the founder vector tends to (1/4,27/100); from above it tends to (1/4,3/20). A is indifferent at the switching parameter, while B loses 3/25. Total expected output falls by the same 3/25, equal to the combat-probability jump 4/25 times the per-fight output loss 3/4. These are one-sided limits; the equality parameter has extra indifferent selections. A's privately optimal reduction in attempts does not maximize the two founders' total physical output.

With reliable installation, kappa_A=0 and kappa_B=119/1000, the limiting initial outcome is combat. With kappa_B=121/1000 it selects A installing while B keeps. The timing and finite-freezing effect likewise survives this particular refinement. These parameter points are in strict regions; no statement assigns the same selection to the excluded equality surfaces.

## 5. Limits of the repair

The original continuous allocation game cannot be given a positive lower bound for every individual allocation. Extending this proof to continuous execution noise requires an explicit kernel and suitable optimization/convergence conditions. A finer physical timeline can introduce new threats and invalidate the finite game's continuation vectors; note 027 gives the appropriate proof obligations. Correlated action mistakes, report-dependent errors, hidden partial installations and strategic control over the error process are different models.

The refinement does not make the outcome a common-goal convergence theorem: one original agent still keeps its goal, and the later modifier's founder gets less than under a protected reciprocal half split. An enforceable unchanged-utility allocation or a different control architecture may yield another equilibrium comparison. Note 030's territorial control is an example. No population prevalence follows without supplying note 019's separate encounter/transmission assumptions.

This result can support those encounter selections in a finite execution variant, but does not automatically add trembles to its published birth map. At a positive eta, mistaken attacks and updates change that map; its population fixed points would need to be recomputed. The limit in eta and the long-run population limit need not be interchangeable without a separate argument.
