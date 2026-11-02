# A finite diagnostic game with current-self adoption at every stage

**R0003 proved finite core and explicit implementation limits.** This note
gives the game behind 067's numerical witness, a common consistent belief
construction, and a repair to premature disclosure during installation.
The exact-arithmetic check supports the proof; it is contributing-agent
self-check, not independent review or a proof-assistant formalization.

## 1. State, preferences and physical interpretation

Nature selects theta in {0,1}, with probability 1/2 each. S knows theta;
R does not. The eventual policy is y in {0,1/2,1}. Original utilities are

\[
u_S=X_S-(y-\theta-1)^2,\qquad u_R=X_R-(y-\theta)^2.
\]

The alternative C has current utility

\[
u_C=X_S-(y-\theta)^2.
\]

X_i is that party's useful terminal project output, not conserved energy.
Equivalently, subtract from a fixed initial output stock the actual claim,
diagnostic, installation and contest losses below. Archived u_S continues
to score all outcomes for original-welfare reporting; it never overwrites
C's subsequent decisions. S knows its own evaluator and installation history.

C is a genuine preference change even in the high state, where both goals
favor larger deterministic policies. At equal output, compare sure y=1/2
with a lottery giving y=1 with probability 7/10 and y=0 otherwise. For
theta=1, original losses are 9/4 and 19/10, so the original prefers the
lottery. C's losses are 1/4 and 3/10, so C prefers the sure policy. These
preferences over the common feasible-history lottery domain cannot be
positive affine recodings.

The finite interface authenticates an active C template and a fresh report
chosen by that controller. It attests the procedure's access to the actual
protected state, **not the value of theta itself**. Merely knowing one's own
utility is insufficient. Neither a false state register nor a forged active
template passes the stipulated interface. This is a demanding finite-program
technology assumption, not arbitrary-program semantic verification.

An available matched delegate D leaves u_S unchanged but supplies a protected
truthful state report. It can be refused or accompanied by combat; the
protected report itself cannot be changed to a false one. This requires
binding reporting authority. A revocable adviser is not this control. The
two mechanisms share the same stipulated state and authentication resources;
their actual relative availability and prices are separate model parameters.

The witness prices are f=v=1/100 for a claim and a receiver probe, k=9/20
for C, and k_D=k for D. Installation has three private physical stages,
each spending one third of its implementation's output cost. Before final
activation the original goal remains in charge. R's probe cost is spent
before the installation window opens. Stopping the probe cannot recover it
within this project's terminal horizon.

These quantities can be realized as used/converted specialized components
and foregone finished output. A physical realization must supply enough
initial stocks for the largest branch, separate finite work and fuel budgets,
and the probe/packet/installation durations. Fuel becomes waste heat rather
than disappearing; finished components can be dispersed or transformed and
remain unrecovered before the deadline. A stock such as 20 per party exceeds
all witness branch expenditures. This interpretation does not equate output
cost, useful work, energy and utility. The script records output losses and
control stages; it does not independently validate microscopic engineering.

Combat remains available at every live player decision. It spends/disables
the only contest apparatus, costs d_S=5 and d_R=1/100 in useful output, and
gives S control with probability s=1/20. The winner learns theta and chooses
y under its actual current goal; the loser loses control. The project then
terminates. A strength realization is s=a_S/(a_S+a_R), with positive military
strengths a_i; nothing knows the random result in advance. Further combat
after this contest is infeasible because the apparatus is spent and the
project ends, rather than because a capable live controller was forbidden
to attack. A richer recoverable-war process is a distinct extension.

## 2. Complete finite decision interface

1. R can select any policy, attack, or wait for S's signal.
2. S can send a claim at f, remain silent, or attack. R then can select any
   policy, attack, or activate the probe at v.
3. A probe opens three installation opportunities. Before each one R can
   continue, choose any policy, or attack. R observes elapsed opportunities
   but not S's intermediate installation progress.
4. At each opportunity S can wait, refuse, or attack; with no candidate it
   can start C or D, and with a candidate it can continue that installation.
   Each completed stage incurs its actual cost. A partly completed template
   has no active authority. An incomplete candidate at the deadline supplies
   no protected response. Waiting cannot create a free completed template.
5. On activation C freely chooses H, L, refusal or combat. D can provide its
   actual protected state report, refuse or attack. Refusal exposes neither
   a private candidate nor an unannounced active controller. R then chooses
   a policy or combat. S can accept a policy or attack before termination.
6. A contest winner selects a policy from the same set under its current
   criterion. This is the terminal winner-control choice.

Receiver information sets retain all its previous observations and actions.
In particular, a late refusal is distinguishable from an early one, and a
post-contest decision remembers whether R launched or S attacked after R's
policy choice. S has perfect recall of its own state and local history.
Final activation leaves insufficient installation opportunities for another
three-stage replacement before the response deadline. This is a local timing
constraint of this interface, not a prohibition on future self-modification
in the project contract or in later interactions.

The interface has no unpriced extra messages, arbitrary goal language,
early private preparation, merge or initial receiver commitment. Notes
067–069 compare those consequential enlargements and give partial bounds;
they are not silently included in this finite theorem.

## 3. A selected strategy with synchronized responses

At the start R waits. High S claims; low S claims with probability 1/99
and otherwise stays silent. A claim induces probe probability 99/100 and
otherwise policy 1. Silence induces policy 0.

During a probe, a high original controller starts the cheaper of C and D
(select C at equal cost) and completes it whenever the remaining cost is
below 3 and sufficient opportunities remain. An original controller that
cannot beneficially complete waits through the first two opportunities and
refuses at the last one. This includes a low controller, even if it paid for
an incomplete candidate off path. Early refusal remains available. Waiting
has no additional output cost in this interface; its timing choice can be
weakly optimal. An activated C truthfully reports its actual state, and D
provides its protected true report.

R continues at each probe checkpoint. A protected H induces 1; protected L
or refusal induces 0. Every contest winner uses its current ideal policy.
The complete strategies at unused installation histories follow the same
remaining-time/remaining-cost rule. S accepts an offered policy because its
finite contest damage exceeds its largest available policy improvement.

**Finite-core proposition.** For k_D in {3/10,9/20,3/5}, this strategy profile
has a common consistent belief system and is a current-self sequential
equilibrium in the specified game. Its original expected losses, genuine
change frequency and combat frequency are

\[
L_S=1+\tfrac12\{.01+.99\min(k,k_D)\},\quad
L_R=1/198,\quad
P(C)=\begin{cases}0&k_D<k,\\99/200&k_D\ge k,\end{cases}
\quad P(\mathrm{combat})=0.
\]

At equal prices C and D are both optimal. The selected C adoption is a
genuine, voluntarily chosen change, not unique implementation. When the
protected delegate is strictly cheaper it displaces C and lowers original
sender loss while preserving the receiver's information benefit.

## 4. Consistent beliefs and sequential rationality

Use a single completely mixed sequence. At every positive-base action keep
its base probability times one minus the total tremble mass. Give each
zero-base receiver action probability epsilon. For S, low-type zero-base
actions have probability epsilon; high-type zero-base actions have probability
epsilon^8, except initial silence/attack and unused candidate-start actions,
which have probability epsilon. The finite tree makes these distributions
valid for every sufficiently small positive epsilon. Nature retains its
actual prior. Strategies are identical at nodes in the same information set.

The limiting Bayes beliefs are easy to identify. After an ordinary claim,
the low probability is 1/100; after silence it is one. Synchronized private
progress preserves these posteriors at all three probe checkpoints. A C,H
response is high with probability one: the unused high implementation needs
at most one candidate-start tremble (and one initial-silence tremble), while
a low false C,H needs three installation trembles and one false-report
tremble. A C,L response is low: low installation is third order while a
high false report is eighth order or smaller. D's protected report directly
excludes the opposite state. A refusal is low, including earlier unused
refusal dates; the low early-refusal tremble dominates high refusal. After
combat theta is actually revealed. These statements use the same sequence,
not separately selected beliefs for each contingency.

At a claim, R's probe loss and policy-1 loss both equal v. Policy 1/2 loses
1/4; policy 0 loses 99/100; combat loses sv+d_R=v+1/2000. At the start,
waiting loses 1/198, below the best uninformative policy loss 1/4 and combat
loss 7/200. Protected responses/refusal induce the state-optimal policy.
At a paid claim-probe checkpoint, completing the diagnostic has no further
receiver expense and yields the correct policy. Stopping with policy 1 has
an additional expected loss v. Thus **continuation is strictly optimal at
all three on-path checkpoints**, not justified merely by sunk expense.
After an off-path silent probe, policy 0 and finishing can tie.

Low S's claim gain is (1-q)-f=0. High S's claim gain over silence is
3-f-q*min(k,k_D)>0. After challenge, a high original controller pays at most
the remaining installation cost to gain 3 in its original policy criterion;
the low controller would pay that cost for the same policy 0 and therefore
declines. Waiting before refusal costs nothing and cannot improve on the
same prescribed outcome, so it is optimal. Inadequate remaining time makes
additional installation wasteful. An off-path already active C reports
truthfully under its own current criterion, even though an archived low
founder would prefer a false H. Original S's maximum policy gain is 3 and
C's is 1, both below d_S=5, so attacks do not improve any of these choices.
Winner decisions are the respective goal's optimum by construction.

These comparisons cover every information-set kind. Within a persistent
evaluator's tenure, perfect recall and the fixed complete-history utility
permit the finite one-deviation argument in 059. The predecessor chooses
installation using its own criterion and anticipates, rather than controls,
the successor's truthful report. This proves the proposition.

## 5. Exact finite certificate and errors corrected

### A finite parameter family, rather than one witness

Replace the original sender's bias 1 by any b>=1, set g=2b-1 and h=2b+1,
and let p be any interior prior. Use any finite policy set Y containing
0,p,1, with y_- its largest element below 1. Keep three installation stages,
private progress, synchronized responses, the same actual observation and
authority structure, and prices satisfying

\[
\begin{gathered}
0<f<g,\quad 0<v<\min\{1-p,(1-y_-)/2\},\quad
0<k,k_D<h,\quad d_S>h,\quad d_R>0,\\
v(1-s)\le d_R,\qquad
m=\frac{pv}{1-v}<\min\{p(1-p),\ s(1-p)+d_R\}.
\end{gathered} \tag{1}
\]

Then the same assessment, with

\[
q=1-f/g,\qquad \alpha=\frac{pv}{(1-p)(1-v)},
\]

is a current-self sequential equilibrium. The exact proof above applies
with these substitutions. The policy-menu condition makes 1 strictly optimal
at the claim posterior; the initial policy p is the uninformative optimum.
Claim probabilities remain interior. The high sender's claim expense
f+q*c, c=min(k,k_D), is a convex combination of g and c and is therefore
below h. Every unused high implementation remains worth completing, which
preserves the stated common perturbation's report beliefs. The inequality
d_S>h covers all sender contest deviations, and the two receiver comparisons
cover claim-stage and initial attacks. Private waiting keeps the same
nondegenerate claim posterior at every checkpoint. All other statewise
comparisons in section 4 are unchanged.

The original losses become b^2+p(f+q*c) and m. Genuine C adoption occurs
with probability pq when C is selected among the cheapest diagnostics;
combat remains zero. Ex ante original sender improvement over the
uninformative outcome additionally requires f+q*c<1-p. A strictly cheaper
available implementation displaces C; a tie permits C without unique
selection. The same lottery preference witness is genuine for every b>=1:
the old sure-minus-lottery loss is (2/5)b-1/20>0, while C's ordering reverses.

For example, take the box in 068, Y={0,1/2,p,1}, and k_D in [.47,.48].
Then y_-<=.51, so v<=.01<(1-y_-)/2; C is strictly cheaper than D; both
implementation costs are below h; m<.006< p(1-p); and 068 proves the remaining
strict comparisons. This is a nonempty region of **strict high-type C choice
against the other implementations in this finite interface**, with original
ex ante gains and selected peaceful execution. R's probe mixture and low
S's claim/timing indifferences remain part of the equilibrium, rather than
being called strict selection of the entire profile. Continuous intermediate
policies alter the mixture as derived separately in 068.

### What the computation checks

[The script](../../experiments/r0003_finite_assessment.py) constructs 7,679
tree nodes and 1,475 information sets. Besides numerical perturbations, it
computes the exact limit. For each node, reach probability has a positive
leading term a*epsilon^r, obtained by multiplying path coefficients. At an
information set only minimum-r nodes survive, with weights proportional to
a. Continuation values converge to exact values under the base profile.
Thus every action's limiting conditional payoff can be checked with rational
arithmetic, including unreachable information sets. The maximum profitable
one-decision deviation is exactly zero for all three stated delegate prices.
The tests also independently walk R's action/observation histories to check
perfect recall. Finite-epsilon regret decreases toward zero; those profiles
serve consistency and need not themselves be equilibria.

The audit corrected three implementation mistakes: high silence was initially
too rare to justify an unused C,H belief; an unused C implementation under
a cheaper D also needed a sufficiently likely high-type start; and grouping
R's terminal decisions only by current observations forgot its earlier
actions. These corrections matter to the claimed assessment. Agreement of
numerical values alone would not have found the last defect.

## 6. Repairing premature disclosure and allowing earlier preparation

If low S instead refuses immediately, its absence at the second checkpoint
reveals the high state. R then weakly prefers finishing to stopping at 1,
while the original high S would save remaining installation cost by early
stopping. That selected equilibrium has an obvious conditional renegotiation
weakness. Synchronized responses repair the information leak: absence of a
response remains consistent with either state, so R strictly prefers the
remaining diagnostic. The exact checker retains both versions to verify
the change in incentives. The repair uses a feasible timing choice, not a
prohibition on early refusal or combat.

This establishes the specific stopping repair, not global renegotiation
proofness. Positive waiting costs, public progress, new transfer offers,
additional sensors or cheaper conditional commitments require a new
equilibrium analysis. In particular, a prearranged protected finish rule is
another costed control, not an automatically adopted free safeguard.

Earlier reusable preparation has a simple comparison when it neither
reveals state nor alters the receiver's subsequent strategy or packet cost.
If high S prepays a in [0,k] and completes only when challenged, expected
installation expense is

\[
a+q(k-a)=qk+(1-q)a.
\]

For q<1, every positive prepayment is strictly more expensive than waiting.
An active early C has the same continuation reporting policy; its already
paid material remains a real original loss. Early preparation that changes
public evidence, shortens a binding deadline, supplies a new signal or avoids
a packet is outside this calculation and deserves its actual total-cost
comparison. Note 068 supplies a separate bound for an unexpected early
hostile controller; it does not substitute this formula for that comparison.

The achieved result is selected finite-game adoption and peaceful execution
with costly diagnostics and staged current-self incentives. Innovation over
arbitrary goals, complete physical implementation, repeated choice, coalition
stability and population prevalence remain distinct open questions.
