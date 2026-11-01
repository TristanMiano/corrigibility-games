# R0002 execution audit: contribution incentives through later renegotiation

**Correction and conservative repair of the integrated construction.** Notes 043/046/048/052/053 prove work incentives in a fixed-contract effort subgame. That comparison alone leaves a further question: can an agent miss its contribution and then gain through a different continuation, a revised plan or a new controller? This note supplies a uniform bound covering those continuations. The smaller reward witnesses remain valid fixed-contract calculations; the integrated E3 construction uses the strengthened parameters below.

## 1. Preserve the meaning of a completed or missed obligation

For each active evaluator epoch, the contribution predicate refers to the actual history of jointly registered obligations. An obligation has a physical action and a performance deadline. Agents may jointly amend an obligation before that deadline. Once the deadline passes with the obligation unmet, the evaluator's contribution predicate is permanently zero. Neither a later no-work plan, a fresh controller nor a changed private register erases that past miss for the archived evaluator.

Once a valid joint plan exists, if no obligation is missed and the required contributions are supplied, the predicate equals one. With no registered joint plan it is zero; a survivor cannot create a fictitious joint plan with a defeated controller to earn it. A jointly registered no-work amendment can fulfill its empty obligation, but it cannot erase a past miss and must pass the current participation/floor checks. Future obligations can be revised through timely joint registration, with the current evaluator assessing the complete resulting history. This is a history preference for fulfilling agreed obligations, not an eternal preference for one particular reactor or a rule forbidding renegotiation. A fresh evaluator may have its own epoch, but an older evaluator considering that change still scores its own historical predicate. A proposal to forgive a *future* obligation is distinct from changing the truth of a past one.

The finite witness registers the plan before calibration. The declared calibration action ends at its performance boundary; a later contribution cannot retroactively fulfill that obligation. Late production, replacement plans and amendments remain physically possible when affordable and timely. They are included in the continuation bound below. Work and Shirk themselves remain outside the approval penalty.

## 2. A uniform finite reward covers all post-miss continuations

Let the current criterion be

\[
G_i(H)=B_i(H)+\beta_i e_i(H)-K_i I_i(H),
\qquad 0\le B_i(H)\le M_i.
\]

The bound must hold over every complete history reachable after the decision, including changed goals, attacks, lotteries, transfers and renegotiated plans. Let the proposed compliant continuation Q have e_i=1 and I_i=0. Every deviation which misses the current obligation has e_i=0 permanently for this evaluator and hence current value at most M_i. Therefore

\[
\boxed{E_QB_i+\beta_i>M_i}
\]

makes Q strictly preferable to *every* such deviation. The convenient stronger condition beta_i>M_i is sufficient because B_i is nonnegative. This is a finite bounded-utility comparison; it does not assume infinite punishment or physically remove the alternative.

The proof uses the current evaluator on complete histories. It remains valid if a later self has a fresh reward or chooses differently: the current evaluator's e_i remains zero following its missed obligation. Unsafe approval adds a nonpositive term and cannot improve the upper bound. If K_i>M_i+beta_i, safe refusal is also strictly preferable to the first unsafe approval, exactly as in 040.

This argument is intentionally conservative. A sharper bound can replace M_i by the best attainable base value after a miss, or retain the positive E_Q B_i. Computing that value may require posterior and renegotiation analysis. The global finite bound avoids presenting a fixed-contract margin as a solution to that larger game.

The lemma establishes the on-path performance comparison against all continuation strategies. The earlier local dominance statements continue to apply to their fixed-contract effort subgames. It does not supply uniqueness of the entire game, a belief system for every arbitrary off-path controller or a general equilibrium refinement.

## 3. Explicit strengthened implementations

The original founders' payoffs, physical costs and successful output laws are unchanged: the larger coefficients change the successor's preferences, not material production. The finite template implementation must actually support these displayed parameters at the declared implementation cost. It is not a claim that describing or realizing arbitrary large numbers is free.

| Instance | Bound on the unpenalized output base | Strengthened contribution and guard parameters |
| --- | --- | --- |
| Linear 046, both agents | B_i=X_i+lambda_i X_j<=16 for lambda_i<=1 | beta_i=18, K_i=40; the interval beta_i in [17,19] is also valid |
| Insured logarithmic A, 048 | B_A=log(1+X)+(X+Y)/10<3+17/10=47/10 | beta_A=6, K_A=12 |
| Insured linear B, 048 | B_B=Y<=17 | Add beta_B e_B with beta_B=18, K_B=40 |
| Two logarithmic founders at R=10, 052 | B_i<= (13/10)log31<9/2 for lambda_i<=3/10 | beta_i in [5,6], K_i=12 |
| Diversified R=3 logarithmic founders, 053 | B_i< (13/10)log17<4 for lambda_i<=3/10 | beta_i in [4,5], K_i=10 |

All guard constants exceed the largest base plus reward in their row. For the linear witness, choosing beta=18 changes the earlier fixed-contract work margins from 24/25 and 19/20 to 424/25 and 339/20. Those margins are not needed for the new uniform proof, but remain consistent with it. The sound implementation still permits an ordinary private Shirk choice.

Adding a contribution term for insured B closes an otherwise unexamined channel: B could try withholding effort and then seek different insurance terms after the opportunity changed. The original effort margin D-c_B only compares the original contract. The stronger B reward covers all later terms, while the saturated-reward certificate still preserves B's original output floor. A matched binding contribution delegate is an equally legitimate control at the same authority and cost.

For the general increasing concave f in 048, subtract f(0) so its original-output part is nonnegative on the physical interval. This additive normalization alone changes no preferences or coefficient ratios. If M bounds material, use a base bound f(M)-f(0)+eta M and choose beta_A above it; give B a reward above its own material bound. Choose each K above its complete base-plus-reward range. For a further positive affine rescaling, rescale all related coefficients consistently. The conditional theorem needs an actual implementation of this chosen f and the finite constants.

For the normalized power class in 055, f_gamma(0)=0. At a fixed finite stock R, M=2R+10 bounds total material, so B_i<= (1+lambda_i)f_gamma(M) is finite. A reward above that bound supplies the same execution repair. The generalization to every fixed finite gamma and sufficiently large R therefore remains available; a universal stock-independent reward was never required.

## 4. How the repair fits the equilibrium proof

Before an obligation is missed, the efficient default attains the common welfare cap and e_i=1. Current participation therefore preserves the original-welfare floor under timely accepted amendments. An initial compatible deviator still faces its partner's protected floor and the same total cap. It cannot gain by choosing a different certified reward or plan.

At performance time, the uniform reward inequality makes missing the obligation worse even after optimizing every later continuation. After compliant performance, the process reward is earned and cancels from attack comparisons. Actual output, recovery, strength and the installed concern for the other project then determine restraint. Accepted safe renegotiations preserve dated conditional floors. Unsafe physical destruction or an incompatible concession is rejected by the finite approval guard. These are separate parts of the proof; a contribution reward is not used to make every later attack unattractive.

The remaining solution concept is existence of the specified peaceful current-self continuation and an equilibrium of initial implementation choice. Mutual attack or failed initial coordination can remain other equilibria. Verification, reference-history integrity, first-contact timing and the physical bounds remain strong implementation assumptions. The construction supplies agents with a reason to *choose* those commitment preferences; it does not infer their natural prevalence from the convenience of the formula.

## 5. Flexibility and the next extension

Timely plan amendments, parameter changes and matched delegates remain in the agreement space. A missed past obligation has a permanent evaluation consequence within its evaluator's epoch, while future obligations can be different. In a repeated-opportunity model, the live controller can install a new criterion with a new epoch when its current criterion approves; the old criterion evaluates that choice using its own history. Such renewal needs an actual repeated-game analysis, not an instruction to freeze every future task or to forget all past commitments.

The repair strengthens the integrated positive claim and locates its cost: a chosen bounded process preference and reliable historical semantics. The original fixed-contract calculations remain useful lower reward benchmarks. Determining the least sufficient reward under richer information and renegotiation is an open optimization question; it can reduce the commitment burden without changing the original founders' reasons to seek accommodation.

## 6. Private information requires a truthful-law check or a stronger safe rule

The conditional expectation certificate assumes that the law used for acceptance is the actual conditional law. That is not automatic after a privately informed proposer chooses which offer to send. A Bayesian equilibrium can supply the appropriate posterior, but it must be derived. The uniform initial-deviation proof must not silently assign an unchanged prior after every message.

The linear fixture illustrates the issue. Under the original contract, failure gives (1.35,1.35) and success gives (5.85,6.85), with success probability 0.4 before observation. Consider replacing those allocations by (0,2.7) on failure and (7.2,5.5) on success. A receiver incorrectly retaining the old prior would value its own output at 3.82 instead of 3.55. A privately informed A with concern 0.2 would offer this only after success: its current output value then increases by 1.08, whereas after failure it decreases by 1.08. A receiver correctly inferring success rejects because 5.5<6.85. This is a warning about an incomplete deviation argument, not a claimed deceptive sequential equilibrium.

For the integrated finite witness, use the following explicit chosen safeguard after the first private performance or outcome information can exist. A replacement must certify, for each still-possible physical private state omega and each participant i,

\[
E[w_i(H_{replacement})\mid\omega]
\ge E[w_i(H_{default})\mid\omega].
\]

The certificate concerns actual executable allocations and histories. It is checked over all relevant private states, not by trusting a report about which state occurred. The original controller's approval monitor rejects an uncertified replacement under the existing finite penalty. Private effort registers need not be disclosed: a finite template/allocator can be audited against the finite table of effort and output states. The transfer example above fails this test in the success state and is rejected regardless of what posterior its message induces.

**Uniform preservation.** For any actual distribution over private states, including a distribution selected by an adaptive proposer or a deviation, averaging the displayed pointwise inequalities preserves each original welfare floor. No claim of correct off-path receiver beliefs is needed for that bound. Applying it at successive replacement checkpoints preserves the dated floors by iterated expectation. Before private physical information exists, the common-kernel expected certificate remains sufficient. Once both agents publicly know a state, only that state's check is needed.

This is an additional, conservative implementation property. It can exclude insurance trades that rely on revelation and cross-state compensation after information arrives. Such trades remain available before the private-information boundary, and richer incentive-compatible disclosure is a possible later repair. The guarded construction does not claim that this conservative rule optimizes the full information-design problem. It permits future plan changes and new productive agreements that preserve the statewise floors; it does not freeze one code, task or material allocation for all future opportunities.

The matched delegate receives the same rule, authority and verification costs. The ordinary hidden-effort frontier remains a separate enlarged control; certifying a contingent transfer table does not make the physical contribution observable. Where a stronger interface reveals effort, include 043's ordinary observation repair. In the integrated claim, the statewise post-information rule and 057's equilibrium scope replace an unsupported appeal to correct beliefs after every arbitrary deviation.

## 7. Ground the guard in physical records rather than a circular utility label

For a finite implementation witness, first specify raw state/action records and an audited relation of certified instructions. Membership tests use actual controller templates, parameter ranges, outstanding commitments, resource/time bounds, registered deadlines and contingent allocator tables. The post-information table check in section 6 uses the declared original welfare coordinates. It is not a predicate saying that an instruction is safe exactly when the guard itself would approve it.

Define I_i on those raw histories as the first approval of an instruction outside that certified relation after this evaluator's activation. Work, Shirk and Attack are explicitly excluded from that approval relation's penalty; their incentives were proved separately. A public commitment to a lottery with uncertified support is itself an uncertified instruction. Once this history predicate is defined, G_i=B_i+beta_i e_i-K_i I_i is an ordinary real-valued function on complete histories. Its utility ordering and its optimal actions can then be checked without defining genuine preference change by code identity or by the word “safe.”

The relation may admit multiple controllers, parameter values, transfers, lotteries and timely task amendments. A certified replacement still undergoes the incumbent's current-utility comparison; membership is permission, not forced acceptance. New entries require a real audit and their actual verification costs. Arbitrary uncertified programs and physical instructions remain possible, with the finite penalty as a chosen preference consequence. The finite table provides a specification witness, not a verifier for arbitrary future semantics.

A new controller can start its own reference epoch, but cannot change which physical approvals or missed obligations occurred in an older evaluator's history. Erasing a private memory register is distinct from changing that history's utility. The implementation needs sufficient protected memory for the active monitor and truthful access to the declared physical interface. These are substantive endowed capabilities. Their costs and compromise by an adversary are part of the security/error extension, not consequences of an agent merely knowing its own utility.

## 8. Preservation through a finite adaptive sequence of replacements

The dated-floor argument can be stated without assuming one final negotiation. Let h_t be the actual complete physical history at the tth checkpoint of the finite episode, and let q_i(h_t) be the original welfare of the certified continuation from there. At a terminal history set q_i(h_T)=w_i(h_T). Suppose every selected safe transition, including a replacement chosen using private information, obeys

\[
E[q_i(h_{t+1})\mid h_t]\ge q_i(h_t).
\]

The common-information expected certificate can supply this inequality before private information; the statewise check in section 6 supplies it after the private-information boundary. The physically unchanged default supplies equality, with success/failure updating the conditional values instead of preserving an impossible fixed mean in every realization.

Iterating conditional expectation gives

\[
E w_i(h_T)=E q_i(h_T)\ge E q_i(h_{T-1})\ge\cdots\ge q_i(h_0).
\]

The same argument applies when the number of offers or changes is chosen adaptively: pad the finite checkpoint sequence after the last change with the certified execution/terminal continuation. Positive operation durations and the finite horizon bound the number of actual revisions. There is no uncounted infinite negotiation before the deadline.

Thus repeatedly accepting certified replacements preserves original welfare under the actual history law. It permits changed goals and tasks when their registered continuation meets the dated comparison. Current selves choose those replacements using their current criteria; the inequality is a consequence of the chosen certificates and incentives, not an extra founder controlling later decisions.

The proof identifies the failure mode precisely. Replacing the reference value by a lower number after an avoidable destructive action, using an incorrect sender-conditioned law, or silently changing which original welfare coordinate is being protected can break the displayed conditional inequality. Physical preservation, private-state certification and explicit evaluator/reference records are the corresponding repairs. If a future opportunity supplies a better certified continuation, the q_i values can increase; 058 section 3 gives the simple transfer-rich refresh example. The finite argument does not prove preservation through arbitrary unbounded innovations or unverified counterparties.

## 9. Loss of agency and voluntary exit need their own allocation check

The guard's partnership requirements apply while the relevant counterpart retains agency and the protected joint continuation is available. After an actual contest resolves, the certified physical rules permit unilateral recovery and allocation by the survivor. That action does not incur an unsafe-approval penalty merely because combat has destroyed the earlier joint fallback. Past approval and contribution flags retain their actual values. Attack itself was unpenalized and its incentives were checked separately. The preservation argument in section 8 concerns the selected peaceful execution and certified replacements, not a promise to preserve welfare after a hostile attack.

Voluntary deactivation or transfer of authority before entry is a different initial deviation. It cannot be dismissed by assigning zero utility to an inactive founder: the original project may still receive output. Grant, as an upper-bound enlargement, that a departing incompatible agent can leave its remaining stock in its project, give its facilities or inputs to the compatible survivor, and receive whatever the survivor's actual goal subsequently allocates. With no earlier binding compensation promise, the survivor need not produce an extra gift for the departure. Such a new promise made by the guarded partner before incompatible exit is still an outgoing concession; a binding compensated delegation that qualifies for compatibility must receive its actual implementation cost.

For the linear and insured survivor goals, all discretionary output goes to the survivor's own project. The departing agent then gets at most the stock it retained, no larger than its original stock. For a concave survivor, let r<=R be the departing agent's remaining endowment. At a realized total T, its unconstrained desired allocation is ell_(lambda,gamma)(T) from 055; with that endowment floor its final quantity is at most max(r,ell_(lambda,gamma)(T)). Thus

\[
\ell_{\lambda,\gamma}(\overline T)\le R
\]

is a sufficient *statewise* bound on the old founder's output from this exit route. Jensen then bounds its original concave utility by f_gamma(R). It covers receiving a gift after losing agency rather than assuming no such gift occurs.

In the symmetric batch instances, success requires at least one calibration and the surviving guarded controller has paid at least 1/20 installation material. Hence a conservative bound is T<=2R+167/20, including solitary success and full success. For the logarithmic R=3 and R=10 witnesses with lambda<=3/10, direct substitution into ell gives an allocation strictly below R. For the R=3, gamma=1/2 witness, lambda^(1/gamma)<=9/100 makes the bound still stronger. The diversified reactor has the same or a smaller maximum material stock.

For the general power-class construction, choose lambda=1/5 and R>=13max(1,gamma)-1. Put a=5^(-1/gamma). The required bound is

\[
(1-a)R\ge(187/20)a-1.
\]

For gamma<=1, a<=1/5 and R>=12 immediately suffice. For 1<=gamma<=2, a<=1/sqrt5<9/20. Using log5>8/5 and 1-exp(-u)>=u/(1+u), the left side is at least 96/13, exceeding the right side's upper bound. For gamma>=2 the same estimate gives a left side at least 100/9, while the right side is at most 167/20. This proves the bound for every fixed positive gamma in that stated stock region. The general construction chooses this concern coefficient; it does not assert the same outside bound for every coefficient arbitrarily close to one.

There is a consequential limiting case. In a transfer/exit module where the departing agent can supply the physical inputs and transfer control while saving its 1/20 goal-installation cost, a nearly equal-weight logarithmic survivor can allocate the departing project more than the earlier symmetric guarded default. With R=10, no extra material exit cost and lambda>287/288, the survivor's allocation exceeds the default in both success and failure. This follows by writing the total as twice the old equal allocation x plus 1/20: ell_(lambda,1)(2x+1/20)>x exactly when lambda>(1+x)/(1+x+1/20), whose larger threshold is 287/288. Positive exit cost reduces the saved amount; a cost at least the installation saving removes this particular comparison.

That is a scoped peaceful exit/delegation competitor, not a combat result or a completed cheaper-exit implementation in the 32-slot hardware. It explains why the actual successor's allocations, agency transitions and alternative implementation costs belong in the initial audit. The explicit concern families above survive this enlarged uncompensated-exit test. Compensated binding transfers, mergers and delegates retain the compatibility/cost comparison rather than being erased from the menu.
