# Prepayment, renegotiation and the choice of a productive partner

**R0005 working derivation; not a completed physical game.** This note
enlarges 095's raw action menu. Its transfer calculations show both a useful
route to voluntary change and why a no-transfer matching result requires
rechecking. All prices and gains below use a declared common project-value
numeraire; funding and work flows belong to the physical implementation.

## 1. A changed producer can make advance payment credible

A producer can supply a buyer with service worth b at an own opportunity
cost c, where b>c>0. The buyer can pay p>=0 before delivery. The producer
then chooses to supply or keep the payment without supplying. No external
enforcement is present in this subgame. With v=b-c and B=b+c, the final
net project gains (producer, buyer) are

    supply: (p-c, b-p),       keep: (p,-p).

An F producer strictly keeps a positive payment. A G producer has 094's
criterion with alpha>=0, beta>0. For p<=B/2 its gain from supply over keep is

    2(alpha+beta)p-c-alpha B.                           (1)

For p>=B/2 the gain is beta B-c. Consequently, when beta B>c, delivery
is strictly credible above the threshold

    p_IC=(c+alpha B)/[2(alpha+beta)] < B/2.              (2)

Equality permits delivery at indifference. Below p_IC, advance payment
followed by voluntary delivery is not a continuation equilibrium for this
unchanged G. The calculation does not assume that the producer values
keeping this utility or its code.

Before taking a payment, the producer also needs to prefer the completed
sale to no sale. For p<=B/2 that condition is

    p>=p_IR=(c+alpha B)/(1+2alpha).                     (3)

For beta<1/2, p_IC>p_IR: the later delivery incentive is the tighter
constraint. For beta>1/2, p_IR>p_IC: participation is tighter. These are
different decision stages and should not be collapsed into one condition.

At p=B/2, both parties obtain v/2 and G strictly supplies whenever beta B>c.
Thus a single G can trade productively with an F through funded prepayment.
In 095's simultaneous two-way-production environment, F chooses no own
contribution, but can buy the G's contribution in this way. Its total pair
surplus is v, rather than the raw G,F subgame's zero or G,G's 2v.

This is a concrete repair to the omitted-transfer restriction. It preserves
the usefulness of genuine change: the F producer would keep the advance,
whereas G delivers. It also limits a mutual-adoption claim: a sufficiently
profitable route to buy another agent's work can replace changing one's
own goal. Funded payments, timing and available counterparties decide which
route is actually chosen.

## 2. Price preferences and the effect of bargaining power

For a completed sale, the producer's G value is

    g(p)=p-c-alpha(B-2p)_+-beta(2p-B)_+.                (4)

It increases with slope 1+2alpha below B/2, and has slope 1-2beta above B/2.
Hence a producer able to choose an acceptable price prefers balanced gains
p=B/2 if beta>1/2, but prefers the highest acceptable price if beta<1/2.
The latter can still credibly deliver because c/B<1/2 leaves a nonempty
interval c/B<beta<1/2. This interval is an open constructive region, not
a claim about its frequency in a population.

It would be incorrect to give the producer its favorite price regardless
of the bargaining protocol. With no sale as its alternative, a G can
accept a lower positive-valued offer; a buyer with proposal power can
extract some of the surplus. If a completed pair has total surplus v,
current G participation alone gives the material-share lower bound

    x_G >= alpha v/(1+2alpha)                         (5)

whenever G is the poorer member and its outside G value is zero. At that
bound, current G utility is zero although original material welfare is
positive when alpha>0. More generally, an outside current value u gives
x_G >= (u+alpha v)/(1+2alpha) in this region. These are necessary
participation bounds; they neither choose a price nor prove that the
relevant delivery technology is available.

An existing balanced G,G partnership offering z to a G raises its outside
value to z. The general welfare-floor lemma then requires any accepted
replacement to give it at least z in original welfare. A replacement
whose total net surplus is at most z cannot also give an F counterparty
a strictly positive payoff. This protects a *real available partnership*;
it is not an assumption that every G always has one.

## 3. Later accommodation can repair a newly binding delivery constraint

Consider alpha=0, 0<beta<1/2 and a buyer whose maximum acceptable price is
P=b-o, with outside payoff o>=0. Suppose

    c<P<B/2,       beta<c/(2P).                        (6)

The existing G cannot credibly deliver at any acceptable price. It may,
however, voluntarily install beta' with

    c/(2P)<beta'<1/2.                                 (7)

The interval is nonempty because P>c. The new G strictly delivers at P;
both the old and new G evaluate the completed sale as P-c because the
producer is behind the buyer. If A_R is the discounted number of remaining
identical opportunities, update expense k is included in own welfare, and
the best genuinely available old-goal alternative has value V_alt, then

    A_R(P-c)-k > V_alt                                (8)

makes this update strictly better than that alternative. For a claim of
optimal adoption, V_alt must include all actually available ordinary
contracts, delegation, other buyers, further bargaining and combat.

**Exact local example.** Let b=3, c=1, P=3/2, beta=3/10, beta'=2/5.
The sale gives (1/2,3/2); keeping the advance gives (3/2,-3/2). Before
the update, the latter is valued at 3/5 and the sale at 1/2, so the buyer
anticipates default and withholds the advance. After the update, keeping
is valued at 3/10 and delivery at 1/2. The old G therefore chooses the
new goal before payment when its actual future profit covers the update
and alternatives. Once paid, the new G refuses a rewrite leading to the
same default, because its own current criterion still ranks delivery
higher. This is a genuine preference reversal with current-self evaluation
at both decisions.

Increasing the buyer's outside opportunity can create this constraint;
renewable profitable opportunities can make the repair worth its one-time
cost. A better available alternative buyer can instead make retaining the
existing goal more attractive. Neither comparison alone establishes an
endogenous market change: the source and price of the outside option must
be supplied in the complete instance.

## 4. A price floor can be relaxed by another voluntary goal change

The delivery threshold p_IC is not automatically a permanent bargaining
floor. An existing G offered p between p_IR and p_IC values completed
service positively, even though it would keep the advance under its old
goal. If a new goal can implement that completed service at a sufficiently
small expense, the old G can approve the change. Equations (6)-(8) are
an explicit example. Thus an obstruction using only unchanged-beta
delivery is repaired by renegotiating the successor goal.

By contrast, a proposed completed sale below the old goal's participation
threshold has negative old-goal value relative to no sale. Merely changing
the evaluator used *after* adoption does not make the old agent consent.
A larger productive surplus, a funded payment, a better continuation,
or another real benefit can repair that participation failure. A source
of those benefits is required; a new utility's approval is insufficient.

## 5. Partner choice can change the goal-design problem

For alpha=0 and beta<1/2, suppose buyer j has an acceptable maximum price
P_j, service cost c_j and benefit b_j. Put

    x_j=P_j-c_j, y_j=b_j-P_j,
    theta_j=c_j/min(2P_j,b_j+c_j),
    d_j=(x_j-y_j)_+.

At an acceptable profitable price, j is credibly serviceable when
beta>=theta_j, with strictness as above. Among such available transactions,
the G producer chooses a maximizer of

    x_j-beta d_j.                                     (9)

This follows from (4), not a type-affinity bonus. With common y_j, the
ranking agrees with original own-welfare ranking. With different y_j it
can differ: at beta=2/5, outcomes (3,0) and (2,2) have G values 9/5 and 2,
so G prefers the second even though F prefers the first. An original
founder choosing beta should anticipate this consequence, together with
the change in which customers can trust it. Actual availability and
counterparty choice cannot be replaced by a favorable list of prices.

A richer candidate is a goal that penalizes unfulfilled accepted service
obligations while agreeing with own welfare on fulfilled contracts. That
design may preserve the founder's ranking among honest partners while
making delivery credible. It must itself have an explicit physical
contract predicate, costs, recognition and revision incentives; the
proposal is developed separately rather than assumed free here.

## 6. Matching-selection attempts that must not become results

A three-G construction with a uniformly rotating idle agent initially
looked promising: each founder would receive 2/3 of a productive pair's
gain, and a unilateral F deviation could leave two G agents trading with
each other. But a voluntary exclusive G,G agreement gives its members the
full pair gain. If such agreements are feasible before the random
rotation, they can block it. Stagewise stability after a lottery therefore
does not prove stability of the earlier partner-selection arrangement.
Random physical availability or costly exclusivity would be different
models requiring new derivations, not repairs already established here.

Likewise, a G excluded from a G,G match may accept productive business
from an F; odd numbers and real outside options matter. A restricted
no-transfer all-G adoption equilibrium from 095 cannot be transferred to
this enlarged menu without checking those options. Positive routes remain:
one founder can choose a credible service goal, later goal renegotiation
can restore a lost market, and genuine alternative partners can protect
participation. The next integrated game must establish their actual
availability and selection rather than imposing rotating access.
