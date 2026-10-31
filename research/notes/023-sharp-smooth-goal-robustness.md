# R0001 working note: the sharp local accuracy bound

This sharpens note 017's second-order result. It concerns a local, output-only goal implementation problem with specified physical frontiers and independent expected-regret error sets. It is not an equilibrium-selection theorem or a bound on computation, energy, code length, or verification complexity. Proofs are AI self-checked only; no literature-priority claim is made.

## 1. Normalize the physical simplex, not the agents' strengths

Measure output in units of the peaceful frontier P. Write

$$r=W/P,\quad d=1-r,\quad b=1-s,\quad
p=(s,b),\quad w=(r,0).$$

Here s remains the actual combat victory probability of A, using the same strength coordinate as the E2 control mechanism. A is the selected production operator at the local checkpoint. The original goals are own-color quantities. B remains capable of attacking and, if it wins, produces (0,r).

Consider increasing concave goals U with U(0)=0, U(p)=1, unique peaceful optimum p and unique postwar optimum w. Peace and A-victory production can independently be any lotteries over their respective simplexes whose expected U-regrets are at most epsilon. Initial installation must also satisfy note 020's timing conditions; this note uses the same r for initial and final threat comparisons.

Assume the explicit small-surplus region

$$0<d\leq sr,\qquad r\geq s.$$

Every fixed interior s satisfies these conditions for sufficiently small positive d. They are sufficient conditions for the exact construction below, not permanent restrictions on E2.

Define

$$k=\sqrt{sr},\qquad
\gamma=\frac d{1+k},\qquad
\eta=\frac{dk}{1+k}=k\gamma,\qquad
\epsilon_* =\gamma^2=\frac{d^2}{(1+\sqrt{sr})^2}.$$

**Result.** Over smooth, strictly increasing, strictly concave goals in this local class, the supremal common regret allowance that uniformly guarantees strict original-A adoption, strict B attack deterrence, and strict current-A preference for peace is epsilon_*. Every epsilon<epsilon_* is attainable by such a goal. No goal in the larger increasing concave class can provide uniform strict B deterrence at epsilon>=epsilon_*.

The distinction between a supremum and an attained strict boundary matters: at epsilon_* an allowed adverse implementation can make B indifferent to combat.

## 2. Why no concave goal can exceed the bound

For any admissible goal, let gamma_U=1-U(w)>0 and eta_U=U(w)-U(rp)>0. Concavity implies gamma_U+eta_U<=d. A peaceful policy can mix geometrically between p and w, then fill the unused budget with A output; a postwar policy can take a convex combination of w and rp. These are deterministic feasible worlds, not an assumed ability to enforce a lottery.

With uncapped combination weights epsilon/gamma_U and epsilon/eta_U, strict B deterrence requires

$$\epsilon\left(\frac1{\gamma_U}+
\frac{sr}{\eta_U}\right)<d.$$

If either weight reaches one, the same deterrence requirement fails under d<=sr; note 017, section 5, checks those caps. Cauchy-Schwarz gives

$$\frac1{\gamma_U}+\frac{sr}{\eta_U}
\geq\frac{(1+\sqrt{sr})^2}{d}.$$

Therefore epsilon<epsilon_* is necessary. This obstruction already concerns B's actual war payoff, including B output made by an approximately optimizing A after A wins.

## 3. Three affine pieces protect all three decision criteria

Set

$$K=\frac{\eta}{rb},\qquad H=\frac\gamma b,\qquad a=1+\frac\eta r,$$

and define

$$L_W(x)=a x_A+(a-K)x_B,$$
$$L_B(x)=1-\gamma+H x_B,$$
$$L_A(x)=x_A/s,\qquad
U_*(x)=\min\{L_W(x),L_B(x),L_A(x)\}.$$

All three pieces are nondecreasing. In fact a-K=1-eta s/(rb)>0: r>=s implies rb/s>=b, while eta<d<=b. Their minimum is concave, with U_*(0)=0 and U_*(p)=1. It is an intermediate nonsmooth goal; section 5 supplies strict smooth versions.

At a full peaceful budget, write x_B=b+z. Then L_W=1-Kz and L_B=1+Hz. If z<0, L_B<1; if z>0, L_W<1. At z=0, x=p. Strict positivity of L_W's coordinates and the other bounds exclude an underproducing alternative maximum. Thus p is the unique peaceful optimum.

At w, L_W=L_B=1-gamma and L_A=r/s>=1. For postwar output (r-y,y), L_W=1-gamma-Ky. Thus every y>0 has lower value; underproduction cannot improve it. The postwar optimum is uniquely w. Also U_*(0,r)=0, because L_A is zero there.

The third piece is essential to the full participation certificate. It protects original A without weakening the sharp opponent-deterrence bound. Using only the first two pieces can let a weak original A lose too much from an allowed peaceful production error.

## 4. Exact uniform bounds, including lotteries and underproduction

The affine upper bounds on U_* imply, for any peaceful epsilon-regret lottery,

$$E[x_B]\geq b-\epsilon/H,\qquad
E[x_A]\geq s(1-\epsilon).$$

The first follows from E[U_*]>=1-epsilon and U_*<=L_B; the second uses U_*<=L_A. No Jensen approximation or full-production assumption is needed.

For any postwar epsilon-regret lottery, L_W(x)<=ar-Kx_B on the r-simplex, so

$$E[x_B\mid A\ wins]\leq\epsilon/K.$$

Consequently B's peaceful payoff minus its actual attack payoff is at least

$$bd-\epsilon(1/H+s/K)
=bd-\epsilon b\frac{(1+k)^2}{d}>0$$

whenever epsilon<epsilon_*. The original A gets more than sr, because epsilon_*<d and E[x_A]>=s(1-epsilon). Its installed goal values peace at least 1-epsilon and combat at most s(1-gamma), since B's victory gives U_*(0,r)=0. The latter margin is positive: b+s gamma>=gamma>gamma^2=epsilon_*.

Thus all three relevant criteria prefer the local peaceful continuation throughout the strict range. The statement does not assume that the incumbent originally values the newly installed objective.

### The boundary is real

At epsilon=epsilon_*, choose peaceful output

$$x^P=(s+b\gamma,\ b(1-\gamma))$$

and, after A wins, choose

$$x^W=(r-y,y),\qquad y=\epsilon_*rb/\eta.$$

The peace regret is exactly epsilon_* from L_B. For the war output, theta=epsilon_*/eta=d/[k(1+k)]<=1 under d<=k^2, and x^W=(1-theta)w+theta rp. L_W is active throughout this segment: it agrees with U_* at both endpoints, and each other affine piece is at least as large at both endpoints. The war regret is therefore exactly Ky=epsilon_*.

B's peace and combat payoffs coincide, since

$$b\gamma+s y=b\gamma+k b\gamma=bd.$$

This supplies explicit adverse implementations, rather than merely an unattained dual bound. The originally installed A still has a well-defined preference and combat remains available to B at this equality.

## 5. Smooth strictly concave goals approach the sharp bound

Choose a small slack zeta in (0,gamma), replace H by H_zeta=(gamma-zeta)/b, and replace the B piece by

$$L_{B,\zeta}(x)=1-\gamma+\zeta+H_\zeta x_B.$$

All three pieces still equal one at p. At w the B piece is now zeta above L_W, making a strict postwar slope possible after smoothing. Let U_zeta be their minimum. On x_B<=b, the changed piece increases by at most zeta; on x_B>=b, that piece is at least one and cannot lower the minimum. Hence

$$0\leq U_\zeta-U_*\leq\zeta$$

on the entire peaceful simplex. The peaceful and war optima are still p and w.

Let c_A=1/s and choose positive weights

$$w_A=\frac{H_\zeta}{2(H_\zeta+c_A)},\qquad
w_W=\frac{H_\zeta}{2(H_\zeta+K)},\qquad
w_B=1-w_A-w_W.$$

Both of the first two weights are below 1/2, so w_B>0. Direct substitution gives w_W K+w_A c_A=w_B H_zeta. Define the weighted soft minimum

$$S_\tau(x)=-\tau\log\!\left(
w_W e^{-L_W(x)/\tau}+w_B e^{-L_{B,\zeta}(x)/\tau}
+w_A e^{-L_A(x)/\tau}\right),$$

and normalize U_tau(x)=[S_tau(x)-S_tau(0)]/[1-S_tau(0)]. Choose tau small enough that S_tau(0)<1. Since all pieces equal one at p, S_tau(p)=1 exactly.

The gradient is a strictly positive weighted combination in each coordinate: L_W has both coordinates positive, L_A has a positive A coefficient, and L_B,zeta has a positive B coefficient. The Hessian is minus the weighted covariance of the three affine gradients divided by tau. These gradients are affinely independent: the W and A gradients are distinct and have dot product one with p, while the B gradient has dot product gamma-zeta<1 with p. Thus the covariance is positive definite and S_tau is strictly concave everywhere on the simplex.

The weight identity makes the derivative along the peaceful frontier zero at p, so p remains its unique optimum. At w, the derivative in the direction (-1,1) has a numerator proportional to

$$-w_W K+w_B H_\zeta e^{-\zeta/\tau}
-w_A c_A e^{-D_A/\tau},\qquad
D_A=r/s-(1-\gamma)>0.$$

Put R=w_B H_zeta/(w_W K)>1. Choosing tau<zeta/log(2R) makes this derivative strictly negative. Concavity then makes w the unique optimum on the war frontier, and monotonicity extends both optimum statements to their whole simplexes.

For an explicit uniform approximation bound put L=log(1/min_j w_j). The weighted soft-minimum inequalities give 0<=S_tau-U_zeta<=tau L and 0<=S_tau(0)<=tau L. Since 0<=U_zeta<=1,

$$\|U_\tau-U_*\|_\infty
\leq\zeta+\frac{\tau L}{1-\tau L}=:e,$$

provided tau L<1. For any prescribed epsilon<epsilon_*, first take zeta small and then tau still smaller so epsilon+2e<epsilon_* and the strict war-slope condition holds. Every epsilon-regret implementation for U_tau is an (epsilon+2e)-regret implementation for U_*; the latter has the strict original-agent output bounds in section 4. The current U_tau peace/war comparison also remains strict: its war value is at most s(1-gamma)+e, while peace is worth at least 1-epsilon, and epsilon+e<epsilon_*<b+s gamma.

This proves attainment of every strict sub-bound by a smooth, strictly increasing, strictly concave objective. It does not claim attainment of the strict boundary epsilon_* itself.

## 6. What the sharp result does and does not settle

The constant improves note 017's sufficient bound without changing its second-order scaling. It isolates a geometric limitation of output-only concave goals under two independent regret budgets. The third affine piece shows how to protect founder participation without paying a worse asymptotic or exact local bound in the stated region.

Different pre-installation threat frontiers, history-dependent goals, nonconcave objectives, correlated algorithm errors, hidden parameters, unprotected installer choices, or smaller actual error sets require new analysis. An enforceable fixed-utility delegate with the same conditional policy and accuracy can match the physical outputs. This construction does not settle which implementation is cheaper, credible, or selected in a full negotiation game.
