# A consistent staged assessment and its controller-completion conditions

**R0004 proof audit.** The finite staged core is checked analytically below
and by the exact tree in `experiments/r0004_staged_assessment.py`. This is
contributing-agent self-check, not independent verification or a proof
assistant certificate. The richer-controller statement has explicit extra
conditions; the finite checker alone does not establish them.

## 1. What the checked tree contains

The tree has original S, actual C_a, a possible protected truthful delegate
D, and the receiver's declared current R_a evaluator. Its terminal coordinates
separately retain original S loss, C_a loss, current R_a loss, original R
loss, actual C activation and combat. A predecessor's installation choice
uses original S loss; its successor's report uses C_a loss. D preserves
original S preferences and restricts the protected report by actual binding
authority, while refusal and attack remain available.

R initially chooses a policy, attacks or waits. S claims, remains silent
or attacks. Each requested frame charges r_i and opens S's begin/refuse/wait/
attack choice. R can interrupt halfway with a policy or attack. A started
sender can then complete, abort or attack; an unstarted sender can make a
late, incomplete and costly attempt. Completed prefixes are public. The
last completion activates C_a or D before a fresh report is chosen. Every
policy still leaves S an attack response. Contest winners explicitly choose
their policies using their actual evaluator. All R information sets retain
the whole prior public observation/action trace, including interruptions.

The physical variant uses 076's finite recovery calculation and clock,
including final shipping time. Recovery has been analytically optimized
over repair/refusal under every core evaluator's increasing own-output
term; it is not an additional strategic oracle. The final dispatch/launch
race in 076 explains why another newly installed controller cannot affect
the already departing stocks and policy. Early new controllers remain a
distinct enlargement discussed below.

For the default three-stage witness, both constant-damage and physical
variants have 3,033 nodes and 635 information sets, with maximum exact
limiting conditional regret zero. Their original sender loss is
1913613/1600000, original receiver loss 269101/53461798, actual C probability
28611/80000 and combat probability zero. Costlier request frames at .004
each give actual combat probability 1881/22372 and no on-path C activation.

## 2. One common belief sequence

At each unused receiver action use probability epsilon. At each unused
low sender action also use epsilon. At each unused high sender action use
epsilon^K, except that a valid, unused recognized C/D installation starts
with epsilon. Positive prescribed probabilities are scaled by one minus
the total assigned tremble mass. Choose K larger than the finite tree's
maximum number of ordinary tremble factors; the implementation uses K=100+10N, above the at most 4N+12
ordinary decision factors on a path in these declared kernels. It is one completely mixed behavioral sequence.

On-path Bayes beliefs are exactly the formulas in 073/075. Low refusals
dominate high refusals. An off-path low C completion requires a start and
a finish tremble; its truthful L then dominates a high C's false L with
exponent K. Conversely, even when a cheaper D is selected, an unused high
C start has order epsilon and its truthful H dominates a low C completion
and false H, which require at least three ordinary trembles. Thus both
recognized templates receive correct limiting response beliefs.

The last exception is essential. The first attempted sequence suppressed
an unused high C start by epsilon^K when D was cheaper. It then incorrectly
made a protected C:H look low. The whole-tree check found receiver regret
one at that information set. Assigning ordinary tremble weight to valid
recognized installation alternatives repairs the sequence. This correction
preserves the explicit cheaper/equal/dearer delegate comparison.

The exact audit multiplies each path's leading coefficient and exponent,
normalizes the minimum exponents in each information set, and evaluates
every available action under the appropriate current criterion. Finite
epsilon members give decreasing maximum conditional regret as epsilon
shrinks. Consistency does not require these perturbed profiles themselves
to be equilibria.

## 3. Sequential rationality, including interruptions

The checkpoint comparisons, low indifference and remaining-cost high
adoption are 073/075's calculations. A halfway receiver has no new
observation and has already spent r_i. Continuing costs no additional
project components and supplies the specified information or pooling
continuation. Its own later contest is no cheaper after spending work and
time. Hence Continue is optimal, including weak continuation in a pooling
off-path branch.

A low sender who has started an intermediate prefix now pays only half
c_i to reach continuation value c_i, so completes strictly. A low sender
who accidentally starts the final C frame instead aborts: truthful C
cannot improve its policy over refusal and completion has a positive
remaining cost. High completion follows the backward remaining-cost
argument, including histories with large sunk prefix expenses. A late
start cannot complete within the hardware's remaining work/time window and
therefore wastes components. Fresh C reports are optimal under C_a; a
protected delegate supplies its actual report. Finite sender damage rules
out voluntary attacks in this core. After a verified report or refusal,
R's declared policy is its posterior optimum, and an additional contest
only adds damage. Contest winners choose their current ideal policies.

Initial waiting must satisfy 073's explicit uninformed-policy and contest
comparisons. The finite-grid condition remains real: adding .99 to the
default a=0 grid makes policy 1 suboptimal and produces positive regret.
Positive a with mu_1<=a instead supports policy 1 against every intermediate
policy. This limitation is retained, not hidden by a numerical grid.

## 4. Increasing physical damage and an unexpected request

Let mu_i^* be the backward threshold using the actual public checkpoint's
effective damage. An on-path or unexpected checkpoint can have prior
pi<=mu_i^*. If pi<mu_i^*, select policy 1. After an unexpected request,
set the next progress posterior to min(pi,mu_{i+1}^*). If this equals pi,
both original types advance and the next receiver accepts at 1. If it is
smaller, high advances and low mixes by Bayes' formula. At the final
request low refuses.

The expected request loss in excess of the high-state minimum is

\[
r_i+D\frac{(1-\pi)\min(\pi,\mu_{i+1}^*)}
 {1-\min(\pi,\mu_{i+1}^*)}.
\]

For pi<mu_{i+1}^* this is r_i+pi D, strictly above accepting. Otherwise
its crossing with pi D is the threshold in 075. The contest crossing is
d_R/(1-s). This proves the accepting continuation below the threshold
and avoids the invalid advancement probability above one that would result
from blindly imposing a larger later posterior. The physical combat
fixtures explicitly exercise this case.

## 5. A sufficient price bound for additional controllers

This is a conditional extension beyond the checked tree. Suppose a public
unexpected sender controller supplies no protected evidence of theta and
can be met by a receiver refusal whose actual expected loss, at theta=0,
is at most r. No net transfer or extra project stock can be created in the
remaining episode. If the receiver still uses R_a when it first responds,
its optimizing continuation, including any later self-modification, obeys

\[
E[(Y-a)^2]\le r.
\]

Writing B_S=b-a and assuming r<=B_S^2, the low original sender's policy
gain is at most

\[
G_{B_S}(r)=2B_S\sqrt r-r.
\tag{1}
\]

This follows from E[Y-a]<=sqrt(E[(Y-a)^2]) and monotonicity of
2B_S sqrt(x)-x on the stated interval. A **remaining** implementation
expense kappa>G_{B_S}(r) blocks profitable low adoption. A high sender
already receives its best available policy 1, so a remaining expense
larger than its prescribed remaining expense blocks high adoption without
using a low-posterior bound for a high-state outcome. That distinction
preserves the correction made in 068.

For the receiver, any new controller costing at least the largest current
excess loss T_1 cannot improve its on-path current payoff, provided it
cannot acquire an additional transfer or create output. The statewise
policy minimum supplies the upper bound. Before the claim its remaining
excess is smaller; after paying a requested frame it is smaller again.
These are live incremental costs, not charges artificially repeated from
the start of the project.

The price condition must cover the **first effective transfer of control**,
including a binding weapon latch, an authority-bearing delegate or a
reused partial implementation. Earlier C costs are sunk and cannot be
charged again to a late alternative. Private preliminary work cannot
obtain a concession before it changes observable authority. If preliminary
work is public while the original sender is still in charge, the receiver
must have an actual opportunity to terminate before the new controller
can launch; 076's dispatch race can supply that opportunity. A device that
already binds the weapon midway counts as active then, at its actual cost.

For a finite enlarged program set, a completion argument can preserve the
supported mixed path: impose its probabilities, put higher-order trembles
on high first departures into unrecognized controllers, and optimize the
remaining finite off-path game. Every low-reachable public controller
history then has a low dominating path unless it contains genuine protected
high-state evidence. The original low and high bounds above rule out first
departures on path; current C's optimal outcomes and receiver cost bounds
cover their on-path changes. Protected evidence and recognized C/D starts
retain their separately correct beliefs. This requires the actual finite
observation/authority conditions just stated. It is not an assertion that
all programs in an unrestricted world satisfy them.

## 6. What the bound establishes and what it leaves to test

The physical core has a complete finite current-self sequential assessment.
The larger price-bounded program class has a conditional completion route;
its premise must be checked at every live opportunity. In particular,
recovery losses rise near the deadline, and reusing partial construction
can lower a new controller's incremental cost. Either can invalidate (1).
The next note tests an actual late threatening controller and a chosen
repair, preserving both genuine accommodation and the limiting incentive.
