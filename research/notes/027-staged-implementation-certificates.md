# R0001 working note: certificates for staged implementation

An atomic agreement is a coarse model of a physical process. Expanding it can introduce attacks, revisions, observations and new current preferences. This note states the conditions under which a coarse equilibrium survives that expansion, and derives an exact attack check along a simple continuous physical path. Its backward-induction and optimization machinery is conventional. The results are self-checked, not independently verified.

## 1. Grafting a physical implementation into a finite game

Take a finite public-history current-self game as in note 018. Replace selected transitions by finite public implementation trees. The leaves of each implementation tree either return to a specified later coarse history or terminate. At every new history record actual physical state, active evaluator, observations, and all feasible actions, including Attack for capable controllers. A new preference label receives its own complete-history evaluation; archived founders remain reporting coordinates.

Fix a coarse subgame-perfect profile. A sufficient certificate for extending it to the expanded game consists of:

1. A continuation at **every** internal implementation history, including histories following failure, rejection, revision and deviations.
2. For every entry action profile at every coarse history, the implementation's selected continuation gives every evaluator the same expected continuation utility as the coarse branch. Equality of the entire relevant history law is sufficient, but equality only for the entry actor is not.
3. At every new internal decision, no active evaluator improves by a one-step deviation, evaluated by its own current criterion and the specified later continuations. This includes the possibility of changing goals, with later decisions assigned to the resulting evaluator.
4. The actions available at coarse boundaries correspond to those in the coarse game. A new alternative at a boundary needs its own incentive check; it is not covered by matching the old actions.

Under these conditions the extended profile is a current-self subgame-perfect equilibrium. Work backward from the leaves. The internal one-step inequalities and already valid continuations prevent a profitable last deviation inside each implementation tree. The entry continuation vectors give the coarse stage game exactly its original payoffs, so its selected equilibrium remains valid. Repeat at earlier histories. The same induction rules out deviations at multiple decisions belonging to one evaluator label; it never gives an old evaluator authority over a genuinely different successor.

This is an application of finite-game backward induction, not a new equilibrium existence theorem. It supplies a usable proof obligation: a physical refinement needs continuation values for all criteria and checks for its new deviations. Matching only the final allocation, total cost, or on-path outcome does not establish the certificate. Note 020's late installer revision is a counterexample to dropping item 3, even when the eventual installed objective is publicly observed and executes correctly.

For a terminal-score model, a quantitative variant is immediate. If every expanded strategy and every unilateral deviation has a corresponding coarse strategy/deviation with each evaluator's value error at most e, an exact coarse equilibrium has deviation gain at most 2e in the expansion. The deviation correspondence is essential: an unrepresented intermediate attack cannot be bounded by comparing only the two intended paths. Note 018 provides explicit coupling bounds when the state/action correspondence and kernel errors are supplied.

## 2. An attack envelope before activation

Consider one declared preparation path t in [0,1]. Before the activation at its end, both incumbent criteria remain own-color output minus any stated completion penalty kappa_i. Completion gives fixed final physical allocations x_A,x_B; the binding parameter and completion technology are already specified. Combat is available at every t and gives original i its victory probability q_i(t) times its actual winner output W_i(t). Delivered-output and process effects, if any, must already be in these values.

In the restricted Continue/Attack path, both incumbents strictly prefer completion at every checkpoint exactly when

$$x_i-\kappa_i>M_i,\qquad
M_i:=\sup_{0\leq t\leq1}q_i(t)W_i(t).$$

Any randomized attack time has an expected value no greater than M_i, so the same bounds exclude randomized stopping deviations. If the suprema are attained and the split is nonnegative and otherwise unrestricted, a strict fixed split with total P exists iff

$$P>M_A+M_B+\kappa_A+\kappa_B.$$

This is a pathwise condition with unchanged criteria. Goal activation changes the relevant evaluator and may change the survivor's production policy, so it starts a new phase of the check. Other actions, private observations, revisions, transfers, strategic delays or a nonbinding completion promise require the full implementation certificate in section 1. The envelope alone is not an equilibrium proof for those larger games.

When strengths stay fixed and the physical preparation only reduces work/time/capacity or changes usable material into no-easier-to-recover dispersed stock, the serial frontier in note 024 cannot increase. With a fixed combat transition, the maximum is at the initial checkpoint. This justifies an initial attack check in that restricted case. It does not justify it when relative strength changes.

### A finite exact check for affine paths

Suppose strengths are affine and positive,

$$a_i(t)=a_i^0+v_i t,\qquad
q_i(t)=\frac{a_i^0+v_i t}{A+Bt},\quad A+Bt>0.$$

With fixed serial recovery coefficients and affine remaining resource stocks, the winner frontier is a minimum of finitely many affine bounds W_i(t)=min_j(c_j-d_j t). Partition [0,1] at all crossings where the lower envelope changes. On one piece write a=a_i^0, b=v_i, c=c_j, d=d_j. The derivative of q_i W_i has the sign of

$$N(t)=A(bc-ad)-Bac-2Abdt-Bbdt^2.$$

This follows by differentiating (a+bt)(c-dt)/(A+Bt); its denominator is positive after squaring. Hence the maximum occurs at a piece endpoint or a real root of this at-most-quadratic polynomial lying inside the piece. If N is identically zero, the piece is constant. This gives a finite exact certificate for all continuous attack times, not a favorable sample of dates. Feasibility boundaries, changing capacity coefficients or nonaffine strength laws need their own partition or optimization.

## 3. Physical surplus at every date does not ensure a fixed stable split

Let

$$a_A(t)=1+2t,\quad a_B(t)=3-2t,\quad
W_A(t)=W_B(t)=\frac45-\frac{t}{20},\quad P=1.$$

Both remain capable. The same strength coordinate governs the baseline control mixture and combat. For this calculation the completion allocation is a declared fixed split; its constitutional shares are not automatically recomputed when physical strength changes.

At every date, P>W(t), so a locally acceptable split exists. But

$$q_A(t)W(t)=\frac{16+31t-2t^2}{80},\qquad
q_B(t)W(t)=\frac{48-35t+2t^2}{80}.$$

The first is strictly increasing and the second strictly decreasing on [0,1]. Their maxima are 9/16 and 3/5, whose sum is 93/80>1. No one fixed final split strictly deters both unchanged-utility agents at every date. Different agents have their strongest threats at different dates. Replacing the sum of their maxima by max_t W(t)=4/5 would miss the obstruction.

One physical realization uses O=1, D=0, work B_work(t)=13/5-t/10, and time T(t)=10-t. Production and dispersed-material recovery each use one work and one time unit per output, at unit capacity. Combat spends one work and one time unit and disperses all usable material. Its work-bound winner output is (B_work(t)-1)/2=4/5-t/20; other frontier bounds are slack. Completion can still produce one. Preparation spends 1/10 work and one time unit while transferring two units of effective actuation strength from B to A. Strength is an explicit control-capacity parameter, not a conserved material or utility stock; the physical material boundary covers the production feedstock. Both controllers retain positive combat capability throughout.

This does not prove that every peaceful mechanism fails. Protected intermediate transfers, a binding delegate, a change of completion timing or a voluntary goal change alter the strategic problem. It establishes failure of the fixed-split/no-intermediate-commitment certificate despite positive physical surplus at every date.

## 4. A current-goal change can stabilize this path, conditionally

Here is a local comparison, with implementation capabilities stated. A has already been designated the final production operator; B retains Attack. Before the strength-transfer path, A may install a publicly recognized goal through a declared activation operation costing 1/10 work and one time unit. Before that operation the work/time stocks are 27/10 and 11 and strengths are (1,3). During activation only the old criterion controls A; attacks interrupt at any checkpoint. Work expenditure weakly lowers each old selfish combat value. At the initial checkpoint the winner output is 17/20, giving original reservations (17/80,51/80).

Choose final allocation p=(7/20,13/20). Both original agents strictly prefer it to these initial reservations. Install note 014's output-only quadratic with P=1, W_max=17/20 and

$$\rho=37/40,\quad z_p=761/800,\qquad
U(x)=2x_A+\frac{61717}{32000}x_B
-\frac12(x_A+\rho x_B)^2.$$

It is increasing and concave, uniquely chooses p from the peaceful simplex, and uniquely chooses (Y,0) from every winner simplex Y<=17/20. The inequalities follow from z_p>17/20 and note 014's derivative calculation.

After activation, B's attack value remains q_B(t)W(t)<=3/5<13/20 because an A victory supplies no B output. The installed A criterion strictly prefers p to every combat continuation: every such world has total output below one, while p uniquely maximizes U on the whole unit simplex. Thus its changed strength does not induce the late original-A attack. It also cannot improve by rollback or another goal change if every reachable continuation remains in that same physical simplex and its current criterion has no additional change reward: even a lottery over alternative outcomes cannot exceed U(p).

At each activation checkpoint before the new goal becomes active, the original criteria prefer the completed target to combat. After activation, use the new criterion for A and the unchanged one for B. Consequently this specified continuation has no unilateral attack or rollback gain. Completion is a supported continuation; weak mutual-attack coordination or a different proposal menu can affect equilibrium selection. The initial goal/menu choice, semantic verification, public activation kernel and designated operator are implementation assumptions, not consequences of self-knowledge.

An unchanged-utility controller that can revoke the target and attack late does not meet the same certificate: its late A combat value 9/16 exceeds 7/20. An enforceable fixed-utility delegate or protected allocation with the same execution power can reproduce the successful path. Neither the example nor the envelope theorem establishes that changing utility is uniquely necessary for peace. They isolate where a changed criterion can provide a commitment effect, and where a conventional mechanism would need comparable control over future deviations.

The staged path is compatible with E2's flexible specification but is a separate local control. It must not be silently inserted into the E2-U population payoff table, the private-strength screening game, or the staged fusion example without recomputing those games.
