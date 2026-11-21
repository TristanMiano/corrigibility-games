# How much peaceful service can an ordinary clearing account actually buy?

**E8, note 170.** The ordinary lottery in 152 deliberately left a positive risk of dispute below the cash threshold for certain service. For an exposed assignment and an ordered last decision, there is an exact optimum over *all* funded, history-dependent ordinary clearing rules in the class below. It is attained by making any remaining dispute risk fall at the last unserved decision. This strengthens the ordinary comparator before pricing any genuine change.

## Assumptions that make the boundary sharp

One designated site gets the whole intact service, and m≥2 other sites can each initiate a costly dispute before the choice becomes irreversible. They take their last independent decisions in a known order. Write j for the last unserved site. The designated site strictly prefers its intact service to even its most generously funded self-initiated dispute when last; e.g. x>t+Q for homogeneous CARA lotteries as in 149 is sufficient. It also prefers to wait in the particular attaining construction below. Dispute awards a physically reduced output y_i to site i if it wins, with probabilities s_i, independent of the earlier history conditional on a dispute. The initiator pays its own finite cost c_i. Local output is nontransferable. A total t of surviving liquid stock can be spent in nonnegative amounts on any sites, potentially contingent on the actual final winner, the first initiator and a privately signaled state. Site i evaluates its own total using increasing concave u_i on the reachable domain, including any fixed protected base stock.

Let d_i be the **cash certainty equivalent for initiating with zero disbursement**, i.e. u_i(d_i)=Σ_w s_w u_i(y_i·1{w=i}-c_i). Take d_i>0 for all unserved originals. All remain independently able to initiate at their own last decision. There is no newly installed goal or ordering delegate. The escrow can observe who initiated and the eventual protected outcome, while a private final draw can be concealed from earlier sites until settlement. An earlier observer cannot learn that final draw while still able to reopen completed service. A finite final response time or private last-stage local information can supply this condition. If everyone observes the last recommendation and can then take another independent action before delivery, it is a different timing game. The cash exists before this exposed interval. All other original wealth is inaccessible to that contract. Coordination to destroy extra nonlocal stock or later independent production would change the payoff bounds.

## An exact feasibility test for heterogeneous founders

For a proposed probability p>0 of peaceful full delivery, take nonnegative cash amounts b_i on peace and a_iw on dispute won by w. The exact conditions for a weakly selected equilibrium, allowing a costless ordinary mediator with the above rights, are

    b_j ≥ d_j,      Σ_i b_i ≤ t,      Σ_(i≠j, unserved) a_iw ≤ t for each w,
    p u_i(b_i) + (1-p) Σ_w s_w u_i(y_i·1{w=i}+a_iw) ≥ u_i(d_i)
                                  for each earlier unserved i.          (1)

Only unserved sites require cash in (1); the designated site and last unserved disputant can receive zero on dispute. Nonbinding residual cash can instead be returned to an eligible passive owner if that preserves the stated incentives. A construction below allocates it or disposes of it consistently. All probability comparisons are conditional on the same fixed public assignment, starting balances and resources.

**Necessity.** At its last decision j can guarantee u_j(d_j) by initiating, and if it passes, the designated site completes the job. On every reached information set with a positive chance of j passing, expected utility of peaceful disbursement is at least u_j(d_j). Conditioning on actual peace and using concavity gives E[cash_j | peace]≥d_j. Every earlier unserved site can also guarantee u_i(d_i) ex ante at exposure: initiate at its turn if reached, and otherwise someone else initiated first, sparing it its own cost. On actual dispute histories give each earlier site the benefit of always being passive. Conditional on the final winner and on dispute, replace its random cash by its mean. On peace do the same. Concavity and nonnegative cash make these optimistic bounds. Since the payoff draw occurs after the first initiative, its probabilities conditional on dispute remain s_w. These conditional means supply a feasible point of (1). This argument includes correlated disbursements, asymmetric histories and privately signaled decisions.

**Sufficiency.** The clearing institution provides the stated settlement if every earlier site passes. Only then disclose the final private branch to j. With probability p, give j b_j on completion and zero on its own initiation; it can choose completion. On the remaining branch, promise it zero on completion or its own initiation. Its strictly positive d_j makes initiation optimal there. Pay the other sites the a_iw on that dispute branch. If an earlier site initiated instead, give that initiator zero, settling residual stock elsewhere. By (1) each earlier site prefers, at least weakly, to wait given the others' specified behavior. Additional identical opportunities before the hidden final draw do not change this comparison if they convey no relevant new information. The designated site needs no inducement when intact service or someone else's disputed draw dominates its self-initiated alternative. Hence p is attained. At binding inequalities specify tie selection. With slack in t and the desired p, strict earlier and peaceful-last decisions can generally be obtained by slightly increasing the peaceful payment to j and lowering p if needed. At the first feasible cash amount the last site can genuinely be indifferent.

## A closed form with common risk preferences

Let n=m+1, h=m-1, homogeneous u, d, y, equal strengths 1/n and identical sunk stocks. For the h earlier sites let

    Φ_h(t,y) = h u((t+y)/h)                       if t≥(h-1)y,
               u(y)+(h-1)u(t/(h-1))               otherwise,
    G_h(t) = (1-h/n)u(t/h) + (h/n)Φ_h(t,y)/h.

For h=1 use only the first branch. G_h is the highest average utility on dispute attainable for the earlier sites. Give them all t. If one of them wins the nontransferable output, use cash to equalize their final values as far as nonnegative disbursements permit. Otherwise split it evenly. On peace the earlier sites can receive at most t-d in total, and symmetric division is best. These distributions attain both group bounds **for every earlier site simultaneously**, because they are exchangeable. Thus the maximum peaceful service probability is

    0                                             for t<d,
    [G_h(t)-u(d)]/[G_h(t)-u((t-d)/h)]            for d≤t<md,
    1                                             for t≥md.            (2)

When t<d the last unserved site always initiates. In the middle range the numerator is positive because the free contest lottery alone beats initiating. At md every unserved site can receive d on peace. For n=3 the middle branch becomes [u(t+Q)-u(d)]/[u(t+Q)-u(t-d)] when u is CARA and Q is the free contest CE. At the 152 fixture t=0.19 the upper boundary is about 0.6637. Its earlier construction of 0.3319 was a strict-waiting example below this boundary. The sharper control explicitly specifies which site sees the resolving information last. The pooled upper bound in 152 remains applicable without this stronger description of final closure and eligible disbursements.

## How the identity of the last decision maker matters

For linear utilities write q_i=s_i y_i, d_i=q_i-c_i. To implement p>0, the minimum cash for the prescribed last site j is

    T_j(p)=max{d_j, p d_j + Σ_(i earlier) [p q_i-c_i]_+}.            (3)

In (1), each earlier site needs expected cash at least [d_i-(1-p)q_i]_+. The total expected cash available after the last site's reservation is at most t-p d_j. This proves necessity. Any sufficient expected cash can be divided among the earlier sites in the same proportions across the peaceful and disputed cash budgets, which suffices by linearity. If the aggregate requirement is zero, each earlier site already strictly or weakly prefers waiting. To choose j to attain a desired p at budget t, require d_j≤t and minimize (3)'s second entry among those eligible. Relative to Σ_i[pq_i-c_i]_+, making j last adds min(p d_j,(1-p)c_j). A real sequencing change needs authority, time and a genuinely private final observation. Permuting labels in an equation does not grant those powers.

**Naturality and frontier.** An accountable settlement operator, bounded cash, indivisible expiring service and an identified last controller give a use case for (1). Insolvent contracts or an operator unable to observe who closed the dispute cannot offer this rule. Common knowledge of every participant's individual certainty equivalent is a strong assumption in the attained heterogeneous bound. The class reveals both a real obstacle and how the ordinary participants can repair it. The framing candidate is that the price of consent depends on the *remaining* opportunity to let another party decide. The structural candidate compares conditional reservation utilities on peaceful and disputed branches and allocates actual cash accordingly. The instance claim that a just-insufficient certain-peace budget always makes all original agents dispute is dead at d<t<md. A sibling uses the last site's private resolving information. A structural successor prices earlier disclosure, new late decision rights and the incentives of the particular actor that finances the account.
