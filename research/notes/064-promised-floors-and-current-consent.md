# Promised floors can prevent breach rents while permitting current-goal repair

R0003 working mechanism refinement. A protected *current fallback* and a chosen *reservation for a new agreement* are different objects. This note distinguishes them and derives the bargaining region, instead of treating an aspirational promise as an already credible fallback. It connects the ordinary-entry repair to the current-self consent rule and exposes a consequence of blindly resetting protection after a strategic miss.

## 1. The actual-fallback rule can reward breach followed by modification

Use note 063's ordinary-A/guarded-B contract with entry transfer r=1/20. Mutual contribution gives (63/20,18/5). A that privately misses its contribution receives mean 31/10; B's actual default falls to 9/4. If A can then install a truthful guarded controller for 1/20 material, disclose the miss, and reopen bargaining using only B's **reduced actual** mean as its reservation, the fully repaired total is 67/10. A proposer allowed to retain all added surplus can offer B 9/4 and retain 89/20=4.45.

B with positive concern for A strictly prefers that feasible repair to its reduced default, despite its own original mean staying at 9/4. A's original payoff 89/20 exceeds both 63/20 and its pre-repair 31/10. Thus the fixed-contract effort margin alone does not secure A's timely contribution when this later entry/renegotiation is actually available. The calculation requires a feasible late installation, credible disclosure, and the stated proposal rights; those are mechanisms to audit, not assumed universal capabilities.

This is a precise repair target. It does not undo the ordinary fixed-contract calculation, nor make profitable renegotiation undesirable. The agreement needs to preserve the benefit of feasible repair without making the earlier deliberate breach a route to a larger claim.

## 2. A reservation for future agreement need not equal unilateral refusal value

An agent can choose a finite approval preference that refuses a new agreement unless it meets a specified original-welfare reservation r_i. Its actual refusal continuation may be lower. The guard makes its reservation credible as a preference/commitment; it does not physically create r_i after the other agent refuses cooperation. State both numbers.

In the preceding ordinary-entry example, B can retain the **pre-performance promised** reservation 18/5 for any late replacement before the reactor outcome is observed. A's private miss or subsequent revelation does not itself reduce this new-agreement reservation. After A's delayed installation, the repaired total 67/10 then leaves A at most 31/10. This blocks the displayed breach-and-late-entry gain relative to 63/20. A can still restore the original ordinary contract without that extra installation and receive 63/20, making delayed performance at most tied in this terminal-material comparison. A real delay cost or an appropriate contribution preference can make the timely action strict.

The reservation is a voluntarily chosen negotiating commitment, not a general theorem that everyone should insist on their earlier allocation. The model must charge its implementation, retain physical refusal and Attack, and evaluate adopting it using the original current criterion. A fixed-utility binding delegate can carry the same reservation when its actual technology permits it.

## 3. Exact current-consent region with reservations

At a negotiation point let the actual executable rejection allocation be (a,b), with total S_0=a+b. A proposed plan has total S=S_0+g and can divide it by transfers. Current output criteria are X+lambda_A Y and Y+lambda_B X, with 0<=lambda_i<1. All other history terms are constant in the comparison. Write ell_i=lambda_i/(1-lambda_i).

Current-utility acceptance requires

\[
x\ge a-\ell_A g,\qquad
x\le a+(1+\ell_B)g.
\]

The selected new-agreement reservations require x>=r_A and x<=S-r_B. Thus a mutually acceptable allocation exists exactly when

\[
\boxed{\max\{r_A,a-\ell_Ag\}
\le \min\{S-r_B,a+(1+\ell_B)g\}.}
\tag{1}
\]

Physical nonnegative holdings and any other actual transfer constraints must also be intersected with this interval. For g>=0 and unconstrained nonnegative divisions, the displayed acceptance/reservation conditions are equivalently

\[
r_A+r_B\le S,\quad
r_A\le a+(1+\ell_B)g,\quad
r_B\le b+(1+\ell_A)g,
\]

together with feasibility of nonnegative holdings. These follow by comparing the two lower bounds with the two upper bounds; the remaining current-acceptance comparison holds for g>=0. Strict current gains require interior inequalities at the corresponding participation boundaries; weak acceptance is stated as such.

This expression separates three mechanisms: enough total resources to honor reservations, enough current concern to accept a loss in own original material in exchange for the other's larger gain, and a feasible physical division. Increasing capability can change S, the actual cost included in g, or the implemented reservation rule. Those are distinct changes.

## 4. Restoring the original productive promise can be acceptable after a miss

Return to two installed controllers, t=9/20, and promised means q=(63/20,71/20). Require a late full-production agreement to restore q before any reactor outcome. This is a new-agreement reservation rule; do not claim that a unilateral refusal after a miss already secures q.

At lambda_A=lambda_B=2/3, both current agents prefer restoring q to each actual missed-input default in note 061:

| Private initial-input state | Change in original A material | Change in original B material | Current A gain | Current B gain |
| --- | ---: | ---: | ---: | ---: |
| SW | -1/4 | 33/20 | 17/20 | 89/60 |
| WS | 27/20 | 1/20 | 83/60 | 19/20 |
| SS | 1/5 | 3/5 | 3/5 | 11/15 |

The old missed process reward remains missed. If a fresh task goal is installed, the old evaluator scores the actual repaired material and its own unchanged past flags; it does not award itself the successor's new reward. A current agent can therefore voluntarily accept a repair that lowers its own original material in one private state, because its **then-current** concern values the partner's larger gain. Original-founder welfare is reported separately in the table.

For arbitrary success share t in (33/80,47/80), a controller that alone missed its contribution accepts restoration of the full promise whenever

\[
3t-8/5+3\lambda(1-t)\ge0.
\]

The largest concern threshold over the closure of that share interval is 29/141. Consequently lambda>=2/3 supplies ample slack for this local repair as well as note 060's stronger attack comparison. After two misses, each original material gain is already positive over that share region. These are current-consent inequalities, not a claim that hidden inputs automatically become publicly known or physically supplied.

The fixed promised allocation also avoids section 1's disclosure-dependent reset of the counterparty's claim. Actual late performance still needs incentives, enough remaining work/time, and binding rights. Note 061 gives voluntary single-input completion and a possible fresh-goal implementation when both inputs are missing. An ordinary contractor's different incentives must be checked under its actual current criterion, as in note 063.

## 5. Loss of resources requires a contingent repair of reservations

If an observed physical shock reduces the new feasible total below r_A+r_B, no division meets both promises, even when a smaller plan would improve both current utilities relative to the damaged refusal continuation. That follows directly from (1). It is a limitation of that reservation rule, not of all goal changes or all feasible compromises.

A chosen rule can instead allow a specified reduction after a verifiable exogenous shock, followed by rechecking (1), or price a reserve/insurance mechanism into the original agreement. Such a revision must distinguish a genuine shock from an agent deliberately damaging the state to lower the other's claim. Sound records of cause, priced insurance, or a different agreed sharing rule are substantive capabilities, not automatic consequences of knowing utilities. An unrestricted exception that lets a private miss or strategic destruction lower the protected reservation restores the breach incentive being repaired.

Thus promised floors supply one constructive protection against strategic renegotiation, while contingent redesign supplies a constructive response to real losses. The complete model must examine both. No indefinite freezing or unrestricted innovation result follows from a fixed finite-episode reservation.
