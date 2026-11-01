# R0002 working generalization: insured guarded accommodation

**Construction with the execution repair in [056](056-contribution-rewards-through-renegotiation.md).** Insurance extends the guarded adoption mechanism from linear founders to an arbitrary continuous increasing concave own-project utility for one participant. The small rewards below describe the fixed-contract subgame. The integrated construction also rewards B's contribution and uses larger finite rewards to cover post-miss renegotiation. It separates a simple original goal from deliberately chosen commitment and protection terms.

## 1. A class of original preferences and negotiated terms

Original A values f(X), where f is continuous, strictly increasing and concave on the bounded physical output interval. Original B values Y linearly. Their stocks are R_A,R_B; contribution costs are c_A,c_B; installation material losses are k_A,k_B. Let V=bY_0, D=(b-a)Y_0 and

\[
C_n=V-c_A-c_B-k_A-k_B>0.
\]

Assume 0<a<b<1, b>=2a, aY_0<min(c_A,c_B), and D>c_B. Choose any r in (0,C_n). A is insured at q=R_A+r by a fixed transfer

\[
k=c_A+k_A+r
\]

in both success and failure states. B receives the reactor output and pays k. Finite collateral requires

\[
R_B\ge c_A+c_B+k_A+k_B+r.
\]

After mutual effort, X=q surely and E Y=R_B+C_n-r. Both original goals strictly improve over retained stocks. The minimum B holding on failure is R_B-c_A-c_B-k_A-k_B-r; choosing it above the late-combat reserve from 047 supplies a direct execution safeguard.

## 2. Current goals, dominant contribution and protection

A may choose

\[
G_A=f(X)+\eta(X+Y)+\beta e_A-K_A I_A,
\qquad \eta\ge0,
\]

and B may choose G_B=Y-K_B I_B. The compatibility gates and unsafe-approval definitions are those in 046. B's guard is a genuine history-preference change even though its ranking of terminal output quantities remains linear. Positive eta additionally gives A a genuine concern for B's output; beta changes its ranking of contribution histories.

Under insurance, A's work-versus-shirk margin against B shirking is

\[
f(q)-f(q+c_A)+\eta(aY_0-c_A)+\beta.
\]

Choose

\[
\beta>f(q+c_A)-f(q)+\eta(c_A-aY_0).
\]

Because b>=2a, this also makes contribution strict when B contributes. A therefore contributes in every effort equilibrium. B's best response is then contribution, since D-c_B>0. The effort outcome is unique. No mutual-shirk selection is required.

The productive default maximizes expected total output S=R_A+R_B+C_n and e_A=1. The certificate in 043 gives E f(X)>=f(q) for every continuation accepted by current A. Concavity then gives E X>=q. Current B's participation gives E Y>=R_B+C_n-r. The total bound leaves no original Pareto improvement over the insured default. Conversely, original A cannot improve beyond f(q) while meeting B's protected output floor: E X<=q and Jensen apply. B cannot improve beyond its default while meeting A's protected expected-utility floor. These statements quantify over all physically feasible accepted lotteries, not just fixed shares.

The finite guard constants exceed the maximum base utility over the bounded episode. Subtracting f(0) makes the output part nonnegative without changing preferences or coefficient ratios. A further positive affine rescaling requires consistent rescaling of eta, beta and K_A. Safe original-f-preserving parameter variations remain available. A proposed change of f itself needs a fresh current-self participation and continuation certificate; its effect on archived founder welfare is not assumed away.

## 3. Adoption in the guarded first-contact game

Use 046's pre-observation installation timing and sound actual-controller verification. Suppose an incompatible controller obtains at most its original retained-stock utility: for A this follows from the unilateral physical audit, concavity and sW_0<=R_A; for B require (1-s)W_0<=R_B. Neither receives outgoing concessions or productive participation from the guarded partner.

Against a compatible guarded partner, any compatible alternative must meet that partner's protected floor. The preceding optimality bounds therefore apply. An incompatible alternative gets at most f(R_A) or R_B, strictly below f(R_A+r) or R_B+C_n-r. Both genuine changes are best responses, with ties for equally costly compatible delegates. Later compatible entry may tie if it preserves the same opportunity. Cheaper compatible implementation changes the comparison, as in 046.

This establishes the adoption argument for a broad original-preference class conditional on the guarded physical implementation. It does not assert unique equilibrium, population prevalence, arbitrary semantic verification, or stability when a partner can alter the protected continuation outside the declared mechanism class.

## 4. A positive-cost numerical witness

Take R_A=3, R_B=4, c_A=c_B=8/5, a=1/10, b=2/5, Y_0=10 and k_A=k_B=1/20. Then C_n=7/10. Choose r=3/10, giving

\[
k=39/20,\quad X=33/10\ \text{surely},\quad E Y=22/5.
\]

B's failure and success holdings are 2/5 and 52/5. Both original agents strictly gain over their original stocks, and B's failure holding leaves a positive late-attack reserve. For f(X)=log(1+X), choose eta=1/10 and beta=1. A's worst effort margin is

\[
1-3/50-\log(59/43)>0,
\]

since log(59/43)<16/43<47/50. B's effort margin against A contributing is 7/5>0. The physical episode has X+Y<=17, so K_A=8 and K_B=20 exceed the respective base bounds: log(18)<3 implies A's base is below 3+17/10+1<8, while B's is at most 17.

The current goal before A's activation is still log(1+X); its adoption gain is log(43/10)-log(4)>0. After activation, the displayed G_A governs its decisions. Neither B's guard nor A's contribution reward is inserted into those original adoption utilities.

## 5. Controls and remaining integration

An ordinary fixed-goal insured A strictly shirks in the simultaneous hidden-effort class. A matched effort delegate implements the same insurance and is a successful alternative. Observing A's effort before B chooses the option contract in 043 also implements it with unchanged goals. These repairs must receive their actual information, cost and timing advantages. The broad ordinary-transfer bound in 042 applies to the simultaneous hidden-effort technology, not to those stronger controls.

The physical schedule, late attacks and first-contact information audit are supplied in 049, with strengthened execution, private-information and exit checks in 056. [E3](../models/E3.md) consolidates the linear and insured cases under one certificate. R206 remains conditional on that implementation and R205's adoption premises; complete off-path private-protocol sequential equilibrium remains open in 057.

## 6. Allowing agents to revise the agreed task

A contribution reward need not forever name one immutable task. Define e_i(H) through timely fulfillment of i's *jointly registered* obligations during its evaluator epoch. Plans may be jointly amended before performance deadlines; a past missed obligation remains missed for the archived evaluator. The goal's history predicate is fixed at installation and reads valid future plan replacements. Neither a new no-work plan nor a changed private report erases an earlier miss. The allocator's joint-authorization record determines which plan is in force; 056 makes this distinction and its execution bound explicit.

For the present project, Work fulfills the obligation and Shirk fails it, regardless of whether the reactor's random outcome succeeds. If agents jointly replace the plan, each evaluates the complete replacement continuation using its current criterion. The indicator is still bounded above by one, and the existing productive fallback attains one. Therefore, for a chosen goal f(X)+beta e_i with beta>=0, every accepted replacement preserves the current original-f floor even when new productive opportunities become available. A vacuous no-work plan cannot purchase a reduction of original expected utility by offering a larger contribution reward: the existing fallback already receives the maximum reward.

This gives a concrete flexible guard design to investigate beyond the fixed project. It requires reliable joint registration and a precise physical fulfillment predicate for each allowed plan. It is not a claim that arbitrary natural-language promises are semantically verifiable. Positive eta on total output instead requires tracking its changing opportunity bound, as quantified by 043's efficiency-gap term. Both designs permit genuine changes; their different protection and flexibility properties should be compared under actual future opportunities rather than imposing a permanently closed task menu.
