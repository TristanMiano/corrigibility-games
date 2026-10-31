# R0001 working note — strength investment can undo a static peace result

The seed's strength parameter need not be exogenous. This note gives an exact finite-stage model in which every realized strength profile admits a stable peaceful split, yet competition to obtain a larger share consumes enough productive work to make an earlier attack profitable. The first comparison deliberately grants **fixed-utility** agents an enforceable split mechanism; it is not a claim that utility modification is necessary. Proofs are self-checked only.

## 1. Resource and timing model

There are n>=2 original agents with linear color utilities x_i, equal initial strength a>0 and a remaining common production-work budget R>0. Strength is measured in units in which one unit of deployment work adds one unit of effective strength. The initial positive communication/verification overhead has already been spent and is recorded before this state. Feedstock and deadline capacity are ample enough that remaining work binds final output.

Each agent chooses investment e_i in [0,b], where b=(n-1)R/n^2. Investment deploys a stock of already fabricated reserve actuators, consumes e_i useful work and a corresponding positive processing time, and raises its strength to t_i=a+e_i. Reserve and deployed actuator material remain on the physical ledger; spent work is dissipated or tied up in equipment that cannot be profitably recovered before the task deadline. The actuator stock supplies the stated finite upper bound. The production feedstock is separate. Thus total production budget after investment is

$$P=R-E,\qquad E=\sum_i e_i,$$

and P>=R/n>0 on the entire action space. This convenient hardware cap lies strictly above the interior equilibrium investment derived below. The result does not require permitting unbounded military investment or an exhausted-battery exception to combat availability.

There are two decision checkpoints. At the first, every agent may Attack or choose its deployment action. If any attacks, the pending deployments are interrupted before expenditure and a global contest occurs at the original equal strengths. Otherwise the finite deployment operation completes, and the second checkpoint begins. This is an explicit time-resolution assumption: new observations and attack decisions occur at those checkpoints. Subdividing deployment into additional observable stages is a different game and may add further preemption.

At the second checkpoint, agents can use the available split mechanism or attack. The split allocates

$$p_i=\frac{t_i}{T}P,\qquad T=\sum_j t_j.$$

The mechanism requires actual enforceable allocation technology; a revocable recommendation is not enough. It leaves each agent physically able to interrupt with combat. Combat victory probabilities are t_i/T and the selfish winner produces only its own color. Its net output is lambda P, for a fixed lambda in (0,1). The first-checkpoint contest instead delivers lambda R, with each agent winning with probability 1/n.

One possible work accounting for lambda is: fighting spends a fraction f>0 of the remaining production-work reserve and disperses usable feedstock; each recovered unit needs w>0 additional work, and production needs one. Then lambda=(1-f)/(1+w). For any specified 0<lambda<1, choose w=(1-lambda)/(2lambda) and f=(1-lambda)/2. Material is relocated to dispersed stock, not destroyed. The finite deadline and capacity can be chosen to leave work binding on every route; positive combat and recovery times must be included. This is an engineering abstraction, not a calibrated law of warfare.

For every realized positive t and P, each original strictly prefers the split t_i P/T to unilateral combat t_i lambda P/T. Select this peaceful continuation at the second checkpoint. Weak simultaneous-attack equilibria remain available there. The allocation mechanism, its observation technology and this continuation selection are stated assumptions throughout the calculation.

## 2. The unique investment equilibrium conditional on no early attack

Let K=R+na. Since P=K-T, the original payoff from investment is

$$u_i(e)=\frac{t_i}{T}(K-T)=\frac{K t_i}{T}-t_i.$$

This is the usual proportional contest payoff with prize K and effort t_i, restricted here to a positive baseline and a bounded deployment range. L17's inspected standard specialization supplies the nearest explicit comparison. The contest best-response machinery is conventional; the local additions are the resource interpretation and the earlier physically available attack option. [Primary manuscript, sections 2 and 3.1](https://ueaeprints.uea.ac.uk/id/eprint/19084/1/GeneralizedTullockContest.pdf).

Holding other investments fixed, its first and second derivatives are

$$\frac{\partial u_i}{\partial e_i}
=\frac{K(T-t_i)}{T^2}-1,$$
$$\frac{\partial^2 u_i}{\partial e_i^2}
=-\frac{2K(T-t_i)}{T^3}<0.$$

Every player's investment problem is strictly concave. Any pure equilibrium must be symmetric. If e_i>e_j, then t_i>t_j and i's displayed marginal is strictly below j's. At an optimum with e_i>0, i's marginal is nonnegative (zero in the interior, nonnegative at the upper endpoint). At an optimum with e_j<b, j's marginal is nonpositive. These endpoint conditions contradict the strict marginal ordering. Thus all investments coincide.

Solving the symmetric first-order condition, including the zero boundary, gives the unique pure equilibrium

$$e^*=\max\left\{0,\frac{(n-1)R-na}{n^2}\right\}.$$

The positive solution lies strictly below b. When R>na/(n-1), the resulting output and each original's payoff are

$$P^*=\frac{R+na}{n},\qquad
u_i^*=\frac{R+na}{n^2}.$$

When R<=na/(n-1), investment is zero and P*=R. No independent mixed investment equilibrium has additional support: for any distribution of the other agents' investments, the expected own payoff remains strictly concave, so the own best response is a single investment. Any mixed equilibrium is therefore pure and is the one just identified.

The peaceful equilibrium can spend nearly (n-1)/n of the available productive work on strength as R/a grows. This loss is not caused by combat occurring on that continuation; agents expend work to obtain a larger share of peaceful production. The equal-strength allocation at zero investment would instead deliver R/n to each, but zero investment is not a best-response profile in the positive-investment region.

## 3. Earlier combat can be preferred to the investment race

The first-checkpoint Attack payoff is lambda R/n. Thus the positive-investment continuation is preferred to an early unilateral attack iff

$$\lambda\le\frac{P^*}{R}
=\frac1n+\frac aR.$$

Strict inequality gives strict preference for continuing with the selected investment equilibrium; the reverse strict inequality makes early combat profitable even though the final split strictly beats combat at **every fixed realized strength profile**.

Under the stated simultaneous first-checkpoint protocol, the reverse strict inequality is stronger than a failure of one candidate equilibrium: **every Nash equilibrium of the reduced first-checkpoint game has combat probability one.**

Proof: suppose an equilibrium has positive probability of no attack. Then every agent chooses an investment with positive probability. Conditional on all others also investing, the strict concavity above gives that agent a unique optimal investment. The branches on which someone else attacks give the same original-strength war payoff regardless of its own action. Consequently the conditional investments must be a Nash equilibrium of the investment subgame, hence e_i=e* for all i. But lambda R/n>u_i* then makes Attack strictly preferable whenever the others all invest, an event of positive probability. This contradicts the positive probability of own investment. The proof uses independent behavioral randomization in Nash equilibrium; a mediator or binding correlated investment agreement changes the mechanism.

For n=2, R=1, a=1/10 and lambda=4/5, e*=1/5 per agent, P*=3/5, and each gets 3/10 by continuing. Immediate combat gives 2/5 each in expectation. At the final strength profile a peaceful split still gives 3/10 versus only 6/25 from attacking then. The harmful incentive is to attack **before** the wasteful strength competition, not a failure to recognize the later bargaining surplus.

At the equality boundary, early attack and the selected investment continuation tie. With lambda below the threshold, the all-invest e* profile is a peaceful equilibrium of the reduced game, but weak war equilibria remain. This note does not import the trembling-hand selection result from a simpler two-action matrix into this richer action space.

## 4. A weaker uncommitted-production control

If the final allocation cannot be enforced and the original-agent production game instead has the war continuation from note 010, its expected payoff after investment is lambda u_i(e). Multiplication by the common positive lambda leaves the investment best responses unchanged. In the positive-investment region, immediate original-strength combat gives lambda R/n, strictly more than lambda P*/n. The same conditional-investment proof then rules out an equilibrium with positive probability of avoiding the first-checkpoint conflict, under that selected final war continuation.

This control makes explicit what the enforceable split accomplished: it can eliminate the later production conflict but need not eliminate the earlier competition for strength. Both controls retain ordinary allocations and combat in their stated feasible menus. Their different execution capabilities are not attributed to a difference in utility labels.

## 5. Alternative mechanisms and the remaining adoption question

A credible agreement limiting deployment can preserve productive work while leaving original combat capabilities intact. If all e_i are held at zero, the proportional split gives R/n and strictly beats the original-strength combat value lambda R/n. Whether such a deployment cap can be monitored and enforced at a lower cost than its gains is a new implementation question. An announced promise does not change the unilateral derivative in section 2.

Likewise, if all acting agents actually share a strictly increasing, strictly concave balanced production goal, and every production operator has the same feasible set, increasing one's control weight no longer changes the chosen allocation. Investment then only reduces total feasible production, so zero investment is preferred. But original agents must decide whether and how to create that shared-goal state. A successful endpoint does not settle sequential adoption, deception, verification, rollback or founder protection; notes 011–013 show why those steps matter. The same physical hardware and credible deployment restrictions must be offered to unchanged-utility controls when available.

The strength-proportional split rule is an explicit protocol here, not a permanent invariant of the minimal contract. Other bargaining selectors, strength depreciation, productive dual-use investment, private reserves, intertemporal security or external opponents can change the investment game. The result isolates a missing mechanism in a static strength model: improving a fixed-state bargaining outcome need not improve the preceding incentives to alter that state.
