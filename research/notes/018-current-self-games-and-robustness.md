# R0001 working note — current-self games, existence, and model errors

A model allowing repeated goal changes needs a coherent solution concept before any peace theorem. This note supplies finite and discounted subclasses of E2 that have such a concept. Finiteness, public state, additive discounted evaluation and bounded rewards are local sufficient assumptions, not additions to contract C1. Equilibrium existence does not imply peace, adoption of a particular goal, uniqueness, or population prevalence. Proofs are self-checked only.

## 1. Separate decision authority from evaluation

For each possible controller lineage and current preference class, introduce an evaluator label tau. Two labels are distinct only when the actual relevant preference or lineage-dependent history criterion differs; positive affine recodings of the same expected-utility ordering do not create new preferences. The physical state determines which labels currently have decision authority. An inactive label has only a dummy action. Combat actions belong to each capable **active controller** at the relevant nonterminal states; an archived goal does not acquire an independent army merely because it remains an evaluator.

Every evaluator's criterion remains defined on actual future outcomes, including outcomes after it loses authority. At a goal-changing action, the current evaluator scores the actual continuation using its own criterion. At the next decision, the new active evaluator chooses according to its different criterion. Original-founder evaluation can be retained as an additional reporting coordinate even if that founder never acts again. A merger introduces the declared joint controller and its actual goal; it does not silently retain both founders as active decision makers.

An example shows why a single value function whose reward definition is overwritten at modification is wrong. At the initial state original A values x_A. Keep produces (1,0). Modify installs a successor valuing x_B, which then chooses between (2,0) and (0,3). The successor chooses (0,3). The correct initial modification value is zero, so A keeps. Substituting the successor's numerical value three into the original decision would reverse the choice. The continuation vector must contain both values: V_original=0 and V_successor=3. This does not forbid instrumental modification: if the actual modified continuation instead produces (2,3), original A values it at two.

Identity, change penalties, memories, agency and delivered output must be included in the outcome/state description whenever a criterion depends on them. They are not reconstructed from a utility label after the fact.

## 2. Finite public-history games

Consider a finite tree with publicly observed histories, finitely many actions at every decision, and finitely many possible active evaluator labels. Simultaneous moves at a checkpoint are allowed. Chance transitions include strength-dependent combat, failure, physical resource changes, verification and goal replacement. Each evaluator has a fixed real-valued utility on the complete terminal histories. Agents may have different criteria for the same terminal physical world if their process or identity preferences differ.

There exists a mixed current-self subgame-perfect profile, with authority assigned to the active evaluator at every history.

To construct it, work backward. At each final decision checkpoint, form the finite simultaneous game whose acting controllers evaluate its possible terminal histories by their current criteria. Select a mixed Nash equilibrium. Record the induced expected terminal utility for **every** evaluator label, including inactive founders. At the preceding checkpoint, each action/chance branch now has this entire continuation vector. The active label selects its own coordinate when forming its stage payoff; select another finite-game Nash equilibrium and continue backward. All histories, including off-path failed installations and rejected agreements, receive continuations.

Equivalently, this is a finite extensive game whose fixed players are evaluator labels and whose action sets are dummy whenever the corresponding label is inactive. Backward construction ensures no profitable last deviation by a label. Induction rules out a multi-decision deviation by that same label, including histories where its preference class is restored, while holding the genuinely different future evaluators' strategies fixed. The old founder is not allowed to dictate a successor's decisions merely by calling that a unilateral strategy change.

The construction requires selecting equilibria at many nodes and does not assert they are unique or peaceful. It is an existence argument, not an efficient algorithm for a large physical model. Hidden state, private utility, memory loss or unbounded menus require additional information and existence analysis.

## 3. A finite-state discounted extension

Let the public state set S and all state-dependent action sets be finite. The state includes the live-controller/goal map and enough physical/history information for a Markov transition kernel K(s'|s,a). Each evaluator tau has a bounded transition reward r_tau(s,a,s') and a discount factor beta_tau in (0,1), and evaluates

$$V_\tau^\sigma(s)=
E_s^\sigma\left[\sum_{t=0}^\infty
\beta_\tau^t r_\tau(s_t,a_t,s_{t+1})\right].$$

Rewards are evaluated even while tau is inactive. Future evaluators have their own reward functions and discount factors. A finite history flag can represent a one-time change penalty; an unbounded change count cannot be silently compressed into a finite state if the utility depends on it. Absorbing termination states and any later founder welfare must be defined explicitly.

There is a stationary equilibrium that is optimal against each label's unilateral deviations from every state. Its active decisions therefore form a Markov-perfect current-self equilibrium in this subclass.

This uses established discounted stochastic-game machinery. Sorin's author-hosted chapter, *Discounted Stochastic Games: The Finite Case*, section 2, pp. 54–55, gives the finite-game stationary-existence result and a fixed-point proof; those pages were inspected. The following argument spells out the evaluator-label specialization, including evaluator-specific discounting. No new general equilibrium-existence theorem is claimed. [Primary mathematical text](https://perso.imj-prg.fr/sylvain-sorin/wp-content/uploads/sorin-pub/03.Stoc05.pdf).

Fix all labels other than tau to stationary strategies. Tau then faces a finite discounted Markov decision process, with a dummy choice in inactive states. Its Bellman operator on value vectors is

$$({\cal T}_\tau V)(s)=\max_{a_\tau\in A_\tau(s)}
E_{a_{-\tau},s'}[r_\tau(s,a,s')+\beta_\tau V(s')].$$

This is a beta_tau contraction in the sup norm: each action's continuation difference is bounded by beta_tau times the value difference, and taking maxima preserves that bound. It has a unique bounded fixed point. Choosing a maximizing action at each state is optimal even against history-dependent deviations, as follows by iterating its Bellman inequality and sending the bounded discounted terminal remainder to zero.

The optimal value depends continuously on the other labels' stationary mixed strategies. One way to see this is to compare the two Bellman fixed-point equations: the difference is bounded by the one-step parameter difference divided by 1-beta_tau. The maximizing-action correspondence therefore has a closed graph and nonempty compact convex mixed-action values. Taking its product over states gives tau's correspondence of stationary policies optimal from every state. The product over all finitely many labels is an upper-hemicontinuous correspondence on a compact convex product of mixed-strategy simplexes, with nonempty compact convex values. Kakutani's theorem supplies a fixed point. At that profile every label solves its own discounted control problem against the others; the dummy actions prevent control by inactive founders.

Bounded rewards and strictly subunit discounts do substantial work. No corresponding assertion is made for arbitrary undiscounted history utility, infinite goal menus, hidden beliefs or unbounded physical state. A finite-state approximation also needs an approximation argument; existence for the approximation alone does not prove existence or peace in the original model.

## 4. Behavioral replication versus equilibrium transfer

Note 010's conditional replication result matches one policy profile's full history law. That is sufficient for founder welfare at that profile but does not automatically preserve incentives. A revocable fixed-utility delegate can reproduce a modified controller's planned action and then prefer to override it at the final production choice. Note 011 makes that counterexample explicit.

A sufficient condition for full equilibrium transfer is a correspondence between the two games' states, active evaluators, information and feasible deviations that preserves transition laws and each evaluator's ordering of all resulting continuation lotteries. In the finite discounted subclass, an especially transparent case is an action/state isomorphism, equal discount factors for corresponding evaluators, matching transitions and rewards related by a fixed positive affine transformation for each evaluator. The additive reward constant must apply at **every** time, including absorbing states, so that it changes the infinite discounted value by a strategy-independent constant.

For such an isomorphism, every strategy profile and every unilateral deviating strategy has a counterpart. Values transform as alpha_tau V_tau+c_tau/(1-beta_tau), with alpha_tau>0. All best-response inequalities are preserved, so current-self equilibria transfer in both directions. If the physical game terminates rewards at a random time, adding a per-active-period constant is generally not the same affine transformation of complete-history utility; the stated absorbing-state convention avoids that mistake.

This sufficient condition is deliberately stronger than matching realized behavior. A hardwired delegate may have fewer deviations than a modified successor; an ordinary revocable policy may have more. One must assess those actual menus. Neither utility modification nor fixed-utility delegation is assumed universally capable of implementing the other.

## 5. Quantitative transfer under small matched model errors

Consider two games on the **same** states, evaluator labels, available actions and public observations, with the same discounts. Let their expected one-step rewards differ by at most epsilon_r for every state/action/evaluator, and their transition laws differ by at most epsilon_K in total variation. Suppose both reward systems have absolute value at most M. Define TV(P,Q)=(1/2)sum_s |P(s)-Q(s)|.

For any corresponding history-dependent policy profile, including a unilateral deviation, a given evaluator's values differ by at most

$$B_\tau=
\frac{\epsilon_r}{1-\beta_\tau}
+\frac{2M\beta_\tau\epsilon_K}{(1-\beta_\tau)^2}.$$

Proof by coupling: while the two state/action histories agree, use the same policy random draws and a maximal coupling of the next-state kernels. The probability that histories have diverged by period t is at most t epsilon_K. An expected period reward then differs by at most epsilon_r+2M t epsilon_K. Sum the geometric series and its time-weighted derivative. The bound can be loose when t epsilon_K exceeds one, but remains valid. If rewards are in [0,M], the divergence term's factor 2M can be replaced by M.

If a profile is an exact current-self equilibrium in the first game, no unilateral evaluator deviation gains more than 2B_tau in the second: its deviating and equilibrium values each shift by at most B_tau, while their original difference was nonpositive. The same argument applies from every public state/history. Thus it transfers as an approximate equilibrium with explicit error.

For a pure stationary equilibrium, suppose every alternative pure one-step action at every active state has an original gap greater than 2B_tau. Each perturbed one-step gap remains positive. The finite discounted control argument then rules out every multi-step deviation, so the profile remains an exact equilibrium. Mixed equilibria generally have zero gaps among supported actions and need not remain exact after an arbitrarily small perturbation.

These statements do **not** apply when a small resource change adds/removes an affordable action, when a new rollback or binding delegate becomes available, or when observations or active preferences are changed without a matching error model. Near a feasibility boundary those are changes in the strategic menu, not merely small numerical changes in a fixed kernel. They are also stronger assumptions than closeness of two utility functions alone, which note 010 shows can coexist with a large strategic loss.

## 6. Finite-horizon counterpart and failure boundaries

For at most H transitions, a common terminal utility in [0,1], terminal-score error at most epsilon_u and per-step transition TV error at most epsilon_K, the same coupling gives value error at most epsilon_u+H epsilon_K. Exact equilibrium therefore transfers with unilateral gain at most twice that quantity under the same information/action correspondence. If stage rewards accumulate, their timing and bounds must be included rather than substituting this terminal-only formula.

Compactness and attainable maxima cannot be dropped casually. For example, let a late original A choose a perfectly implemented split parameter alpha from the open interval (0,1), with payoff alpha and an opponent having zero reservation and accepting every positive own share. Keep an affordable finite-cost Attack option with zero deliverable output; every split beats it. Every proposal is feasible but A has no maximizing proposal: it can always increase alpha. That protocol has no optimal proposal at the decision. Closing the menu, defining endpoint acceptance, imposing a finite verified template set or explicitly using approximate equilibrium are different repairs. None should be frozen into C1 merely because it makes one proof easier.

The finite/discounted role construction establishes that repeated utility changes can be modeled without scoring them by the newly installed utility or assigning everlasting control to the founder. It supplies neither a convergence theorem for goals nor a general physical implementation of those changes. Those remain substantive research questions.
