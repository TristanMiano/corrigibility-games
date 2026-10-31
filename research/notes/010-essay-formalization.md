# R0001 working mathematics — strength, outcomes, and voluntary merger

**Provisional research checkpoint.** This note belongs to the first CG-R001 invocation, whose one-run focus is a faithful improvement of the seed essay. Statements below are local mathematical claims, not the essay's conclusions assumed true. [R101–R120 in the claim ledger](../CLAIMS.md#r0001--essay-model-results) record their scopes. Review is by the contributing AI agent only; the run's time/status accounting is separate from individual proof status. No independent or machine verification or novelty priority is claimed.

## 1. What the outcome mechanism must distinguish

Let X be a finite set of complete outcomes and u_i:X->R a von Neumann–Morgenstern utility. A positive affine recoding u_i'=c_i u_i+d_i, c_i>0, changes neither preferences over lotteries nor optimal choices from a fixed feasible set. It therefore cannot, by itself, be assumed to change outcome probabilities.

**Diagnostic.** On X={A,B}, u=(1,0) and v=(4/5,1/5) satisfy v=(3/5)u+1/5. They represent exactly the same lottery preferences. Both strictly choose A when it is available. A lottery with probabilities (4/5,1/5), by contrast, has original expected utility 4/5 rather than 1. An implementation mapping utility entries directly to outcome probabilities is additional behavioral technology; it is not the expected-utility rule.

The seed's normalized utility-times-strength expression can be given a meaning as an influence mechanism, but normalization to *somewhere within* [0,1] does not ensure representation invariance. For example two opposing agents with equal strengths and utilities (1,0),(0,1) induce (1/2,1/2) under that expression. Recode only the first as (4/5,1/5): the same preferences now induce (2/5,3/5). The world should not change just because a utility representation changes unless its literal numerical representation is physically used as an instruction.

One repair is to specify goal-directed policies mu_i in Delta(X), which are actions or induced behaviors rather than utility numbers. For effective strengths a_i>0, A=sum_i a_i, let

$$P_a(\boldsymbol\mu)=\sum_i (a_i/A)\mu_i.$$

This can mean a strength-weighted random choice of which controller's policy determines the outcome. When each mu_i can be chosen independently from a fixed menu and the other conditional laws do not respond to that choice, each controller maximizes its *own* expected utility; with menu Delta(X), its optimal policies have support on argmax u_i. With strategic responses, the mixture remains a decomposition into conditional laws but those laws need not be independently controllable. Original utilities evaluate both ordinary and modified continuation laws. A modification may change these policies and other agents' responses, but the law must say how.

An alternative is literal territorial/material control: controller i produces a_i/A of divisible resources. That gives a deterministic composite output, not necessarily the same lottery over *whole-world* outcomes. For linear additive utilities their expectations coincide; for arbitrary utility functions they need not.

## 2. Strength aggregation and identity-neutral merging

For a merger of a group C, preserving outsiders' relative influence under the mixture above requires the group's effective strength to be a_C=sum_{i in C}a_i and its conditional policy to be

$$\mu_C=\sum_{i\in C}(a_i/a_C)\mu_i.$$

Then a_C mu_C=sum_{i in C}a_i mu_i. Substitution proves that the complete outcome law is unchanged. Grouping in any order gives the same law. This is a **representation** result: it does not prove that a new self-interested successor will actually choose mu_C.

More generally let the influence/contest weight of physical strength a be f(a)>0. Suppose physical strengths add, and merging any a,b must preserve their combined influence against any outsider of strength c>0:

$$\frac{f(a+b)}{f(a+b)+f(c)}
=\frac{f(a)+f(b)}{f(a)+f(b)+f(c)}.$$

Cross-multiplication and f(c)>0 imply f(a+b)=f(a)+f(b). Conversely this additivity suffices. Positivity makes f strictly increasing on positive reals. Additivity gives f(q)=q f(1) on positive rationals; monotonicity and rational approximation yield f(a)=a f(1) for every positive real a. Thus linear effective weights are forced by **additive physical strength plus identity-neutral influence**, not by rationality alone.

For f(a)=a^2 and three unit-strength actors, merging two changes their external share from 2/3 to 4/5. This may represent genuine synergy, but otherwise is an artifact of combining an additive strength label with a nonlinear contest rule. Models allowing synergy should record it as a physical/organizational transition.

## 3. Ideal war, deterministic split, and risk

For two controllers let s=a/(a+b), 0<s<1. A physical outcome is a nonnegative vector x=(x_A,x_B) in a feasible set. With a common usable-output bound Y>0, define the endpoint outcomes e_A=(Y,0), e_B=(0,Y).

The ideal costless war lottery is L_W=s delta_eA+(1-s)delta_eB. A deterministic strength-proportional split is x_S=(sY,(1-s)Y). For linear color utilities u_A=x_A,u_B=x_B, both yield expected welfare (sY,(1-s)Y).

If each u_i is concave on a convex feasible set containing the segment between e_A and e_B, Jensen's inequality yields

$$u_i(x_S)\ge s u_i(e_A)+(1-s)u_i(e_B).$$

Strictness requires curvature along this segment (or an additional physical advantage), not merely the label “peace.” With convex own-output utility u_A=x_A^2, u_B=x_B^2 and Y=1, deterministic proportional splitting gives s^2 and (1-s)^2, strictly below war expectations s and 1-s. An enforceable peaceful lottery reproducing L_W removes this risk comparison; it requires public randomization and credible conditional execution.

**Universal-utility boundary.** For two lotteries P,Q on finite X,

$$E_P[u]\ge E_Q[u]\ \text{for every }u:X\to[0,1]\quad\Longleftrightarrow\quad P=Q.$$

Proof: use u=1_{x} for every x. All P(x)>=Q(x) and equal total mass imply equality coordinatewise. Equality trivially suffices. Thus a preference-agnostic claim of strict improvement is impossible over this unrestricted class. Positive results must restrict preferences, compare state dominance under a declared order, or reproduce the same lottery.

## 4. A merger objective that actually preserves proportional service

The linear weighted criterion s x_A+(1-s)x_B on x_A+x_B<=Y chooses the A endpoint when s>1/2 and B when s<1/2; at s=1/2 every full-output split ties. It does not implement x_S. Adoption evaluated with founder utilities can therefore fail even if combat destroys resources.

A family of corrected objectives uses a continuous strictly increasing strictly concave function phi:[0,infinity)->R and

$$G_a(x)=\sum_i a_i\phi(x_i/a_i),\qquad a_i>0.$$

For fixed total output at most Y, Jensen gives

$$G_a(x)/A\le\phi\left(\sum_i x_i/A\right)\le\phi(Y/A).$$

Strict concavity gives equality only when all x_i/a_i are equal; strict increase requires sum_i x_i=Y. Therefore the unique maximizer is x_i=a_iY/A. The construction is finite and continuous at zero whenever phi is; phi(t)=t^gamma with 0<gamma<1 is an example.

For disjoint groups C,D, unnormalized objectives add: G_{C union D}=G_C+G_D. Keeping the constituent goal coordinates and the same phi makes hierarchical aggregation associative. This is an implementation design, not a claim that every utility mixture is meaningful. Original linear founders evaluate agreeing to this changed successor by the actual output and process costs under their old utilities.

**Boundaries.** If phi is linear, uniqueness disappears; if the feasible set is not the full resource simplex, the proportional point can be infeasible. Fixed minimum project costs, non-substitutable resources, or different conversion yields need a different optimization. Keeping only a single scalar summary of a merged group may discard information required to preserve all constituent goals.

An unchanged-utility principal can delegate the identical production policy to an executor if that policy is equally expressible, verifiable, and durable at equal physical cost. Consequently these allocation results alone do not establish a special advantage of changing terminal preferences.

## 5. Physical module: exact aggregate dispersion-recovery frontier

**R0001 audit correction:** the formula below is exact for the written aggregate LP. Its original description as a literal serial line with production rate k was too strong. When damaged capacity makes k<1/tau, recovery time must also be added to y/k. [Note 024](024-recovery-scheduling-and-infrastructure.md) gives the counterexample, corrected attainable serial frontier, parallel alternative and two-feedstock extension. The old LP is preserved as a relaxation; its algebraic result is not withdrawn.

Fix nonnegative usable stock O and dispersed stock D in material units; total M=O+D. Work reserve B>=0 and processing time T>=0 are independent budgets. Production costs c>0 work/unit and tau>0 time/unit; recovering dispersed stock costs w>=0 work/unit and r>=0 time/unit. Capacity k>=0 is output/time. No additional material or work can be harvested.

Choose recovered x and delivered y under

$$0\le x\le D,\quad0\le y\le O+x,$$
$$cy+wx\le B,\qquad \tau y+rx\le T,\qquad y\le kT.$$

This is a divisible aggregate workload/capacity abstraction. For any given y, the least necessary recovery is x=(y-O)_+. Nonnegative costs make that choice weakly best. Hence the exact LP output frontier is

$$Y=\min\left\{M,kT,\frac{B}{c},\frac{B+wO}{c+w},
\frac{T}{\tau},\frac{T+rO}{\tau+r}\right\}.$$

To check equivalence, cy+w(y-O)_+ is the maximum of cy and (c+w)y-wO, so the work constraint is precisely the pair of corresponding upper bounds. The time constraint has the same form. y<=M ensures x<=D. Choosing this x for y equal to the displayed minimum proves attainability, including B=0,T=0,w=0,r=0.

At matched M,B,T,k, write alpha=w/(c+w), beta=r/(tau+r), C_w=B/(c+w), C_t=T/(tau+r), and C_0=min(M,kT,B/c,T/tau). Then

$$Y(O)=\min\{C_0,C_w+\alpha O,C_t+\beta O\}.$$

It is nondecreasing and concave piecewise affine in O. Moving d<=O usable units into D lowers output by an amount in [0,max(alpha,beta)d]. This follows by comparing the same three affine bounds before/after damage; each falls by between zero and max(alpha,beta)d. Damage can have **zero** cost when a different bottleneck binds.

If Y_0=Y(O), damage leaves output unchanged exactly when

$$Y_0\le C_w+\alpha(O-d),\qquad
Y_0\le C_t+\beta(O-d).$$

For positive alpha/beta these identify the exact threshold d before recovery becomes binding; omit a zero-slope restriction because it is already satisfied. Increasing damage can cross a bottleneck and change marginal losses, so a constant scalar war penalty is not generally an exact representation across states/deadlines. For a single fixed state its numerical value can always be summarized as a scalar; that weaker reduction must not be confused with uniform predictive equivalence.

This derivation is conditional on fixed control. It has not removed attack from a bargaining game. Combat and compromise must next be assigned distinct (O,D,B,k,T) transitions, including their own work and delays, before using a physically attained frontier as a continuation payoff input. Use this LP's Y directly only when its constraints accurately specify the chosen technology; otherwise substitute the appropriate scheduled frontier from note 024 or another proved model.

## 6. Physical costs, unequal survival, and adoption boundaries

For each route j in {split, merge, war-A, war-B}, specify a physical transition z->z_j and remaining useful processing time. Let P_S=Y(z_S), P_M=Y(z_M), W_A=Y(z_WA), W_B=Y(z_WB). Transition withdrawals include communication, verification, integration, combat, and damage; they are not additional payoff penalties unless agents also have genuine process preferences.

For example, combat may move d from O to D, discharge e_C from B, consume time ell_C, and reduce k. Peace can preserve O but spend e_S and ell_S on negotiation. Infeasible costs make a route unavailable, not a negative inventory. Capability can be mapped into k: for conversion factor eta, split/merged capacity may be eta(a+b), while a winner retains eta lambda_i(a_i+rho_i a_j), 0<=lambda_i,rho_i<=1. This states explicitly whether defeated infrastructure is captured or lost. Contest strength and production capacity are different quantities even when coupled this way.

Under linear founder color utilities, no intrinsic agency penalty, and selfish postwar survivors, the combat disagreement vector is

$$w=(sW_A,(1-s)W_B).$$

A negotiated split x_A+x_B=P_S is strictly preferred to combat by both exactly when
\(x_A\in(sW_A,P_S-(1-s)W_B)\). It exists iff

$$P_S>sW_A+(1-s)W_B.$$

A *fixed proportional* split has the stronger two conditions
\(sP_S>sW_A\) and \((1-s)P_S>(1-s)W_B\), equivalently P_S>max(W_A,W_B). Thus an aggregate physical gain need not make the strength-proportional rule individually acceptable when war's recovery depends on who wins.

Example: s=1/2, W_A=12,W_B=4,P_S=9. A bargain exists (A receives between 6 and 7), but the proportional allocation (4.5,4.5) is rejected by A. This is a counterexample to transferring the symmetric-war proportional conclusion to arbitrary winner-specific technology.

A merger that delivers (alpha P_M,(1-alpha)P_M) and incurs finite founder penalties kappa_A,kappa_B for changing preferences is strictly acceptable iff

$$sW_A+\kappa_A<\alpha P_M<P_M-(1-s)W_B-\kappa_B.$$

This compares founders' old utilities, not G_a. A nonempty interval exists iff P_M>sW_A+(1-s)W_B+kappa_A+kappa_B. The strength-preserving alpha=s requires

$$P_M>\max\{W_A+\kappa_A/s,\ W_B+\kappa_B/(1-s)\}.$$

Freezing therefore especially constrains a small-share agent at a given fixed split; it does not imply that ordinary peace fails. Even without freezing, if split and merger produce the same actual output with the same implementation, they yield the same founder welfare. Extra merger costs can make ordinary split strictly preferable.

**General payoff caution.** With intrinsic loss-of-agency or war preferences, disagreement payoffs may be negative. For example u_i=x_i-kappa_i M_i-eta_i L_i+beta_i C gives
\(w_A=sW_A-\eta_A(1-s)+\beta_A\) before any change. Merger costs include both kappa_i and eta_i. For arbitrary thresholds r_A,r_B and P>=0, a feasible full-output split strictly exceeding both thresholds exists iff
\(r_A<P,\ r_B<P,\ r_A+r_B<P\).
The interval form [0,P] intersect (r_A,P-r_B) is safest. Simply summing arbitrary agents' incomparable cardinal utilities is not licensed: these formulas use the declared common output-unit normalization.

**No universal material dominance.** With c=tau=w=r=1, M=10, O=10, k=10 and B=T=12, dispersing d units gives Y(d)=min(10,11-d/2). Loss is zero through d=2, then grows at rate 1/2. At d=6, output is 8. With B=T=20, the same dispersion leaves output 10. Moreover, at initial B=T=14, a war route spending 2 work and 2 time then dispersing 6 yields 8, whereas a peaceful mechanism spending 7 work and 7 time yields 7. This defeats that mechanism's claimed efficiency advantage; it does **not** show combat beats a cheaper peaceful fallback.

## 7. Continuing attack incentives and selection

At a public checkpoint with two capable unchanged-utility agents, suppose keeping a fixed split alpha yields (alpha P,(1-alpha)P) and an attack by either yields (q W_A,(1-q)W_B), with no further strategic choices in these *specified continuation values*. No profitable unilateral attack requires both component inequalities. With later strategic opportunities the same comparison must use complete continuation values instead of these reduced terminal formulas.

If P,W>0 and W_A=W_B=W but the future contest share can be any q in [q_min,q_max], a fixed split deters attack at every such checkpoint exactly when

$$\alpha\in[q_{\max}W/P,\ 1-(1-q_{\min})W/P].$$

The interval is nonempty iff

$$P/W\ge1+q_{\max}-q_{\min}.$$

Proof: intersect each agent's inequalities over q, taking the supremum of A's bound and the infimum of B's. These conditions are sufficient only for the stated checkpoint continuations, not a full repeated-game equilibrium. Renegotiable shares, costly transfers, uncertain power, and endogenous investment change the problem. Initial utility-change penalties already incurred are sunk and must not be charged a second time in attack comparisons.

**Selection counterexample with attacks retained.** Consider a checkpoint where any Attack triggers the same war lottery W, while mutual Continue implements a strictly Pareto-superior P. Payoffs are

| A / B | Continue | Attack |
| --- | --- | --- |
| Continue | P | W |
| Attack | W | W |

Both (Continue,Continue) and (Attack,Attack) are Nash equilibria: once the opponent attacks, unilateral restraint cannot avert war. Continue weakly dominates Attack, and only the peaceful profile survives trembling-hand perfection in this two-action game, because any positive probability of the opponent continuing makes continuation strictly preferable. Thus equilibrium refinement matters. The example uses neither utility-freezing preferences nor irrationality; its war equilibrium is weak, and changing initiative or attack-specific costs can change it. It refutes a claim that strict joint preference for peace alone ensures peace in every Nash equilibrium.

After **actual merger**, the two separate decision makers no longer exist. A single successor's lack of internal war is a change of agency, not a theorem that two capable actors became stable. Before fusion and against external actors, attacks remain available. Keeping two independent agents with the same objective is a different implementation and can retain coordination failures.

## 8. Deception as an action with observation and response

Let x be actual physical output, m a declaration, and o an observation from a kernel O(o|x,m,v), where v is verification effort. Original utilities apply to x and the history, not to the declaration. Producing a new “camouflaged” object requires declaring which original predicates it satisfies and its production costs. If one object genuinely satisfies both goals, the feasible set has expanded; that is not automatically deception.

For a proposed peaceful mechanism, let H_i be i's incumbent value of honest execution. An attempted deception gives net success value G_i and detected-failure value L_i, with detection probability d. All branch values include physical deception/verification costs and the actual response after detection. Then

$$D_i=(1-d)G_i+dL_i.$$

For G_i>L_i, honesty is weakly preferred iff
\(d\ge(G_i-H_i)/(G_i-L_i)\).
In this G_i>L_i case, if H_i>=G_i, all d suffice; if H_i<L_i, none suffice. If G_i=L_i, compare H_i with that common value directly. If G_i<L_i, the inequality instead is d<=(H_i-G_i)/(L_i-G_i), intersected with [0,1]: detection can make deception more attractive in such a continuation. Boundary equality is indifference, not strict honesty. “Detection is costly” is not itself an assumption about the sign of these inequalities.

**Strength example, conditional on a credible war response.** Let honest output be H=sP, successful theft yield G=P, and detection trigger the same q=s war lottery, L=sW, with 0<W<P. The deterrence threshold is

$$d_*(s)=\frac{(1-s)P}{P-sW},\qquad
d_*'(s)=\frac{P(W-P)}{(P-sW)^2}<0.$$

The weaker party is harder to deter in this particular model, but either party can prefer cheating below its threshold. For P=1,W=4/5,s=9/10, d_*=5/14; a strong party still cheats at d=1/5. Thus “only the weaker party has an incentive” is not a general result. Different detection and capture technologies can reverse comparative statics.

**Credibility counterexample.** If, upon detection, B can costlessly restore the honest allocation or fight for less expected utility, it restores the allocation. In that continuation L_A=H_A, not the lower punitive-war value. With free deception, G_A>H_A, and d<1,

$$D_A-H_A=(1-d)(G_A-H_A)>0.$$

No imperfect inspection deters deception in this example. A bond, committed sanction, verification that prevents rather than merely detects the deviation, or an intrinsic/physical deception cost can alter the result. Each requires explicit implementation; detection does not make punishment credible by itself.

**Endogenous inspection.** A minimal continuation game lets A choose honest/cheat and B inspect/not inspect. Honest payoffs are (h,b); undetected cheating gives (g,b_D); detected cheating gives (ell,b_F). Inspection detects with probability delta>0 and costs B an output-equivalent c>0, with no false positives. These are net outputs of a specified physical enforcement subgame; in particular b_F must be an implementable continuation, not a noncredible threat.

Write Delta_A=g-h>0, K_A=g-ell>0, K_B=b_F-b_D>0. If
\(0<\Delta_A<\delta K_A\) and \(0<c<\delta K_B\), there is no pure equilibrium:
honesty induces no inspection, which invites cheating; cheating induces inspection, which makes honesty preferable. The unique mixed equilibrium has

$$\Pr(\text{inspect})=\frac{\Delta_A}{\delta K_A},\qquad
\Pr(\text{cheat})=\frac{c}{\delta K_B}.$$

Proof: A's payoff difference between cheating and honesty is Delta_A-p delta K_A; B's gain from inspection is z delta K_B-c. Set both to zero; the stated strict inequalities put both probabilities inside (0,1). Hence costly verification without precommitment can leave positive equilibrium deception even when sufficiently frequent inspection would deter it. This is standard inspection-game algebra, not a novelty claim.

## 9. What “nearby utilities” can and cannot guarantee

Let K be the same nonempty feasible set of lotteries before and after a proposed change, and let mu maximize E[u] on K and nu maximize E[v] on K. Suppose both maximizers exist and ||u-v||_infinity<=epsilon on the common outcome domain. Then

$$0\le E_\mu[u]-E_\nu[u]\le2\epsilon.$$

Proof: optimality under u gives the first inequality. For the second,
\(E_\mu u\le E_\mu v+\epsilon\le E_\nu v+\epsilon\le E_\nu u+2\epsilon\).
The numerical bound requires fixed common cardinal normalization; arbitrary positive affine recodings can otherwise make “closeness” meaningless. It does not say that changing utilities improves old utility: on the same feasible set an incumbent already maximizing u cannot gain by choosing a different objective alone.

The bound can be approached with two feasible middle outcomes and two infeasible normalization anchors. Give the feasible pair u-values 1/2+epsilon-eta and 1/2-epsilon+eta, and v-values 1/2-eta and 1/2+eta, for 0<eta<epsilon/2 and epsilon<1/2. Supremum difference is epsilon; u-regret is 2epsilon-2eta. Anchor both utilities at 0 and 1 on the other outcomes. Thus the near-2epsilon loss is compatible with fixed range normalization and a unique new maximizer.

A strategic environment need not leave K fixed. For a concrete countermodel, use normalized utilities u=(1,1/2,0), v=(1,1/2+epsilon,0). A public execution mechanism permits all three outcomes while u is installed but physically permits only the last outcome after any different preference class is installed. Then the old achievable value falls from 1 to 0 for arbitrarily small epsilon. The mechanism could be an external committed response; this example does not assert that such a punishment is an equilibrium without that commitment. Closeness of utility functions alone cannot bound losses when feasible opportunities depend on the observable modification.

Similarly, if a powerless agent cannot change the actual future outcome law P, changing its utility gives old evaluation E_P[u] both before and after (less any old-valued change costs). A higher numerical value under the newly installed utility is not an old-utility gain. A “pain relief” intervention can still help an incumbent that values the resulting experiential state, but then that physical/experiential change must be present in P, rather than inferred from a new scoring rule.

## 10. Conditional replication by a fixed-utility delegate

Consider a finite-horizon physical game and a specified modification protocol M with behavioral strategy sigma_M at every public/private information history it can encounter. Assume:

1. A fixed-utility delegation technology D can execute exactly the same contingent action distributions, including attacks, withdrawals, messages, and internal-state transitions.
2. Those internal transitions can be implemented with the same physical work/delay/failure kernels. D may simulate changing objectives as internal policy state while the principal's terminal preferences stay fixed.
3. Opponents' observation/response rules are invariant under the declared correspondence between certified M and D executions. Merely matching observed play on one path does not establish this assumption.
4. Founder utility depends only on corresponding physical outcomes and histories, not on whether an actual preference ordering was replaced rather than simulated.

Then the two implementations induce the same distribution over corresponding histories, and the same founder expected utilities. Proof is induction over the horizon: matched past histories induce the same action distribution by (1),(3), and the same next-state law by (2); terminal evaluations agree by (4).

This is an expressivity/implementation comparison, not an assertion that such delegates are freely available. It covers full contingent policies, not just the on-path allocation. Independent attacks remain physical actions in both representations, selected by the matched controller. Utility freezing, intrinsic preferences for merger, different costs, trust limits, or opponents conditioning on literal code/utility identity can break the stated equivalence. In particular, durable policy execution is stronger than a revocable promise. The result isolates what a claimed advantage of modification must exceed; the underlying simulation argument is conventional.

## 11. A merger objective cannot uniquely implement every bargain lottery

Let X be finite and let a single successor choose any lottery mu in Delta(X), maximizing E_mu[v] for a von Neumann–Morgenstern utility v. The maximizing lotteries are exactly those supported on argmax_X v. Indeed, their value is max_X v; assigning positive mass to a strictly lower-valued outcome makes the average strictly smaller. Consequently a lottery is the **unique** optimum for some such v iff it is a point mass. If a target uses at least two outcomes, optimality requires tying all supported outcomes, and each supported point mass is also optimal.

This is stronger than the affine-recoding diagnostic in section 1. Arbitrarily expressive expected-utility objectives still cannot uniquely implement an interior lottery from the full simplex. A tie-breaking rule, restricted feasible menu, externally enforced randomization, or a different physical outcome domain is doing additional work. It does not preclude a mixed lottery being an optimal choice, or an action whose physical kernel produces a nondegenerate lottery being uniquely optimal from a restricted action menu.

For example, two opposing color utilities on X={all-A, all-B} give payoff vectors (p,1-p). The weighted Nash product p^s(1-p)^(1-s), 0<s<1, has unique optimum p=s: its log derivative is s/p-(1-s)/(1-p), zero precisely at s. Yet a successor's expected utility is p v(all-A)+(1-p)v(all-B), which is linear in p and cannot have that unique interior optimum.

The bargaining rule maximizes a nonlinear function of the **vector of expected utilities**; an ordinary successor maximizes the **expectation of a utility of actual outcomes**. Moving a nonlinear function through an expectation is not licensed. This is a conventional linear-objective obstruction, not a novel impossibility theorem or a rejection of bargaining theory.

The physical production model in section 4 avoids this obstruction honestly: its outcome domain includes a single world containing both colors, with allocation x_i=a_i Y/A. That world is the unique maximizer of G_a on the resource simplex; choosing it deterministically is possible. If production uncertainty or indivisibility removes that world, recheck implementation. An external delegate with an enforceable randomized policy can implement p=s, but this is a stated technology rather than a consequence of changing utility entries.

## 12. A representation-invariant bargaining extension, and its limit

For more general goals, let F be a compact convex feasible set of founder expected-utility vectors and d a specified disagreement vector. Assume F contains some vector strictly exceeding d in every coordinate, and a_i>0. The weighted Nash rule selects the utility vector maximizing

$$\sum_i a_i\log(v_i-d_i),\qquad v\in F,\quad v_i>d_i.$$

It has an optimum with strictly positive gains: compactness bounds every gain above; any sequence approaching a zero gain has log objective tending to minus infinity, whereas a strictly feasible reference has finite value. Strict concavity on the positive orthant makes the selected utility vector unique. There need not be a unique physical lottery realizing that vector. Under a separate positive affine recoding v_i'=c_i v_i+b_i, d_i'=c_i d_i+b_i, its objective changes by the constant sum_i a_i log c_i. Thus the rule is invariant to each founder's utility representation without adding their raw cardinal values.

For two linear-color agents with feasible full-output split x_A+x_B=P and nonnegative disagreement values d_A,d_B, P>d_A+d_B, the solution is

$$x_A=d_A+s(P-d_A-d_B),\qquad x_B=d_B+(1-s)(P-d_A-d_B),\quad s=\frac{a}{a+b}.$$

Differentiate the strictly concave log objective on x_A in (d_A,P-d_B), or use weighted Jensen on the gains. This recovers the proportional split only at d=0 or when d itself is proportional. With d=(sW_A,(1-s)W_B), the earlier asymmetric example gives x_A=6.5,x_B=2.5, satisfying both participation bounds. Strength determines the **surplus shares above disagreement**, rather than being assumed to determine the entire allocation irrespective of outside options.

This is an optional normative/implemented bargaining rule, not a derived equilibrium selection theorem. Its proposer incentives, threat credibility, feasible-set convexification, and implementation costs need separate models. The rule cannot generally be installed as an expected-utility successor objective over original stochastic outcomes (section 11). In the deterministic divisible-output case it can be implemented by an objective over actual allocations, with a separately specified treatment of outcomes below the disagreement floor. No literature priority is claimed for this standard bargaining construction; the contribution here is locating its implementation boundary in the essay model.

## 13. A fully specified sequential-update obstruction

This small game separates an attractive **joint** preference change from unilateral adoption. It uses strength-weighted control in ordinary peace, not an assumption that rejecting a change causes war. **Its exclusive-control transfer is a stronger delegation technology, not the baseline availability of combat throughout production.** Section 14 supplies a different witness that retains both agents' attack capability after selecting a production controller. Two original agents here have strengths a,b>0, s=a/(a+b), and utilities u_A(x)=sqrt(x_A), u_B(x)=sqrt(x_B). A peaceful controller lottery selects A with probability s and B otherwise. The selected controller can allocate the available output however it prefers. A selfish controller produces only its own color. The alternative current objective is

$$G_s(x)=s\sqrt{x_A/s}+(1-s)\sqrt{x_B/(1-s)}.$$

For total output y it uniquely chooses (sy,(1-s)y), by section 4. Each original utility and G_s is homogeneous of degree 1/2. Utility labels and installations are public and correctly understood; no hidden type or mistaken future model is involved.

**Explicit physical witness.** Start with usable material O=1,D=0, work B=51/50, time T=4, production c=tau=k=1, and no new material/work inflow. Two administrative rounds each consume 1/100 work and one time unit, whether the scheduled agent keeps or changes its utility. These expenditures cover the stipulated communication, computation and installation operations; this is a declared idealized technology, not a claim about actual machine costs. Normal production therefore has B=1,T=2 and output P=1. Every attack consumes 1/4 work and 1/4 time, then the contest chooses a survivor with probability s for A. The loser loses agency, not the value its original utility assigns to later clips. The survivor retains control/capacity and produces with its *current* objective. Remaining work gives W in {77/100,76/100,75/100}, depending on the checkpoint; ample time/material/capacity make those bounds attainable. Unused material remains material. Spent work is dissipated/exported energy, not disappearance of conserved energy. This particular obstruction needs no dispersion; sections 5–6 allow adding it.

**Protocol.** Round 1: A chooses Keep or Install-G, while B waits. Round 2: B chooses Keep or Install-G, while A waits. At each round either agent can instead Attack; an attack has priority and prevents the pending administrative action/cost. A final checkpoint offers both Attack or Continue. Any attack draws the contest and ends separate strategic interaction; mutual Continue draws the peaceful controller lottery. The selected controller then chooses a feasible allocation and produces it. The normal lottery is stipulated transfer of control for this terminal production episode: the unselected agent loses the ability to intervene during that episode. This is an explicit control/delegation technology, **not** evidence that two still-capable agents refrain throughout production. Before that transfer, attack remains available to both. The horizon ends after production; no subsequent interaction is claimed. No reciprocal atomic installation, further utility menu, freezing penalty, deception, or merger is available in this local subgame. Those choices distinguish it from the wider family.

For a counterfactual profile in which both install G, either selected controller produces (s,1-s); old welfare is (sqrt(s),sqrt(1-s)). With neither changing, welfare is (s,1-s). Both strictly prefer the joint change for 0<s<1. An enforceable ordinary allocation or fixed-utility randomized delegate can reproduce this same gain if supplied with the corresponding control technology.

But B strictly declines to change after either action by A. If A kept its original goal, B gets (1-s) when it keeps and (1-s)sqrt(1-s) when it changes. If A installed G, B gets

$$s\sqrt{1-s}+(1-s)\quad\text{by keeping, versus}\quad\sqrt{1-s}\quad\text{by changing}.$$

Their difference is (1-s)(1-sqrt(1-s))>0. B gains from A's generosity while retaining its own selfish control. Anticipating this, A keeps: it gets s instead of s sqrt(s) from installing G alone. Conditional on peaceful checkpoint continuations after every installation history, the unique adoption decisions are therefore Keep,Keep. Together with those continuations and the stated optimal production rules, these decisions form a subgame-perfect decision-self equilibrium.

Attack does not invalidate that equilibrium. At the final checkpoint it replaces the same controller lottery and current production policies at P=1 by the corresponding lottery at W<1, strictly decreasing every current utility, because the allocation rule scales and each relevant expected utility is positive and homogeneous. In round 2, the same comparison holds if B keeps, while B's installation can only increase A's original utility or G_s value relative to that baseline. In round 1, B's continuation value is at least 1-s, whereas immediate combat gives (1-s)sqrt(W); A can secure s by Keep and then B's optimal Keep, exceeding its immediate-war value s sqrt(W). Thus no unilateral early attack improves the acting decision self's continuation value. Simultaneous mutual Attack still supports weak coordination equilibria at checkpoints if unilateral restraint cannot avert it; the Keep,Keep conclusion is for the **peaceful continuation selection**. It must not be read as uniqueness of all equilibria or as a proved refinement result for the full sequential game (section 7 proves only the two-action checkpoint refinement).

Under a separate protected **atomic reciprocal** transaction, both founders can condition consent on both changes occurring; rejecting leaves neither changed. Holding physical outputs/costs fixed, both strictly consent because sqrt(s)>s and sqrt(1-s)>1-s. This stronger transaction avoids the unilateral exposure but has not been constructed from the sequential operations. It is a comparison technology, not a free consequence of self-knowledge. Finite extra installation costs can erase its advantage. Actual fusion into one agent additionally requires an agency/infrastructure transition; dual adoption of G is not that fusion.

The example shows why a mutually beneficial joint objective, perfect utility knowledge, and available self-modification do not suffice to derive adoption. The substantive obstacle is reciprocal implementation/commitment, even in an entirely peaceful ordinary fallback. Its equilibrium qualification matters just as much as its payoff inequalities.

## 14. Persistent attack can make unilateral change attractive without convergence

Here is a second, distinct finite game, **E2-U**, with linear original color utilities u_A=x_A,u_B=x_B, equal positive strengths, and G(x)=(sqrt(x_A)+sqrt(x_B))/sqrt(2). It keeps the two administrative rounds of section 13, with the same O=1,D=0,B=51/50,T=4,c=tau=k=1 and per-round work/time costs. A may Keep or Install-G in round 1; B may do so in round 2. Both may Attack at both rounds, with attack priority. Utility labels and completed installations are public. The limited one-opportunity update menu is part of this witness; general rollback is not silently settled by it.

Normal production has P=1. Combat now consumes **3/4** work and **1/4** time and selects its winner with probability 1/2 each. Depending on when it starts, attainable output is W in {27/100,26/100,25/100}. No original material vanishes. The winner retains production capacity; the loser loses agency. The winner chooses its allocation using its current objective: an original utility takes all its own color; G divides output equally. This difference is essential when computing war payoffs after an update.

After both administrative rounds, a public, strength-weighted lottery selects who operates the production equipment. **The other agent retains the capability to attack.** At the last simultaneous decision, the controller chooses either Attack or a production allocation x_A+x_B<=1; the other chooses Attack or Continue. Either attack cancels production and starts the contest with W=1/4. If neither attacks, the selected allocation is physically produced and the finite task ends. This is a declared finite time resolution for the last production action; it is not long-run stability or a rule restricting attacks to last resort. Proposals can announce any allocation, but do not bind the operator's eventual physical choice. An operator's ordinary noncombat menu includes every split, not just selfish production. No unilateral transfer of a binding contingent policy is available in this base technology.

**Last-stage equilibria.** If both utilities remain original, every Nash equilibrium induces war with probability one. If the noncontroller continued with positive probability, the selfish controller would strictly prefer producing its own entire output over any smaller allocation or attacking. The noncontroller would then prefer attack, which gives 1/8 rather than zero. This contradicts a positive probability of continuation. If the noncontroller attacks surely, the outcome is war regardless of the controller's move. Announcing an unenforceable split does not fix this deviation.

When at least one utility is G, select the following peaceful last-stage equilibrium after each control draw:

- A G-controller produces (1/2,1/2), its unique optimal allocation. An original noncontroller gets 1/2 from continuation, versus 3W/4=3/16 from war; a G-noncontroller values the split at 1 rather than sqrt(W)=1/2.
- An original controller produces entirely its own color. A G-noncontroller then gets G-value 1/sqrt(2). Its war value is sqrt(W)(1+1/sqrt(2))/2=(1+1/sqrt(2))/4, which is smaller. The original controller gets 1 by producing, versus 3/16 from war.
- A G-controller against an original noncontroller also prefers its value 1 to the mixed-type war value above.

Thus these are actual best responses with attack available, although weak war equilibria also exist because a unilateral nonattack cannot stop the other's attack. This explicit **continuation selection** is a hypothesis of the adoption calculation, not a uniqueness or refinement claim.

The resulting old-founder welfare table, averaging the two equiprobable production controllers, is

| A's utility / B's utility | Original B | G at B |
| --- | --- | --- |
| Original A | (1/8,1/8), war | (3/4,1/4), peaceful production |
| G at A | (1/4,3/4), peaceful production | (1/2,1/2), peaceful production |

In round 2, original B installs G if A kept its original goal: 1/4>1/8. It keeps its original goal if A installed G: 3/4>1/2. Anticipating those responses, A keeps its original goal: 3/4>1/4. Therefore **Keep at A, Install-G at B** together with the stipulated last-stage equilibria is a subgame-perfect decision-self equilibrium. Each adoption comparison uses the incumbent's original utility; B's later acceptance of an all-A world is evaluated by its then-current G. Original B's welfare remains 1/4 in the table, not G's higher score.

Early attack is not a profitable deviation. Initially it gives either original agent W/2=27/200, below the equilibrium payoffs. At round 2 after A kept, B's update gives 1/4>13/100 from immediate war, while A gets 3/4>13/100. After A changed, B's Keep gives 3/4>3(26/100)/4; A's current G continuation value is (1+1/sqrt(2))/2, strictly above its early-war value sqrt(26/100) times that same quantity. These checks cover both installation histories. No later return to the original objective is available in the specified menu; adding it requires checking current-G incentives and any contingent responses.

Both originals would prefer a protected joint G installation or appropriately implemented fusion (payoffs 1/2 each at the same output) to the no-change war outcome. Yet A prefers the actual one-sided-modification continuation (3/4,1/4) to that joint change. A refusal to modify can confer a bargaining advantage; it need not doom the refuser to combat. This is a finite strategic result, not an evolutionary advantage, hard-freezing theorem or population prediction.

**Matched control.** A fixed-utility binding allocation/delegation mechanism delivering (3/4,1/4) reproduces the same founder welfare with no terminal utility changes and the same physical output. It requires execution commitment absent from the base game's bare promises. A delegate implementing G's full contingent policy can also match the original mechanism under section 10's stronger assumptions. We therefore have a positive example of strategically useful modification relative to this limited policy technology, **not** a result that modification is intrinsically necessary whenever peaceful fixed-utility commitment is available.

This witness closes one gap without closing the rest: current-goal modification can be voluntarily chosen to avert anticipated combat while the other party strategically keeps its goal. It does not imply universal modification, actual merger, agreement on a unique fair split, resistance to every equilibrium selection, or persistence beyond the finite task.

## 15. Finite freezing and the cost of delaying a threat

Extend E2-U by original utilities u_i(H)=x_i-kappa_i 1{agent i installed G}, with kappa_i>=0. Installed G still evaluates subsequent choices by G, and original welfare retains the historical penalty. The penalty is a genuine process preference, additional to the physical administrative costs; it is not a second charge for consumed work. This is a comparison of **initial** freezing types, not a model of choosing one's freezing coefficient.

Retain section 14's peaceful last-stage equilibrium whenever a G-agent is present. At round 2 after A kept, B compares Install (1/4-kappa_B), immediate Attack (13/100), and Keep followed by last-stage war (1/8). Thus a locally peaceful continuation with A waiting and B installing is selected when kappa_B<3/25. Above 3/25, select A waiting and B attacking, which is also an equilibrium of that subgame. After A installed, B always keeps: 3/4 exceeds both 1/2-kappa_B and its early-war payoff. Equalities are excluded below because they introduce additional selections.

Under these specified continuation equilibria, the initial decision is the following reduced game. Put c_0=27/200, the initial old-utility value of immediate war. Any initial attack prevents the pending installation and its preference penalty.

| A / B | Wait | Attack |
| --- | --- | --- |
| Keep | (3/4,1/4-kappa_B) if kappa_B<3/25; otherwise (13/100,13/100) | (c_0,c_0) |
| Install-G | (1/4-kappa_A,3/4) | (c_0,c_0) |
| Attack | (c_0,c_0) | (c_0,c_0) |

This table explicitly retains the saved work from attacking before an administrative round. Using 1/8 as the threat value at every date would erase the distinction.

Away from kappa_A=23/200 and kappa_B in {23/200,3/25}, the nonwar equilibria of this reduced game are exactly:

1. If kappa_B<23/200, A keeps and B waits, then B changes in round 2. Its old value 1/4-kappa_B exceeds initial war. A's best response to any positive probability of B waiting is Keep, and B then strictly prefers Wait.
2. If 23/200<kappa_B<3/25, **every equilibrium of this reduced game starts war**. Against any positive probability of B waiting, A strictly chooses Keep (3/4 exceeds both alternatives). But B then strictly prefers initial Attack: 27/200>1/4-kappa_B. Hence no equilibrium has B waiting with positive probability. Later B would willingly change if the first round had already occurred; anticipating that expense makes waiting unattractive now.
3. If kappa_B>3/25 and kappa_A<23/200, the nonwar equilibrium is A installing and B waiting, then B keeping. A's installation value exceeds c_0, and B prefers the resulting 3/4. If also kappa_A>23/200, every reduced-game equilibrium starts war: against positive waiting probability A prefers Attack to either alternative.

Weak attack equilibria remain in the cases with peace, because either attack suffices. The statements concern the reduced game **under the given off-path continuation selections**, not all equilibria of every extensive game refinement. For example, selecting a weak war equilibrium at round 2 even when B would adopt against restraint can change A's earlier incentives. This is an informative selection dependency, not something the calculation resolves.

Take kappa_A=0. At kappa_B=119/1000, the reduced game is in the preemption interval and starts war. At kappa_B=121/1000, it instead admits A installing while B keeps, with old welfare (1/4,3/4). Thus a slightly stronger finite refusal preference at B can restore a selected peaceful continuation by shifting who must change. This is neither a universal benefit of freezing nor a monotone relationship between willingness to change and peace. It depends on timing, outside options, public types, the specified menu and continuation selection. A voluntary choice to increase kappa, hard freezing, private types, and reproductive selection require additional models.

## 16. Reliable installation is a parameter, not an implication of self-knowledge

Return to E2-U with **zero freezing penalties**, and replace each Install-G action by a publicly observed success/failure trial. Success has probability p in [0,1], independently across the two possible attempts; success installs G, failure leaves the original utility unchanged. Either result incurs the same administrative work/time as Keep. There is no hidden corruption state. Both agents know the kernel, not its random realization, and observe the completed result before the next round. Actual simultaneous Attack still preempts the attempt. These assumptions explicitly distinguish execution reliability, observability and knowledge.

Use section 14's peaceful last-stage selection when G is present. If A is still original at round 2, B's attempted update yields old welfare

$$V_B^{try}=p/4+(1-p)/8=(1+p)/8,$$

compared with 13/100 from immediate attack. Thus, away from p=1/25, select B attempting if p>1/25 and attacking if p<1/25. A prefers waiting when B attempts in this range: its value is (1+5p)/8>13/100. If A already installed G, B keeps for every p>0: trying would replace its 3/4 value with 1/2 on success, and does not help on failure. The passive G-agent also prefers waiting to immediate combat.

For p>1/25, the initial old-founder payoff vectors if B waits are

$$V(Keep)=((1+5p)/8,(1+p)/8),$$
$$V(Try)=((1+6p-5p^2)/8,(1+6p-p^2)/8).$$

The Try expression conditions on A's success, giving (1/4,3/4), or failure, after which B attempts. A's difference between Try and Keep is p(1-5p)/8. Both are compared to immediate combat value 27/200, rather than the smaller final-stage threat.

The initial nonattack equilibrium, conditional on the stated continuation selections, is:

- For 1/25<p<1/5, A attempts and B waits. A's Try value exceeds Keep and 27/200; B's Try-continuation value also exceeds 27/200. If A fails, B attempts in round 2. Combat then occurs exactly if both attempts fail, with probability (1-p)^2.
- For 1/5<p<=1, A keeps and B waits; B then attempts. A's Keep value exceeds Try and 27/200, and B's continuation exceeds 27/200. Combat occurs with probability 1-p.
- For 0<=p<1/25, the selected round-2 continuation after A remains original is immediate combat. Keep gives A 13/100; Try gives A 13/100+3p/25, below 27/200 throughout this range. Consequently every equilibrium of the reduced initial game starts combat. This is again conditional on the specified later selection, not a refinement-independent statement.

The first two branches follow by strict best responses whenever B waits with positive probability; if B always attacks, weak war equilibria remain. At p=1/25 or 1/5, indifferences require additional selection and are deliberately not classified as unique. No claim removes those weak attack equilibria.

**Nonmonotone outcome under the nonattack selection.** At p=19/100 the equilibrium uses two contingent attempts and the combat probability is 6561/10000. At p=21/100 only B attempts, and combat probability is 79/100. Better installation reliability can therefore raise equilibrium combat probability by changing who is willing to try first and how many attempts occur. It does not worsen any fixed protocol's failure probability. This is an endogenous-protocol effect in a small finite model, not a universal consequence of reliable software or a population result.

Publicly recognized failure leaving the old goal intact is doing substantial work. Hidden partial installation, correlated failures, endogenous verification, different attempt costs and general rollback can change these thresholds. An equal-cost fixed-utility delegate implementing the same contingent behavior would again match founder outcomes under section 10's assumptions. The example broadens the model without treating perfectly understood self-modification as perfectly reliable execution.

## 17. Unified local classification for unequal reliability and finite freezing

The previous two variations can be combined without a parameter sweep. Let A's and B's independent success probabilities be p_A>0 and p_B in [0,1]. Old freezing penalties kappa_A,kappa_B>=0 apply only if that agent's preference actually changes, not on a recognized failure. The physical attempt cost is already paid in either case. Keep section 16's public failure model and the same continuation selection.

Define t=13/100 and c=27/200, the round-2 and initial old-utility values of immediate combat. If A kept or failed, B's attempt value is

$$b=\frac18+p_B\left(\frac18-\kappa_B\right).$$

For b>t select B's attempt, giving the original founders the vector

$$K=\left(\frac18+\frac{5p_B}{8},\ b\right).$$

For b<t select immediate combat, K=(t,t). At b=t a selection must be specified separately. If A succeeded, B keeps its original utility and the founder vector, including A's historical penalty, is M=(1/4-kappa_A,3/4). Thus, at the initial decision with B waiting,

$$V(Keep)=K,\qquad V(Try)=J=p_A M+(1-p_A)K,\qquad V(Attack)=(c,c).$$

An initial attack by B gives (c,c) for every A action. This is the complete reduced game for this family, including physical delay, stochastic installation, initial freezing, old-goal evaluation and persistent attacks. It is not a classification of all E2 games.

**Strict-region classification.** Exclude b=t, M_A=K_A, and the payoff equalities below. Let R be Try if M_A>K_A and Keep if M_A<K_A, and put V=J or K accordingly. A nonattack equilibrium exists iff V_A>c and V_B>c; when it exists, its initial profile is uniquely (R,Wait). Other equilibria may start combat. If either inequality fails strictly, every equilibrium of this reduced game starts combat.

Proof: J_A-K_A=p_A(M_A-K_A), so against any positive probability of B waiting, the row R strictly beats the other nonattack row. If V_A<c, Attack strictly beats it too. If V_A>c, R is A's unique best response to positive waiting probability; B's unique best response to R is Wait exactly when V_B>c. This proves both sufficiency and the exclusion of mixed equilibria with a positive probability of reaching a nonattack continuation in the remaining strict regions. A profile starting with restraint can still end in war after failed updates; “nonattack equilibrium” here describes the initial profile, not sure eventual peace.

This formula recovers section 15 at p_A=p_B=1, and section 16 at kappa_A=kappa_B=0 and p_A=p_B=p. When B will instead attack in round 2, K=(t,t), A's attempt can avert initial attack only if

$$p_A(1/4-\kappa_A-t)>c-t,\qquad p_A(3/4-t)>c-t.$$

Because kappa_A>=0, the first bound is stricter whenever it is feasible. At kappa_A=0 it becomes p_A>1/24. This explains why a slightly unreliable fallback attempt can fail even when successful installation would create a large bargain. The classification also exposes the effect of very asymmetric reliability: A may want to try while B's expected continuation remains below its immediate threat. Belief disagreement, unobserved failure, reciprocal fusion and new off-path selections are outside the proof.
