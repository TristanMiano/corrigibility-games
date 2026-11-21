# Paying for the slot can also insure its users

**E8, note 145.** A booked facility can use an ordinary price when the parties have a liquid stock they can exchange. When the holder and the customer are both risk sensitive, that price also shares the windfall from an urgent job. Paying the holder can improve each original's prospects even relative to a free arrangement for giving the slot to the highest-value job.

## A voluntary price on delivery

Keep the exchangeable private binary demand, original CARA utilities and finite expiry in [140](140-reciprocal-access-to-a-scarce-slot.md). Use physical outputs `L,H` with 0<L<H. Write v(x)=1-exp(-γx). Start with a three-member club. The holder can offer one spot delivery at a posted price p from an eligible buyer's safe stock. Seller and buyer expend d_s,d_b ≥ 0 on an executed trade. They know their own demand. An actuator exchanges payment and delivery jointly. A buyer can decline, and a seller can keep the slot. The price and tie lottery are fixed before requests. Every interested buyer can pay the price and delivery cost from its initial stock. A participant can willingly help create this interface for an ex ante gain. Costly metering, thin stocks or an inability to couple payment to delivery give concrete reasons for the interface to be expensive or missing.

If L < p-d_s < H and L < p+d_b < H, precisely a low holder offers and precisely high nonholders want to buy an offered slot. At least one such buyer suffices. A high holder prefers local service. The highest real output is produced in every profile. Against uncompensated efficient routing, each low-holder/high-buyer trade changes the *sum* of normalized original increments by

    G(p) = v(p-d_s) + v(H-p-d_b) - v(H).

The comparison uses the same initial wealth for everyone and the same efficient, symmetric routing distribution. The identity of a tied buyer may be randomized independently. With a uniform owner, iid demand and urgency probability π, trade takes place with probability T=(1-π)[1-(1-π)^2]. The ex ante increment of each founder changes by T G(p)/3. Positive correlation or asymmetry changes those weights. Let z be the symmetric uncompensated increment. A new fixed per-party connection cost k is worth paying relative to free routing iff

    k < log[(1-z)/(1-z-T G(p)/3)]/γ.

The optimum of G is p*=(H+d_s-d_b)/2 and both traders then receive the same net y=(H-d_s-d_b)/2. Strict concavity gives uniqueness. If y>L, the strict buyer and seller conditions hold (including p*+d_b < H because y>0). Direct substitution gives

    G(p*) > 0   iff   d_s+d_b < (2/γ) log cosh(γH/2).

For example, γ=1, L=log(4/3), H=log(4), d_s=d_b=0. Each trader gets log(2). Their two normalized gains sum to 1, compared with 3/4 for the sole recipient. This is a strict open comparison, not a population frequency. A common-goal club can use the same transfers when it has the same spendable balances. Accordingly this argument establishes the value of sharing the receipts. The difference between keeping or changing preferences depends on which receipt-sharing rule each can actually sustain.

## A stronger ordinary arrangement with two possible values

Permit a public external booking device to bind the booking and funded transfers using reports, while each participant alone observes its realized job value. Let n≥2, s_i>0, Σs_i=1. Given reports in {L,H}, serve a highest reporter, use a late lottery for ties, let the winner pay (1-s_i) times its report and give each other j the fraction s_j times the winning report. A deposit of (1-s_i)H covers i's largest bill. On truth each i's net private income is s_i M where M is the actual maximum. Equal shares give complete within-state insurance for identical concave founders. The aggregate maximum M itself can still vary between states.

**Truth test.** A low type reporting high loses (1-s_i)(H-L) when everyone else is low. With some other high report, its wealth is unchanged when it loses the tie and falls by H-L when it wins. A high type reporting low changes its wealth only when everybody else reports low. Let p_i be its chance of being served in the all-low tie, and Δ=H-L. Understatement then gives w+s_i L+Δ with probability p_i and w+s_i L otherwise. Truth gives w+s_i H. The exact conditional constraint for an increasing original utility u_i is

    p_i ≤ [u_i(w+s_i H)-u_i(w+s_i L)] /
          [u_i(w+s_i L+Δ)-u_i(w+s_i L)].

The right side exceeds s_i for strictly concave u_i. Choosing the tie lottery p_i=s_i therefore sustains truth conditional on every profile of other reports, in expectation over the late tie lottery. Full support gives a strict interim gain for each type. Under CARA the bound is v(s_i Δ)/v(Δ). Publicly revealing the draw before reports can give the favored high type a strict understatement incentive. Sharing booking rights in advance or selling a bond does not by itself supply the needed timing. Members can choose a concealed draw because it insures them before they know who is urgent or favored.

This repair covers arbitrary incidence of binary types whenever each agent sees only its own tie prospects at reporting. Original utility, reporting, liquidity and conditional execution all matter. A genuine common-goal club achieves the same within-state optimum if members can route to the highest job and redistribute real balances. With equal reliability, lower setup cost selects the cheaper feasible device in a symmetric invitation game. Equal prices allow both. Costly full insurance can also lose to the spot arrangement.

## What changes when intermediate values are possible

Keep fixed shares 0<s_i<1 and private continuous values. Consider *any* truthful implementation that funds transfers internally, serves the largest value and gives every i the income s_i M in every truthful state. The transfers on a mimicked report profile are fixed by that outcome. This claim uses private values which can be imitated at every observable history, so a direct report replicates the outcome even if the original protocol is indirect. Local access to unforgeable evidence changes this premise.

Suppose other truthful values have independent-of-i maximum Z with continuous density near x, F_Z(x)>0. A type x imitating r close to x gets income x-(1-s_i)r when Z<r and s_i Z otherwise. Differentiating its expected utility with respect to r at r=x gives

    -(1-s_i) u_i'(w+s_i x) F_Z(x) < 0.

The two boundary values at Z=x agree, so the contributions from switching the recipient cancel to first order. Differentiation is justified locally by bounded derivatives and the continuous density. A small downward report improves the original's prospects. The conclusion concerns exact within-state sharing *and* efficient dispatch under the stated private information. Efficient auctions, approximate insurance, different shares by state, audits, built-in sensors and genuine changes all remain open. Even the binary instance already supplies an ordinary success.

**Exploration ledger.** The framing candidate is mutually advantageous risk sharing. The structural candidate is an institution joining service assignment to funded insurance. The binary instance with a concealed tie lottery is promising. Its literal extension to continuous private demand is dead at the exact fixed-share instance, by the local shading deviation. A sibling uses verifiable graduated claims or a coarse price schedule. A structural successor asks how expensive it is for any affordable information architecture to approach the best sharing of real output. [146](146-the-private-value-of-a-common-goal.md) gives a finite-type way of bounding that loss. Evidence for the class comes from discrete service categories, genuinely private job value and escrowable wealth. The exact two-category restriction is plausible for a two-product queue and unusually demanding as a description of an arbitrary organization.
