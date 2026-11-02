# Finite private-information current selves: completing a supported path

R0003 working mathematical note. Review is contributing-agent self-check. This note develops an existence/completion tool; an application still has to verify its bounds in a specified physical protocol. It does not turn E3's conditional Nash result into a sequential-equilibrium theorem merely by changing the label.

## 1. The decision maker and the belief system

Take a finite physical extensive tree, with finite actions and chance outcomes and a common specified chance law. Remove zero-probability chance edges, but retain every physically possible player action, including attacks. No information set contains both a node and a descendant of that node; a known finite control clock is one way to ensure this. Feasible action sets agree at nodes in the same information set. At an information set I the active controller knows its current evaluator epoch and its own relevant history. That evaluator has a fixed real-valued function u_I on complete terminal histories, including histories after replacement or loss of agency. The function is not overwritten when a successor activates.

Give each information set a separate decision agent. It controls that information set only and evaluates terminal histories with u_I. Its utility away from histories that can reach I can be completed arbitrarily: those terms cancel in its own action comparison. Each such agent has perfect recall trivially, since it has no previous decision of its own. A behavioral profile and conditional distributions over the nodes in each I form an assessment.

Call the assessment a **local current-self sequential equilibrium** when (a) every local action is optimal for u_I given its conditional distribution and the other decision agents' continuation, and (b) those distributions are limits of Bayes beliefs from a common sequence of completely mixed behavioral profiles. Separate agents do not give archived founders decision authority. Their preferences remain reporting coordinates.

For an evaluator that persists over several decisions, assume perfect recall and consistency of its complete-history criterion during that tenure. Local optimality then also rules out a multi-action tenure deviation: starting at the last changed decision, replace it by the prescribed best response, and repeat backward. Stop this comparison when a genuinely different evaluator acquires authority; a predecessor cannot include that successor's choices in its own deviation. Memory reset and reactivation must use the actual new epoch, as in note 029. Without the stated tenure assumptions the local concept is the claim, not a claim of optimality for a commitment-capable persistent player.

## 2. Existence, with beliefs at every information set

**Finite existence lemma.** Every finite current-self tree just described has a local current-self sequential equilibrium.

For 0 < epsilon < 1/max_I |A(I)|, restrict every local behavioral probability to be at least epsilon. The product of these restricted simplexes is compact and convex. Each decision agent's ex-ante payoff is continuous in the profile and affine in its own local action distribution; its best-response correspondence is nonempty, convex valued and upper hemicontinuous. A finite-game fixed point supplies a restricted equilibrium sigma_epsilon.

Every information set is reached with positive probability under this completely mixed profile. Its reach probability is independent of its own decision agent's action, because that agent acts only there and the tree never revisits the same information set. Dividing its best-response inequalities by that positive probability gives conditional best-response inequalities under Bayes beliefs mu_epsilon.

Choose a convergent subsequence of the strategy/belief pairs in their finite products of simplexes. At a local action assigned positive limiting probability, the lower probability restriction eventually has slack. Its conditional payoff is at least that of every action with slack transfers available. Conditional continuation payoffs are continuous functions of the local beliefs and future behavioral strategies. Passing to the limit gives local sequential rationality. The same subsequence establishes belief consistency by construction. This proves the lemma, including off-path information sets. It establishes existence, not selection of an accommodation outcome.

This is a specialization of conventional finite extensive-game/agent-form fixed-point reasoning. Kreps and Wilson (1982), *Sequential Equilibria*, pp. 867–868 specify perfect recall and terminal preferences; pp. 871–872 define sequential rationality and consistent assessments; Proposition 1 on p. 876 states existence, referring to Selten's existence theorem and their Proposition 5. Those primary passages and the perfection comparison on pp. 882–884 were inspected in the [original article scan](http://www.dklevine.com/archive/refs4237.pdf). Selten's external proof and the paper's genericity/topological theorems were not audited. The present local construction spells out its own fixed-point/limit argument; no novelty claim attaches to general existence.

## 3. A completion lemma for a proposed accommodation path

The missing step in an application is ensuring that an equilibrium contains the proposed installations and peaceful execution. The following stronger sufficient condition is useful because it separates that work from arbitrary off-path beliefs.

Specify a pure action prescription p on a set P of information sets. Following p, with all positive-probability chance branches retained, must generate a well-defined finite path tree. Every I in P is reached with positive probability in that tree, and every nonterminal decision reached in that tree belongs to P. Consequently its Bayes belief mu^p_I is determined by the prescribed path tree and the actual chance kernel. Hidden effort is permitted; prescribing Work does not publicly reveal it.

**Universal continuation condition.** At every I in P, following p(I) and the subsequent path prescription is at least as good under u_I and mu^p_I as taking any alternative local action and then following *any* continuation allowed in the remaining game, while all other prescribed on-path actions are retained. This can be a bound over a larger class than feasible continuation strategies. The condition must cover offers, changes of goals, implementation alternatives and physical actions, not only a named Attack deviation.

**Completion lemma.** Under that condition, there exists a local current-self sequential equilibrium whose path is p. Equality is allowed; the result is existence of a selected implementation, not strict selection or trembling-hand perfection.

**Proof.** In the epsilon-restricted construction, force each I in P to assign 1-(|A(I)|-1)epsilon to p(I) and epsilon to every other action. Leave all other decision agents free in their restricted simplexes. Their finite constrained game has an equilibrium. All its information sets, including those outside P, have positive reach probability, so Bayes beliefs are defined. Choose a convergent subsequence. Outside P the preceding conditional-best-response proof applies unchanged. At I in P, the limiting reach probability is positive and its belief is mu^p_I; limiting off-path behavior is one of the continuations covered by the hypothesis. The universal continuation condition therefore establishes its best response. Beliefs are consistent through the same common sequence. QED.

The perturbations used for consistency need not themselves be equilibria at the forced path choices. Sequential rationality is required in the limit. This matters for an equal-cost matched delegate: a weakly optimal genuine change need not survive every refinement that favors one device's response to trembles. Its sequential-equilibrium adoption can nevertheless be substantive.

The hypothesis is stronger than a Nash inequality against one conjectured off-path reaction. If a deviation can induce a better concession in some feasible continuation, the displayed lemma is unavailable until the continuation class is narrowed by separately proved rationality, or the protection design is repaired. Ordinary equilibrium existence does not supply that missing bound.

## 4. A useful extension: first-approval protection at unreached sets

An application can impose additional restrictions during the constrained construction, provided their local rationality is proved separately in the limit. For example, suppose a clean guard has

\[
u=B+\beta e-KI,\qquad 0\le B\le M,\quad 0\le e\le1,
\quad K>M+\beta.
\]

Here I records that evaluator's actual first unsafe approval. At every information set where its flag is zero, an unsafe approval makes every resulting terminal value strictly negative. If safe refusal, followed by the other imposed clean-guard restrictions, secures a terminal value at least zero, unsafe approval is strictly suboptimal for every posterior. Impose only epsilon probability on unsafe approvals at these sets, and allow all safe choices to optimize freely. In the limit the imposed restrictions are sequentially rational even at unreached sets. The finite number of future trembles contributes an error tending to zero during the construction.

Any other already-fixed historical penalty is first subtracted from both alternatives when using the zero comparison. Past penalties remain sunk for the evaluator whose flag is already one; that case is unconstrained and receives an ordinary best-response completion. A newly installed guard has its own epoch. The physical action relation defining unsafe approval must be specified before its utility, and the continuation must preserve the old evaluator's actual historical flags. Work, Shirk and Attack remain outside this approval predicate and need their own comparisons.

With these independently validated restrictions, section 3 only needs its deviation bound over the resulting limit continuations. This is useful for an incompatible initial controller: a compatible partner's first unsafe concession can be ruled out by rationality at *every* relevant information set, rather than by an arbitrary hostile belief.

## 5. What an implementation still must prove

The application must specify the finite raw action/observation tree and physical transition kernel; the goal/contract language and its costs; the clean-guard relation and safe refusal; original adoption against all compatible, incompatible and abort routes; private performance incentives; current attack and exit comparisons; and actual costs and beliefs after messages. A finite list of possible mechanisms is a local technology assumption, not a fixed model contract or a result about arbitrary utility programs.

A concrete issue from E3 shows why this audit matters. After one agent has privately worked, a posterior that the other shirked can change its return from continuing. For original-output B in the linear example, own holding 1.35 plus a 0.1 chance of 5.5 gives 1.9. An early equal-strength recovery bound of 4 permits a combat mean of 2. The earned contribution reward cancels. Thus a proof cannot assert posterior-independent restraint at every unexpected pre-reaction message from the on-path mutual-work calculation alone. A lower recovery frontier, an additional task-completion preference, an information-compatible continuation, or a direct equilibrium completion can repair this local gap; their costs and the corresponding successful region must be checked. This observation does not undo the existing on-path calculation or imply that the actual message induces that posterior.

The next note will apply the completion argument to an explicit finite agreement class, retaining the positive instrumental-change target and testing the physical, informational and alternative-mechanism boundaries together.
