# R0002 working derivation: allocation safeguards over rich renegotiation menus

**Local certificate and scoped adoption benchmark, registered as R203; contributing-agent self-check.** This note extends 012's chosen accommodation/safeguard question from a finite goal menu to a class of output criteria and all lotteries over a bounded physical opportunity set. The target is constructive: identify a genuine goal an original project seeker can choose instrumentally, and determine when its protection survives transfers and further goal changes. The corresponding failure boundary concerns this declared class, not all accommodation. Note 035's ordinary late-offer repair changes the benchmark used here; [E3](../models/E3.md) gives the final integrated productive construction.

## 1. A bounded physical outcome class and a chosen successor

Original A and B value final project quantities x and y, respectively. Let T=x+y and let

$$K_P=\{(x,y):x,y\geq0,\ x+y\leq P\},\qquad P>0.$$

P is the actual maximum output after the declared communication, verification, production and update costs. It is not an arbitrary utility prize. The later physical construction must justify a common bound across all relevant transfers and continuations. Delivered quantities count in the totals, so producing B's output early does not remove it from the successor's evaluation. Combat, ordinary allocations and further changes remain available as specified in the game.

A can install a criterion, with parameters fixed at installation,

$$U_{\alpha,\kappa,\psi}(x,y)
=T-\kappa P\,\psi\left(\frac{|x-\alpha T|}{P}\right),$$

where 0<alpha<1, kappa>0, and psi:[0,1]->R_+ is convex, strictly increasing, Lipschitz with constant L, and psi(0)=0. Assume

$$\kappa L\max\{\alpha,1-\alpha\}<1.$$

The first term values total useful output; the second penalizes deviation from the chosen allocation proportion. This is an output preference, not a code-identity or goal-change-event penalty. Positive affine recodings leave its ordering unchanged. A evaluates installing it using original x; subsequent decisions use the installed criterion.

**Basic properties.** U is concave because the imbalance term is convex and T is affine. Raising x by d>0 changes its imbalance argument by at most (1-alpha)d/P, so its utility gain is at least [1-kappa L(1-alpha)]d>0. Raising y similarly gives a gain at least [1-kappa L alpha]d>0. On a total-output simplex of capacity Y<=P, monotonicity uses all Y and the unique maximum is (alpha Y,(1-alpha)Y), where U=Y. The goal genuinely changes original A's preferences: at total P it strictly prefers this interior allocation to (P,0), while original A strictly prefers (P,0).

## 2. A partial-production continuation with retained attack

Use the explicitly declared random-operator authority from E2: A's successor F is selected with probability s in (0,1), B with probability 1-s, and both remain capable of attack after selection. A war has winner output W=rP, 0<r<1, and F wins with probability s. F's survivor maximizes its actual U; B's survivor maximizes y. Thus F's victory produces (alpha W,(1-alpha)W), while B's produces (0,W).

The candidate peaceful fallback Q is

$$Q=s\,\delta_{(\alpha P,(1-\alpha)P)}
 +(1-s)\,\delta_{(0,P)}.$$

Its original-A mean is s alpha P; B's value and F's current value are

$$d_B=(1-s\alpha)P,\qquad
L_F=P-\kappa P(1-s)\psi(\alpha).$$

The nonoperating B restrains from attack strictly when

$$ (1-\alpha)P>(1-s\alpha)W,
\quad\text{equivalently}\quad
\alpha<\bar\alpha(s,r):=\frac{1-r}{1-sr}.$$

The nonoperating F restrains strictly when its all-B peaceful value exceeds its actual combat value:

$$P-\kappa P\psi(\alpha)
>W-\kappa P(1-s)\psi(\alpha r).$$

Equivalently,

$$\kappa<\frac{1-r}{\psi(\alpha)-(1-s)\psi(\alpha r)}.$$

The denominator is positive. Thus sufficiently small positive kappa satisfies this condition and the monotonicity condition whenever r<1. The operators themselves prefer their maximizing production, of current value P for F and P for B, to their combat values. These inequalities support the selected peaceful fallback. Weak mutual-attack coordination remains possible in the simultaneous-attack game; this note has not supplied a universal equilibrium-selection result.

## 3. Exact protection against all accepted output lotteries

Let mu be any probability law on K_P whose *actual complete continuation* gives the current F at least L_F. It may involve deterministic transfers, randomized final goals, goal-preserving prepayment or later genuine changes. Those mechanisms must be implemented and evaluated under the current criterion, not approved merely by a proposed successor's new utility. For this bound, giving the proposal menu every law on K_P is a conservative enlargement even when physical technology implements only a subset.

Define

$$q_\psi=P\left[\alpha-\psi^{-1}\big((1-s)\psi(\alpha)\big)\right].$$

Then

$$\boxed{\mathbb E_\mu x\geq q_\psi.}$$

**Proof.** Increasing y at fixed x to the full-output frontier can only increase U, so

$$U(x,y)\leq P-\kappa P\psi(|x/P-\alpha|).$$

Concavity of the right side as a function of x and Jensen give

$$\mathbb E U\leq P-\kappa P\psi(|\mathbb E x/P-\alpha|).$$

Combining with E U>=L_F yields the bound. It is sharp: the deterministic full-output allocation (q_psi,P-q_psi) has U=L_F. Compactness and continuity make this a minimum, not only an infimum. No claim that a vNM utility uniquely chooses an interior lottery is used; the attaining proposal is deterministic.

Convexity gives psi((1-s)alpha)<=(1-s)psi(alpha), hence

$$0<q_\psi\leq s\alpha P.$$

Strict convexity on the relevant chord makes the upper inequality strict. The gap is the amount of original-A mean output a bargaining opponent can extract by replacing the fallback's allocation uncertainty with a deterministic allocation acceptable to F. This is a positive explanation of a vulnerability and of how changing the chosen curvature reduces it.

If B can offer every implemented output lottery, F can reject to Q, and acceptance at equality is selected, B's optimal accepted proposal is the deterministic q_psi allocation. Indeed E y<=P-E x<=P-q_psi, and this bound is attained. B gets at least d_B, strictly more under strict convexity. This is a local proposal/acceptance result. Implementation checkpoints, the availability of rejection and initial adoption must be checked in the full game.

The protection covers any anticipated later goal changes because mu is their actual final output law evaluated by the current F. It is not an assumption that the original founder controls those later selves. If transfers change the attainable total-output bound, or F loses its fallback before any decision covered by this comparison, recompute the certificate; the inequalities do not silently transfer.

## 4. Power-loss family and a sharp local adoption boundary

For psi(z)=z^p, p>=1, let

$$c_p(s)=1-(1-s)^{1/p}.$$

Then q_p=alpha P c_p(s). The p=1 goal gives the maximal fallback-mean protection q_1=s alpha P; p=2 gives q_2=alpha P[1-sqrt(1-s)]. Both are genuine compromise goals. The linear loss is nonsmooth at the target; the quadratic loss is smooth. Neither uses an infinite penalty or rules out physical combat.

For the matched local benchmark where original A's best unchanged-goal continuation is sW, strict adoption protection and strict B restraint require

$$\frac{sr}{c_p(s)}<\alpha<\frac{1-r}{1-sr}.$$

Such an interval exists exactly when

$$c_p(s)(1-r)>sr(1-sr).$$

Since its quadratic is positive at r=0 and negative at r=1 for s<1, this is exactly r<r_*(s,p), where the smaller root is

$$r_*(s,p)=
\frac{2c_p(s)}{s+c_p(s)+\sqrt{(s+c_p(s))^2-4s^2c_p(s)}}.$$

For p=1 this reduces to 1/[1+sqrt(1-s)]. At equal strength the linear-loss threshold is approximately 0.586 and the quadratic threshold approximately 0.427. Above the threshold, no alpha in this specified power-loss/fallback class satisfies both strict inequalities. That is a class boundary; history-sensitive goals, a different fallback or another execution architecture can change it.

For example, P=1, W=27/100, s=1/2, alpha=4/5 and p=2 give q=(4/5)(1-1/sqrt(2))>27/200. B receives 1-q, above its partial fallback 3/5. Small positive kappa satisfies both the current-F attack and monotonicity checks. The bound covers all accepted lotteries on K_1, including the goal-preserving transfer route that bypassed 012's event-only freeze. A full staged game and matched ordinary/delegation controls are still required before promoting this local construction to an integrated adoption theorem.

## 5. A smooth repair approaching fallback-mean protection

The linear loss protects the entire original fallback mean but is nonsmooth. Let delta>0 and use instead

$$\psi_\delta(z)=\sqrt{z^2+\delta^2}-\delta.$$

This is smooth as an even function of signed imbalance, strictly convex, and 1-Lipschitz. Its inverse on nonnegative arguments is sqrt(v^2+2 delta v). Put t=1-s and A=sqrt(alpha^2+delta^2)-delta. The exact protected share is

$$q_\delta/P=\alpha-\sqrt{t^2\alpha^2+2st\delta A}.$$

Because A<=alpha,

$$\sqrt{t^2\alpha^2+2st\delta A}\leq t\alpha+s\delta,$$

and therefore

$$\boxed{q_\delta\geq sP(\alpha-\delta).}$$

Consequently any r below the linear-loss threshold admits a smooth chosen safeguard with strict adoption: choose r<alpha<bar_alpha and 0<delta<alpha-r, then choose sufficiently small positive kappa for the current-F attack condition. The strictly convex smooth loss gives B a strict improvement over its fallback at the optimal accepted deterministic proposal. The original-A protection approaches the maximal fallback mean as delta decreases. Precision and verification costs of making delta small remain implementation questions; existence of the formula alone does not make those costs zero.

## 6. Conditional comparative statics within this class

For the power loss, increasing p decreases c_p(s), hence decreases the protected share for fixed alpha and shrinks the successful r region. The mechanism is the successor's stronger preference for replacing uncertain allocations by a deterministic one, allowing the proposer to extract more of the founder's expected project output. A flatter allocation loss near this bargaining region preserves more of that output; this is a chosen-goal design comparison, not a claim that risk aversion universally favors combat.

For fixed p, c_p(s)/s is nondecreasing in s: c_p is convex with c_p(0)=0, so its secant slope from zero increases. In the adoption comparison,

$$\frac{c_p(s)}s\frac{1-r}{1-sr}>r,$$

both factors on the left are nondecreasing in s (the second strictly so for r>0). Thus a larger strength share for the prospective modifier enlarges this locally successful class when kappa can also be chosen to satisfy its current-self attack check. This explicitly varies both ordinary operator authority and combat odds. It does not hold fixed every other current-self incentive by fiat.

At fixed strengths and goal parameters, increasing P while W remains fixed raises q in proportion to P and relaxes B's restraint condition. If a capability change alters W, the fallback, or the bargaining protocol as well, those actual changes must enter the comparison.

## 7. Disposition after integration

Section 5 supplies the smooth repair and its local margin. Notes 035–040 test ordinary late offers, productive commitments and future-goal guards; 045 exposes an unprotected physical fallback. The final conditional adoption construction uses the productive certificate and strengthened guards in E3/046/049/056, with controls and costs in 042–044/057. It is a different integrated environment, not a proof that every initial game implementing this allocation-loss family has the same result. Further use of this local family must still supply its actual ordinary alternative, credible dated fallback and installation protocol. Constructive adoption and failure boundaries should both be tested over that enlarged game.
