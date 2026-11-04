# A chosen contractual floor for renewable service

**R0005 local mathematical construction, self-checked.** This note repairs
a post-payment weakness in the simple fairness service model. It uses a
bounded, contract-dependent concern for another agent's outcome, related
to E3's capped auxiliary goals. The extension being investigated is
renewable service with voluntarily chosen counterparties and new accepted
obligations, without a penalty for changing utility or code. The elementary
incentive and compensation arguments are not claimed as novel machinery.

## 1. Why a delivery check alone misses post-payment bargaining

In 096, b=3, c=1, p=3/2 and a producer with alpha=0, beta=2/5 strictly
prefers delivery to simply keeping the advance. Delivery gives net gains
(1/2,3/2). That local comparison does not by itself settle the full game.

Suppose that after receipt the producer can install, at real cost k, a
goal that credibly withholds service until an additional fee q is paid,
then supplies and insists on that revised total price. Such a goal must
be implemented and recognized; it is not obtained from a verbal threat.
For q=1/4, the completed gains become (3/4,5/4). The existing G values
this outcome at 3/4, compared with 1/2 from honoring the first quote.
For k<1/4 it therefore prefers this continuation if the buyer actually
pays. A buyer whose remaining alternative is worth less than 5/4 pays.

One explicit implementable preference template can rank, first, delivery
at the revised total price; second, retaining an insufficient payment
without delivery; and last, delivering below the revised price or
overcharging it. On the finite payment/outcome grid, bounded numerical
utilities implement those rankings. An extra small term favoring retained
payment over refund makes the refusal branch strict. The template can
remain indifferent between code representations: its preferences concern
physical receipts and delivery, not code retention. This is a candidate
additional goal capability, not a consequence of the two-parameter G menu.

More generally, with alpha=0 and beta<1/2, the old G's value of a completed
sale strictly increases with its total price, with slope at least
1-2beta. A recognized demand for extra fee q can improve its current
value by at least (1-2beta)q-k, subject to the buyer's actual response.
The buyer's advance is sunk at this later decision. Initial willingness
to pay a quote therefore differs from willingness to pay an extra fee
after exposure. Anticipated revisions can destroy the initial trade.

This is a scoped failure of the simple fairness mechanism in a richer
goal-and-offer menu. Ordinary refusal to supply is only one deviation.
The constructive repair below gives the supplier an incentive to preserve
the customer's agreed outcome, while allowing productive amendments.

## 2. A contractual outcome floor

Let an accepted and funded service agreement specify a customer's net
project gain q=b-p. The relevant outcome includes all payments, refunds,
delivered service, delay and other expenses attributable to that agreement.
Labels such as an extra "gift" cannot erase a transfer from the account.
Before accepting an agreement there is no obligation to this customer.
After acceptance the promised q is a dated physical/economic term, not a
number the producer can rewrite by editing its memory.

Consider the producer's genuine successor criterion

    C_i(H)=W_i(H)-lambda [q-W_j(H)]_+,    lambda>1.     (1)

The W's in this local equation are the two parties' net gains for this
transaction. At a later choice the current C evaluates an offered goal
change through its actual resulting history. A successor uses its own
criterion after activation; the old criterion still evaluates the dated
obligation when deciding whether to create that successor.

Suppose:

1. An executable honored continuation has gains (v-q,q), where v=b-c.
2. Every feasible continuation being compared has W_i+W_j<=v, including
   transfers, additional fees, partial performance and interruption.
3. The incumbent can still choose that honored continuation under the
   counterpart's actual strategy.

**Proposition 1 (productive-frontier certificate).** The honored continuation
maximizes current C. Every outcome with W_j<q is strictly worse; outcomes
with W_j>=q can tie only if they give i the same maximum v-q. The statement
also applies to lotteries and arbitrary proposed successor goals through
their induced outcome laws.

**Proof.** If W_j<q, then

    C_i <= v-W_j-lambda(q-W_j)
         = v-q-(lambda-1)(q-W_j) < v-q.

If W_j>=q, then C_i=W_i<=v-W_j<=v-q. Taking expectations preserves the
weak bound, with strictness for positive-probability shortfalls. An
anticipated goal rewrite is a continuation law, so has the same bound.
Any extra real implementation expense reduces its feasible net surplus.
QED.

For direct default, C_keep=p-lambda b and C_supply=p-c. Delivery therefore
has advantage lambda b-c>0. For an extra fee a after full delivery, the
change in C is (1-lambda)a<0. The latter check closes the profitable
renegotiation direction in section 1 under the proposition's resource cap.
There is no utility-change penalty in either comparison.

The change from F to C is genuine. At a prepaid decision F ranks keeping
p above supplying for p-c, while C ranks supply above keeping. It is a
change of outcome ordering, not a positive affine recoding or a new policy
described with the old terminal preferences.

## 3. Partial service and refunds remain available

Let y be delivered service, 0<=y<=b, and k(y) its real own-project cost.
Allow a net payment r, including refunds and additional fees. Then

    W_i=r-k(y), W_j=y-r, W_i+W_j=y-k(y).

If y-k(y) is maximized at full delivery b, Proposition 1 applies. For
example k(y)=cy/b with c<b gives a strictly increasing total surplus;
the quadratic-effort specialization y=be, k=ce^2/2 also has this property
when b>c. If the producer refunds b-y to keep the customer at q after
partial delivery, its own value is y-k(y)-q. Full delivery is strictly
better in these examples. Thus the proof neither deletes partial effort
nor presumes that a refund is costless to its payer.

If a different delivery method raises joint net surplus while preserving
q, the new C prefers it. If a buyer has a better outside service, a funded
cancellation can make the buyer whole and release the producer for a
better task. The relevant condition is the actual attainable surplus and
compensation, not preservation of an initially named action or partner.

## 4. A compensation repair beyond a fixed surplus cap

For several outstanding obligations, let

    C_i=W_i-sum_j lambda_j(q_j-W_j)_+.                 (2)

Suppose a feasible continuation has deficits d_j=(q_j-W_j)_+. If the
producer can actually implement a compensation continuation that raises
each W_j by d_j, lowers its own W_i by at most a_j d_j, and changes no
other valued consequence, then the C improvement is at least

    sum_j (lambda_j-a_j)d_j.                          (3)

For lambda_j>a_j, every positive deficit is therefore dominated by its
funded compensation repair. At unit transfer cost, a_j=1. With real
transport/settlement expense or differing dates, a_j must include those
conversion costs. This is a pointwise argument and extends to stochastic
outcomes when the repair is feasible in each realized state.

Equation (3) does not create funds or a settlement window. It requires
available material, transferable value, enough work and time, and an actual
continuation that makes the payment. A proposal to install a later
controller must be evaluated with that controller's real behavior;
assuming that every controller will subsequently compensate is invalid.
A current settled deficit with immediately available transfer has the
simple repair. A contingent future deficit may need retained control,
funded conditional execution, a reserve, or an appropriate new goal.

Without this repair property, a rise in total attainable surplus can relax
the fixed-cap protection. If the cap rises from v to v+Delta, the same
calculation only gives

    C_i <= v-q+Delta-(lambda-1)(q-W_j)

on a deficit outcome. A sufficiently large additional gain can outweigh
a finite penalty. This is a precise remaining obligation, paired with
the funded compensation condition that restores the protection; finite
penalties are not silently promoted to unconditional rights.

## 5. Renewable contracts and actual partner choice

For episodes t=1,...,N, let j(t) be the voluntarily chosen customer and
q_t the outcome promised by an accepted contract. A reusable criterion is

    C_i(H)=W_i(H)-sum_t delta^(t-1) lambda_t
                     [q_t-x_{j(t),t}(H)]_+.           (4)

Only actual accepted obligations enter. Net episode gains include all
associated payments and physical costs; accepting another partner does
not erase an outstanding obligation. A concrete model must specify the
available capacity, overlapping promises, funded settlement and the
reference epochs. One-shot assertions cannot justify double booking.

Choosing a new contract q_t under the same rule (4) is a policy/contract
choice, **not another utility change**. Installing (4) from F, changing
its substantive penalty rule, or replacing it by a genuinely different
ordering can be a utility change. This distinction is needed when
counting actual accommodation across renewable opportunities.

Whenever all obligations can be honored, C_i agrees with own W_i on those
continuations. It therefore preserves the founder's ranking among honest
partners and productive methods at that stage. Unlike the unequal-payoff
ranking in 096 equation (9), extra concern for a customer's unpromised
surplus does not distort this ranking. The producer still needs an actual
offer, a willing customer, funding and credible implementation.

The criterion also has 094's form W_i-P with P>=0. An executable honored
reference Q has zero penalty. Any further change approved by current C
therefore preserves at least Q's expected original welfare. This floor
can continue to apply as resources renew because it uses a nonnegative
shortfall penalty; it does not cap all future productive wealth by an
initial constant. It remains conditional on Q's real availability.

## 6. Initial choice, costs and controls still need the complete game

If the recognized, executed goal opens a sequence of transactions with
current-original net value V_C, its real preparation, activation,
verification and reserve costs must be subtracted. Adoption is optimal
only when that resulting value reaches the best actually available
ordinary commitment, delegate, other partner, delay strategy and combat
continuation. Equal-cost matched delegation may tie; cheaper ordinary
implementation may win. The present certificate proves continuation
incentives, not these earlier inequalities by itself.

A staged installation can occur before the customer exposes its payment.
If the original founder expects gains exceeding the total remaining and
already-paid installation expense, it also wants to pay the final
activation expense after preparation is sunk. But this elementary
observation requires the customer's real later response and the actual
attack and interruption options. No atomic mutual rewrite is inferred.

The construction's independent motivation is a preference for fulfilling
voluntarily accepted obligations. The exact numerical floor, reference
account and recognition technology are deliberately designed. That is
an intervention to investigate, not empirical evidence that such goals
arise frequently. Subsequent work must establish who can construct and
fund it, why each party consents, and which physical or informational
changes support it or instead favor ordinary cooperation, exit or combat.
