# How often can someone win the slot by reporting one level lower?

**E8, note 147.** The two-level contract in [145](145-trading-and-insuring-a-private-slot.md) has an exact extension across finite demand classes. The decisive facts are the mass of jobs below each class, the return to moving up one class and the agents' risk sensitivity. Three or more classes can support truthful full insurance.

## A boundary for every finite ladder

Suppose n≥2 founders have equal initial liquid wealth w, identical original CARA utility, independent private values with the same ordered finite support x_1<...<x_d and positive masses p_k. Conditional on reports, an external escrow serves a highest reporter, breaks ties uniformly after reports and redistributes the winning reported value to give each an equal share s=1/n on truthful histories, as in 145. All shares and the selection coin are known in distribution. No side information reveals the coin or private values. Setup and service time leave a usable slot, and enough stock is deposited to cover the largest obligation. The party who controls an expired job cannot improve it by physically capturing the slot after expiry.

Let F_k=Σ_{j≤k}p_j, F_0=0, z_k=F_{k-1}/F_k and Δ_k=x_{k+1}-x_k. Define

    Ω_k = (1 + z_k + ... + z_k^(n-1))/n,
    Q_k = (1-exp(-γ Δ_k/n))/(1-exp(-γ Δ_k)).

**Exact condition for this contract.** Truth is a Bayesian equilibrium if and only if Ω_k ≤ Q_k for every k<d. If the inequalities are strict, every feasible downward lie strictly loses in interim expectation, and so does every upward lie. This result allows taxes on the winner funded entirely from deposited balances. It concerns this fully insured assignment, not the best trade or insurance scheme over all possible contracts.

To see the local condition, consider type x_(k+1) reporting x_k. The report matters only when all other jobs are at most x_k, an event of probability F_k^(n-1). Conditional on that event, the chance it receives the slot is Ω_k. Indeed, by symmetry the unconditional chance of service for a reporter with value x_k is

    (F_k^n - F_(k-1)^n)/(n p_k)

because the numerator is the probability that the maximum is exactly x_k. Divide by F_k^(n-1) and factor the difference of powers. When the understatement matters, the reported site earns x_k/n+Δ_k if served and x_k/n otherwise. Truth yields x_(k+1)/n. The original prefers that sure share exactly when Ω_k≤Q_k. An upward lie can only cost the overreporter money: if it wins, it is charged for unearned value, and when a still higher report wins its payment is unchanged. More explicitly, with an exaggerated report r exceeding its actual value x and all rival reports below r, winning gives x-(1-s)r<s x≤s max(x,Z), where Z is the maximum rival value. A tie with a rival at r gives s r on a loss and strictly less on a win. The event of all rival values minimal yields strict interim loss.

Why do the adjacent tests suffice? With report r and true value x, the original's expected utility, up to the positive scale exp(-γw), is an affine function of v(x)=1-exp(-γx) with slope

    exp(γ(1-s)r) P(serve i | report r).

The slope strictly increases with the report. The probability of service is positive and weakly increasing, and exp(γ(1-s)r) strictly increases. If a type x_(k+1) prefers its own report to x_k, all higher types also prefer x_(k+1) to x_k. Sum these comparisons along the chain. All upward deviations were already excluded. A violated inequality makes that particular adjacent understatement profitable. The proof does not require the selected applicant to have public access to anyone's private value.

## Reading the condition

For n=2 the condition reduces to z_k≤tanh(γΔ_k/4). More generally, set a=exp(-γΔ_k/n). The product of the two finite sums (1+...+z_k^(n-1))(1+...+a^(n-1)) must be at most n. Greater separation between adjacent outputs or stronger risk aversion makes honest sharing easier. A larger pool of strictly lower jobs relative to the mass at the claim level increases the appeal of understatement. The first level always passes for γ>0. As a ladder becomes fine over a region of positive cumulative demand and bounded positive density, z_k approaches one and Δ_k approaches zero, so that region violates the condition. This is the finite counterpart of the continuous deviation in 145.

For a three-tier, three-site example take γ=1 and adjacent physical gaps 3 log(2), giving Q_k=4/7. For masses (1/8,5/8,1/4), z_2=1/6 and Ω_2=43/108<4/7. The ordinary club fully insures everyone. For (1/2,1/8,3/8), z_2=4/5 and Ω_2=61/75>4/7. In the latter case high jobs often outbid everyone even as middle jobs, so truth loses. Both outcomes persist under small perturbations. An observer could estimate z_k from actual demand counts and measure the production differences rather than assuming that every three-tier organization faces the second outcome.

**Why this situation might arise or be built.** Real production may come in discrete batch sizes with genuinely different yields. Check actual output and private use values, since merely binning continuous reports does not change what a winner actually obtains. Founders can erect an ordinary clearing account and choose an unpredictable tie draw when the gain over their existing booking rights covers deposits, enforcement and transaction costs. A concealed lottery is feasible if the relevant parties cannot learn the draw early. A participant that already knows it will win the tie has a different incentive. Constructing discrete output classes from continuous jobs would involve changing the physical production menu and foregoing some productive value. The formula alone does not establish that anyone would choose that intervention.

**Exploration ledger.** Framing: the nature of private job values shapes the gains from changed goals. Structural: truthful complete insurance turns on the probability of winning after understating. The finite iid CARA instance is promising and has an exact criterion. “Adding a third level always destroys ordinary full insurance” is dead at instance level by the first three-tier example. A sibling measures the mass at the intermediate category. A structural successor asks whether a less than fully insured contract can recover most of the mutual gain, and how to price that loss against actual changes, a funded local controller or verification. An adjacent-claim test with correlated types is live, with the conditional distribution changing when an agent considers mimicking a different type.
