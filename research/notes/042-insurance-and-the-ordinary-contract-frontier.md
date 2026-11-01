# R0002 working proof: insurance and the ordinary contract frontier

**Ordinary-frontier result registered as R210; contributing-agent self-check.** This note strengthens the control comparison for 041. It gives ordinary fixed-goal agents contingent transfers, waste, finite collateral, transfer lotteries and a mediator recommending effort. The constructive counterpart is insured accommodation or a matched binding effort delegate. The result concerns the same reservation payoff in the actual bargaining game; freezing all future goal changes can change that reservation and defines a different comparison. Notes 043/057 carry the observation and actual-cost controls into the final comparison.

## 1. Physical and informational class

Two agents choose hidden binary efforts e_A,e_B. Success probabilities are p_00=0, p_10=p_01=a and p_11=b, with 0<a<b<1. Success produces Y_0 units of project material. Agent i spends c_i units of its own material on effort. Initial stocks are R_i. Let

\[
V=bY_0,\quad D=(b-a)Y_0,\quad C=V-c_A-c_B>0,
\qquad aY_0<\min(c_A,c_B).
\]

The full-effort profile uniquely maximizes expected total final material: its net surplus is C, while the other three pure profiles have net totals 0, aY_0-c_A and aY_0-c_B. Mixtures attain C only when both agents work almost surely. Contract costs already included in a dated physical frontier must be charged consistently to every mechanism; this note uses the common net frontier conditional on reaching the effort stage.

Original A evaluates f(X), where f is continuous, strictly increasing and strictly concave on the bounded range of possible outputs. Original B evaluates Y linearly. A contract can redistribute stocks and success output, destroy material, and use lotteries, but observes only the success signal and its own prior messages, not actual effort.

Require transfer vectors g=(g_A,g_B) in compact sets K_k for k=0,1, with g_A+g_B<=kY_0 and R_i-c_i+g_i>=0. These bounds enforce nonnegative final holdings even after an unobserved effort deviation. The sets allow all allocations consistent with the declared finite collateral; no external subsidy is available.

## 2. A compact enlarged mechanism class

Allow a mediator to privately recommend a joint effort vector e in {0,1}^2 with probability q_e. Conditional on that recommendation and on output k, it draws a transfer vector from a law mu_{e,k} on K_k. Recommendations do not make effort observable or enforceable. The agent can deviate while the transfer law remains tied to the recommendation and the observed output.

For compactness use subprobability measures nu_{e,k}=q_e mu_{e,k}. Require both nu_{e,0} and nu_{e,1} to have mass q_e, q_e>=0 and sum_e q_e=1. The space of these finitely many bounded measures on compact sets is compact in the weak topology. For every agent and every recommended action, impose the obedience inequality obtained by summing over the other recommendation: expected current utility from the recommended effort is at least that from switching effort. Each inequality is a continuous linear functional of these measures. The feasible mechanism set is therefore compact and convex.

This is an enlargement of ordinary public contingent contracts and their public randomizations. Extra disclosed information can impose additional conditional obedience inequalities; averaging those inequalities gives the ones used here. Consequently this relaxation also bounds such more informative implementations. The claim is about this explicit hidden-effort/output-transfer class, not every possible future monitoring or commitment technology.

Attacks are omitted only from this *upper-bound relaxation of ordinary peaceful mechanisms*: dropping a deviation can enlarge their attainable payoffs. The physical game retains attacks and checks their values separately. This argument does not establish peace by removing combat.

## 3. Strict ordinary-contract gap at an insured frontier

Fix B's actual reservation payoff R_B+C', with 0<C'<C, and set

\[
q=R_A+C-C'.
\]

For every feasible ordinary mechanism satisfying B's participation,

\[
E X+E Y\le R_A+R_B+C,\quad E Y\ge R_B+C'
\quad\Longrightarrow\quad E f(X)\le f(E X)\le f(q).
\]

**Claim.** If the feasible ordinary set is nonempty, its maximum original-A utility is strictly below f(q).

**Proof.** Compactness and continuity give a maximizer. Suppose it attained f(q). Strict concavity and monotonicity force X=q almost surely, E X=q, E Y=R_B+C', and maximum total surplus C. The unique physical surplus maximizer then forces e_A=e_B=1 almost surely and no waste on positive-probability outcomes. Since 0<b<1, both success and failure occur with positive probability. In each outcome the realized transfer to A must therefore equal c_A+q-R_A almost surely. If A secretly shirks, the success probability changes but its transfer remains that same constant in both outcomes. A saves c_A and receives X=q+c_A surely. Strictly increasing f makes this a profitable deviation, contradicting obedience. Thus the attained maximum is below f(q). QED.

The proof includes private effort recommendations and arbitrary bounded transfer lotteries. It does not need a numerical lower bound on the gap. It relies on strict concavity, compact finite collateral and hidden effort; changing these assumptions changes the control frontier. The insured preference change in 041 attains f(q) under its own implementation and selection assumptions. A binding effort delegate can attain the same insured frontier; if available at matched cost it ties the goal-change mechanism.

For affine f, equality in Jensen does not force insurance. Use the separate summed incentive condition for ordinary deterministic budget-balanced contracts, or a full ordinary mechanism optimization. Do not extend this strict-concavity proof to affine preferences by continuity alone.

## 4. A useful deterministic control bound for every concave f

For a deterministic binary transfer to A, write d=g_A1-g_A0. When B works, A's work and shirk output laws are, after translating by z=R_A+g_A0,

\[
W=z-c_A+d\,\mathrm{Bernoulli}(b),\qquad
S=z+d\,\mathrm{Bernoulli}(a).
\]

For d<=0, shirking first-order dominates working. For 0<d<=c_A, the largest work output is at most the smallest shirk output, so the same conclusion holds. For d>c_A, order the four translated support points as -c_A<0<d-c_A<d. The difference of integrated distribution functions, equivalently E[(t-W)_+]-E[(t-S)_+], is nonnegative everywhere exactly when

\[
(b-a)d\le (1-a)c_A.
\]

To check this directly, the difference increases from zero on [-c_A,0], decreases with slope -(b-a) on [0,d-c_A], reaches c_A(1-a)-(b-a)d at d-c_A, and then increases with slope a until d. Its final value is c_A-(b-a)d. This proves second-order dominance by S under the displayed inequality. Evaluating piecewise-linear concave interpolants at the four support points then gives the expected-utility ordering for every increasing concave f. It is strict for strictly increasing f: the final mean gap is at least a c_A>0, and the interpolant has a strictly positive final slope.

If B is linear and the deterministic contract balances its budget in each output state, B's effort requires (b-a)d_B>=c_B, while d+d_B=Y_0. Consequently

\[
D-c_B\le (1-a)c_A
\]

is sufficient to rule out both agents working under any such contract, for every strictly increasing concave original f. The fixture a=.1, b=.4, Y_0=10, c_A=c_B=1.6 satisfies 1.4<=1.44. This deterministic dominance bound is not asserted for arbitrary state-dependent transfer lotteries; the compact frontier proof above supplies the broader strict-gap result when f is strictly concave.

## 5. Scope still to integrate

The ordinary bound and the insured mechanism must use the same dated output frontier, collateral, information and actual B reservation. Costly verification and goal installation can lower the insured frontier; an ordinary mechanism with genuinely lower costs must receive that advantage. The sufficient adoption comparison is the resulting original-utility payoff after those costs. Observable effort, enforceable effort policies, richer success signals and different proposer rights are constructive repairs to test, not silently excluded universal impossibilities.
