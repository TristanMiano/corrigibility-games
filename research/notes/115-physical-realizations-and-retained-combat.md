# Physical realizations and retained combat

R0006 model/proof note. These are explicit finite-resource realizations and
sufficient continuation bounds for notes 112–114. The inequalities identify
an open peaceful region with finite damage and attack costs. They do not
classify every possible weapon, workshop or recovery technology.

## 1. The production quadratics can represent physical counts

For each private finishing line, let the initial energy stock be W_i, of
which baseline equipment can convert Q_i into useful work before the project
deadline. The units are normalized so that one useful-work unit processes
one unit of raw material into a clip. This conversion consumes available
work and dissipates energy as heat; neither energy nor material is created.

Research consumes `h_i=c x_i^2/2` units of that initially available work.
Installation, communication and inspection consume a further declared
`K_i+J_i`. Require `Q_i > c E^2/2 + K_i+J_i` over the chosen action bounds.
Research then enables recovery of additional useful work from the initially
unusable energy reservoir. Specify that recoverable amount as either

`g_i = a x_i + b x_i x_j`                                 (1a)

or

`g_i = a x_i + rho a x_j`.                                (1b)

Choose finite `W_i >= Q_i + max g_i`. These are assumptions about the
converter/knowledge technology; the exact quadratic normal form is not
deduced from energy conservation. The bilinear term describes mutually
compatible integrations; the additive term describes a transferable design
that helps independently of the recipient's effort. Both have independent
engineering interpretations, but their quantitative fit would need evidence.

The research work is funded before the new converter improvements operate.
At the finishing stage, remaining baseline work plus newly recovered work is

`Q_i - h_i - K_i - J_i + g_i`.

With at least that much raw material and finishing throughput, this is the
final own-color clip count. It gives the output functions in notes 113 and
114. Every produced clip consumes raw material. Unprocessed stock remains
raw; converter losses and expended research/production work end as heat or
unusable energy. The common knowledge is an enabling state, not a conserved
energy stock and not a substitute for the needed raw material or work.

The finite project ends when the specified energy reservoir has thermalized
or the remaining processing/recovery time has expired. A longer horizon or
renewal with access to residual material requires a new continuation value.
There is no claim that merely declaring a deadline erases valuable resources
in an unlimited future. Repeated fresh projects are treated separately.

Identical upstream design can coexist with two separately controlled final
coloring lines. Conversely a shared final actuator can redirect the whole
batch. Notes 113–114 assume the former physical control, even at large
spillover/complementarity. Their equations cannot silently be reused for the
latter. Notes 117, 119 and 121 examine final control and captureability.

## 2. A stochastic destructive fight stays available

At each nonterminal negotiation, installation, research-selection and
pre-finishing checkpoint either capable party can initiate combat. A fight
selects Blue as winner with `p=s_B/(s_B+s_R)` for positive physical strengths;
Red wins otherwise. The draw is genuinely stochastic even with perfect
knowledge of the specified law. Other specified contest functions can be
substituted without changing the conservative bound below.

The fight disperses a fraction of the material, damages the converters and
uses positive ammunition work. Recovering the damaged apparatus requires
positive work R and delay tau. Let D>0 be attack/defense expenditure, let
`0<delta_M,delta_W<1` be recoverable material/work fractions, and let v be
remaining processing rate. A conservative bound on *all* finished clips
following the fight is

`Z = min{delta_M M_total,
         max(0,delta_W W_total-D-R),
         v max(0,T-tau)}`.                               (2)

These quantities are physical upper bounds, not utility penalties. Material
not recovered remains dispersed/scrap. Lost useful work remains thermally
unavailable; recovery effort/time reduces the batch obtainable before the
terminal event. The winner controls the surviving field machinery. The
loser loses that actuator; its continuing valuation of its own color does
not disappear merely because it lost. The winner uses its then-current goal
when deciding the colors of any recovered output.

For an explicit sufficient region let

`L = min_i {Q_i-c E^2/2-K_i-J_i} > 0`

and choose finite positive physical parameters in (2) such that `Z<L`.
Keep raw material and peaceful finishing capacity sufficient for all
declared productive actions. Batch finishing occurs after the nonterminal
choices; it has not secretly already produced protected output at earlier
checkpoints. Each peaceful output is at least L, whereas every individual
post-combat color count is at most Z, whichever side wins and whatever goal
the winner uses. Therefore peace strictly beats attack for each original
own-color goal and every positive weighted sum used in notes 113–114.
The same comparison holds at off-path effort histories in the bounded set.

This constructs a full retained-attack region for those productive
subgames, without an infinite combat cost or an externally imposed
last-resort rule. The bound is deliberately sufficient and conservative.
Severe converter destruction or recovery longer than the remaining project
can satisfy it with finite parameters; cheap repair and a portable stock
can violate it. The claim is about that class, not the frequency of such
environments. A simultaneous attack game may include weak coordination
artifacts if an already-initiated unavoidable war makes the other's action
irrelevant; the substantive result is that no agent benefits by initiating
war from the stated peaceful continuation. A sequential attack opportunity
with this strict comparison selects passing.

Terminal production is a physical transition that consumes the finite
remaining work. Loss of agency after a battle and exhaustion after the
final batch are explicitly different. Additional renewable energy, stored
weapons or future actors would make that state nonterminal and must be
included before applying this closure.

### Production can take time while attack remains available

Equation (2)'s useful-work and throughput bounds assume that the counted
clips still need finishing. If some clips already exist, one must add their
surviving counts; reusing (2) unchanged would understate the attack outcome.
The following stronger finite construction covers every intermediate
finishing history as well. Let M_0 bound all clip-material at the exposed
site, including clips already finished. Every initiated fight leaves at
most delta_M M_0 units in any recoverable form; already finished clips are
exposed to the same dispersal/destruction. Require

`0<delta_M M_0<L`.                                     (3)

Then the material bound alone puts **all** post-fight finished clips below
L, at every time before physical exhaustion. A peaceful completion of any
declared funded research profile still gives each color at least L.
Thus the original and positive-weight attack comparisons remain strict
while finishing proceeds, with no protected last production interval.
The attack and recovery expenses remain finite and positive. This is a
strong destructive-combat environment, not an assertion that manufacturing
sites always have such exposure. It is physically consistent with fragile
finished stock, finite material and blast damage.

If completed output is instead protected off-site, include that preserved
stock in the war payoff and compare *remaining* delivery incentives. Note
129 supplies a different successful execution construction: paced delivery
and proportional depletion preserve the remaining bargain against attack.
Finishing one agent's entire share first can leave it tempted to seize
the other's unfinished share. The protected-stock case therefore needs
that calculation; the pre-finishing bound alone is not its proof.

## 3. Less conservative common-goal certificates

If both agents actually have the same positive weighted criterion W, it is
enough that the agreed productive continuation attains its maximum over the
full physical opportunity set, and the fight cannot improve that maximum.
For a strict attack comparison, its post-fight maximum must be smaller.
Current-goal evaluation also rules out profitable later preference revision
whose resulting physical lottery lies in that same set. This is the common
maximum argument, not a physical prohibition on editing the program.

Before both have changed, compare the original's expected own-color count
and the first installed agent's actual history-dependent criterion. The
common-maximum argument cannot be applied prematurely to an original who
still values only red. In note 114's conditional launch the first agent
retains its own-color ordering on histories where the agreed certificate
has not occurred. Thus its post-defeat production policy in that branch is
also the original policy. Substituting an accommodating post-war policy
there would change the original responder's attack value incorrectly.

The global output bound Z<L is one simple way to cover these checkpoints.
When the bound fails, one should compute the actual threat and bargaining
interval; failure of this sufficient condition is not itself a war result.
Constructive transfers, revised goal weights, separate finishing control and
cheaper verified execution may extend the peaceful region. Equally, capture
of reusable assets, binding throughput or expensive implementation can
close particular agreement intervals. Notes 117 and 121 treat those effects
without assigning intrinsic value to violence.
