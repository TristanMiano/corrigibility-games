# Continuous compromise, credible refusal and diagnostic costs

**R0003 mathematical extension and scope audit.** This note removes the
three-action policy restriction from 067's best-response calculation and
derives a bound against an entire costed class of hostile controllers. The
explicit inspection assessment and its inequalities are proved below. A
claim about a fully specified physical game still needs the interface and
timing conditions listed in section 5. Self-review only.

## 1. The receiver can choose any intermediate policy

Retain the on-demand timing of 067: a claim costs f; initiating a real probe
costs v; a challenged high sender voluntarily pays k to install C; the probe
authenticates a fresh C response. The low sender declines or, if it has
installed C off path, reports its actual low state. Initial utilities and
the genuine-change witness remain those in 066.

Now permit any y in [0,1]. Let z=P(theta=1|claim) be the posterior high
probability. Without a probe, R's unique best action is y=z, with expected
decision loss z(1-z). With the successful diagnostic its decision loss is
zero and its material cost is v. For 0<v<1/4 choose the upper root

\[
z=\frac{1+\sqrt{1-4v}}2,\qquad \mu=1-z,\qquad v=z\mu. \tag{1}
\]

Assume p<z. Define the low type's gain from the uninspected compromise z,
relative to silence and action 0, as

\[
g_z=2bz-z^2>0.
\]

For 0<f<g_z the inspection probability and low false-claim probability are

\[
\rho=1-f/g_z,\qquad
\alpha=\frac{p\mu}{(1-p)z}. \tag{2}
\]

Bayes' rule gives posterior z. R is indifferent because v=z(1-z). Low S is
indifferent because (1-rho)g_z=f. A challenged high F strictly changes when
k<h=2b+1. Its unchallenged decision loss exceeds b^2 by

\[
D_z=(b+1-z)^2-b^2=\mu(2b+\mu).
\]

High S strictly claims when

\[
f+\rho k+(1-\rho)D_z<h. \tag{3}
\]

The original expected losses are

\[
L_R=m_c=\frac{pv}{z}=p\mu,\qquad
L_S=b^2+p\{f+\rho k+(1-\rho)D_z\}. \tag{4}
\]

The low sender's claim expenses again cancel its expected policy gains by
indifference. The high sender bears both possible installation expense and
the shortfall from an uninspected intermediate policy. Its ex ante original
welfare exceeds the uninformative value iff the braces in (4) are below 1-p.
Goal changes occur with probability p*rho, while false claims occur with
probability p*mu/z. With a continuous intermediate policy, a wrong-policy
probability is not the same outcome measure as mean squared decision error.

All policy deviations are checked by the strict quadratic minimization, not
merely by comparing 0 and 1. For a finite extensive game, include 0, p, z and
1 in the policy menu: the same assessment is a current-self sequential
equilibrium, with the common perturbation construction from 067. Adding any
other finite set of policy values in [0,1] leaves the best-response proof
unchanged. The continuous-action version has the same explicit sequentially
rational Bayesian assessment; no general finite-game existence theorem is
silently applied to an infinite action space.

## 2. Calibrated checking can benefit both original agents

Suppose R can credibly commit to an audit probability, at actual cost j.
With no false claims the posterior after a claim is high with certainty, so
the uninspected action is 1. The low type's imitation gain is now
g=2b-1, rather than g_z. Its deterrent threshold is

\[
q_D=1-f/g>\rho. \tag{5}
\]

At q_D the low type is indifferent and can be selected to remain silent;
strict deterrence uses a slightly larger available probability. The selected
threshold implementation has original losses

\[
L_R^K=j+p q_Dv,\qquad L_S^K=b^2+p(f+q_D k). \tag{6}
\]

R gains iff

\[
j<\Delta_R=p\mu-pq_Dv
=p\mu\{\mu+(f/g)z\}. \tag{7}
\]

S also strictly gains whenever 0<z<1 and k<h. To see this, subtract its
committed cost from its uncommitted cost in (4):

\[
\Delta_S=p\{(1-\rho)D_z-(q_D-\rho)k\}
=\frac{pf}{g_z}\left[D_z-\frac{(g-g_z)k}{g}\right]. \tag{8}
\]

Here g-g_z=mu(2b-2+mu). The identity

\[
g(2b+\mu)-h(2b-2+\mu)=2z>0
\]

implies the bracket in (8) is positive for k<h. More frequent goal changes
are outweighed by more favorable uninspected actions for the high sender.
This repairs the inference that stronger checking must burden the sender:
its policy response changes too. The three-action case in 067 has a different
response and gives equality at its threshold; both results are scoped to
their actual action spaces.

For b=1,p=1/2,v=f=1/100,k=9/20:

| Quantity | Value (rounded; equations define exact values) |
| --- | --- |
| Uninspected compromise z | 0.9898979486 |
| Uncommitted inspection rho | 0.9899989794 |
| Original receiver loss m_c | 0.0050510257 |
| Original sender loss | 1.2278513115 |
| R's gross value of threshold commitment Delta_R | 0.0001010257 |
| S's original gain Delta_S | 0.0001013115 |

This is a jointly advantageous chosen safeguard when its real cost fits
(7), subject to the alternative-controller comparison in 067. A much
cheaper destructive screening commitment may still compete with it; the
pairwise gain is not a global optimality claim.

## 3. Public verification failures and capability

Perfect success at opening a diagnostic channel is unnecessary for this
calculation. Let a probe attempt cost c and establish a usable authenticated
channel with probability a>0. Success or public erasure is known **before**
S decides whether to pay for installation. On success the same diagnostic
runs; on erasure R uses its uninspected action. A probe's effective cost per
successful opportunity is

\[
                         v_{\rm eff}=c/a. \tag{9}
\]

Use v_eff in (1), and let an attempt occur with probability rho/a. If a>=rho,
this is feasible and the resulting effective inspection probability is rho.
The low-type IC, the receiver indifference condition c=a*z*(1-z), and the
current-self adoption calculation are unchanged. Actual goal changes still
occur only on established, challenged high branches, with probability p*rho.

This models an erasure, not false authentication. A detector that accepts a
forged controller with positive probability needs the separate imitation
calculation in 066 and a new belief audit. Nor is a failed attempt declared
free. If multiple independent attempts are feasible, their physical costs,
timing and conditional continuation must be charged. Repeated attempts can
raise the total success probability; they do not improve c/a merely by
relabeling failures.

At fixed c, a higher a reduces v_eff and the posterior ambiguity mu in (1),
so it reduces R's expected loss p*mu and low false-claim frequency p*mu/z.
Other costs, including f and the costs of alternative mechanisms, must be
held fixed, and the capacity to attain the required inspection rate must
remain available, for that comparative claim. Better communication/verification is a specified capability, not a
synonym for greater combat strength or universal cooperation.

The original sender also benefits throughout this selected region, despite
more frequent genuine changes. Let H(z)=f+rho*k+(1-rho)D_z be its high-state
expense in (4), and t=b-z>=0. Since
H(z)=f+k+f(D_z-k)/g_z, differentiation gives

\[
H'(z)=\frac{2f}{g_z^2}\{t(k-1-t)-b^2\}<0
\quad\text{when }k<h=2b+1. \tag{19}
\]

For the sign, replace k by h to obtain the upper bound
t(2b-t)-b^2=-z^2<0. Also rho'(z)=2f(b-z)/g_z^2>0 for
the interior z<1,b>=1. Thus lower v_eff raises z, reduces both original
expected losses, reduces false-claim frequency, and raises p*rho. This is
a positive capability comparison under fixed f,k,b,p and the same diagnostic
availability, provided the audit-capacity, adoption and combat inequalities
continue to hold. Peaceful play already has zero combat in this region;
the improved outcome measures are original welfare and informative
accommodation, rather than a further reduction below zero combat.

One initial-choice boundary is explicit. With the same combat outside loss
w_0=s(1-p)+d_R, R prefers this information channel when p*mu<w_0. If
0<w_0/p<1/2, this is equivalent to
v_eff<(w_0/p)(1-w_0/p); when w_0/p>=1/2 it holds throughout the upper-root
region. The live-claim comparison still separately requires
(z-s)*mu<=d_R. It cannot be inferred from the initial-choice boundary alone.

## 4. A bound against uncertified threats

Suppose an unexpected controller H is followed by a receiver decision whose
posterior is concentrated on the low state. The receiver can immediately
contest. With original receiver utility, its loss from that option is at
most

\[
                              r=s+d_R, \tag{10}
\]

because an S winner can cause policy loss at most 1 and an R winner learns
theta and chooses 0. Let H's installation and any binding conditional-action
device cost its original sender at least kappa. No resource transfer can
increase R's material stock during this horizon. Rational R continuation
therefore has expected policy loss E[Y^2]<=r after subtracting already sunk
costs; additional R costs only tighten the inequality.

An original low sender's policy gain is 2b E[Y]-E[Y^2]. Jensen/Cauchy gives,
for 0<=r<=1 and b>=1,

\[
2bE[Y]-E[Y^2]\le 2b\sqrt r-r=:G_b(r). \tag{11}
\]

Its own later costs and combat damage cannot improve this bound. Consequently

\[
                       \kappa>G_b(s+d_R) \tag{12}
\]

strictly rules out an original-low gain from **every** such H continuation,
not just a named attack-reward goal. For the high sender, a diagnostic giving
policy 1 already reaches its maximum policy payoff. Any alternative with at
least the same response cost cannot improve that payoff coordinate. These
are useful complete-menu bounds, provided the actual interface satisfies the
belief, cost and resource conditions; they are not assumed for free.

For a fixed finite policy set, replace G_b by its piecewise linear lottery
frontier. On {0,1/2,1}, for example,

\[
G_b^{\rm grid}(r)=
\begin{cases}
(4b-1)r,&0\le r\le1/4,\\
2b/3+(4b/3-1)r,&1/4\le r\le1.
\end{cases} \tag{13}
\]

This follows by taking the upper concave envelope of the three points
(y^2,2by-y^2). It already allows policy lotteries. Thus policy indivisibility
can strengthen credible refusal, while a richer set of peaceful policies
can enable more concessions. Equation (11) is the conservative bound that
survives all intermediate policy values.

The bound has meaningful failure and repair directions. If a hostile goal
costs kappa below 2ba-a^2 and can credibly demand policy a with a^2<r, a low
original sender can gain by adopting it when R prefers that concession to
contest. This requires actual threat credibility and available policy a;
it is not inferred solely from failure of (12). Stronger refusal, a higher
actual hostile-controller cost, a chosen safeguard, or a different counterparty
can restore the successful region. A cheaper truthful device can also offer
peace while changing which implementation is adopted.

## 5. Conditions for using the bound in a full game

At an off-path uncertified controller, a low posterior must be supplied by
one common consistent belief construction. In a finite interface, suppose
every observable uncertified-controller history accessible to a high type
is also physically accessible to a low type. Give a high type's first
off-path entry probability epsilon^K, a low type's entry probability epsilon,
and subsequent raw-action trembles at least epsilon. Taking K larger than
the finite maximum path length makes low histories dominate at the relevant
receiver information sets. Actual protected state evidence is an exception:
if it physically excludes the low state it belongs to the recognized
diagnostic comparison, not to this likelihood argument.

This construction is useful only where the prescribed entry choices are
optimal. Equation (12) supplies the low-type bound; the maximum-policy and
actual-cost comparison supplies the high-type bound. Current C reporting,
ordinary F claims, initial receiver waiting and all on-path attacks still
need their separate comparisons. Unspecified remaining decision agents can
then use 059's constrained finite-game completion, rather than independently
chosen convenient beliefs. This is a sufficient completion route, not a
claim of refinement robustness or unique off-path expectations.

**Timing and private-state qualification.** The maximum-policy argument
compares alternatives at the same response opportunity. An alternative
installed before the ordinary claim might avoid its packet cost, so its
total cost cannot be compared with k alone. Moreover the receiver's
low-posterior bound E[Y^2]<=r concerns its low-state continuation law. It
does not by itself bound the high state's actual continuation law. Section
8 supplies an explicit counterexample to that attempted strengthening.

There is a simpler valid high-type bound. If an implementation cannot raise
S's stock beyond baseline and costs kappa, the high original sender's gain
over policy 0 is at most

\[
                              h-\kappa. \tag{17}
\]

Hence a sufficient initial comparison, even if the alternative avoids the
ordinary packet, is

\[
                           \kappa>f+qk. \tag{18}
\]

Use the continuous claim expense from (3) in the continuous version. Later
comparisons remove actual sunk costs and use actual incremental prices.
At a challenged response, kappa>=k suffices for the maximum-policy argument;
at an earlier choice it need not. Protected evidence that physically rules
out the low state belongs to the recognized diagnostic comparison. No
belief choice may override it. Same-cost early alternatives need their own
continuation proof rather than this stronger sufficient price condition.

The physical interface must additionally state:

- Which costly signals and state measurements are actually observable, with
  their measurement and response costs. A free observable sacrifice or a
  cheaper truthful device can displace the diagnostic.
- The minimum costs of conditional weapons, binding delegates, goal changes,
  authority transfers and mergers. Calling a cheap tripwire an ordinary
  action does not exempt it from the alternative-menu audit.
- Actual staged installation, a fresh post-change response, the time at which
  probe cost becomes sunk, and the allowed repair/message opportunities.
- Combat's state-revelation assumption, material dispersion, useful work and
  finite recovery deadline; any action that can damage a different amount
  must be included in the bound.
- The horizon over which specialized resources cannot be transferred. A
  longer interaction or usable common medium changes the resource bound.

These are substantive assumptions. The inequalities do not themselves
construct arbitrary-program attestation or an unrestricted physical world.

## 6. An open successful parameter region and its interpretation

For the discrete-policy core, a conservative rectangular region is

\[
\begin{gathered}
b\in[1,1.01],\ p\in[.49,.51],\ s\in[.048,.052],\
d_R\in[.010,.011],\ v\in[.009,.010],\ f\in[.009,.010],\\
k\in[.45,.46],\ d_S\in[4.9,5.1],\ j\in[.011,.020].
\end{gathered} \tag{14}
\]

Let unrecognized alternative controllers cost at least .48 at an early
installation, with the actual live-response lower bounds also checked; let
a matched truthful delegate cost at least k; and impose the stated measurement
interface. The .48 bound exceeds f+qk<=.47 and supplies (18), independently
of the private-state continuation law. It is an additional technology/cost
assumption, not inferred from the cheaper C template. The sender ex-ante
cost is at most f+k<=.47<1-p. The receiver
loss is at most .51*.01/.99<.006, below every j and below its earliest combat
loss .048*.49+.01. More importantly, j>.010>=v also covers a controller
installed conditionally at a live claim, where the remaining receiver loss
is v. The post-claim combat condition has a strict margin since
.01*(1-.048)<.010. Also d_S>2b+1.

For the threat bound, r<=.063. Monotonicity of G_b on this range reduces the
check to b=1.01,r=.063,k=.45. The exact square certificate is

\[
(.45+.063)^2-4(1.01)^2(.063)=30519/5000000>0. \tag{15}
\]

Thus this is an open-margin class, not a single favorable sample. It is not
an empirical distribution of agents. Its exposure is quite asymmetric:
S is weaker in combat and loses much more useful project output in a clash.
Those assumptions help R refuse extortion while S finds truthful
accommodation attractive. They should be described as consequential,
potentially engineered conditions, not silently called typical.

Balanced strengths can also fit the same bound when the high state is rarer
and the implementation cost fits the remaining interval. For b=1 in the
discrete-policy calculation, a cost k can satisfy both (12) with kappa=k and
the ex ante condition exactly when

\[
s+d_R<\left(1-\sqrt{\frac{p}{1-f}}\right)^2,
\qquad p<1-f, \tag{16}
\]

apart from the other explicit inspection/combat conditions. Derivation:
the upper adoption cost is (1-p-f)/(1-f)=1-p/(1-f); invert the increasing
function 2*sqrt(r)-r. This shows how the prior, combat leverage and costs
jointly delimit the protected diagnostic region. A rare-state balanced-power
case can improve information while its unmodified baseline already remains
peaceful; it should not be reported as a reduction in combat.

The continuous-policy core has the different cost expression (4), which
also admits an explicit certificate throughout (14). Set
u=10103/1000000. The exact inequality u(1-u)>.01 and monotonicity on
[0,1/2] give mu<u whenever v<=.01. Consequently z>1-u,
g_z>=1-u^2>.99, f/g_z<.011, and D_z<u(2.02+u)<.021. Therefore

\[
f+\rho k+(1-\rho)D_z<.47+.011(.021)=.470231<.49,
\]

while p*mu<.51u=.00515253 and (z-s)mu<.952u=.009618056<.01.
The initial-combat, conditional-control and low-threat bounds retain their
strict margins. The .48 early-controller cost exceeds .470231, supplying
the corrected high-type comparison (18). Thus the continuous-policy **core
inequalities and stipulated controller bounds** hold over this rectangle as
well. This certificate does not eliminate section 5's missing full-interface
obligations, and (16)'s exact discrete cost frontier is not reused as an
exact continuous-policy frontier.

## 7. A usable safe exit can replace asymmetric combat exposure

The threat bound has a more general source than combat strength. Suppose
R has an actual refusal action at an unexpected-controller decision that
secures original expected loss at most r, with r in [0,1]. No positive
transfer to R is available in this specialized-asset comparison. Rational
continuation then again gives E[Y^2]<=r at a limiting low-state posterior,
and the low-type bound G_b(r)-kappa follows exactly as before. A high-type
comparison requires (18) or an independently justified statewise bound.
The refusal may be a contest, a usable exit, or a genuinely available
alternative partner; its physical date, costs and continued control matter.

For a concrete enlargement, allow R to close this interaction and secure
policy 0 at output cost e, before a later launch can reach the actuator.
This is an explicit physical escape, distinct from ordinary Set:0, which
still leaves S an attack response. Escape ends control over this episode;
combat remains possible at the preceding live choices. If a threat can
arrive before escape completes, the option supplies no such guarantee.
At a low posterior this refusal has loss e, so r=min{s+d_R,e} can be used.

The diagnostic's on-path equilibrium is preserved: after a claim, exit
loses 1-v+e rather than v; initially it loses p+e rather than m; after a
verified response it is worse than the correct policy. During a paid probe
it also loses the value of the remaining information. For e>0 these
comparisons are strict under the witness parameters. The extra option is
available but is not used to delete on-path combat or force agreement.

For example b=1,p=1/2,f=v=.01,k=.45,k_D=.47,e=.05 works with **equal
combat damages d_S=d_R=5 and any interior strength split**. The finite core satisfies
071's comparisons; the low-threat certificate is

\[
(k+e)^2-4e=.05>0,
\]

so k>2*sqrt(e)-e. For an early unrecognized alternative, a cost at least
.46 exceeds the ordinary high claim expense .4555 and supplies (18).
The exact finite assessment also passes when the
physical escape action is added, at equal strengths. The statement across
strengths follows from the displayed bounds, not a sample count. The
unexpected-controller extension still requires the common-belief and actual
interface conditions of section 5.

This variant shows which assumption substitutes for favorable combat
exposure: a sufficiently cheap, timely safe refusal. It does not establish
that such escape is typically available. It supports genuine accommodation
in an environment whose original baseline already favors peace, rather
than claiming an additional reduction in combat there. A slower exit,
cheaper seizure or more valuable lost project can restore the threatening
controller's advantage and needs its actual comparison, as in 062.

## 8. A low-state belief bound is not a high-state payoff bound

The following audited counterexample explains why (18) uses actual total
cost. It concerns a continuation after an unexpected active H, not a claim
that every initial implementation of H has been physically completed.
Let b=1,s=.05,d_R=.01,d_S=5. R believes theta=0. A finite history preference
can make H choose the following responses: in the low state it attacks after
every offered policy, then if it wins chooses 0 following offer 1 and chooses
1 following any other offer or an immediate receiver contest. In the high
state it accepts offer 1. A bounded material term plus a sufficiently large
finite reward for these actual conditional choices implements the responses;
the template uses its protected state but does not disclose that state.

R strictly prefers offering 1: under its low-state belief the ensuing
contest leaves policy 0 regardless of the winner, so R loses only d_R=.01.
An immediate contest or another offer loses s+d_R=.06. Thus its rational
low-state continuation satisfies E[Y^2]=0<=r, yet the actual high H accepts
and obtains Y=1. The claimed transfer of that moment bound to the high
state is false. A simple high-type bound G_{b+1}(r)-kappa would be invalid.

If this early H is actually available for kappa=.45 and avoids the normal
claim packet, the high original sender's loss 1.45 is below the diagnostic's
conditional loss 1+.01+.99*.45=1.4555. The low original sender instead
loses 1+5+.45 and will not choose it. This alternative can be another
instrumentally chosen genuine goal change with peaceful actual high-state
play; it challenges the particular C implementation's optimality, not the
constructive accommodation hypothesis. Its initial implementation, other
available proposals and common assessment still need their own audit.

Condition (18) blocks the saving without conflating the private-state laws.
A same-cost enlarged-menu theorem remains open unless it supplies stronger
implementation or statewise continuation structure. The explicit finite
core in 071 and the low-type bound (11)–(12) do not depend on the invalid
high-type inference and remain intact.
