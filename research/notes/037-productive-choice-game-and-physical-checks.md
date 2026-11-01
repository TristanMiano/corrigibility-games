# R0002 working derivation: a productive choice game with retained combat

**Retained staged construction with a known physical-menu limitation; contributing-agent self-check.** This note connects 036's certificate to actual goal choice, proposal, installation and production. It uses a finite bargaining game with continuous goal parameters and broad output contracts. Its selection and timing assumptions are explicit; later sections test renewed update opportunities rather than treating an initial Keep choice as permanent freezing by definition. The final integrated claim is R205/[E3](../models/E3.md), with the separate scope below.

**Later audit scope:** 045 supplies a profitable public resource-burning deviation outside this staged action space. Thus this note's algebraic last-window result is preserved, while its 20-slot physical prototype is not an unrestricted physical equilibrium theorem. The guarded construction in 046/049 repairs the identified preservation problem under explicit additional technology and timing assumptions.

## 1. Contracts and current selves

Each agent begins with R_i units of its valued project. Net outcomes x,y subtract these initial constants, so original utilities may be written x,y without changing preferences. A's public goal parameter is lambda in [0,1), with current utility x+lambda y; B may install y+mu x, mu in [0,1). The original parameters are both zero. Positive parameters genuinely change lottery preferences on the common outcome domain.

Hidden simultaneous efforts e_i in {0,1} consume c_i units of the agent's existing project material. They affect a common reactor's success probability: p_00=0, p_10=p_01=a, p_11=b. Success yields Y units of new project material; failure yields none. Set V=bY, Delta=b-a, D=Delta Y and C=V-c_A-c_B. A success/failure contract specifies g_i^0,g_i^1, independent of hidden effort. Budget-balanced contracts satisfy g_A^k+g_B^k=kY; waste and physically financed penalties may reduce these sums. Final project output is R_i-c_i e_i+g_i^k>=0. Collateral constraints must hold in each branch, not only in expectation.

Write d_i=g_i^1-g_i^0. At mutual effort the incentive conditions are

$$\Delta(d_A+\lambda d_B)\geq c_A,\qquad
\Delta(d_B+\mu d_A)\geq c_B.$$

A conditional output allocator enforces g after the terminal success observation. It cannot observe effort or compel it. Installing a goal is a different physical operation, publicly verified within the declared parameterized template family. Public statements alone do not bind goals or effort.

The default allocator gives success shares t_0 and 1-t_0 and makes no failure transfer. Take the strict class from 036: aY<min(c_A,c_B), c_A+c_B>D, C>0, and c_A/V<t_0<1-c_B/D. Let r_A=t_0V-c_A, r_B=(1-t_0)V-c_B and

$$\lambda_0=\frac{c_A/D-t_0}{1-t_0}\in(0,1).$$

For lambda<lambda_0, A strictly shirks under the default even when B works; solitary effort is also unprofitable. Thus the default has the unique effort outcome (0,0), for every mu in [0,1). For lambda>lambda_0, mutual effort is a strict equilibrium for every such mu. The selected continuation uses mutual effort when it is incentive compatible. The remaining mutual-shirk equilibrium is reported separately.

## 2. A solved last public-update window

First solve the final public-update window. A chooses a public lambda, including zero. B then may retain its goal or install a nonnegative mu, and propose any available contract, lottery or consensual successor arrangement. A can accept or use the default. Both retain Attack throughout installation and execution. Unilateral public reprogramming requiring another full verification window cannot fit after this last window; private changes still require current-self approval and are not assumed publicly verified. Section 5 discusses earlier windows.

B's own change precedes its binding proposal. Otherwise it could promise a goal and decline installation after the allocator was activated. After actual installation, the new B chooses its proposal using y+mu x. This timing is part of the mechanism and will be checked during physical implementation.

Assume every actual continuation has E(x+y)<=C. This is proved for the physical instance below, not imposed as an abstract claim about all technology.

**High-lambda branch.** If lambda>lambda_0, rejection supplies the efficient default Q with expected net outputs (r_A,r_B). Every allowed nonnegative B goal preserves this default's effort incentives. By 036's certificate, every arrangement accepted by A has E x>=r_A, so original B gets at most r_B. Keeping its original goal and executing the default attains that upper bound. A's original payoff is r_A>0. The same reasoning covers arbitrary accepted output lotteries and further consensual goal changes within the physical opportunity class.

**Zero-lambda branch.** If A keeps its original goal, it can reject to net zero. B can sometimes attain the entire cooperative surplus C by first installing a goal that makes its effort incentive compatible, then offering a contract with original A's expected net payoff zero and strict effort incentives. Original A accepts at indifference. Since accepted contracts have E x>=0 and E(x+y)<=C, no proposal can give B more than C. Thus this implementation solves B's enlarged optimization, including ordinary penalty contracts and lotteries: A's payoff is zero, B's C. This off-path B modification is itself a valid current-goal adoption when B prefers C to its available unchanged-goal outcomes.

Consequently A strictly prefers a genuine high-lambda installation to remaining original in this last-window comparison. Its gain is evaluated by its original project output r_A, not by the installed utility's numerical value. Equality at A's off-path contract acceptance remains a selected tie; on the constructive default both effort incentives and A's initial adoption can be strict.

**Intermediate-lambda branch.** When 0<lambda<lambda_0, rejection again gives net utility zero. The upper bound on B's original payoff is C/(1-lambda), attained if a suitable goal and collateralized contract implement

$$E x=-\frac{\lambda C}{1-\lambda},\qquad E y=\frac{C}{1-\lambda}.$$

An installed B with 0<=mu<1 also prefers this offer: under A's participation and the surplus cap,

$$E[y+\mu x]\leq\frac{1-\mu\lambda}{1-\lambda}C,$$

and the displayed efficient offer attains the bound. Hence B has no profitable post-installation proposal revision. Feasibility is checked explicitly in the witness; a general class must include the needed collateral and incentive inequalities. The initial original A rejects these intermediate choices because they give negative net founder welfare.

## 3. Exact witness with finite collateral

Use R_A=R_B=3, Y=10, a=1/10, b=2/5, c_A=c_B=8/5 and t_0=9/20. Then C=4/5, r_A=1/5, r_B=3/5 and lambda_0=5/33. A may choose lambda=1/5; B stays original; expected final project outputs are 16/5 and 18/5. Initial stocks alone give each 3. The changed A's actual current utility at the productive outcome is 98/25 in absolute project units; its net value is 8/25.

For every 0<=lambda<5/33, let B install mu=1/5 and offer success-minus-failure differences

$$d_A=11/2,\qquad d_B=9/2.$$

Put z=lambda C/(1-lambda). Choose

$$g_A^0=-3/5-z,\qquad g_A^1=49/10-z,$$

and g_B^0=-g_A^0, g_B^1=10-g_A^1. These contracts are budget balanced in each outcome and give expected net payoffs (-z,C+z). Changed A's work incentive is at least (3/10)(11/2)-8/5=1/20>0; changed B's is (3/10)[9/2+(1/5)(11/2)]-8/5=2/25>0. All failure transfers are feasible: 0<=z<1/7, so A's largest failure payment is below 26/35, less than its remaining stock R_A-c_A=7/5. B receives rather than pays on failure; success allocations are also nonnegative after actual effort costs.

At lambda=0, B's installation yields original B C=4/5 with original A indifferent at zero, and both subsequent efforts strict. This beats the maximum 2/5 total surplus of the ordinary failure-penalty construction in 036. The initial A instead selects lambda=1/5, activates the efficient default, and protects its own gain 1/5 across B's complete proposal menu. This is the chosen accommodation/safeguard mechanism: sufficient concern for the other agent makes productive effort credible, while the efficient fallback and retained own-project preference protect the founder.

## 4. A finite physical realization and all attack checks

The following is a mechanistic finite-horizon witness, not a thermodynamic law. Initially there are 3 units of each finished project material and 10 units of common feedstock. Calibration effort consumes 8/5 units of the agent's existing project material, transforming it into spent calibration material; its opportunity cost is an actual loss of valued output. The reactor converts the common feedstock into the allocated project materials on success, and into a specified unrecoverable-by-deadline state on failure. Material remains accounted for as products, feedstock or spent/transformed stock. Useful work is tracked separately.

There is an 11-unit productive work store and a separate finite military charge for each agent, sufficient for one conflict operation. Every communication, computation, verification or update step consumes 1/100 unit of productive work and one time slot. A declared implementation uses at most twelve such administrative steps. Reactor execution uses ten work units over two final slots, with an intermediate attack checkpoint. A 20-slot horizon leaves room for calibration and delivery. A concrete state table is still to be checked against this budget; the route must never silently use more steps.

At any nonterminal checkpoint a capable agent can spend its military charge to initiate the strength contest. Both remain capable before terminal delivery, even after productive work is spent. Conflict expends or disables both military charges; their energy is dissipated or left unusable within the episode, rather than becoming an uncounted recovery-work source. With equal strength, either wins with probability 1/2; the loser loses decision authority. Conflict disperses all then-remaining finished project material, damages the reactor, and transforms its feedstock. The transformed feedstock needs a finite 30-slot repair/recovery latency, longer than the remaining horizon. It therefore supplies no project output within this episode. Finished material can be recovered and recolored at one recovery-work unit plus one production-work unit per output unit. Conflict leaves at most 8/11 of the productive work store available for recovery, and recovery also takes positive time.

Thus every checkpoint's winner frontier is bounded by

$$W_h\leq\min\{O_h,\ (8/11)B_h/2,\ k_h(T_h-1)_+\}\leq4,$$

where O_h is the actual remaining finished-material stock and B_h<=11 is the remaining productive work. Spent calibration material and transformed feedstock have their separately specified finite delays. Destroyed useful work is dissipated/degraded, not deleted conserved energy. A surviving x+lambda y controller with lambda<1 produces only x; a surviving y+mu x controller with mu<1 produces only y.

Original A and B therefore get at most 2 from any early attack, below their retained-stock default of 3 and below the productive continuation's 16/5 and 18/5. A with lambda=1/5 gets at most (1+lambda)W_h/2<=12/5 from combat, below its productive value 98/25. B with mu=1/5 in the off-path implementation likewise gets at most 12/5, below its accepted efficient continuation. The other agent's low-lambda criterion values the off-path offer exactly as its stock fallback, 3(1+lambda), which exceeds 2(1+lambda), its maximum combat value. These strict inequalities also deter attacks during their respective installation steps, when the old or new criterion actually in force is used. Later productive work expenditure and shorter time only reduce W_h.

At a deviation that shirks while the other works, the deviator keeps all its own 3 units of project stock and receives a nonnegative expected net transfer in the default witness; it therefore prefers that direct deviation payoff to its combat option. The default's previously checked strict effort incentives consequently remain sufficient when an additional Attack action is offered. Other off-path histories may select combat if it is optimal; no peace claim is made at every arbitrary rejected contract.

For every pure effort profile, expected final total project output is at most 6+C: totals are 6, 6+aY-c_A, 6+aY-c_B and 6+C. Mixtures preserve this upper bound. Budget-balanced transfers do not change it, while actual waste and positive physical costs cannot increase it. Combat yields at most 4, strictly below it. The declared technology offers no additional productive route; a new recovery or production capability would require recomputing the bound. This proves E(x+y)<=C for the net outcomes used above.

The success observation and contract's conditional material routing occur at the final declared physical resolution. Earlier attack opportunities remain; the episode ends only after delivery at the valuation deadline. This is a finite-horizon continuation result, not an assertion that agents lose all agency forever after production. Finer observation during reaction, a longer valuation horizon, or post-delivery battles would enlarge the game and must be rechecked.

## 5. Reconsideration, verification and matched alternatives

The last-window theorem does not make an earlier Keep action a permanent prohibition on later change. If more public update windows remain, keeping now can lead to profitable change later; its value must include that option. With no additional loss from waiting, initial change and later change may tie. At the final opportunity the strict comparison above still applies. A finite repeated-window game needs its continuation and proposal timing solved explicitly before claiming which agent changes first or how quickly.

After a high-lambda installation, a later consensual arrangement evaluated against the same efficient default protects the founder by 036. A later unilateral change that destroys that default must be evaluated using its actual new bargaining continuation, not assumed to preserve the old rejection value. In the solved B-proposer last-window branches, reducing lambda below lambda_0 produces negative founder output under the new proposal and therefore lowers the preceding high-lambda self's utility at the same maximum surplus. Such a change is unattractive. Changing to another high lambda leaves the same output default and gives no strict benefit. This argument is conditional on the proposal rule and declared B-goal class; broader threat preferences and new proposer rights require new checks.

A public template verifier is not a verifier for arbitrary semantics. The rational parameters in the witness have finite descriptions; an implementation must charge their actual verification work and time. Continuous expressions establish parameter regions and conservative output-law bounds, while a finite physical witness uses explicitly representable parameters and contracts. Goal self-knowledge alone supplies none of this public evidence.

The private effort cost must remain unobservable to the output allocator. Project stocks in private facilities enter actual utility and physical accounting, but the allocator observes only the common success signal and its predeposited collateral. A monitor that can verify final private stocks or actual catalyst use adds information and may permit ordinary effort contracts. It is a substantive repair, not already part of the binary-output contract class.

The same output allocator, conditional transfers, ordinary failure penalties, attacks and productive resources are available to unchanged-goal agents. Observable sequential effort can repair their incentive problem. A binding delegate that reproduces a changed goal's complete effort policy at equal cost ties the goal-change route; cheaper or more reliable delegation may displace it. Such a policy commitment is stronger than the output allocator specified here and must be labeled when added. Equal-cost replication preserves this result's voluntary-change interpretation and limits claims of unique technological advantage.
