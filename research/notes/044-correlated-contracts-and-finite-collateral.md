# R0002 working proof: ordinary contracts with correlation and finite collateral

**Exact ordinary-frontier result registered as R209; contributing-agent self-check.** This extends the ordinary-control comparison beyond independent effort mixtures. The constructive counterpart is the productive goal change or a matched effort commitment; increasing collateral and improving observation also supply ordinary repairs. Section 5 establishes the collateral enlargement anticipated in section 3. Full earlier-stage attack implementation remains open as stated in section 6.

## 1. The enlarged ordinary class

Both original utilities are linear in own final output. Use the technology and compact transfer sets in 042. Put L_i=R_i-c_i>=0, so g_i^k>=-L_i, and define

\[
M=Y_0+L_A+L_B,\quad \Delta=b-a,\quad D=\Delta Y_0,
\quad C=bY_0-c_A-c_B.
\]

For each recommended effort profile e, conditional transfer means have differences d_i(e)=g_i^1(e)-g_i^0(e)<=M. This follows from g_i^1<=Y_0+L_j and g_i^0>=-L_i. Allow arbitrary lotteries within these bounds and private correlated effort recommendations, as in 042. All subsequent inequalities use their conditional means, which suffices for the linear original utilities.

Assume

\[
aM\le\min(c_A,c_B),\quad aY_0<\min(c_A,c_B),\quad c_A+c_B>D.
\]

The collateral condition has economic content: even the largest feasible success-minus-failure reward cannot make solitary effort profitable. It is not asserted for unlimited external finance.

## 2. Summed obedience and the exact surplus bound

Let q_e be recommendation probabilities. Summing the two obedience inequalities for recommended effort 1 gives

\[
q_{11}\{\Delta[d_A(11)+d_B(11)]-c_A-c_B\}
+q_{10}[a d_A(10)-c_A]+q_{01}[a d_B(01)-c_B]\ge0.
\]

Write ell_k(e)=kY_0-g_A^k(e)-g_B^k(e)>=0 for actual destroyed or otherwise unavailable output. Then d_A(11)+d_B(11)=Y_0+ell_0(11)-ell_1(11). Put m_i=c_i-aM>=0. The preceding inequality implies

\[
q_{11}\Delta[\ell_0(11)-\ell_1(11)]
\ge q_{11}(c_A+c_B-D)+q_{10}m_A+q_{01}m_B.
\]

Expected waste in the 11 branch is at least q_11(1-b)[ell_0(11)-ell_1(11)]. Other branches have nonnegative waste. Consequently expected total net output N obeys

\[
N\le q_{11}C_{\rm burn}
-q_{10}\left[c_A-aY_0+\frac{1-b}{\Delta}m_A\right]
-q_{01}\left[c_B-aY_0+\frac{1-b}{\Delta}m_B\right],
\]

where

\[
C_{\rm burn}=C-\frac{1-b}{\Delta}(c_A+c_B-D).
\]

Thus

\[
\boxed{N\le\max(0,C_{\rm burn}).}
\]

This upper bound holds for the enlarged mediated class, not only independent effort or a displayed penalty contract. It also bounds public mixtures of such mechanisms. It drops the recommendation-0 constraints, so enforcing them cannot weaken the bound. Actual combat opportunities can further restrict peaceful implementations and remain present in the surrounding physical game.

The bound is tight when a collateral-feasible full-effort failure-penalty contract attains C_burn and that value is nonnegative; otherwise the no-effort stock continuation attains zero. Tightness of the full-effort construction includes its weak effort selection where its incentive constraints bind.

## 3. Exact witness and interpretation

Take a=1/10, b=2/5, Y_0=10, c_A=c_B=8/5 and R_A=R_B=3. Then M=64/5, aM=32/25<8/5, C=4/5 and C_burn=2/5. A tight ordinary contract has

\[
g_A^0=-8/15,\quad g_A^1=24/5,
\qquad g_B^0=-2/15,\quad g_B^1=26/5.
\]

It destroys 2/3 units on failure, none on success, and gives expected net outputs (0,2/5) at full effort. Both work incentives bind. The goal-change contract in 037 instead attains net total 4/5 with strict effort incentives and no waste. B's off-path original-goal gain from its own change is therefore strict even against the mediated ordinary class under these collateral assumptions.

The finite-collateral bound identifies a sufficient condition for the ordinary incentive problem and the exact cost of its failure-penalty repair. More collateral can make the displayed bound inapplicable; it does not automatically prove an improvement. The relevant next mathematical test is the enlarged mediated optimization with those constraints relaxed. Better observation already supplies the explicit option-contract repair in 043.

## 4. Combat comparison requires a physical frontier audit

If an actual disagreement combat lottery gives original agents a summed expected project payoff above R_A+R_B+max(0,C_burn), no ordinary mechanism in this class can satisfy both combat participation constraints. A productive modification can satisfy them when its larger attainable surplus and collateral permit an appropriate split. This is a conditional comparison, not yet a separate physical combat witness.

In particular, raising a postwar recovery frontier above retained stocks requires explaining why agents cannot peacefully use that same recovery machinery, pool resources or delegate control at lower cost. A proposed W>R_A+R_B witness fails if peaceful reuse supplies the omitted ordinary route. The physically audited low-combat instance in 037 avoids that unsupported extension; the transfer-setup attempt in 039 remains unresolved for related reasons. An exact payoff inequality alone cannot establish a broad physical obstruction.

## 5. Larger collateral supplies a constructive correlated repair

The optional computation in `experiments/r0002_mediated_frontier.py` suggested a sharp extension for the symmetric fixture. The following derivation establishes the relevant bound directly. Keep a=1/10, b=2/5, Y_0=10 and c_A=c_B=c=8/5. Let R be each initial stock and require final holdings at least m>=0 in every effort/transfer state. Usable collateral is L=R-c-m; write R_*=R-m. Assume R_*>=3.

Set h=2c-D=1/5, J=c-aY_0=3/5 and G=a(Y_0+2L)-c. For q=q_11 and t=q_10+q_01, summed work obedience implies

\[
q\Delta[\ell_0(11)-\ell_1(11)]\ge qh-tG.
\]

Since waste is nonnegative, expected total net output is bounded by

\[
N\le qC-tJ-\frac{1-b}{\Delta}\max(0,qh-tG),
\quad q,t\ge0,\quad q+t\le1.
\]

If G<=0 the earlier bound applies. If G>0, positive homogeneity reduces a positive maximum to q+t=1. The resulting piecewise-linear expression is maximized at t=0 or at t=h/(G+h), or by choosing no production. These yield C_burn, C-h(C+J)/(G+h), and zero. Substitution gives

\[
\boxed{N_{\rm ordinary}(R_*)=
\begin{cases}
2/5,&3\le R_*\le71/10,\\
4/5-7/(5R_*-18),&R_*>71/10.
\end{cases}}
\]

The second expression is relevant only when G>0 and exceeds 2/5; its denominator is positive on the displayed branch. This is an attained frontier of the mediated output-contract class with weak obedience/acceptance selections; it is not an assertion about arbitrary public renegotiation after every private recommendation.

### Attaining the correlated branch

For R_*>71/10, recommend (0,1) with probability

\[
t=\frac5{5R_*-18},
\]

and (1,1) otherwise. In the solitary-B branch use transfers

\[
(g_A^0,g_A^1,g_B^0,g_B^1)=(L,-L,-L,Y_0+L).
\]

In the full-effort branch set d_A=16/3, d_B=14/3 and

\[
g_B^0=\frac{40R_*+41}{15(5R_*-23)},\qquad
g_B^1=g_B^0+14/3,
\quad g_A^0=-g_B^0,\quad g_A^1=Y_0-g_B^1.
\]

The full-effort B margin is -h and its solitary-effort margin is G, so its work recommendation obeys (1-t)(-h)+tG=0. A's work recommendation occurs only in the full-effort branch and its work margin is zero. When A is told to shirk, its success-minus-failure transfer is -2L, so it strictly shirks. Both agents' ex-ante participation holds: B's net payoff is zero by the chosen constant transfer, and A receives the displayed positive total surplus.

All collateral constraints hold. On this branch L>=11/2 while 0<g_B^0<=26/15; the full-effort success transfers are also within the stated budgets. In the solitary branch B's final failure holding is exactly m and A's smallest holding is c+m. Transfers balance the budget in every outcome. Thus this is a concrete ordinary-contract repair using more collateral and private correlation, rather than merely a statement that the earlier bound stops applying.

For R=10 and m=0 the frontier is 93/160, with solitary probability 5/32. For R=10 and m=3/5 it is 81/145, with solitary probability 5/29. Larger finite collateral raises this frontier toward 4/5; the gap 7/(5R_*-18) stays positive at every finite R_* in this branch.

## 6. Information and combat implementation of the repair

B receives the same work recommendation in both branches and must not learn A's recommendation before choosing effort. The allocator enforces the privately correlated payment rule. A publicly disclosed recommendation or a right to void the contract after learning the branch changes the obedience/participation conditions. The mechanism therefore requires private mediation and binding contingent transfers, which may be stronger than the original public allocator. Its costs and actual availability must be stated when used as an attainable alternative; the bound can still be used as an upper-bound enlargement.

The m=0 construction leaves B with zero after a solitary-branch failure. With a remaining positive combat recovery opportunity, that terminal holding may trigger an attack before delivery. The m=3/5 construction repairs this particular late-attack problem in the low-combat schedule, where the reactor's completed work leaves a much smaller recovery frontier. Earlier private-signal and execution-stage attacks still need the actual state-table check; the ordinary mediated frontier by itself is an effort/transfer result. Choosing a positive protected holding is a physical safeguard with a collateral cost, not the deletion of combat.
