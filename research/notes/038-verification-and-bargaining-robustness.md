# R0002 working derivation: verification and bargaining robustness

**Local robustness calculations for the staged 036–037 mechanism; contributing-agent self-check.** These checks seek conditions that preserve an adopted productive agreement and conditions that change its bargaining value. Neither perfect arbitrary-goal verification nor a universal commitment obstruction is assumed. They retain 037's physical-menu limitation. R217 and 046/058 provide the final guarded module's different error/perturbation bounds; the proposer-rights closure here remains conditional.

## 1. A verified parameter interval suffices

Exact public knowledge of lambda is stronger than the productive mechanism needs. Suppose a sound certificate establishes that the installed goal belongs to the template x+lambda y with

$$\lambda\in[\underline\lambda,\overline\lambda],\qquad
\lambda_0<\underline\lambda\leq\overline\lambda<1.$$

All types in this interval strictly work when B works at the default split. B's own default work incentive is independent of A's precise lambda, since the actual action and output law are the same. Therefore every posterior supported on the certified interval admits the same mutual-effort continuation, including after a rejected offer. Each actual A type has the same efficient fallback law Q and independently applies 036's certificate. Every accepted continuation gives its founder at least r_A. Consequently B cannot gain by screening these types through a menu of accepted contracts: every type's founder floor is the same and total surplus is at most C.

This is a robustness result to private parameter variation and bounded installation error within a verified template. It still assumes sound evidence of family membership and the interval. Self-knowledge or a textual declaration is not such evidence. A failed or unsound certificate needs a different game, including its resulting beliefs and proposal incentives.

In the 037 fixture, lambda_0=5/33. A target 1/5 has a symmetric admissible error radius smaller than

$$1/5-5/33=8/165.$$

Thus a public certificate of lambda in [9/50,11/50], for example, preserves strict default incentives. Exact goal identification is unnecessary. The finite verification cost must fit the physical ledger.

## 2. Unsound certification changes the strategic question

For a preliminary binary-type check, suppose the default's A is truly changed with posterior probability pi and otherwise retains the original goal. A changed type works when B works, while the original type shirks. At the numerical default, original B's work-versus-shirk gain is

$$\frac{11}{2}\left[\frac1{10}+\frac15\pi\right]-\frac85
=\frac{11}{10}\pi-\frac{21}{20}.$$

B therefore works only when pi>=21/22. This threshold is a local Bayesian effort check, not a complete verification equilibrium. The small B effort margin in the example makes false certification consequential.

In particular, observing rejection of a screening offer can change B's posterior. A fallback that was attractive under the original posterior may then disappear. One cannot insert the old efficient Q into the acceptance certificate without checking these beliefs. Strategic attempts to fake the certificate, and the available verification/repair choices, remain part of the full imperfect-information problem. A sound interval certificate is the constructive repair established above; the binary posterior calculation identifies a concrete boundary for the unsound alternative.

## 3. A proposer-rights comparison to be integrated

The B-proposer rule in 037 is consequential. Consider an explicitly richer bargaining-closure benchmark: when the default is unproductive, the selected proposer can implement maximum net surplus C using voluntary goal changes and collateralized output contracts, and the responder is left at its current zero reservation value. Such implementation requires the current-self and timing checks of 037; it is not supplied by the word bargaining.

Let A become proposer with probability theta and B otherwise. Suppose B's incumbent goal is y. If A has chosen a low parameter lambda<lambda_0, the A-proposer branch gives A C, while the B-proposer branch gives A -lambda C/(1-lambda). Thus its original expected project payoff is

$$F_\theta(\lambda)=C\frac{\theta-\lambda}{1-\lambda}.$$

For theta<1, this decreases in lambda, with derivative -C(1-theta)/(1-lambda)^2. Its best low-goal value is theta C, attained by the original goal lambda=0. The efficient productive default instead supplies r_A, independently of proposer identity because both current agents strictly prefer their own project at a fixed total and can reject reallocations.

Within this closure benchmark, choosing the productive compromise is strictly preferable to retaining the original goal exactly when

$$r_A>\theta C.$$

The same inequality prevents a high-lambda current self from benefiting by hardening back to a low lambda before the bargaining lottery: all resulting routes have the same total C, so that current self ranks them by founder x. Equality gives indifference; theta C>r_A favors the stronger original-goal bargaining alternative. In the fixture the boundary is theta=1/4.

This is a useful candidate broadening from monopoly proposal rights to an interval of bargaining environments. Its full-game status is still provisional: respondent goal changes must be installed voluntarily before the incentives they support are used; collateral must suffice in every outcome; late renegotiation can change zero reservation values; and newly available binding policy commitments must be compared. No claim about an arbitrary bargaining protocol or infinite sequence of reopened negotiations follows from the algebra alone.

## 4. A uniform neighborhood of original project preferences

The linear original goals in 037 can be perturbed. Suppose the original goals are commonly known, continuous, strictly increasing f_A(X), f_B(Y), with normalized representations satisfying

$$|f_i(z)-z|\leq\delta\quad\text{for }0\leq z\leq16.$$

This is a quantitative preference class, not a claim about a distribution of natural agents. Existence of such a positive-affine normalization is the relevant condition; an arbitrary rescaling cannot be inserted into the numerical bound.

If delta<1/40, original B's default work margin 1/20 remains positive: an expected-utility comparison changes by at most 2delta. Original A's unchanged default still strictly shirks, and the other strict effort/attack margins used below persist. A can install the same linear compromise goal as before. Its efficient fallback then protects E X>=3+1/5 over all accepted continuations, giving original utility at least 3+1/5-delta.

To bound the Keep alternative, start with 037's lambda=0 contract and add a constant transfer 2delta to A in both success and failure states. Original A's expected project output is then 3+2delta, so its expected f_A is at least 3+delta>=f_A(3). Its strict effort margin remains at least 1/20-2delta. B can install mu=1/5; its linear effort comparison is unchanged by a constant transfer. The candidate gives original B expected project output 3+4/5-2delta.

After B installs that linear other-regarding goal, its actual maximizing proposal gives at least the candidate's current value. Since the candidate already attains maximum expected total output, the same efficient-fallback algebra bounds its actual expected Y below by 3+4/5-2delta. Original B therefore evaluates this available initial route at least as highly as 3+4/5-3delta. Whatever its optimal initial response to Keep, it obtains original utility at least this much, hence E Y>=3+4/5-4delta. The physical total bound yields E X<=3+4delta, and original A's Keep utility is at most 3+5delta.

Thus A's original-utility gain from the changed-goal route is at least

$$\frac15-6\delta>0\qquad(\delta<1/40).$$

This extends the strict adoption construction to a uniform neighborhood containing mildly concave, convex and other increasing original project utilities. It does not rely on sample frequencies or assert that the neighborhood is large. The exact original functions are common knowledge here; a private-type version requires conditioning the proposer-optimality bound correctly. Larger risk aversion motivates the insured construction developed next.
