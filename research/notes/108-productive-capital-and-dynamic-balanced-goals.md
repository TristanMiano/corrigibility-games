# Productive capital, changing partners and dynamic balanced goals

**R0005 extension and proof audit.** The independent fresh-supply workshops
are one renewable environment. Here investment changes future productive
capacity. The result supplies a continuation certificate for genuine goals,
an exact capital example and adoption comparisons. Initial staged launch,
actual ordinary alternatives and membership changes remain distinct choices.

## 1. A flow goal can align productive investment without freezing code

There are n>=2 consenting participants, positive negotiated weights gamma_i
with sum gamma_i=1, and a finite sequence of dated consumption vectors x_t.
All outputs, losses and real expenses in the collaboration are included in
these net vectors. Any fixed outside reference is declared separately.
Original i values E sum_t delta^t x_it. Consider the successor criterion

    G_i = E sum_t delta^t g_i(x_t),
    g_i(x) = (1-beta_i)x_i
              + beta_i gamma_i min_j(x_j/gamma_j),
    1-gamma_i <= beta_i < 1.                         (1)

This is the flow version of 107, not its lifetime-wealth or expectation-only
version. It is increasing in own output, weakly increasing in others' output
and concave. It values relative collaboration gains; it assigns no value to
retaining a particular program. Its genuine preference reversals are those
in 107, applied at a single date with other dates held fixed.

For every realized vector, with S=sum_j x_j,

    g_i(x) <= gamma_i S.                            (2)

To prove this, put z_j=x_j/gamma_j. If z_i<=S, the minimum is at most z_i,
so g_i<=gamma_i z_i<=gamma_i S. If z_i>S, the weighted average of the
other z's is at most (S-gamma_i z_i)/(1-gamma_i). Substituting this upper
bound on their minimum into (1) gives

    g_i-gamma_i S
       <= gamma_i[1-beta_i/(1-gamma_i)](z_i-S)<=0.

For beta_i>1-gamma_i, equality in (2) requires x_j=gamma_j S for every j.
At the boundary beta_i=1-gamma_i, some unequal vectors can tie.

Let V(s) be the maximum expected discounted total output attainable from
the actual physical state s, including all available investment, recovery,
trade, combat and ordinary-control technologies. If an executable plan P
attains V(s) and divides each realized date's net output in the proportions
gamma, then

    G_i(P)=gamma_i V(s) >= G_i(L)                    (3)

for every physically attainable continuation law L. This includes laws
implemented by another future utility. Current-goal evaluation therefore
approves no strictly better revision away from P. With strict beta thresholds,
an indifferent revision can attain the same value only by preserving dated
balance almost surely and maximum expected total production. It cannot
improve one current participant by reducing another within this same class.

This is an outcome comparison, not an assumption that descendants continue
to maximize founder utility. A changed successor would use its actual new
goal; its predecessor evaluates the resulting law using (1).

### Sequential implementation at an attained common maximum

For a finite perfect-information continuation game with fixed installed
criteria, suppose a physically feasible path attains every player's global
maximum as above. There exists a subgame-perfect profile following that
path. Complete each off-path subgame with a backward-induction equilibrium;
at each on-path decision, following the path yields that mover's maximum
over every terminal history, so deviation cannot improve it. The same
argument applies at later on-path installation decisions when they are
evaluated by the then-current criterion and their actual continuation law.

This elementary existence statement uses a finite game, including a finite
physical implementation of investment/allocation, or separately justified
equilibrium existence for continuous menus. It does not assert that every
equilibrium selects the productive path. A continuous optimum calculated
below is an opportunity/continuation bound; a grid containing its exact
optimal actions supplies a finite instance. It is not used to replace the
divisible transfers required in 105's different ordinary-trade theorem.

An on-path history fixes earlier dated outcomes. If the remaining productive
plan still attains its conditional total frontier and dated balance, (3)
applies to the remaining horizon. Attack remains available: it loses when
its actual resulting productive law falls below that frontier. No external
last-resort rule or infinite combat cost is imposed.

## 2. An explicit renewable-capital technology

Let k>=0 be usable productive equipment. During a period, f(k)=A sqrt(k)
units of raw input can be processed. Output can be consumed or invested:

    sum_i x_i + z <= A sqrt(k),
    k_next=(1-d)k+eta z,
    0<=z<=A sqrt(k),  0<eta<=1, 0<=d<=1.             (4)

This is a reduced plant technology with explicit material destinations.
The raw feedstock and process energy enter from a declared external stream;
the finite-horizon stream bounds exceed the displayed feasible processing
quantities. Process work becomes heat. Invested material produces eta z
equipment and (1-eta)z spent material; worn d k enters the worn/spent account.
Consumption leaves the active plant as delivered project output. It is not
recreated next period. The square-root rate represents a capacity bottleneck,
not a law equating energy, thermodynamic entropy or utility. Recovery and
repair routes capable of improving (4) must be included in f and the state;
the exact instance specifies no faster profitable route before its deadlines.

Over two dates, total discounted output is

    V_2(k)=max_z [A sqrt(k)-z
                   +delta A sqrt((1-d)k+eta z)].    (5)

Concavity gives the exact investment rule

    z* = clip(((delta A eta/2)^2-(1-d)k)/eta,
              0, A sqrt(k)).                       (6)

At an interior optimum,

    V_2(k)=A sqrt(k)+(1-d)k/eta+delta^2 A^2 eta/4.  (7)

Thus a longer-valued future (larger delta), better conversion eta, and more
productive future operation can increase chosen investment in their relevant
interior regions. Each change also alters actual combat and ordinary options;
the implication here concerns the efficient productive plan, not automatic
adoption. For more periods the same state has the Bellman equation

    V_n(k)=max_{0<=z<=f(k)} [f(k)-z
                         +delta V_(n-1)((1-d)k+eta z)],
    V_0=0.                                         (8)

The goal certificate (3) applies to any n for which the balanced efficient
plan is physically executable; linearity of V_n is unnecessary.

## 3. A destructive contest and a strict consent interval

Take A=4, delta=3/4, d=1/2, eta=1 and initial k=1. Equations (6)-(7) give

    z*=7/4,    consumption dates=(9/4,6),
    V_2(1)=27/4.                                   (9)

For comparison, a contest spends each side's finite combat consumable and
leaves usable equipment k/3 plus dispersed equipment 2k/3. Portable recovery
work can restore at most k/9 before the production deadline, one unit of
work per restored unit. Full recovery of that allowed amount is optimal;
the remaining 5k/9 stays dispersed. The batteries and processing stream are
distinct specified resources, not free conversion of unavailable work. The
winner's remaining usable capital is therefore 4k/9. Strength gives winner
probabilities p_i=s_i/sum_j s_j in this two-agent contest; the loser lacks
the plant actuator for this horizon. Its surviving outside controller can
act again only if a later replacement process is supplied.

At k=4/9 the optimal investment is 73/36, first consumption 23/36 and
second consumption 6. The winner's attainable discounted plant output is

    Y=V_2(4/9)=185/36 < 27/4.                       (10)

Let c_i be i's own dated-output opportunity cost of using its preloaded
combat consumable, measured relative to retaining it. The original duel
value is d_i=p_i Y-c_i. Let K_i be the actual one-time setup expense of
the implemented goal package, evaluated under the original criterion.
Setup must preserve the stated capital, deadline and disagreement values
or those values must be recomputed. A negotiated share gamma_i gives
strict original consent relative to this duel exactly when

    gamma_i V_2(1)-K_i > p_i Y-c_i.                 (11)

For two parties, a strictly acceptable interval of shares exists when

    V_2(1) > Y + K_1+K_2-c_1-c_2,                 (12)

provided positive shares and the actual payment/funding constraints can be
met. With c_i=K_i=1/20, the interval for the first share is

    (185/243)p < gamma_1
         < 1-(185/243)(1-p).                       (13)

Its width is 58/243. Equal shares work for 127/370<p<243/370.
At p=3/5 both originals strictly prefer the installed productive allocation
to the duel. At p=4/5 equal shares give the stronger original too little;
gamma_1=7/10 repairs consent. For those weights, beta_1=1/2 and beta_2=4/5
strictly satisfy (1). Negotiating the goal's weights, rather than requiring
an equal split regardless of strength, matters to the constructive region.

The intervals compare genuine adoption with the stated duel. An ordinary
controller or fixed-utility arrangement implementing the same investment
and allocation must be compared at its actual cost. If cheaper, it displaces
this adoption; if equally costly, genuine change remains an optimal route.
A full launch or adoption equilibrium is conditional on the actual selection,
verification, staged-cost and counteroffer game. The continuation certificate
does not supply those missing physical actions.

## 4. New partners and productive expansion

Suppose an old group already attains total continuation value V_old with
weights gamma and goals (1). A new willing partner and a changed production
plan can attain V_new after all real new expenses. If each date's old-member
net gains remain proportional to gamma, and the newcomer receives fraction
theta in (0,1), the old group evaluates the new plan as

    G_i(new)=gamma_i(1-theta)V_new.

Each old member strictly approves the implemented expansion when

    (1-theta)V_new>V_old.                           (14)

The newcomer must also beat its actual outside option and fund its share of
setup. With a zero incremental outside reference already charged in V_new,
there is a positive admissible theta precisely when V_new>V_old. With an
unfunded required newcomer increment r, the interval instead requires
V_new>V_old+r and r/V_new<theta<1-V_old/V_new.

The old criteria evaluate the expansion before any rewrite. A successor
criterion including the new partner in its minimum is a genuine further
change over outcomes where that partner's welfare varies. Complementary
skills, added capital, cheaper operation or additional input access can
increase V_new; congestion, entry costs or a stronger outside option can
close (14). The physical production change and the newcomer's willingness
must be supplied. A new name on a partner list is not additional surplus.

## 5. Balance costs and uncertainty are consequential scope conditions

The maximum certificate needs an efficient plan that can actually deliver
dated proportional gains. It is stronger than equal expected receipts.
For two equal-share agents with beta=3/4, a fair lottery over (2,0),(0,2)
has original expected own output 1 but expected installed score 1/4.
A balanced delivery (1,1) has score 1. If making that balanced delivery
costs h total output, its score is 1-h/2 and it beats the lottery for h<3/2.
The original evaluates the actual reduced own output 1-h/2 at installation;
the successor's taste for balance cannot be counted as an original benefit.

When costly balancing reduces the attainable total, a balanced plan may
fail to attain the upper bound in (3); its optimality requires a new
comparison. State-contingent delivery, insurance, cheaper verification or
different negotiated goals are constructive repairs to test. Uninsurable
idiosyncratic production is a meaningful limiting environment. Common
productivity risk is harmless to (3) if every realized total can be shared
in the agreed proportions with its actual costs included.

Naturality and design are separate here. Concave production, depreciation,
finite recovery work and valuable future capital have independent physical
motivations. The weighted minimum and exact dated allocation are designed
conditions. Parties have a current-goal reason to pay for them under (11)
and the actual control comparison, but reliable activation and cheap risk
sharing are substantive technologies. This is a constructive continuation
and bargaining region, not a population-prevalence result or a completed
theory of membership bargaining with hostile outsiders.

## 6. Patience and reconstruction change both sides of the comparison

Suppose peaceful and post-combat capital k and chi k both have interior
investment optima. Put J=delta^2 A^2 eta/4. Then

    V=A sqrt(k)+(1-d)k/eta+J,
    Y=A sqrt(chi k)+(1-d)chi k/eta+J.               (15)

Increasing patience raises both frontiers by the same marginal amount.
For a fixed share gamma_i, victory probability p_i and costs, the original
adoption margin m_i=gamma_i V-p_i Y-K_i+c_i satisfies

    dm_i/ddelta=(gamma_i-p_i) delta A^2 eta/2.       (16)

Consequently more patience favors this offered change for gamma_i>p_i,
and favors rejecting this offered change for gamma_i<p_i. This is a
comparison with the stated duel, not an assertion that rejecting the offer
selects combat when ordinary peace or a different quote is available.

In the numerical technology, both optima are interior for
1/(2 sqrt(2))<delta<sqrt(26)/6. There

    V=9/2+4 delta^2,   Y=26/9+4 delta^2,
    V-Y=29/18.                                     (17)

Take p=7/10, equal shares and K_i=c_i. The stronger party's margin is
41/180-(4/5)delta^2. It is positive at delta=1/2 and negative at delta=3/4;
the boundary is delta=sqrt(41)/12. The total gain from avoiding the duel
remains 29/18. At delta=3/4, changing its negotiated share to 3/5 restores
strict consent for both originals. Thus a flexible agreement uses the
available joint gain even when a fixed equal-share proposal loses consent.

In the same interior region,

    V-Y=A(sqrt(k)-sqrt(chi k))+(1-d)(1-chi)k/eta.   (18)

Increasing reconstruction efficiency eta reduces the second term. It raises
the two productive values but lets the damaged winner rebuild more cheaply,
reducing the total advantage of avoiding damage. Reducing chi at fixed
peaceful technology instead raises the avoided-loss advantage. If changing
chi also consumes productive resources, alters attainable recovery, invites
preemption or changes strength, those effects must enter V, Y and the game.
Equation (18) alone supplies a parameter effect, not a chosen defense device.

The stationary renewal result in 099 remains valid under its fixed per-cycle
advantage. Equations (16)-(18) identify a different environment where the
same improvement changes disagreement and investment together. Better
ordinary reputation at higher patience can also divert gains to unchanged
goals (095). These three effects must be compared under the actual menu.
