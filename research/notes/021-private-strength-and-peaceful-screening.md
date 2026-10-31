# R0001 working note: private strength, offers, and verification

This is a local asymmetric-information module of E2, not an assertion that strength is always private. Proofs are AI self-checked only. The elementary bargaining machinery is not claimed as new. In particular, a known stochastic contest law does not reveal its private strength parameter or the random winner.

The nearest primary comparison is Fearon (1995), pp. 394–396 and appendix pp. 410–414, including the take-it-or-leave-it and restricted cheap-talk arguments. Its private-cost model differs from this note's private-strength calculation; see L01's exact audit scope in the [literature ledger](../LITERATURE.md). [Original article](https://pages.ucsd.edu/~bslantchev/courses/pdf/Fearon%20-%20Rationalist%20Explanations%20for%20War.pdf).

## 1. A restricted but explicit information structure

A's effective strength gives its combat probability Q in [l,h], where 0<l<h<1; B knows the distribution F and A knows its realized Q. For example, B's strength is b and A's strength is bQ/(1-Q), so the E2 contest rule gives exactly Q. Ordinary uncontracted operator selection can use that same probability. The agreement route considered here instead binds a declared allocation; an uncontrolled operator draw is not silently treated as an enforceable agreement.

Original utilities are own-color quantities. A completed peace produces P units and war produces W<P units, all in the winner's color. The physical recovery module supplies these two frontiers after the costs common to the bargaining checkpoint. No war realization is known in advance. Strength has no other effect on the *agreement route*: every type can send the same reports, install the same available templates, and execute the same allocation. This last assumption is essential. A public strength-dependent production signal or a different type-dependent implementation cost changes the result.

Attack remains feasible before the offer, in response to it, and at the final production checkpoint. The split execution device is binding at that checkpoint but does not remove combat. After completed delivery the local game is terminal; later expropriation would require a new continuation. This is an enforceable-split comparison, with stronger implementation capability than a revocable promise. Conditional on acceptance, beliefs and attack incentives are checked below.

The threat payoffs are QW for A and (1-Q)W for B. Write mu=E[Q] and Delta=P-W. No private freezing or modification penalty is included in this module.

The local offer/response formulas idealize their additional marginal cost as zero after setup costs have been debited in the stated frontiers. They are not claims that communication or computation is physically free. With nonzero marginal message costs, use dated frontiers and recheck each participation condition, as section 6 does for testing. This explicit zero-cost local comparison does not replace E2's physical cost accounting.

## 2. A peaceful report cannot identify strength for free

Consider a direct mechanism that always ends peacefully and assigns expected A output x(r) from report r. Its allocation kernel, costs, and feasible actions conditional on a report do not otherwise depend on the true Q. Every type evaluates every report by the same number x(r). Thus truthful incentive compatibility implies

$$x(q)\geq x(r)\quad\hbox{for all }q,r,$$

and hence x is constant on the type support. This is equality of expected allocations, not necessarily equality of lotteries. With linear original utilities, different lotteries having the same mean do not produce strict revelation either.

For all types to participate instead of attacking, the constant x must satisfy x>=hW (replace h by the essential supremum for an almost-sure condition). B's prior participation requires P-x>=(1-mu)W. Therefore an always-peaceful, type-neutral allocation with weak participation exists exactly when

$$\boxed{\Delta\geq W(h-\mu).}$$

Strict participation for every supported type, including h, is possible when the inequality is strict. A pooled fixed split attains the bound. When all types accept, observing acceptance does not change B's prior, so the same B condition applies at the final checkpoint. A's pointwise condition also continues to hold. This establishes a peaceful equilibrium continuation under the binding split technology, not that every negotiation game selects it.

Publicly observing an installed utility template does not invalidate this argument when every original type can select the same template at the same cost and obtains the same peaceful output from it. The original agent evaluates the report/adoption under its current own-color utility. Templates can alter later incentives without certifying the original strength. Type-dependent physical signals, collateral, testing, unequal implementation costs, or a combat branch can make the report's consequences type dependent and are outside this particular impossibility statement.

## 3. A proposer can prefer an offer that sometimes starts war

Let B make one binding offer x=qW, with q in [l,h]. A accepts if Q<=q and attacks otherwise. Select acceptance at exact indifference; for atomless F this choice changes no ex ante probability. A also retains Attack after accepting. Accepted types get at least their war payoff, so the selected final continuation is sequentially rational.

B's expected payoff is

$$V(q)=F(q)(P-qW)+W\int_{(q,h]}(1-t)\,dF(t).$$

An equivalent formula, valid with atoms, is

$$V(q)=W(1-\mu)+\Delta F(q)-W\int_l^q F(t)\,dt.$$

To verify it, A gets its war baseline Wmu plus the rent W E[(q-Q)_+]; total expected output is W+Delta F(q), and E[(q-Q)_+]=integral_l^q F(t)dt. Endpoint atoms are handled by the stated acceptance convention.

B must also prefer restraint after an offer has been accepted. Conditional on Q<=q, its gain from the split over immediate war is

$$\Delta-W\{q-E[Q\mid Q\leq q]\}.$$

Multiplying by F(q) gives V(q)-W(1-mu). Thus any selected offer with V(q)>=B's initial attack payoff also gives B weakly optimal restraint after acceptance. This uses the same W at the two checkpoints; costs spent between them require the dated-frontier adjustment in section 6. No action is removed to obtain this conclusion.

Full-pooling peace corresponds to q=h. Comparing all offers gives the exact proposer-selection condition

$$\boxed{\Delta\geq W\sup_{q<h,\ F(q)<1}
 \frac{\int_q^h F(t)\,dt}{1-F(q)}.}$$

Indeed V(q)-V(h)=W integral_q^h F(t)dt-Delta(1-F(q)). The threshold is generally stronger than peaceful participation. Maximization and boundary attainment must be checked for the chosen distribution; the explicit distributions below have attained optima. No general claim about arbitrary discontinuous menus is needed.

### Two strengths

Let Pr(Q=h)=pi in (0,1), and Pr(Q=l)=1-pi. Only q=l and q=h need be considered: within an interval with no additional accepting type, raising the offer strictly lowers B's payoff. The low offer induces war with probability pi; the high offer induces peace. Their difference is

$$V(l)-V(h)=(1-\pi)(h-l)W-\pi\Delta.$$

The low offer beats immediate war by (1-pi)Delta>0. Thus the selected proposer optimum is peaceful exactly when

$$\Delta\geq\frac{1-\pi}{\pi}(h-l)W,$$

with indifference at equality. Yet a pooled split acceptable to both exists already at Delta>=(1-pi)(h-l)W. The nonempty interval between these thresholds separates existence/participation from offer incentives.

For l=1/4, h=3/4, pi=1/2, W=4/5, P=11/10, Delta=3/10. Pooling at x=3/5 gives (3/5,1/2), above A's weak-type threat and B's prior threat 2/5, and equal to A's strong-type threat. A slightly higher x gives both strict participation. But B's low offer x=1/5 yields payoff 11/20, exceeding the pooling offer's 1/2, and starts war against the strong type. The example retains an individually acceptable, credible peaceful split while exhibiting a profitable screening offer.

### Uniform strengths

If Q is uniform on [l,h], differentiating the displayed V gives

$$V'(q)=\frac{\Delta-W(q-l)}{h-l}.$$

The unique maximizer is q*=min(h,l+Delta/W). Its combat probability is

$$\Pr(\mathrm{war})=\max\{0,1-\Delta/[W(h-l)]\}.$$

Pooling participation requires only Delta>=W(h-l)/2, whereas the optimal offer is fully peaceful only at Delta>=W(h-l). These are exact statements for this ultimatum protocol, not an impossibility of all more elaborate bargaining.

## 4. The value of a public strength test under matched costs

For the two-type case, a costless public test followed by the same proposer power yields expected B payoff P-mu W: the offer can equal the revealed type's threat. Relative to the best untested offer, the gain is

$$I=\min\{(1-\pi)(h-l)W,\ \pi\Delta\}.$$

This follows by subtracting V(h) and V(l), respectively. It is a private informational benefit to the proposer, not a social surplus calculation. Testing can redistribute rents as well as avoid combat.

If a *specified* test consumes resources so the new frontiers are P_c,W_c, the corresponding post-test payoff is P_c-mu W_c. One cannot simply subtract a scalar test price from I unless that scalar correctly describes these transitions and all parties' earlier participation. In particular, knowing a test is accurate says nothing about whether agents willingly wait for it.

## 5. A public signal can change revelation, but it is extra structure

Suppose a publicly observed bit Z is generated with Pr(Z=1|Q)=Q by the ordinary strength-weighted control device, and a protected execution device can condition A's allocation on Z without changing the contest strengths. For reports r in {l,h}, the expected score

$$E[2rZ-r^2\mid Q]=Q^2-(r-Q)^2$$

is uniquely maximized at r=Q. Therefore an allocation x(r,Z)=c+eta(2rZ-r^2), eta>0, can elicit strength strictly when its full range fits inside the sequential participation constraints.

For both reported types and both signal realizations, a sufficient common interval is

$$[hW,\ lW+\Delta].$$

It is nonempty with positive width exactly when Delta>(h-l)W. Since the score range over r in {l,h}, Z in {0,1} has width 2h, choose 0<eta<\{Delta-(h-l)W\}/(2h) and shift c to place every allocation strictly inside that interval. Every actual type then prefers acceptance to combat at every signal; B also does so even if it learns the true type. Truthful reporting gives a strict expected advantage eta(h-l)^2 over the other report. Subsequent deviation to combat cannot improve a misreport's payoff because all allocations lie above every A threat.

This is a sufficient implementation, not an optimal revelation threshold. It requires an actual strength-dependent signal, a report-independent signal law, and binding conditional execution. A utility declaration alone supplies none of these. Signal collection and commitment costs must be included in P,W or in earlier dated frontiers. The construction also illustrates why the type-neutral-kernel condition in section 2 cannot be dropped.

## 6. Testing can create a hold-up problem

Suppose waiting for a public test changes the war frontier from W_0 to W_1<W_0. After the test, a B-proposer with no prior binding promise offers the revealed type exactly QW_1, extracting the remaining output; suppose peace is feasible and continuation selection is as above. Original A then gets QW_1 by waiting, strictly less than QW_0 from attacking before the test. Every type therefore preempts. A larger post-test peace frontier does not repair this incentive by itself.

A binding pre-test contingent offer x(Q)=QW_0 preserves A's earlier threat value. If P_1>=W_0 and W_1<=W_0, then, for every Q,

$$x(Q)\geq QW_1,\qquad
P_1-x(Q)\geq(1-Q)W_1.$$

B's prior value P_1-mu W_0 is at least its original threat (1-mu)W_0. Thus this stronger mechanism can sustain weak participation at the early and late checkpoints; a small positive slack allocation gives strict participation when P_1>W_0. The test must reveal true Q before executing its contingent allocation, and the earlier promise must actually bind. With arbitrary intermediate cost states, repeat these inequalities at every checkpoint; endpoint conditions alone do not prove uninterrupted stability.

This is the information-acquisition counterpart of note 020's proposal-revision obstruction. Both show why informational accuracy, semantic observability, and commitment must be represented separately. A fixed-utility delegate given exactly the same contingent test/allocation capability matches the original welfare; utility modification is not established as an exclusive source of the benefit.

## 7. Limits and next removal tests

The results concern original linear color goals, one-sided private strength, a declared offer protocol, and a protected split route. They do not solve two-sided private values, unbounded bargaining, risk aversion, correlated private information, false public test results, endogenous evidence suppression, or physical combat during each bit of a test. The no-war reporting bound does not apply when strength changes the peaceful production kernel. The signal construction explicitly demonstrates one such exception.

The relevant unresolved comparison is a costly, fallible, interruptible public test with endogenous refusal and a matched ordinary delegate. It must track how verification changes both beliefs and the physical threat frontier, rather than treating better information as automatically peace-promoting.

## 8. More public information can increase combat under the selected offers

Return to two strengths and write D=(h-l)W. A public test produces a posterior p=Pr(Q=h|signal). Signals have no additional physical cost in this subsection. From section 3, the proposer pools at the high offer exactly when

$$p\geq\theta:=\frac{D}{D+\Delta},$$

and otherwise makes the low offer, causing conditional combat probability p. At equality either offer is optimal; all examples use strict inequalities. Therefore the overall combat probability is

$$\mathcal W=E[p\,1\{p<\theta\}].$$

Bayes plausibility requires E[p]=pi. The proposer's optimal value is the maximum of two affine functions of p, so a public refinement of information weakly raises its expected payoff when physical costs are matched. The displayed combat function is not convex or concave; no corresponding monotonicity follows for combat.

For l=1/4, h=3/4, W=4/5, P=11/10 and pi=4/5, theta=4/7. Without a signal, the high offer is strictly optimal and combat probability is zero. Now give a binary public test that correctly labels each type with probability 9/10. Its posteriors are 36/37 after the high label and 4/13 after the low label. The proposer pools after the former and screens after the latter. Combat occurs precisely for a strong type receiving a low label, with probability 2/25.

The expected old-agent welfare changes from (3/5,1/2) without the test to

$$ (66/125,\ 137/250)=(0.528,0.548). $$

Total production falls from 11/10 to 269/250=1.076, exactly the loss Delta times 2/25. B gains 6/125 while A loses 9/125. The weak type still obtains 6/25>its pre-test war payoff 1/5; the strong type obtains 3/5, equal to its war payoff. Thus the test's adverse effect on A relative to the untested equilibrium does not by itself force preemption. A small fixed offer increment can make the latter participation strict without changing the strict screening choices, although it changes the exact numerical payoffs.

Perfect revelation instead gives no combat: the low offer is accepted when the type is known low, and the high offer is accepted when known high. The example is a comparison of available information structures, not a claim that an agent with free access to a perfect test would deliberately choose the inferior test. A limited menu consisting of no test and this fallible test makes the proposer's preference for testing explicit.

### An exact bound over public information structures

For any public experiment and the strict low-offer region,

$$\mathcal W\leq\min\{\pi,\ \theta(1-\pi)/(1-\theta)\}
 =\min\{\pi,\ (1-\pi)D/\Delta\}.$$

The first inequality is immediate from E[p]=pi. On p<theta, (1-p)>=(1-theta)p/theta; integrating gives the second bound. If pi<theta, no information attains the first bound. If pi>=theta, take posteriors theta-epsilon and 1, with the former occurring with probability (1-pi)/(1-theta+epsilon). This is a valid binary experiment: assigning those joint masses to each true type produces nonnegative conditional signal probabilities summing to one. Its combat probability tends to theta(1-pi)/(1-theta) as epsilon decreases to zero. Thus the bound is a supremum; it is attained at the boundary only if the tie selection there permits the low offer. Perfect revelation attains the minimum zero.

This classifies a worst case over allowed public experiments for the selected offer game. It is not an equilibrium claim that an information provider chooses that experiment, and it is not a distribution-free claim about other bargaining protocols.

### Exact peace can be more demanding after a fallible signal

With full-support signals, both strength types remain possible at every signal. Section 2's pooled-peace threshold after signal z is Delta>=(1-p_z)D. Under a nonconstant posterior, some p_z<pi, so the worst conditional requirement is stronger than the prior requirement. For pi=1/2, symmetric test accuracy 9/10, and the same D=2/5, Delta=3/10, peace is feasible before observing a signal because 3/10>1/5. After the low signal, however, it would require 3/10>=9/25, which fails.

At a perfectly revealing signal the low branch's support changes to the singleton {l}; its h in section 2 is l, and the information rent disappears. The discontinuity concerns the requirement of zero combat for every supported type, including arbitrarily unlikely misclassified strong types. It does not imply that expected combat stays high as error probability tends to zero. This is an additional reason to distinguish exact stability, approximate risk bounds, and population-average outcomes.
