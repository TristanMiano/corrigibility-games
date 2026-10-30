# Elementary baselines and boundaries

Date: 2026-10-30. These are initialization benchmarks, not a completed CG-R001 run. Proofs below are direct elementary derivations. They are not independently reviewed, machine verified, or asserted to be novel. See [L01](../LITERATURE.md) for the related standard bargaining-range literature and [L02](../LITERATURE.md) for the self-modification evaluation issue.

## B01 — The linear bargaining range

Let P,W >= 0 be usable resource amounts after peaceful and combat pathways respectively. They are **assumed net amounts here**, not derived physical laws. Agent A wins a winner-take-all combat lottery with probability q in [0,1]; B wins with probability 1-q. Agent i values only the final resource allocated to its objective, linearly. Defeat yields zero; there are no additional process, death, identity, or modification terms. Both use the same lottery probabilities.

Peace allocates x to A and P-x to B, with 0 <= x <= P. Strict preference over combat requires

$$
x>qW,\qquad P-x>(1-q)W.
$$

Thus the acceptable set is

$$
(qW,\ P-(1-q)W).
$$

Its length is P-W. Since qW >= 0 and P-(1-q)W <= P, it contains a feasible x exactly when P>W. This proves B01, including q=0 or q=1: a tiny positive allocation can strictly benefit a zero-win-probability agent when there is surplus. When P=W, a weakly preferred division exists but none strictly improves both agents.

Power shifts the division but not the interval's width in this model. This says nothing about bargaining selection, enforcement, preemption, dynamic stability, or why P exceeds W physically. In particular it does not require utility modification at all.

## B02 — An explicit successor objective

For P>0 and a chosen share s in (0,1), suppose a merged executor can be installed and chooses nonnegative x_A,x_B with x_A+x_B <= P. Give it

$$
U'_s(x_A,x_B)=\min\{x_A/s,\ x_B/(1-s)\}.
$$

Writing its achieved value as v, feasibility implies x_A >= sv and x_B >= (1-s)v, hence v <= x_A+x_B <= P. The allocation (sP,(1-s)P) attains v=P. Equality forces both coordinate bounds to be tight, so the maximizing allocation is unique.

For 0<q<1, choose s=q. If P>W, each original linear utility strictly prefers that allocation to its combat expectation. This evaluates adoption using the originals, not U'_s. Endpoint q values can instead use an interior split in B01's interval.

The construction is conditional on the feasibility of installing and executing the objective. It does not prove that installation is verified, simultaneous, durable, or safe from later attacks or self-modification. A fixed-utility contract could implement the same allocation if the implementation technology permits it; that comparison is essential.

By contrast, simply maximizing theta*x_A+(1-theta)*x_B on the simplex usually selects an endpoint: all to A if theta>1/2, all to B if theta<1/2, and indifference if theta=1/2. A utility mixture is not automatically a proportional compromise.

## B03 — Finite freezing penalties and combat bonuses

Now assume every agreement in the **particular update mechanism under study** changes both agents' preferences, incurring finite penalties kappa_A,kappa_B >= 0 under their original utilities. Combat in this seed causes no utility rewrite and delivers bonuses beta_A,beta_B >= 0, if specified. All quantities are in the seed's resource-utility normalization; these are not sums of arbitrary incomparable utilities.

Original expected payoffs are

$$
\begin{aligned}
V_A^M&=x-\kappa_A,&V_A^C&=qW+\beta_A,\\
V_B^M&=P-x-\kappa_B,&V_B^C&=(1-q)W+\beta_B.
\end{aligned}
$$

Strict preference for the update by both agents requires

$$
qW+\beta_A+\kappa_A<x<P-(1-q)W-\beta_B-\kappa_B.
$$

The lower endpoint is nonnegative and the upper endpoint is at most P. The interval is therefore feasible and nonempty exactly when

$$
P-W>\kappa_A+\kappa_B+\beta_A+\beta_B.
$$

This proves B03 by subtracting endpoints. Equality permits indifference at a single allocation, not a strict improvement for both. Larger freezing penalties or direct combat bonuses can remove this mechanism's bargaining range.

**It does not follow that combat is chosen.** If ordinary peace can implement the same allocation without utility changes, its kappa penalties are zero. For P=10, W=8, q=1/2, and kappa_A=kappa_B=2 with no combat bonuses, the update interval is empty, yet ordinary trade at x=5 strictly beats combat's (4,4). A frozen terminal utility can support peace. To establish genuine combat appeal, compare against the entire feasible peaceful set and account for strategic adoption.

Capture-induced rewrites, additional survival preferences, asymmetric losses, and endogenous bonuses alter these formulas and must be modeled explicitly rather than treated as covered by this example.

## B04 — A long horizon need not defeat freezing

Consider a separate single-agent decision whose original utility penalizes one modification by kappa >= 0. Suppose modifying produces an exogenous gain g>0 in original goal satisfaction each period t=0,...,T-1 relative to not modifying. No extra penalties recur. With 0<=delta<1,

$$
\Delta_T=g\sum_{t=0}^{T-1}\delta^t-\kappa
=g\frac{1-\delta^T}{1-\delta}-\kappa.
$$

The geometric-series identity proves this formula. Modification is strictly preferred exactly when Delta_T>0. As T grows, the gain converges to g/(1-delta). If kappa >= g/(1-delta), no finite horizon yields strict preference for modification. If kappa < g/(1-delta), some sufficiently long finite horizon does. For delta=0, the gain is already g at every T>=1 and the same criterion applies.

For example, g=1 and delta=1/2 never strictly outweigh kappa=2, but do outweigh kappa=3/2 by T=3. Thus finite freezing can be overcome, yet extending the horizon is not a universal argument against it. Endogenous opportunity gains and commitment benefits are the actual research problem; the exogenous-gain calculation is only a benchmark.

Lexicographic preservation is a different preference class: an agent that strictly ranks every preserving trajectory above every modifying trajectory cannot prefer modification while a preserving option remains, by that definition. A descendant population could nevertheless lose ground under a separately defined fitness process. This logical observation is neither a proof that such preferences are evolutionarily stable nor a reason to assume they disappear.

## Reproducible checks and next obligations

Run `python -m unittest discover -s tests -v` from the repository root. The exact-arithmetic checks cover example allocations, interval identities, boundaries, the max-min executor on a finite grid, and the geometric sum. Tests are not proofs of dynamic behavior or thermodynamics.

Next derive P and W (or the appropriate non-scalar frontier) from physical transition and recovery models, embed peaceful options in a game with persistent combat, and analyze voluntary freezing changes separately from population selection. Those obligations remain open in [the claim ledger](../CLAIMS.md).
