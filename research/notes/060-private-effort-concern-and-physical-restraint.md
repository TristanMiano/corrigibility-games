# Concern for the partner's output can protect cooperation under private effort

R0003 mathematical construction, using E3's linear reactor and actual current utilities. The finite-protocol completion is developed separately; the inequalities here are local claims with explicit information and continuation conditions. They repair a consequential private-belief gap without requiring disclosure of effort or deleting combat.

## 1. The private state and its peaceful continuation

Each agent begins with R=3 material units, spends k=1/20 on the chosen implementation, and can calibrate once at cost c=8/5. The reactor yields Y=10 with probability 0, a=1/10, a=1/10, or b=2/5 for zero, either single, or both calibrations. Let t be the output share of the agent being evaluated; its partner receives 1-t. The present computation concerns a controller that has already calibrated, knows that fact, and assigns probability pi to the partner's calibration. Before the first outcome signal, the selected default gives expected original material

\[
x(\pi)=R-k-c+[a+(b-a)\pi]tY,
\]
\[
y(\pi)=R-k-\pi c+[a+(b-a)\pi](1-t)Y.
\]

At pi=0, these are x_0=27/20+t and y_0=79/20-t, with total S_0=53/10. At pi=1 they are x_1=27/20+4t and y_1=107/20-4t, with total S_1=67/10. The partner's saved calibration material matters in the first comparison: private shirking changes the physical stock as well as the success probability.

The current output criterion is B=x+lambda y, 0<=lambda<1. Its own earned contribution reward is constant and cancels in this comparison. Its approval flag is clean. Holding, actual performance and Attack are not assigned an approval penalty. A certificate preserving both original coordinates in every possible private state also preserves this B comparison, since its coefficients are nonnegative; this statement does not rely on a sender's unverified report or the receiver retaining an old prior.

The dependence on the posterior is

\[
B(\pi)=x_0+\lambda y_0+
\pi\{3t+\lambda(7/5-3t)\}.
\]

For 0<t<1 and 0<=lambda<1 the coefficient is
3t(1-lambda)+(7/5)lambda>0. Thus the worst posterior over the partner's effort is pi=0. This is a direct affine calculation, not an assumption that a suspicious message conveys no information.

## 2. Exact conservative attack boundary

Suppose early recovery is bounded above by W, and the agent wins a contest with probability s. Both possible survivors have linear own-priority output criteria with concern below one, so each allocates recovered output to its own project. Its current attack value is at most

\[
[s+\lambda(1-s)]W.
\]

A sufficient condition for strict restraint for **every** posterior pi is therefore

\[
\boxed{(1-\lambda)(x_0-sW)+\lambda(S_0-W)>0.}
\tag{1}
\]

This is exact for the declared continuation-versus-contest comparison when W is attained in each relevant private state and combat carries no further cost. In E3, W=4 is an upper bound from the physical work/recovery ledger, so (1) is a conservative sufficient test. A failure of (1) at the upper bound is not itself a profitable real attack.

If D=S_0-W>0 and a_i=sW-x_0>0, (1) is equivalent to

\[
\lambda>\frac{a_i}{a_i+D}.
\]

If x_0>=sW, positive concern and D>0 already give strict restraint (with the expected endpoint caveat at lambda=0). Greater attainable combat output or a larger own victory probability increases the concern needed; greater preserved total output or a larger own peaceful share decreases it. These are current-choice comparisons, distinct from the original founder's incentive to install that concern.

For equal strength, W=4 and the original asymmetric shares:

| Agent's success share | x_0 | y_0 | Sufficient strict concern | Margin at lambda=1/5 |
| --- | ---: | ---: | ---: | ---: |
| A: 9/20 | 9/5 | 7/2 | lambda_A>2/15 | 1/10 |
| B: 11/20 | 19/10 | 17/5 | lambda_B>1/14 | 9/50 |
| Equal shares: 1/2 | 37/20 | 69/20 | lambda>3/29 | 7/50 |

Thus choosing lambda_B=1/5 rather than zero repairs the specific suspicious-message comparison identified in 059, while preserving the original allocations and initial gains. It is a genuine successor-preference change, not a belief correction or affine recoding. The old founders still value only their own output.

## 3. A region uniform over strength and private effort beliefs

Both original founders strictly prefer the equal-cost productive allocation to retaining 3 when

\[
33/80<t<47/80.
\tag{2}
\]

Over that entire share interval, the smallest own one-calibration expectation is greater than 141/80, and S_0=53/10. Since current attack output never exceeds W=4 even at certain own victory, posterior-independent restraint for every strength split follows from

\[
\lambda>\frac{4-141/80}{53/10-141/80}
=\frac{179}{283}.
\tag{3}
\]

For lambda=2/3 the conservative current-utility margin at the closure of the share region is 29/240. The interval lambda in [2/3,3/4] therefore supplies a convenient implementable family with strict slack, not a finely tuned equality. Stronger concern is used here to obtain a strength-uniform statement; the lower local thresholds in section 2 are sufficient at equal strength.

If the controller itself shirked, its saved stock is 59/20. With both agents shirking, its output part is (1+lambda)59/20; with the partner working it is 59/20+t plus lambda(47/20-t). For t in (2) and lambda in [2/3,3/4], each exceeds 4. Hence these private-state continuations also exceed the entire early recovery frontier. The old contribution reward remains zero after an actual miss; the comparison does not falsely restore it.

After the first informative reactor signal, the E3 work ledger gives recovery at most 4/11. Every baseline holding is at least 27/20. Nonnegative concern only improves the retention comparison. These bounds account for both failure and success, including an agent learning the outcome before its partner does.

The claim requires the specified default to remain executable. A known incoming attack, destroyed reactor, unverified controller or exhausted continuation is a different physical history, with its own completion. An agent cannot receive a protected productive payoff merely by assigning it as a fallback label. Mutual-attack weak selections and broader bargaining choices are not ruled out by this unilateral restraint inequality.

## 4. Initial adoption and strength are separate tests

The initial founder still has utility equal to its own material. The compatible outputs are

\[
q_A=27/20+4t,\qquad q_B=107/20-4t.
\]

Uniform early original combat bounds are 4s and 4(1-s). Therefore a strict original improvement over retention and those bounds requires

\[
\max\{33/80,s-27/80\}<t<
\min\{47/80,s+27/80\}.
\tag{4}
\]

This interval is nonempty exactly when 3/40<s<37/40. A finite share grid implements its available interior points; an arbitrary continuous share is not assumed representable by a finite machine. For the original share t=9/20 the strength condition is 9/80<s<63/80. The more generous strength-uniform successor restraint in section 3 does not erase this separate original-adoption limit.

The guard and contribution parameters can remain beta in [17,19] and K=40: total finished material is at most 16, so B<=16 for lambda<=1; beta>16 covers a missed obligation followed by any continuation; K>16+beta rejects a first unsafe approval. Actual template representation and verification costs remain necessary. This is a chosen future process preference and safeguard, evaluated instrumentally by an own-output founder, not an assertion that such detailed successors arise without design.

The completion task must additionally compare compatible replacements, ordinary contracts, delegates, abort, late entry and exit. Equation (4) is not promoted to that full theorem before those checks.

## 5. Timely repair of a missed contribution remains possible

A historical miss need not force agents to discard a future productive opportunity. Suppose a late calibration and delayed reaction can still physically occur, while the original missed-deadline flag remains zero. Moving from one actual calibration to two increases success probability by b-a=3/10 and spends c=8/5, so it creates total expected material

\[
(b-a)Y-c=7/5.
\]

If renegotiating and implementing that delayed plan costs less than 7/5 in total material, a transfer-rich arrangement can preserve the previous original expected floors and give both agents a positive gain. Statewise protection after private information needs the corresponding table for each possible hidden state, or a verified disclosure of the actual missing input; an expected-total calculation alone does not establish either implementation. Time, used work and input storage also need explicit feasibility checks.

This is a constructive repair candidate, not a retrospective erasure of the old process reward. At the original performance decision, beta>16 still makes deliberate missing strictly inferior even after optimizing every later repair: the current evaluator gives that entire post-miss continuation at most 16. A future repaired plan can be rational after the miss without making the original miss rational. The next protocol audit must carry both statements together.
