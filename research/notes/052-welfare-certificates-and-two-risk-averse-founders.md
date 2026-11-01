# R0002 extension: original-utility welfare certificates

**Derived welfare and adoption boundary, with the execution repair in [056](056-contribution-rewards-through-renegotiation.md).** Insurance in 048 uses a linear risk bearer. The protection argument extends to two strictly concave original utilities when the productive fallback maximizes a positive weighted sum of those original utilities. The reward 1 below suffices for the fixed-contract subgame; E3 uses a larger finite reward to cover post-miss renegotiation. This locates a substantive risk/capital boundary instead of assuming that greater expected material output always makes accommodation attractive.

## 1. Replace the material frontier by an original-utility frontier

Let original utilities be w_i on physical histories and choose positive weights alpha_i. Define W=sum_i alpha_i w_i. Suppose a credible productive continuation Q maximizes E W over the actual physical continuation set, and fulfills each participant's contribution predicate e_i=1. A compatible successor can use

\[
G_i=(1-\lambda_i)\alpha_i w_i+\lambda_i W+\beta_i e_i-K_iI_i,
\quad 0\le\lambda_i<1,\quad\beta_i\ge0.
\]

On histories with no unsafe approval, current participation against Q implies

\[
(1-\lambda_i)\alpha_i(Ew_i-E_Qw_i)
\ge\lambda_i(E_QW-EW)+\beta_i(1-Ee_i)\ge0.
\]

Thus every accepted continuation preserves E w_i>=E_Q w_i. If all other participants retain their bounds, the positive weighted total cap prevents any compatible deviator from improving its original expected utility. If an incompatible deviation gives original utility at most d_i<E_Qw_i, and the guarded physical/initial-choice module of 046 is available, choosing the compatible arrangement is a best response and strictly improves on remaining incompatible.

This is a sufficient class theorem. Existence of a credible welfare-maximizing continuation, its physical protection, affordable implementation and a bound on incompatible deviations remain substantive premises. The weights are fixed for this certificate, not a theorem that every Pareto boundary point admits strictly positive supporting weights. The maximum is over the same dated opportunity set; new opportunities require a new bound or the process-only certificate in 048.

Finite process rewards can supply effort incentives in a bounded model. For example, a reward exceeding the greatest possible original-base loss from performing the specified contribution makes that action strictly preferable while the task remains feasible. The guard must still exclude unsafe approval without penalizing the ordinary Work/Shirk action itself. A matched binding effort/guard delegate can reproduce the mechanism.

## 2. Symmetric logarithmic founders

Use two original utilities w_A=log(1+X), w_B=log(1+Y). Each initial stock is R. Keep the two-input technology a=1/10, b=2/5, Y_0=10, contribution c=8/5 and installation loss k=1/20 per agent. Divide successful output equally. Under mutual contribution each final holding is

\[
R-33/20\quad\text{with probability }3/5,
\qquad R+67/20\quad\text{with probability }2/5.
\]

Put z=R+1 and define the original adoption gain

\[
F(z)=\tfrac35\log(z-33/20)+\tfrac25\log(z+67/20)-\log z.
\]

The relevant domain is R>=33/20, so holdings are nonnegative. There is one adoption threshold z_* on this domain, with

\[
7.7391<z_*<7.7392,
\qquad F(z)>0\ \Longleftrightarrow\ z>z_*.
\]

Equivalently, both founders strictly prefer the productive outcome to retaining their stock for R>R_*=z_*-1, where 6.7391<R_*<6.7392.

**Proof of the unique threshold.** Differentiation gives

\[
F'(z)=\frac{2211-140z}{z(20z-33)(20z+67)}.
\]

Hence F increases up to z=2211/140 and then decreases to zero from above; the positive approach follows also from F(z)=(7/20)/z+O(z^{-2}). It is negative at z=7 and positive at z=8. Strict monotonicity before the maximum gives exactly one root. The sign can be checked without logarithmic approximation: F(z) has the sign of

\[
(z-33/20)^3(z+67/20)^2-z^5.
\]

Exact rational substitution at z=7.7391 and 7.7392 brackets the root. Numerical digits are an enclosure, not an asserted exact formula.

## 3. Why the fallback maximizes the relevant welfare

Take W=log(1+X)+log(1+Y). For each realized total output, strict concavity makes equal allocation maximize W. Full contribution with the equal split attains that statewise allocation. Its expected welfare exceeds 2log(1+R) whenever R>R_*.

No contribution leaves total 2(R-k), whose maximum welfare is 2log(1+R-k), below that full-contribution welfare. A solitary contribution has expected total 2(R-k)+aY_0-c<2(R-k). Jensen bounds its maximum possible expected welfare by a value strictly below the no-contribution welfare, even granting arbitrary ex-post redistribution. Waste, additional lotteries and mixtures of effort profiles cannot improve these bounds. Therefore full contribution and the equal statewise split uniquely maximize expected W within the productive physical opportunity set.

Combat has at most four recoverable output units under the work kernel in 049, so even its optimally split W is at most 2log(3). This is below the productive welfare in the stated stock region. Arbitrary earlier resource loss or a solitary gamble followed by late attack cannot improve the bound: the gamble's first informative signal comes after the reactor work is spent, and every remaining own holding in this fixture exceeds the resulting recovery frontier. Thus the relevant physical cap includes those alternatives, rather than considering output transfers alone.

Choose lambda_i=1/5, beta_i=1. The installed base becomes log(1+X_i)+(1/5)log(1+X_j)+e_i. Its worst calibration cost in original log units is bounded by

\[
\log\frac{R+1-k}{R+1-k-c}<1
\]

throughout R>R_*. The success-probability improvement gives a nonnegative additional term for both projects. Both effort choices are therefore strictly dominant after compatibility. A finite K_i larger than the maximum bounded base criterion makes unsafe approval strictly unattractive as in 046. At R=10, total material is at most 30, so K_i=6 suffices: the base is below (6/5)log31+1<6.

Every failure holding R-33/20 exceeds 4 in the adoption region. It therefore exceeds the entire combat recovery frontier, at every strength split, before applying the still stronger post-production work bound. Both compatible continuation and each agent's retained stock dominate unilateral combat. The initial incompatible own-output bound E X_i<=R also gives E log(1+X_i)<=log(1+R) by Jensen. The original-goal adoption comparison is thus strict for every strength split under this resource-limited combat kernel.

The same finite-template, latency and actual-state attestation qualifications apply as in 049. Installation, input delivery and output shipping fit that schedule. The larger private stocks need not be shipped: the default moves only the ten possible output units, so increasing R does not silently require a larger routing budget. Existing storage is an initial resource, not free additional productive work.

For a nontrivial compatible family at R=10, lambda_i can vary over [1/10,3/10] and beta_i over [4/5,6/5], with K_i=6. The worst calibration log loss is below 8/[5(R+1-k-c)]<4/5 throughout the adoption region. At R=10 the largest base is below (13/10)log31+6/5<6. This permits genuine later goal variations while retaining the stated certificate. The floors and welfare maxima are conditional on the current information as explained in 043; they become the realized equal holdings after the output signal.

## 4. A risk boundary with a constructive counterpart

At R=10, both original logarithmic utilities strictly gain from the guarded productive arrangement. At R=3, even removing the installation cost leaves

\[
\tfrac35\log(12/5)+\tfrac25\log(37/5)<\log4.
\]

The exact equivalent inequality is (12/5)^3(37/5)^2<4^5. Full effort's maximum expected sum of original utilities is then below stock retention. Solitary effort is also worse by the Jensen argument, and reallocating the initial equal stocks cannot improve the sum. Hence no arrangement using only this one-shot reactor and transfer technology can strictly improve both original logarithmic utilities over retaining their stocks at R=3, even with free goal installation. Retention supplies a peaceful alternative; this boundary predicts rejection of that risky productive bargain, not combat.

The paired result is specific and informative: sufficiently large stocks make this same stochastic technology attractive to both diminishing-returns founders, while the small-stock case favors retaining their stock. Different success probabilities, insurance from a third party, repeated independent production, or a safer technology can change the risk boundary. Those are meaningful potential repairs, not evidence that the stated small-stock inequality is wrong or that the large-stock construction is uninformative.

## 5. Ordinary controls at the same dated welfare frontier

At the full-effort equal allocation, an unchanged-goal agent strictly prefers to shirk. Write x=R+1-k-c>0. Its work utility is (3/5)log x+(2/5)log(x+5); shirk utility is (9/10)log(x+8/5)+(1/10)log(x+33/5). The sign of ten times their difference is the sign of

\[
x^6(x+5)^4-(x+8/5)^9(x+33/5).
\]

Expanding in x gives only negative coefficients (the leading x^10 cancels); the leading remaining terms are -x^9-(186/5)x^8-(11308/25)x^7. Thus the difference is strictly negative for x>0. The exact coefficient check is reproducible in the supporting script/tests; it is an algebraic proof once the displayed expansion is verified.

In the compact mediated output-transfer class of 042, attaining the full welfare maximum would force full effort and equal allocation in every success/failure state. The profitable private shirk then contradicts obedience. Compactness therefore gives a strict gap below that welfare maximum for ordinary hidden-effort mechanisms at the same dated physical frontier. This is a total original-utility comparison, not a claim about every bargaining split. Costs cheaper for ordinary implementation must be credited before comparing original adoption payoffs.

A binding effort delegate or the appropriate observed-effort contract changes the implementation technology and can repair that incentive gap. Matched delegation remains compatible with voluntary genuine preference change as an optimal implementation. The construction's new breadth is two strictly concave original goals and an explicit capital/risk threshold; it does not establish natural population frequencies or unique selection of goal modification.
