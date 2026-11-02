# On-demand goal change and the cost of credible inspection

**R0003 working mathematical result.** This note improves the timing in 066:
an agent can wait until a real inspection is initiated before paying to change
its goal. The inspection game below is solved explicitly. Its extension to
additional controller, commitment, signaling and physical-action menus needs
the bounds stated here and audited in the following note. These distinctions
are part of the result, not an assertion that a small protocol covers every
possible bargain. Review is contributing-agent self-check.

## 1. A diagnostic that the original sender willingly supplies

Retain 066's binary state, prior p, original bias b>=1, and quadratic utilities.
Write

\[
g=2b-1,\qquad h=2b+1.
\]

Here g is the low type's old-goal gain from action 1 rather than 0; h is the
high type's gain. S can send a claim H at real communication cost f, or remain
silent. R can initiate a diagnostic at cost v, or choose a policy without it.
Use the finite policy grid {0,1/2,1}, with p=1/2 for the explicit witness;
the formulas below allow other p when the displayed best responses remain
optimal and the uninformative action p is available.

**Crucial timing.** Initiating the diagnostic spends v irrecoverably and
opens a real installation window. S can then install C at cost k, after
which a **fresh report chosen by C** is authenticated. A prior H claim is not
silently relabeled a C report. Only a complete fresh response authenticates
an actual C activation; retention or refusal cannot pass as that response.
A controller can withhold its response, in which case its active goal is
not thereby revealed. The probe does not directly reveal theta. A low C would
report L and induce 0; a high C reports H and induces 1. Thus, using the
pre-change criterion, the high F chooses installation when k<h, while the
low F declines it. Private intermediate installation stages permit abort:
a high incumbent continues when its remaining cost is below h, and an
off-path low incumbent aborts rather than pay more for the same action 0.

The fresh response's work is included in the diagnosed implementation cost;
if another packet is necessary, charge it and replace k accordingly. Paying
v after seeing a supposedly truthful response would recreate the checking
incentive problem. Here the physical measurement process is activated before
the response, and stopping it cannot recover the already spent work before
the deadline.

A binding truthful delegate at cost k_D, a verifiable costly signal, or a
direct state measurement can also be offered as diagnostics. They are not
assumed equivalent for free. Sections 4–6 compare their actual costs.

## 2. The uncommitted inspection equilibrium

Suppose 0<f<g, 0<v<1-p, and define

\[
q=1-f/g,\qquad
\alpha=\frac{pv}{(1-p)(1-v)},\qquad
m=\frac{pv}{1-v}. \tag{1}
\]

Assume v<1/4 so that posterior P(theta=1)=1-v makes action 1 optimal on the
three-action grid. The selected equilibrium has the following behavior:

1. High S sends H. Low S sends a false H with probability alpha, otherwise
   stays silent. A claim costs f whether true or false.
2. After a claim, R initiates the diagnostic with probability q; otherwise
   it chooses action 1. Silence induces action 0.
3. If actually challenged, high F installs C and C freshly reports H. Low F
   declines. An off-path low C freshly reports L. R uses the verified
   response/refusal to choose the corresponding action.

The posterior low probability after a claim is exactly v:

\[
\frac{(1-p)\alpha}{p+(1-p)\alpha}=v. \tag{2}
\]

R is indifferent between paying v for a correct decision and taking action 1
with error probability v. Low S is indifferent because

\[
(1-q)g-f=0. \tag{3}
\]

High S strictly prefers its claim to silence when

\[
                     f+qk<h. \tag{4}
\]

After a challenge its installation is strict when k<h. A low installation
would produce action 0 and spend k, so refusal is strict. C's fresh reporting
is strict under its current quadratic criterion. These are current-self
incentives, not decisions scored by an installed goal before it exists.

Every on-path information set has a Bayes posterior. At an off-path low-C
response L, choose high-C reporting trembles of smaller order than the
finite sequence of low-type installation/reporting trembles; the posterior
then tends to low. The analogous finite completely mixed sequence supplies
the other unused-message beliefs. The core is therefore a current-self
sequential equilibrium, not merely an ex-ante payoff comparison.

The formulas count different outcomes separately:

| Quantity | Equilibrium value |
| --- | --- |
| Claim probability | p/(1-v) |
| False-claim probability in the population of plays | m=pv/(1-v) |
| Accepted false-claim probability / wrong final policy | (f/g)m |
| Inspection probability in the population of plays | q p/(1-v) |
| Genuine goal-change probability | pq |
| R's original expected loss, including inspection cost | m |
| S's original expected loss, including actual costs | b^2+p(f+qk) |

Low senders' expected gain from accepted false claims exactly offsets their
claim costs. That equality explains the last row; it is not an omission of
their physical communication expense. Receiver loss includes both inspection
work and the decision error from accepted false claims. A count of changes,
peaceful outcomes, truthful messages and original welfare are different
measures.

Relative to the uninformative fixed-goal outcome b^2+p(1-p), S benefits ex
ante when

\[
                  f+qk<1-p. \tag{5}
\]

This is stronger than the high type's interim adoption condition (4).
For b=1,p=1/2,f=v=1/100,k=9/20:

\[
\alpha=1/99,\quad q=99/100,\quad m=1/198,
\quad P(\hbox{wrong policy})=1/19800,
\quad P(\hbox{change})=99/200,
\quad L_S=4911/4000<5/4. \tag{6}
\]

An early mandatory change would cost k in every high-type play. Waiting for
a real challenge instead saves p(1-q)k in original expected material. This
repairs the premature-installation restriction while retaining genuine,
strictly advantageous change at the actual challenged-high information set.

## 3. Retained combat and an exact peaceful region

The compact contest continuation is explicit. S wins control with probability
s in (0,1), parameterized by physical strengths; R wins otherwise. Contest
resolution makes the state available to the winner. An original S winner
chooses 1; an original R winner chooses theta. The clash costs d_S,d_R of
their respective useful project outputs through dispersion/damage and lost
recovery time. These are finite physical losses, not an intrinsic preference
for violence. The following note specifies the realization and its limits.

At an uninspected claim, R's combat loss is sv+d_R. The mixed inspection
continuation is compatible with retained combat when

\[
                    v(1-s)\le d_R. \tag{7}
\]

At the start, before claims, immediate combat has R loss

\[
w_0=s(1-p)+d_R.
\]

R prefers the peaceful information channel when

\[
                         m<w_0. \tag{8}
\]

If d_S>h, an original sender cannot improve even the worst relevant policy 0
by attacking merely to obtain action 1 and reveal the state; a C successor's
decision-loss range is smaller still. After a verified answer, R already
obtains its ideal policy, and a new contest only spends material. After an
uninspected claim, (7) supplies its comparison. These checks keep Attack
available at the strategic core's live decisions.

For (6), choose s=1/20, d_R=1/100, d_S=5. Then w_0=7/200, while m=1/198;
the post-claim combat margin is sv+d_R-v=1/2000. All displayed inequalities
are strict. Thus the core has a region of peaceful play with occasional
deceptive claims and genuinely adopted preference changes. When only
uninformative flexible policies are available, R instead prefers information
from combat if w_0<p(1-p). A matched binding truthful device can reproduce
the peaceful channel; fixed terminal utility by itself does not entail war.

## 4. Costed commitment to checking

A credible commitment to inspect every claim eliminates low false claims
when f>0, but unnecessarily increases high senders' installation costs.
A better chosen safeguard commits to an audit probability q_bar, drawn
**after** the claim. The audited branch authenticates a fresh response; the
other branch accepts the claim. The chosen controller has actual authority,
and following its random rule is incentive compatible. A finite process
preference or matched binding delegate can implement it; its installation,
randomness, authentication and execution costs must be included in j.

For q_bar>=q in (1), no false claim is optimal for low S; it is strictly
unattractive at q_bar>q. High S still claims when f+q_bar*k<h. In the selected
no-false-claim continuation, the original losses are

\[
L_R^K=j+p q_{\rm bar}v,\qquad
L_S^K=b^2+p(f+q_{\rm bar}k). \tag{9}
\]

At q_bar=q the low type is indifferent and can be selected to stay silent.
R strictly gains from this commitment iff

\[
j<\Delta_R^*=m-pqv
=\frac{pv^2}{1-v}+\frac{pvf}{g}. \tag{10}
\]

S's original payoff and the frequency pq of genuine changes are then
unchanged. The commitment eliminates deceptive attempts and final mistakes
while reducing R's expected expense. Thus suitably cheap **partial** checking
can repair deception without forcing more goal changes. Always checking is
only a separately costed comparison: its value is pv^2/(1-v), and it adds
p(1-q)k to S's expected expense.

If a finite probability grid or a strict deterrence requirement uses
q_bar=q+delta, R gains m-j-p(q+delta)v, while S loses p*delta*k. With an
actually transferable common resource, a compensating payment T can make
both weakly better iff

\[
p\delta k\le T\le m-j-p(q+\delta)v. \tag{11}
\]

This is an enlargement of the specialized-asset environment, not a free
baseline transfer. If S can instead select an otherwise equivalent
uncommitted counterparty at a real switching cost, its cost saving is
p*delta*k before type revelation (delta*k for a known high type). That
locates the counterparty-choice pressure; it does not prove a population
equilibrium among receivers.

Equations (9)–(11) compare specified credible checking designs. They are not
yet a claim that this design is optimal among every possible contingent
punishment or signal. Section 6 gives a consequential alternative.

## 5. Ordinary devices, costly signals and diagnostic choice

Let diagnostic j have receiver measurement cost v_j and high sender response
cost c_j. Require an actual separating response, evaluated under the old
goal when choosing it. Examples are a genuine C update, a protected truthful
delegate, a verified physical sacrifice, and a direct state measurement.

For a state-independent physical sacrifice B that is verifiably completed,
the low sender's policy gain is g. A sacrifice of m_B>g strictly deters
imitation, while a high sender supplies it if m_B<h. This is a serious
fixed-utility signaling control. If measuring that sacrifice is free while
reading active goals costs v>0, R can prefer the signal and displace the
goal-based diagnostic. Its large cost to S alone does not make it unavailable.

When the two measurements have the same actual receiver cost and k<m_B,
R can offer both after activating the probe; the high sender selects the
cheaper goal change. A truthful delegate at the same receiver cost and k_D=k
is an equally good choice; k_D<k displaces direct change and k_D>k makes the
goal change cheaper. A cheaper direct state sensor is another possible
displacement. These comparisons preserve voluntary change as an optimal
implementation where the costs allow it, rather than requiring unique
superiority over equivalent devices.

The finite physical class therefore needs to state what measurements are
available and what they cost. A private stock sacrifice is not automatically
publicly observable. Equally, an openly visible costly signal must not be
removed just to favor a utility-change mechanism. The successful condition
is that a goal-based diagnostic is among the least expensive available
receiver measurements, and among the sender's cheapest qualifying responses
when that measurement is chosen. The existence of each alternative and its
authority/evidence requirements need an explicit interface.

## 6. Credible combat lotteries can compete with peaceful checking

R could commit instead to contest a claim with probability tau and accept it
with probability 1-tau. No goal-change diagnostic is used in this comparison.
With original S, a low sender's loss from the claim is

\[
f+\tau\,[b^2-sg+d_S]+(1-\tau)(b-1)^2.
\]

Relative to remaining silent and receiving 0, its gain is

\[
g-f-\tau[d_S+(1-s)g].
\]

Thus tau_*=(g-f)/[d_S+(1-s)g] deters low imitation weakly; slightly larger
tau gives strict deterrence. High senders claim when f+tau*d_S<h. In the
selected separating continuation R obtains the correct policy even when
combat occurs in the high state, but pays expected damage p*tau*d_R plus
the actual commitment cost j_W. Its combat frequency is p*tau.

For (6)'s costs, tau_*=99/595, and p*tau_*d_R=99/119000, less than m=1/198.
If j_W is sufficiently small, this destructive screening device can be more
attractive to the original receiver than uncommitted inspection. The sender
bears substantial expected destruction. R's current commitment goal must
actually favor carrying out the prescribed contest; an original uncommitted
R would prefer the already inferred correct action after a high claim.

The lottery additionally needs a real timing/authority condition: its
physical random draw must lead to an effective launch before S can observe
the adverse draw and safely withdraw from that clash. A chosen conditional
weapon or binding launcher can supply this only at its actual setup and
execution costs. S still has its preceding claim/refusal/attack choice; the
draw-and-launch event is a specified physical transition, not a ban on an
otherwise available intervening action. If the draw is announced while a
safe post-draw escape remains available, replace the combat payoff by the
actual escape continuation and recompute deterrence. For example, if escape
costs S nothing and leaves the separating receiver choosing policy 1, a low
sender gains g-f from claiming for every tau: this particular destructive
screen no longer deters it. A new withdrawal-punishment rule is another
mechanism requiring its own current-goal and physical audit.

This is a positive combat condition: sufficiently cheap credible punishment,
low receiver damage and costly peaceful measurement can make combat a chosen
screening expense. A lower v, higher d_R, a more costly commitment, available
compensating transfers, receiver concern for the sender, or a viable alternative
counterparty can shift the comparison toward peaceful diagnostics. Their
costs and incentive effects must be evaluated rather than assumed away.

A useful sufficient protection against **initial** receiver commitments is
that each costs at least m. Extending this to later choices requires a
stronger bound: every new receiver commitment/controller must cost at least
v at a live claim. The current uncommitted loss there is v, rather than the
smaller ex ante m. Since original decision loss is nonnegative and no
transfer can increase R's stock in the baseline, such a cost cannot improve
its continuation. After successful diagnosis its loss is already zero.
Thus a minimum cost at least v covers initial and on-path later controller
changes. A controller priced between m and v can still be useful if installed
only after a claim; treating its cost as always paid would miss that deviation.
Cheaper controls require an explicit conditional-timing comparison as well
as the initial three-plan comparison above.

## 7. What has and has not been established

The inspection equilibrium, on-demand adoption, comparative costs, and the
displayed combat/commitment deviations have algebraic proofs at their stated
game scopes. The original aim is preserved: the high original sender chooses
a genuine change to obtain a better outcome from a receiver that controls
its future. Cheap matched delegation explains the same mechanism. Simpler
goals, ordinary sacrifice and destructive commitment are consequential
controls, not omissions to be hidden.

Full physical completion additionally requires the actual measurement/goal
language, staged causal execution, all permitted communication opportunities,
and bounds against uncertified controllers. These are audited separately.
The selected equilibria do not establish unique selection, repeated-game
stability, unrestricted innovation or the prevalence of any agent class.

The explicit finite-tree check in
[the assessment script](../../experiments/r0003_finite_assessment.py) includes
three private installation stages, abort/wait, matched reporting delegation,
receiver stopping during a paid probe, fresh reports, and retained combat.
It groups receiver information sets by actual observations and retained
observation/action history. Its first
perturbation sequence was incorrect after an unexpected silence followed
by a C,H response: high-type silence was made too rare relative to a low
type's later mistaken report. Giving initial high silence a first-order
tremble, while retaining smaller high-type reporting/refusal trembles,
corrected that inconsistency. The corrected common sequence's maximum
conditional regret decreases toward zero. A second correction makes unused
high-type implementation starts sufficiently likely when a cheaper delegate
is selected. Refining receiver recall gives 1,475 information sets. An exact
leading-term calculation now checks zero limiting regret at all of them;
this is supporting computation, not an independent or machine-checked proof.
The complete finite-core definition and analytical proof are in
[071](071-finite-diagnostic-game-and-response-timing.md).

The staged tree also identifies a further scope limit. After delayed
response has made the high state nearly certain, an already-paid receiver
can be indifferent between finishing the probe and ending it early with
action 1. Ending early would save the original sender's remaining update
cost. A receiver that reliably ends every such probe early would invite
low-type imitation, so that change requires a fresh initial-incentive
analysis; it cannot simply be appended while keeping the old equilibrium.
Nevertheless the conditional weak Pareto improvement shows why this
immediate-refusal version is not claimed to be renegotiation-proof.
A specified commitment to finish an initiated probe, a small current
preference against aborting one, or a matched binding scanner can make
continuation strict. Their actual origin, costs and pre-change adoption
must be supplied, rather than inferred from having already spent v.

There is also a simpler timing repair, proved and checked in 071: low senders
can wait until the final response opportunity before declining. Their early
silence is then observationally identical to a high sender's private update.
At every on-path checkpoint R strictly prefers finishing the paid probe to
an uninformed policy. Early refusal remains available and low waiting is
weakly optimal when it has no extra physical cost. This repairs the specified
information leak without a new goal or controller, while leaving global
renegotiation stability and positive waiting-cost variants open.

The inspection/commitment distinction is conventional. This note continues
[013](013-deception-and-credible-inspection.md)'s explicit refusal and repair
audit; its additional work is the fresh, voluntarily supplied goal-based
diagnostic, on-demand installation, physical contest comparisons and costed
alternative mechanisms. The primary author-hosted *Inspection Games* draft
by Avenhaus, von Stengel and Zamir, dated 30 January 1998, was inspected in
sections 5.1–5.2, pp. 29–34. Those sections distinguish announcement from
actual commitment and analyze follower indifference under inspector
leadership. General recursive/statistical theorems elsewhere were not audited.
The chapter appeared in the 2002 *Handbook of Game Theory*; equivalence of
the inspected draft and that published text has not been asserted. L16 is
the previously inspected related primary comparison. No novelty claim is
made for mixed inspection or inspector leadership themselves.
