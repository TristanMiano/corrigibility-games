# Renewable markets and the option to wait for a partner

**R0005 analytical extension.** This is an optimal-stopping calculation over
implemented cooperative opportunities. It retains the actual implementation
and combat comparisons in the per-period menu; it does not derive them from
the stopping equation. It extends 099's stationary stream to observed,
changing partner opportunities and a chosen market-access intervention.

## 1. The common-state comparison

At a settled cycle boundary the agent observes state s. Fresh physical
supplies and potential partners follow a known finite-state Markov kernel
P. There are no unpaid earlier obligations. In this specialization,
installation and current partner choice do not change P. Let a(s) be the
best current original payoff without the proposed reusable goal, and r(s)
the best payoff with it. Both include actual consenting counterparties,
ordinary policies/controllers, exit and physically available combat, with
all recurring material, work, information and settlement costs charged.

Assume the installed contractual criterion attains r(s) with its accepted
obligations honored, ranks those honest alternatives by own original
welfare, and has the required continuation incentive certificate. It may
decline new contracts. Thus r(s)>=a(s) when installation preserves access
to every ordinary option. This is an explicit menu assumption; loss of
outside options after adoption requires a different comparison.

Write Delta(s)=r(s)-a(s)>=0, setup cost k(s)>0, and 0<delta<1.
Let U be the installed value and V the current-original value before
installation. The relevant Bellman equations are

    U(s)=r(s)+delta sum P(s,s')U(s'),
    V(s)=max{U(s)-k(s), a(s)+delta sum P(s,s')V(s')}.

Put D=U-V. Subtracting gives the simpler loss-of-delay equation

    D(s)=min{k(s), Delta(s)+delta sum P(s,s')D(s')}.    (1)

The operator in (1) is a contraction in sup norm, so this finite bounded
problem has a unique value. Equivalently,

    D(s)=inf_tau E_s[sum(t<tau)delta^t Delta(S_t)
                         +delta^tau k(S_tau)],       (2)

where tau is a stopping time and tau=infinity means never installing.
Installation is optimal at s exactly when

    k(s)<=Delta(s)+delta E_s D(S_1).                  (3)

Strict inequality gives strict preference over waiting; equality permits
either. The current original pays the setup cost and evaluates this
choice. Later installed selves use their actual contractual criterion;
the assumed honored-menu certificate is what makes U their implemented
own-welfare value rather than a fictitious founder-controlled policy.

The finite-horizon version has D_0=0 and the same recursion with D_(n-1)
on the right. Equation (1) reduces to 099's immediate-versus-delay result
when every state has the same Delta and setup cost.

## 2. Conditions that expand actual adoption, and a timing reversal

At fixed P and k, increasing Delta pointwise increases D by monotone
iteration in (1). It therefore enlarges the weak adoption region (3).
An improvement confined to the goal-enabled opportunity has this effect;
an equally large improvement in an ordinary option cancels it in Delta.
Raising ordinary outside returns at fixed r weakly contracts adoption.
These are conditional choice effects, not a sign claim about capability
improvements that simultaneously change both menus or the transition law.

A uniform reduction d in setup cost, with 0<d<=min k, also enlarges
adoption. From (2), 0<=D_old-D_new<=d because the discounted cost reduction
at any stopping time lies between zero and d. The right-minus-left margin
in (3) therefore rises by at least (1-delta)d. In contrast, reducing
only a *future* state's installation price can make waiting more attractive
today. For a deterministic transition to an absorbing opportunity with
Delta=1, delta=1/2, current k=1 and future k=1, immediate installation
is strict. Reducing the future price to zero makes current installation
tie waiting; reducing the current flow advantage to 3/4 makes it strictly
lose, while it was strictly preferred at future k=1. The current state
has Delta=3/4 in that final comparison in both cases. This illustrates
the importance of specifying which capability or price actually changes.

## 3. Exact independent partner-arrival solution

Each period, after observing the current market, a suitable willing
customer is available with probability q in (0,1]. Its implemented
incremental profit is g>0; otherwise the increment is zero. States are
independent across periods. Setup k is constant. Background ordinary
payoffs are the same in this comparison and have been subtracted.

Let D_G,D_B denote (1)'s values in good and bad states. Waiting is strictly
preferred in a bad state for k>0: if D_B=k, its continuation expression
is at most delta k<k, a contradiction. Define

    z=1-delta+delta q,       alpha=delta q/z.

Then D_B=alpha D_G and

    D_G=min{k, g+alpha D_G}.

Consequently installation at a good arrival is optimal exactly when

    k <= g z/(1-delta) = g[1+delta q/(1-delta)].       (4)

Below the strict boundary, install at the first good arrival; above it,
retain the original in this two-option market. Installation in a bad
state can have positive value compared with permanent refusal while
still being inferior to waiting. For example delta=9/10,q=1/2,g=1,k=2
gives installed bad-state value 9/2; paying 2 now is profitable, but the
first good-arrival strategy does better. A positive net present value
is therefore only the refusal comparison; (3) also evaluates delay.

Before observing a period's state, the original's value is

    V(q)=max{0, qg/(1-delta)-kq/(1-delta+delta q)}.     (5)

In the active region this is increasing in q. Its derivative is
g/(1-delta)-k(1-delta)/z^2>0, using k<gz/(1-delta).
This is an opportunity/choice calculation under the declared arrival
process, not evolutionary fitness or a prevalence claim about arbitrary
agents. For a homogeneous class with this process, eventual adoption
probability is one when q>0 and (4) is strict; the expected delay and
discounted installation expense remain positive.

## 4. A finite horizon separates availability from adoption frequency

For n remaining periods, write d_n=q D_G,n+(1-q)D_B,n, with d_0=0.
Then

    D_B,n=delta d_(n-1),
    D_G,n=min{k,g+delta d_(n-1)}.                     (6)

d_n is nondecreasing with n. Let n_* be the first positive integer with

    k <= g[1+delta q A_(n_*-1)],
    A_m=sum(t=0,...,m-1)delta^t.                      (7)

If no such integer exists, no finite horizon induces installation. Before
this first crossing, all later opportunities are too short to support
installation and d_m=qg A_m, which proves (7). Monotonicity then makes
every earlier good arrival with at least n_* periods remaining eligible.
With acceptance at equality, an N-period market therefore has adoption
probability

    1-(1-q)^max(N-n_*+1,0).                           (8)

At equality the probability depends on the selected installation tie.
For delta=1, use A_m=m directly; the finite recursion remains valid.
For example q=1/2,g=1,k=2,delta=1 gives n_*=3. With N=4,
only the first two good-arrival opportunities justify installation, so
its probability is 3/4. The last two customer appearances may still support
ordinary peace; failure to install is not identified with combat.

## 5. An agent can choose to create better access

Suppose before observing arrivals the agent can pay a funded expense sigma
to change q_0 into q_1>q_0. The search/network service has the specified
effect, and parties it finds still consent under the implemented terms.
The original chooses this intervention exactly when

    V(q_1)-V(q_0)>sigma,                              (9)

against this alternative and with indifference handled explicitly. This
identifies the actor, timing, information, cost and current-goal reason,
instead of treating a favorable q as if somebody automatically created it.

For delta=9/10,g=1,k=4, q_0=1/5 gives V=0 and no installation.
Changing access to q_1=1/2 gives V=15/11. An available, funded access
service costing sigma=1 is strictly chosen; the agent then installs at
its first suitable customer and receives net value 4/11. Thus the model
contains a chosen action that creates consensual utility-change adoption,
conditional on the service and implementation capabilities stated here.

A cheaper ordinary delegate delivering the same g changes the comparison:
the agent may still buy access and cooperate while choosing that delegate.
An equal-cost delegate can tie genuine installation. If better access also
raises ordinary profits, changes bargaining shares, consumes service
capacity or reveals vulnerabilities to attack, recalculate a,r,P and the
funding before applying (9). Those effects can enhance adoption, divert
it into ordinary cooperation, or favor continued refusal. The simple
arrival model isolates a mechanism; it is not a complete biological or
AI market model.
