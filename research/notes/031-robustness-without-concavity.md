# R0001 working note: the accuracy boundary changes without concavity

This removes the concavity assumption from note 023 while retaining its normalized physical frontiers, strength-weighted contest, output-only preferences and independent expected-regret error sets. The result is a sharp local implementation bound, not a full negotiation equilibrium or a complexity estimate. All proofs are contributing-agent self-checks.

## 1. Statement and common comparison

Normalize peaceful output to one. Put r=W/P, d=1-r, b=1-s, p=(s,b) and w=(r,0), where s is A's actual victory probability. Retain the explicit region

$$0<d\leq sr,\qquad r\geq s,\qquad 0<s<1.$$

An original own-color A considers installing a goal U. Its unmodified combat value is sr. Original B retains Attack and, on winning, makes (0,r). After A wins, the installed U controls the r-simplex. Peace uses the unit simplex. Each implementation can independently be any lottery with expected U-regret at most epsilon. The normalization is U(0)=0, U(p)=1; p and w must be the respective unique optima. As in note 023, this is the protected local execution comparison with the same initial and final threat frontiers. Proposal revision, installation cost and earlier attacks require the separate timing checks of notes 020/027.

**Result.** Over continuous, strictly increasing output-only goals in this class, without a concavity restriction, the supremal common regret allowance uniformly guaranteeing strict original-A adoption, strict B attack deterrence and strict current-A preference for peace is

$$\epsilon_N=\frac{b d}{(\sqrt b+\sqrt{sr})^2}.$$

Every epsilon<epsilon_N is achieved by such a goal. No nondecreasing goal with the stated unique optima guarantees strict B deterrence at epsilon>=epsilon_N. The construction below is continuous and piecewise defined; no smoothness or implementation-cost bound is asserted.

For fixed interior s and d tending to zero, epsilon_N has first-order scaling in d. Note 023's sharp concave allowance is epsilon_C=d^2/(1+sqrt(sr))^2, with second-order scaling. Concavity therefore changes the mathematical accuracy obstruction in this error model. The broader result does not establish that a nonconcave goal is cheaper to compute, install or verify.

## 2. Universal adverse lotteries

For an admissible nondecreasing goal, write

$$a=U(1,0),\qquad t=U(r,0),\qquad z=U(0,r).$$

The assumptions imply 0<=z<t<=a<1. A peaceful lottery can mix p with (1,0), with the latter's probability epsilon/(1-a). Independently, A-victory production can mix w with (0,r), with the latter's probability epsilon/(t-z). When both probabilities are below one, these implementations each use exactly the regret allowance. B's peace payoff minus its attack payoff is

$$bd-\epsilon\left[\frac b{1-a}+\frac{sr}{t-z}\right].$$

If the peaceful probability reaches one, B gets zero from peace and has a positive combat value. If the postwar probability reaches one, attack gives B all r output regardless of the winner; exact peace gives B only b. Here r>b, because d<=sr implies r>=1/(1+s)>1-s. Thus the capped cases also defeat strict uniform deterrence.

In the uncapped case, monotonicity and Cauchy-Schwarz give

$$\frac b{1-a}+\frac{sr}{t-z}
\geq\frac b{1-t}+\frac{sr}{t}
\geq(\sqrt b+\sqrt{sr})^2.$$

Hence strict uniform deterrence requires epsilon<epsilon_N. Equality in the last inequality uses

$$t_* = \frac{\sqrt{sr}}{\sqrt b+\sqrt{sr}}.$$

Unlike the upper bound in note 023, this argument uses allowed lotteries directly and does not use concavity to bound the utility of an interpolated physical world.

## 3. A monotone goal approaching the bound

Fix epsilon<epsilon_N and put t=t_*. Choose a small zeta>0 such that E=(1+zeta)epsilon<epsilon_N. The symbol E here is a regret allowance before renormalization, not energy or a physical stock. Let

$$C=1-ts/r>0,\qquad L(v)=\min\{1,\max\{0,v\}\}.$$

For a sufficiently small eta>0, define on the physical unit simplex

$$U_\eta(x)=t\min\{x_A/r,1\}
+C\,L((x_A-s+\eta)/\eta)\,L((x_B-b+\eta)/\eta),$$

$$V_{\eta,\zeta}(x)=\frac{U_\eta(x)+\zeta(x_A+x_B)}{1+\zeta}.$$

Take

$$0<\eta<\min\left\{s,b,d/2,\frac C{t/r+(1-t)/b}\right\}.$$

Both functions are continuous and nondecreasing. V is strictly increasing in each coordinate wherever a coordinate increase stays feasible, because zeta>0. They are normalized to zero at the origin and one at p.

The bonus is positive only in the region R_eta={x_A>s-eta, x_B>b-eta}. This region does not intersect the r-simplex, since its points have total output greater than 1-2eta>r. Consequently U_eta=t x_A/r throughout the postwar simplex, and w is its unique maximum. Adding zeta times total output preserves that maximum.

To check the peaceful optimum, write a point on the unit frontier as (s+h,b-h). For -eta<=h<=0 its value is t(s+h)/r+C(1+h/eta), strictly increasing in h. For 0<=h<=eta, the bonus is C(1-h/eta), while the base has slope at most t/r, so the total is strictly decreasing by eta<Cr/t. Outside this interval the bonus is zero and the value is at most t<1. Thus p is the unique frontier optimum. Strict monotonicity of V excludes an underproducing optimum; at p it has value one.

This bonus is an output preference, not a history flag for whether combat occurred. The construction distinguishes opportunities by their different feasible output sets; it never assigns different utility to the same physical output depending on its route.

## 4. Exact uniform bounds, including lotteries and underproduction

Two global affine upper bounds hold on the peaceful simplex:

$$U_\eta(x)\leq x_A/s,\qquad
U_\eta(x)\leq t+(1-t)x_B/b.$$

For the first, x_A>=s gives a right side at least one. Below s-eta the bonus vanishes and t/r<1/s. Between s-eta and s, upper-bound the B clip by one: the resulting affine function is below x_A/s at the left endpoint and equals it at s. This proves the first bound everywhere.

For the second, monotonicity allows filling unused capacity with A output while holding x_B fixed. On the full frontier, x_B>=b gives a right side at least one. Writing x_B=b-h for 0<=h<=eta, the goal is at most 1+(t/r-C/eta)h, which is bounded above by 1-(1-t)h/b by the chosen eta. For h>=eta the bonus is zero and U_eta<=t<=1-(1-t)h/b. This proves the second bound.

Any peaceful epsilon-regret lottery for V has expected unnormalized value at least 1+zeta-E. Since total output is at most one, the two bounds imply

$$\mathbb E[x_A]\geq s(1-E),\qquad
\mathbb E[x_B]\geq b\left(1-\frac E{1-t}\right).$$

Each individual lower bound is sharp in its uncapped range: mix p with (0,1) for the A bound, or with (1,0) for the B bound. These are separate adverse implementations; they need not minimize both founders' outputs at once.

On the war simplex the unnormalized regret is at least (t/r)x_B, including underproduction: its additional missing-total-output term is nonnegative. Thus every allowed A-victory implementation satisfies

$$\mathbb E[x_B\mid A\text{ wins}]\leq rE/t.$$

This upper bound is also sharp before its cap, by mixing w with (0,r). B's worst peaceful payoff minus its worst attack payoff is consequently exactly

$$bd-E\left[\frac b{1-t}+\frac{sr}{t}\right]
=bd-E(\sqrt b+\sqrt{sr})^2$$

through the relevant uncapped range. At E=epsilon_N both mixing weights are below one: epsilon_N/(1-t)=sqrt(b)d/(sqrt(b)+sqrt(sr))<d<1, while epsilon_N/t=bd/[sqrt(sr)(sqrt(b)+sqrt(sr))]<b<1 using d<=sr. Thus for this fixed goal family the exact strict B-deterrence boundary is epsilon_N/(1+zeta).

Original A's participation is strict throughout E<epsilon_N, since epsilon_N<d and s(1-E)>sr. This decision uses the original own-color utility. The newly installed criterion gives peace at least 1-epsilon and combat at most [s t+zeta r]/(1+zeta), so its unnormalized margin is at least

$$1-st-E+\zeta d>0.$$

Here epsilon_N<b follows from d<=sr<(sqrt(b)+sqrt(sr))^2, while 1-st>b. The strict inequality follows from E<epsilon_N. All three decision criteria therefore have the required margins. For every epsilon<epsilon_N a positive zeta with (1+zeta)epsilon<epsilon_N exists, proving the supremum statement.

At E=epsilon_N the explicit endpoint lotteries make B indifferent. They establish an exact failure boundary for this family; the original A still has a positive participation margin there. For the nondecreasing intermediate goal zeta=0, the same continuous U_eta attains the weak boundary itself. Strict coordinate monotonicity is restored by any positive zeta, with the explicitly calculated normalization cost.

## 5. Exact checks

An exact parameter example is s=3/4, r=64/75, d=11/75. Here t_*=8/13,

$$\epsilon_N=11/507,\qquad \epsilon_C=121/18225.$$

The difference is a property of the goal classes under the same normalized regret model. It is not obtained by rescaling a utility or deleting B's attack action. Both peaceful and postwar errors remain independently adverse, with the latter affecting B's actual war incentive. The exact lottery checks in `tests/test_e2_nonconcave_robustness.py` enumerate every full-frontier breakpoint and every two-point error mixture for three rational parameter cases. The general statements rest on the proofs above, not those samples.

## 6. Regularity and physical-state sensitivity limit the improvement

### A normalized modulus restores a second-order obstruction

Suppose an otherwise admissible goal additionally satisfies U(p)-U(rp)<=m, where 0<m<1. Then t=U(w)>=U(rp)>=1-m, because w maximizes U on the war simplex. The universal bound in section 2 can be minimized only over t>=1-m. If 1-m>t_*, strict uniform deterrence necessarily requires

$$\epsilon<\frac{bd}{b/m+sr/(1-m)}.$$

If 1-m<=t_*, the unrestricted epsilon_N bound still applies. This is a necessary bound; sharpness within a globally regular goal class is not asserted.

In particular, if the normalized U is L-Lipschitz in the L1 distance on the unit simplex, then m=Ld is available whenever Ld<1. For fixed L and sufficiently small d, the necessary bound is at most Ld^2. To achieve a first-order allowance epsilon>=c d along a small-surplus sequence, the normalized Lipschitz constants must therefore grow at least as c/d. This follows also directly from epsilon<d(1-t)<=Ld^2; it does not require a differentiable goal.

The class in the main theorem does not hold this modulus fixed. Its bonus becomes steep as the two physical frontiers approach. The improved optimization-regret allowance should not be interpreted as robustness to arbitrary perturbations of the physical model.

For the explicit family, V(rp)=(ts+zeta r)/(1+zeta)<r, directly witnessing nonconcavity. Its normalized Lipschitz constant must be at least [1-ts+zeta d]/[(1+zeta)d], by comparing p and rp. This makes the increasing steepness visible in the actual construction, rather than only in the universal necessary bound.

### A changed physical budget can destroy deterrence even at zero regret

Take the constructed V with d<br, and let the actual peaceful frontier after a public material loss be Y=1-2eta. Since eta<d/2, one has r<Y<1. The bonus region is now infeasible: every feasible output has total at most 1-2eta, while a positive bonus requires strictly more than that. The installed criterion is not automatically redefined when the physical state changes.

Every exact V-maximizer at this new frontier uses total Y and assigns at least r to A: the base reaches t at x_A=r and remains flat thereafter, while the zeta term requires full production. Thus B receives at most Y-r<d<br. On attack, B gets br, since A's victory optimizer on the r-simplex still uniquely makes (r,0). B therefore strictly attacks under every exact peaceful implementation, even though Y>r and ordinary unchanged-goal territorial division would give both founders more than their selfish combat values. Current A still prefers a peaceful optimum to combat; the failure is B's retained incentive.

These frontiers have a matched serial physical realization. Set usable material O=Y, dispersed material zero, work B=1+2r and a sufficiently long deadline. Production, recovery work and recovery time coefficients are one, with production capacity one. Combat consumes one work and one time unit and disperses all material. Peace yields Y; combat yields min{Y,(B-1)/2}=r. The same budgets with O=1 give the nominal frontiers one and r. Changing available material, rather than arbitrarily assigning a payoff penalty, produces the comparison.

For the exact example above, choosing eta=11/600 and zeta=1/100 gives Y=289/300, while r=64/75. Every peaceful optimum gives B at most 11/100, below its combat value 16/75. The unanticipated loss is 11/300 of the nominal stock. More generally eta can be arbitrarily small for fixed r,s, so the family has no uniform physical-state robustness radius as its bonus is narrowed. A fixed chosen positive eta can still have local slack; this is a family-level nonuniformity, not a claim that every fixed goal fails under every tiny perturbation.

If the physical signal arrives before installation and a new goal can be chosen and executed at its actual costs, the parties may repair this failure. A contingent goal library must confront note 028's common-output and information constraints. Neither repair follows from merely reducing the optimization-regret parameter.

## 7. Limits

The limiting goal as eta tends to zero need not be continuous. The theorem uses finite positive eta for every strict sub-bound and claims a supremum, not strict deterrence at the boundary. A restricted goal library, cost tied to description complexity or correlated implementation errors could change the achievable allowance. Section 6 makes two particular limits precise rather than treating all meanings of robustness as interchangeable. The normalization is an explicit implementation comparison, not interpersonal utility comparability.

An enforceable fixed-utility delegate that implements the same conditional physical policy with the same error sets matches this local outcome comparison. The theorem supplies no independent reason to prefer utility modification over that control. C1 should leave both concavity and the mechanism's error model open to future recurrences.
