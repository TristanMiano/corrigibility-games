# R0002 working derivation: strength, negotiated shares and combat reserves

**Conditional parameter analysis.** This connects the guarded partnership to the project's combat-versus-compromise question. It distinguishes a sufficient adoption region, actual attack incentives at a given history, and the stronger task of solving an enlarged bargaining game outside that region.

## 1. Negotiating shares expands the guarded adoption region

Let original agents value their own project quantities, initial stocks be R_A,R_B, contribution costs c_A,c_B, installation losses k_A,k_B, and expected joint output V=bY_0. A's strength gives contest probability s and B's 1-s. Suppose the physical unilateral-deviation audit gives an upper bound max(R_i,s_i W_0) on each incompatible controller's original payoff. This bound includes retention, direct combat and the permitted solitary-production/stopping routes; it is an assumption to prove from the physical instance, not a replacement for that audit.

With negotiated default shares t and 1-t, compatible productive outputs are

\[
\bar X=R_A-k_A-c_A+tV,\qquad
\bar Y=R_B-k_B-c_B+(1-t)V.
\]

Contribution rewards beta_i>c_i make contribution strictly dominant in the fixed-contract effort subgame for every share in [0,1] when 0<=lambda_i<1, a>0 and b>=2a. The integrated continuation uses 056's stronger uniform reward to cover subsequent renegotiation. The guard makes participation with an incompatible counterparty unattractive. Hence shares can be negotiated over the full interval rather than being confined by the original private-effort incentives.

Strict gains over both the stock and combat upper bounds are possible exactly when the share interval

\[
\frac{k_A+c_A+\max(0,sW_0-R_A)}V
<t<
1-\frac{k_B+c_B+\max(0,(1-s)W_0-R_B)}V
\]

is nonempty. Equivalently, writing C=V-c_A-c_B,

\[
\boxed{C-k_A-k_B>
\max(0,sW_0-R_A)+\max(0,(1-s)W_0-R_B).}
\]

Under the verified guards, timing and implementation conditions of 046, every share in this interval supports strict original-goal improvement over remaining incompatible. This is a sufficient equilibrium-existence region for that class. Failure of this stronger stock-and-combat comparison is not a theorem that combat occurs: actual stock retention may itself be threatened, unilateral gifts may change threats, and other safeguards or counterparties may be available.

For the witness R_i=3, c_i=8/5, V=4, k_i=1/20, W_0=4, the fixed share t=9/20 gives a sufficient strength interval

\[
9/80<s<63/80.
\]

Allowing the agents to negotiate t expands it to

\[
3/40<s<37/40.
\]

For example, s=9/10 is outside the fixed-share region but t=23/40 gives expected outputs (73/20,61/20)=(3.65,3.05), exceeding both retained stocks and the combat upper payoffs (3.6,.4). Changing the agreement repairs the fixed-share limitation. The guarded contribution rewards keep both effort incentives strict at that revised split.

These are strict sufficient regions based on W_0's upper bound; equality requires the actual recovery frontier and tie behavior. A claim that raising s causes actual combat requires an attainable contest payoff and the full alternative agreement space, not merely crossing the boundary of one selected split.

## 2. Exact attack threshold at a resolved allocation

At a history with final project holdings x and y and no additional productive opportunity, put T=x+y. Suppose the available contest yields W<=T, A wins with probability s, and each survivor values its own project most at a fixed total. For current A utility x+lambda y, 0<=lambda<1, the attack value is [s+lambda(1-s)]W. Keeping the allocation is preferred exactly when

\[
x\ge sW-\frac{\lambda}{1-\lambda}(T-W).
\]

Thus greater concern for the other project lowers A's required own holding when combat loses total output. Increasing the destruction/recovery loss T-W has the same effect. Greater own victory probability raises the required holding, and a larger attainable recovery frontier raises the appeal of combat. These are current-utility attack comparisons at the stated history, with physical access retained; they are not initial adoption claims.

For original increasing concave f(x), an independently sufficient holding condition is x>=sW, since E f(combat output)<=f(sW). A chosen goal f(x)+eta T additionally favors retention by eta(T-W). A contribution reward already earned at this history cancels from the comparison. If contribution is still future, its lost reward must be included instead of silently canceling it.

## 3. Chosen minimum holdings and their collateral cost

Suppose the post-observation recovery frontier is bounded by W_late. Requiring each final holding to satisfy m_i>=s_i W_late deters late attacks for linear original utilities and, by Jensen, for increasing concave own-output utilities. For positive linear concern for both projects, imposing both component holding bounds also suffices. The inequalities are strict when the bounds have a strict margin or the actual recovery frontier is smaller.

Such a reserve is a chosen contractual safeguard. It consumes usable collateral: in 044's symmetric mediated-contract class, collateral becomes L=R-c-m. The exact ordinary frontier then depends on R_*=R-m. At R=10, raising the protected holding from 0 to 3/5 changes that frontier from 93/160 to 81/145. The zero-holding mechanism needs a late-attack repair; the positive reserve supplies one under the audited low-recovery schedule. This connects physical security to the cost of an ordinary incentive mechanism rather than declaring either mechanism automatically stable.

More available recovery work can increase W_late and hence the reserve needed for peace, even if the productive reactor's output is already saturated. Better verification can enlarge the feasible agreement set, but any saved work that also raises combat recovery must be included in the joint comparison. Deliberately dissipating otherwise unusable residual work is a candidate physical safeguard: it can reduce recovery without deleting the military attack action. Its voluntary adoption, opportunity cost and timing remain to be solved before treating it as an available repair.

## 4. A positive no-effort success probability preserves an open region

The zero success probability under mutual shirking is not essential to the guarded adoption comparison. Replace it by p_0 in (0,a), keeping the other probabilities a,a,b. If (a-p_0)Y_0<c_i, an incompatible agent's best solitary material opportunity is bounded by R_i+p_0Y_0, even granting it all of the no-effort reactor output. The final-signal timing still prevents an early informative gamble followed by a better recovery option. Thus a sufficient original-payoff bound is max(R_i+p_0Y_0,s_i W_0).

The negotiated-share condition becomes

\[
C-k_A-k_B>
\max(p_0Y_0,sW_0-R_A)+
\max(p_0Y_0,(1-s)W_0-R_B).
\]

For the equal-strength linear fixture, its fixed t=9/20 allocation retains strict gains when 0<p_0<3/200. Allowing shares to adjust gives the larger sufficient interval 0<p_0<7/200. Contribution rewards of 2 still make effort strict; the smaller marginal probability a-p_0 is charged in that comparison. The productive total remains the maximal expected output throughout these intervals.

In the insured fixture, any p_0Y_0<r<C_n-p_0Y_0 preserves strict gains over the same upper bounds, subject to collateral and the adjusted contribution-reward inequality. The displayed r=3/10 therefore survives 0<p_0<3/100. This supplies a nonzero-probability perturbation of the physical kernel, not only small changes in utility coefficients.

The ordinary mediated bound can be enlarged consistently: the no-effort alternative contributes p_0Y_0, while the solitary incentive term becomes G=(a-p_0)M-c in the symmetric calculation. The bound is the maximum of that no-effort value, the failure-penalty frontier, and the feasible correlated branch. For the small-probability, R=3 region above, the ordinary maximum remains 2/5. Do not reuse the larger-collateral closed form from 044 without making this change to G.
