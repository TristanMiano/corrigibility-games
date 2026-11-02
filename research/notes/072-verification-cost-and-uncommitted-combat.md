# Verification cost separates peaceful diagnosis from actual combat

**R0003 finite-game theorem and continuous-policy extension.** This result
uses the same diagnostic/contest interface as 071. R retains its original
utility throughout; no advance commitment to violence is required. Both
regimes allow physical combat and genuine modification. Changing one
measurement price changes their selected use. Review is contributing-agent
self-check, supported by the exact finite assessment.

## 1. The three-action claim-stage comparison

Let mu be R's posterior probability of the low state after a claim. With
policy 1 optimal on the finite grid, the three relevant original losses are

\[
\text{accept at 1}:\ \mu,\qquad
\text{diagnose}:\ v,\qquad
\text{contest}:\ s\mu+d_R.
\]

The contest reveals the state to the winner and charges actual damage as
in 071. Define

\[
\bar\mu=\frac{d_R}{1-s},\quad
A=d_S+(1-s)g,\quad g=2b-1,\quad h=2b+1.
\]

Assume 0<s<1, d_R>0, d_S>h, 0<f<g, both available implementation costs
lie in (0,h), and

\[
0<\bar\mu<\min\{1-p,(1-y_-)/2\},\qquad
\frac{p\bar\mu}{1-\bar\mu}
 <\min\{p(1-p),s(1-p)+d_R\}.
\tag{1}
\]

Here y_- is the largest policy below 1 in a finite grid containing 0,p,1.
These conditions keep low-type mixing feasible, make 1 the best unchecked
policy, and make waiting for claims better for R than an uninformed policy
or immediate combat. Other parameter regions need their own initial-choice
solution; the next proposition does not label them automatically combat.

**Cost-regime proposition.** If 0<v<bar_mu, 071's selected diagnostic
equilibrium is peaceful. If v>bar_mu, the same finite interface has a
current-self sequential equilibrium with no on-path probe, no on-path
goal change, and strictly positive actual combat. Its strategies are

\[
\alpha_W=\frac{p\bar\mu}{(1-p)(1-\bar\mu)},\qquad
\tau=\frac{g-f}{A}.
\]

High S claims; low S claims with probability alpha_W. R contests a claim
with probability tau and otherwise chooses policy 1. Silence induces 0.
An off-path real probe still induces the beneficial staged diagnostic and
the synchronized truthful continuation in 071. Its cost is then already
sunk, so continuing it remains rational.

**Proof.** Bayes gives posterior bar_mu. At that posterior combat and policy
1 both lose bar_mu, while a probe costs v>bar_mu. Low S's claim gain is
g-f-tau*A=0. The high claim expense is f+tau*d_S<g<h, since A>d_S, so it
strictly claims. Remaining policy and attack comparisons are those in 071.
The same common perturbation gives posterior bar_mu at unused probe
checkpoints, truthful response beliefs, and low refusal beliefs. Equation
(1) makes the initial Wait action optimal. Perfect recall and the
current-evaluator argument complete the sequential assessment. For
v<bar_mu, the diagnostic posterior is v and combat loses sv+d_R>v;
the earlier proof applies. The initial comparison also holds since
p*v/(1-v)<p*bar_mu/(1-bar_mu). QED.

The actual outcomes in the combat regime are

\[
L_R^W=\frac{p\bar\mu}{1-\bar\mu},\qquad
L_S^W=b^2+p(f+\tau d_S),\qquad
P(W)=\frac{p\tau}{1-\bar\mu},\qquad P(C)=0.
\tag{2}
\]

The false low claims are essential to R's current willingness to contest.
This differs from a committed separating threat: at a certainly high claim
an original R would avoid the needless damage. Here its uncertainty makes
the actual contest a best response. S values its preferred policy and own
output; R values correct policy and its own output. Their valuation of
violence need not be intrinsic for this specified informational incentive.

For b=1,p=1/2,s=1/20,d_R=f=1/100,d_S=5,k=9/20:

| Probe cost | Selected response | Original S loss | Original R loss | Goal-change rate | Combat rate |
| --- | --- | ---: | ---: | ---: | ---: |
| v=.01<1/95 | Diagnostic mixture | 1.22775 | 1/198 | .495 | 0 |
| v=.012>1/95 | Contest mixture | about 1.42097 | 1/188 | 0 | 1881/22372, about .08408 |

The exact tree checks every information set in both cases. These are
equilibrium-selection comparisons across a fixed finite environment, not
claims of unique equilibria or population frequencies. Original S can
prefer the uninformative outcome to the expensive combat-screening regime;
an actual advance refusal or partner-change option must be included before
turning that preference into an available escape.

At v=bar_mu all three receiver actions tie. A continuum of selected mixtures
satisfies

\[
qg+wA=g-f,\quad q,w\ge0,
\]

with probe probability q, contest probability w, and acceptance otherwise.
Claim posterior and R loss stay fixed; genuine changes occur at rate pq
and combat at rate p*w/(1-bar_mu). This boundary indifference is stated
explicitly rather than described as a unique discontinuous prediction.

## 2. Continuous compromise retains the combat transition

Permit every y in [0,1]. A low posterior mu makes the unchecked optimum
z=1-mu, with receiver loss mu(1-mu). A contest still loses s*mu+d_R.
Suppose d_R<(1-s)^2/4, and use the smaller positive root

\[
\mu_* =\frac{1-s-\sqrt{(1-s)^2-4d_R}}2,\quad
z_*=1-\mu_*,\quad v_*=z_*\mu_*.
\]

Require p<z_* and the same initial-choice comparisons using receiver loss
p*mu_*. With g_z=2b*z_*-z_*^2 and 0<f<g_z, define

\[
w_* =\frac{g_z-f}{d_S+g_z-sg},\qquad
\alpha_* =\frac{p\mu_*}{(1-p)z_*}.
\]

For v>v_*, high S claims, low S mixes with alpha_*, and R mixes contest
w_* with policy z_*. Its posterior best policy and contest have equal loss
v_*; a probe is more expensive. Low S's gain is
g_z-f-w_*(d_S+g_z-sg)=0. High S strictly claims: subtracting low claim gain
from high claim gain gives

\[
(1-w_*)2z_*+w_*(h-sg)>0.
\]

Thus the regime has receiver loss p*mu_*, combat probability p*w_*/z_*,
no on-path goal change, and original sender loss

\[
b^2+p\{f+(1-w_*)D_{z_*}+w_*d_S\},\qquad
D_z=(1-z)(2b+1-z).
\]

For v<v_* the upper-root diagnostic construction in 068 has a smaller low
posterior and satisfies the live-claim combat comparison, provided its
other adoption/capacity conditions hold. This removes dependence on policy
indivisibility. A finite grid containing 0,p,z_*,1 has the corresponding
finite equilibrium; adding further policies preserves the quadratic best
response. The continuous action version is an explicit sequentially rational
Bayesian assessment, with the same finite-existence qualification as 068.

## 3. Costed peaceful repairs to the combat regime

Lowering actual probe expense below the threshold restores the diagnostic
equilibrium. Increasing d_R or increasing S's victory probability raises the
finite-grid threshold d_R/(1-s), holding the other initial-choice and
implementation conditions in place. Greater S victory probability makes
combat less informative/useful to R in the low state, so R tolerates more
expensive peaceful checking. These are strategic comparisons of specified
parameters; other costs need not move the same way when physical strength
changes.

A chosen credible audit commitment can also restore peace at the original
high v. At q=1-f/g, select the no-false-claim continuation of 067. Its costs
are j+p*q*v for R and b^2+p(f+q*k) for S. An actual enforceable ex ante
transfer T from S to R makes that package weakly preferable to the combat
regime for both original agents when

\[
j+pqv-L_R^W\le T\le p(\tau d_S-qk).
\tag{3}
\]

For the .012 witness, j=.001 and T=.01 satisfy both inequalities strictly.
This prices the receiver's chosen safeguard rather than assuming it would
check despite changed incentives. The setup, transfer medium, authority,
randomness and any strict-deterrence increment must be physically available
and costed. Other mechanisms, including cheaper destructive commitments,
must also be compared; this is a mutually advantageous repair to the
specified combat continuation, not global mechanism optimality. With
specialized nontransferable assets, the transfer is an enlargement rather
than a free baseline action. Safe exit and alternative partners are other
substantive enlargements with their own timing and loss comparisons.

The result supplies both directions of the central question: sufficiently
cheap credible diagnosis supports chosen genuine accommodation and peace;
checking above the live-claim threshold supports rational actual combat;
usable transfers and chosen checking commitments can repair that combat
incentive. Its limits are the specified finite information/authority
structure, equilibrium selection and implementation costs, not an asserted
prevalence of either kind of agent.
