# Production uncertainty and public goal choice

R0006 mathematical extension. This keeps linear exclusive own-color
originals and a complementary production mechanism, but lets productive
returns be uncertain when a goal is chosen. It is a comparison of specified
information structures, not a claim that overlap uniquely determines risk.

## 1. Timing and physical assumptions

Use

`q_i=Q+a_i x_i+b x_i x_j-(c/2)x_i^2`,                    (1)

where `0<s=b/c<=1/4`. The bounded nonnegative pair (a_B,a_R) is drawn after
public goal weights beta_i in [0,1] are installed. Both realizations are
then observed by both agents before simultaneous effort. Originals know the
distribution, not its future realization. They maximize E q_i when choosing
the goal `q_i+beta_i q_j`. There is no intrinsic value for the other color
in either original and no risk aversion in this comparison.

Assume an exchangeable joint distribution, positive second moment, and
finite physical work/material bounds covering all realizations. Put

`t_i=a_i/c`, `m_2=E[t_i^2]>0`,
`chi=E[t_B t_R]/m_2 in [0,1]`.

The chi bound follows from nonnegativity and Cauchy–Schwarz with equal
second moments. Zero productivity realizations are permitted; the exact
effort formula remains valid and nonnegative there. A strictly positive
lower support bound can instead ensure interior efforts. The retained
combat bounds must hold over the entire support if used to embed this
productive subgame. Initial update cost is zero for the exact equilibrium;
a positive expense needs the finite ex ante gain comparison.

## 2. Exact best response under the prior

Let `k_i=1+beta_i`, `k_j=1+beta_j`. In a realized state,

`x_i=(t_i+s k_i t_j)/(1-s^2 k_i k_j)`.                   (2)

Write `q=s k_j` in the following best-response formula (this q is a scalar
response coefficient, not a clip count):

`h_chi(beta_j)`
` =q[chi(1+s q)+q+s]`
`   /[1+q^2-s q+chi(2q-s q^2)]`.                        (3)

Derivation: `dx_i/d beta_i=s x_j/(1-s^2 k_i k_j)`.
The founder's derivative therefore has the sign of
`-beta_i E[x_j^2]+s k_j E[x_i x_j]`. Use
`x_i=t_i+s k_i x_j`,
`E[x_j^2]=m_2(1+q^2+2q chi)/(1-s q k_i)^2`, and
`E[t_i x_j]=m_2(chi+q)/(1-s q k_i)`.
After multiplication by positive denominators the derivative is linear
in beta_i, with positive intercept and negative slope, and its root is (3).
The denominator in (3) is positive. The root lies strictly in (0,1), so
it is the global best response over the actual menu.

To verify the last bound and comparative statics, differentiating (3) in
chi gives the positive numerator

`q(1-q^2)(1-2s q)`                                      (4)

over the squared denominator. Thus (3) increases with chi, and at chi=1
equals the earlier best response `q(1+s)/[1+q(1-s)]<1`.

The derivative in q has numerator

`(chi+s)+2(1+s chi)q+(chi-2s+3s chi^2)q^2`,              (5)

which is positive for the stated domain. For a simple global contraction
bound, its derivative in beta_j is no greater than
`s(1+4s^2+5s)<=5/8`: the denominator is at least one,
its derivative in q is nonnegative, and the numerator's derivative is at
most `1+4s^2+5s` on `q in [s,2s]`, chi in [0,1].
Hence the public goal game has a unique equilibrium, symmetric by
exchangeability, solving `beta=h_chi(beta)`.

## 3. Greater shared variation raises the chosen weight in this class

The unique equilibrium weight increases strictly with chi. One proof uses
(4) and the contraction fixed point: the derivative is
`(partial h/partial chi)/(1-partial h/partial beta_j)>0`.
At chi=1 it is `s/(1-s)`. At chi=0 it is lower but positive; for s=1/4
it is the unique root in (0,1) of

`beta^3+13 beta-2=0`.

This compares productivity co-movement while keeping the marginal physical
technology and information timing fixed. For independent identical draws,
chi equals squared mean divided by second moment; greater idiosyncratic
variance at fixed positive mean lowers it. Perfectly shared productivity
variation has chi=1. A common upstream technology may affect this
co-movement, but it can also affect failure rates, available work and
captureability; those joint changes require their actual comparison.

Both originals gain in expectation relative to retaining beta=0. Along a
common weight beta, each effort increases, while the derivative of total
output with respect to x_i is `(1-beta)b x_j>=0`. Total output therefore
increases toward the common optimum as beta rises from zero to one.
Exchangeability makes each expected own-color gain half that total gain,
strictly positive when productive interaction has positive probability.
This is an ex ante expected-output result, not statewise Pareto dominance.

The mechanism has a close strategic-delegation precedent in the basic
framework of Fershtman–Judd (note 118); its specific corrected oligopoly
theorems are not imported. A matched observed controller with the same
state-contingent effort authority reproduces (2)–(3). Private unobserved
productivity, unverifiable weights, nonlinear original risk preferences
and newly available renegotiation are separate environments. A consensual
common-goal package can still improve further, with its actual costs and
selection obligations, rather than treating independent weight choice as
the entire agreement space.
