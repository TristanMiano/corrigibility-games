# R0002 audit and extension: concave survivors and broader original goals

**Derived correction and generalization.** A linear own-priority survivor allocates every recovered unit to its own project. A strictly concave own/other criterion may allocate some to the defeated agent's project. This note checks the actual postwar optimization and extends the guarded productive construction to a familiar family of diminishing-returns original goals.

## 1. A survivor's allocation must be optimized under its current goal

Let a winner control W recovered units and value f(x)+lambda f(y), where x is its own project, y the other project, 0<=lambda<1 and f is strictly increasing and strictly concave. The unique optimum uses x+y=W, assigns x>=W/2, and at an interior solution satisfies f'(x)=lambda f'(y). The boundary y=0 is optimal when lambda f'(0)<=f'(W), with the usual one-sided derivative interpretation. Thus own priority does not in general mean zero output for the defeated agent.

For the normalized family

\[
f_\gamma(x)=
\begin{cases}
[(1+x)^{1-\gamma}-1]/(1-\gamma),&\gamma\ne1,\\
\log(1+x),&\gamma=1,
\end{cases}\qquad\gamma>0,
\]

put a=lambda^(1/gamma). The defeated project's quantity is

\[
\boxed{\ell_{\lambda,\gamma}(W)=
\max\left\{0,\frac{a(1+W)-1}{1+a}\right\}.}
\]

This follows by solving 1+y=a(1+x) on the full-output line and checking the boundary. For the logarithmic goal, a=lambda. At lambda=1/5 and W<=4 the defeated project's output is zero, including the unique boundary optimum at W=4. At lambda=3/10 and W=4 it is 5/13. Both allocations remain physically bounded by the same recovery frontier.

Where positive, defeated output increases with lambda and, for fixed 0<lambda<1, with gamma. This is a comparative result about realized project quantities. It is not a general monotonicity theorem about equilibrium cooperation: the larger gift also raises an original opponent's payoff from losing a contest against that survivor.

## 2. Recheck the diversified logarithmic witness

In 053, the installed lambda=1/5 makes the earlier own-priority combat calculation valid. A broader safe interval, including lambda in [1/10,3/10], also preserves the original outside bound when combat strength is equal. An incompatible agent can receive at most W<=4 if it wins. If it loses to a logarithmic compatible survivor with lambda<=1, it receives at most W/2<=2. Therefore

\[
E\log(1+X_i^{combat})
\le\tfrac12\log5+\tfrac12\log3
=\tfrac12\log15<\log4.
\]

The inequality includes the defeated agent's project output; it does not set its welfare to zero by fiat. Retained stock still bounds the original combat alternative, so the diversified gain above log4 remains a strict adoption gain.

After both calibrations but before the reaction signal, the total finished material in the diversified witness is at most 266/100. Any current combat allocation then gives

\[
G_i^{base}\le(1+\lambda_i)\log(366/100),
\]

excluding the already-earned process reward, which cancels. The cooperative base is (1+lambda_i)U_(3,3,0), and U_(3,3,0)>log4>log(366/100). Thus attack is strictly inferior for every strength split at this stage, independently of which concave allocation the survivor selects. After the signal, both holdings exceed the whole remaining recovery frontier 4/11, so the comparison is pointwise. Before calibration, beta_i>=4/5 covers the smaller remaining utility gap to the W<=4 combat bound; the precise finite inequalities are checked in the tests.

For a general strength p and a logarithmic original opponent, a sharper upper bound is

\[
p\log(1+W)+(1-p)\log[1+\ell_{\lambda,1}(W)].
\]

Increasing the prospective winner's concern lambda increases this incompatible opponent's outside payoff once ell is positive. That feedback must be included when changing goal parameters and strength together. The sufficient equal-strength adoption region above survives it.

## 3. Both original goals can belong to any fixed diminishing-returns power class

Use the symmetric single-batch productive instance of 052, but let both original goals be f_gamma with any fixed finite gamma>0. Set z=R+1 and let each full-effort material increment D equal -33/20 with probability 3/5 or 67/20 with probability 2/5. Then

\[
m=E D=7/20,\qquad E D^2=2449/400.
\]

Taylor's formula and f_gamma''(x)=-gamma(1+x)^(-gamma-1) give, for z>33/20,

\[
E f_\gamma(R+D)-f_\gamma(R)
\ge m z^{-\gamma}
-\frac{\gamma E D^2}{2(z-33/20)^{\gamma+1}}.
\]

Hence the explicit sufficient condition

\[
\boxed{2m(z-33/20)^{\gamma+1}>
\gamma(E D^2)z^\gamma}
\]

makes both original agents strictly prefer the productive outcome to retained stocks. A simple explicit sufficient stock condition is

\[
\boxed{R\ge13\max\{1,\gamma\}-1.}
\]

To check it, divide the preceding inequality by z^gamma. Bernoulli's inequality with exponent gamma+1>=1 gives

\[
2mz(1-33/(20z))^{\gamma+1}
\ge \tfrac7{10}[z-\tfrac{33}{20}(\gamma+1)].
\]

For gamma>=1 and z>=13gamma, the right side is at least (679/100)gamma, strictly above (2449/400)gamma. For 0<gamma<=1 and z>=13, it is at least 679/100, again strictly above (2449/400)gamma. Thus the sufficient stock condition holds for every finite positive gamma and every larger R. The bound is conservative; the exact logarithmic threshold in 052 is sharper.

Full effort and equal statewise allocation maximize W=f_gamma(X)+f_gamma(Y) under that condition. Equal division is optimal at every total by strict concavity. Solitary effort lowers expected total relative to the no-effort stocks, so Jensen places its optimal welfare below stock retention; mixtures and waste cannot improve the bound. Full effort's strict original improvement then makes it the unique maximizing effort profile. This is the same welfare-certificate mechanism, not a separate argument from mere higher expected material output.

Choose successors f_gamma(X_i)+lambda_i f_gamma(X_j)+beta_i e_i-K_iI_i. A finite beta_i above the maximum f_gamma loss from calibration makes effort strict in the fixed-contract subgame. For the full continuation, [056](056-contribution-rewards-through-renegotiation.md) uses a finite reward above the bounded output base and preserves missed-obligation history through later changes. Choose K_i above the whole base plus reward. The initial guarded-choice theorem therefore applies whenever its attestation and entry conditions hold. The displayed stock condition also ensures R-33/20>4, so every possible own productive holding exceeds the entire combat recovery frontier, making all on-path attack comparisons strict at every strength split. Original incompatible combat also gives at most four units, below R.

Thus **for each fixed finite gamma>0, sufficiently large stocks support voluntary guarded goal change by two f_gamma founders, with combat retained**. This is a quantified preference-and-environment class. It does not say that arbitrarily high curvature is harmless at a fixed stock, that stocks are typically large, or that verification is cheap in actual agents. The lower-stock diversification repair in 053 and the risk boundary in 052 explain how changing the production arrangement can supply another route.

## 4. Representation and physical scope

The normalization f_gamma(0)=0 and f_gamma'(0)=1 fixes the stated units. Equivalent affine recodings require corresponding changes to utility weights and penalty bounds. The logarithmic finite witness and rational/integer gamma examples have explicit descriptions; arbitrary real parameters need their own representation and verification technology. The analytical class does not supply an arbitrary semantic oracle.

This correction changes the survivor allocation used in a combat calculation, while preserving the established initial and on-path bounds through stronger arguments. The general saturated-welfare theorem already allowed this allocation; an own-only survivor shortcut must be used only for the linear or insured criteria for which it was proved.

## 5. At fixed stocks, a precise curvature boundary orders the risky bargain

Let

\[
F_\gamma(R)=\tfrac35 f_\gamma(R-33/20)
            +\tfrac25 f_\gamma(R+67/20)-f_\gamma(R),
\qquad R\ge33/20.
\]

For every fixed finite R in this domain there is a unique gamma_*(R)>0 such that

\[
F_\gamma(R)>0\quad\Longleftrightarrow\quad0<\gamma<\gamma_*(R),
\]

with equality at gamma_*(R). This is a preference boundary for the same actual risky productive outcome versus certain stock retention, with all material costs included.

**Proof.** If gamma_2>gamma_1, write f_gamma2=phi composed with f_gamma1 on the bounded output interval. Its derivative with respect to f_gamma1 is (1+x)^(gamma_1-gamma_2), strictly decreasing in x, so phi is strictly increasing and strictly concave. Jensen on the nondegenerate two-state output therefore implies that weak acceptance under gamma_2 entails *strict* acceptance under gamma_1. This orders the acceptance sets without falsely claiming that differently normalized utility differences themselves are numerically monotone.

The gain is continuous in gamma, including its logarithmic value at gamma=1. As gamma tends to zero it tends to the positive expected material increment 7/20. For sufficiently large gamma>1 it is negative: writing z=R+1, the sign is that of

\[
1-\tfrac35(1-33/(20z))^{1-\gamma}
 -\tfrac25(1+67/(20z))^{1-\gamma},
\]

whose negative first power term grows without bound as gamma grows. Continuity gives a zero; the strict comparison above permits only one and fixes the signs on either side. QED.

Two exact checks make the boundary interpretable:

The threshold gamma_*(R) strictly increases with R when this technology and combat-work frontier are held fixed. For a positive stock increment d, the derivative of f_gamma(x+d) with respect to f_gamma(x) is [(1+x)/(1+x+d)]^gamma, strictly increasing in x. Thus the former is a strictly convex increasing transform of the latter. Jensen implies that weak acceptance of the nondegenerate increment at the smaller stock becomes strict acceptance at the larger stock. Applying this to gamma_*(R) proves the strict expansion of the accepted curvature range. A simultaneous change in military strength or production technology needs its own comparison.

- At R=3, gamma=1/2 strictly favors the single batch, while gamma=1 favors retention. For gamma=1/2, positivity is equivalent to 3sqrt(47/20)+2sqrt(147/20)>10. Squaring positive sides reduces it to 144*6909>989^2. Thus 1/2<gamma_*(3)<1. The earlier logarithmic small-stock failure is a curvature boundary, with a successful less-curved counterpart in the same physical technology.
- For gamma=2, the exact gain is

\[
F_2(R)=\frac{(7/20)z-2211/400}
 {z(z-33/20)(z+67/20)},\qquad z=R+1.
\]

It is positive exactly when R>2071/140, approximately 14.792857. Thus gamma=2 needs a larger stock buffer than the logarithmic threshold R>6.7392; the general R>=25 bound from section 3 for gamma=2 is conservative.

At R=3 and gamma=1/2, the integrated guarded execution can use 056's finite reward bound and the same 32-slot schedule. The welfare maximum is the symmetric full-effort allocation. At equal combat strength, an incompatible winner gets at most four units and a defeated project gets at most two from an own-prioritizing concave survivor, so mean combat output is at most three. Jensen places its original combat utility below or at retention. After calibration the total material available to combat is at most 2.7, below retained stock three; the productive current base exceeds (1+lambda)f_gamma(3), whereas every combat allocation has base at most (1+lambda)f_gamma(2.7). After observation each holding exceeds 4/11. These checks connect the less-curved successful preference case to adoption and retained combat, rather than only comparing two exogenous lotteries.

Greater curvature here means greater aversion to the particular material risk under the normalized shifted-power class. Insurance or diversification can change the lottery itself, as 048/053 show. Rejection of the risky batch predicts peaceful retention in this comparison; it is not a combat theorem or an estimate of how common these preferences are.
