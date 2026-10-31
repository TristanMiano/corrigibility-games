# R0001 working note — deception, repair, and credible inspection

This note extends the staged merger in note 012. Detection, punishment, verification incentives and initial adoption are different questions. The calculations below supply conditional results for a declared finite protocol; they do not give utility self-knowledge the force of public semantic verification. Proofs are self-checked only.

## 1. A detected bad proposal may still be worth making

At the partial-controller checkpoint of note 012, take equal strengths, total output one, and current successor criterion g_lambda with lambda=9/100. Write

$$g(\beta)=\frac{\sqrt\beta+\sqrt{1-\beta}}{\sqrt2},\qquad
L=\frac{1+1/\sqrt2}{2}.$$

The honest final share is beta=1/5; a deceptive actual template instead installs beta=1/16 while claiming the honest template. Original B's outputs are 4/5 if honest, 15/16 if undetected, and 3/4 on rejection. F's corresponding current values are g(1/5)-9/100, g(1/16)-9/100 and L. Thus honest acceptance has current surplus

$$h=g(1/5)-9/100-L>0,$$

whereas accepting deception has current loss

$$\ell=L-g(1/16)+9/100>0.$$

Numerically h is about 0.00513 and ell about 0.08212. These are F's own utility units, not work units or B's utility units.

If a detected bad proposal is actually rejected, detection probability d deters B exactly when

$$ (1-d)\frac{15}{16}+d\frac34\le\frac45,
\quad\text{or}\quad d\ge\frac{11}{15}.$$

But suppose detection merely leads to cheap repair, after which B obtains its honest 4/5. With no additional private cheating cost, any d<1 leaves deception strictly profitable: its payoff becomes (1-d)15/16+d4/5. One must establish the credibility of rejection against the *whole* feasible repair and renegotiation menu. Checking only whether the original proposed split survives a repair cost is insufficient; the parties may change the split, retain their goals, transfer output early, or use a fixed-utility controller.

## 2. A sufficient physical obstruction to consensual repair

Here is a useful conditional bound. Suppose rejecting the candidate preserves the separate-controller continuation with current values (L,3/4). Suppose every alternative consensual repair route, including transfers and lotteries, has total physical output at most R. B must voluntarily accept that route. Ignore F's goal-change penalty when bounding its repair payoff; this makes the bound generous and includes goal-preserving repairs.

For R=17/20, any B-acceptable repair has E[x_B]>=3/4 and therefore E[x_A]<=1/10. By concavity of the output criterion,

$$E[g(x_A,x_B)]\le g(E[x_A],E[x_B])
\le g(1/10,3/4)<L.$$

Here g(x_A,x_B)=(sqrt(x_A)+sqrt(x_B))/sqrt(2). To justify the second inequality, first use monotonicity to put the mean on the total-R frontier, then note that g(R-b,b) decreases for b>=3/4>R/2. A simple exact certificate for the final strict comparison is sqrt(1/10)<317/1000, sqrt(3/4)<867/1000 and sqrt(2)>1414/1000, giving g(1/10,3/4)<592/707<17/20<L. No repair lottery or omitted goal-change penalty can overturn this upper bound.

This is a condition on actual available mechanisms, not an intrinsic cost of dishonesty. For example, in a restricted single-batch controller implementation, a detected candidate may require rebuilding a physical integration latch before any consensual replacement route is usable. At note 012's third checkpoint the work stock is 107/100. An unavoidable rebuild consuming at least 22/100 work leaves at most 17/20 output even before further operations, when production consumes one work unit per output unit. Rejecting the integration candidate leaves the independent production apparatus usable and its total output one. Such a mechanism must explicitly account for why every binding alternative needs that latch; its rebuild cost does not follow from thermodynamics or from the fact of deception.

If a cheap enforceable transfer route bypasses the latch, the stated bound on all repair routes is false. Note 012's goal-preserving route then applies, subject to its explicit control-transfer requirement; that note also shows why an unsecured prepayment alone is insufficient. Likewise a cheap binding delegate or fresh unaffected integration unit can invalidate the bound. The numerical example therefore supports a **conditional credible-rejection model**, not a claim that the broader E2 mechanism already excludes every repair. More generally, one should compute the post-detection feasible payoff set and test whether it contains a mutually acceptable alternative to rejection.

Combat remains physically available. In the equal-strength example with war output W<=27/100, F's current expected output-goal value from combat is sqrt(W)L<L, before any extra penalties; B's combat output is at most W<3/4. Thus neither prefers attacking to the selected rejection continuation. Rejection is supported by actual continuation values, not an imposed prohibition on attack or an arbitrary punishment utility.

## 3. Inspection followed by a real accept/reject decision

Let B privately choose an honest or deceptive candidate. F chooses whether to inspect without observing that choice, and B does not observe the inspection draw before choosing its candidate. Inspection detects a deceptive candidate with probability delta in (0,1], with no false positive in this benchmark. F then sees its inspection result and chooses Accept or Reject. A detected deception has the credible rejection continuation established separately above. Actual installation and loss of the old controller's authority occur only after acceptance, through the specified finite protocol. The ability to check this restricted template probabilistically is an additional implementation primitive.

Allow inspection to change the physical continuations. Denote F's reject values by R_0 without inspection and R_1 with inspection. Let h_j>0 be the surplus of honest acceptance over R_j and ell_j>0 the loss from accepting a bad template relative to R_j. Let z be B's probability of deception. Sequential optimization gives F the values

$$V_0(z)=R_0+\max\{(1-z)h_0-z\ell_0,0\},$$
$$V_1(z)=R_1+\max\{(1-z)h_1-z(1-\delta)\ell_1,0\}.$$

The inspection expression includes rejection on the detected branch. Conditional on a passed test, the posterior probability of deception is z(1-delta)/(1-z delta), whenever that event has positive probability. Multiplying the conditional acceptance gain by the pass probability gives the displayed numerator. These formulas permit rejection after a passed test; treating every undetected proposal as automatically accepted can overstate both trade and inspection incentives.

Physical communication, computation, verification and update costs should be propagated into the branch values before this comparison. A utility cost cannot be inferred merely by naming an energy expenditure. Different verification technologies can change R_j, h_j, ell_j and B's payoffs in different ways.

## 4. An additive-cost benchmark with an explicit physical interpretation

For a tractable specialization, let R_1=R_0-c with c>0, and h_0=h_1=h, ell_0=ell_1=ell. This can represent a separate inspection work reservoir whose residual useful work F values linearly: an extended current criterion is g(main output)+gamma E_reserve minus its stated change penalty. Inspection spends e units from that reservoir, so c=gamma e. Its work cannot be transferred to the main production line before the deadline, and post-detection repair does not increase its remaining stock. Main production and B's output are unaffected in this particular control. This is an explicitly extended objective and resource state, not an identification of g, work and conserved energy. A shared production battery instead requires the general branch formulas above.

Assume B's acceptance gains over rejection are h_B>0 when honest and g_B>h_B when deceptive, and inspecting has no additional direct effect on these gains. Honest and deceptive preparation have equal already-accounted costs in this benchmark. Deception is an actual hidden installation choice, not a utility declaration that the verifier simply trusts.

Without inspection F accepts iff z<=z_0=h/(h+ell). After an inspection pass F accepts iff z<=z_1=h/[h+(1-delta)ell]. Suppose

$$0<c<\frac{\delta\ell h}{h+\ell}.$$

Define

$$z_a=\frac{c}{\delta\ell},\qquad
z_b=\frac{h-c}{h+(1-\delta)\ell}.$$

Then z_a<z_0<z_b<=z_1. F's optimal complete strategies are:

- z<z_a: do not inspect; accept.
- z_a<z<z_b: inspect; accept a pass and reject a detected deception.
- z>z_b: do not inspect; reject.

At the two boundary values the neighboring strategies tie. Proof: when both untested and passed proposals would be accepted, V_1-V_0=-c+z delta ell. When an untested proposal would be rejected but a passed proposal accepted, V_1-V_0=-c+(1-z)h-z(1-delta)ell. When both would be rejected, inspection only wastes c. The assumed bound on c places the first crossing below z_0 and the second above it. The formulas also cover delta=1, with the usual care at zero-probability pass histories.

Thus the standard comparison c<delta ell is not enough to support an accepted-trade inspection equilibrium. Inspection must also be worthwhile relative to refusing trade altogether, which introduces the current honest surplus h.

## 5. A mixed sequential equilibrium with accepted trade

In addition to the preceding strict cost bound, assume

$$\delta g_B>g_B-h_B.$$

There is a sequentially rational mixed profile with

$$p_{inspect}=\frac{g_B-h_B}{\delta g_B}\in(0,1),
\qquad z_{deceive}=\frac{c}{\delta\ell}\in(0,z_0).$$

F mixes between inspecting and not inspecting, accepts every untested proposal and every pass, and rejects a detected bad template. B mixes between honest and deceptive candidates. At the displayed inspection rate, B's deceptive gain (1-p_inspect delta)g_B equals h_B. At the displayed deception rate, F is indifferent about inspection. Because z_deceive<z_0, both untested and pass acceptance are strictly optimal; rejection of a detected bad template is strictly optimal. Bayes' rule supplies the pass beliefs. Completely mixed approximations generate these beliefs, so the finite hidden-action game has the corresponding sequential-equilibrium assessment. Extra physical checkpoints with no new information preserve it when their attack and withdrawal alternatives are strictly worse than the stated continuation values.

For the numerical merger values, h_B=1/20 and g_B=3/16. With delta=9/10,

$$p_{inspect}=22/27,\qquad p_{inspect}\delta=11/15.$$

Taking c=1/500 satisfies the strict current-participation bound; z_deceive is about 0.0271, below z_0 about 0.0588. The mechanism sometimes discovers and rejects a bad proposal, sometimes accepts an undetected bad proposal, and sometimes completes the honest merger. Original B's expected output remains 4/5 by its indifference; original A's expected output is 1/5 because every branch delivers total main output one. The distinct inspection reservoir pays the verification cost. The probability of actual fusion is 1-z_deceive p_inspect delta; it is not one.

These expectation identities are particular to constant total output, equal preparation costs and the specified fallback. They are not general guarantees that deception leaves founder welfare unchanged.

## 6. No-trade selection and an audit-commitment comparison

The same benchmark also has a no-trade equilibrium: B always chooses the deceptive candidate, F does not inspect and rejects. Given certain deception, inspecting cannot produce an acceptable proposal and wastes c. Given rejection without observation, an honest deviation remains rejected and gives B the same fallback. Beliefs following a pass can be taken as the limits of fully mixed profiles. Hence an accepted-trade equilibrium's existence does not establish unique selection or prevalence. This no-trade construction uses the equal-cost preparation assumption; a strict extra private cost of deception can remove this particular equilibrium and requires a fresh analysis.

If F can instead **credibly commit in advance** to an inspection probability p with p delta>(g_B-h_B)/g_B, B strictly prefers honesty. F then gets honest surplus h-pc, which is positive when h>pc. For the numerical values, p just above 22/27 works and still gives F a positive surplus. Maintaining this audit probability on an all-honest path needs an actual commitment mechanism: once honesty is certain, an uncommitted F prefers to save the inspection expenditure. Announcing an audit probability is not enough.

The comparison separates mechanisms with different implementation technology. It does not give utility modification an automatic audit commitment, and a fixed-utility controller with an equally enforceable audit capability can make the same commitment. Conversely a goal change designed to value auditing would need its own pre-change adoption, execution and later-deviation checks.

The nearest inspected primary comparison is von Stengel's *Recursive Inspection Games*, arXiv v2 (2016), section 5, Proposition 1/proof, PDF pp. 18–19: it treats commitment to the inspection randomization in a two-by-two game. The optional refusal and repair set here change that game. [Primary manuscript](https://arxiv.org/pdf/1412.0129v2); source record L16.

## 7. What remains open in this extension

The key unsolved engineering input is the complete post-detection repair set. If a cheap alternative permits mutually beneficial renegotiation, the rejection payoff used in the inspection game must be replaced by that continuation. False positives, endogenous verification effort, correlated execution failures, private physical strength and repeated encounters also change the belief and payoff equations. None is ruled out by the minimal contract. The present result is a conditional finite-game derivation that preserves deception as a strategic route and records exactly where its deterrence depends on physical and informational assumptions.
