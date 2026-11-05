# Capped defensive reservations and mixed combat offers

R0006 final agreement-space check. Note 133's calibrated additive attack
bonus protects accepted purely peaceful offers and, with a stronger beta,
deters the specified combat-production controllers. A lottery combining
peace and attack is a different offer. This note constructs that deviation
and a finite, statewise preference repair. All proofs are self-reviewed.

## 1. A real mixed offer can exploit the additive calibration

Use R=5, J=1, p=4/5, delta=99/100, epsilon=1/4 and beta=3 in note 133.
Then the calibrated goal is q_R off the Blue-attack branch and
`M+q_R-3q_B` on that branch, with M=366/25=14.64.
The remaining total native stock is nine. Give Blue a publicly recognized
controller that actually executes the following offered lottery:

* With probability 4/5 there is peace and all nine clips are Blue.
* With probability 1/5 Blue really initiates combat. If it wins, its
  committed production criterion makes all recovered clips Red.

This requires an actual randomization/attack/production commitment, not
a verbal promise. Red can still disable its own stock after an attack.
On that branch both possible winners produce Red; its current additive
goal therefore makes preserving the entire stock strictly optimal.
Actual recovery yields 8.91 Red clips. Expected current Red value from
the mixed offer is `(14.64+8.91)/5=4.71`, exceeding native production four.
Expected original Blue output is `9(4/5)=7.2`, exceeding native five and
the best pure peaceful offer leaving Red at least 3.75. Founder Red output
is only 1.782. Small sufficiently funded implementation expenses preserve
these strict inequalities; their effect on stocks must be included.

The lottery performs a genuinely damaging battle with positive probability.
It is not a forged history label. The example shows why the original
additive calibration's deterministic counteroffer scope was consequential.
A high conditional attack value can subsidize an accepted lottery with
very poor peaceful original output. This is one unilateral counter-design
against one defensive goal, not a general obstruction to chosen safeguards.

## 2. A finite statewise cap supplies a stronger safeguard

Let Blue's fixed native stock be r>0 and Red's post-installation stock be
m>0. Write `V=m-epsilon>0`. As before, a battle leaves fraction delta,
Blue wins with fixed probability p in (0,1), and Red can choose remaining
stock `S in [r,r+m]` by disabling its own material after Blue launches.
Replace the defensive criterion by the fixed terminal-history utility

`U_R=q_R`, if Blue has not initiated attack;
`U_R=min{V, V+beta delta r+q_R-beta q_B}`, if it has.     (1)

Here beta>0 is finite. This is a finite utility on the compact physical
outcome set. Its expected utility is **the expectation of the statewise
minimum**, not the minimum of expected values. Reliable event attribution,
resource calibration and genuine installation are actual premises. Its
full preparation expense belongs in the original J or the stated budget m.

Full disabling gives S=r and ensures q_B<=delta r at every realized
outcome. Therefore it guarantees U_R=V pointwise. No attacked outcome has
U_R>V. Optimal current Red consequently obtains expected utility V, and
any outcome with positive probability under its chosen response must
satisfy

`q_R-beta q_B >= -beta delta r`.                       (2)

Against an original all-Blue winner, expected attacked value at S is
`V-p beta delta(S-r)`, strictly maximized by full disabling. Thus this
criterion is a genuine change of ordering: original Red would preserve
its material after the attack, while the installed goal destroys it.

For any feasible Blue-victory production policy, including random
allocations, (2) and q_B+q_R<=delta S imply

`q_B <= delta r+delta(S-r)/(1+beta)`.

Hence original Blue's conditional expected combat output is at most

`B_max=p delta r+p delta m/(1+beta)`.                   (3)

This proof uses pointwise feasibility and the statewise cap. Red-winning
production gives Blue zero because the acting defensive criterion can
maximize at all-Red production; select that current-optimal continuation.
A different tie-selected Red-victory production giving Blue clips must
be included in (3). The following stronger bound removes that selection
requirement rather than silently imposing an own-color tie-breaker.

Consequently `beta>p delta m/[r(1-p delta)]-1`, together with beta>0,
makes B_max<r in this selected continuation. For the earlier stocks
r=5,m=4, beta=3 gives B_max=594/125=4.752<5. All expenses and strengths
remain finite. A matched automatic controller can provide the same
defensive continuation at its actual cost.

Indeed (2) holds at every realized outcome, whichever party wins, because
Red attains its pointwise upper bound V in expectation. Thus **every**
optimal capped-goal response, including any victory-allocation ties, gives

`E q_B <= B_any=delta r+delta m/(1+beta)`.               (6)

For delta<1 the finite stronger condition
`beta>delta m/[r(1-delta)]-1` makes B_any<r. In the fixture this threshold
is 391/5=78.2; beta=80 gives `B_any=4499/900<5`. This covers random
production and mixed disabling choices too: the statewise cap and the
available pointwise guarantee force (2) almost surely. The larger weight
is a substantial design requirement. Finite war destruction matters to
this selection-independent version; as delta approaches one, its required
weight grows without bound.

## 3. Peaceful offers dominate mixed ones in the specified offer class

Consider an offer class with fixed stocks r,m and no further physical
opportunities. All implementation expense is already included in those
stocks, or a mixed offer costs at least its corresponding pure peaceful
offer. Actual controllers can execute feasible allocations and lotteries.
Red can reject for at least V under (1), and accepts at equality.

For any accepted mixed offer, attacked utility is at most V. Therefore,
if its probability of peace is positive,

`E[q_R | peace] >= V`.                                (4)

This follows directly by conditioning its expected-utility participation
inequality on peace and attack. The peaceful total cannot exceed r+m,
so conditional Blue output is at most `r+m-V=r+epsilon`. The conditional
attack bound is B_max under its stated victory selection, or B_any under
the stronger condition (6). If that bound is below r+epsilon, every accepted offer with
positive attack probability gives Blue strictly less than the available
pure peaceful offer

`q_R=V`, `q_B=r+epsilon`.                              (5)

The pure offer is therefore optimal in this class. If rejection instead
secures a higher current value w>=V, replace (4) by its stronger bound
and leave Red w in the pure comparison; feasibility and the corresponding
attack inequality must then be checked. The theorem does not substitute
an arbitrary low reservation for an actual stronger outside option.

The cheaper-weight version's all-Red victory selection in section 2 is an
explicit implementation obligation; (6) supplies a finite alternative
covering all those ties. More generally the proof works with any verified bound on
conditional original Blue combat output below its available pure peaceful
payoff. Multiple equilibria in a capped common-value branch cannot simply
be declared to select the worst outcome for the attacker.

## 4. Initial incentives and remaining scope

With r=R and m=R-J, the original Red receives at least R-J-epsilon on
the selected peaceful path. Paying for this safeguard advances its old
own-color objective when `J+epsilon<R-2(1-p)delta R`, relative to the
specified unprotected threat benchmark. Initial Blue's best selected offer
is peaceful under the conditions above. This is a constructive repair
against mixed attack offers, with actual current-goal evaluation throughout.

The safeguard remains one unilateral genuine change, rather than two-party
accommodation. An earlier consensual common goal can still save the real
expense J, as in note 133, with the *actual* defensive fallback shares
recomputed. If those shares sum to 2R-J, a cheaper agreed implementation
with total expense below J has a strict Pareto-improving division. Matched
ordinary controllers remain substantive alternatives at their real costs.

The cap, observable attack event, fixed resource bounds, offer authority,
equality rule and either verified victory selection or the stronger weight
are designed conditions.
They establish a conditional successful repair, not general protection
against new weapons, altered strengths, hidden stocks or arbitrary
renegotiation. The useful contrast is between two actual goal designs:
an additive event bonus can reward a harmful lottery; a statewise cap plus
the verified production response makes the available pure peace offer
better for the original proposer.
