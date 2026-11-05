# Shared-process substitutability and chosen goals

R0006 second production family. This tests the strategic-accommodation
mechanism beyond the linear-quadratic cross term. The shared intermediate
is useful to both separate finishing lines; their originals still value
only their own final clips. The degree of complementarity of contributions
is distinct from the fraction of common steps in a manufacturing diagram.

## 1. A bounded common productive process

For r<=1 define the common usable-knowledge/process index

`F_r(x_B,x_R)=[(x_B^r+x_R^r)/2]^(1/r)` for r!=0,
`F_0(x_B,x_R)=sqrt(x_B x_R)`.

For r<=0 the continuous boundary value is zero if either contribution is
zero. As r tends to minus infinity it approaches min(x_B,x_R). At r=1
contributions are perfect substitutes. Throughout this class F_r(x,x)=x;
the balanced productivity scale is matched when r changes.

Actual final counts are

`q_i=Q+v F_r(x_B,x_R)-(c/2)x_i^2-K_i`,                  (1)

with v,c>0, x_i in [0,E], and E=v/c. Shared knowledge unlocks usable work
for each private finishing line; it does not duplicate the material or
energy needed for the clips. Finite initial reservoirs fund research and
installation, with Q large enough for all declared expenses. Since the
power mean is at most (x_B+x_R)/2, its useful-work benefit is bounded by
vE independently of r. Note 115's finite physical embedding applies.

The process is concave. To check directly, write F=x_R g(z), z=x_B/x_R,
where `g=[(1+z^r)/2]^(1/r)`. For positive efforts,

`g''=(r-1)g z^(r-2)/(1+z^r)^2 <=0`.

Its Hessian is a nonpositive multiple of the outer product (1,-z).
The continuous boundary extension preserves concavity. Each player's
own quadratic expense makes its effort objective strictly concave. At
x_i=E and x_j<=E, F_i<=1/2, so any goal weight below has nonpositive
marginal value of increasing effort beyond E. The finite cap includes
all relevant effort best responses.

## 2. Public goal weights and the positive production continuation

Let each original publicly choose `H_i=q_i+beta_i q_j`, 0<=beta_i<=1,
using its original q_i to evaluate that choice. Set k_i=1+beta_i in [1,2].
The subsequent effort first-order conditions are

`c x_i=k_i v F_i`.

Put d=2-r>0. In the positive effort equilibrium,

`z=x_B/x_R=(k_B/k_R)^(1/d)`,
`x_R=(k_R v/c) g(z)/(1+z^r)`, `x_B=z x_R`.              (2)

The derivative ratio F_B/F_R=z^(r-1) proves the first formula, and the
second follows from Red's condition. These determine a unique positive
effort equilibrium for every goal profile. For r=0 use g=sqrt(z) and
z^r=1; the same expressions have their continuous meanings.

At symmetric weights k, efforts equal k v/(2c). Original retention uses
x_F=v/(2c), with per-agent output `q_F=Q+3v^2/(8c)`. A common total goal
(both beta=1) gives x_C=v/c and `q_C=Q+v^2/(2c)-K_i`.
The per-agent gross reciprocal gain is therefore

`Delta_C=v^2/(8c)`,                                    (3)

independent of r at the matched balanced scale. The way agents can induce
the partner's response nevertheless varies with r.

## 3. Exact independent goal choice on that continuation

Fix k_j, write u=z^r, and substitute (2) into original output. Apart from
Q and the factor v^2/c, it is

`k_j [g/(1+u)]^2 [(1+u)-(k_j/2)z^2]`.                  (4)

Differentiating with respect to z, and using k_i=k_j z^d, shows that the
sign of the original goal-choice derivative is the sign of

`h(u)-k_i`, where `h(u)=d(1+u)/(1+d u)`.                (5)

There is one best response, with clipping to [1,2]. Here is a global check,
including negative r. The logarithmic elasticity of h is

`u h'(u)/h(u)=-(d-1)u/[(1+u)(1+d u)]`,

whose absolute value is less than one. Since u=(k_i/k_j)^(r/d), for r<0
the product of that elasticity and r/d is positive but less than one
(|r|<d). For 0<=r<1 it is nonpositive. Therefore k_i/h(u) increases
strictly with k_i, so (5) changes sign at most once. At k_i=1 the
derivative is positive for r<1; at the upper cap the constrained optimum
can occur when contributions are very complementary.

At an interior mutual optimum,

`k_i/k_j=h(u)/h(1/u)=(d+u)/(1+d u)`.                    (6)

It also equals u^(d/r) when r!=0. For 0<r<1 these sides move in opposite
directions from u=1. For r<0 the logarithmic slope magnitude of the right
side is at most (d-1)/(d+1)<1, while |d/r|>1. Hence again equality holds
only at u=1. An asymmetric upper-bound equilibrium is also excluded:
if k_i=2>k_j then its upper-bound optimality requires
`k_i/k_j<=h(u)/h(1/u)`, whereas the same slope comparison gives the
strict opposite inequality. Both at 2 are not optimal since h(1)<2.
Neither can be at 1 for r<1. For r=0, (5) directly gives h=4/3.

Thus the unique pure zero-cost goal equilibrium **on the selected positive
effort continuation** is

`beta_*=(1-r)/(3-r)`,
`x_*=(v/c)(2-r)/(3-r)`.                                (7)

For r=1, beta_*=0. As r decreases, the chosen positive other-color weight
increases toward one. Each original's gain at (7) is

`Delta_*=v^2/(8c)[1-4/(3-r)^2]`.                        (8)

This is positive for every finite r<1 and rises toward the full reciprocal
gain (3) as complementarity becomes stronger. The originals did not begin
with any value for the other color. Their changed goals affect the other
factory's productive response, which advances their own original output.
Both changes are voluntary public choices; this independent-choice result
is distinct from a jointly negotiated common-goal package.

A positive installation cost leaves the optimum *conditional on changing*
unchanged, but introduces the retain alternative. At the profile (7),
adoption remains a strict best response exactly when its actual gross
gain over setting k_i=1 with partner k_j=k_* exceeds K_i. Formula (4)
computes that finite gain; it is strictly positive for r<1. This gives
an open positive-cost adoption region. It is not a claim of uniqueness
of the fixed-cost goal game or of an uncomputed population adoption rate.

## 4. Coordination and the exact bottleneck endpoint

For 0<r<=1, producing alone has positive marginal benefit, so (0,0) is
not an effort equilibrium. At any other boundary an inactive producer
benefits by a small positive effort. Thus the positive continuation is
the unique effort equilibrium.

For r<=0, both contributions are essential and (0,0) is an additional
effort equilibrium for every goal profile. The positive equilibrium still
exists and can be selected, but (7) must not be reported as selection-free.
If zero effort is instead selected for every profile, positive-cost goal
installation serving only this task is displaced. A startup agreement or
a different order of productive moves is a relevant repair, analyzed below.

The literal min endpoint has additional equilibria. With
`F=min(x_B,x_R)`, original effort best responses are
`x_i=min{x_j,v/c}`. Every equal-effort pair in [0,v/c] is a Nash
equilibrium, including the efficient x=v/c. Common-goal responses are
`x_i=min{x_j,2v/c}` before the physical cap; with the matched cap E=v/c,
the same entire interval remains. Enlarging the cap to 2v/c would add
inefficient overinvestment equilibria under the common goal. Thus ordinary
coordination can already reach the joint optimum at the exact bottleneck.
The finite-r strategic-weight limit is not a uniqueness theorem at r=-infinity.

This is a concrete explanation for inspecting actual process structure.
Smooth complementarities create a useful marginal response to a changed
objective. A rigid shared bottleneck can instead make the main problem
selection among mutually compatible effort levels. Nearly identical
upstream work does not identify which technology applies.

## 5. A timed production repair with a matched ordinary benchmark

Allow Blue to choose its actual effort first and Red to observe it before
choosing its own. When both have the common total goal, backward induction
selects the unique joint maximum x_C: Blue can choose that effort and
Red's unique best response completes it; every other achievable outcome
has a smaller common value. This removes the zero-effort equilibrium
without removing zero effort from the action set. It requires observable,
durable first effort, with all startup work funded and attack still tested.

The originals receive the same move order. In the Cobb-Douglas case r=0,
Red's original response is `x_R=(v/(2c))^(2/3)x_B^(1/3)`. Maximizing
Blue's original output along that response gives

`x_B=(v/(2c))(4/3)^(3/4)`,
`x_R=(v/(2c))(4/3)^(1/4)`.

Their original surpluses over Q are respectively
`2v^2/(3 sqrt(3)c)` and `sqrt(3)v^2/(4c)`. Both are strictly below the
common-goal surplus v^2/(2c). Hence equal update costs satisfying

`K < (2-sqrt(3))v^2/(4c)`                               (9)

leave both originals strictly better off under the negotiated common
goal, with a unique sequential productive continuation. Its initial
installation still requires an actual consent mechanism; a protected entry
and reservation of note 128 is one candidate when available. This is a
successful timing repair with the ordinary timing advantage included.
Other r values require recomputing each party's sequential outside value;
the symmetric simultaneous baseline cannot be reused automatically.

The finite common maximum also rules out profitable later goal changes
within this production set. Actual binding ordinary controllers can achieve
the same production; relative costs and availability determine which route
is selected. The mathematical mechanism is robust across a range of smooth
productive processes. Reliable public goals, startup coordination and
protected staged implementation remain separate naturality and design
questions, rather than consequences of the amount of shared manufacturing.
