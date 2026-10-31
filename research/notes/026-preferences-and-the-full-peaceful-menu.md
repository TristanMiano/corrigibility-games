# R0001 working note: preferences and the full peaceful menu

The failure of one utility-update route does not establish that peace is unattractive. This note evaluates the whole declared peaceful set under the pre-change criteria and gives exact examples where physical abundance does, and does not, suffice. Its convex-feasibility and linear-inequality machinery is conventional. Proofs are AI self-checked only; no equilibrium or novelty claim is implicit in a feasible bargain.

## 1. A finite full-menu criterion

At a specified history, let d_i be agent i's actual current-utility value from initiating combat, including stochastic winners, physical damage, agency changes and any process preferences. Suppose the declared peaceful implementation menu has complete-history payoff vectors v^1,...,v^m under those same current criteria. These vectors must already include communication, verification, installation, later-successor behavior, and any genuine change penalties. They cannot be scored solely by the proposed new utilities.

If a protected randomization mechanism can implement mixtures of these histories without additional physical or informational effects, the feasible payoff set is their convex hull. Define

$$z_* =\max_{p\in\Delta_m}\min_i
\sum_jp_j(v_i^j-d_i).$$

A strict all-agent improvement exists exactly when z_*>0. Its finite linear-program dual is

$$z_* =\min_{\lambda\in\Delta_n}\max_j
\sum_i\lambda_i(v_i^j-d_i).$$

The primal maximizes z subject to one expected-gain lower bound per agent. Giving these constraints nonnegative multipliers lambda_i and bounding the probability simplex gives the displayed dual, with sum_i lambda_i=1. Feasibility and compactness make the finite optimum attained; standard finite LP duality gives equality. A direct qualitative certificate is also useful: if the compact convex gain set misses the strictly positive orthant, separation supplies a nonzero nonnegative lambda whose weighted gain is nonpositive for every peaceful vector. Conversely, such a lambda excludes any strictly positive gain vector.

The value of z in arbitrary utility units is not an interpersonal welfare measure. Its **sign** is invariant under separate positive affine recodings. Gain offsets cancel; when utility i is rescaled by alpha_i>0, a separating certificate is transformed by lambda_i/alpha_i and renormalized. The test asks whether each current ordering improves.

Without an implementable randomizer, use the actual menu rather than its convex hull. For example, peaceful allocations (3,0) and (0,3), with disagreement (1,1), have no deterministic mutual improvement. Their half-and-half mixture would give (3/2,3/2) in expectation, if that lottery can actually be implemented. A successor vNM utility cannot uniquely choose that interior lottery merely because the original agents would like its expected payoffs; note 010's lottery-implementation obstruction still applies.

If randomization itself consumes work, reveals information or triggers a process penalty, its actual outcomes require new payoff vectors. Convexifying a menu is an implementation assumption, not a free mathematical operation on the universe.

## 2. A common physical comparison gives a sufficient condition

Suppose current utilities depend only on physical output vectors and are increasing and concave. If the deterministic mean of the combat output lottery is peacefully feasible, Jensen's inequality gives every agent at least its combat value. If peaceful capacity permits a feasible strict increase in coordinates to which every utility is strictly increasing, all agents improve strictly.

Alternatively, a peaceful mechanism that reproduces each combat world's valued physical consequences and improves them pointwise gives a weak improvement for arbitrary increasing utilities, without concavity. The actual outcome coupling must be implementable, and each agent needs a positive-probability strict gain for strict preference.

These are useful sufficient conditions with visible failure boundaries. Intrinsic preferences for the combat event, agency, histories, thresholds or relative outcomes can invalidate them. Knowing that a route preserves more material or work does not establish monotonicity of every utility in those resources.

## 3. Finite freezing and combat bonuses over all split/merge routes

Let original utilities value own-color output in resource units. A war produces W conditional on victory, A wins with probability s, and each original criterion additionally gives a nonnegative event bonus b_i for combat. Its reservations are

$$d_A=sW+b_A,\qquad d_B=(1-s)W+b_B.$$

Each peaceful route j has actual output frontier P_j and permits every nonnegative split of that output. It incurs a current-utility change/process penalty kappa_i^j>=0 for agent i. Physical communication and implementation costs have already reduced P_j; do not subtract them again as utility penalties unless the agent separately values the process.

Route j has a strict mutually acceptable split exactly when

$$P_j>W+b_A+b_B+\kappa_A^j+\kappa_B^j.$$

Indeed its A allocation must exceed sW+b_A+kappa_A^j and be below P_j-[(1-s)W+b_B+kappa_B^j]. Nonnegativity of the thresholds makes the interval test sufficient as well as necessary.

For the full route menu, including mixtures implemented as in section 1, the exact condition is

$$\boxed{\max_j(P_j-\kappa_A^j-\kappa_B^j)>W+b_A+b_B.}$$

If one route passes, its split suffices. If none passes, every route's sum of original payoffs is at most W+b_A+b_B, so the nonnegative certificate lambda=(1/2,1/2) also excludes every mixture.

An ordinary unchanged-utility split has kappa_A^j=kappa_B^j=0. Consequently arbitrarily strong aversion to **changing utilities** alone cannot rule out peace whenever that ordinary route satisfies P_j>W+b_A+b_B. Conversely, sufficiently large direct combat bonuses can rule out mutual improvement across the entire bounded peaceful menu. Installing a successor that lacks the bonus does not erase the incumbent's evaluation of the initial choice.

Hard or lexicographic goal preservation is not represented by inserting infinity into this finite-payoff LP. It may exclude utility-change choices under that preference ordering while leaving ordinary policies and physically available combat intact. A change penalty refers to an actual preference-class change, not positive affine recoding or code identity alone.

## 4. Relative and destructive preferences need not favor war

Take output-only original utilities

$$u_A(x)=x_A-\alpha x_B,\qquad
u_B(x)=x_B-\beta x_A,\qquad \alpha,\beta\geq0.$$

Peace permits all x>=0 with x_A+x_B<=P, including producing less than P. Combat has W>0 and 0<s<1; the winner produces only its own color. The war payoff vector is M w, where

$$M=\begin{pmatrix}1&-\alpha\\-\beta&1\end{pmatrix},\qquad
w=(sW,(1-s)W).$$

Thus d_A=sW-alpha(1-s)W and d_B=(1-s)W-beta sW. These are ordinary utilities, not reproductive fitness.

### alpha beta < 1

If a peaceful vector gives strict gains g=M(x-w)>0, then

$$x-w=\frac1{1-\alpha\beta}
\begin{pmatrix}1&\alpha\\\beta&1\end{pmatrix}g>0.$$

Both coordinates increase, so P>W is necessary. It is sufficient by taking any sufficiently small positive gain vector and applying the same inverse. Therefore the exact strict-peace condition remains P>W, despite the negative externalities.

### alpha beta = 1

Now beta u_A+u_B=0 on every world and hence every lottery. Both agents cannot improve strictly over combat, whatever P. This is a preference obstruction, not a physical lack of surplus. Weakly matching the war vector is possible exactly when P>=max(0,d_A,d_B): the equality line can be reached most cheaply on the appropriate coordinate axis. At d_A=d_B=0, producing nothing matches both. No claim that all equilibria fight follows from the absence of a strict bargain.

### alpha beta > 1

At least one war reservation is negative. If both d_A,d_B<0, producing nothing strictly improves both, even at P=0. If d_A>=0, the B reservation is negative and

$$-\beta d_A-d_B=(\alpha\beta-1)(1-s)W>0.$$

So x=(d_A+epsilon,0) strictly improves both for sufficiently small epsilon>0. Its infimal total budget is d_A, and strict A improvement makes P>d_A necessary. The symmetric argument applies when d_B>=0. Therefore strict peace is feasible exactly when

$$P>\max(0,d_A,d_B),$$

or when P=0 and both reservations are strictly negative. The stated W>0 and interior-strength conditions matter; one cannot apply this branch unchanged when a war-coordinate mean is zero.

For example, with alpha=beta=2, s=1/2 and W=1, each combat value is -1/2. A zero-output peace gives both zero. Strong dislike of the opponent's projects can make restraint and underproduction attractive. Forcing full production would hide this peaceful option and reverse the comparison artificially.

## 5. Combat-event preferences can overwhelm that benefit

Add nonnegative combat bonuses b_A,b_B to the relative-utility model, and now let d=Mw+(b_A,b_B).

For alpha beta<1, the same inverse shows that strict peace exists exactly when

$$P>W+\frac{(1+\beta)b_A+(1+\alpha)b_B}{1-\alpha\beta}.$$

For alpha beta=1, any positive weighted bonus beta b_A+b_B makes even weak all-agent improvement impossible, because every peaceful vector has weighted utility zero while combat has a positive weighted value. With both bonuses zero, the preceding no-strict-improvement conclusion remains.

For alpha beta>1, strict feasibility at any sufficiently large P first requires

$$d_A+\alpha d_B<0,\qquad \beta d_A+d_B<0.$$

To prove necessity, a strict gain g>0 would give x=M^(-1)(d+g). The inverse has strictly negative entries, so nonnegative x requires both coordinates of M^(-1)d to be strictly positive, which is exactly the pair of inequalities. For sufficiency at finite P, these inequalities imply either both d_i<0, allowing x=0, or one nonnegative d_i whose corresponding near-axis allocation gives a strict improvement as in section 4. The budget condition is again P>max(0,d_A,d_B), with the same P=0/both-negative exception.

For alpha=beta=2, s=1/2, W=1 and b_A=b_B=3/5, both combat reservations are 1/10. Every peaceful allocation has u_A+u_B=-(x_A+x_B)<=0, whereas combat's summed value is 1/5. No peaceful lottery gives both their combat value, even if P is arbitrarily large. The obstruction is finite, explicit and applies to the whole feasible output set. There is no infinite combat cost, deleted attack action, or assumption that ordinary trade was unavailable.

## 6. What the certificates establish

These results classify beneficial-bargain existence under the declared full peaceful menus. An accepted bargain still needs a proposal rule, current-goal adoption, actual installation, credible verification, and attack incentives at every nonterminal checkpoint. A missing strict bargain does not by itself prove combat in every equilibrium; a feasible one does not select peace.

The examples also caution against treating “destructive,” “frozen,” or “flexible” as scalar predictors. A preference can value avoiding both projects, dislike changing itself, or reward combat as an event; these are different functions on complete histories. Comparing their actual attainable payoff sets is more informative than assigning them a common label.
