# R0002 working derivation: saturated rewards and observation repairs

**Certificate and ordinary repair registered as R201/R211; contributing-agent self-check.** The efficient-fallback mechanism has a general form: chosen auxiliary goals protect the original criterion when the fallback already attains their maximum. This note derives a process-based implementation that removes the simultaneous-effort coordination selection in the fixed-contract subgame, and an ordinary-contract repair when effort becomes observable to the partner. Note 056 strengthens the reward for post-miss renegotiation. Neither result is a claim about typical preferences.

## 1. A general current-utility certificate

Let w(h) be the original utility on complete physical histories. A current successor uses

\[
U(h)=w(h)+\sum_j\eta_j v_j(h),\qquad \eta_j\ge0.
\]

Suppose a credible rejection continuation Q has E_Q w=w_0 and E_Q v_j=m_j, where every actual continuation mu satisfies E_mu v_j<=m_j. Then every arrangement accepted by that current successor satisfies

\[
E_\mu U\ge E_Q U\quad\Longrightarrow\quad E_\mu w\ge w_0.
\]

If Q falls short of the jth bound by g_j and acceptance has error epsilon, the founder-utility floor is w_0-sum_j eta_j g_j-epsilon. This is an algebraic sufficient condition, not a generic guarantee that a credible joint maximizer exists. It covers the physical-total certificate in 041 and bounded process rewards. Increasing future productive capacity can loosen the physical-total bound; a process indicator already equal to one remains saturated under a larger output frontier.

### Dated information and continuation floors

Apply the inequality at the actual decision history or information set, with its current conditional law and feasible continuation set. After a random outcome is observed, the fallback is the resulting conditional allocation; it is not the original ex-ante mean. In 046, for example, a failure protects the actual failure holdings, not the earlier expected outputs 63/20 and 71/20. Averaging the preserved conditional floors recovers the original ex-ante bound by iterated expectation.

The construction must therefore supply the cap at each renegotiation stage. Under the declared productive continuation and its information, the relevant conditional frontier is maximal; after production its total or welfare cap is pointwise. Correct posteriors cannot be assumed after arbitrary privately selected offers. For the integrated witness, [056 section 6](056-contribution-rewards-through-renegotiation.md#6-private-information-requires-a-truthful-law-check-or-a-stronger-safe-rule) adds a statewise original-floor certificate after private performance or outcome information can arise. That stronger chosen rule protects the actual conditional laws against deceptive offer selection without making effort public. The algebra here remains a conditional-law theorem; richer signaling mechanisms require their own incentive and belief analysis.

## 2. A chosen contribution reward gives a unique effort outcome

Use 041's insurance contract: A receives k=c_A+r in either success state, so actual contribution gives X=q=R_A+r and shirking gives X=q+c_A. Let e_A indicate actual physical calibration supplied to this agreed joint project, not a self-reported bit. Original A values f(X); choose

\[
U=f(X)+\eta(X+Y)+\beta e_A,\qquad\eta\ge0.
\]

Actual calibration must be defined by the physical transition. Merely editing a record or asserting compliance does not set e_A=1. Its private observability to the controller and the verifier's ability to certify the declared utility implementation are distinct assumptions.

When B shirks, A's work-versus-shirk gain is

\[
f(q)-f(q+c_A)+\eta(aY_0-c_A)+\beta.
\]

When B works, replace aY_0 by D=(b-a)Y_0. For b>=2a the first case is the harder one. Thus

\[
\boxed{\beta>f(q+c_A)-f(q)+\eta(c_A-aY_0)}
\]

makes A's contribution strictly dominant in the effort subgame. Since D>c_B, B then strictly contributes. Mutual effort is the unique Nash outcome of that subgame; the mutual-shirk selection from 041 is removed. This does not by itself select the earlier bargaining outcome or rule out hostile future commitments.

The productive fallback simultaneously maximizes expected total output and e_A=1. Section 1 therefore protects original E f(X) against all accepted renegotiations. With eta=0, the saturated contribution term alone protects that utility floor, even when future productive capacity expands, provided the same insured contribution fallback remains credible. Positive eta additionally makes B's output intrinsically valuable to the successor; beta is an explicitly chosen contribution preference, not an original preference secretly inserted into f.

Original A chooses the arrangement because f(R_A+r)>f(R_A) for r>0; B benefits when C-r>0. At matched implementation cost a binding effort delegate can reproduce the insurance and effort behavior. The goal is deliberately designed and requires a trustworthy reference to actual contribution; that is a substantive implementation assumption, not evidence of prevalence.

## 3. Observation can provide an ordinary-contract repair

Now let B privately observe A's actual effort before choosing its own effort and an option in the allocator. Original utilities remain f(X) and Y. The allocator cannot itself verify A's effort, but can enforce B's option choice and the observed success signal. This changes the information structure from the simultaneous hidden-effort class in 042.

Offer B two contractual options after its observation:

- **Buy the insured project:** pay A k=c_A+r in either output state, and receive all reactor output.
- **Decline:** make no transfer and give all reactor output to A.

The options and their allocations are committed before A acts. Under Decline, B optimally exerts no effort and receives net zero. If A contributed, Buy plus B effort gives B C-r>0; buying and shirking gives aY_0-k, which is smaller when D>c_B. Thus B buys and contributes. If A shirked, buying and shirking gives -k<0, and buying plus solitary effort gives aY_0-c_B-k<0. B declines and shirks.

Original A anticipates insured X=R_A+r after contribution and its retained R_A after shirking. It strictly contributes for every strictly increasing f. Hence this ordinary option contract implements the same insured full-effort outcome, without utility modification, through observable sequential action and B's voluntary contingent purchase. The partner's report is incentive compatible through the option payoffs; external verification of A's effort is unnecessary in this construction.

Finite collateral still requires B to finance k after its own effort. The mechanism needs a binding pre-effort assignment of all output to A when B declines; omitting that assignment would create a hold-up opportunity. Charge the costs of that option allocator and the observation. Lower cost can make this repair preferable; equal cost permits a tie with the goal-change implementation. This supplies a concrete condition under which improved observation expands cooperation while changing the relative attraction of preference modification.

## 4. Future commitments remain a separate check

A contribution reward commits effort, but does not automatically protect an insured default from a partner's later threat commitment that destroys it. The guards in 040 are one candidate repair; their verification, physical preservation and voluntary adoption must be checked. A generic binding delegate adds both productive commitments and threat commitments. Replicating an on-path action with a delegate establishes implementation equivalence, not preservation of a full-game equilibrium under every newly available commitment.

An alternative physical repair to investigate is timely exit or delivery before a public threat commitment can take effect. That requires actual launch, certification, observation and exit latencies. It is not assumed here and does not justify removing Attack from the game.
