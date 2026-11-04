# Renewable resources, combat and fundable production

**R0005 physical and bargaining derivation.** This note supplies
a small material/work mechanism for the productive contract construction.
It distinguishes a combat comparison, an individually rational agreement,
funding, and an implemented current-self equilibrium. No one of those
levels is automatically all the others.

The numerical fixture below is an intermediate opportunity calculation.
[100](100-quality-liquidity-and-credible-retaliation.md) identifies its
ordinary retaliation repair and supplies the revised witness; [E6](../models/E6.md)
records the final scope. Section 6 retains the original integration agenda.

## 1. Resource accounts for one workshop cycle

Agent i begins a cycle with R_i units of project-ready value. Of these,
a_i>0 are preloaded combat consumables. They remain usable for defense
through the cycle and can serve the agent's own project if unused at its
end, but cannot be unloaded, transferred or used as service parts before
the deadline. The remaining R_i-a_i are transferable organized material.
This is a distinction between physical material types, not a legal ban on
attacking. Later examples leave the preloaded apparatus intact on peaceful
paths, so both agents retain their combat action.

A supplier can use c units of transferable organized parts, positive
work w_s and time t_s to activate a customer's raw project batch. This
produces b units of dated customer project benefit, with b>c>0. Raw
material is transformed; the spent c units remain in a spent category.
The b units are personalized productive achievement, not automatically
transferable money. Without that service, a separate process can produce
at most o units from the batch. Communication, transport, verification
and setup consume explicitly budgeted material/work/time. Their aggregate
project-value expense is h=h_i+h_j for the chosen agreement and kappa
for a goal installation. Recurring service costs and one-time setup costs
must not be charged twice.

Payments transfer organized material at one unit of project value to each
party. That common linear numeraire is an instance assumption. Work is
a battery budget; expended work becomes heat. Neither useful work nor
project value is identified with conserved energy. The physical state
retains organized, raw, dispersed and spent material, battery work,
infrastructure, time and agency.

In a renewable version, each workshop cycle receives declared external
flows of raw material, organized supplies, charged batteries and replacement
equipment. Earlier dated outputs are already delivered and recorded;
spent material and retired equipment leave the active workshop boundary.
They are not erased from the material ledger or counted again as new
wealth. Controllers and installed preferences persist across cycles.
A fresh supply stream, rather than resource reproduction by assumption,
supports the repeated opportunities. The independent-cycle specialization
uses scheduled replacement equipment even on peaceful paths; endogenous
repair and resource accumulation are separate extensions.

## 2. A strength-dependent, destructive combat kernel

When combat is initiated, the two preloaded consumables a_i,a_j are spent.
The winner is i with probability

    p_i=s_i/(s_i+s_j),       s_i,s_j>0.

Strength describes the current combat apparatus. Knowing this stochastic
kernel does not reveal its realized winner. Let

    Q=R_i+R_j-a_i-a_j,
    O=(1-d)Q, D=dQ,        0<=d<=1.

O remains organized and D is dispersed. The defeated workshop actuator
is incapacitated for the remaining cycle; its off-site controller and
earlier dated achievements are not destroyed. Future agency is restored
only by the declared replacement stream. The winner may recover x<=D
using portable recovery equipment. It may also choose r in {0,1} to
repair a damaged processing line, costing m_K organized units, w_K work
and t_K time, then process y<=r o of the raw batch. In the serial
specialization, recovery precedes repair and production. The maximum
usable output retained by the winner is

    Y = max [O+x-m_K r+y]                              (1)

subject to

    0<=x<=D, 0<=y<=r o, O+x>=m_K r,
    w_x x+w_K r+w_y y <= B^C,
    t_x x+t_K r+t_y y <= T^C.

B^C and T^C are the actual remaining work and time after combat. They
can include recoverable batteries from both workshops if that wiring is
physically available; the instance must say so. Positive repair and
recovery costs and delay are retained. A continuous version permits
divisible x,y; an integer fixture uses indivisible batches. They are
different specified technologies, not interchangeable numerical rounding.

The material identity for a winner's realized choices is

    (O+x-m_K r+y) + (D-x) + (a_i+a_j+m_K r) + (b-y)
    = R_i+R_j+b.                                     (2)

The four terms are usable output, remaining dispersed material, spent
material and remaining raw material. Available work falls by the stated
operations; corresponding energy remains as heat. The loser's current
workshop has no remaining physical action, while both had Attack before
the fight. Post-combat terminal/incapacity states therefore have a physical
explanation rather than an imposed peace rule.

For simple original preferences over own dated output, expected terminal
holdings from this duel are

    d_i=p_i Y, d_j=(1-p_i)Y.                           (3)

The original net gains relative to initial holdings are d_i-R_i and
d_j-R_j. Increasing strength raises the first quantity at fixed kernel
and stock; more dispersion, tighter work/time limits or more expensive
repair weakly lower Y. Whether that favors an actual agreement also
depends on its costs, funding and execution.

Attack remains an option at installation, inspection, payment and service
checkpoints. An interrupted operation leaves its actual used material,
work and time in the state; the kernel must use those remaining budgets.
Spending setup resources without improving combat capacity weakly lowers
the attainable Y. A simultaneous-attack collision invokes one duel,
not two independent copies of the same stocks. Additional targets,
coalitional attacks and protected outside locations require additional
kernels; they are not resolved by (1).

## 3. Ordinary division can itself make peace stable

Suppose an ordinary settlement consumes h organized units and divides
the remaining R=R_i+R_j-h into x_i,x_j. Its individual rationality
relative to (3) requires x_i>=d_i and x_j>=d_j. Without extra funding
constraints such a division exists exactly when

    h <= R_i+R_j-Y.                                   (4)

This is the real material loss avoided by settlement in this kernel.
For strict inequality, both can improve if shares are divisible. If
settlement expenditures do not improve military capacity or recovery,
the later combat prize Y' is no larger than Y. Thus x_i>=p_i Y and
x_j>=(1-p_i)Y also make a new attack unprofitable for both original
linear agents. Physical attack is retained; the changed status quo
removes its material incentive.

Consequently ordinary peaceful division must be included in the comparison.
Genuine utility change can supply additional productive credibility; it
is not needed merely because static trade was omitted. When h exceeds
the avoided loss, no division of the specified remaining stock can make
both originals as well off as this duel. A cheaper transfer route, a
productive agreement or a changed physical outside option is a candidate
repair and must be tested before generalizing that obstruction.

## 4. Productive service adds surplus but also needs funding

Take a producer i and customer j. A chosen goal installation costs
kappa, and the customer pays p from transferable material after the
specified access/transport fees. If service is delivered, terminal
project holdings are

    x_i=R_i-h_i-kappa-c+p,
    x_j=R_j-h_j-p+b.                                  (5)

The customer retains its preloaded a_j, so feasible payment requires

    0<=p<=R_j-h_j-a_j.                                (6)

Original participation requires x_i>=d_i, x_j>=d_j. Hence a funded
participation interval is

    max(0,d_i-R_i+h_i+kappa+c)
      <= p <=
    min(R_j-h_j-a_j, R_j-h_j+b-d_j).                  (7)

The additional conditions include enough supplier parts after payment,
positive work/time budgets, live attack capability, recognition and a
continuation implementing the promised service. In particular, positive
joint surplus by itself does not finance an advance from personalized
future output. Credit, collateral, in-kind delivery or another partner
may repair a failed (6), but their physical feasibility and incentives
must be supplied.

If the supplier can select the largest acceptable funded price in this
declared offer game, its maximum terminal holdings are

    P_C=R_i+R_j-h-kappa-c-max(a_j,d_j-b).              (8)

This presumes the upper price in (7) is nonnegative and actually accepted.
Strict price-grid consent and bargaining selection require their own
statement; (8) is also an upper endpoint of the feasible payoff interval.
The analogous ordinary division endpoint is

    P_O=R_i+R_j-h-max(a_j,d_j).                        (9)

The extra supplier return from productive goal implementation is

    P_C-P_O=min(b,(d_j-a_j)_+)-c-kappa.               (10)

Thus productive value can be only partly monetizable when the customer's
liquid payment capacity binds. At fixed physical disagreement and costs,
larger b helps up to that bound. Renewable funded payment opportunities,
a cheaper implementation, a funded credit facility or a customer with
greater payment capacity can change it. Calling b large alone is not
an adoption proof.

## 5. An exact physical/funding fixture to audit

Use R_i=2, R_j=8, a_i=a_j=1, s_i:s_j=2:3 and d=1/2. After combat the
winner has B^C=4 and T^C=3. Recovery uses w_x=2,t_x=1; repair has
m_K=w_K=t_K=1; raw processing has w_y=t_y=1 and o=1. Then O=D=4.
In the integer technology, recovering x=2 without repair yields Y=6.
Repair with x=1,y=1 yields only 5; enumeration of the small feasible
set checks that 6 is the maximum. The original duel holdings are

    d_i=12/5, d_j=18/5.

An ordinary agreement costing h=5 leaves only 5, below the duel total 6.
For productive service use b=4,c=1,kappa=1/2,h_i=1/2,h_j=9/2.
Payment p=5/2 gives

    x_i=5/2 > 12/5,
    x_j=5 > 18/5.                                    (11)

Both retain their preloaded combat consumables. The customer has exactly
5/2 transferable units after h_j, so payment is funded. The supplier
has its preloaded unit after h_i and installation, and uses one of the
received units for service. This is a feasible, strictly mutually preferred
productive arrangement at its stated price. The high common transfer cost
is a deliberately adverse comparison, not a claim that it is typical.

For a smaller h, (4) restores ordinary peace; the extra productive and
goal-implementation comparison remains meaningful. For the high-h
fixture, a contractual supplier floor for the customer can make delivery
and later price compliance optimal within 097's relevant physical
frontier. A full selection claim must also check when the floor becomes
active, fee exposure, customer responses, alternative transfer routes,
ordinary controllers and any additional hostile-goal menu. Those checks
are not supplied merely by the strict inequalities in (11).

## 6. Renewal and the next integration step

With genuinely renewed workshops, an installation can persist while
productive and bargaining opportunities recur. Per-cycle gains, attack
returns, customer budgets and recurring verification must all be renewed
according to their stated laws. A one-time kappa can be amortized;
past resource destruction cannot be counted as though it never happened.
Independent identical cycles give a tractable boundary. Endogenous
strength, accumulated wealth, uncertain replacement and changed partners
can move that boundary and require a new continuation calculation.

The next integration should compare the best actual ordinary peaceful
allocation and contract/delegate with the funded productive goal route,
then verify staged current-self choice and the retained attack actions.
The positive opportunity in (7) and the physical ordinary-peace region
in (4) are preserved while testing the funding, implementation and combat
regions that make another route preferable.
