# Nonlinear original values and flexible promise design

**R0005 theory extension.** The original own-output criterion is a useful
class, not a definition of every agent. This note states which contractual
arguments survive nonlinear values, identifies the relevant coefficient
normalization, and constructs a stronger local promise goal when a finite
linear penalty is insufficient. All installation choices still use the
incumbent's current criterion and actual implementation costs.

## 1. Certainty equivalents change the productive-agreement boundary

Let original i value its terminal own holding w by a strictly increasing
continuous u_i(w). Against an original duel awarding Y with probability
p_i and zero otherwise, define its certainty-equivalent holding

    d_i=u_i^(-1)[p_i u_i(Y)+(1-p_i)u_i(0)].            (1)

A deterministic agreement is individually rational exactly when x_i>=d_i.
Thus 102's productive opportunity calculation continues to apply after
replacing the linear d_i=p_iY by (1) and replacing its D by

    D_u=h-[R-(d_i+d_j)].                             (2)

For a<d_j<a+b, the supplier's best deterministic holdings above its
reservation are still

    M_u=(1-c/b)(d_j-a)-D_u-K.                        (3)

This follows from the physical payment/effort constraints and monotonicity
of u_i. It is a comparison in holding units, not the utility difference
u_i(x_i)-u_i(d_i). Physical setup expense K is subtracted from resources
before applying u_i, not silently treated as K units of nonlinear utility.

If u_i is concave, d_i<=p_iY; if convex, d_i>=p_iY, by the defining
chord inequality. For u(w)=w^rho, rho>0, d_i=Y p_i^(1/rho).
Concavity therefore expands the deterministic agreement region relative
to the same physical linear instance, while convexity contracts it.
The separate division between ordinary peace and genuine change still
depends on payment capacity, service value and implementation prices.

For example, using square-root originals in 100's physical fixture gives
d_i=27/8 and d_j=3/8. Ordinary payment up to the customer's funded limit
can then leave the supplier 49/10 and customer 1, improving both over
their duel certainty equivalents without requiring service or a new goal.
This is a successful ordinary alternative created by different original
values. With sufficiently valuable goal-enabled opportunities beyond the
best such alternative, (3) and the renewal comparisons can still support
genuine adoption. Neither increased peace nor increased goal-change
frequency is substituted for the other outcome measure.

For a specified deterministic peaceful holding z between loss l and win w,
original utility prefers peace to that duel exactly when

    p <= [u(z)-u(l)]/[u(w)-u(l)].                    (4)

This is only a comparison against that offer. An implementable peaceful
lottery with at least the combat holding in every corresponding state
dominates combat for every increasing u. Its funding and authority matter:
in the preloaded-consumable specialization, a peaceful loser must retain
a_j, so allocating Y to the winner can require R-h>=Y+a_j, stronger
than the risk-neutral expected-division inequality R-h>=Y. A lottery is
an available repair only when those state-contingent allocations and its
execution are actually feasible.

## 2. Penalty weights have units

For a goal C_i=u_i-lambda(q_j-u_j)_+, changing representations to
u_i'=A_i u_i+B_i and u_j'=A_j u_j+B_j, A_i,A_j>0, requires

    q_j'=A_j q_j+B_j,        lambda'=(A_i/A_j)lambda.

The resulting C_i'=A_i C_i+B_i represents the same preference ordering.
Consequently a numerical statement such as lambda>1 presumes the declared
common linear physical-value scale. It is not invariant under unrelated
rescalings of two agents' utility representations. The dimensionless
tradeoff ratios in 102 are computed in that actual scale.

Suppose y_i+y_j<=S, with accepted deterministic point (S-z,z), and
u_i,u_j are differentiable and increasing on the relevant compact ranges.
A sufficient condition for the accepted point to maximize

    C_i=u_i(y_i)-lambda[u_j(z)-u_j(y_j)]_+

is u_i'<=M_i, u_j'>=m_j>0 and lambda>M_i/m_j. If the other falls
short by d, own improvement is at most M_i d and the utility deficit
is at least m_j d. A sharper threshold is the supremum of the actual
secant ratio

    [u_i(S-z+d)-u_i(S-z)]/[u_j(z)-u_j(z-d)].           (5)

A physical holding-floor goal u_i(y_i)-lambda(z-y_j)_+ instead needs
lambda>M_i. It avoids dividing by a near-zero other-agent marginal utility,
while making its physical reference explicit. Each is a substantive
preference design with different reference/observation requirements.

## 3. The relevant geometric condition is a bounded gain-to-harm ratio

Let F be an actual set of attainable terminal welfare vectors and q in F
an accepted Pareto-efficient point. Use original welfare coordinates W_i,
not newly installed utilities. Define

    d_i(W)=sum(j!=i)(q_j-W_j)_+,
    M_i(q)=sup{(W_i-q_i)/d_i(W): W in F, W_i>q_i}.    (6)

Pareto efficiency makes every denominator in this set positive. If
M_i(q)<infinity, then C_i=W_i-lambda_i d_i with lambda_i>M_i(q)
strictly rejects every outcome improving own welfare by harming an
accepted floor. Outcomes lowering own welfare also lose; outcomes with
the same own welfare and all others above their floors may tie. Pointwise
domination extends to arbitrary lotteries over these physical outcomes.
For 102's two-party service frontier the bounds are c/b and b/c.

If F is a bounded polytope, M_i(q) is finite. Partition F by the signs
of W_j-q_j. Each part is a polytope on which the numerator and denominator
are affine. At a vertex with zero denominator the numerator is nonpositive
by Pareto efficiency. At all other finitely many vertices choose M at
least the positive numerator/denominator ratio. The affine inequality
W_i-q_i<=M d_i holds at every vertex, hence throughout each part. This
proves the bound without importing a general equilibrium theorem.

Smoothness alone is insufficient for this *linear* design. On the compact
frontier W_i=q_i+sqrt(d), W_j=q_j-d for 0<=d<=epsilon, q is
Pareto efficient but (6) is unbounded as d approaches zero. For every
finite lambda, a small positive d has sqrt(d)-lambda d>0. The constructive
repair is a different penalty shape, a physically meaningful minimum
resolution, or an available funded compensation, rather than declaring
all negotiated goal changes impossible.

## 4. A stronger local goal can preserve growth above the promise

For a fixed accepted q, define a gain-forfeiture criterion

    C_i(W)=W_i-P_i(W),
    P_i(W)=0,                                      if d_i(W)=0,
           (W_i-q_i)_+ + gamma_i d_i(W),            if d_i(W)>0,
    gamma_i>0.                                      (7)

Every deficit outcome has C_i<q_i: if W_i>q_i the first penalty removes
the entire excess, and otherwise the positive deficit penalty reduces
an already no-greater own welfare. With all other floors honored, C_i=W_i.
Thus q beats every shortfall outcome, while a feasible Pareto improvement
above q remains desirable. This repairs the curved-frontier example
without assigning intrinsic value to frozen code or capping honest growth.
It is a genuine ordering change whenever a profitable harmful outcome
exists. It also has 094's original-welfare-floor form W_i-P_i, P_i>=0.

The price of this generality is substantive: (7) has a discontinuity at
zero deficit when own gain is positive. It needs exact reference/shortfall
semantics, or an explicitly modeled discrete resolution. It is a designed
promise preference, not evidence that such a preference is common. Under
noisy observation, mistaken shortfall judgments and actual verification
expense can make a smoother goal or an ordinary funded remedy preferable.

This is a result for a fixed feasible obligation set and reference q.
An agent cannot erase an old shortfall by renaming the contract or changing
its code; the old evaluator assesses the actual history. Allowing arbitrary
new obligations to inflate q_i, overlapping capacity, cross-cycle investment
or counterparty replacement requires an admission and settlement rule.
The local construction does not solve that history dependence. Independent
settled cycles or an explicit funded compensation rule supply useful
tractable extensions; unbounded simultaneous commitments remain open.

## 5. Uncertain production needs contingent promises

A deterministic floor in a stochastic workshop can penalize unavoidable
bad outcomes. If the productive state omega is legitimately observable and
the agreement uses q(omega), the preceding pointwise proof applies in each
state with its actual feasible set F(omega). Expected original gains can
then make installation attractive even though random outcomes are unknown
beforehand. This uses knowledge of the stochastic dynamics, not foresight
of their realizations. A merely expected promise generally differs:
E[(q-W)_+] is not (q-EW)_+. Insurance, reserves or state-contingent terms
are constructive repairs with costs; unverifiable state claims and missing
funding are genuine limits to check before asserting execution.
