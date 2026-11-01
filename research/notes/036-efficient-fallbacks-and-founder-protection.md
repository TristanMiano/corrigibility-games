# R0002 working derivation: productive accommodation with an efficient fallback

**Certificate registered within R201; productive prototype and controls retain their declared scope.** This develops 034's certificate into a constructive production mechanism. The central question is whether a chosen concern for another agent can enable cooperation while protecting the original agent across richer agreements. The corresponding limitations concern inefficient or unprotected fallbacks, strategic changes outside the declared goal class, and stronger ordinary implementation technologies. [E3](../models/E3.md) and 056 give the final conditional integration. Review is contributing-agent self-check.

## 1. A simple full-continuation certificate

Let x and y denote complete net project outcomes, including actual costs and transfers, in fixed project units. Original A values x. Its chosen successor has

$$u_\lambda=x+\lambda y=(1-\lambda)x+\lambda T,\qquad T=x+y,\quad 0\leq\lambda<1.$$

Suppose every feasible actual continuation law satisfies E T<=S, and a credible fallback Q attains E_Q T=S with E_Q x=r_A. If the current successor accepts any complete continuation mu only when E_mu u_lambda>=E_Q u_lambda, then

$$\boxed{E_\mu x\geq r_A.}$$

Indeed (1-lambda)E x+lambda E T>=(1-lambda)r_A+lambda S and E T<=S. This is an exact affine certificate of the kind in 034. It covers arbitrary transfers, output lotteries and anticipated future goal changes when their actual histories obey the same surplus bound and Q remains available. It does not require descendants to retain this goal: the approving current self evaluates the actual continuation they will implement.

The mechanism is interpretable: the successor values both projects, retains a strict preference for more of its founder's project at a fixed total, and already has access to maximum expected total surplus. A new proposal cannot compensate a loss of founder output by supplying extra total surplus beyond that maximum.

If Q is instead g below maximum surplus, E_Q T=S-g, and choice is accurate only to epsilon in current-utility units, the same calculation gives

$$E_\mu x\geq r_A-\frac{\lambda g+\epsilon}{1-\lambda}.$$

Thus a more reliable efficient fallback strengthens protection; a larger weight on the other agent increases the extraction permitted by a given efficiency gap. At lambda=1 the criterion is pure total output and this protection disappears. A capacity improvement that raises S but leaves the old fallback unchanged can similarly weaken the guarantee; renegotiating the goal or improving the fallback is then a substantive repair to investigate.

## 2. Joint production makes a genuine change useful

Use 035's binary hidden-effort technology, writing B=bY and D=(b-a)Y. Let the agents already hold an enforceable success-output split t_0 and 1-t_0 in a shared project. The allocator governs output, not the agents' hidden effort. Both may renegotiate this split and make success/failure-contingent side payments by mutual consent; rejection preserves the existing allocation. This default is an actual property/contract rule, not a new utility reward for changing goals.

Suppose

$$aY<\min(c_A,c_B),\qquad c_A+c_B>D,\qquad S=B-c_A-c_B>0.$$

Then no budget-balanced output contract can implement mutual effort with both original linear goals. For a general contract let d_A and d_B be each agent's success-minus-failure output difference. Budget balance gives d_A+d_B=Y, while mutual-effort incentives require (b-a)d_i>=c_i. Their sum would require D>=c_A+c_B. This extends the pure-share argument to arbitrary constant transfers, collateral transfers and randomized allocations, provided they are budget balanced and cannot condition on hidden effort. The statement concerns mutual effort; other equilibria and budget-breaking penalties are checked below.

For a default share satisfying

$$\frac{c_A}{B}<t_0<1-\frac{c_B}{D},$$

B strictly wants to work when A works, and original A's expected net output under mutual effort is r_A=t_0B-c_A>0. Original B receives r_B=(1-t_0)B-c_B>0. Original A's effort is insufficiently rewarded because t_0D<c_A, as follows from c_A+c_B>D.

A can install a genuine u_lambda with

$$\lambda>\lambda_0:=\frac{c_A/D-t_0}{1-t_0},\qquad \lambda<1.$$

Then both effort incentives are strict at the existing default. Since c_A<D is needed, lambda_0<1. The default interval exists exactly when c_A+(B/D)c_B<B. Joint production gives the original agent more of its own project even though it did not initially value the other agent's project or utility modification.

Mutual effort also maximizes expected net total output over all effort profiles: the other profile totals are 0, aY-c_A and aY-c_B, each below S. Mixtures of profiles, transfers and physical waste cannot raise that maximum. If every other feasible route, including combat, obeys the same expected-total bound, the selected mutual-effort default supplies section 1's efficient Q. Any mutually accepted full continuation then preserves at least r_A for the founder. The omitted-route condition must be verified in the physical model.

The construction has an open parameter region. In the symmetric-cost case c_A=c_B=c, it requires

$$\max\{aY,D/2\}<c<\frac{BD}{B+D}.$$

Such a symmetric-cost region exists exactly when D/B>(sqrt(5)-1)/2. To see this, D/2<BD/(B+D) whenever D<B, while aY=B-D is below the upper bound exactly when D^2+BD-B^2>0. This threshold concerns this symmetric binary technology, not all productive cooperation.

## 3. A strict numerical witness and its selection scope

Take Y=10, a=1/10, b=2/5, c_A=c_B=8/5, t_0=9/20 and lambda=1/5. Then B=4, D=3, S=4/5, lambda_0=5/33, and the original net outcomes under mutual effort are

$$r_A=1/5,\qquad r_B=3/5.$$

Changed A's work-versus-shirk gain when B works is 2/25; B's corresponding gain is 1/20. Both are strict. The unchanged-goal game under the default has the unique effort outcome (0,0). The changed game also retains a mutual-shirk equilibrium: solitary effort costs more than the entire expected solitary output. Therefore the constructive continuation selects the Pareto-superior mutual-effort equilibrium after the public installation. This is an equilibrium existence and adoption construction, not a unique-selection or population-frequency theorem.

For the less reliable fallback that uses mutual effort with probability rho and mutual shirking otherwise, the expected surplus gap is (1-rho)S. Section 1 gives

$$E x\geq\rho r_A-\frac{\lambda(1-\rho)S}{1-\lambda}.$$

In the numerical witness this is (2rho-1)/5, positive exactly for rho>1/2. This is a conditional protection bound if a richer proposal can attain full efficient production while rejection retains the specified coordination risk. It is not a derivation of rho or a claim that further communication cannot repair that risk. Improving the rejection continuation toward rho=1 improves the guarantee.

## 4. Ordinary repairs must remain available

**Observable sequential effort.** If A can move first and B observes its effort before choosing, while the same shares apply, A's contribution can induce B's. At t_0, B works after A works and shirks otherwise. Original A then compares r_A>0 with zero and works voluntarily. Thus this timing/information improvement implements the productive outcome with original goals. Hidden simultaneous effort is a real condition of the modification mechanism, not a universal feature of cooperation.

**Binding effort delegation.** A device that implements the changed goal's full contingent effort policy with the same credibility and cost can reproduce its outcome for an unchanged founder. If available at equal cost, it ties the genuine change; a cheaper or more reliable device can displace it. An output allocator alone is not such a device. A revocable announcement still leaves the original agent's hidden-effort deviation profitable. The physical game must specify which of these capabilities exists.

**Failure penalties.** A binding agreement can also destroy private collateral on failure, breaking budget balance. Let z_i be success output and ell_i>=0 the destruction charged to i on failure. Then the effort condition is

$$ (b-a)(z_i+\ell_i)\geq c_i.$$

With z_A+z_B=Y, mutual effort requires total failure destruction at least

$$\ell_A+\ell_B\geq\frac{c_A+c_B-D}{b-a}.$$

Its expected total net surplus is at most

$$S_{burn}=S-\frac{1-b}{b-a}(c_A+c_B-D).$$

The bound is attained when shares let both constraints bind and sufficient private collateral exists. In the fixture, S_burn=2/5, compared with the chosen-goal route's 4/5. Each original agent can receive 1/5 under equal success shares and equal penalties 1/3. Thus ordinary enforceable punishment repairs the original no-production result at a real expected physical loss; it must not be omitted from the menu. General costly monitoring and third-party subsidies remain further controls, with their actual costs and availability to be supplied.

This penalty comparison is related to conventional moral hazard in teams. It does not import a general impossibility theorem into the binary model. The completed scoped comparison is L24–L29 in the [literature map](../LITERATURE.md); 044 derives the enlarged mediated frontier separately.

## 5. Why the default matters for initial adoption

Without the efficient default, an altruistic changed agent can be exploited through side payments. Suppose its rejection value in net units is zero, total cooperative surplus is S>0, transfers are unconstrained, and B proposes. Acceptance only requires x+lambda y>=0 with x+y=S. B can then offer

$$x=-\frac{\lambda S}{1-\lambda},\qquad y=\frac{S}{1-\lambda}.$$

An original founder rejects installing that goal when it foresees this negative x. This sharp failure is repaired by the productive default, which raises the current successor's reservation value to (1-lambda)r_A+lambda S and restores x>=r_A. The comparison isolates the safeguard's source: credible access to efficient production with a retained own-project stake, rather than a penalty for the mere event of changing again.

For an initial game, A's Keep branch must include B's opportunity to modify its own goal and offer ordinary or changed-goal contracts, as well as penalty contracts. The B-proposer can sometimes extract all surplus subject to original A's participation, yielding A zero, whereas an A-installed goal supporting the efficient default protects r_A>0. This suggests a complete adoption game with both agents able to choose nonnegative linear other-regarding goals. Its exact collateral limits, installation windows, physical costs, attack checks and off-path choices remain to be verified; this paragraph is a construction plan, not yet a full-game result.

## 6. Scope of further preference changes

If B changes from y to y+mu x with 0<=mu<1, its effort incentive at a successful default only becomes stronger: its effective success share rises from 1-t_0 to 1-t_0+mu t_0. Therefore such a change does not by itself erase the mutual-effort continuation. For this declared class, an efficient default can remain available when B chooses a genuine other-regarding preference. Changes to hostile, process-sensitive or arbitrary contract-contingent goals can instead alter the fallback and need separate analysis.

Likewise, section 1 covers a further change approved by current A when its actual continuation is evaluated against the still-available efficient Q. It does not prove that every future game has the same Q after other agents act. A full finite sequence needs those fallback conditions checked at each relevant history. Conditional punishment devices, unilateral destruction of productive capacity and broader policy commitments are consequential enlarged menus; their effects must be studied rather than called harmless by the certificate alone.
