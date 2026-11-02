# Late controls, usable transfers and the design of screening

**R0003 mathematical audit and repair note.** This note expands the
inspection/communication mechanism rather than treating its initial menu
as the whole agreement space. The results are conditional comparisons and
explicit bounds; they do not close the arbitrary physical-protocol audit.
Review is contributing-agent self-check.

## 1. Conditional installation changes the relevant cost bound

In 067, R's ex ante original loss is m=pv/(1-v), but its loss after an
unverified claim is v. A receiver controller costing j>=m can therefore
still be profitable if it is installed only at a claim and j<v. Charging
that controller in every state would overstate its actual cost.

For a bound independent of the particular controller, require j>=v at every
live claim. Original decision loss is nonnegative, and in the specialized-
asset baseline the controller cannot create a positive transfer to R.
Therefore paying j cannot improve on loss v. Before a claim, m<v when
p<1-v, and after a successful diagnostic the remaining decision loss is
zero. A uniform incremental cost j>=v thus covers all these on-path
installation opportunities, including authority transfers and binding
delegation if their actual costs satisfy the bound.

The same argument applies to 068's continuous-policy core: its live-claim
loss is v=z(1-z), while its initial loss p(1-z) is smaller when p<z. It does
not cover off-path histories with different current losses; those receive
an actual optimizing continuation.

A concrete alternative is **late destructive screening**. After a claim,
R could install a controller that offers a second, costly-risk acceptance
decision. A high sender accepts an appropriate combat lottery, while a low
sender declines. If it yields correct decisions, the receiver's conditional
cost is j+(1-mu)*tau*d_R, plus its actual extra messaging/implementation
costs, where mu is its current low posterior. This can be below v even when
j exceeds m. Its new response opportunity and credible lottery are real
technological requirements. It is an informative deviation, not a proof
that any announcement of future combat works.

Similarly, a commitment to check after giving a false claimant a withdrawal
opportunity can sometimes save work: once checking is certain, a low sender
is indifferent between withdrawal and an unsuccessful fresh response when
its earlier claim cost is sunk. A selected withdrawal can save the receiver
the later probe cost. The sender's earlier incentive and the actual cost of
installing that commitment must then be recomputed. Retaining the simple
core under j>=v is a sufficient region, not a claim that cheaper redesign
always produces combat or always improves cooperation.

## 2. Comparison of two chosen screening commitments

In the declared **initial** menu of 067, let the peaceful audit commitment
and the destructive screening commitment have the same actual receiver
setup cost j. The threshold probabilities are

\[
q=1-f/g,\qquad
\tau=\frac{g-f}{d_S+(1-s)g},\qquad g=2b-1.
\]

Their original receiver costs are j+p*q*v and j+p*tau*d_R. Hence peaceful
checking is cheaper precisely when

\[
                 v<\frac{g d_R}{d_S+(1-s)g}. \tag{1}
\]

The common setup cost and the claim-cost factor g-f cancel in this
pairwise boundary. At b=1,s=1/20,d_S=5,d_R=1/100 the boundary is v=1/595.
Above that value, destructive screening is the cheaper of these two
commitments for R; below it, peaceful checking is cheaper. Each must still
beat uncommitted inspection m and other actually available alternatives.
Different setup costs add their actual difference to the comparison.

The sender has a separate comparison. Under the selected truthful
continuations, peaceful checking costs it p(f+q*k), while destructive
screening costs p(f+tau*d_S), apart from common b^2. Thus its preference is
determined by q*k versus tau*d_S. In the numerical witness it strongly
prefers the peaceful mechanism even when R prefers destructive screening.
Those are two original-agent welfare coordinates, not a claim that a single
"cooperation" score settles the choice.

If a common transferable resource is actually available, an ex ante,
state-independent arrangement payment from S to R can make the more costly
peaceful receiver choice mutually acceptable
when its amount T satisfies

\[
p(qv-\tau d_R)\le T\le p(\tau d_S-qk), \tag{2}
\]

with the appropriate real differences in setup/transaction costs added.
The lower endpoint is R's additional expense; the upper is S's saved
expense. For the witness the interval is nonempty by a wide margin. This
is a constructive transfer repair to destructive screening, conditional on
an enforceable, usable transfer that does not itself change the contest
prize or get seized in the combat alternative. It is not assumed to exist
in the specialized-asset baseline. A physical escrow or payment channel
requires its own authority, timing and cost audit.

## 3. A whole class of ordinary transfer menus

To test how strongly specialized nontransferability favors the goal-based
diagnostic, enlarge 066's ordinary screening control. Allow arbitrary policy
lotteries and enforceable payments t_0,t_1 to R, selected by an unchanged
sender's reports. Set b=1,p=1/2. The receiver's money valuation and the
sender's payment cost are both one per unit of an explicitly usable common
resource; this is an additional technology, not identification of utility
with energy. Permit subsidies t_0<0 and ignore their funding/transaction
costs in the upper bound. Require only a high-report payment cap t_1<=B.

Let m_t=E[Y|t], q_t=E[Y^2|t]. Low-type incentive compatibility requires

\[
t_1-t_0\ge2(m_1-m_0)-(q_1-q_0).
\]

R's expected original loss, net of receipts, therefore obeys

\[
\begin{aligned}
L_R&=\tfrac12(q_0+q_1-2m_1+1-t_0-t_1)\\
&\ge q_0-m_0+\tfrac12-t_1\\
&\ge(m_0-\tfrac12)^2+\tfrac14-B
\ge\tfrac14-B. \tag{3}
\end{aligned}
\]

The bound includes randomized policies, arbitrary transfer differences,
and a generously funded subsidy. It does not rely on a restricted list of
offers. Positive execution costs only worsen the receiver's value. Thus
ordinary truthful report-selection menus of this class are less attractive
to R than a diagnostic costing m whenever

\[
                            B<1/4-m. \tag{4}
\]

At m=1/198, even B=1/5 leaves a strict gap 89/1980. This is a useful
robustness result: some transferable capacity can be added without
displacing the diagnostic. A protected state-report delegate is outside
(3)'s freely manipulable-report premise and remains an explicit matched
diagnostic control. Combat-containing screening lotteries are also a
different class, compared in section 2.

The bound can be sharp under suitable participation/authority conditions.
A pooled policy y=1/2 with payment B attains 1/4-B. If refusal induces action
0, both original types accept for B<3/4 (the low type's gain from 1/2 is
3/4). Whether refusal actually induces 0 and whether the payment/policy
exchange is enforceable must be checked in the expanded game. This
attainment is not used to assume a punitive outside policy for free.

## 4. Prior robustness of the ordinary-menu bound

The preceding comparison extends beyond p=1/2. Allow b>=1 and any p in
(0,1), retaining policies in [0,1], arbitrary lotteries, report payments,
and the high-report cap t_1<=B. Both type IC inequalities imply
Delta=m_1-m_0>=0. Define the nonnegative low-IC slack

\[
D=t_1-t_0-2b\Delta+(q_1-q_0)\ge0.
\]

Substitution into the receiver's actual expected loss gives

\[
L_R=2(1-p)q_0+(2p-1)q_1-2pm_0
 +2\{(1-p)b-p\}\Delta+p-t_1+(1-p)D.
\]

For p>=1/2, this equals

\[
\begin{aligned}
L_R={}&(1-p)/2-B+(B-t_1)+(1-p)D
 +2(1-p)(b-1)\Delta\\
&+2(1-p)(q_0-m_0^2)+(2p-1)(q_1-m_1^2)\\
&+2(1-p)(m_0-1/2)^2+(2p-1)(m_1-1)^2.
\end{aligned}
\]

Every term after the first is nonnegative. For p<1/2, set
a=1/[4(1-p)] and instead complete the square to get

\[
\begin{aligned}
L_R={}&p-\frac1{8(1-p)}-B+(B-t_1)+(1-p)D
 +2(1-p)(b-1)\Delta\\
&+2(1-p)(q_0-m_0^2)+(1-2p)(m_1-q_1)\\
&+(1-2p)\Delta+2(1-p)(m_0-a)^2.
\end{aligned}
\]

The support [0,1] gives q_1<=m_1, so these terms are nonnegative as well.
Consequently the entire IC class satisfies

\[
L_R\ge F(p)-B,\qquad
F(p)=\begin{cases}
p-1/[8(1-p)]&p<1/2,\\
(1-p)/2&p\ge1/2.
\end{cases} \tag{5}
\]

At p=1/2 the exact gap reduces to

\[
L_R-(1/4-B)=\tfrac12D+(b-1)\Delta
 +(q_0-m_0^2)+(m_0-1/2)^2+(B-t_1).
\]

For p in [.49,.51], F(p)>=1249/5100. With B<=1/5, ordinary
menu loss is therefore at least 229/5100, above .0449; the diagnostic
receiver loss across 068's continuous-policy box is below .005153.
This is a strict prior-robust comparison, not a balanced-prior equality.

The bound is sharp for b=1 if only the stated IC/moment/payment-cap
constraints are imposed. For p>=1/2 choose deterministic policies 1/2 and
1, payments t_1=B and t_0=B-1/4. For p<1/2 choose low-report deterministic
a, high-report Bernoulli(a), t_1=B and t_0=B+a-a^2. The two means then
coincide and both types are indifferent between the latter report bundles.
These are algebraic attainment witnesses; actual participation, funding,
payment authority and post-lottery incentives remain required for adoption.
In particular, capping only t_1 permits t_0>B in the second construction.
The lower bound generously allows that advantage to ordinary contracts.

This class consists of policy/payment menus. An additional observable burn
with unrestricted cost, a protected sensor or a combat lottery is a different
diagnostic or screening technology, already given explicit standing in 067.
No bound here removes those alternatives by relabeling them as messages.

## 5. Endpoint revelation and funding

An even simpler control separates types using policies 0 and 1. Write
g=2b-1 and h=2b+1. A high-payment difference between g and h satisfies the
two type IC inequalities. With low payment zero and high payment T in
(g,h), only high S prefers to pay relative to policy 0. Upon an actual
high payment, R chooses 1 because its posterior is high. The ordinary
payment can therefore reveal the state without a utility change, if the
payment itself is observable and usable and if combat cannot cheaply seize
additional balances. Those are consequential physical enlargements.

For a cap B<g, full endpoint revelation can instead use t_1=B and
t_0=B-g<0. Its expected receiver receipt is B-(1-p)g. Funding the low-type
subsidy and committing to deliver it are real requirements; once R knows
the low state it would otherwise prefer not to pay. The loss of receipts
is not a thermodynamic cost, and the transfer must not be counted as
destroyed output. Partial-policy menus can do better than this endpoint
construction, which is why (3) gives a broader comparison for b=1,p=1/2.

The combined implication is conditional and constructive in both directions.
Cheap, observable and enforceable ordinary transfers can supply information
or compensate a receiver for peaceful checking. Limited transferable
capacity and costly payment authority leave a region in which a genuine
goal-based diagnostic or matched truthful delegate remains attractive.
Neither result licenses a distribution-free claim about which technology
or agent type is more common.
