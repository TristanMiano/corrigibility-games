# R0001 working note: stochastic production and overlapping opportunity sets

The deterministic construction in note 014 uses different production budgets to induce different peace and war allocations. Perfect knowledge of a stochastic law does not reveal its realization, and the two routes can have overlapping budget supports. This note gives an exact finite-support boundary for a local output-only implementation problem. Proofs are AI self-checked. The optimization uses ordinary fractional-knapsack reasoning; no literature-priority claim is made.

## 1. A local stochastic execution problem

Condition on A being the designated production operator. Original utilities are x_A,x_B and A's combat victory probability is s in (0,1). The same strength coordinate determines the E2 operator draw before this conditioning. Let Y_P, Y_W, Y_B denote total output under peaceful execution, A's combat victory and B's victory. Their finite-support laws are known, with nonnegative values bounded by Y_max. They include the actual route costs and outcome-dependent physical damage. Write their means as mu_P,mu_W,mu_B.

The current comparison is made before these production realizations. An installed output-only goal U uniquely chooses its optimal allocation from each full output simplex. Thus at budget y it supplies B the same quantity m(y) in peace and after an A victory. B remains selfish and supplies only B output when it wins. A history flag, a route-dependent constraint, or a tied objective with a separately promised contingent policy is a different implementation class.

This is a **local execution module**, not a complete information protocol. Its last strategic checkpoint precedes the terminal production kernel. If a budget or signal is observed while either party can still attack, that later checkpoint needs conditional incentive checks; section 6 spells out the limitation. Atomic execution at this resolution, public recognition of the restricted goal, installation timing and the selected continuation require the same explicit justification as in notes 020 and 027. No action is removed from a capable agent at a modeled nonterminal checkpoint.

Let y_1,...,y_n be the distinct union of the supports, with probabilities p_j for Y_P and w_j for Y_W. Put m_j=m(y_j), so 0<=m_j<=y_j. Original A's pre-change combat value is s mu_W, and B's original combat value is d_B=(1-s)mu_B. With this matched initial/post-installation frontier comparison, the two relevant strict conditions are

$$\sum_jp_j m_j<c:=\mu_P-s\mu_W,$$
$$\sum_j(p_j-sw_j)m_j>d_B.$$

The first is original-A adoption: its peaceful output is mu_P minus B's share. The second is B's **post-modification** attack deterrence; an A victory now gives B E[m(Y_W)]. It also implies B's original participation because m>=0. Different pre-installation costs or threats require separate initial constraints.

## 2. Exact implementability is a finite knapsack frontier

If c<=0, strict original-A adoption is impossible. For c>0 define

$$F(c)=\max\left\{\sum_j(p_j-sw_j)m_j:
0\leq m_j\leq y_j,\ \sum_jp_jm_j\leq c\right\}.$$

There is an allocation schedule satisfying both strict inequalities exactly when

$$\boxed{F(c)>d_B.}$$

Necessity is immediate. For sufficiency, take a maximizing schedule. If its peaceful B share equals c, scale all m_j by a factor slightly below one. Its attack-deterrence expression stays above d_B while original A's inequality becomes strict. A positive objective cannot come from a zero peaceful share, since coefficients at p_j=0 are nonpositive. All allocations remain feasible.

The frontier has an explicit finite form. Set m_j=0 whenever p_j=0; that cannot reduce the objective. For p_j>0 write

$$v_j=p_jy_j,\qquad R_j=1-s\frac{w_j}{p_j},\qquad z_j=p_jm_j.$$

Then maximize sum R_j z_j subject to 0<=z_j<=v_j and sum z_j<=c. Discard nonpositive R_j and order the remaining ones decreasingly. If V_{j-1} is the sum of preceding capacities, then

$$F(c)=\sum_j R_j\min\{v_j,\max(0,c-V_{j-1})\}.$$

An exchange proof establishes optimality: if a smaller-rate coordinate is positive while a larger-rate one has unused capacity, moving a small amount of peaceful B share to the larger rate increases the objective without changing its total cost. Repeating leaves at most one partly filled rate level. Zero/negative rates do not improve a maximization with an upper, rather than equality, budget.

The ratio w_j/p_j measures how much a unit of promised B output also benefits B after losing a war. Giving B output at budgets that occur only in peace has rate one; giving it output at war-heavy budgets has a smaller or negative rate. This is a statement about the actual physical opportunity laws, not about reported utility numbers.

## 3. The schedule can be implemented by a smooth concave current goal

The preceding inequalities are not merely a policy relaxation. Any finite feasible schedule can be interpolated by a twice continuously differentiable A-output schedule a(y)=y-m(y) in [0,y], with a(0)=0, as in note 014, section 4. That note constructs

$$U(x)=C Y-KY^2-\varepsilon[x_A-a(Y)]^2,\qquad Y=x_A+x_B,$$

which is strictly increasing and strictly concave on the bounded physical domain when K and then C are sufficiently large. It uniquely implements the prescribed schedule at every support point. Increasing C further preserves those allocation choices and curvature.

We must also check the **installed** A's own combat incentive. Its optimal value at budget y is f(y)=Cy-Ky^2. After B wins, U(0,y)=f(y)-epsilon a(y)^2. Hence its expected peaceful advantage over combat is

$$C\Delta-K\Delta_2+(1-s)\varepsilon E[a(Y_B)^2],$$

where

$$\Delta=\mu_P-s\mu_W-(1-s)\mu_B,$$
$$\Delta_2=E[Y_P^2]-sE[Y_W^2]-(1-s)E[Y_B^2].$$

Every strictly feasible schedule has Delta>0: its peaceful B share is less than c but exceeds d_B plus a nonnegative war-sharing term. Choose C also greater than K max(Delta_2,0)/Delta. The displayed current-goal advantage is then strictly positive. This does not require first-order stochastic dominance of peace over each war distribution; the bounded-support moments suffice for this constructed goal.

Therefore, in the local execution class, F(c)>d_B is necessary and sufficient for a smooth strictly increasing strictly concave output-only objective that uniquely implements a schedule with strict original-A adoption, B attack deterrence and installed-A peace preference. The new criterion uses its own values; original A's adoption was checked separately in section 1. The construction does not imply cheap or transparent implementation of large coefficients.

The proof gives only ex ante attack comparisons at the declared checkpoint. It does not give a successor authority to bind other agents, replace public verification by self-knowledge, or eliminate a later information-dependent deviation.

## 4. Positive expected physical surplus can still be insufficient

Let peace always produce one. Conditional on either combat winner, total output is one with probability theta in (0,1) and zero otherwise. Combat victory and damage draws are distinct; all agents know their laws. Then mu_P=1 and mu_W=mu_B=theta, so ordinary expected-output bargaining has a positive surplus 1-theta.

An output-only unique optimizer must give B the same share b at budget one whether that budget follows peace or an A combat victory. It gives nothing at budget zero. The conditions reduce to

$$\frac{(1-s)\theta}{1-s\theta}<b<1-s\theta.$$

They are feasible exactly when

$$1-(1+s)\theta+s^2\theta^2>0,$$

or

$$\theta<\theta_*(s)=
\frac{2}{1+s+\sqrt{1+2s-3s^2}}.$$

For equal strength, theta_*=3-sqrt(5). At theta=9/10, the lower bound on b is 9/11 while the upper bound is 11/20, so no such output-only goal works despite a positive expected-output surplus. At theta=7/10, the interval is (7/13,13/20); b=3/5 works. A fixed strength-proportional split b=1-s instead requires the stronger condition theta<1/(1+s).

The algebra matches note 011's homothetic deterministic threshold, but the reason for the restriction differs. There, proportional production is imposed across different budgets. Here the same budget can arise on both routes, so **every uniquely optimizing output-only goal** must make the same choice at that budget. Nonhomothetic flexibility alone cannot distinguish two identical choice problems.

A physical realization can have spare work/time under both routes and one unit of feedstock. Combat has finite work/time costs and a strength-dependent winner. Its damage draw either preserves sufficient production infrastructure or leaves zero usable capacity before the deadline; the latter branch has explicit incapacity/termination. Repair capabilities and deadline are part of that physical kernel. Expected cost is not represented as a negative utility constant, and a known damage probability does not reveal which branch will occur.

An equally enforceable history-contingent delegate, or note 011's finite combat-history goal, can supply B a peaceful share b while supplying it zero after A wins even at the same total budget. Then any theta<1 admits the ordinary strict interval ((1-s)theta,1-s theta). This comparison changes the available contingency information/execution, not the amount of physical surplus. Goals with ties plus an additional contingent tie-selection rule must likewise have that policy and its credibility analyzed; the unique-optimizer impossibility does not cover them.

## 5. Separation of supports and continuity boundaries

If the finite positive peace and A-victory budget supports are disjoint, every peaceful unit has rate one and all A-victory B output can be zero. Then F(c)=min(c,mu_P); since c<=mu_P, the condition reduces to ordinary positive expected surplus Delta>0. Finite distinct budgets can be interpolated smoothly even when their numerical separation is small. That does not supply uniform accuracy or bounded implementation coefficients as the supports approach one another.

For infinite supports a zero-probability distinction is not enough. If a continuous unique-allocation schedule must give B zero at every budget in the A-victory support, it also gives zero on its closure. If that closure contains the peaceful support, this requirement leaves no peaceful B output. Approximate optimization, measure-zero exceptions and noisy budget observation need a separate quantitative analysis; the finite knapsack theorem does not assert a discontinuous physical classifier is available for free.

### A quantitative boundary for limited budget sensitivity

Suppose the actual B-output schedule is L-Lipschitz in total budget. For any coupling of Y_P and Y_W,

$$E[m(Y_P)]-E[m(Y_W)]\leq L E|Y_P-Y_W|.$$

Let D be the smallest E|Y_P-Y_W| over these finite-support couplings. This is a finite transport minimization, not a claim about utility or thermodynamic distance. Original-A participation requires b=E[m(Y_P)]<c, so B's deterrence margin is bounded above by

$$b-sE[m(Y_W)]<(1-s)c+sLD.$$

Thus (1-s)c+sLD>d_B is necessary for a strict bargain in this bounded-sensitivity class. The inequality follows directly from the Lipschitz bound for each paired realization, then expectation and minimization over couplings. No information about the random realization is assumed available in advance.

For deterministic P>W with the same W under both winners, put delta=P-W and assume L>=1. At a fixed peaceful B share b, the least possible war B share is max(0,b-L delta). Its available interval also contains this value: b<=P and L>=1 ensure it is at most W. Under the closed original-A bound b<=c=P-sW, the maximal B deterrence expression is therefore

$$\min\{c,(1-s)c+sL\delta\}.$$

It follows that a strict allocation-schedule solution exists exactly when

$$L>\frac{(1-s)(sW-\delta)}{s\delta}$$

in addition to P>W and L>=1. The first branch c>(1-s)W is just P>W. The strict second branch is the displayed condition. If it holds, choose b slightly below c and a feasible war share close to max(0,b-L delta). Linear interpolation through (0,0), (W,m(W)), and (P,b) is a feasible L-Lipschitz schedule. With strict slack it can be smoothed with an arbitrarily small increase in L and implemented by note 014. No exact smooth attainment at a saturated derivative bound is asserted.

For P=1,W=49/50,s=1/2, the lower threshold is L>47/2. Arbitrary expressive output-only goals can solve the deterministic problem, but a uniformly slowly changing allocation rule cannot. As the surplus tends to zero, the necessary sensitivity grows like 1/(P-W). This complements the regret bounds of notes 017/023; it is not a bound on physical energy, runtime or code length.

## 6. What changes when information arrives before the last attack

If a public signal sigma is observed at a nonterminal checkpoint, recompute conditional laws p_j^sigma,w_j^sigma and the B-winner mean, as well as the conditional strength s_sigma. A single installed output-only objective must use the **same** m_j wherever the budget y_j is the same. Its B-deterrence constraints are jointly

$$\sum_j(p_j^\sigma-s_\sigma w_j^\sigma)m_j
>(1-s_\sigma)\mu_B^\sigma$$

for every relevant signal. The unconditional inequality is their average only in suitably matched cases, and never implies each one. A finite set of these constraints gives a linear feasibility problem rather than the single-constraint knapsack ordering.

A sufficient current-A certificate for the same smooth schedule is Delta_sigma>0 at every such checkpoint. Choose C above the maximum of the corresponding K max(Delta_2,sigma,0)/Delta_sigma bounds, as well as note 014's monotonicity bound. Original-A adoption still uses its actual pre-change continuation value at the entry history, not the later U scores. The signal process, off-path continuations and installer incentives still require a full game specification.

If a signal announces that the peaceful apparatus cannot produce anything while combat can still capture usable output, the conditional B inequality is impossible. An attractive ex ante average cannot certify peace through that history. Conversely, a physically coupled model in which all later conditional inequalities hold can use note 027's staged checks. The location of chance and observation in the game tree is therefore substantive, even when the unconditional production laws and all expected physical totals agree.

An explicit nonzero-budget example illustrates both the moment construction and this timing boundary. Let peaceful budgets be 1/2 and 3/2 with equal probability, let A's winner budget be one and B's be 1/2, and take s=1/2. Prescribe B outputs 1/5, zero and 3/5 at budgets 1/2, one and 3/2 respectively. Original expected peaceful quantities are (3/5,2/5), exceeding original combat values (1/2,1/4), and B's post-modification threat is still 1/4.

To give a concrete smooth goal, set a(y)=y h(y), with h=3/5 up to y=1/2. On [1/2,1], use h=3/5+(2/5)S(2y-1); on [1,3/2], use h=1-(2/5)S(2y-2), where S(t)=6t^5-15t^4+10t^3. The pieces join twice continuously differentiably. Bounds |a'|<=13/4 and |a''|<=87/5 suffice for note 014's construction with epsilon=1,K=27,C=100 on Y_max=3/2. The resulting U has expected peaceful value 265/4 and combat value 1452/25, a strict difference 817/100, although peace does not first-order stochastically dominate the A-winner budget.

If the low peaceful budget is instead publicly revealed before a remaining attack checkpoint, its current-U value is only 173/4, below 1452/25, and its B output is 1/5<1/4. Both then prefer combat, assuming the same conditional combat technology remains available. This is a different observation-timing game with the same unconditional budget laws. A production uncertainty claim must specify which of these games it means.
