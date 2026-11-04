# Investment surplus and voluntarily chosen productive partners

**R0005 integrated productive construction.** A partner retains influence
by choosing whether and how much to invest. Genuine negotiated goals can
make efficient investment and its division optimal for both successors.
This note derives the original adoption region, the continuation proof,
renewal and partner-choice comparisons. Initial reliable, staged activation
is an explicit implementation interface, not a consequence of knowing the
utility formulas.

## 1. Physical opportunity and the ordinary continuation

An owner O controls the final output of a joint project. A partner P can
invest effort/preparation e in [0,E] at original project-output cost

    I(e)=c e^2/2,       a,c>0,   a/c<=E<2a/c.

The prepared project yields a e units of transferable output. Define

    A=a^2/c,   T(e)=a e-I(e),
    e*=a/c,   T*=A/2.                               (1)

Preparation consumes actual organized parts and positive work over positive
time. Those parts enter the installed/spent account; work becomes heat.
The final goods come from a declared raw-material stock large enough for
aE, processed through the prepared apparatus. Output is not created from
utility or from conserved energy. The convex preparation expense represents
the increasing material/work opportunity cost of preparation. The partner
must possess or obtain the inputs for I(e); its personal outside activities
cannot be treated as a free lender. Setup, inspection, transport and upkeep
are separate expenses unless explicitly included in a or c.

The owner proposes a final transfer z to P. If accepted,

    W_O=a e-z,       W_P=z-I(e).                    (2)

The contested object is this active workshop and its prepared batch. Combat
damages the specialized preparation line; repairing that line takes positive
work and longer than this project's remaining deadline. Portable recovery
can still salvage the declared fraction of already prepared output. Thus a
winner cannot silently resume investment after the fight in this instance.
The remaining raw feedstock stays in the raw ledger and has no additional
delivered-project value before the deadline. An earlier attack at e=0 is
available and spends consumables, but has no prepared output to seize. The
loser loses its current workshop actuator; off-site agency is distinct and
returns to a later workshop only through the declared renewal process.
Faster repair, useful capture of a partner's skills, or attacks on off-site
input stores require additional continuation values; they are outside this
particular one-project kernel. The same physical limits apply to ordinary
and changed-goal controls. Note 108 studies a different kernel in which the
winner can rebuild and invest, rather than treating this closure as universal.

Before final delivery both retain Attack. A contest leaves prize chi a e,
0<chi<1, after the specified material dispersion, finite recovery work and
infrastructure losses. P wins with probability p in (0,1), O with 1-p.
Each also spends a preloaded consumable whose own-project opportunity cost
is d_P>0 or d_O>0. These separate costs are not subtracted again from chi.
The constant-fraction prize is a specified scalable recovery specialization;
a fixed recovery bottleneck or changed military investment requires its
actual Y(e) instead. Neither a random winner nor remote utility is inferred
from self-knowledge. Earlier investment remains spent whichever side wins.

Thus P's post-investment combat receipt before its sunk I(e) is
p chi a e-d_P. Its nonnegative reservation transfer is

    z_F(e)=max(0,p chi a e-d_P).                     (3)

This game has O as proposer. Acceptance at exact reservation is a stated
tie selection. Other bargaining rules can give a different share and are
not ruled out by rationality. O prefers this peaceful division to its own
duel: the retained output is at least (1-p)chi a e-d_O, with a strict
avoided-loss margin for e>0. Ordinary peace is therefore already present.

Put theta=p chi. If d_P<theta^2 A/2, P's best unmodified investment is

    e_F=theta a/c,
    U_P^F=theta^2 A/2-d_P,
    U_O^F=theta(1-theta)A+d_P.                      (4)

Proof: on the positive-transfer branch, P maximizes
theta a e-d_P-c e^2/2; its maximizer is e_F and its value is positive by
the displayed condition. On the zero-transfer branch every positive
investment loses and e=0 gives zero. The stated e_F is within capacity.

The resulting total is T(e_F)=A(theta-theta^2/2), below T*. Anticipating
the later division reduces P's return to preparation. This is a standard
relationship-specific-investment mechanism in a specified contest-backed
bargaining game. It is not a claim that all ordinary contracts fail.

## 2. A simple gross-output goal improves investment in a restricted class

When theta<1/2, an owner criterion

    H_O(x,y)=x-beta(x-y)_+,        1/2<beta<1,        (5)

over gross project receipts chooses equal receipts after investment. Its
ranking genuinely reverses the original owner's preference for keeping
more of a fixed output. P accepts the half share because 1/2>theta, and
chooses e=a/(2c). O then receives A/4 before setup, compared with
theta(1-theta)A+d_P in (4). This is a strict original improvement when

    K_O+d_P < A(1/2-theta)^2.                      (6)

P's net investment return becomes A/8, above (4) in the same useful region.
This goal balances gross receipts, not net gains including P's preparation
expense. The distinction is deliberate. It needs less cost-specific goal
information but leaves investment below e*.

Restricting the research to constant gross shares would freeze the agreement
too early. A cost-sensitive surplus-sharing rule can reimburse productive
preparation and improve both parties' returns. A promise activated only by
one exact completion target is also inadequate: changing the target during
partial preparation can evade that promise. The next construction covers
every effort level, including partial work, under the same criterion.

## 3. Negotiated net-surplus goals implement efficient investment

Choose a negotiated owner fraction tau in (0,1). Let the net collaboration
gains W_O,W_P be the actual quantities in (2), with their real losses under
combat, disposal or other outcomes. Install the weighted-minimum goals

    G_O=(1-beta_O)W_O
                +beta_O tau min(W_O/tau,W_P/(1-tau)),
    G_P=(1-beta_P)W_P
                +beta_P(1-tau)min(W_O/tau,W_P/(1-tau)),
    1-tau<beta_O<1,       tau<beta_P<1.              (7)

The two criteria are monotone, concave and genuine changes from own-output
originals. They care about the division of net gains, including P's actual
preparation cost. They do not value permanent code identity. Their valuation
and implementation require the declared payoff scales and information about
the actual investment cost; knowing one's own utility does not supply that
information about a counterparty.

At any feasible outcome of this project,

    W_O+W_P <= T(e) <= T*.

The pointwise bound proved in 108 therefore gives

    G_O<=tau T*,          G_P<=(1-tau)T*.            (8)

Both bounds are attained by e=e* and the funded transfer

    z*=I(e*)+(1-tau)T*=A(1-tau/2).                 (9)

The output a e*=A finances z*: it lies strictly between A/2 and A.
P must still fund the earlier investment I(e*)=A/2. A later reimbursement
does not remove this initial liquidity requirement.

More generally, the same rule gives P the transfer

    z(e)=I(e)+(1-tau)T(e),                           (10)

so the net gains are tau T(e),(1-tau)T(e). Both are uniquely maximized
at e*, since T is strictly concave. Equation (10) is feasible for the
declared e range where T(e)>=0. The same goal applies at every partial
investment level; changing an effort target does not erase concern about
the other party's share of the actual resulting net gain.

### Continued choice, threats and further utility changes

At an on-path preparation checkpoint, earlier investment is sunk but the
full net outcome still includes it. If completing e* remains feasible,
the planned continuation attains both current goals' maxima over the
entire original project. An extra proposal, partial stop, transfer,
disposal, combat or later goal change can produce only a feasible outcome
law bounded by (8). Neither current goal strictly approves such a deviation.
With the strict beta thresholds, attaining its maximum requires balanced
net gains and maximum total output, so an indifferent rewrite preserves
the same expected gains for both in this class.

This also handles a later threatening utility: the incumbent evaluates
its actual consequences using (7), including the counterparty's loss.
The successor would use the new criterion if installed. The proof does
not silently require it to maximize the founder's utility.

For a finite physical implementation whose action grid includes e* and
z*, the common-maximum argument in 108 gives a selected subgame-perfect
continuation with efficient investment and peaceful delivery. For continuous
menus, the maximization bound remains exact; any stronger equilibrium
existence/selection claim needs its specified implementation. New productive
technology, outside partners while obligations remain unpaid, or an attacker
able to obtain additional outside resources can enlarge the feasible frontier
and must be assessed rather than excluded by the phrase "genuine goal."

## 4. Both originals can pay for the genuine changes

Let K_O,K_P be the actual setup expenses of the implemented package. Comparing
with the ordinary continuation (4), both originals strictly prefer adoption
when

    tau T*-K_O > theta(1-theta)A+d_P,
    (1-tau)T*-K_P > theta^2 A/2-d_P.                (11)

These setup expenses occur before the project and are charged once to the
original decision maker. The successor's project reference in (7) uses (2),
with setup already sunk, rather than silently redistributing past setup
costs through its net-gain rule. Later revisions still incur their actual
new expenses; the incumbent evaluates those expenses with its current goal.

Equivalently,

    2theta(1-theta)+2(d_P+K_O)/A < tau
       < 1-theta^2+2(d_P-K_P)/A.                   (12)

A strictly acceptable fraction exists, subject to the physical funding and
outside-option constraints, exactly when

    K_O+K_P < A(1-theta)^2/2.                       (13)

The right side is the actual lost productive surplus from underinvestment:
T*-T(e_F). The combat-consumable term changes the bargaining distribution
in (12), but cancels from the joint gain. The full-surplus construction
works beyond theta<1/2; that restriction belonged to the gross-half-share
repair. A high theta leaves less underinvestment to repair and shrinks
(13). An already efficient ordinary arrangement leaves no such incremental
gain; its costs and other benefits determine the actual comparison.

### Exact example

Take a=2,c=1,E=3, chi=4/5,p=1/4, d_O=d_P=1/50. Then A=4,theta=1/5.
Ordinary play invests e_F=2/5 and gives

    (U_O^F,U_P^F)=(33/50,3/50),  total=18/25.

With tau=1/2,beta_O=beta_P=3/4, the implemented changed goals choose
e*=2 and transfer z*=3 from output 4. P's preparation cost is 2, so both
net gains before setup are 1. If K_O=K_P=1/10, original net receipts are
(9/10,9/10), strictly above the ordinary pair. Both installations are real
preference changes: at e*=2 an original O would prefer the reservation
transfer 39/50 and keep 161/50, whereas G_O scores that uneven net result
below the agreed balanced outcome. The changed P likewise reverses the
ranking of a larger own share obtained by reducing O's gain.

This is productive cooperation in addition to ordinary peace: combat
occurs on neither selected equilibrium path. The threat shapes the ordinary
division and investment incentive. Genuine accommodation raises production
and both originals' welfare in the stated implemented comparison.

## 5. Matched controls, renewal and voluntary partner choice

An enforceable net-surplus contract or appropriately controlled delegate
can implement (10) without changing terminal utility. Compare its actual
authority, investment-cost information, setup, recurring verification and
stability costs with those of (7). At equal performance and equal cost,
both are optimal implementations; the genuine changes remain substantive
voluntary accommodation. A cheaper ordinary method displaces them. Perfect
cost enforcement or reliable code recognition is a separate technology,
not something supplied to only one side by terminology.

For N independent fresh projects with the same invested-input technology,
renewal requires actual new raw stocks, preparation parts, batteries and
customers. Spent material and previously delivered benefits are not reused.
If the negotiated goal rule persists, one setup expense can support many
projects. At fixed implemented per-project improvement Delta_i over the
best actual no-update route, original adoption beats retention when

    A_N Delta_i > K_i,    A_N=sum_{t=0}^{N-1}delta^t. (14)

History-dependent reputation, accumulated capital, private-type learning
and changes in military capacity must enter the actual outside value;
they are not erased by summing (4). Notes 103 and 108 treat changing
opportunities and endogenous capital separately.

At a settled boundary, let a willing potential partner j have feasible
net project frontier T_j*=a_j^2/(2c_j), required original return b_j and
setup/recurring expenses K_Oj,K_j. Let v_O be O's best actual alternative,
including other partners and unchanged-goal controls. A strictly acceptable
share interval exists precisely when

    T_j*-K_Oj-K_j > v_O+b_j,                        (15)

with tau T_j*>v_O+K_Oj and (1-tau)T_j*>b_j+K_j.
Actual funding I_j(e_j*)=T_j*, willingness, physical access and information
are additional requirements. More partners help genuine adoption when they
raise the goal-enabled return after their reservations and costs more than
they raise v_O. The optimum may instead use an ordinary controller or
decline the project.

A generic accepted-contract goal can apply (7) to a newly chosen partner
and negotiated share after previous obligations are settled. This is reuse
of one changed utility, not a fresh utility change each time a contract is
signed. Its accepted terms must remain well-defined in the evaluator across
later revisions; simply overwriting a record cannot be counted as honoring
an earlier obligation. Broader scope changes or a new net-gain criterion
are genuine further modifications and must pass the incumbent's evaluation.

## 6. Naturality, feasible interventions and remaining implementation

Specialized investment, valuable output, a party controlling the later
division and an investing partner able to choose another project are
independently motivated economic features. The exact quadratic and linear
functions make the boundary analytical; (8) extends to any attainable net
frontier with an efficiently balanced plan. The payoff-scaled goal and
reliable measurement of net investment cost are deliberate designs. No
frequency of these conditions in a population is asserted.

The candidate intervention is concrete: the parties choose the share tau,
pay for recognizable net-surplus goals or a matched ordinary controller,
and retain investment and combat choices. Their current-goal reason to
pay is (11) or the full-menu condition (15). The package needs affordable
preparation, known cost accounting, verification and reliable staged launch
before P exposes its investment. If those are supplied, (8) handles partial
preparation, later threats and further utility choices within the physical
class. If they are costly or unavailable, funding, a cheaper controller,
staged refundable preparation, another partner or a different goal are
repairs to test. Restricted early activation promises were replaced by
the all-effort net-surplus rule; the remaining initial activation interface
has not been promoted to a general solved bargaining game.

## 7. A previously changed owner can approve a further genuine revision

Suppose O already uses the gross-output goal (5), P still values its own
net return, and the current implemented project has e=a/(2c). O's current
score is A/4, and P's original net return is A/8. Now negotiate the net-gain
goals (7), paying new costs k_O,k_P before the next project.

At efficient investment, O's gross receipt is tau A/2 and P's gross receipt
is A(1-tau/2). For 0<tau<1 the former is smaller. O's *existing* gross-output
criterion therefore evaluates the new outcome at tau A/2, without a penalty.
Both current evaluators strictly approve the new package when

    1/2+2k_O/A < tau < 3/4-2k_P/A.                 (16)

This interval is nonempty exactly when k_O+k_P<A/8. It is the actual
additional productive surplus from improving investment a/(2c) to a/c.
The criterion used to approve O's second modification is H_O, not the
original own-output utility and not the proposed net-gain utility.

For A=4,k_O=k_P=1/10, choose tau=5/8. O's existing score rises from 1
to 5/4-1/10=23/20; P's net return rises from 1/2 to 3/4-1/10=13/20.
At fixed later output, H_O would prefer equal gross receipts, while the
new criterion prefers the negotiated unequal gross receipts that compensate
preparation. This is a further genuine preference reversal. A cheaper
ordinary contract implementing the same improved arrangement remains an
available competing route when its authority can actually be supplied.

## 8. A funded advance can be a chosen repair to the investment constraint

Let P initially have B units of preparation inputs. Then e<=sqrt(2B/c),
and the implemented net-surplus goals choose

    e_G=min(a/c,sqrt(2B/c)).                         (17)

If ordinary investment has positive value and B<=theta^2 A/2, the ordinary
and changed-goal investments are limited by the same input budget. No
additional investment surplus is then available to pay positive setup costs.
In the region theta^2 A/2<B<A/2,
put u=sqrt(2B/A). The additional productive surplus over e_F is

    A(u-theta)[1-(u+theta)/2],
    dT(e_G)/dB=1/u-1>0.                            (18)

These formulas use the active ordinary-investment branch of section 1;
if its value is nonpositive, the outside comparison is instead no project.

Now suppose O can actually advance L>=0 units from its own input stock.
The principal is used in preparation and repaid from actual output; only
the real delay/opportunity expense rL, r>=0, is an additional joint cost.
Count O's advance and P's remaining investment separately in their net
gains, so neither the principal nor its repayment is counted twice. A
funded net-surplus agreement can choose L to maximize

    F(L)=T(min(a/c,sqrt(2(B+L)/c)))-rL.             (19)

At an interior optimum with r>0,

    B+L*=A/[2(1+r)^2].                              (20)

If the right side is below B, choose zero; if O's available lending stock
is insufficient, use the actual upper bound and re-evaluate the gain.
For r=0 the smallest advance attaining full investment is max(0,A/2-B).
Concavity of the productive-value function in B+L proves these choices.

Because (7) divides the resulting *net* surplus, each installed evaluator
receives a positive fraction of F(L). It prefers an affordable L* to no
advance whenever F(L*)>F(0), and the other party agrees. Keeping the advance
instead of investing gives a transfer between participants, not newly
created total surplus. When the agreed project attains the maximum of
(19), the common-maximum certificate also covers such diversion, repayment
renegotiation and later goal changes within this physical class. The actual
loan and reimbursement must be feasible sequential actions; the certificate
does not create the lender's stock or verify a hidden input cost.

For a=2,c=1,B=1/2,r=1/4, an owner with at least 39/50 available units can
choose L*=39/50. Total preparation is 32/25, effort is 8/5, productive net
value is 48/25, and the additional holding expense is 39/200. The final
net surplus is 69/40, exceeding the unfinanced 3/2 by 9/40. Equal net
sharing gives each current criterion 9/80 more. The output 16/5 funds
actual receipts 147/80 to O and 109/80 to P: subtract O's advance plus
holding cost, and P's 1/2 input, to obtain 69/80 each.

This is a feasible, beneficial post-installation intervention under declared
stocks and information, rather than an unexplained increase in B. Before
initial adoption, the same advance, collateral, retaliation or an enforceable
loan must also be tested under the ordinary menu. If they already attain
the same frontier more cheaply, they change or displace the update. The
construction establishes what the installed parties can arrange and want
to arrange; the initial choice uses the resulting full-menu values.

## 9. The mechanism extends beyond the quadratic, with a joint capability boundary

Replace a e by an increasing differentiable concave output function f(e),
and I by an increasing differentiable strictly convex preparation cost.
Assume an interior positive ordinary investment, publicly known technology,
the same contest-backed original fraction theta in (0,1), and sufficient
funding. The ordinary and efficient first-order conditions are respectively

    theta f'(e_F)=I'(e_F),       f'(e*)=I'(e*).     (21)

The monotonic derivatives imply e_F<e*. The weighted net-gain goals implement
the balanced efficient plan through the same bound G_i<=gamma_i T*, with
T*=max_e[f(e)-I(e)]. Both originals can strictly gain from a funded package
whenever their combined new expense is below T*-T(e_F), after the actual
outside options and controls are included. The quadratic supplied a closed
form, not the source of the mechanism. A capacity-bound ordinary optimum
or an already efficient ordinary commitment supplies the limiting region.

For the quadratic, increasing theta raises ordinary investment and reduces
the surplus available to finance a further change. It improves ordinary
productive cooperation while narrowing this particular adoption advantage.
Changes in output efficiency and input wealth can have a different joint
effect. Fix B,theta and vary A=a^2/c, with the ordinary project profitable.
The additional investment surplus is

    Delta(A)=A(1-theta)^2/2,                 A<=2B;
    Delta(A)=sqrt(2AB)-B-A(theta-theta^2/2), 2B<A<2B/theta^2;
    Delta(A)=0,                            A>=2B/theta^2. (22)

It increases up to

    A_peak=2B/[theta^2(2-theta)^2],
    Delta_peak=B(1-theta)^2/[theta(2-theta)],         (23)

then decreases to zero as both methods hit the same funding constraint.
To verify (23), the middle derivative is sqrt(B/(2A))-theta+theta^2/2;
it crosses zero exactly at the displayed A_peak. Output itself continues
to rise: it is the difference between the two methods that shrinks.

Thus efficiency growth expands the genuine-adoption budget in the first
region, whereas sufficiently severe common liquidity constraints eliminate
that incremental budget in the last. The funded advance in section 8 is
a candidate repair that the installed parties can choose when its net gain
is positive. Initial adoption must then be recomputed against ordinary
financing and other partners. This joint variation preserves the distinction
between more production, more ordinary cooperation and more actual utility
changes.

## 10. Known genuine goals can support truthful private-cost reporting

Suppose c is P's private cost parameter, with a known bounded type domain.
The parties know that the installed criteria are (7), evaluated using the
*actual* net gains, including P's true c. O does not observe c directly.
This is an explicit Bayesian continuation premise about preferences and
type information. Self-knowledge alone does not make it true; certification
of an arbitrary hidden program or its use of the true cost is not supplied
by this calculation. Initial deceptive goal installation remains a separate
screening problem.

Consider the selected direct continuation: P reports r, prepares e=a/r,
and the parties divide the predicted net surplus with transfer

    z_r=(a^2/r)(1-tau/2).                           (24)

At r=c, actual investment is efficient and actual net gains are balanced,
so P attains G_P=(1-tau)a^2/(2c). Any other feasible report, effort choice,
message or later goal law is bounded by the same true maximum in (8).
With strict beta thresholds and strict concavity, a report producing a
different effort or actual net division strictly loses. Thus truthful
reporting is incentive-compatible for the genuinely installed P. Given
truthful reporting, O's posterior identifies c and the intended transfer
maximizes its actual criterion as well. The finite continuation therefore
has a truthful, efficient selection when its feasible grid contains the
type-dependent optima. It is not a proof that an original unmodified P
would choose to be truthful under the same transfer rule.

Indeed, keeping original P preferences while mechanically trusting the
same report would give

    W_P(r)=a^2(1-tau/2)/r-c a^2/(2r^2).

If the type/effort domain permits it, this is maximized at
r=c/(1-tau/2)>c. The gain over truth is a^2 tau^2/(8c)>0. For
a=2,c=1,tau=1/2, reporting r=4/3 gives actual net gains (3/4,9/8),
rather than (1,1). Original P gains 1/8; its genuinely changed criterion
with beta_P=3/4 scores the false report at 27/32, below the truthful 1.
This is a constructive information-incentive distinction. An ordinary
truthful mechanism can use other transfers, verification or information
rents, which require their actual comparison rather than being omitted.

With a fixed negotiated tau, uniform strict original adoption can be checked
over the entire type domain using (11). For example, when K_P>=d_P and
the ordinary project is active for every c<=c_max, both inequalities are
tightest at c_max. The sufficient-and-necessary common-share interval under
those assumptions is (12) evaluated at A=a^2/c_max. Its positive width
requires K_O+K_P<a^2(1-theta)^2/(2c_max). A shared launch at those terms
would serve every type's original interest, but its actual staged incentives,
goal recognition and alternatives still need their own proof. Type-dependent
shares negotiated *before* installation introduce an additional reporting
problem and are not covered by this fixed-share statement.

The qualification premise is consequential. If an original P can cheaply
install a publicly recognized goal using an arbitrary *imputed* cost r,
and O treats that parameter as the true c, the original can prefer the
distorted r in (24). Recognizing genuine preference change is not sufficient
to establish that its reference cost is honest. O's beliefs and proposed
division would have to respond to that incentive. A trusted cost input,
funded cost verification, an ordinary screening contract or a goal that
uses only observable gross receipts are repairs with different costs and
performance. The full endogenous-goal-reporting game remains open.

There is an exact limit to the gross-receipt repair. If P also installs

    H_P=x_P-I(e)-beta_P(x_P-x_O)_+,   beta_P>1/2,

then every feasible post-investment allocation gives
H_P<=a e/2-I(e)<=A/8. Balanced gross receipts at e=a/(2c) attain this
maximum. This current criterion therefore favors the lower investment
over a net-gain revision that it scores below A/8, even if that revision
would benefit the original own-net-gain evaluator. A richer productive
opportunity or funded compensation can change the comparison; the known
net-gain goals in section 3 instead support efficient investment directly.
Which quantity the negotiated concern balances matters substantively.

## 11. Several investors can share net gains from complementary work

The certificate does not require one owner and one investor. Let n agents
choose efforts e_i in compact intervals, incur real costs I_i(e_i), and
jointly produce F(e). Suppose

    T(e)=F(e)-sum_i I_i(e_i)

is differentiable and strictly concave on the effort box. Suppose actual
funded output allocations can give each participant net gain gamma_i T(e),
for positive weights summing to one, at every relevant effort profile.
For example, gross receipts I_i(e_i)+gamma_i T(e) are nonnegative and sum
to F(e) when T(e)>=0. Each investor still has to fund its preparation
before reimbursement. All available hostile continuations must satisfy
their actual net-total bound, not an assumed sum that omits captured assets.

Install the n-participant goals in 108. A continuation delivering the
balanced net division makes each effort chooser maximize gamma_i T(e).
Every Nash effort profile then satisfies the coordinate first-order
optimality conditions for T on a product of intervals. Summing the
coordinate inequalities gives the joint first-order condition. Concavity
makes it sufficient for global maximization, and strict concavity gives
a unique effort profile e*. The realized-output bound also excludes a
profitable later utility change from that common maximum. This is a
continuation result conditional on the funded balanced-division subgame;
it is not uniqueness of initial goal adoption or alliance formation.

If the actual original outside/ordinary values are v_i>=0 and new expenses
are K_i>=0, weights with gamma_i T*-K_i>v_i for every original exist
exactly when

    T* > sum_i(v_i+K_i).                            (25)

This statement permits the whole negotiated weight simplex. It does not
prescribe equal shares independently of strength, input costs or alternatives.

### A smooth complementary technology

For two investors, take identical c and

    F(e_1,e_2)=2a[sqrt((epsilon+e_1)(epsilon+e_2))-epsilon],
    I_i=c e_i^2/2,  epsilon=a/c,
    0<=e_i<=3a/(2c).                                (26)

F is concave and smooth; subtracting the strictly convex costs makes T
strictly concave. Its symmetric optimum is e_1=e_2=a/c, with T*=a^2/c.
T is nonnegative throughout the box: concavity bounds it below the smallest
vertex value; the vertices give zero, positive unilateral values, and
3a^2/(4c) at the upper corner. Thus the gross reimbursement shares are
funded from actual output, while initial investment funding remains explicit.

For comparison, an ordinary *implemented* fixed-fraction return of F/2
minus own cost gives the unique effort equilibrium e_i=a/(2c). Its
potential F-2 sum_i I_i is strictly concave, so the same first-order argument
proves uniqueness. Each gets 3a^2/(8c), compared with a^2/(2c) under equal
net sharing before new expenses. New expenses below a^2/(8c) per participant
give strict original improvement relative to that benchmark. Whether the
fixed fractions are the best actual original continuation, or whether an
ordinary net-surplus controller already supplies the efficient outcome,
is an implementation comparison required by (25).

The positive baseline epsilon represents existing complementary capacity.
With exact zero baseline, F=2a sqrt(e_1 e_2) also has a zero-effort
coordination equilibrium because either agent alone produces nothing.
Positive baseline capacity and smooth strict concavity remove that particular
effort equilibrium in the stated balanced-division continuation. Goal change,
capacity, funding, partner availability and selection thus play separate
roles; increasing a parameter within this class is not a count of new
independent environments.
