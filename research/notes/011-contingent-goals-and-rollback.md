# R0001 working note — late goal changes, credible threats, and rollback

This continues E2 with a broader update menu. The two-round restriction in note 010 is an informative local model, not a claim that capable agents cannot update later. The claim ledger registers the results; their review remains contributing-agent self-check only. Combat remains available before and after installation. A conditional equilibrium calculation must specify the selected continuations; weak mutual-attack equilibria are not silently discarded.

## 1. The operator can still change its goal

Condition on A being selected to operate the production equipment. Before this draw the probability of selecting A is its strength share s=a/(a+b); its combat victory probability remains s after selection. The other agent retains the ability to attack. Original goals are u_A=x_A and u_B=x_B. Available production totals and their physical transitions must be supplied by the recovery module, not assigned as intrinsic utility penalties.

At a late installation opportunity, immediate combat would permit output W_0>0. Paying a declared installation work/time cost leaves peaceful output P and post-installation combat output W_1, with 0<W_1<=W_0 and P>W_1 in the following comparison. The inequality W_1<=W_0 is a local monotone-budget assumption; a changed power/capture technology can invalidate it. An administrative Keep can pay the same overhead, or be costless; in either case its resulting unmodified combat continuation is no better for A than immediate combat. Rejection is not defined to cause war: the final production game contains every ordinary allocation, and its uncommitted original-goal players generate the conflict as in note 010 section 14.

The installed goal is publicly observed and reliable in this module. A can choose an output-only homothetic objective

$$G_\alpha(x)=\sqrt{\alpha x_A}+\sqrt{(1-\alpha)x_B},\qquad 0<\alpha<1.$$

On the nonnegative simplex x_A+x_B<=Y it uniquely chooses (alpha Y,(1-alpha)Y) with value sqrt(Y), by Cauchy–Schwarz or the weighted-concavity argument in note 010. Crucially it makes the same proportional choice after winning a war. B remains original and produces only B's color if it wins.

After installation, B's combat value is therefore

$$s(1-\alpha)W_1+(1-s)W_1=W_1(1-s\alpha).$$

The lower value (1-s)W_1 would incorrectly treat a G_alpha survivor as still selfish. B accepts the peaceful production continuation exactly when

$$ (1-\alpha)P\ge W_1(1-s\alpha),\quad\text{or}\quad
\alpha\le h(s)=\frac{P-W_1}{P-sW_1}.$$

A's current G_alpha value of peaceful production is sqrt(P). Its combat value is

$$\sqrt{W_1}\,[s+(1-s)\sqrt{1-\alpha}]<\sqrt P.$$

Thus its new self does not want to attack in the proposed peaceful continuation. Production of the target allocation is its actual best response, not an assumed promise. B's weak inequality allows indifference; a strictly smaller alpha supplies a strict attack-deterrence margin.

## 2. Consent before the installation cost is sunk

Before the update, B can also attack. Its participation requires (1-alpha)P>=(1-s)W_0. A evaluates changing its goal under x_A, requiring alpha P>=sW_0. The largest peaceful operator share satisfying both of B's checkpoints is

$$\bar\alpha=\min\left\{1-\frac{(1-s)W_0}{P},\ \frac{P-W_1}{P-sW_1}\right\}.$$

A strictly beneficial share with strict B deterrence at both checkpoints exists iff

$$P>W_0,\qquad P(P-W_1)>sW_0(P-sW_1).$$

Proof: the permitted interval is (sW_0/P,bar-alpha), and both denominators are positive. The first upper bound exceeds the lower one precisely when P>W_0; the second does so precisely at the displayed second inequality. These conditions imply the interval intersects (0,1), since all combat values are positive.

**Protocol requirement for adoption.** This interval is first a participation/execution result. The adoption equilibrium discussed below assumes that the proposed alpha is the actual installer choice, bound before B allows the relevant outside-option-reducing costs, or that any revision is observable early enough to reopen B's attack response. Public observation only after installation is insufficient. Note 020 supplies a strict finite counterexample: an original proposer revises the goal choice after preparation, even though the initially proposed split passes every displayed inequality. The required binding or timely-response capability is an instance assumption, not a consequence of utility self-knowledge or a C1 default.

When inequalities are weak and feasible, the upper endpoint maximizes original A's peaceful payoff, conditional on selecting the peaceful response at B's indifference. Under strict deterrence alone the supremum can fail to be attained: one can take alpha arbitrarily close below the endpoint, but there need not be a best strict offer in a continuum. Do not silently call that limiting offer an equilibrium. A finite offer grid, a specified tie-breaking selection, or an explicit bargaining protocol resolves a different problem.

An off-path offer above the post-installation bound can be met by the final-stage war equilibrium. Its old-A payoff is s alpha W_1<=sW_0, so it cannot beat a strictly beneficial peaceful installation. An off-path early attack is also no better. Together with the bound-choice/timely-response protocol just stated, this supports an adoption equilibrium when the endpoint/response rule is specified; it does not force adoption in all equilibria or eliminate the simultaneous-attack coordination equilibria. An unsecured declaration does not supply the same deviation constraints.

## 3. Equal-cost benchmark and a nontrivial power boundary

Set W_0=W_1=W and let r=W/P in (0,1). The post-installation bound h(s) is stricter than B's initial participation bound, because

$$\left[1-(1-s)r\right]-\frac{1-r}{1-sr}
=\frac{s(1-s)r^2}{1-sr}>0.$$

The original operator strictly prefers some strictly accepted homothetic goal to immediate combat iff

$$f(s,r)=1-(1+s)r+s^2r^2>0.$$

For a fixed s this holds exactly below the smaller root

$$r_*(s)=\frac{2}{1+s+\sqrt{1+2s-3s^2}}.$$

The other root lies above 1 for 0<s<1. At s=1/2, r_*=3-sqrt(5), about 0.764. Thus P>W alone is insufficient: the modification makes B partly benefit even from losing the war, and a modest production surplus can no longer compensate the original A for that softened threat.

The worst strength is s=2/3, where r_*=3/4. Equivalently, for fixed r, f(s,r)=r^2(s-1/(2r))^2+3/4-r. For 0<r<3/4 it is positive for every interior s; at r=3/4 it vanishes only at s=2/3; for 3/4<r<1 it is negative between

$$s_\pm(r)=\frac{1\pm\sqrt{4r-3}}{2r}.$$

Both endpoints lie in (0,1) in that range. These are properties of the **output-only homothetic goal menu**, not general restrictions on all possible self-modification. They also concern a late operator's adoption, not population frequencies.

## 4. A history-contingent goal preserves the original war response

The common outcome domain may include whether combat occurred. An installed utility can be a fixed function of that history, without undergoing another utility change when a combat event happens. Consider

$$V_\alpha(H)=
\begin{cases}
\min\{x_A/\alpha,x_B/(1-\alpha)\},&\text{no combat},\\
x_A,&\text{combat occurred}.
\end{cases}$$

For 0<alpha<1, peaceful production uniquely maximizes the first branch at (alpha P,(1-alpha)P), with value P. After combat, an A-survivor actually maximizes x_A and produces only its own color. B's post-installation threat is now (1-s)W_1. At the pre-combat checkpoint, A's installed criterion gives peaceful value P and expected war value sW_1<P, so it prefers peace while retaining the physical attack action. This uses a finite history-dependent preference, not an infinite combat cost.

For W_1<=W_0, the stricter B constraint is its initial opportunity to attack: (1-alpha)P>=(1-s)W_0. A's old criterion still requires alpha P>=sW_0. Strict mutual participation and strict post-installation deterrence are possible iff P>W_0. This recovers the ordinary bargaining surplus condition under a richer successor-objective menu.

This is not a theorem that arbitrary goal blending preserves threats. The objective explicitly distinguishes peaceful and wartime production. Such a state-contingent goal is a physical implementation obligation, with its verification, failure, cost and rollback properties to be compared against a **fixed-utility contingent delegate** implementing exactly the same policy. The delegate can reproduce the result if granted the same execution technology. Merely keeping the original utility with a revocable promise does not supply that commitment.

## 5. Rollback after a successful installation

Suppose the target allocation is actually executed on the peaceful path. G_alpha attains its maximum sqrt(P) over every feasible physical allocation with total output at most P. Therefore a later change to another objective cannot increase its current expected value if all resulting continuations are lotteries over that same physical feasible set. Any combat continuation with total output at most W_1<P has strictly smaller G_alpha value, even allowing different survivor policies. This establishes **no profitable rollback**, not a prohibition on changing.

Returning specifically to original u_A leads, against original B under the uncommitted final production game, to war. With post-rollback output W_R<=P, the old installed G_alpha evaluates that outcome at

$$\sqrt{W_R}\,[s\sqrt\alpha+(1-s)\sqrt{1-\alpha}]<\sqrt P,$$

where strictness holds for interior alpha,s even when W_R=P, since both square-root coefficients are below one. The founder would prefer other distributions in many cases, but the acting self no longer evaluates by the founder's x_A alone.

Likewise V_alpha's peaceful value P bounds every attainable noncombat continuation when total output<=P, and every combat continuation has V_alpha=x_A<=W_1<P. It cannot gain from rollback under these conditions. An alternative objective implementing the identical peaceful outcome may tie; a positive update cost only makes all changes strictly worse if it actually lowers the current criterion's attainable maximum. Cost spent from slack need not do that.

The fixed-feasible-set assumption is substantive. A publicly observed change could unlock a new coalition, technology or offer with output beyond P, and then this argument would not apply. A merger can also change which selves exist. This local no-profitable-rollback argument is not a claim of general goal-content immutability or of an irreversible installation.

### Which of the two threat dates binds?

The initial B-participation bound is no larger than the post-installation bound iff

$$P(W_0-W_1)\ge sW_0W_1.$$

To verify, cross-multiply the positive denominators in
\(1-(1-s)W_0/P\le(P-W_1)/(P-sW_1)\), cancel P squared, and divide by 1-s. Thus sufficiently costly delay can make the **earlier** attack opportunity bind even though the later goal change softens the war response. When W_0=W_1>0, the later softening bound always binds. This is a joint physical/timing effect, not a constant utility charge.

## 5a. Behavioral replication is not automatically equilibrium replication

Consider an original-u_A controller using a revocable production program that recommends (alpha P,(1-alpha)P). Immediately before the finite terminal production action it can either execute that program or override it with any allocation. B chooses Attack or Continue simultaneously with that last choice; a late override is not observed soon enough to change B's already selected action. Both versions retain the same low-level production and attack actions and the same physical costs and information.

If B continues with positive probability, the fixed-u_A controller strictly prefers overriding with all-A production. Against that behavior, original B strictly prefers combat to receiving zero, provided its combat value is positive. Hence no equilibrium of this unprotected fixed-utility version has a positive probability of peaceful production. This is the same final-stage argument as E2-U, now explicitly applied to a revocable policy program.

For an installed G_alpha or V_alpha satisfying the earlier participation bounds, target production is a best response of the current self, even though the same override is physically available. A rollback that atomically changes the goal and produces all A is evaluated by the pre-rollback G_alpha or V_alpha, so it also fails to improve the current self's payoff. The difference here is incentive compatibility, not a smaller physical action set for the modified controller.

A binding fixed-utility delegate, a separate controller that cannot be overridden before execution, a timely observable revocation followed by a response window, or enforceable clawback can reproduce the desired allocation with unchanged founder utility. Each changes the execution/observation/agency technology of the revocable-program example. This is why note 010's R113 equality of history laws is conditional: matching an advertised policy is weaker than ensuring that policy is rationally executed at every later decision.

Formally, a correspondence between two protocol histories preserves a selected equilibrium only if the chosen action at every corresponding decision history is a best response for the acting criterion in **both** implementations, given their actual deviation menus and mapped continuations. A sufficient condition is equality of the ordering of all attainable unilateral-deviation continuation lotteries under those two criteria, together with the physical/observation correspondence. One then transfers each best-response inequality individually. Positive affine equivalence on the relevant domain suffices but is stronger than necessary on restricted deviation menus. R113 alone proves neither those inequalities nor that a fixed-utility controller can be treated as a committed executor for free.

Conversely, a single history where the mapped action is strictly dominated under the fixed utility defeats equilibrium replication with that unchanged deviation menu, even if the desired on-path outcome law is identical. Here, producing all A rather than the promised interior split supplies that deviation when B continues. This is a scoped implementation separation relative to revocable policy technology, not a theorem that goal modification outruns equally capable binding commitment.

## 6. Strength-proportional expectations can depend on the goal menu

In the equal-cost benchmark, suppose both possible operators adopt their largest weakly accepted share with the specified peaceful tie selection. Under V_alpha, operator A keeps P-(1-s)W and operator B leaves A sW. Since the operator draw selects A with probability s, original A's expected output is

$$s[P-(1-s)W]+(1-s)sW=sP.$$

Thus strength-proportional **expected** shares emerge even though the realized allocations differ according to who operates. A deterministic proportional world and this lottery are still different outcomes for nonlinear preferences.

For output-only G_alpha, when both operators' adoption inequalities hold, their maximal shares are h(s) and h(1-s). Direct calculation gives

$$\frac{\mathbb E[x_A]}P-s
=\frac{s(1-s)(1-2s)r^2}{(1-sr)(1-(1-s)r)}.$$

The weaker agent gets more than its raw strength share and the stronger less, except at equal strength or the zero-war-output limit. This is an implementation effect of goals that remain compromising after a war, not a change in the strength-weighted control or combat rules. Both agents can still gain relative to war when the stated conditional adoption inequalities hold. Do not extend the formula to states where one operator rejects the proposed goal: those states have a different continuation law.
