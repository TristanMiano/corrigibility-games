# Imperfect recognition, partner acceptance and revisable adoption

**R0005 selected-market calculation and repair audit.** This adds uncertain
recognition and privately known installation costs to an implemented service
opportunity. It distinguishes a specified Bayesian continuation from global
selection, and explicitly tests later adoption and rechecking. The signal
error bound is an implementation assumption about the declared template and
fraud class, not a theorem about verifying arbitrary programs.

## 1. Normalize by the actual refusal outcome

A supplier and customer have a funded service offer. Relative to their
actual refusal payoffs, a fulfilled offer gives supplier g>0 and customer
v>0 before the supplier's installation expense. A falsely trusted original
supplier can default, gaining f>g while the customer loses ell>0. A genuine
contractual goal supplies the promised outcome by 097/100's incentive proof.
An original supplier knows its own setup cost k, drawn from the commonly
known uniform distribution on [0,K]. This is a distribution over a declared
implementation cost, not a distribution over arbitrary agents' values.

An actual recognition procedure passes a genuine installation with
probability one and a fraudulent original with probability epsilon in
[0,1). It costs the customer mu. Random errors are not known in advance.
After a pass or failure the customer remains free to accept or refuse.
The original supplier can choose installation, imitation or refusal using
its current original welfare. The baseline of this section permits one
recognition opportunity; sections 4–5 examine relaxing that restriction.

If the customer checks and accepts only passes, initial supplier values
above refusal are g-k for genuine adoption and epsilon f for imitation.
Therefore the adoption threshold and share are

    H=g-epsilon f,
    pi=clip(H/K,0,1).                               (1)

Conditional on a pass, the posterior probability of a genuine installation
is pi/[pi+(1-pi)epsilon]. The customer's expected gains from checking,
trusting without checking, and refusing are respectively

    A=pi v-(1-pi)epsilon ell-mu,
    T=pi v-(1-pi)ell,
    E=0.                                            (2)

Thus the following strict conditions support the stated selected Bayesian
assessment, with both adoption and retention represented:

    0<H<K,
    A>max(T,0).                                     (3)

The pass decision is strictly optimal since A+mu>0. Failure identifies
an unmodified supplier and refusal is optimal. Each supplier's threshold
in (1) is its actual original best response. This verifies the assessment
directly; it does not assert uniqueness. A no-trade coordination assessment
can coexist when false passes occur even in an all-unmodified pool.

If refusal means the physical duel and the original supplier actually
prefers initiating it to autarky, the outcome probabilities are

    productive cooperation / genuine adoption: pi,
    accepted fraud: (1-pi)epsilon,
    combat after failed recognition: (1-pi)(1-epsilon). (4)

If refusal instead leads to a physically feasible peaceful exit, the last
quantity is exit, not combat. Identifying the actual refusal action is
essential. The agent's installation is voluntary under its own current
criterion; the customer's acceptance is voluntary given its information
and refusal option. This is bargaining in a potentially coercive physical
environment, not an assertion that the environment itself is coercion-free.

## 2. A physical productive instance

Use the dedicated-setup specialization from 105, with the strict service
offer p=17/5,e=1/5. Successful service gives supplier 47/10 before its
private setup expense and customer 9/5. Refusal gives 9/2 and 3/2.
False acceptance lets an F supplier retain 49/10, leaving the customer 1.
Thus

    g=1/5, f=2/5, v=3/10, ell=1/2.

The post-entry retaliation bound still holds. Put epsilon=1/10,
K=3/10 and mu=1/50. Then H=4/25, pi=8/15,
A=7/60>0 and T=-11/150<0. The outcome probabilities are

    genuine productive adoption 8/15,
    accepted fraud 7/150,
    combat 21/50.                                   (5)

The customer's expected original gain is 7/60. The supplier's expected
original gain is epsilon f+H^2/(2K)=31/375, averaging its chosen action
over the stated cost distribution. Neither party intrinsically values
combat or corrigibility. Low enough installation cost makes a real changed
goal more profitable than the available attempt at deception; the customer
checks because the resulting productive opportunities justify its expense.

An ordinary binding device may provide the same credible outcome. If it
costs less than a provider's k, that provider can choose the ordinary route;
an equal-cost device can tie genuine adoption. A full market with both must
recompute the credible-cost distribution and recognition responses. The
displayed counts assume no cheaper qualified ordinary device in this offer
class. The ordinary-policy bound of 105 supplies a relevant comparison;
it does not prove every physical enforcement technology expensive.

## 3. Accuracy can change cooperation, deception and combat separately

In the maintained interior checking assessment, lower epsilon increases
genuine adoption at rate f/K. The combat derivative is

    d[(1-pi)(1-epsilon)]/d epsilon
        = (f+g-2 epsilon f)/K-1.                     (6)

Consequently more accurate recognition reduces combat when
f+g-2 epsilon f>K, and increases combat when the reverse strict
inequality holds. In the second region, detection replaces accepted fraud
with enough failed encounters that combat rises despite increased genuine
adoption. The third outcome is why cooperation and combat rates need not
move in opposite directions. At the numerical point (5), the first
inequality holds. These signs require (3) to remain valid.

Reducing mu in this pure-checking region raises customer welfare and
expands its participation condition; it does not change (1) once checking
already occurs with probability one. In a mixed checking/trusting region,
indifference instead gives

    pi*=1-mu/[(1-epsilon)ell],
    z*=[f-g+K pi*]/[(1-epsilon)f],                    (7)

where z is the checking probability. These formulas require 0<pi*,z*<1
and T>=0, with the stated posterior acceptance. Lower mu then raises the
adoption share in that maintained region. Other equilibrium regions and
ordinary-control options must be rechecked before extrapolating the sign.

## 4. Later goal change is a profitable repair to the one-check restriction

If a failed original can install the goal and be recognized again at no
additional cost, it can first try to pass without changing. For k<g,
that strategy gives

    epsilon f+(1-epsilon)(g-k),

which exceeds immediate genuine installation g-k whenever
epsilon[f-g+k]>0. Thus the early-adoption count (1) is not a theorem
about a freely revisable multi-check encounter. Genuine adoption can still
occur after failure; it is the timing and deception incentive that changed.

Charge each attempt a real supplier expense t>0, paid from its dedicated
controller/project budget, and first consider a **remediation menu**: a
second check is offered after failure, while a pass leads to the funded
offer. This is a restricted diagnostic policy, not the full menu of all
two-check policies. The customer also pays mu for each check it chooses. At the last
opportunity the original supplier compares

    G_1(k)=g-k-t,       F_1=epsilon f-t,       exit=0.

If F_1>0, it genuinely installs at that opportunity iff k<H=g-epsilon f.
At the first opportunity, immediate installation has value g-k-t, while
trying the original first has value

    -t+epsilon f+(1-epsilon)max(g-k-t,epsilon f-t,0). (8)

Within k<H, immediate genuine adoption is preferred exactly when

    k <= [(1-epsilon)t/epsilon]-(f-g)=:a,            (9)

for epsilon>0. When 0<a<H<K and F_1>0, low-cost types k<a install
before the first check, middle types a<k<H try once and install if caught,
and high-cost types H<k<K try the original at both opportunities. Ties
are recorded separately. This is a substantive chosen later change, not
an automatic inherited type transition.

For the physical values above and t=3/100, a=7/100,H=4/25. The outcome
probabilities become

    genuine installation: a/K+(1-epsilon)(H-a)/K =151/300,
    accepted fraud: epsilon(K-a)/K
                 +epsilon(1-epsilon)(K-H)/K =89/750,
    combat: (1-epsilon)^2(K-H)/K =189/500.             (10)

Expected checks are 169/100. The customer's original gain after both
checking expenses is 217/3750>0. At the second check, following a first
failure, the genuine-adoption share before that check is 9/23. Checking
there gives 2/23-1/50>0, while untested trust loses. At the first pass
the genuine posterior is 70/93; at the second pass it is 45/52.
Both exceed the acceptance threshold ell/(v+ell)=5/8. Thus subsequent
checking and acceptance are actual best responses within this specified
remediation continuation. The supplier's ex ante original gain is
3493/60000, using the piecewise values in (8), above refusal.

The first-pass posterior follows from mass a/K=7/30 and false-pass mass
epsilon(1-a/K)=23/300: (7/30)/(7/30+23/300)=70/93.
These posterior checks matter; simply applying (8) while assuming buyers
continue to trust would leave the repair incomplete.

**A further successful repair changes that assessment.** If a second check
is also available after a pass, the customer can request confirmation.
Keep the displayed first-stage strategy temporarily fixed to test this
deviation. In unnormalized cost-distribution masses, a first pass contains
7/100 genuine low-cost suppliers and 23/1000 original suppliers. Of those
originals, 9/1000 install the goal if offered confirmation and 14/1000
remain original; only 14/10000 of the latter pass again. The customer's
conditional gain from confirmation is therefore

    [(79/1000)(3/10)-(14/10000)(1/2)]/(93/1000)-1/50
      = 115/465-1/50,

above the immediate-acceptance gain 95/930. Consequently the remediation
assessment is **not** an equilibrium of this enlarged audit menu. The
deviation creates additional genuine later changes and reduces fraud;
it is a constructive repair, not evidence against goal accommodation.
Initial suppliers would then revise their choices as well. A full joint
choice of audit timing, later goals, prices and available capacity remains
open. Equations (8)–(10) retain their restricted-menu meaning.

## 5. Capacity and perfect recognition are distinct interventions

A customer may prefer one available check ex ante even though another
check is worthwhile after the first fails. With the same t in the example,
one check gives the customer 7/60, above the two-check value 217/3750.
Two checks give the supplier more expected original welfare and permit
profitable delay. A chosen single-use verification device or a deadline
with one remaining check can therefore be a relevant safeguard. This is
only an attainable intervention if its physical capacity, price and the
other party's ability to supply another check are accounted for. It is
not a justification for imposing a no-renegotiation rule for free.

At t=0, unbounded independent false-positive attempts under an unchanged
pass-acceptance rule eventually let an original pass with probability one.
When f>g, no positive-cost genuine installation beats that strategy.
Rational customers then have a reason to abandon the assumed acceptance
rule. This is a boundary of that recognition protocol. Costed checks,
sound certification, ordinary funded protection and a different partner
are consequential constructive repairs; no general obstruction follows.

With a sound certificate epsilon=0, a recognized successful installation
can be distinguished from every declared original fraud strategy. If the
customer can irreversibly buy that checking service before the supplier
chooses, and using the already purchased result has no additional cost,
types k<g choose genuine installation and the others refuse. The customer
chooses this available intervention when

    min(g/K,1)v > mu.                                (11)

After a valid certificate, acceptance is optimal; after failure, refusal
is optimal. A consistent assessment assigns a valid certificate to a
genuine installation even if that event was initially off path. This is
a conditional selected implementation with actual current-goal reasons
on both sides. Soundness over the declared program class, sunk purchase,
physical funding and stagewise attack comparisons are demanding assumptions.
A cheaper ordinary qualified controller can replace some or all genuine
updates; an equal-cost one preserves indifference. Repeat failures or a
larger program class cannot be treated as evidence that sound certification
has already been built.

## 6. Choosing contract ambition changes the recognition effect

The fixed strict offer is not automatically the buyer's best quality.
Retain the physical workshop and let x=c e be service cost, rho=b/c,
and ell the customer's loss if falsely accepted. With ordinary-division
shortfall D=h-(R-Y), the supplier's fraud gain is f=ell-D and its
honest gain is g=ell-D-x. Write L=1-epsilon. In the interior selected
one-check assessment,

    pi=[L(ell-D)-x]/K,
    A(x,ell)=pi(rho x-L ell)-epsilon ell-mu.          (12)

At fixed price/ell this is strictly concave in x, with unconstrained
optimum

    x*=L[(rho+1)ell-rho D]/(2rho),
    H*=L[(rho-1)ell-rho D]/(2rho),
    A*=rho(H*)^2/K-epsilon ell-mu.                   (13)

Feasibility, positive honest benefit, posterior acceptance and audit
optimality must hold at this point. In the example ell=1/2,D=1/10,
rho=4,K=3/10,epsilon=1/10,mu=1/50, they do: x*=189/800,
pi*=33/80 and A*=2147/16000. The buyer asks for more service than
x=1/5 and obtains a larger expected gain, while fewer suppliers find
genuine installation worthwhile. The buyer's own objective does not
maximize the count of changed agents.

For these fixed price and technology parameters, reoptimizing x gives
pi*=11L/24 and combat L(1-11L/24), increasing with L on [0,1].
Increasing recognition accuracy now raises both genuine cooperation and
combat, while reducing accepted fraud. This differs from (6) with quality
held fixed because the customer also raises its service demand. A candidate
accuracy upgrade must therefore include that strategic response.

For example, a publicly available upgrade from epsilon=1/10,mu=1/50
to epsilon=1/20,mu=3/100 raises the optimized customer value from
2147/16000 to 33121/192000, with the same maintained assessment conditions.
The customer has a current-goal reason to buy it in that selected
continuation. Building the device or selecting the positive market
assessment is an additional condition, not inferred from these prices.
Late rechecking and alternate contracts in sections 4–5 remain relevant
enlargements; (13) is a selected one-check price/quality calculation, not
a global mechanism optimum over every subsequent negotiation.
