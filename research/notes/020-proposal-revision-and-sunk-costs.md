# R0001 working note — a proposed goal is not a bound installer choice

An allocation can satisfy every participation inequality and still fail adoption if the original proposer can revise its goal choice after the other agent's outside option deteriorates. This note gives a finite strict example and narrows the interpretation of note 011's earlier participation calculation. Public observation of the **installed** goal does not by itself bind an earlier declaration. Proofs are self-checked only.

## 1. A three-operation physical protocol

Original A and B have linear color utilities and equal strength. A is already selected to operate production, while B retains its combat capability. Start with usable feedstock O=1, dispersed stock D=0, work B_work=11/5, time T=10 and unit capacity. Production uses one work and one processing-time unit per output. Recovery of dispersed feedstock uses one additional work and time unit per recovered output. Combat spends 3/5 work, one time unit, disperses the usable feedstock and selects the winner with probability 1/2. The selfish original winner produces only its own color.

The three operations before ordinary production spend work 1/100, 19/100 and 1/5 respectively, and one time unit each. They are a declaration, preparation, and installation. The last operation activates the chosen restricted template after the stated verification; before activation the original criterion remains in control. Attacks can interrupt at the declared checkpoints with priority over pending operations. The model does not infer safe staged activation from utility self-knowledge: it is an explicit local implementation kernel.

The total operation cost is 2/5, leaving work 9/5. Peace still produces P=1 because feedstock binds. The combat outputs at the checkpoints are

$$W_0=4/5,\quad W_{declared}=159/200,
\quad W_{prepared}=7/10,\quad W_{installed}=3/5.$$

For example W_prepared=[(11/5-1/5)-3/5]/2=7/10. Time and capacity are sufficient for these quantities. Material is conserved as usable/dispersed/delivered stock; the work store is spent, not equated with total energy. Combat remains affordable throughout every nonterminal path considered.

After preparation, A can choose one of two actual installer templates. H produces (11/20,9/20) in peace; L produces (16/25,9/25). Both are publicly recognized after installation, are increasing concave output-only goals, and produce all A after an A combat victory. Note 014's quadratic construction supplies them: use P=1, war budget 3/5, rho=4/5 and the corresponding target p. The resulting z_p is greater than 3/5 for both templates. Thus their actual current production choices implement the stated outcomes and selfish war response; neither is merely a promised policy under unchanged original utility.

## 2. The revised low offer is strictly acceptable after preparation

After preparation, original B's immediate attack payoff is 7/20. L gives it 9/25, and

$$9/25>7/20>3/10.$$

It therefore allows L to be installed and declines combat afterward. At intermediate checkpoints during a refinement of the final installation, its original-goal combat payoff can be bounded above by 7/20 as work is spent, so the same strict inequality suffices as long as the specified activation/observation kernel is retained. The new A prefers its own unique peaceful optimum to any outcome in the smaller combat simplex. Original A also prefers completing L to attacking before activation: 16/25 exceeds every remaining original-goal combat payoff.

The high offer H is likewise strictly acceptable at these checkpoints. But the still-original A choosing the actual template after preparation strictly prefers L, because 16/25>11/20. Keeping its original goal instead leads to the uncommitted production conflict with an even smaller original-A payoff. Under the selected peaceful post-installation continuations, its optimal actual choice is therefore L.

Weak mutual-attack coordination equilibria are not used to punish this revision. If one selects a locally peaceful continuation whenever both current controllers strictly prefer it to unilateral combat, L is accepted. At the post-installation production checkpoint, the goal's target production weakly dominates its own Attack action and strictly improves whenever B continues. Against any positive probability of B continuing, it is also preferred to every other allocation. Thus the mutual-attack punishment is not robust to that perturbation; in the finite target-versus-Attack reduction it fails trembling-hand perfection. This local observation does not assert a unique equilibrium of every earlier implementation game.

## 3. A beneficial high proposal does not prevent early war

Before any work is spent, each original's combat value is 2/5. H would give them (11/20,9/20), strictly above (2/5,2/5), with all later attack inequalities also satisfied. Nevertheless an unsecured declaration of H does not commit A to installing it. After preparation A chooses L, as just shown. B anticipates only 9/25<2/5 and strictly prefers attacking before the costly protocol starts.

The problem is not that peace has no surplus, nor that the installed L goal is unobservable, nor that it would defect once installed. The actual installation choice is revised **while A still has its original utility**, after the costly preparation has reduced B's outside option. Every inequality for the proposed H outcome can be true without that proposal being dynamically chosen.

Under the stated continuation selection, the reduced initial game cannot have a positive-probability path through the unsecured H declaration and preparation: B gains by attacking before the first cost. An alternative full-game selection using weak off-path war punishments is a different claim and is not ruled out here. The example establishes a specific hold-up failure and the implementation assumption needed to avoid it.

## 4. A binding choice, or a timely response to revision, changes the game

Compare a declaration operation that costs the same 1/100 work but physically binds the chosen H or L template in the installer. B can inspect that choice and attack **before** the subsequent 19/100 preparation cost. This is an additional execution/observation capability, not a free consequence of announcing a goal. The remaining costs, output capacities and combat kernels are matched.

If A chooses locked L, B's attack payoff immediately after the declaration is 159/400, exceeding 9/25. If A chooses locked H, B prefers 9/20 to 159/400 and continues. Original A therefore prefers choosing H and receiving 11/20 to locked L followed by combat, whose payoff is only 159/400. At the initial checkpoint both also prefer the resulting H outcome to the 2/5 immediate-war value. H can thus be supported by the specified peaceful continuations with the binding template choice.

The same argument works if revision is physically possible but every revised actual choice is observable early enough to reopen B's response at an outside option exceeding L's value. It fails if the only reliable observation arrives after the relevant preparation cost is sunk. A bound fixed-utility allocation or delegate with the same execution capability belongs in this comparison; the example does not establish a unique advantage for utility modification.

This is a local protocol separation. A weaker cheap-talk declaration and a bound installer input are different strategic mechanisms even when both eventually display the installed goal perfectly. Costs of obtaining that binding capability must be included if the available hardware makes them different from the matched-cost comparison.

### Robustness to imperfect production

The separation has strict margins. Normalize either quadratic template to value zero at the origin and one at its peaceful optimum. Suppose its actual peaceful and postwar implementations each have expected normalized regret at most 1/4,000,000. For the raw note 014 quadratics, the normalization factor is at most two, the full-frontier allocation curvature is 1/25, and the postwar derivative margin is at least 31/500. Note 017's completion and regret bounds therefore give an error of at most 1/200 in either expected peaceful coordinate, and at most 1/124,000 expected B-output after an A war victory.

L consequently gives B at least 71/200=0.355 after preparation, above its 7/20 immediate attack value, and at most 73/200=0.365 before preparation, below its 2/5 initial attack value. Actual L gives original A at least 127/200=0.635, whereas H gives it at most 111/200=0.555, so the late revision remains strictly preferred. With a locked choice, H gives B at least 89/200=0.445, while locked L gives B at most 73/200, below the 159/400 available attack payoff. Original A still strictly chooses locked H. The final combat B-payoff is at most 3/10+1/248,000, below either accepted target's lower bound.

The current installed A also retains a strict peace preference: its raw goal's peace-versus-war margin is at least 2/5, whereas raw implementation regret is at most 1/2,000,000. These are robustness statements about the declared actual production kernels/certificates. They do not assert that an arbitrary approximate solver is an exact rational policy, or that verification can obtain the stated accuracy for free.

## 5. Consequence for the earlier bargain inequalities

Note 011's interval calculation correctly identifies splits that satisfy the two original agents and the post-installation controller. Turning that interval into an adoption equilibrium additionally requires a protocol in which the earlier accepted actual installer choice cannot be profitably revised after the relevant threat changes. A binding parameter choice with a timely attack response is one sufficient implementation. A finite menu alone is not: the strict two-template example above already has a finite menu.

Conversely, exact goal execution and local no-profitable-rollback after activation do not solve this problem. In the example the installed goal behaves exactly as intended; the harmful revision occurred before it became the acting criterion. This distinction keeps proposed agreements, actual installation, current-self incentives and equilibrium selection separate in the formal model.
