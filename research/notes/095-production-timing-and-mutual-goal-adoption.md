# Production timing, complementarity and mutual goal adoption

**R0005 working derivation; self-checked, not independently reviewed.**
This note extends 094's productive exchange. It isolates the action and
matching games before adding physical combat and implementation. Statements
about these subgames are not yet statements about the completed game.

## 1. The same goals produce different adoption incentives under different timing

Retain 094's b>c>0, v=b-c, B=b+c and preferences

    F_i(x)=x_i,
    G_i(x)=x_i-alpha_i(x_j-x_i)_+-beta_i(x_i-x_j)_+.

Both alpha_i>=0 and c/B<beta_i<1 are allowed. Imposing alpha_i>=beta_i
selects the familiar inequity-aversion subclass; it is not required here.
The payoffs describe project gains, not energy or a comparison of arbitrary
utility scales.

### Sequential delivery with a fair role lottery

In each episode a physical role lottery independently chooses the last
producer, with probability 1/2 for either party. The last producer observes
the first producer's action. By 094 Proposition 1, a G last producer
enables C,C; an F last producer yields D,D. The expected original gain
to each member of a pair is consequently

| Pair | Each member's gain per episode |
| --- | ---: |
| G,G | v |
| G,F | v/2 |
| F,F | 0 |

All realized productive gains on these paths are balanced, so current G
preferences assign the same values before any separately priced expenses.
Let A_N=sum(t=0,...,N-1) delta^t and let one-time adoption cost kappa be
paid by the adopter. In a fixed pair the unilateral gain from adopting
G, holding the other's type fixed, is A_N v/2-kappa. Thus

* kappa<A_N v/2 makes adoption strictly worthwhile in this specified game;
* A_N v/2<kappa<A_N v makes mutual adoption jointly beneficial to the
  originals, while each prefers to leave the other doing the adoption;
* kappa>A_N v makes even mutual adoption worse than the zero baseline.

These are initial-goal payoff comparisons, not evolutionary fitness claims.
The middle interval motivates a joint agreement or an implementation-cost
repair. It does not establish an obstruction after those repairs.

Allowing parties freely to choose the order repairs much of the lost
production: one G can always be the last producer. A technological ordering
restriction must therefore have a physical justification before the role
lottery is treated as essential. Transfers contingent on delivery, bonds,
delegates and staged exchanges can change this table as well.

### Simultaneous delivery

Now the two contributions must be chosen before either observes the other.
The physical payoff table and successor formula stay the same. A G player's
gain from C rather than D is

    beta_i B-c > 0,        when the partner chooses C;
    -c-alpha_i B < 0,      when the partner chooses D.

Hence G,G has both C,C and D,D as strict pure Nash equilibria. G,F and F,F
have the unique pure or mixed equilibrium D,D: F strictly chooses D,
and G then strictly chooses D. Calling C,C *the* outcome of G,G requires
a coordination selection. A public proposal to play C,C followed by
acceptance can support that continuation, but does not eliminate the D,D
equilibrium by itself.

For identical coefficients, the probability q of the partner cooperating
at which a G player is indifferent is

    q*=(c+alpha B)/((alpha+beta)B).

C,C has the larger basin in this two-action best-response comparison
precisely when q*<1/2, equivalently

    (beta-alpha)B>2c.                                  (1)

This is a risk-dominance calculation in the symmetric two-action game,
not a theorem about which equilibrium a population or bargaining process
selects. In the alpha>=beta subclass, D,D has the larger basin. In the
alpha=0 subclass, beta>2c/B makes the cooperative basin larger; this is a
nonempty interval because b>c. Thus choosing a successor with less concern
about being behind can improve coordination incentives while retaining
the incentive to reciprocate. Actual trust and implementation remain
separate requirements.

## 2. A monotone successor class

When alpha=0,

    G_i(x)=(1-beta_i)x_i+beta_i min(x_i,x_j).             (2)

For 0<beta_i<1 this is increasing in own output, weakly increasing in the
partner's output, concave and piecewise linear. It therefore has a simple
interpretation: value own achievement and the lower of the two achievements.
It has no direct taste for violence, code retention or a partner's type.
Its preference change is genuine by 094's deterministic-outcome reversal.

The monotonicity matters. Reducing the partner's output alone can improve
an envy-sensitive goal with alpha>0 when the agent is behind. It never
improves (2). This is a conditional claim about goal design, not an assertion
that cooperative agents in nature generally have these coefficients.

For every history, (2) is own welfare minus a nonnegative penalty. The
balanced-reference welfare-floor result of 094 applies. Current successors
can adopt further goals; they evaluate the resulting physical continuation
using their actual current criterion, not the new goal's numerical score.

## 3. Continuous effort supplies the same mechanism

To test whether the result is an artifact of binary actions, let effort
e_i lie in [0,1], with

    x_i=b e_j-(c/2)e_i^2,      b>c>0.

Here c is the marginal cost at full effort; the full-effort net gain is
w=b-c/2, not the binary exchange's v. Each inequality comparison concerns
the current episode's net gains. Their difference is

    x_i-x_j=(e_j-e_i)[b+(c/2)(e_i+e_j)].                (3)

Thus equality of gains is equivalent to equality of efforts. Below the
other's effort the own-effort derivative of G_i is

    beta_i b-(1-beta_i)c e_i;

above it the derivative is

    -alpha_i b-(1+alpha_i)c e_i < 0.

The unique best response, including the kink, is

    BR_i(e_j)=min(e_j,t_i),
    t_i=min(1,b beta_i/[c(1-beta_i)]).                  (4)

For F, t_i=0. This derivation applies also to alpha_i=0: the derivative
above e_j is negative for positive effort; at the origin the unique
maximizer is still zero. No differentiability through the kink is assumed.

**Sequential consequence.** If j moves second, either F or G moving first
chooses e_i=t_j, and j matches it. On e_i<=t_j both receive
V(e_i)=b e_i-(c/2)e_i^2, which strictly increases on [0,1]. Beyond t_j,
the first mover's own payoff and its G criterion decrease. This proves
the claim for both current preference classes.

**Simultaneous consequence.** The complete Nash-equilibrium effort set is

    e_i=e_j=e,       0<=e<=min(t_i,t_j).                (5)

Indeed, (4) implies e_i<=e_j and e_j<=e_i, hence equality, bounded by
both capacities; every such common effort is a best-response pair.
The Pareto-best member for both current goals uses e=min(t_i,t_j).
It still requires a coordination selection. If either party is F, zero
effort is the unique equilibrium. Simultaneous productive reliability is
therefore complementary; sequential random-role reliability is additive.

This distinction uses the same family of goals, technology and continuous
actions. It explains why extra future production can support mutual
adoption in one timing environment and leave a free-rider problem in
another. It also identifies an available repair: changing delivery timing
may substitute for changing both goals, if its physical cost is affordable.

## 4. Voluntary partner choice under selected productive coordination

For this section only, suppose there are 2m agents, all available for
bilateral partnerships, an exit payoff of zero, publicly recognized
preferences, and no search/transport expense yet. A pair must be accepted
by both members. Use the selected Pareto-best simultaneous continuation
from (5), with pair gain

    A_N V(min(t_i,t_j))                                (6)

to each. In the binary full-reliability specialization this is A_N v for
G,G and zero otherwise. No utility bonus for a partner's label is added.
The preference for a reliable partner follows from productive outcomes.

With no side payments, sorting capacities from highest to lowest and
pairing adjacent agents is pairwise stable. A proposed pair not already
matched must include someone whose existing partner has at least as high
a capacity as the proposed partner; that member cannot strictly gain.
Ties give weak alternatives, so neither uniqueness nor a decentralized
search process is established.

The same adjacent pairing maximizes total selected output. For ordered
a>=b>=c>=d, its two-pair value V(b)+V(d) weakly exceeds the crossed value
V(c)+V(d) and the outer-inner value V(d)+V(c). Repeated uncrossing proves
the finite statement. Total output is twice this sum. The argument uses
monotonicity of V and min-complementarity, not a general matching theorem.

**Transfer-robust binary exclusion, with its scope.** An existing G,G
pair obtains positive balanced gain z=A_N v each. A G,F pairing whose
actual production remains zero cannot make G as well off while leaving
the F party nonnegative by merely reallocating that zero surplus. More
generally, G's zero-penalty fallback z and 094's welfare-floor inequality
require its own expected material payoff at least z. This cannot be
financed by an F with no positive outside subsidy in a zero-total pair.
Binding performance payments that make F cooperate change the production
frontier, and are not covered by this exclusion. Neither are a subsidy
from a third party, group production, or a new delegate. Those are serious
controls or repairs to be priced in the completed model.

## 5. Initial adoption and the coordination obligation

Take the binary simultaneous specialization, publicly observed adoption,
cost kappa paid once, enough partners, and the selected positive G,G
continuation. This initial binary adoption subgame holds the selected
criterion fixed over its N-episode payoff comparison; it is not the full
later-revision game. Notes 099/103 explicitly admit delayed installation,
and 097/102/107 give continuation goals with broader revision checks.
Initially every founder has F. If 0<kappa<A_N v, an all-G
profile with productive matching is a strict equilibrium of the initial
adoption game: one founder reverting to F saves kappa but loses A_N v.
The remaining G agents can re-match or leave one unmatched; none can
profitably produce with F under the specified action subgame.

The all-F profile is also an adoption equilibrium: one costly G adopter
has no productive partner. Yet a pair of F founders can both improve by
jointly adopting G and choosing each other. These conclusions distinguish
individual equilibrium, a mutually beneficial proposal, and coalition
deviation. They do not turn a favorable equilibrium into a prevalence claim.

Sequential implementation can resolve this particular adoption coordination
problem conditional on productive coordination and transparent updates.
After the first founder's completed adoption, the second founder compares
zero with A_N v-kappa>0, so it wants to complete its own adoption. Knowing
this, the first founder also prefers the package. The argument needs all
of the following in the full game: the installed goal's response during
the unfinished interval; physical control and attack; the actual duration
and price of each installation; reliable recognition; exit and alternative
partner access; and competing ordinary contracts. An instantaneous
two-party atomic update is not assumed by this argument.

For nonidentical costs kappa_i, the same inequalities apply individually.
Funded agreed cost sharing can repair an asymmetric participation failure
when total net surplus is positive; its execution and effect on the chosen
goal's reference domain must be checked rather than treated as free.

## 6. Boundaries carried forward

The constructive target is a chosen, productive, mutually acceptable
successor package, with later revision still available. This note identifies
complementarity and a modest-cost region that can support it. It also
exposes the real weak links: positive coordination, recognition and
non-atomic execution, priced transfers and ordinary alternatives, attack
returns, and matching with search costs. Sequential delivery, unlike the
simultaneous case, offers a productive unchanged-goal partner a free-rider
route; lower-cost binding contracts can displace goal change in either
environment. Those controls and limitations refine rather than erase the
conditional adoption construction.

## 7. A longer relationship also improves ordinary reputation

For a repeated version of the raw donation game, an unmodified pair can
play C,C until a defection and then D,D forever. With public observations,
infinite horizon and discount delta, its original incentive constraint is

    (b-c)/(1-delta) >= b,
    equivalently delta>=c/b.                         (7)

The punishment D,D is a strict stage equilibrium. Hence (7) supports
ordinary full cooperation in this explicitly repeated game. Finite-cost
combat can remain available with nonpositive original gain to its initiator
and a known return to the specified continuation; it then supplies no
profitable extra deviation. If attacks instead offer a better physical
outside payoff, the constraint and punishment must be recomputed.

A genuine goal that implements the same stream but costs kappa>0 is
displaced by this available costless ordinary reputation arrangement when
both arrangements' information and continuation assumptions actually hold.
The positive utility-change counterpart is the finite-horizon class with
known terminal date, independent episodes and no binding ordinary device:
the unique all-F stage equilibrium unravels by backward induction, while
a selected G,G continuation can produce A_N(b-c). A jointly implemented
update costing each original less than that stream is beneficial there.
Staged installation, matched delegation and alternative delivery timing
remain the obligations already identified above.

For beta>=1/2, alpha>=0, the bilateral G goal has an additional useful
continuation bound. At every realized allocation with x_i+x_j<=2v,
G_i<=v. If i is behind, G_i<=x_i<=(x_i+x_j)/2; if ahead,
beta>=1/2 gives G_i<=(x_i+x_j)/2. Balanced full cooperation attains v.
Thus both current G's can prefer this outcome even over later goal changes
and transfers within that physical surplus bound. This is the two-member
case of 107's broader goal construction. It preserves a real negotiated
preference change while permitting future improvements outside the old
frontier to be assessed under the actual current goals.

Equation (7) is a sufficient ordinary-cooperation condition, and a necessary
condition for this full-cooperation payoff against a zero credible punishment
floor. It is not a classification of every partly cooperative equilibrium
below c/b. More future interaction raises the gross value of a reusable goal
and can also create a better ordinary alternative; 099's adoption boundary
uses the difference between their actual values.
