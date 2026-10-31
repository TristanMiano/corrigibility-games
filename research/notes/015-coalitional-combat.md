# R0001 working note — coalitional combat and the peaceful allocation set

Two-agent participation does not settle coalition stability. This note studies one explicitly declared deviation technology: a coalition can coordinate an attack and enforce a division of its victory output among its members. This is stronger than merely allowing individuals to talk. It can represent a binding fixed-utility alliance or a correctly implemented common controller, with their respective formation costs included in the war output. Sequential alliance formation and stability after victory remain separate questions. These are local, self-checked results, not population claims.

## 1. Coalition threat values under linear original goals

There are n>=2 agents, strengths a_i>0, and original utilities x_i for their respective physical products. Peace can deliver any x>=0 with sum x_i<=P. For each nonempty proper coalition S, let q_S be its specified probability of winning against its complement and W_S>=0 its total deliverable output on victory, after the coalition's actual preparation and combat costs. A losing coalition receives none of its colors in this particular benchmark. Its members can enforce any nonnegative division of the victory output. Thus its total expected color payoff from this deviation is

$$v(S)=q_S W_S.$$

A proposed peaceful allocation p is immune to a deviation making every member of some coalition strictly better iff

$$p(S):=\sum_{i\in S}p_i\ge v(S)
\quad\text{for every nonempty proper }S.$$

Proof: if p(S)>=v(S), the coalition cannot give all members strictly more because the expected sums would contradict this inequality. If p(S)<v(S), q_S must be positive. Divide the positive excess among members as epsilon_i>0 and choose victory quantities (p_i+epsilon_i)/q_S summing W_S. Each member then strictly improves in expectation. This proof uses linear color utilities and an enforceable division; risk preferences, losing-world value, endogenous internal conflict and indivisible output change the threat set.

The inequalities characterize a **coalition-deviation constraint set** for the stated attack opportunities. They do not establish that the coalition forms, that the division is credible, or that a peaceful protocol selects p. Free simultaneous mutual-attack equilibria and earlier implementation attacks have not disappeared.

## 2. The additive-strength special case

If q_S=a(S)/A, where a(S)=sum_(i in S) a_i and A=sum_i a_i, and every W_S<=P, then the proportional allocation p_i=a_i P/A satisfies every coalition constraint:

$$p(S)=\frac{a(S)}A P\ge\frac{a(S)}A W_S=v(S).$$

If W_S<P for every proper coalition, each of these inequalities is strict. Destructive coalition combat is therefore compatible with a coalition-resistant proportional allocation under this specific linear contest law and enforceable-division threat technology. There is no coalition formation theorem here, nor a general result for nonlinear combat probabilities. A merger that changes effective combined strength or the victory production frontier changes the calculation.

This statement retains combat as an available deviation and proves an incentive inequality against it. It does not ban attacks or suppose infinite costs.

## 3. An exact three-agent feasibility boundary

For n=3, write a_i=v({i}) and b_ij=v({i,j}); these a_i are threat values in this section, not physical strengths. Define

$$P_* = \max\left\{
a_1+a_2+a_3,
b_{12}+a_3,
b_{13}+a_2,
b_{23}+a_1,
\frac{b_{12}+b_{13}+b_{23}}2
\right\}.$$

There exists a nonnegative full-output peaceful allocation satisfying all coalition constraints iff P>=P_*.

Necessity follows by summing the three singleton constraints; each pair constraint with the complementary singleton; and all three pair constraints, respectively. For sufficiency, rewrite the pair constraints at total P as p_i<=P-b_jk. The assumed inequalities ensure

$$a_i\le P-b_{jk},\quad
\sum_i a_i\le P\le\sum_i(P-b_{jk}).$$

Starting from the lower endpoints p_i=a_i, distribute the remaining P-sum a_i among the three nonnegative interval capacities. Their total capacity is at least that remainder. The resulting vector lies in every interval and sums to P, proving all singleton and pair constraints. This constructive proof avoids treating a general cooperative-game theorem as already audited.

The final half-sum term is the overlapping-coalition obstruction: every pair might be individually offerable its desired amount, yet all pair demands cannot simultaneously be met. Individual participation alone misses it.

## 4. A destructive-combat counterexample with nonlinear strength

Let three agents have equal unit physical strength and let a coalition's strength add. Use the contest law

$$q_S=\frac{a(S)^r}{a(S)^r+a(S^c)^r},\quad r>0.$$

At r=2, singleton victory probability is 1/5 and pair victory probability is 4/5. Take P=1 and common postwar output W=19/20, so combat reduces deliverable output by five percent. Singleton threat values are 19/100; pair threat values are 19/25. Their pair half-sum is 57/50>1. Therefore **no** peaceful allocation can deter every coordinated pair, even though each pair's own threat value is below the whole peaceful output and every individual can easily be given its singleton threat.

The proportional allocation gives each pair 2/3, less than its 19/25 war value. Every possible reallocation leaves at least one pair dissatisfied, by the half-sum bound. The example does not prove that war occurs in every dynamic equilibrium; coalition formation may fail, other peaceful instruments may alter the deviation set, or changing the goals may change which deviations are preferred.

The quadratic contest is deliberately not neutral to regrouping identities with added strength. Note 010's linear-weight grouping theorem identifies this difference. Nonlinear combat effectiveness or coordination synergy is an explicit model variation, not something inferred from the word strength. In the r=1 comparison, the proportional allocation is coalition-resistant for the same P and W.

The W<P relation can be supported by positive fight work and dispersion/recovery in the physical resource kernel. It does not require destruction of conserved material or an entropy-to-utility identity. A calibrated technology would still need to justify the numerical ratio.

## 5. Symmetric n-agent threshold

With equal strengths, common victory output W>0, and q_k=k^r/[k^r+(n-k)^r] for a coalition of size k, the coalition constraint set is invariant under every permutation of agents and is convex. If it contains any full-output allocation, average all its permutations. The average is (P/n,...,P/n) and remains feasible. Hence feasibility is equivalent to

$$\frac PW\ge R_n(r):=
\max_{1\le k<n}\frac{n k^{r-1}}{k^r+(n-k)^r}.$$

Conversely this inequality directly makes the symmetric allocation satisfy every coalition constraint. This is an exact finite-n criterion for the declared threat technology, including equality as weak deterrence.

At r=1, R_n(1)=1. At n=2, R_2(r)=1 for every r>0: the two-agent symmetric benchmark cannot reveal this nonlinear coalition obstruction. At n=3,r=2, R_3(2)=6/5, so peace requires W/P<=5/6. A five-percent output loss is insufficient; at least one-sixth is needed in this comparison.

For r>1 and a continuous coalition fraction x in (0,1), maximize

$$H_r(x)=\frac{x^{r-1}}{x^r+(1-x)^r}.$$

Its derivative has the sign of (1-x)^(r-1)(r-1+x)-x^r. Substituting t=x/(1-x) gives a unique positive maximizing root t>1 of

$$t^r=r t+r-1.$$

Indeed t^r-r t-(r-1) decreases until t=1 and then strictly increases from a negative value to infinity. At r=2, t=1+sqrt(2), x=1/sqrt(2), and max H_2=(1+sqrt(2))/2. Thus R_n(2) is bounded above by that value and converges to it as the discrete coalition fractions become dense. The large-n sufficient-and-limiting threshold is W/P<=2/(1+sqrt(2)), about 0.8284. The most demanding coalition need not be the smallest majority or the largest available coalition.

For 0<r<1, smaller coalitions instead have an advantage relative to proportional strength. The same discrete R_n formula remains valid; the continuous small-x expression diverges and cannot be substituted for a fixed finite population. These are comparative statics of a specified contest, not a law connecting intelligence, utility or reproductive fitness.

## 6. Implementation and scope

A coalition's threat may be overestimated if members cannot commit to the promised postwar division, if preparing the alliance changes the opponent's opportunities, or if a surviving merged controller cares about outsiders. In such cases replace the scalar v(S) by the actual attainable expected-payoff set and test whether it contains a vector strictly above p on all coalition members. The vector formulation is the general object; the scalar reduction uses transferable linear color quantities.

Ordinary fixed-utility agents with the same enforceable alliance or allocation technology must receive the same opportunity set. Conversely a physically verified shared goal can be one way to implement an alliance, but its voluntary installation and later stability require the current-self analysis from the earlier notes. None of the coalition inequalities establishes that corrigibility is prevalent in an evolving population.
