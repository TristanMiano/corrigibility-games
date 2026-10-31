# R0001 working note — sequential fusion and the founder's participation problem

This note continues the first recurrence with an explicitly staged fusion mechanism. It separates the old founder, its currently acting successor, and the remaining original agent. Provisional derivations are self-checked only; implementation assumptions and equilibrium selections are part of each statement. The eventual single controller's lack of internal war is loss of separate agency, not a proof about two actors who remain capable.

## 1. A staged protocol with attacks and a rollback menu

Initially A and B have strengths a,b>0 and original color utilities x_A,x_B. Write s=a/(a+b). A can first prepare a common controller F with goal

$$G_\alpha(x)=\sqrt{\alpha x_A}+\sqrt{(1-\alpha)x_B},\quad 0<\alpha<1.$$

This first transfer ends A's independent decision authority and gives F strength a; original A's welfare remains reportable. B still has strength b and its original goal. This is an agency transition, not an assumption that an inactive copy of A controls future decisions. It can be modeled either as replacement or as goal modification with a specified lineage; any identity/freezing preference must say which physical/history events it counts.

At the next checkpoint F can Continue, Rollback, or Attack. B can Join, Stay, or Attack. Attack has priority and prevents pending transfers. Rollback has priority over pending Join and restores the specified separate-controller state, consuming a declared work/time cost; it does not make B involuntarily join. With F continuing, Join transfers B's control to F, combines effective strength a+b, installs the agreed final goal, and leaves one agent. Stay ends the integration attempt and proceeds to ordinary two-controller production. In each two-controller production state a strength-weighted public draw selects the equipment operator, while both retain Attack at the last production choice, as in E2-U. Operators may choose any feasible allocation.

Communication, verification, transfer and reassembly costs are physical route transitions before the corresponding recovery frontier is evaluated. Let P be the total achievable output on the unmerged Stay route, M on successful integration, and W on the relevant post-preparation combat route. These are not interchangeable utility penalties. The following local calculations assume a common W for both winners and P>W>0; asymmetric winners can be supplied without changing the need to evaluate their actual current goals. No production or transfer is assumed to be safely atomic across checkpoints: attacks can interrupt before either transfer. The final finite control-transfer operation has its declared time resolution; a more detailed implementation may insert additional vulnerable checkpoints.

If F wins a conflict, its current goal produces (alpha W,(1-alpha)W). If B wins, it produces only B's color. A lost founder does not automatically assign zero value to these outcomes. After successful fusion, F can produce, or choose a costly Split operation restoring explicitly specified separate controllers. There are no longer two independent internal attackers in the fused state. The local task ends after production; external encounters and later power investment are not claimed solved.

## 2. The remaining original agent can prefer staying separate

First suppose the Stay continuation selects peaceful production for both possible operators. When F operates it produces the alpha split; when B operates it produces all B. Old-founder continuation values are

$$d_A=s\alpha P,\qquad d_B=(1-s\alpha)P.$$

F's actual current value is

$$L_F=\sqrt P\,[s+(1-s)\sqrt{1-\alpha}].$$

This continuation is incentive-compatible only if both relevant nonoperators decline attack:

$$ (1-\alpha)P\ge W(1-s\alpha),$$
$$ \sqrt{(1-\alpha)P}\ge\sqrt W\,[s+(1-s)\sqrt{1-\alpha}].$$

The operators themselves prefer their chosen maximal production to combat when P>W. Weak mutual-attack equilibria remain; the peaceful continuations are specified selections, not unique outcomes.

If the final fused goal must remain G_alpha, B's Join value is (1-alpha)M-k_B, where k_B>=0 is B's **current** output-unit disutility for the particular goal/agency transition. The definition must distinguish a literal utility change, replacement by a different controller, and loss of independent agency; k_B is not inferred from code replacement alone. B joins iff

$$ (1-\alpha)M-k_B\ge(1-s\alpha)P.$$

With alpha=s=1/2 and k_B=0, this requires M>=3P/2. The original founders can both prefer a hypothetical half-and-half merger to their original war threat while B, after A has already compromised, prefers the separate continuation paying 3P/4. Thus a jointly attractive endpoint is not sufficient for sequential fusion.

If B's condition holds, M>P for interior s,alpha when k_B>=0. Then F also prefers fusion: sqrt(M)>L_F. A costly rollback to original goals instead produces the specified uncommitted conflict continuation; if its output is at most P, F's value is bounded by sqrt(P)[s sqrt(alpha)+(1-s)sqrt(1-alpha)], below L_F. In this local menu F has no profitable rollback. Broader renegotiation options require a new check rather than being silently removed.

The M/P gain, when present, must be physical. For example, an integration operation may change a throughput bottleneck or communication delay. The same hardware integration should be available to a fixed-utility joint controller when the technology allows it. Assigning M>P only to goal change without such a mechanism would merely assume the desired advantage.

## 3. Renegotiating the final goal can repair the last-mover objection

Allow F and B to agree on a final G_beta, rather than freezing alpha before bargaining. F evaluates this proposal using its current G_alpha. B evaluates it by its still-original utility, including any k_B. The final controller subsequently uses G_beta. Let

$$q_B=d_B+k_B,\qquad \beta_{max}=1-q_B/M,$$

and assume 0<q_B<M. B accepts beta<=beta_max. F's value of a fused beta allocation is

$$G_\alpha(\beta M,(1-\beta)M)
=\sqrt M\,[\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}].$$

This is strictly increasing in beta up to alpha and strictly decreasing after alpha. F's best B-acceptable final objective therefore has beta*=min(alpha,beta_max), if the endpoint acceptance is selected. F accepts renegotiation iff its displayed value at beta* is at least L_F. Any intrinsic penalty in F's current criterion for changing again must be subtracted in F's own utility units; it cannot be added to k_B as if both criteria shared a cardinal scale. Physical renegotiation costs are already in M.

At M=P, k_B=0 and peaceful Stay, beta_max=s alpha<alpha. The fused output (s alpha P,(1-s alpha)P) is exactly the mean of the separate continuation. Strict concavity of G_alpha makes F strictly prefer that deterministic mean to the nondegenerate Stay lottery. B is indifferent in its linear utility. Original A is also indifferent between these two outputs in expectation, although it still must compare its initial transfer with its own earlier alternatives. Thus no integration-output gain is needed to make this **reweighted** merger weakly acceptable to both current decision makers. The fixed-alpha 3P/2 threshold was a menu restriction, not a general impossibility of fusion.

## 4. A general mean-allocation sufficient condition

Let Q be any specified fallback lottery over nonnegative color outputs with finite expectation. F's current output utility g is continuous, increasing in each coordinate and concave; B has linear x_B minus a Join penalty k_B>=0. Suppose integration can produce every deterministic allocation with total at most M, and

$$M\ge \mathbb E_Q[x_A+x_B]+k_B.$$

Give B its reservation output E_Q[x_B]+k_B and give A the remainder. This gives A at least E_Q[x_A]. By monotonicity and Jensen,

$$g\big(M-E_Q[x_B]-k_B,E_Q[x_B]+k_B\big)
\ge g(E_Q[x_A],E_Q[x_B])\ge E_Q[g(x)].$$

B's current utility is at least its fallback value, and F also weakly gains. A sufficiently expressive final-goal menu implements that deterministic allocation; G_beta does so for interior allocations. The proposed fusion must still be physically achievable, correctly observed, consensual, and reachable without a profitable early attack. This is a local consent result at the current checkpoint, not an equilibrium of the entire installation path.

If the inequality has positive slack, a small additional B allocation can make B strictly better while keeping A at least at its fallback mean; strict monotonicity then also improves F. With zero slack, a strict Jensen gain can still pay for a small transfer to B by continuity, provided A's mean output is positive. In that case the **old A founder** may lose expected color output relative to the fallback even while its current successor strictly prefers fusion. That distinction is the next participation problem.

## 5. Renegotiation can benefit both current actors while harming the first founder

Take s=alpha=1/2, P=M=1 and k_B=0. The peaceful separate continuation has old-founder values (1/4,3/4) and F's current value

$$L=(1+1/\sqrt2)/2.$$

Suppose B proposes the final beta and F accepts or rejects. B's best accepted proposal gives F as little A-color as its current utility will tolerate, while leaving B at least 3/4. On beta in [0,1/4], F's value

$$g(\beta)=\frac{\sqrt\beta+\sqrt{1-\beta}}{\sqrt2}$$

is strictly increasing. Its smallest weakly acceptable beta solves g(beta)=L:

$$\beta_{min}=\frac{4-\sqrt{7+4\sqrt2}}8\approx0.0553.$$

Derivation: g(beta)^2=1/2+sqrt(beta(1-beta)); L^2-1/2=(2sqrt(2)-1)/8; solve the resulting quadratic and select the root below 1/2. With acceptance at indifference, B proposes beta_min and gets about 0.945. F is indifferent to its own fallback, and B strictly improves. Original A gets only beta_min, well below its separate-continuation expectation 1/4.

For a finite strict witness, allow final shares {1/16,1/4,1/2}. F strictly accepts beta=1/16 because (1+sqrt(15))/(4sqrt(2))>L, and B chooses it over the other accepted offers. Original A then gets 1/16. If its initial original-goal combat value was 27/200, it refuses the first transfer despite both current actors later accepting the proposed merger. This avoids reliance on a continuum's indifference endpoint. The successful local renegotiation cannot be promoted to an initial adoption theorem.

## 6. A finite successor freeze can protect the founder's initial decision

An original A that can choose its successor objective can instead install a criterion that evaluates final color output by g but charges a finite lambda>=0 if F later installs a different preference class. Call this criterion g_lambda. The event is a genuine subsequent preference change on the declared outcome/history domain; an affine recoding alone is not a change. A failed attempt that leaves the criterion unchanged need not count unless explicitly specified. This is a new initial-goal design, not an assertion that the old A already values freezing.

Against the same B proposal protocol, a changed final goal beta is accepted only if

$$g(\beta)-\lambda\ge L.$$

For beta in [0,1/4], a larger lambda raises the minimum accepted A-share. For example choose a target q=1/5 and lambda=g(q)-L=3/sqrt(10)-L>0. Under the stated acceptance selection, B's smallest accepted changed goal gives original A q, and B 1-q. A now prefers the initial transfer to its 27/200 combat alternative, because 1/5>27/200. A small finite offer grid and a lambda strictly between adjacent acceptance thresholds can make both proposal and acceptance choices strict.

The new F's decision is still evaluated by its **current g_lambda**, including the impending change penalty; the final successor uses its installed G_beta afterwards. Original A's initial decision is evaluated by its own color objective and any actual initial-change penalty. Nobody scores the initial decision solely by the newly installed criterion.

Thus voluntarily installing a finite preference for future goal preservation can enable an initially acceptable compromise by protecting against later exploitation. At larger lambda, renegotiation may fail and the agents stay separate; this is not a universal monotone benefit of freezing. A binding contingent delegate can supply analogous commitment if its execution technology is available. No population fitness, hard-freezing theorem, or long-run convergence claim follows from this finite construction.

## 7. A physical finite-protocol witness with strict finite offers

The numerical participation example can be supported by explicit resource transitions rather than a free integration operation. Start with O=1,D=0, work B=11/10, time T=8 and capacity k=1. Production and dispersed-stock recovery each consume one work unit and one processing-time unit per material unit. No imports or new work are available. A preparation, proposal/verification, acceptance/transfer or rollback operation costs 1/100 work and one time unit. Use at most four such operations before a production decision on the successful path. Material therefore binds peaceful production at P=M=1 despite these positive costs: at least 106/100 work and four time units remain. Spending work from slack is not the same as assuming that the operation is costless.

Combat consumes 14/25 work and one time unit and disperses all currently usable stock. At a checkpoint after j administrative operations, its remaining work is 54/100-j/100; recovery plus production cost two work units per delivered unit. Thus

$$W_j=\frac{27}{100}-\frac{j}{200},$$

for j<=6, with work binding and enough time/capacity; the intended pre-fusion path uses at most four operations. At later off-path states use the full work/time frontier: if j=7, combat exhausts the remaining time and delivers zero. At T=0 the finite task has ended. Equal strengths give initial original-agent war value 27/200. Material not recovered remains dispersed; no material or energy is claimed destroyed. Combat remains affordable at every nonterminal two-agent checkpoint. Winners have their actual current criteria and retain the production capacity; losers lose agency while original welfare remains defined.

A concrete timing is: A's first transfer; B's public proposal; a verification checkpoint; F's acceptance and B's voluntary handover; then production. At every pre-fusion checkpoint both capable actors have Attack, with attack priority over pending transfers. B can Stay instead of proposing and Withdraw before handover. F can Reject or perform the declared Rollback. Verified goal templates are the finite menu with final A-shares {1/16,1/5,1/4,1/2}. The verification technology checks the actual restricted goal template and its installation; that is a stated strong capability, not inferred from utility self-knowledge. There is no hidden execution failure in this witness. Imperfect verification requires new beliefs/continuations.

Rejection/withdrawal gives the partial F/B production game. Rollback restores original A/B controllers and proceeds to the uncommitted production game, with the relevant recovery frontier. Rejected transfers do not force combat: all ordinary production allocations remain available, and original-controller conflict follows from deviations in that final game. After actual fusion there is a single F; a costly Split can restore separate controllers, and later objective changes can be offered from the declared menu. Producing the current goal's maximum at total one already weakly dominates every such further change because no route can deliver more than one unit. A finite time budget prevents endless zero-time update loops. At the task boundary delivered output is protected; no claim is made about later external encounters.

Select the peaceful partial-production continuations after F exists. They are strictly supported against unilateral attack for every W_j<=27/100: original B's half-share beats 3W_j/4, and a nonoperating F's g-value 1/sqrt(2) exceeds sqrt(W_j)L. F also rejects rollback: it would incur the subsequent-change penalty, if present, and replace its partial value L with a strictly smaller war value. Initial original controllers' final uncommitted game instead has only war outcomes, as proved in note 010; no last-resort rule is imposed.

At lambda=0, B's smallest offered share 1/16 is strictly accepted by F. The exact inequality

$$\frac{1+\sqrt{15}}{4\sqrt2}>\frac{1+1/\sqrt2}{2}$$

reduces, by positive squaring, to 9>8. B obtains 15/16, so it prefers this offer to Stay and to every larger A-share. Original A anticipates 1/16<27/200 and refuses the first transfer. A locally consensual merger fails initial adoption.

At lambda=9/100, F strictly rejects 1/16 and strictly accepts 1/5; it also accepts 1/4. On [0,1/2], g increases, so 1/5 is B's best accepted offer. To certify the nontrivial strict acceptance without relying on rounded decimals, use
\(1414/1000<\sqrt2<1415/1000\) and
\(3162/1000<\sqrt{10}<3163/1000\):
\(3/\sqrt{10}>3000/3163>L+9/100\).
For rejection, \(g(1/16)<25/28\) and \(L>85/100\) give
\(g(1/16)-9/100<L\).

The resulting old-founder welfare is (1/5,4/5), both above their initial attack values. After A's transfer, F's current value g(1/5)-9/100 exceeds L, so neither rollback nor an intermediate attack helps it. B's 4/5 also exceeds its partial 3/4 and every available immediate-war value. The final G_(1/5) controller actually produces the proposed split. Consequently a selected decision-self equilibrium completes the staged merger with the finite successor-freezing preference, while the corresponding lambda=0 candidate is not initially adopted. Weak simultaneous-attack equilibria still exist.

The initial menu and proposal rule are part of this witness. If an ordinary binding split/delegate or a suitable late history-contingent objective from note 011 is added at comparable cost, original agents may obtain an alternative peace and decline this fusion. The result establishes a strategic role for finite successor freezing within the declared menu, not necessity for peace, an optimum over all utility functions, or a reason to permanently restrict later recurrence models.

In the finite witness A's initial Start menu can contain the two specified objectives g_0 and g_(9/100). Given the stated continuation selections, Start with g_(9/100) yields A 1/5; Start with g_0 yields 1/16; ordinary uncommitted production or immediate attack yields at most 27/200. Thus the finite freeze is voluntarily **chosen** under the original color utility, rather than being attributed to an agent that merely inherits it. The active-continuation lineage identifies F as A's successor; inactive stored copies confer no decision authority. Other identity conventions matter only after the relevant intrinsic preferences are explicitly added.

## 8. Removal tests: implementation can preserve a goal while changing the bargain

The finite-offer protection does **not** cover a feasible, enforceable production route that gives B 15/16 units first, transfers B's remaining authority as agreed, and leaves 1/16 units of material for F. F can retain g_lambda unchanged. Once B's delivery and the control transfer are actually secured, F's best remaining production is all A: B already has much more than A. The final output is (1/16,15/16), with no further preference-class change and therefore no lambda penalty. F's value exceeds L by the exact inequality in section 7, and B's output exceeds 3/4. Such an enforceable route can bypass the goal-only freeze; an initial founder anticipating that selected route would reject the first transfer.

**The unsecured prepayment attempt fails.** Merely adding protected early deliveries does not establish that route as an equilibrium. If B receives 15/16 and then keeps its independent authority, the remaining operator draw gives F the last 1/16 with probability 1/2 and B that quantity with probability 1/2. B's fallback is therefore 31/32, greater than the promised 15/16, so it refuses the handover. F's resulting current value is [g(1/16)+1/sqrt(2)]/2<L, and it would not willingly make that unsecured bulk payment in anticipation of refusal. A partial delivery can improve B's outside option rather than induce surrender.

In the concrete finite-work example, producing 15/16 has already left less than 14/25 work, so the residual combat operation is unaffordable; this is physical incapacity, not deletion of an available attack. The remaining control draw still makes handover unattractive to B. Adding more interruption checkpoints before that fuel depletion requires checking them too. These observations refute the attempted inference from a mutually preferred final allocation to a self-enforcing prepayment path.

The successful bypass thus requires an actual conditional handover, escrow, binding production program or another mechanism that resolves this problem. It need not require new hardware if existing machinery already supports those operations, but it is **stronger execution capability than an unsecured promise**, and its physical costs and attack exposure must be stated. A matched fixed-utility controller should receive it too. If available within the budget, the route belongs in the comparison; it cannot be assumed from ordinary communication alone. The restricted finite-offer protection is a local-game result, and a goal-preservation preference is not automatically an allocation commitment.

An analogous caution applies to an outcome threshold. A criterion g(x)-K 1{x_A<q} can deter deterministic offers below q but need not protect the original founder's expected allocation when randomized goal installation is feasible. At q=1/5,K=3/10, the partial value is L-K/2. A half-and-half lottery installing goals for shares 1/16 and 1/5 gives current expected value

$$\tfrac12[g(1/16)-3/10]+\tfrac12 g(1/5)>L-3/20,$$

yet original A's expected share is (1/16+1/5)/2=21/160<27/200. Both lottery components are in the previously named final-goal menu; implementing the lottery requires an explicit random installation kernel, not an assumption that a vNM utility uniquely chooses an interior lottery. This removal test illustrates why protection against all deterministic proposals is weaker than protection against the full feasible lottery set.
