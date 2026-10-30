# Model contract — draft for CG-01

This is an interface and a starting construction, not a solved dynamic game. CG-01 must instantiate the timing, transition parameters, information structure, and equilibrium concept before CG-R001 claims dynamic results. Elementary static benchmarks are in [notes/000-baselines.md](notes/000-baselines.md).

## 1. Agents, histories, and evaluation

Let a history h record physical states, messages, actions, outcomes, and utility installations. Agent i at time t has utility U_i^t over complete histories, power a_i, a policy, beliefs, and a permitted modification map. Its own utility and modification options are known to it. Choose a finite horizon or a discounting/boundedness condition that makes expectations well-defined.

A prospective modification m is evaluated by the incumbent:

$$
V_i^t(m\mid h)=\mathbb E[U_i^t(H)\mid h,\operatorname{do}(m)].
$$

The modification changes the subsequent policy and possibly U_i^{t+1}. That successor evaluates its later choices by its own current utility. For reporting, also compute founder welfare E[U_i^0(H)]; do not confuse this external comparison with an assumption that the founder remains in control.

Specify whether utility values deaths, successor behavior, control, physical outputs, resource stocks, modification events, or the route to an outcome. Knowledge of transition probabilities is not knowledge of future random realizations. Self-transparency does not imply another agent can inspect or verify the utility.

## 2. Physical state and transition kernels

A useful state interface is

$$
z=(\mathbf m,\ell,\chi,\Theta,B,K,t),
$$

where m describes material amounts/composition, ell their spatial distribution, chi their organization or functional condition, Theta the thermal state, B available useful work relative to a declared environment, K productive infrastructure/capacity, and t time. B is an exergy/work budget, not total energy or utility. It may be derived from the fuller state rather than treated as an independent quantity; a model must avoid inconsistent or duplicate accounting.

Define separate stochastic kernels for combat C, ordinary agreement P, and modification-based agreement M:

$$
K_j(dz',d\mathbf U',d\mathbf a',d\tau\mid z,\mathbf U,\mathbf a,\text{actions}),\quad j\in\{C,P,M\}.
$$

Combat may disperse material, mix or transform it, damage organization and infrastructure, expend useful work, create thermal recovery delays, and kill or disable agents. Consensual action may preserve those structures while changing allocations, control, or objectives, but it must pay its own communication, computation, verification, and installation costs. Forced utility rewriting after defeat is a distinct possible combat outcome, not consensual corrigibility.

Track matter/energy flows across the chosen boundary, losses of available work, and unrecovered resources. Heating does not destroy energy; whether it reduces useful work depends on the initial state and reference environment. Material disorganization need not be captured by one entropy number. Background for exergy accounting is [L07](LITERATURE.md); any numerical physical bound requires its own derivation and assumptions.

Do not assert K_C is always physically inferior. Specify a class of destructive mechanisms and the parameter region in which dominance might hold. Include expensive compromise, recoverable debris, different time horizons, heterogeneous goal requirements, and combat that preserves most infrastructure as boundary cases.

## 3. A minimal recovery model to instantiate

For a first tractable physical model, partition a tracked material stock into usable O, dispersed D, and transformed Z, all in consistent material units. Add useful-work budget B, capacity k, and a remaining time budget T. Let x_D and x_Z be recovered amounts and y final useful output. A candidate production frontier is the linear program

$$
Y(O,D,Z,B,k;T)=\max y
$$

subject to

$$
\begin{aligned}
&0\le x_D\le D,\quad 0\le x_Z\le Z,\quad y\ge0,\\
&y\le O+x_D+x_Z,\\
&w_Dx_D+w_Zx_Z+w_y y\le B,\\
&t_Dx_D+t_Zx_Z+t_y y\le T,\\
&y\le kT.
\end{aligned}
$$

Here w terms are work per unit and t terms are time per unit; coefficients are nonnegative and the model must ensure boundedness. The additive time constraint represents a chosen sequential-processing abstraction. k is an additional capacity bound, not a claim that every process has this architecture. Dispersion distance, transformation severity, and cooling can change the recovery coefficients or available T.

Combat and compromise produce different distributions of these inputs and incur their own delays before recovery. Material fractions can change categories without disappearing; imported/exported stock must be explicit. Map power expenditure and damaged productive capacity into the transitions rather than charging the same loss a second time as an arbitrary utility penalty.

**First research target:** solve informative parameter regimes of this frontier, derive which physical changes enlarge or shrink the bargaining set, and determine whether these predictions reduce to a scalar cost or exhibit state/horizon-dependent effects that such a surrogate misses. This target is OPEN, not satisfied by writing down the LP.

## 4. Power and stochastic combat

A two-agent reference contest is

$$
q_A=\frac{a_A^r}{a_A^r+a_B^r},\quad q_B=1-q_A,\quad r>0,
$$

with nonnegative powers and a nonzero denominator. It is a toy specification, not a physical law. Start with r=1 if useful. Define casualties, surviving control, destruction, and recovery conditional on the outcome; the victory probability alone does not specify the combat kernel. Future variants can include first-move advantage, costly power investment, partial victories, and coalitions. A multi-agent winner-take-all contest is only one possible extension.

## 5. Timing and persistent attack options

Use proposal, response/verification, implementation, and continuation stages. At each nonterminal decision point where an agent remains capable, include an attack option in its physical action set. Allow attack during bargaining and following agreement. Model interruption opportunities during implementation; atomic installation is a separate idealization with its own attack boundary.

Rejection can lead to another offer, inaction, exit where physically possible, or combat. The disagreement continuation must be solved or specified, not automatically equated with war if a better peaceful fallback remains available. A last-resort threat is a role in the game, not a lexicographic prohibition on initiating conflict.

Choose an explicit solution concept: for example subgame-perfect equilibrium under complete information, or a specified sequential equilibrium/belief model under private information. Report multiplicity and off-path attack incentives. An existence proof for an acceptable division is not an equilibrium proof for this protocol.

## 6. The mechanism comparison

Hold the physical opportunities and information fixed where possible and compare:

- unchanged terminal utilities with flexible policies, trade, and resource allocation;
- unchanged utilities with verifiable policy commitments or delegation;
- voluntary utility modification, reciprocal updates, or a merger with an explicit successor objective;
- combat and any noncombat disagreement continuations.

Verification, enforcement, rollback, and atomicity costs belong to the implementation technology. Strong commitment controls must be labeled if they have abilities other agents lack. Distinguish a physically executable attack that an installed objective never selects from an action removed from the physical game. Model further self-modification instead of silently treating the first installed utility as permanent.

## 7. Freezing and pro-combat preferences

A finite freezing model is

$$
U_i^0(H)=G_i(H)-\kappa_i D_i(H)+\beta_i C_i(H),
$$

where D_i specifies the type and occurrence of disfavored utility change, C_i is a declared combat/process feature, and kappa_i and beta_i are preference coefficients in that agent's utility units. Define whether changes caused by capture, successor creation, code refactoring, or representation changes count. Penalties are evaluated under the incumbent criterion; a successor deleting its penalty does not erase it from the original evaluation.

Do not compare or average unrelated agents' cardinal utilities without a normalization or explicit aggregation rule. In particular, a positive affine recoding is not by itself a change of expected-utility preferences.

Also examine hard admissibility constraints and lexicographic goal-preservation priorities. These are different mathematical preference classes, not simply a large finite kappa inside a bounded real-valued expected-utility theorem. Compare terminal-goal freezing with policy freezing and with contingent commitments chosen for their strategic effects.

Combat appeal can also come from direct destruction preferences, control/status, relative rather than absolute outcomes, survival or identity constraints, indivisible goals, or a first-move advantage. Determine whether the effect survives all available peaceful alternatives, not only a selected utility-update scheme.

## 8. Long-run and population models

For voluntary adaptation, compare the complete continuation value of keeping versus relaxing a freezing rule under the current utility, including future opportunities, commitment benefits, exploitation, and changes in power. Distinguish one-time versus recurrent modification costs and finite, discounted, and average-reward horizons.

For a separate population model, let x be the frequency of a flexible type and define fitness F_M(x) and F_F(x) from the actual interaction game, material budgets, survival, maintenance, and a specified reproduction or imitation process. A possible baseline is

$$
\dot x=x(1-x)[F_M(x)-F_F(x)].
$$

This equation defines a proposed selection dynamic; it does not establish the sign of selection. Derive fitness rather than identify it with subjective utility. Analyze rare-type invasion, reciprocal invasion, coexistence, and boundary stability. Add mutation, observation limits, or assortment explicitly when used. Freezing can persist through commitment value, niche structure, or absent mutation even when another type would be materially efficient in some encounters.
