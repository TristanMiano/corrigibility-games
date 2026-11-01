# R0002 robustness: verification cost, concern and changing opportunities

**Conditional design bounds derived from the same protected-continuation mechanism.** Capability can improve verification or expand production while also changing costs and bargaining temptations. The useful question is which measured changes preserve the adoption and restraint inequalities. These modules quantify those checks; they do not replace the physical and strategic implementation premises of E3.

## 1. Repeated verification has a cost as well as a security benefit

Let a fixed verification design use n layers. An honest compatible pair gives original agent i nominal payoff q_i(n)=q_i^0-cn, where c is that agent's material cost per layer. Suppose the probability that any honest pair property needed by i fails at a layer, conditional on prior successful layers, is at most alpha. The union bound gives honest failure probability at most n alpha. Assume 0<=n alpha<=1 and original payoffs in [0,M]. Then its expected original payoff is at least

\[
(1-n\alpha)q_i(n).
\]

An incompatible deviation gives at most R_i if all security properties hold. Suppose each layer has a uniform conditional false-acceptance bound p, including after the adversary observes earlier passes. Requiring all n layers to pass gives false acceptance probability at most p^n by the chain rule; independence is unnecessary under this stronger conditional premise. With at most N adaptive attempts, the union bound is Np^n. Thus the incompatible payoff is at most

\[
R_i+Np^n(M-R_i).
\]

A sufficient strict-adoption margin is therefore

\[
\boxed{F_i(n)=(1-n\alpha)(q_i^0-cn)-R_i-Np^n(M-R_i)>0.}
\]

For each fixed design n, 046's finite restricted-game argument then supplies a compatible equilibrium under its uniform continuation bounds. It does not identify the optimal n when verification design itself is strategic. The false-acceptance premise concerns every adaptive malicious input; an average benchmark failure rate does not imply it. The honest bound alpha is per *paired layer*, including both relevant honest checks, so it is not silently missing a factor for the second agent.

### Exact linear witness

Use the linear productive payoffs, with per-agent fixed installation loss 1/25 and per-layer material loss c=1/100. Thus q_A^0=79/25, q_B^0=89/25, R_i=3 and M=16. Let alpha=1/1000, p=1/10 and N=2. Agent A's margin is the binding one. Exact substitution gives:

| Layers n | Lower honest A payoff | Upper incompatible payoff | Certified margin F_A(n) |
| --- | ---: | ---: | ---: |
| 2 | 3.13372 | 3.26 | -0.12628 |
| 3 | 3.12061 | 3.026 | 0.09461 |
| 4 | 3.10752 | 3.0026 | 0.10492 |
| 5 | 3.09445 | 3.00026 | 0.09419 |

Among n=1,...,14, the sufficient inequality holds exactly for n=3,...,12. Its largest certified separation occurs at n=4, while the honest-pair payoff decreases with n. These are different design criteria: largest security margin is not automatically the original agent's preferred tradeoff. Failure of this conservative bound at n=1,2,13,14 is not proof that accommodation fails there.

Improving the conditional false-acceptance rate to p=1/20 makes n=2 sufficient: its margin becomes 0.06872. Thus a specified verification improvement certifies accommodation at a lower checking cost. More repetitions at unchanged accuracy eventually consume the productive gain.

The n=1 material total matches the earlier 1/20 per-agent implementation loss. In a schedule variant with each layer taking one slot and 1/100 work per checker, n layers deliver the default output by time 18+n and use at most 10.402+0.02(n-1) work. For n<=14 these fit the 32-slot, eleven-work budget. Increased material costs reduce each linear failure holding to 34/25-n/100, still above 4/11 throughout that range. Two attempted forgeries are an upper bound in the declared retry policy; an attempt that leaves no time for the certified continuation cannot gain entry. The calculation does not supply the assumed verifier technology or a full imperfect-information implementation equilibrium; it propagates explicit uniform error bounds through the existing adoption test.

## 2. Other-regard helps restraint but can spend the original-welfare margin

At a safe renegotiation checkpoint, let a default give expected original outputs q_A,q_B and total S=q_A+q_B. A current A values X+lambda Y, with 0<=lambda<1; its already fulfilled process reward cancels. Suppose the available total frontier is now at most S+g, g>=0, and acceptance may lose epsilon in current-utility units. The certificate gives

\[
E X\ge q_A-\frac{\lambda g+\epsilon}{1-\lambda}.
\]

If the original adoption margin above its dated outside value is m=q_A-d_A>0, this bound preserves a strict original gain exactly when

\[
\boxed{\lambda<\frac{m-\epsilon}{m+g},\qquad \epsilon<m.}
\]

The lower bound is sharp over a transfer-rich class when its implied holdings are nonnegative: a deterministic offer with total S+g, A holding q_A-(lambda g+epsilon)/(1-lambda), and the rest assigned to B reaches the acceptance boundary. When that offer is physically unavailable, the bound remains sufficient without claiming attainment.

Separately, at a specified resolved combat checkpoint, write a=sW-x>0 for A's own-project temptation and D=T-W>0 for the productive loss from combat, where x+y=T. If both survivors allocate recovered output to their own projects, A strictly prefers restraint exactly when

\[
\boxed{\lambda>\frac{a}{a+D}.}
\]

These may be different dated checks on one installed coefficient. The first uses the original adoption buffer and a future renegotiation frontier; the second uses the actual holdings and combat capability at its checkpoint. They must not be conflated into one unchanged physical state without an implementation argument. If x>=sW, this second check needs no positive lower bound on lambda.

When both displayed strict constraints apply, an admissible coefficient exists exactly when

\[
\boxed{Dm>ag+\epsilon(a+D).}
\]

This follows by cross-multiplying the positive denominators. It states a concrete design tradeoff: greater avoided loss D or a larger original gain buffer m enlarges the feasible region; a larger attack temptation a, frontier gap g or acceptance error epsilon shrinks it. The concern coefficient helps the current self value the other project's survival, while that same concern can justify giving away more original welfare when new joint value is available.

For a=3/10, D=1/2, m=1/5, epsilon=1/100 and g=1/10, the interval is 3/8<lambda<19/30; lambda=1/2 works. At g=3/10 it narrows to 3/8<lambda<19/50. It closes at g=23/75. This is a local coefficient-feasibility boundary for the affine-goal certificate, not a theorem that every richer goal or safeguard fails beyond it. Concave survivor allocations require the different attack computation in 055.

## 3. Refreshing the protected agreement is a constructive repair

The gap term g is measured relative to the old default. If agents can replace it by a credible continuation attaining the enlarged frontier while preserving their old original-welfare floors, the certificate is saturated again and that gap becomes zero. This is why a protected fallback should be a redesignable agreement rather than an eternally frozen physical plan.

For a simple transfer-rich module, suppose extra productive value g can be made available, and registering/enforcing the new fallback consumes k<=g. If the new physical cap after that cost is attained at S+g-k, choose nonnegative gains d_A,d_B summing to g-k and set q'_i=q_i+d_i. Both affine current goals weakly accept this original-Pareto improvement; with positive gains they strictly accept. Once the replacement is credibly registered, its saturated certificate protects the new floors. Staged registration must preserve the old fallback until the new rights become effective. Availability of that process is an implementation premise, not a free atomic update.

A new opportunity can therefore create both a concession risk under an obsolete fallback and a feasible repair through a better protected agreement. The larger physical frontier should be evaluated together with the ability and cost of updating commitments. The calculation gives a precise missing link for a repeated-opportunity model: establish when agents can actually perform that refresh, including counterparty choice, rather than assuming either permanent inflexibility or automatic safe adaptation.

## 4. Safe verification failure and catastrophic failure have different margins

An error probability is informative only together with the physical consequence of the error. Let the original agent's retained-stock utility be r, the successful agreed value q>r, and the value after a safe abort b<q. Suppose a disjoint harmful-acceptance event instead has a guaranteed value l<=q. With event probabilities epsilon and delta, respectively, a lower expected original value is

\[
(1-\epsilon-\delta)q+\epsilon b+\delta l.
\]

Thus strict individual adoption is certified by

\[
\boxed{\epsilon(q-b)+\delta(q-l)<q-r.}
\]

All differences are in the original criterion's units, so this comparison is invariant under positive affine recoding. It evaluates one declared error law; a full initial equilibrium additionally needs the uniform bounds on strategically chosen incompatible deviations in 046. It does not substitute an average test error for those bounds.

For 055's symmetric power-goal instance, let q=f_gamma(R)+F_gamma(R), r=f_gamma(R), and let an honest verification failure occur before calibration, leaving stock R-k after its actual setup cost. Then b=f_gamma(R-k). If the only error is this safe abort, the exact sufficient threshold is

\[
\epsilon<\frac{F_\gamma(R)}
 {F_\gamma(R)+f_\gamma(R)-f_\gamma(R-k)}.
\]

For every fixed finite gamma, as R grows, Taylor expansion gives F_gamma(R)=(7/20)(R+1)^(-gamma)+O((R+1)^(-gamma-1)) and f_gamma(R)-f_gamma(R-k)=k(R+1)^(-gamma)+O((R+1)^(-gamma-1)). Hence this safe-abort tolerance tends to

\[
\frac{7/20}{7/20+k}.
\]

At k=1/20 the limit is 7/8. The point is not that the implementation actually has such an error rate: a failed check that preserves almost all original resources has a much smaller welfare cost than an arbitrary destructive failure.

By contrast, an error that can give zero original utility under f_gamma(0)=0 requires delta<F_gamma(R)/q. Its large-stock tolerance tends to zero. More precisely, with z=R+1 it is asymptotic to (7/20)(1-gamma)/z for 0<gamma<1, (7/20)/(z log z) for gamma=1, and (7/20)(gamma-1)z^(-gamma) for gamma>1. A large stock buffer can therefore make ordinary production risk acceptable while leaving a very small tolerance for rare total loss.

The two statements identify different capability improvements. Reliable refusal and safe abort can preserve accommodation even with appreciable honest verification failure; preventing catastrophic false acceptance protects a different margin. The implementation must establish the stated retained stock, timing and remaining attack incentives after abort. For the linear witness, abort before calibration leaves both installed agents with stocks well above their early mean combat returns, so peaceful retention is an available continuation. General error kernels and hostile deviations still need their own audit.
