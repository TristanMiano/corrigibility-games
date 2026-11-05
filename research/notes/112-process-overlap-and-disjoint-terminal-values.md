# Shared production processes with disjoint terminal values

**R0006 definitions and physical opportunity results.** Blue originally
maximizes the final physical count B of blue paperclips; Red maximizes R.
Thus U_B(B,R)=B and U_R(B,R)=R. Neither original values a common factory,
knowledge, friendship or the other color intrinsically. The counts refer to
the world outcome, not possession or the continued existence of the original
controller. A successor's different ordering must be chosen using the current
criterion. No independent review or novelty claim is made.

## 1. What production overlap measures

Represent a production method by a directed network of physical operations:
acquisition of feedstock, preparation, construction, research, processing,
finishing and final-color production. Each operation specifies required input
materials, work, capacity and time; outputs include useful intermediates,
spent/dispersed material and heat. Knowledge is an enabling state of a
controller or machine, not extra material. Final-color conversion consumes
its stated inputs and can remain different even if the preceding operations
are almost identical.

Three quantities must be distinguished:

- **Reusable knowledge/setup overlap:** performing one operation can supply
  both production lines without performing that operation twice. Research
  can be nonrival in use while access to its result is costly or excludable.
- **Reusable equipment overlap:** the same equipment can serve both colors,
  with a specified throughput and scheduling constraint. Identical machine
  designs do not make one machine's time nonrival.
- **Rival input/intermediate overlap:** either final product can consume
  the same metal, energy, prepared blank or factory slot. Consumption by
  one line then changes what remains for the other.

Control rights, transferability, copy cost, recoverability after combat and
the exclusivity of a partner are additional variables. A count of common
graph nodes is not invariant: subdividing one operation into ten would alter
it without changing the world. A useful scalar fraction is therefore tied
to a declared baseline workload and cost account. Changing that fraction
can alter several incentives jointly; every comparative claim states which
other physical quantities are held fixed.

The zero-overlap endpoint means no shared productive dependency or useful
cross-line transfer in the specified class. If the two feasible sets also
factor and neither can improve by capture, separate own-color maximization
already attains their joint feasible maximum. At positive agreement cost,
the same outputs with an additional agreement are strictly worse for any
party whose cost displaces its valued production. This is an ordinary
independence result, not a conclusion about a world with omitted trade,
complementary endowments or a useful shared resource. Introducing those
channels creates a different, potentially beneficial cooperation problem.

At the other endpoint, all upstream operations may be shared while final
color remains a distinct choice. Blue and Red still have different terminal
preferences. The technology determines the available gains from sharing;
authority and division determine who obtains their own color.

## 2. Avoided duplication gives an explicit cooperation budget

Consider a workload specialization. Each standalone line needs F>0 units of
setup work before manufacturing. A fraction theta in [0,1] of that work is
identical and reusable across the lines; the remaining (1-theta)F is specific
to each color. Sharing an executed common setup therefore costs

    K_shared(theta) = theta F + 2(1-theta)F
                    = (2-theta)F.                   (1)

The standalone requirement stays 2F. This interpolation concerns reusable
setup, not the entire vector of overlap in section 1. It reaches complete
setup overlap at theta=1; actual final-color work remains separate.

Let M be the total available feedstock, one material unit per finished clip,
and W the total available battery work. Each manufactured clip needs w>0
work units, including final-color finishing. Let H>=0 be the actual extra
work required by the sharing route: communication, transfer, checking,
installation if used, and any recurring administration in this workload.
Suppose both colors can use the shared setup without reducing the total
throughput capacity C, measured in clips before the deadline. Then the total
finished-output frontier is

    Q_theta(H)=min{M, C, [W-(2-theta)F-H]/w},        (2)

on the domain W>=(2-theta)F+H. A route outside that domain cannot complete
setup; a negative bracket is not negative manufactured output.

The physical ledgers remain separate. One unit of raw metal becomes one
finished clip or enters the specified scrap account. Spent battery work
becomes heat. Setup operates on existing equipment and information states;
any construction parts consumed are separately budgeted or included in M's
available remainder. Formula (2) presumes sufficient setup parts, feasible
positive-duration scheduling and the declared common throughput C. It does
not identify work with material or utility.

Let standalone work budgets W_i>=F and stocks M_i give feasible original
outputs a_i=min{M_i,C_i,(W_i-F)/w}. For a comparison with a=a_B+a_R,
the sharing route permits both originals to improve strictly exactly when

    Q_theta(H)>a,                                  (3)

provided any split of its total between final colors is physically available
and funded. Necessity follows by summing B>a_B and R>a_R. Sufficiency follows
by selecting B in (a_B,Q_theta-a_R) and R=Q_theta-B. This is a feasible
opportunity statement; it does not assign the selected split to an equilibrium.

In the work-limited matched case a=(W-2F)/w, put
L=min(M,C)-a>=0. Then the gain over standalone output is exactly

    Q_theta(H)-a = min{L, (theta F-H)/w}.            (4)

Thus positive remaining material/throughput slack and theta F>H give a
strictly beneficial share interval. Until a physical cap binds, each unit
increase in theta saves F work and expands the cooperation budget by F/w
clips. Once the cap binds, further setup sharing saves work but creates no
additional clips in this deadline model. That saved work becomes valuable
again only if an actual later or alternative productive use is supplied.

The corresponding consent thresholds for a particular proposed allocation
must use each agent's actual alternative, including other partners, ordinary
contracts and combat, in place of a_i. Formula (3) then remains a feasible
split test only when those outside values and this common frontier are the
appropriate comparison in the stated initial game.

### Worked physical comparison

Take W=24,F=4,w=1, ample M>=30 and C>=30. Separate lines produce a=16
clips, eight of each color under equal budgets. A shared route costing H=1
has Q_theta=15+4theta. Its strict mutual-improvement region is theta>1/4.
At theta=1/2, equal division gives 8.5 clips of each color; at theta=1 it
gives 9.5. Fractional quantities denote divisible manufacturing batches;
integer fixtures must instead select an actual granularity and tie rule.

No agent is rewarded for the other color in these original comparisons.
Each values the increased count of its own clips. A genuine goal-change
route with an extra total work expense k has H increased by k. Its positive
budget must be compared with the best actual ordinary sharing route, rather
than only with duplication.

## 3. Shared machines need a capacity comparison

If sharing replaces two machines by one of lower aggregate capacity,
replace C in (2) by the shared machine's actual C_shared. An independently
replicated design may retain C_B+C_R while sharing only research work;
one common physical tool may instead have C_shared<C_B+C_R. The efficient
choice compares both routes, with their actual setup and scheduling costs.

For the numerical data, C_shared=15 makes every shared-machine route produce
at most 15, below the separate total 16, even at theta=1. Keeping two machines
and sharing only the reusable design can restore the 19-clip frontier when
its additional cost permits it. The restriction is scarce machine time,
and the repair is actual replication or scheduling capacity, not a change
in either original's terminal values.

The final-color stage also remains a possible bottleneck. A common upstream
capacity of Q with color capacities c_B,c_R permits a strict improvement
over a_B,a_R only if c_i>a_i for both and Q>a_B+a_R. When these conditions
hold, sufficiently small positive increments satisfy all three constraints.
If a color's final station is saturated, shared upstream improvements alone
cannot increase that original's clips; expanding that station is a distinct
funded intervention to evaluate.

## 4. Opportunity, chosen arrangements and the next proof obligations

These equations identify the real avoided work, its finite-resource limits
and the original consent budget. They preserve peaceful alternatives with
unchanged utilities. A funded ordinary contract or delegate that implements
the same physical route at lower total cost can outperform a goal change;
at equal cost genuine change can remain an optimal implementation.

The constructive goal-design question is whether the parties can choose
new criteria that make the shared process and agreed final colors credible,
then prefer their actual implementation under their existing own-color
criteria. Equally test underprovision, last-stage redirection, capture,
recognition and staged-exposure failures, and relevant transfers, duplication,
modularity, partner choices or safeguards that repair them. Combat remains
available in the surrounding game and needs an explicit physical kernel;
(1)-(4) are productive subproblem results, not a baseline that deletes it.

Naturality and deliberate attainment differ. Reusable designs and finite
machine time have independent motivations. A party can choose standardization,
knowledge exchange or machine replication only through specified actions,
resources and information. An exogenous increase in theta is a parameter
comparison until that intervention and its current-goal incentive are proved.
