# R0001 working note — selection depends on what offspring inherit

The essay's population intuition requires a fitness and transmission model, not just a bargaining advantage. This note adds an explicitly restricted population process to the finite E2-U encounter. It gives counterexamples to universal elimination of freezing and separates an individual's objective, its reproduction and the frequency of its former goal type. These are self-checked calculations for a renewal population, not a model of all agents sharing one indefinitely evolving universe.

## 1. Encounter, fitness and birth assumptions

Each pair receives the finite physical encounter from note 010, with equal initial strengths, total peaceful output one, initial war output 27/100, the specified positive operation costs and the selected peaceful continuations when a G-controller is present. Either capable agent retains Attack at the relevant checkpoints. Roles A and B are independently assigned with equal probability. Goals and the finite menu are public. The initial types are:

- R: own-color linear utility and zero intrinsic penalty for the allowed change to G.
- K: own-color utility with a finite initial change penalty kappa=1/5. In the specified encounter this exceeds the relevant adoption thresholds, so K keeps its goal.
- G: the installed balanced criterion (sqrt(x_A)+sqrt(x_B))/sqrt(2), with no extra freezing penalty.

The goal menu and equilibrium selections are exactly part of the encounter definition. Existing G types keep G; a larger menu permitting new goals, reversals or alternative indifference selections needs a new payoff and transmission table. This is not a theorem that every revisable agent behaves as R or G.

After its single encounter, each parent's **own-color physical output** produces offspring at the same conversion rate. That is the fitness map. In particular G does not maximize its own offspring count: its utility values both colors through a concave joint criterion. K's intrinsic penalty affects its decisions but is not subtracted from physical offspring unless an actual resource mechanism says so. Combat winners, losers and modified lineages reproduce from their actual delivered quantities; losing agency is not automatically assigned an additional fitness penalty.

The next generation receives fresh encounter resources from a specified external renewal supply; they are not created by recycling the previous generation's consumed work. Each parent acts in one finite batch and its decision criterion concerns that batch. Birth instantiates the inherited objective template for the new agent's batch and color identity. Thus types describe **objective constructors**, not an assertion that distinct agents or newly indexed batches have identical complete-history preferences. The current installed template, or a reset template in the separate control below, is inherited by a stated birth kernel. No parent is forced to optimize a founder's criterion after modification.

Use an infinite-population deterministic limit of expected offspring, no mutation, and no immigration. A common fertility multiplier or type-neutral density regulation can normalize population size without changing the frequency equations; any extra birth inputs come from the declared renewal supply. Copying/instantiating the finite templates is assumed to have the same already-accounted per-offspring resource cost in the two transmission controls. A costlier reset would require a different birth kernel. Finite-population drift, resource competition across batches, long-lived agents, coalition encounters and preferences about later descendants are outside this process.

## 2. The encounter table must include transmitted types

The selected E2-U continuations give the following expected totals **per pair**:

| Pair before play | Behavior / own-color quantities | Offspring by installed template |
| --- | --- | --- |
| R–R | Earlier R keeps and gets 3/4; later R changes to G and gets 1/4 | 3/4 R, 1/4 G |
| R–K | R changes and gets 1/4; K keeps and gets 3/4 | 1/4 G, 3/4 K |
| R–G | R keeps and gets 3/4; G gets 1/4 | 3/4 R, 1/4 G |
| K–K | Initial war; expected 27/200 for each parent | 27/100 K |
| K–G | K keeps and gets 3/4; G gets 1/4 | 3/4 K, 1/4 G |
| G–G | Both retain the balanced goal; 1/2 each | 1 G |

The R–R and R–K changes are evaluated by the original own-color criterion as in note 010, not by G's later approval. In R–G, changing would give the original R only 1/2 instead of its 3/4 separate continuation, so it declines. K declines the same change even more strongly. A G-controller prefers the selected peaceful continuation to available combat. These are encounter equilibrium statements conditional on the specified menus and selections; the evolutionary equations do not supply missing strategic incentives.

Own-color expectations suffice for the chosen linear reproduction rule. A different nonlinear fitness map cannot generally be applied to the mean quantities in this table instead of to their full outcome lotteries.

## 3. Random matching with inheritance of the installed template

Let r,k,g be current frequencies, summing to one. Under independent random matching, expected offspring masses per current individual are

$$R=\frac38r^2+\frac34rg,$$
$$K=\frac34k(r+g)+\frac{27}{200}k^2,$$
$$G=\frac18r^2+\frac14rk+\frac14rg+\frac14kg+\frac12g^2.$$

The R–R terms are halved because the pair's 3/4 R and 1/4 G offspring are shared between two current individuals. The cross-pair terms separately count the two parental types. Their total is

$$Z=R+K+G=\frac12-\frac{73}{200}k^2>0.$$

Every peaceful pair delivers total one; only a K–K pair delivers 27/100. The next frequencies are (R/Z,K/Z,G/Z).

The K-frequency evolves independently of the mix of R and G:

$$k'-k=\frac{k(1-k)(50-73k)}{200Z}.$$

For 0<k<1 it converges to k*=50/73. To see that it cannot oscillate across this fixed point, differentiate its update map: the derivative has numerator (300-492k+219k^2)/800 and positive denominator Z^2. On [0,1] that numerator is positive, since it decreases there to 27/800. Thus the map is increasing; values below k* increase while staying below it, and values above decrease while staying above it.

Within the non-K population set q=r/(1-k). Its update is

$$q'=\frac32\frac{1-k}{2-k}\,q(2-q).$$

Once k is sufficiently close to 50/73, q contracts uniformly: its limiting multiplier is at most 23/32<1. Hence any initial r>0 and 0<k<1 converges to

$$\boxed{(r,k,g)\longrightarrow(0,50/73,23/73).}$$

Finite-freezing K types survive at positive frequency. The selfish revisable template R disappears through the combination of competition and conversion into G, while the revisable balanced template G remains. This does not say that revisability itself disappears.

At this limiting K/G mixture, a rare R parent has total expected offspring (1/4)(50/73)+(3/4)(23/73), which exceeds the resident average 24/73. Nevertheless its **R-template offspring** come only from the G encounters and have growth factor 23/32<1. Offspring produced after changing to G transmit G. A parent can therefore have above-average reproduction while the frequency of its initial goal template declines. Selection on a transmitted trait cannot be inferred from parent payoff alone.

Boundary populations differ without mutation. Pure K remains pure K. If K is absent and R is present, q'=(3/4)q(2-q) and the population converges to (r,g)=(2/3,1/3). Pure G remains pure G. Claims about invasion require specifying that the corresponding rare type is actually introduced.

## 4. Explicit assortative matching

Let rho in [0,1]. A parent meets its own current type with probability rho; otherwise it meets a random population member. Thus P(partner=j | type=i)=rho 1{i=j}+(1-rho)p_j. This is a symmetric feasible pairing rule: cross-type pair masses agree in both directions. It is exogenous matching, not an inferred social capability.

The R and K offspring masses become

$$R=\frac38\rho r+(1-\rho)\left(\frac38r^2+\frac34rg\right),$$
$$K=\frac{27}{200}\rho k+(1-\rho)
\left[\frac34k(1-k)+\frac{27}{200}k^2\right],$$

and

$$Z=\frac12-\frac{73}{200}
[\rho k+(1-\rho)k^2].$$

Again G=Z-R-K. The K update satisfies

$$k'-k=
\frac{k(1-k)[50-123\rho-73(1-\rho)k]}{200Z}.$$

Its map remains strictly increasing on [0,1]. The derivative numerator, after multiplication by 800, is

$$300-246\rho-492(1-\rho)k+219(1-\rho)k^2,$$

which decreases with k and is at least 27(1+rho)>0. Therefore for 0<k_0<1,

$$k_t\to
\begin{cases}
(50-123\rho)/[73(1-\rho)],&\rho<50/123,\\
0,&\rho\ge50/123.
\end{cases}$$

At the equality threshold convergence to zero can be slow; the formula does not assert exponential convergence there.

The non-K share q has the update

$$q'=\frac32q\,
\frac{\rho+(1-\rho)(1-k)(2-q)}{2-(1-\rho)k}.$$

For each k this map is increasing on [0,1] and has the form A(k)q-B(k)q^2. Since k converges, its coefficients converge. If the limiting A<=1, q converges to zero; at A=1 the positive quadratic term still decreases every positive q. If A>1, q converges to (A-1)/B when q_0>0. For the latter claim, outside any small interval around that positive fixed point the limiting growth ratio is uniformly above or below one; the same holds for all sufficiently late maps. Monotonicity makes a slightly larger interval invariant, giving convergence by shrinking the interval. Zero cannot be a limit when A>1 because sufficiently small positive q then grows by a factor bounded above one.

Substituting the K limit gives the full phase table below, for r_0>0 and 0<k_0<1. A missing initial G type is generated by the R encounters.

| Assortment rho | Limiting r | Limiting k | Limiting g |
| --- | --- | --- | --- |
| 0<=rho<=18/91 | 0 | (50-123rho)/[73(1-rho)] | 1-k |
| 18/91<rho<50/123 | (91rho-18)/[73(1-rho)] | (50-123rho)/[73(1-rho)] | 41/73 |
| 50/123<=rho<2/3 | (2/3-rho)/(1-rho) | 0 | 1/[3(1-rho)] |
| 2/3<=rho<=1 | 0 | 0 | 1 |

For rho<50/123, the limiting rare-R growth ratio within the non-K population crosses one at rho=18/91. In the middle coexistence region the G fraction is exactly 41/73; the other two fractions exchange mass as assortment changes. Once K disappears, R can invade the G population only for rho<2/3. Very strong same-type matching removes R's opportunity to exploit G while R–R encounters still convert some offspring to G.

These thresholds concern this matching and transmission kernel. They do not follow from a general assertion that intelligence favors compromise or that a goal's numerical utility equals reproductive fitness.

## 5. A reset-transmission control gives a different type story

For comparison, suppose birth resets every descendant of an R parent to the selfish revisable template R even when that parent installed G. This is an explicit reinitialization mechanism, not inheritance of the installed preference. Keep only the hereditary R/K labels. Their own-color fitness matrix is

$$\begin{array}{c|cc}
&R&K\\\hline
R&1/2&1/4\\
K&3/4&27/200
\end{array}.$$

Under random matching, R's fitness minus K's is (23-73r)/200, giving stable coexistence r=23/73. Under the assortment rule it is

$$[23+50\rho-73(1-\rho)r]/200.$$

For rho<50/123 the stable interior R fraction is (23+50rho)/[73(1-rho)]; at or above that threshold R tends to fixation from a mixed population. The finite-freezing parent has not voluntarily relaxed its penalty: its frequency changes through the declared birth and matching process.

The control shares encounter physics and choices with the installed-template model but changes what reproduction transmits. Even where the total non-K frequency happens to agree, it cannot answer the same question about actual current goals. Treating the 2x2 fitness matrix as a closed model while claiming that offspring inherit the installed G would omit a real type transition.

## 6. Scope and next removal tests

This is an explicit counterexample family to universal elimination of finite freezing, and a demonstration that goal change, individual reproductive success and goal-type prevalence can diverge. The algebra uses familiar population-update methods; no novelty claim is made. The preference-evolution literature in L08 is a close comparison, but its theorem is not imported: this note has its own encounter, fitness, transmission and assortment assumptions.

The strongest restrictions are the finite public goal menu and selected encounter equilibria, renewal resources, one-batch objectives, inherited constructor templates, equal encounter strengths and exogenous assortment. Hidden types, strategic matching, correlated execution failures, offspring inheriting strength, expanded goals or different continuation selections can change the table before any population calculation begins. A continuous-time replicator equation that ignores conversion is not a substitute for the discrete birth kernel used here.

## 7. Recurrent innovation removes exact extinction without removing selection

Retain random matching (rho=0) and the installed-template encounter/birth map above. After reproduction, with probability epsilon in (0,1] independently of the parent's type, instantiate the offspring template from a fixed full-support distribution nu=(nu_R,nu_K,nu_G). With probability 1-epsilon inherit the just-produced template. This is an explicit mutation/innovation channel, not voluntary relaxation by an incumbent. Its material/work requirements come from the same declared renewal supply; template-independent instantiation cost is a local assumption.

If T is the original frequency map, the new map is

$$p'=(1-\epsilon)T(p)+\epsilon\nu.$$

Every type then has frequency at least epsilon nu_i after one generation. More strongly, the map has a unique interior fixed point and converges to it from every initial population. For epsilon=1 this is immediate: p'=nu. The following proof covers 0<epsilon<1.

The K frequency still evolves autonomously, with

$$k'=(1-\epsilon)\frac{150k-123k^2}{100-73k^2}
+\epsilon\nu_K.$$

The numerator of k'-k after multiplying by its positive denominator is

$$D(k)=73k^3-[123(1-\epsilon)+73\epsilon\nu_K]k^2
+(50-150\epsilon)k+100\epsilon\nu_K.$$

It satisfies D(0)>0 and D(1)=27epsilon(nu_K-1)<0. Its leading coefficient is positive, so there is also a negative root and a root greater than one, by the signs at minus/plus infinity. A cubic cannot have more than these three distinct roots. Therefore exactly one root k_epsilon lies in (0,1), and D is positive below it and negative above it inside that interval. The K update is increasing, because the original update is increasing and the mutation term is constant. Iteration thus moves monotonically toward k_epsilon without crossing it.

Given k, the R update is

$$r'=A(k)r-B(k)r^2+\epsilon\nu_R,$$
$$A(k)=\frac{(1-\epsilon)(3/4)(1-k)}{Z(k)},\qquad
B(k)=\frac{(1-\epsilon)(3/8)}{Z(k)},\qquad
Z(k)=\frac12-\frac{73}{200}k^2.$$

At the limiting k_epsilon, the fixed-point equation is

$$B_*r^2+(1-A_*)r-\epsilon\nu_R=0.$$

It has one positive and one negative root. The positive root r_epsilon lies strictly between zero and 1-k_epsilon: at the lower endpoint the R update is positive, while at the upper endpoint the mandatory G innovation leaves R below that endpoint. Explicitly,

$$r_\epsilon=
\frac{A_*-1+\sqrt{(1-A_*)^2+4B_*\epsilon\nu_R}}{2B_*},
\qquad g_\epsilon=1-k_\epsilon-r_\epsilon>0.$$

For convergence, the limiting R map is increasing on the feasible interval: its derivative is proportional to 1-k_epsilon-r. For all sufficiently late generations, the bound g>=epsilon nu_G keeps the evolving R values in a slightly smaller interval where this monotonicity also holds uniformly. The coefficients converge with k. Continuity and monotonicity imply that the liminf and limsup of r_t are fixed points of the limiting map. Its only feasible fixed point is r_epsilon, so both limits coincide. This proves global convergence of the full frequency vector under the stated innovation channel.

The small-innovation behavior makes the distinction from a no-mutation extinction claim quantitative. As epsilon tends to zero,

$$k_\epsilon=\frac{50}{73}
+\frac{96}{23}\left(\nu_K-\frac{50}{73}\right)\epsilon
+O(\epsilon^2),$$
$$r_\epsilon=\frac{32}{9}\nu_R\epsilon+O(\epsilon^2).$$

For the first expansion, the derivative of the original K map at 50/73 is 73/96; implicit differentiation of k=(1-epsilon)T_K(k)+epsilon nu_K gives the coefficient. For the second, A(50/73,0)=23/32, so the linearized R balance is (1-23/32)r=epsilon nu_R. Both fixed-point equations have nonzero derivatives at the limiting roots, justifying their local expansions.

Thus R is present at every positive innovation rate but remains of order epsilon when innovation is rare, while K retains an order-one share approaching 50/73. The K fixed point lies between nu_K and 50/73: outside that interval the selection drift and the innovation drift have the same sign, so they cannot cancel. Innovation does not generically favor flexibility; its direction depends on the specified channel.

These results use rho=0, full-support parent-independent innovation and the original encounter menu. They do not extend the four assortment phases unchanged, assign mutation rates from rationality, or turn population replacement into voluntary current-utility choice.

## 8. Assortment with innovation: persistence at the thresholds

The same innovation channel can be applied explicitly to section 4's assortative map; one must recompute that map rather than retain its zero-frequency phases. Fix rho in [0,1] and 0<epsilon<1. Put

$$C_\rho=50-123\rho,\quad D_\rho=73(1-\rho),\quad
H_\rho(k)=100-73\rho k-D_\rho k^2=200Z_\rho(k).$$

The sign of the new K drift is the sign of

$$D_{\rho,\epsilon}(k)=
(1-\epsilon)k(1-k)(C_\rho-D_\rho k)
+\epsilon(\nu_K-k)H_\rho(k).$$

For rho<1 this is a cubic with positive leading coefficient D_rho, positive value at zero and negative value 27epsilon(nu_K-1) at one. The negative/unit/above-one root argument from section 7 applies unchanged, giving a unique k_{rho,epsilon} in (0,1) and convergence to it. At rho=1 the polynomial is quadratic with positive leading coefficient 73; its signs give one root in (0,1) and one above one, with the same conclusion. The K update remains increasing.

The R coefficients now are

$$A_\rho(k)=\frac{(1-\epsilon)
[(3/8)\rho+(3/4)(1-\rho)(1-k)]}{Z_\rho(k)},\qquad
B_\rho(k)=\frac{(1-\epsilon)(3/8)(1-\rho)}{Z_\rho(k)}.$$

Its update is A_rho(k)r-B_rho(k)r^2+epsilon nu_R. For rho<1 the same positive-root equation and monotone limiting-map proof give one interior fixed point and global convergence. At rho=1 it is linear in r; at the limiting k the obligatory G innovation forces A<1, so r=epsilon nu_R/(1-A) is the unique feasible fixed point and attracts the sequence. Thus every positive innovation rate gives a unique all-positive limiting population for every fixed assortment value in this model.

The no-innovation thresholds remain visible in the **rate** at which small-innovation frequencies vanish. With nu fixed and epsilon tending to zero:

- At rho=18/91, k tends to 32/73 and the limiting R linear multiplier is one. Here Z=75/182 and B=73/100, so
  $$r_{\rho,\epsilon}\sim10\sqrt{\nu_R/73}\,\sqrt\epsilon.$$
- At rho=50/123, the zero-K linear multiplier is one and the leading selection drift is -[5329/12300]k^2. Hence
  $$k_{\rho,\epsilon}\sim\frac{10\sqrt{123\nu_K}}{73}\,\sqrt\epsilon.$$
- At rho=2/3, k is of order epsilon, the zero-R linear multiplier is one and B=1/4. Therefore
  $$r_{\rho,\epsilon}\sim2\sqrt{\nu_R}\,\sqrt\epsilon.$$

These expansions follow by balancing the stated negative quadratic selection drift against epsilon nu_i. At the first and third thresholds the other frequency alters the linear multiplier only by order epsilon, so its product with the square-root frequency is of smaller order. At the K threshold the factor epsilon k and cubic terms are likewise smaller than the leading epsilon and k^2 terms. Continuity and the unique fixed-point equations justify choosing the nonnegative branch.

Away from the thresholds, vanishing types are ordinarily of order epsilon. For example, for fixed rho>50/123,

$$k_{\rho,\epsilon}\sim
\frac{100\nu_K}{123\rho-50}\epsilon,$$

and for fixed rho>2/3,

$$r_{\rho,\epsilon}\sim
\frac{4\nu_R}{3\rho-2}\epsilon.$$

The limits here hold at a **fixed** rho; the coefficients diverge on approaching a threshold and must not be used uniformly through it. Positive innovation therefore removes exact extinction, while selection still determines whether a type has an order-one, square-root, or linear small-innovation share. The result depends on the specified channel and remains distinct from an incumbent choosing to relax its own goal.

## 9. Local stability under other small encounter or transmission changes

Parent-independent innovation is one specific perturbation. A limited robustness statement also applies to other nearby finite birth kernels. It does not assume that every new utility type or implementation technology is nearby.

Use coordinates (r,k), with g=1-r-k. At rho=0 the original fixed point is p_*=(0,50/73). The derivative of the original normalized map at this point is diagonal:

$$D T(p_*)=\begin{pmatrix}23/32&0\\0&73/96\end{pmatrix}.$$

The first off-diagonal entry is zero because every R-output term contains r; the second is zero because the K map is autonomous. Both eigenvalues lie strictly between zero and one. Suppose a family of actual finite birth maps T_eta maps the population simplex into itself, has a continuously differentiable extension near p_*, and converges in C1 there to T as eta tends to zero. Positive total expected reproduction is required so normalization remains well defined.

There is then a unique fixed point near p_* for sufficiently small eta, and it is locally attracting. Here is a direct justification of the local statement. In a suitable norm the derivative at p_* has norm below one. Continuity gives a neighborhood on which the original and all sufficiently close derivative maps have a common contraction bound below one. A small closed ball about p_* is mapped into itself once the displacement T_eta(p_*)-p_* is sufficiently small. The contraction theorem gives a unique fixed point in that ball and convergence from a smaller neighborhood. Starting at the physical p_* and using simplex invariance shows that this fixed point is physically feasible even though the differentiable extension's ball may cross the simplex boundary. This is local uniqueness and attraction; global convergence of a changed map needs an additional proof.

If, more specifically, T_eta=T+eta h+o(eta) in that neighborhood, the fixed-point equation yields

$$r_\eta=\frac{32}{9}h_R(p_*)\eta+o(\eta),\qquad
k_\eta=\frac{50}{73}+\frac{96}{23}h_K(p_*)\eta+o(\eta).$$

Subtract the unperturbed equation, expand T at p_*, and invert I-DT(p_*). This recovers section 7 when h=nu-p, but also states exactly which first-order component a different transmission or encounter perturbation would have to supply. Simplex invariance implies h_R(p_*)>=0 for a one-sided positive perturbation. Full-support births at positive eta put the nearby fixed point in the interior; a perturbation that never regenerates R need not do so.

Away from the three assortment thresholds, the same argument applies to the attracting limit in section 4. Its Jacobian is triangular because K is autonomous. At a positive K fixed point the K eigenvalue is

$$1-\frac{73(1-\rho)k_*(1-k_*)}{200Z_*}\in(0,1),$$

and at K=0 above its threshold it is (150-123rho)/100 in (0,1). At a positive R fixed point the R eigenvalue is 1-B_* r_* in (0,1), using the quadratic form A r-B r^2 and its fixed-point identity; at R=0 it is the strictly subunit rare-R multiplier in the corresponding phase. Monotonicity proved earlier gives the positive lower bounds. At rho=1 both eigenvalues are directly 3/4 and 27/100. At the stated threshold surfaces an eigenvalue is one, so this contraction argument and its linear response fail; section 8's square-root examples show why the omission matters.

This supplies a stability check for small, explicitly matched changes to the **same finite type system**. It does not prove uninvadability against arbitrary new preferences, preservation of every global basin, or interchange of an execution-noise limit with a population limit at a phase boundary. A small change in a strategic protocol can change its selected encounter equilibrium discontinuously and need not induce a small C1 change of this birth map. Note 032's finite behavioral refinement specifies one execution limit; positive-error population claims still require the actual resulting birth kernel.
