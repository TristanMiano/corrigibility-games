# Partial concern can finance sharing and make a coarse message credible

**E8, note 148.** A winner with partial concern willingly pays its partners but retains a premium for itself. That premium gives each site a reason to overstate its need. A group can accommodate this bias by choosing how much detail to request. This connects preference choice, credible reporting, actual service and original insurance in the same finite opportunity.

## The informed winner's payment

Let n identical CARA sites each value its own final output with weight 1 and its partners' original utilities with a negotiated weight β, 0<β≤1. The original has β=0. Stocks and additive yields are as in 145. The winner with true yield x can unilaterally transfer safe wealth after service, before the opportunity closes. Only its own private information is required. Set a=-log(β)/γ. When x>a and the safe stock suffices, its unique current optimum gives itself and each other site these respective gains:

    y_self = [x+(n-1)a]/n,      y_other = (x-a)/n.                (1)

The recipient's marginal utility of keeping wealth equals β times each partner's marginal utility at (1). Strict concavity gives uniqueness and symmetry among recipients. If x≤a the winner keeps the whole increment; the nonnegative voluntary transfer constraint binds. After (1) no recipient wants to give back wealth or transfer to a peer, since its own holdings are among the smallest and it weights itself most. On this terminal service a positively costly further edit cannot improve the winner's own optimal settlement. Different future activities or the ability to extract a partner's existing stock need separate analysis.

For x>a the chooser's disutility if it wins, apart from a common positive wealth factor, is W(x)=n β^((n-1)/n) exp(-γx/n). If another site wins at x it is K W(x), where

    K = [1+(n-2)β+β²]/(nβ) = 1+(1-β)²/(nβ).                     (2)

Thus i prefers its own job x over a partner's y iff y-x < (n/γ)log K. Near full concern the temptation to favor oneself in routing is second order in 1-β even though the winner's payment premium is first order. For any symmetric routing that serves a job X>a, each original's expected exponential loss, apart from its common wealth and setup factor, is

    H(β) E exp(-γX/n),         H(β) = (β+n-1)/(n β^(1/n)).       (3)

This follows by averaging its payoff as winner or nonwinner conditional on the selected job value, using permutation symmetry. H(1)=1 and H increases as β falls below one. Funded sharing of earned returns and assignment to the right job both affect the founders' price ceiling for the negotiated change. A direct price cannot simply be added to (3) without re-solving settlement with the resulting balances.

## A binary check with three sites

In 143's holder-controlled game suppose both possible yields L,H exceed a and members can make payment (1). Let r be the chance of the other remote job being high conditional on both the focal reporter and holder being low. A late fair tie between two high requests sustains truthful partial reporting when

    (1-r)(K-1)+(r/2)(K exp[-γ(H-L)/3]-1) ≤ 0.                   (4)

With full support and β<1 it implies that a low holder strictly prefers an honestly high job to its own. A high holder strictly keeps the slot. For a low requester, falsely claiming high either replaces a low holder, gaining W(L)(K-1), or displaces a high rival with probability 1/2, gaining W(L)(K exp[-γ(H-L)/3]-1). The high reporter strictly benefits from truthful eligibility when it can replace a lower-valued job. These are tests under the postchange preferences. Founders still use (3) to compare paid implementation with available ordinary trade, other membership and genuine alternatives.

## Two sites with a continuous spectrum of actual jobs

The following construction tackles the analogous two-site bluff in 143 by changing both settlement and messages. The club has a binding slot selector that sees only a short message from each site and can assign service. Each winner controls its own subsequent voluntary payments. Queue reservation and a private wallet can have precisely that division of authority. The same selector is available to ordinary agents. Public settlement based on enforceable prices and funded local delegates, if available, are distinct competitors.

Take n=2 and all x>a. Let b=exp(-γx/2), so *smaller* b means a more valuable job. Suppose iid b is uniform on [A,B], 0<A<B<1. This corresponds to a bounded decreasing density of physical yields. A bounded, smooth distribution is plausible for service with diminishing incidence at higher values. The exact uniformity in transformed units provides an analytically checkable instance. Agents can choose categorical messages; they need not be capable of altering the distribution. The selector serves the smaller reported category, with a late fair tie. Settlement depends on true earned output.

Let A=b_0<b_1<...<b_d=B be d common reporting categories. If a type b moves its message from category j+1 to j, it gains a half chance of being served when the rival belongs to either of these two categories. Outside their union its allocation is unaffected. The gain at a given rival type t has the sign of Kt-b. Consequently the indifferent boundary and the complete adjacent-report indifference equations are

    b_j = K (b_(j-1)+b_(j+1))/2,        1≤j<d.                    (5)

At smaller b this upward priority claim is attractive, at larger b it loses. If the cutoffs are increasing, summing adjacent comparisons shows truth in categories is a Bayesian equilibrium. Each interior type strictly prefers its assigned category to all alternatives. The cutoff types are indifferent and have zero probability. Conditional on a common category, serving either site by lottery loses some productive value but avoids the gain from pretending to be an arbitrarily close, slightly more urgent type.

For β<1 let θ=arccos(1/K). A strictly ordered d-category equilibrium of this form exists exactly when

    (d-1/2)θ < arccos[(A/B)cos(θ/2)].                             (6)

Indeed any solution of (5) is a sine wave with discrete phase increment θ. Write b_j=R sin(φ+jθ) with 0<φ<π. Strictly positive increments force φ+(d-1/2)θ<π/2: the first positive increment places its midpoint on this ascending branch, and a step θ<π/2 cannot skip an entire interval of negative cosine. In particular sin(dθ)>0. The endpoint solution is

    b_j = [A sin((d-j)θ)+B sin(jθ)]/sin(dθ).

For d satisfying (6) it is positive at intermediate indices and strictly concave as a sequence by (5). Its final increment is positive precisely when B cos((d-1/2)θ)>A cos(θ/2), by the difference of sines. This suffices for all increments and proves necessity and sufficiency on the ascending branch. d=1 always succeeds. When β=1 take equally spaced cuts for any d; full common concern also supports truthful continuous reporting.

For [A,B]=[1/4,1/2], γ=1, all yields exceed a both at β=1/2 and at β=4/5. At β=1/2 the largest d is 2. At β=4/5 it is 5. The density of private needs remains continuous in both. A site that originally kept its entire gain can now choose to pay the others and reveal which of several productive situations it faces. As β approaches one, θ is asymptotic to 1-β for n=2 and the number of sustainable categories grows on the order of 1/(1-β). For each fixed strictly feasible d, small smooth density perturbations preserve a nearby cutoff solution: the finite indifference equations are differentiable in cutoffs, and at the uniform law the tridiagonal linear system in (5) is nonsingular since sin(dθ)≠0. The strict inequalities between consecutive boundaries persist.

## Valuation by the founders

Within a common category of width h_j=b_j-b_(j-1), a random recipient has expected b exceeding the better job's expected b by h_j/6. The event has probability h_j²/(B-A)². Different categories select the better job. Thus, with `min` denoting the smaller of both b values,

    E b_selected = E min(b_1*,b_2*) + Σ_j h_j³/[6(B-A)²],         (7)
    E min = A+(B-A)/3.

The stars denote the two private draws, distinct from the cutoffs. Formula (3) times (7) is the original's actual exponential-loss factor before setup. If an outside option gives an original loss factor L_out, a common setup expense k is acceptable iff exp(γk)H(β)E b_selected < L_out. For example, sole use under a fair booking gives L_out=(1+E b²)/2, since exp(-γx)=b². Any priced ordinary exchange or funded binding local delegate must enter with its own factor. At matched outcomes and prices the voluntary change is an available adoption equilibrium alongside the ordinary mechanism. Equations (6)–(7) provide an incentive to fund a richer reporting interface only when the gain under original goals covers its added cost.

**Exploration ledger.** Framing: changing what the future informed winner cares about can make real cooperation possible. Structural: voluntary settlement changes how costly a reporting error is to its maker. The categorical partial-concern instance is promising. Literal assumption of continuously truthful ranking with β<1 and these payments is dead at that instance: imitating a slightly higher type gives a first-order chance of receiving the winner premium while only displacing a nearly identical job. A sibling uses the coarse, endogenous boundaries above. A structural successor combines changes to goals and to the precision or evidence of admissible claims. Natural realizations require private demand, transferable funds and the ability to make credible partial changes at an acceptable price. A known winner, confiscable deposits, extra supply acquired by force, or a cheap equivalent local controller changes the founder's calculation.
