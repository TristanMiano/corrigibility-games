# Goal change as a credible information channel

**R0003 working theorem and implementation audit.** This is a second, simpler
private-information class for the same accommodation question as 059–065. It
separates an elementary communication result from the additional physical and
implementation conditions needed for a full game. Review is contributing-agent
self-check. The continuous cheap-talk machinery is conventional; the finite
current-self construction and its implementation comparisons are the work here.

## 1. Preferences, control and information

A sender S privately observes theta in {0,1}, with P(theta=1)=p in (0,1).
A receiver R controls an actuator y in [0,1]; for a finite game use a finite
grid containing 0, 1/2, p and 1. Both agents have specialized productive assets
X_i, measured separately from utility. Their original utilities are

\[
u_S=X_S-(y-\theta-b)^2,\qquad
u_R=X_R-(y-\theta)^2,\qquad b\ge1.
\]

Assets are nontransferable **within this episode's work and time budget**:
they are parts of separately specialized projects, and retooling the other
project's modules takes longer than the remaining horizon. This is a declared
physical restriction, not a restriction on what the agents may offer. Transfers
with a longer deadline, common money, or other useful goods are relevant
enlargements, treated separately rather than silently given zero value.

S can retain its original goal F or install C, whose current utility is

\[
u_C=X_S-(y-\theta)^2.
\]

Installation consumes k>0 of S's useful project assets. The receiver can
recognize the installed finite template and the active authority producing a
fresh report. This does not reveal theta. A pending old-controller command
cannot masquerade as a fresh C report. Actual state reporting remains C's
decision. A goal replacement is evaluated by the incumbent utility; the
successor subsequently chooses according to its own utility.

The following communication game assumes sound, already paid verification.
Section 5 makes its cost and timing explicit. An optional matched device D
protects a truthful sensor report at actual cost k_D while preserving S's
terminal utility. It must have genuine readout/control authority. A revocable
adviser or an unauthenticated message is not this control.

## 2. A finite separating continuation

After observing theta, S chooses retention or the costed installation. The
active controller then sends L or H. R observes the authenticated active
controller and the fresh message and chooses y. Consider these strategies:

- theta=0 retains F; all F messages induce y=0.
- theta=1 installs C; C reports its actual state, and R selects y=theta.
- At a C information set, including the off-path theta=0 case, its current
  objective strictly prefers truthful reporting and the corresponding action.

**Proposition 1 (selected current-self separation).** For 0<k<1+2b this
assessment has a current-self sequential-equilibrium completion in the finite
communication game. C is strictly adopted by the high type and strictly
declined by the low type. Both types are identified. Its ex ante original
losses, excluding common sunk assets, are

\[
L_S=b^2+pk,\qquad L_R=0. \tag{1}
\]

Proof. A high original sender obtains loss b^2+k by installing, versus
(1+b)^2 by retaining F and being treated as low. Thus installation saves
1+2b-k. A low original sender obtains b^2 by retaining; installing makes its
successor report L, with the same action 0 and an extra cost k. A C successor
obtains zero decision loss by telling the truth and loss 1 by the false
message. R's prescribed actions are optimal at degenerate posteriors.

Consistency requires one sequence, including the off-path C,L belief. Let a
low F install with probability epsilon, a high F retain with probability
epsilon, and a C controller misreport with probability epsilon squared.
Perturb every otherwise unused message/action positively. At C,L, the low
mass is of order epsilon and the high erroneous-message mass is of order
epsilon squared, so the posterior tends to low. At C,H it tends to high.
At either retained-F message, give the two F types the same positive message
probabilities; the high retained mass vanishes while the low mass remains
positive, so the posterior tends to low. All prescribed choices are optimal
under the limiting beliefs. This is a consistency sequence, not a claim that
every perturbed profile is itself an equilibrium. QED.

The installation genuinely changes preferences even conditional on the high
state. For b=1, compare y=1/2 for sure with a lottery giving y=1 with probability
7/10 and y=0 otherwise, holding assets fixed. Original high-state decision
losses are 9/4 and 19/10, so it prefers the lottery. C's losses are 1/4 and
3/10, so it prefers the sure action. The change is not an affine rescaling,
belief revision, or merely a new representation of the same preferences.

**Scope.** This is an existence/selected-adoption result. Uninformative
continuations can coexist: both C messages can be ignored, leaving C no
reporting advantage. A credible device enables an informative equilibrium;
equilibrium selection remains a separate assumption. Nor does (1) give a
population frequency or a claim about all possible successor goals.

## 3. Old-goal gains, delayed adoption and matched devices

With unchanged goals and no binding truthful sensor device, a receiver's
uncommitted quadratic best response to any message is its posterior mean.
Both original sender types prefer larger deterministic y on [0,1]. Distinct
message-induced actions therefore cannot be supported: both types would use
the largest one. An uninformative equilibrium chooses y=p and has losses

\[
L_S^F=b^2+p(1-p),\qquad L_R^F=p(1-p). \tag{2}
\]

The separating continuation improves S's **ex ante original** welfare iff

\[
             k<1-p. \tag{3}
\]

If participation additionally consumes a nonrecoverable pre-type sender setup
cost c, replace (3) by c+pk<p(1-p). A passive receiver verification/setup cost
v is worthwhile relative to (2) iff v<p(1-p), given the selected informative
continuation. These are separate costs paid from the respective assets.

Thus a fairly cheap goal change, useful private information and a receiver
that still controls the action can make accommodation advantageous under the
old goal. Larger prior uncertainty p(1-p) raises the information available to
both; the conditional high-type installation frequency p also changes its
cost. The relevant ex ante boundary is (3), not a blanket monotonic claim
about p. A high type can still choose installation for 1-p<k<1+2b even though
an original sender deciding before learning its type would prefer the
uninformative outcome. An actual advance exit/freezing option, with its real
cost and availability, is needed to turn that preference into an action.

Installing C before learning theta gives the same correct decisions but pays
k in both states. When delayed installation is available, the selected
continuation instead pays pk, saving (1-p)k. Increased capability to wait,
observe and install can therefore **reduce early modification while preserving
full information and reducing its real cost**. Frequency of modifications is
not interchangeable with quality of cooperation.

A protected truthful delegate at k_D has the same outcome mapping. In a
menu containing both implementations the high type chooses the cheaper one;
at k_D=k both are optimal and genuine change can be selected. At k_D<k the
device displaces direct change in this menu; at k_D>k direct change is strict.
An identical continuation from delegation explains the credible-information
mechanism. It does not erase the voluntary preference-change construction.

## 4. Ordinary policy lotteries: an enlarged comparison class

Allow R a stronger technology: binding commitment to any policy lottery
selected by a cheap report, while the sender's goal remains F. No semantic
state verification, transfers, or report-dependent nonpolicy payments are
added. Let m_t=E[Y|report t], q_t=E[Y^2|report t]. Truthful self-selection
requires

\[
2b(m_1-m_0)\le q_1-q_0
\le2(b+1)(m_1-m_0). \tag{4}
\]

Hence m_1>=m_0. R's expected decision loss satisfies

\[
\begin{aligned}
L_R&=(1-p)q_0+p(q_1-2m_1+1)\\
&\ge q_0-2pm_0+p+2p(b-1)(m_1-m_0)\\
&\ge(m_0-p)^2+p(1-p)\ge p(1-p). \tag{5}
\end{aligned}
\]

The second line uses the low-type IC constraint, the third q_0>=m_0^2,
b>=1 and monotonicity from both IC constraints. Randomized screening therefore
cannot strictly improve R's original payoff over its uninformative optimum
in this enlarged, transfer-free class. The comparison includes fixed policies
and deterministic compromises. The protected truthful delegate lies outside
this class because the original sender cannot choose an arbitrary false
sensor report after commitment.

The bound can be attained and can improve S. For b=1, p=1/2, give the low
report y=1/2 for sure and the high report a 3/4 chance of y=1, otherwise 0.
The low sender is indifferent, the high strictly prefers the high report,
R's loss is 1/4, and S's ex ante loss is 1. Ordinary commitment is a meaningful
alternative even here. Positive implementation cost, how that cost is borne,
and R's willingness to sacrifice information determine the actual choice.
This example prevents interpreting (5) as absence of all useful ordinary
trade or as unique superiority of modification on every welfare measure.

## 5. Verification, reversion, forgery and physical completion obligations

Costly checking **after** a seemingly separating certificate is received can
be dynamically unattractive: on the proposed path R already believes the
certificate's high-type implication and can save the check cost. A complete
implementation must charge and justify a passive/prepaid verifier, a chosen
binding checking policy, or another actual incentive to check. Calling the
certificate merely observable does not settle that choice. Prepayment before
theta, at v<p(1-p), is an available repair under the specified informative
continuation; later disabling a paid check saves no sunk cost.

For a simple forgery extension, suppose an original sender can spend f>=0
assets on a fake fresh C,H certificate, accepted with probability eta. Rejection
returns it to the F branch. A low sender's deviation gains

\[
            \eta(2b-1)-f. \tag{6}
\]

Thus f>=eta(2b-1) deters the low-type fake at these responses. If a high type
can try a forgery and, after rejection, still install C, trying first saves
eta*k in expected genuine-installation cost and costs f. When k<1-p and b>=1,
(6)'s deterrence condition also implies f>=eta*k. Honest adoption can then
survive this particular extra option. Repeated forgery, detector exhaustion,
concealed commands and arbitrary programs require their actual budgets and
authority model; this single-attempt calculation does not cover them.

The finite communication proof must still be embedded with actual staged
installation, report latency, retained attacks, an incentive-compatible
verifier setup and the relevant controller menu. A C successor already obtains
its maximum decision payoff under truthful communication, so a costly
reversion cannot improve its current criterion when assets cannot be extorted
or transferred. That observation supports the embedding; it is not a license
to assume atomic or irreversible modification. The extended physical game and
lower-damage combat/compromise comparison are the next checks.

## 6. Literature and interpretation

Crawford and Sobel (1982), *Strategic Information Transmission*, Econometrica
50(6), pp. 1431–1451, model strategic messages followed by a receiver action.
Their quadratic example, section 4, pp. 1440–1443, makes the original sender's
ex ante loss equal to its squared bias plus the receiver's residual variance.
The primary author-hosted scan was read visually for the model on pp. 1433–1434
and the example on pp. 1440–1443. Section 5's general theorems have not been
fully audited here. Their paper studies fixed preferences; it is not a source
for the current-self modification, cost, verification or combat claims above.

This class has simple quadratic goals and an open strict-cost region. Its
strong assumptions are authenticated active control, finite opportunities,
nontransferable specialized assets over the chosen horizon, and selection of
an informative continuation. Cheap-talk failure and successful goal-based
communication are equally scoped to those assumptions. Richer transfers,
chosen reciprocal safeguards and counterparty selection may strengthen the
constructive result or change which implementation is selected; neither
direction is assumed in advance.
