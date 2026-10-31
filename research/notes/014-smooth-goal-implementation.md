# R0001 working note — smooth goals across physical opportunity sets

The homothetic goal menu in note 011 is a restriction, not a consequence of expected-utility rationality. This note constructs broader outcome-only goals that implement compromise at one physical budget and selfish production at another. The utilities are smooth, increasing and concave in **physical quantities**; their evaluation of lotteries remains linear in probabilities. No adoption or verification technology follows from the construction alone.

## 1. An explicit quadratic goal with a selfish war response

Let P>W>0 be peaceful and war production budgets, and let the desired peaceful allocation be p=(p_A,p_B), with p_A,p_B>0 and p_A+p_B=P. Choose 0<=rho<1 such that

$$z_p=p_A+\rho p_B>W.$$

For example rho=(P+W)/(2P) works for every such p, since z_p>=rho P>W. Set a=2P and b=a-(1-rho)z_p, and define

$$U(x_A,x_B)=a x_A+b x_B-\tfrac12(x_A+\rho x_B)^2.$$

On x_A,x_B>=0, x_A+x_B<=P this utility is concave, with Hessian minus the outer product of (1,rho) with itself. Both marginal utilities are strictly positive: U_A>=a-P=P, and U_B>=b-rho P>=P. At a fixed total output Y, the derivative along A's share is

$$\frac{d}{dx_A}U(x_A,Y-x_A)
=(1-\rho)[z_p-\rho Y-(1-\rho)x_A].$$

At Y=P it vanishes uniquely at x_A=p_A, with strictly negative second derivative -(1-rho)^2. Monotonicity ensures full production, so p is the unique optimum on the peaceful simplex. At Y=W the derivative remains strictly positive even at x_A=W because z_p>W; thus the unique postwar choice is (W,0). The same is true at every smaller positive war budget.

The modification therefore does not have to give the opponent a share after losing a war to the modified agent. In note 011's late-operator game, B's combat value remains (1-s)W. Any p_A>sW, p_B>(1-s)W is acceptable to the original agents and deters B's attack. The new U-agent also prefers peace: its peaceful optimum strictly exceeds every outcome in the smaller war simplex. For P>W there are such interior allocations. This recovers the ordinary bargaining-surplus boundary with a smooth, monotone, concave **output-only** goal, without a combat-history flag.

The goal is nonhomothetic. It can treat A-color as an inferior good over part of the budget range: more total resources allow it to reduce A's quantity while increasing B's. That feature is deliberate and must not be mistaken for a normal-goods assumption or for a universal preference class. It is a genuine change from original x_A preferences, since the new utility strictly values x_B as well.

## 2. Approximate optimization and changing budgets

For any full-output peaceful allocation x_A+x_B=P, the exact regret is

$$U(p)-U(x)=\tfrac12(1-\rho)^2(x_A-p_A)^2.$$

If a policy has expected U-regret at most epsilon_P, then either coordinate's root-mean-square allocation error is at most sqrt(2 epsilon_P)/(1-rho), and its expected signed error is bounded by the same quantity. This also holds when a policy underproduces: complete unused material into the *other* color, preserving the coordinate being bounded; monotonicity raises utility, and the full-frontier regret identity supplies the lower bound on original regret. Since both marginal utilities are at least P, expected unproduced quantity is also at most epsilon_P/P. At war budget W the derivative's minimum is

$$\mu=(1-\rho)(z_p-W)>0.$$

Moving t units from A to B on that war frontier loses at least mu t utility. Expected war regret epsilon_W therefore permits at most epsilon_W/mu expected B-output from an A victory. A sufficient robust B-deterrence condition is

$$p_B-(1-s)W>
\frac{\sqrt{2\epsilon_P}}{1-\rho}+s\frac{\epsilon_W}{\mu}.$$

This uses common actual utility units; rescaling U requires rescaling the regret tolerances. The war bound also allows underproduction: completing unused output into A preserves B's amount and can only reduce regret. These statements concern approximate production at the specified physical budgets, not errors in the physical model or in the opponent's utility.

For rho=(P+W)/(2P), the allocation curvature shrinks as the peaceful surplus closes. Exact implementation remains possible at every P>W, but a fixed approximation tolerance need not preserve agreement when P-W becomes small. The separate new-goal attack comparison has a margin of at least P(P-W): U(p)>=U(P,0), and U(P,0)-U(W,0)=(P-W)(3P-W)/2>=P(P-W). The allocation and attack margins are different quantities.

At another actual production budget Y, this same installed goal chooses

$$x_A^*(Y)=\operatorname{clip}_{[0,Y]}
\left(\frac{z_p-\rho Y}{1-\rho}\right).$$

Where interior, its derivative with respect to Y is -rho/(1-rho). A goal calibrated for P can change its division sharply when the physical frontier changes. Correctly knowing a stochastic law does not reveal its later realization, so uncertain budgets require evaluating the entire induced allocation rule, not substituting an expected P into the deterministic result.

## 3. Implementing any smooth two-color allocation schedule

Let P_max>0 and let m:[0,P_max]->R be twice continuously differentiable, with 0<=m(Y)<=Y. Interpret m(Y) as the desired A-output at each total budget Y. Write

$$M_1=\sup|m'|,\quad M_2=\sup|m''|.$$

Choose epsilon>0, K>epsilon P_max M_2, and

$$C>2KP_{max}+2\epsilon P_{max}(1+M_1).$$

For Y=x_A+x_B and d=x_A-m(Y), define

$$V(x_A,x_B)=CY-KY^2-\epsilon d^2.$$

Then V is strictly increasing in each quantity, strictly concave on the physical simplex of total at most P_max, and uniquely implements (m(Y),Y-m(Y)) at every budget Y in that interval.

**Proof.** Since |d|<=P_max, the original-coordinate partial derivatives are

$$V_B=C-2KY+2\epsilon d m'(Y),$$
$$V_A=C-2KY+2\epsilon d[m'(Y)-1],$$

and the choice of C makes both positive. In coordinates (Y,x_A), V_AA=-2epsilon, V_YA=2epsilon m', and

$$V_{YY}=-2K-2\epsilon(m')^2+2\epsilon d m''.$$

The Schur complement of V_AA is -2K+2epsilon d m''<0. Hence the Hessian is negative definite; the invertible linear change of coordinates preserves negative definiteness. Monotonicity puts every maximizer on the full-budget line. There CY-KY^2 is fixed, and the negative square has its unique maximum at x_A=m(Y). The zero-budget case has only the origin. This proves the statement, including target allocations on the boundary.

The construction does not require this highly expressive menu in every model. It shows why failure of one fixed goal blend should not be generalized to all smooth concave successor utilities. Verification, coefficient precision, installation and ongoing deviation incentives remain separate obligations.

## 4. An explicit smooth transition between war and peace

For W<P and desired fraction alpha in (0,1), let chi(Y)=0 for Y<=W, chi(Y)=1 for Y>=P, and on the intervening interval set

$$\chi(Y)=6t^5-15t^4+10t^3,\qquad t=(Y-W)/(P-W).$$

This function and its first two derivatives join continuously at the endpoints, and 0<=chi<=1. Define

$$m(Y)=Y[1-(1-\alpha)\chi(Y)].$$

It satisfies 0<=m(Y)<=Y, gives all output to A at every Y<=W, and gives alpha Y to A at Y>=P. Section 3 therefore supplies a strictly concave, strictly increasing utility that implements those choices. A shrinking separation P-W enlarges the derivatives and the sufficient coefficients; the construction is not a claim of implementation robust to fixed numerical errors at zero surplus.

More generally, at finitely many distinct positive budget levels one may prescribe any feasible allocation and interpolate the fractions m(Y)/Y smoothly, using constant fractions near each prescribed level and bounded smooth transitions between them. The resulting m is C2 and stays in [0,Y]. At Y=0 choose a constant fraction on a neighborhood. The theorem then implements every prescribed allocation uniquely. Identical budget levels with different desired unique allocations cannot be treated this way.

## 5. Asymmetric winners and the exact separation obstruction

Let original war outcomes be (W_A,0) with probability s and (0,W_B) otherwise. If a peaceful full-output allocation p strictly exceeds both components of that mean, then every increasing concave utility U satisfies

$$U(p)>U(sW_A,(1-s)W_B)
\ge sU(W_A,0)+(1-s)U(0,W_B).$$

Thus, if a concave successor objective implements p at the peaceful budget P and its original selfish allocation (W_A,0) at the A-winner budget W_A, its new self also prefers peace. B's original goal keeps its original war response. A's original adoption and B's attack deterrence are exactly the two component inequalities. Such p exists iff P>sW_A+(1-s)W_B.

When P and W_A are distinct, the smooth-schedule theorem can implement both specified allocations, even if W_A>P; use a domain up to max(P,W_A,W_B). Concavity then supplies the displayed attack comparison. This establishes a local output-only implementation construction under asymmetric winner technology, not a claim that peace has more output than each possible war result.

When P=W_A and the peaceful p is interior, **no single output-only utility can uniquely choose both p and (W_A,0) from that same full simplex**. The feasible set is identical. This is an implementation obstruction even when a strict bargaining surplus exists because W_B is small. A history-dependent criterion, different control constraints, or a changed war response can resolve a different model; changing the utility's expressivity while retaining the same outcome-only choice problem cannot.

For a continuous allocation schedule, if war budgets requiring all-A production accumulate at P, continuity likewise forces m(P)=P. Therefore a positive separation of the relevant budget supports matters when one wants a smooth goal preserving the selfish response in every war state. Perfect modeling does not remove that restriction. The deterministic finite-budget construction is not automatically a result for overlapping stochastic opportunity sets.

## 6. More than two projects

For n projects and x>=0 with total Y<=P_max, let m(Y) be a C2 vector of nonnegative target quantities summing to Y. Put d=x-m(Y), so sum d_i=0, and

$$V(x)=CY-KY^2-\epsilon\|d\|^2.$$

Let D=sqrt(2)P_max, M_1=sup||m'|| and M_2=sup||m''||. Choose K>epsilon D M_2 and C>2KP_max+2epsilon D(1+M_1). Each partial derivative equals C-2KY-2epsilon d dot(e_i-m'), hence is positive. In coordinates Y and any orthonormal coordinates on the sum-zero subspace, the transverse Hessian is -2epsilon I and its Schur complement is -2K+2epsilon d dot m''<0. Thus V is strictly concave and uniquely implements m(Y) at every budget.

This is an executor construction for multiple physical projects. It says nothing by itself about coalition consent, stability, representation of identical goals, external war, or population selection. Those require their own game and identity assumptions.

## 7. A strength-weighted operator draw implements a familiar surplus division

At a checkpoint with already specified net P,W_A,W_B and common strength share s, suppose the selected operator can install an implementing goal and make a take-it-or-leave-it allocation that its counterpart accepts at its original war reservation. Use the peaceful tie selection, public reliable implementation and the absence of additional unaccounted costs. The preceding constructions supply one such implementation when their opportunity-set conditions hold; a binding fixed-utility delegate can supply another.

If A operates, it retains P-(1-s)W_B; if B operates, it leaves A sW_A. The operator draw picks A with probability s, so

$$E[x_A]=sP+s(1-s)(W_A-W_B)
=sW_A+s[P-sW_A-(1-s)W_B].$$

Likewise B receives its disagreement value plus fraction 1-s of the surplus. This is exactly the weighted log-gain allocation from note 010 section 12 **in expected linear founder utility**, now generated by a specific random-proposer/commitment protocol. It is deterministic strength-proportional output only in special implementations; even with symmetric war output it is generally a lottery whose mean is (sP,(1-s)P).

This algebra does not bypass endpoint indifference, equilibrium selection, earlier attacks during costs, or the need for actual commitments. With nonlinear original utilities the same output means need not deliver the same welfare or bargain. The contribution is an explicit connection between the essay's shared strength parameter, a bargaining protocol and the resulting expected surplus shares, not a novelty claim about bargaining theory.
