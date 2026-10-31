# R0001 working note — approximation robustness and the shape of an installed goal

Exact implementation is weaker than robust implementation. This note derives an accuracy boundary for note 014's late-operator model and constructs goals attaining its order. All accuracy measures are expected regret in a specified, normalized current utility. This is not a computational-complexity theorem or a proof that a particular machine can verify these goals. Proofs are self-checked only.

## 1. Local implementation question and invariant normalization

Let P>W>0, delta=P-W, and 0<s<1. The original A and B objectives are x_A and x_B. A is the selected equipment operator and can install an output-only goal U; its original strength share is s and its combat victory probability is s. A peaceful allocation is

$$p=(sP,(1-s)P),\qquad p_B=(1-s)P.$$

If A wins combat it controls the W-budget simplex; if B wins, B produces (0,W). Require U to be increasing and concave on x>=0, x_A+x_B<=P, uniquely maximized at p on the P-budget simplex and at w=(W,0) on the W-budget simplex. Normalize U(0)=0 and U(p)=1. The normalization is well defined for the goals constructed below. It fixes a preference-invariant accuracy scale: replacing a representation by a positive affine transform and then normalizing gives the same regret criterion.

A peaceful implementation may use any lottery over the P-budget simplex with expected U-regret at most epsilon_P. On an A victory, it may use any lottery over the W-budget simplex with expected U-regret relative to U(w) at most epsilon_W. Underproduction is allowed. The two error sets are independent in this robustness question. An actual algorithm may have a smaller, correlated error set, in which case these bounds can be conservative.

B's actual combat payoff is (1-s)W+s E[x_B | A wins], so approximately selfish postwar production matters too. A's original adoption payoff and its installed goal's later peace/attack comparison must also be checked separately. Physical installation and verification costs belong in the actual P and W before applying this local calculation; if the initial attack has a different output W_0, substitute that initial reservation value in the adoption inequality.

## 2. Exact error envelopes for a concave quadratic goal

Let U(x)=b dot x-(1/2)x^T H x, with H symmetric positive semidefinite, after the chosen normalization. Write d=(1,-1),

$$\kappa=d^T H d>0,\qquad
\mu=d\mathbin{\cdot}\nabla U(w)\ge0.$$

The interior peaceful optimum gives d dot grad U(p)=0. Hence on the full P frontier,

$$U(p)-U(x)=\tfrac12\kappa(x_B-p_B)^2.$$

On the W frontier at x=(W-z,z),

$$U(w)-U(x)=\mu z+\tfrac12\kappa z^2.$$

Completing unused output into A preserves B's amount and weakly raises U. Jensen's inequality then proves the exact worst-case bounds

$$\inf E[x_B\mid peace]
=\max\{0,p_B-\sqrt{2\epsilon_P/\kappa}\},$$
$$\sup E[x_B\mid A\ wins]
=\min\left\{W,
\frac{\sqrt{\mu^2+2\kappa\epsilon_W}-\mu}{\kappa}
\right\}.$$

The same completion argument works for A's peaceful coordinate. These bounds are attained by deterministic full-output allocations at the displayed quantity, so they are exact over the specified lottery sets, rather than merely sufficient estimates. The formulas include mu=0 and zero tolerances without dividing by mu.

Consequently B weakly prefers peace **for every pair of admissible implementations** iff the first displayed quantity is at least (1-s)W plus s times the second. Strict inequality supplies uniform strict deterrence. A's original adoption can be checked with max{0,sP-sqrt(2 epsilon_P/kappa)} against its initial war value. Finally, if epsilon_P<1-U(w), the new A also strictly prefers the approximate peaceful implementation to every possible W-budget combat lottery, since U(w) is the maximum current value at that budget.

These are local incentive comparisons. They do not certify semantic verification, successful installation, equilibrium selection, or protection from later changes in the physical frontier.

## 3. Why normalized quadratic goals become poorly conditioned

Let c=d^T H e_A and h_AA=e_A^T H e_A. Since p-w=delta e_A-p_B d,

$$\mu=\delta c-p_B\kappa\ge0.$$

Positive semidefiniteness gives c^2<=kappa h_AA. Combining these inequalities yields

$$\kappa\le h_{AA}\frac{\delta^2}{p_B^2}.$$

Monotonicity along the A axis implies b_A>=h_AA P. Therefore

$$1\ge U(P,0)=b_A P-\tfrac12 h_{AA}P^2
\ge\tfrac12h_{AA}P^2,$$

and so

$$\boxed{\kappa\le\frac{2\delta^2}{P^2p_B^2}.}$$

This is a property of the whole normalized monotone concave **quadratic** class satisfying the two implementation requirements. It is not caused merely by an arbitrary choice of coefficient scale. If kappa were zero, the goal would be constant along the peaceful frontier and could not uniquely implement its interior split.

Consider the full-output allocation with B quantity (1-s)W, exactly its ideal selfish-war reservation. Its peaceful U-regret is (1/2)kappa[(1-s)delta]^2, at most

$$\left(\frac\delta P\right)^4.$$

Thus uniform **strict** B-deterrence for all epsilon_P-optimal peaceful policies requires epsilon_P<(delta/P)^4, even if postwar production is exact. Equality at the actual lower regret threshold permits indifference; above it, a nearby allocation can make B strictly prefer war. This is an upper bound on the tolerable regret, not a lower bound on algorithm runtime.

## 4. The quadratic order can be attained up to constants

Assume delta<=p_B and let m=min{s,1-s}. Use note 014's quadratic with

$$\rho=1-\frac\delta{2p_B},\qquad
z_p=p_A+\rho p_B=P-\delta/2,$$
$$U_0(x)=2P x_A+[2P-(1-\rho)z_p]x_B
-\tfrac12(x_A+\rho x_B)^2.$$

It is increasing and concave, uniquely produces p at P and (W,0) at W. Let N=U_0(p). Its marginal utilities are at least P and U_0(x)<=2P^2 on the simplex, so P^2<=N<=2P^2. Normalize U=U_0/N. Then

$$\kappa\ge\frac{\delta^2}{8p_B^2P^2},\qquad
\mu\ge\frac{\delta^2}{8p_BP^2}.$$

If both error tolerances are at most

$$\epsilon_Q=
\frac{m^2}{64(1-s)^2}\left(\frac\delta P\right)^4,$$

the peaceful error in either expected coordinate is at most m delta/2, and the expected B output after an A war victory is at most m delta/8. These follow by substituting into sqrt(2 epsilon_Q/kappa) and epsilon_Q/mu, using delta/P<=1 and m<=1-s. Thus the original A's peaceful payoff exceeds sW, B's peaceful payoff exceeds its actual combat value, and the new A prefers peace. For the last assertion, note 014's unnormalized current-goal margin is at least P delta; after normalization it is at least delta/(2P), which exceeds epsilon_Q.

For fixed interior s, the fourth-power accuracy order is therefore both necessary and sufficient up to constants within this quadratic class. The constants are not optimized, and the common W assumption remains local.

## 5. A general concave-goal upper bound is only second order

Now drop the quadratic restriction while retaining monotonicity, concavity, normalization and the two specified optima. Set r=W/P and consider the same potentially troublesome peaceful allocation

$$x_{bad}=(P-rp_B,rp_B).$$

Concavity from the origin gives U(rp)>=r U(p)=r. Since rp is feasible at the war budget, U(w)>=r. The vector x_bad componentwise dominates

$$y=r p+(1-r)w:$$

their B coordinates coincide and x_bad,A-y_A=delta^2/P>=0. Hence monotonicity and concavity imply

$$U(x_{bad})\ge U(y)
\ge r U(p)+(1-r)U(w)
\ge r+(1-r)r=1-(1-r)^2.$$

Therefore every such goal admits a peaceful allocation at B's exact selfish-war reservation with regret at most (delta/P)^2. Uniform strict B-deterrence for all approximate policies requires epsilon_P<(delta/P)^2. This argument applies to nonsmooth as well as smooth concave goals and does not assume a particular utility representation beyond the invariant normalization.

The gap between this second-power bound and the quadratic fourth-power bound is real. The following construction attains second-power robustness with a smooth, strictly concave goal.

### A stronger bound when both implementations have the same error tolerance

Let d=delta/P=1-r and suppose d<=s r. For any goal in the stated class set gamma=1-U(w) and eta=U(w)-U(rp). Uniqueness and strict monotonicity give gamma>0 and eta>0; concavity gives gamma+eta=1-U(rp)<=d.

For a common regret allowance epsilon, peaceful implementation can take the convex combination (1-t)p+t w and complete its unused output into A, where t=min{epsilon/gamma,1}. Its B-output is (1-t)p_B, and concavity ensures regret at most t gamma. Postwar implementation can take (1-theta)w+theta rp, where theta=min{epsilon/eta,1}; this has B-output theta r p_B and regret at most theta eta. These are deterministic feasible policies, so the construction does not require an independently enforceable randomizer.

If t=1, B strictly prefers its positive combat reservation. If theta=1, the adverse-output comparison t+s r>=d already holds because s r>=d. Otherwise strict B-deterrence requires

$$\epsilon\left(\frac1\gamma+\frac{s r}{\eta}\right)<d.$$

For positive gamma,eta with gamma+eta<=d, Cauchy-Schwarz gives 1/gamma+s r/eta>=(1+sqrt(s r))^2/d. Therefore uniform strict B-deterrence requires

$$\boxed{\epsilon<\frac{d^2}{(1+\sqrt{s r})^2}.}$$

This improves the constant when both peaceful and postwar implementations can err. The restriction d<=s r handles the capped-mixture case explicitly; no formula outside that region is asserted. For fixed s and a vanishing surplus, the leading upper-bound constant is 1/(1+sqrt(s))^2. This subsection addresses the opponent's deterrence condition; original-founder participation remains a distinct constraint.

## 6. A piecewise-linear construction with the better order

Assume again delta<=p_B. Define Y=x_A+x_B and

$$c=1+\frac{2p_B}{\delta},\qquad
e=2p_A-(2-c)P,$$
$$L_1(x)=cY+x_A,\qquad
L_2(x)=2Y-x_A+e,$$
$$F(x)=\min\{L_1(x),L_2(x)\}.$$

Both affine functions are strictly increasing in each output, and e>0, so F is increasing, concave and F(0)=0. On a fixed budget Y the first branch has A-share slope +1 and the second slope -1. Their intersection is

$$x_A=\frac{(2-c)Y+e}{2}.$$

At Y=P it is p_A, so the peaceful optimum is unique. At Y=W it is W+delta/2, beyond the feasible frontier, so the war optimum is uniquely all A. The same holds at smaller budgets. Let

$$N=F(p)=cP+p_A
=\frac{2Pp_B}{\delta}+P+p_A
\le\frac{4Pp_B}{\delta}.$$

The normalized full-frontier peaceful regret is |x_B-p_B|/N, and war regret from B-output z is z/N. Consequently a common regret tolerance of order (delta/P)^2 bounds both output errors by a fixed fraction of the agents' order-delta bargaining slack. The exact normalized error envelopes are max{0,p_B-N epsilon_P} and min{W,N epsilon_W}. No discontinuous goal jump or combat-history flag was used.

## 7. A smooth, strictly concave version with explicit constants

Let m=min{s,1-s}, tau=m delta/16, and define the soft minimum

$$S_\tau(x)=-\tau\log\left(
e^{-L_1(x)/\tau}+e^{-L_2(x)/\tau}\right).$$

Use the raw goal

$$J(x)=S_\tau(x)-\frac{Y^2}{8P},$$

then normalize U(x)=[J(x)-J(0)]/[J(p)-J(0)]. This formula is a mathematical definition; numerical implementations should use a stable log-sum-exp calculation and separately certify their regret.

The soft-minimum gradient is a convex combination of the two affine gradients, whose coordinates are at least one. The subtractive term changes either partial derivative by -Y/(4P)>=-1/4, so J remains strictly increasing. Its Hessian is the negative weighted covariance of the affine gradients divided by tau, minus (1/(4P)) times the outer product of (1,1). The affine-gradient difference is (c,c-2), which is not parallel to (1,1). Both soft-minimum weights are positive at every finite point. Thus the Hessian is negative definite, and J is smooth and strictly concave.

Subtracting a function of Y does not change allocation choices on a fixed budget. At P, the symmetric soft minimum of slopes +1 and -1 is uniquely maximized at p. At W, the first branch lies below the second by at least delta throughout the feasible A-share range; the share derivative of S_tau is at least tanh(delta/(2tau))>1/2, so all-A production remains uniquely optimal. Monotonicity makes these the optima over the entire corresponding simplexes.

Write N_tau=J(p)-J(0). The soft-minimum bounds F-tau log 2<=S_tau<=F show 0<N_tau<=N. For a full-output peaceful allocation differing by z in either color, raw regret is

$$\tau\log\cosh(z/\tau).$$

Since log cosh v>=|v|-log 2, expected normalized regret epsilon_P bounds either expected signed output error in magnitude by N epsilon_P+tau log 2. The completion argument extends this to underproduction. The war derivative lower bound gives E[x_B | A wins]<=2N epsilon_W, also allowing underproduction.

Now take both tolerances at most

$$\boxed{\epsilon_S=
\frac{m}{64(1-s)}\left(\frac\delta P\right)^2.}$$

Then N epsilon_S<=m delta/16 and tau log 2<m delta/16. Peaceful error is below m delta/8; B-output after an A victory is at most m delta/8. Original A therefore strictly prefers adoption to its sW reservation, and B strictly prefers peace to its actual combat payoff: its total adverse error is below m delta(1+s)/8<=(1-s)delta/4, whereas its ideal peaceful slack is (1-s)delta.

The installed goal also prefers peace. Before smoothing and the Y-square term, F(p)-F(w)=p_B+2delta. Smoothing loses at most tau log 2, and the square term loses at most delta/4. Thus the raw current-goal margin remains greater than p_B; after normalization it is at least p_B/N>=delta/(4P). This is greater than epsilon_S. These comparisons include the old founder, the original opponent, and the installed successor in their respective criteria.

For fixed interior s and a shrinking positive surplus, second-power normalized regret tolerance is therefore attainable by smooth, strictly increasing, strictly concave goals and is optimal in order over the whole concave class by section 5. This is a statement about robust local goal implementation under the declared error sets, not about the computational cost of constructing or verifying the goal.

## 8. Boundaries of the result

[Note 023](023-sharp-smooth-goal-robustness.md) sharpens the sufficient constant: when d<=sr and r>=s, the section 5 upper bound is the exact supremum over smooth strictly increasing strictly concave goals, including original-founder participation. It adds a third affine piece before calibrated smoothing; the earlier two-piece construction remains a simpler order-optimal witness.

The goals are nonhomothetic and change allocation sharply across nearby physical budgets. Stochastic or misestimated frontiers require evaluating their actual induced schedules; inserting an expected budget is not valid. A fixed-utility delegate that can execute the same conditional allocations with the same error and verification guarantees supplies the corresponding control, although revocability and deviation incentives remain separate.

A solver certificate epsilon=2^(-b) would have to increase b as the surplus closes, with the indicated second- or fourth-power logarithmic dependence. This does **not** prove a lower bound on energy use, runtime, code length or verification complexity. An exact rational policy, a restricted action menu or a different error model may avoid that certificate requirement. Utilities outside the monotone concave class, combat-history-dependent goals, changes in the feasible set or additional initial freezing penalties also require new bounds. The minimal contract does not fix these choices.
