# Smooth common goals, final-color protection and ordinary repetition

R0006 derivation extending the common-goal opportunity in note 116. This
supplies a smooth negotiated goal with unique productive continuation, then
compares it with revocable policies and an actual repeated-game control.
Initial consent/installation still uses its specified protocol and costs.

## 1. A finite, monotone goal that selects both colors

Use note 116's compact physical effort/output class. Write

`T=q_B+q_R`, `D=q_B-q_R-d_0`,
`H(q_B,q_R)=T-eta D^2`, `eta>0`.                          (1)

The target difference d_0 is negotiated. For symmetric production and equal
expenses use zero. If only installation expenses differ, use
`d_0=-K_B+K_R`, so that equal efficient effort attains D=0. This is a genuine
new output ordering for both originals, with a finite balance penalty and
no reward for retaining particular code. Choose a valid finite bound
`|D|<=D_max` over every relevant physical continuation, and require
`2 eta D_max<1`. Both partial derivatives of H in the color counts are then
positive. The goal never needs an intrinsic liking for destruction within
that declared domain.

For any physical outcome, `H<=T`, with equality exactly at the target
difference. If a feasible plan attains the maximum total T_max and that
difference, it attains the global H maximum T_max. A different final color
split at the same total is strictly worse. Thus a shared final actuator can
be permitted to choose the split without leaving the indifference of a pure
total-count goal. The physical plan must actually be able to produce both
colors in the target amounts; a utility function does not create finishing
capacity.

For a final allocation choice, moving epsilon clips from Red to Blue at the
target increases the original Blue goal but decreases H by `4 eta epsilon^2`.
That is an explicit preference reversal where both allocations are feasible.
Expected utility is `E[H(q)]`, not `H(E[q])`. In particular the penalty
includes the variance of D; this difference matters under stochastic output.

## 2. The effort equilibrium is unique under an explicit curvature bound

For the symmetric linear-quadratic physical family,

`T=2Q+a(1+rho)(x_B+x_R)+2b x_B x_R`
`  -(c/2)(x_B^2+x_R^2)-K_B-K_R`,
`D=a(1-rho)(x_B-x_R)-(c/2)(x_B^2-x_R^2)`                 (2)

when d_0 accounts for the cost difference. Its effort Hessians satisfy

`lambda_max(Hess T)=-c(1-2|s|)`,
`Hess D=diag(-c,c)`.

Differentiating (1),

`Hess H=Hess T-2 eta grad D grad D' -2 eta D Hess D`.

The middle term is negative semidefinite; the last has operator norm at
most `2 eta c D_max`. Therefore the strict bound

`0<eta<(1-2|s|)/(2 D_max)`                               (3)

makes H strictly concave in joint efforts throughout the rectangle. A
conservative valid effort-domain bound is
`D_max=a(1-rho)E+(c/2)E^2`; enlarge it if final reallocations or other physical
outcomes have a greater difference. If D_max=0 no balance correction is
needed on that singleton-difference domain. All constants are finite.

At `x_B=x_R=x_eff`, T attains its unique maximum and D=0. Hence H attains
its unique joint effort maximum there. In a simultaneous common-payoff
effort game, differentiable concavity makes every coordinatewise best
response profile a joint maximum: add the two individual first-order
variational inequalities to obtain the joint one. Strict concavity then
gives a unique Nash effort equilibrium. This avoids treating a merely
available common maximum as a unique selection under an arbitrary nonsmooth
goal. The proof uses both smoothness and the explicit curvature restriction.

If the final actuator can freely allocate a previously produced total T,
it first chooses D=0 whenever feasible. Its optimized H value is T, so the
same strictly concave total-production problem gives efficient efforts.
However the **original-goal** benchmark in such a centralized finishing game
must be recomputed; it is not automatically note 116's private-line q_F.

Current H-agents cannot profit by changing their later goals or policies
when the resulting physical lottery remains in this same opportunity set:
every realized H is at most the attained maximum. A fight with a strictly
lower total bound is also strictly worse. This allows revisions and attack;
it does not forbid them. Future technology, new partners or capital beyond
that feasible set require a fresh comparison.

## 3. A revocable ordinary plan and a repeated ordinary control

Return to the private-line production family, with actual original efforts
available at each production decision. Merely recommending x_eff to a
retained original fails the one-shot incentive test when ell is nonzero.
Against a partner's x_eff, the original best response is

`x_dev=t+s x_eff`,
`x_eff-x_dev=t ell/(1-2s)`.

The original gain from this unilateral effort deviation is

`Tempt=A ell^2/[2(1-2s)^2]`.                             (4)

The cap assumptions in note 116 include this best response. Completing the
own-effort quadratic proves (4). A publicly committed controller can prevent
or deter this deviation if that technology is actually available; a late,
unobservably revocable instruction cannot be treated as the same device.

Now consider indefinitely renewed, independent production opportunities
with the same per-period technology, common discount d in (0,1), perfect
public action monitoring, and no inter-period accumulation or retaliation
resource cost. Effort here means recurring integration/maintenance; a
persistent stock of already learned research is a different model. The
retained-goal strategy 'play x_eff until a detected deviation, then play
the ordinary stage equilibrium x_F forever' is subgame perfect exactly
when the cooperation incentive condition holds:

`d >= d_crit=Tempt/(Tempt+Delta_eff)`
`           =(1-s)^2/[(1-s)^2+(1-2s)]`.                  (5)

The cooperative and best-deviation payoffs differ by (4); the permanent
punishment is credible because x_F is the stage Nash equilibrium. Comparing
discounted sums proves (5). It is the threshold for this explicit trigger
control, not a universal necessity for all repeated strategies. Monitoring
costs, noise, different punishments and endogenous renewal require their own
calculation. Retain the physical attack action at each date; note 115's
uniform dominance bound is one sufficient condition to preserve this
ordinary equilibrium without an extra combat deviation.

Thus sufficiently patient originals can achieve the productive cooperation
without changing utilities in this repeated environment. Below (5), the
same trigger strategy is not incentive compatible; this does not by itself
exclude every possible repeated agreement.

## 4. Renewable consensual change and honest alternative comparisons

For a common H installed once and applied as the discounted sum of its
per-period values, the efficient physical continuation is optimal at each
fresh project. Under the same bound and unchanged feasible opportunities,
the total current H maximum rules out profitable future policy/goal
revisions. Original participation against repeated independent stage play
requires

`K_i < Delta_eff/(1-d)`                                  (6)

for each one-time physically funded installation expense, with any recurring
inspection/maintenance cost subtracted from Delta_eff. The expense must be
paid initially; a large discounted benefit alone does not provide liquidity.
Finite horizons replace `1/(1-d)` by the actual annuity factor. This is an
initial adoption comparison under the actual launch protocol, not perpetual
founder control of successors.

If an available ordinary repeated control already attains x_eff with equal
or lower real expense, its value replaces repeated stage play in (6).
Positive-cost goal installation can then be displaced. If maintaining
ordinary incentives requires more ongoing monitoring than actual installed
goals, the reverse cost comparison can make genuine change optimal. Neither
ordering is established by calling one route 'policy' and the other 'goal'.
At matched availability and cost, genuine change and delegation can tie.

For renewable resources with accumulating knowledge or productive capital,
the opportunity set depends on earlier actions. Apply a dynamic feasible
maximum and the acting successor's current utility, as in note 108, rather
than repeating (6) mechanically. The finite common-goal construction is a
positive continuation result; chosen initial activation, market selection
and population prevalence retain their separate evidential levels.
