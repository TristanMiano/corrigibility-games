# Renewal, current-goal adoption and voluntary assignment

**R0005 conditional integration, self-checked.** The continuation mechanism is 097's
chosen preference for honoring accepted outcome floors. This note joins
it to recurring opportunities and partner choice at explicit levels of
support. The assignment certificate uses standard matching/LP machinery;
it does not claim a new matching theorem or turn a core allocation into
a complete bargaining protocol.

## 1. A recurring opportunity can pay for one genuine change

Consider n remaining identical renewable cycles, discount factor
delta in (0,1], and A_n=sum(t=0,...,n-1)delta^t. Let a be the largest
per-cycle original/current payoff actually available without installing
the proposed reusable goal. This includes ordinary peaceful division,
available policy commitments or delegation, alternative customers,
autarky and physically available combat. Let r be the per-cycle payoff
from the best implemented goal-enabled service arrangement, after all
recurring communication, verification, work and transport expenses.
Let kappa>0 be its one-time installation expense.

For the contractual criterion, honored continuations have zero penalty,
so the current agent ranks them by own original welfare. At a settled
cycle boundary this permits a comparison on the same scale. A different
current goal, such as 096's unequal-gain fairness criterion, requires
its actual current values rather than silently replacing them by own
material profits.

Suppose the physical state and menu genuinely renew, retaining the goal,
and that the no-update continuation value is A_n a. Suppose further
that r remains attainable, the installed current selves choose it, and
arbitrary relevant deviations have been included in these two values.
Then immediate adoption has advantage

    A_n(r-a)-kappa.                                   (1)

It is strictly optimal over permanent refusal when this is positive,
ties at zero, and loses when negative. The conclusion is about a genuine
update only when its terminal/history ordering actually changes, as in
097's supply-versus-default comparison.

The important quantity is the *advantage over the best available route*,
not gross cooperative revenue. A matched delegate at equal cost can tie;
a cheaper implementation that supplies the same r replaces the goal
option. More future output can support adoption only to the extent that
it improves this comparison.

### Delay is a real option

In the stationary renewal specialization, waiting t cycles and then
adopting has advantage over permanent refusal

    delta^t [A_(n-t)(r-a)-kappa].                      (2)

Subtracting the t+1 expression from the t expression gives

    delta^t [(r-a)-(1-delta)kappa].                    (3)

If (1) is positive, then r-a>kappa/A_n>=(1-delta)kappa,
so every additional delay strictly lowers the advantage. Immediate
adoption is therefore optimal over every delayed installation in this
specified stationary comparison. If (1) is negative, no delayed
installation can be positive: A_(n-t)<=A_n. At equality, immediate
adoption and refusal tie, with delays checked by (3).

This proof assumes history-independent renewed opportunities and the
stated no-update value. Reputational policies, an anticipated future
goal change that supports earlier trade, changing installation prices,
resource depletion or new customers can alter a. They must be included
before using (1) as a complete initial-game theorem. The result does not
discard them by calling all unchanged-goal behavior uncooperative.

## 2. Why another customer can change the adoption decision

Let r_j be the actual current-goal value of an implemented arrangement
with available customer j, net of recurring expenses. If partners accept
the proposed terms and capacity permits only one, then r=max_j r_j.
Changing an available customer can improve r, improve the no-update
alternative a, or do both. For a target whose advantage is Delta,
adoption requires A_n Delta>kappa. A newly available ordinary partner
raising a by d reduces the advantage by A_n d; a new goal-enabled
partner raising r by d increases it by the same amount, other options
held fixed. These are explicit conditional effects, not a claim that
adding agents always has one sign.

In 096's local example, b=3,c=1,p=3/2 yields own profit 1/2 but needs a
change from beta=3/10 to beta'=2/5 to make delivery credible. An alternative
customer with b=3,c=1/2,p=9/10 gives own profit 2/5 and already satisfies
the old goal's delivery threshold. Both outcomes leave the supplier
behind, so the old alpha=0 goal assigns their own-profit values. With
these actual offers and no better method, updating for the first customer
requires k<A_n/10; without the second offer, the boundary is k<A_n/2.
Richer post-payment renegotiation defeats the simple fairness mechanism
unless repaired as in 097. The numerical comparison is an opportunity
and current-goal calculation, not that missing full-game proof.

### Searching for the opportunity is an intervention

Suppose an agent can pay sigma to search. With known probability q it
finds a willing partner providing implemented advantage Delta; otherwise
the old option remains. Suppose the search result is observed before
paying kappa. Then the net current-goal value of search is

    q max(A_n Delta-kappa,0)-sigma.                   (4)

Positive value makes searching privately worthwhile in this search game.
If A_n Delta>kappa and search is selected, actual adoption occurs with
probability q. Increasing q or lowering sigma can therefore make a
physically available search-and-change intervention selected, with the
other payoffs and implementation held fixed. An exogenous favorable
customer parameter alone establishes neither that action nor its cost.

Equation (4) assumes the discovered partner actually consents, the search
has the stated information and funding, and failure does not alter the
old opportunity. A harmful exposure during search, a rival bid, a cheaper
ordinary contract or a search method improving combat as well changes
the calculation. Those are comparisons to investigate, not universal
obstructions to the positive region of (4).

## 3. A voluntary assignment certificate

Consider finite provider set I and customer set J. Each can take at most
one partnership for a declared N-cycle contract. For edge (i,j), let
v_ij^m be the total **attainable original welfare above both outside
options**, using implementation m, after all setup and recurring costs.
m can be a genuine goal, an ordinary contract/delegate or another
physically available route. Define

    v_ij=max(0,max_m v_ij^m).                          (5)

For this subsection impose the following interface, rather than silently
assuming it:

* Every proposed edge is implemented by its specified current-self
  continuation, including genuine changes where selected.
* Money/physical value can be transferred so the relevant nonnegative
  surplus splits are actually funded. Restricted liquidity from 098
  must be checked separately.
* An agent's outside option is genuinely available. There are no omitted
  cross-pair attack or production externalities.
* Costs are edge-additive, with one installation per chosen provider and
  no sharing of that installation across multiple simultaneous edges.
* On honored contracts the installed goals agree with original own-welfare
  comparisons. Existing obligations must be fulfilled or validly settled
  before a different match can be used as an alternative.

Let M be a matching and assign nonnegative gains u_i to providers and
w_j to customers. The following readily checked conditions certify
voluntary individual participation and resistance to all profitable
coalitions within this interface:

    u_i+w_j >= v_ij                 for every edge,
    u_i+w_j = v_ij                 on chosen edges,
    u_i=0 or w_j=0 respectively    for unmatched agents.       (6)

**Proof.** For any alternative matching available to a coalition, sum the
first inequality over its disjoint edges. The resulting productive value
is no larger than the sum of the participating agents' current gains;
unmatched coalition members have nonnegative gains too. Thus the
coalition cannot make everyone weakly better off and someone strictly
better off using only its attainable edge surplus. The chosen matching
distributes exactly its value by the second and third conditions. Each
agent gets at least its outside option because its gain is nonnegative.
QED.

This is the standard assignment-game/dual certificate. Shapley and
Shubik's *The Assignment Game I: The Core*, journal scan pp. 117-118,
Theorem 2, supplies the classical LP characterization under its money
transfer assumptions. Its section 5.2 also explicitly distinguishes
core stability from a bargaining theory. The source is not a theorem
about utility self-modification, combat, launch costs or constrained
payment timing; those are the interface obligations above.

When an optimal chosen edge has a genuine-goal implementation attaining
(5), it can carry that implementation in this certificate. An equally
priced delegate can tie without erasing the chosen-goal outcome. If a
strictly cheaper available ordinary method achieves the same physical
continuation, (5) selects that cheaper method instead. Thus the matching
comparison preserves both routes and assigns the goal its actual level
of support.

## 4. An exact two-by-two assignment to check

Let the net edge values, already including goal implementation and outside
options, be

    [[6,4],
     [3,5]].

Choose the diagonal and gains u=(3,2), w=(3,3). The chosen sums are 6
and 5, while the cross sums are 6>=4 and 5>=3. Equation (6) holds with
strict cross-pair slack and positive individual gains. This is a stable
voluntary assignment in the declared transferable-surplus interface.
If those four chosen payoffs are implemented and funded, originals can
consent to genuine goal installation and counterparties simultaneously
have a reason to participate. It is not a claim that a cheap-talk market
automatically discovers these particular prices.

Renewal can make an edge with larger flow surplus but a higher one-time
goal cost replace a cheaper initial alternative: compare
A_n s_ij-kappa_i against the relevant alternative edge/method. Actual
partner changes depend on the whole matrix and the feasible splits, not
only on that edge's standalone return. A new high-value ordinary edge
can instead displace a goal edge while increasing total welfare. The
number of installed goals is not itself the welfare criterion.

## 5. Launch, funding and broader scope

An agreed split is not a free enforceable launch. A producer can prepare
and activate a recognized goal before a customer exposes its advance;
the customer then checks the active criterion and accepted terms. If
customers finance installation, a conditional deposit can release funds
on actual activation and refund them on abort. That is an additional
commitment technology with real costs. The same technology must be
offered to ordinary controls; free selective escrow is not assumed.
The installed goal must cover the funding customer's promised outcome,
or it could collect the setup subsidy and abandon the service.

Staged fees, abort opportunities, attack during implementation, honest
recognition and later renegotiation remain part of the required execution
check. Pairwise/core stability concerns the attainable agreement space;
it does not settle coalitional coercion, collusive withdrawal, arbitrary
group production or population prevalence. Fixed template counts are
not a model of lifelong innovation. These limits preserve a usable
conditional positive result while identifying the repairs and stronger
implementations still required for a broader one.
