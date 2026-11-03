# Ordering work can improve the founder's compromise

**R0004 derivation; analytical self-check.** This studies a design choice
inside the same public-progress class. Permuting stages is allowed only
when actual engineering dependencies, work, timing and setup expense
permit it. It is not a claim that every installation can be reordered.

## 1. Sender work and receiver checking have different best orders

Take the peaceful full-budget assessment, b=1, 0<a<1, g=D=(1-a)^2,
and every sender installment c_i<g. Keep f fixed. With e_0=f and
e_i=c_i for i<N, define hazards x_i=e_{i-1}/g and suffix odds
w_i=mu_i/(1-mu_i). They satisfy w_1>...>w_N>0. Then

\[
F/p=\sum_{i=1}^N\left[\prod_{j<i}(1-x_j)\right]x_iw_i.
\tag{1}
\]

Swapping adjacent hazards x,y changes their contribution by
Q(x-y)(w_i-w_{i+1}), with Q the unchanged earlier survival product.
The later survival product is unchanged. Thus smaller hazards first
minimize F. Increasing any one hazard also increases F: it replaces
some later stopping value, at most w_i, by w_i now. Consequently the
minimum puts the largest sender installment last, where it causes no
unchecked-stop hazard, and orders the remaining installments increasingly.

The sender's original expense E is invariant under these permutations:
E=g[1-(1-f/g) product_i(1-c_i/g)]. Current receiver loss m is also
unchanged. The original receiver's extra term 2a(1-a)F falls. Putting
the largest installment last also maximizes actual C probability,
p(1-f/g) product_{i<N}(1-c_i/g). This is a joint improvement in founder
receiver welfare and literal C completion, with sender welfare unchanged,
within the stated feasible permutations.

For receiver request costs, mu_1 and m depend only on
product_i(1-r_i/D), hence not on order. Swapping adjacent r_i,r_{i+1}
changes only the suffix odds w_{i+1} in (1): placing the smaller cost
second lowers those odds. Thus larger receiver costs first minimize F.
These ordering results coexist: inexpensive sender progress first and
expensive receiver verification first serve different incentive roles.
Constant-damage peace/combat boundaries remain unchanged because their
first-stage product is unchanged. Changing the actual damage/clock law
can invalidate that last invariance and requires another comparison.

## 2. Balanced checking need not maximize original welfare after adoption

For two receiver stages, fix r_1+r_2=V<D and put r=r_2, x=f/D,
y=c_1/D and K=2a(1-a). Original receiver loss above its low-policy
baseline, divided by p, is

\[
J(r)=(D+Kx)\left\{\frac{D^2}{(D-V+r)(D-r)}-1\right\}
       +K(1-x)y\frac r{D-r}.
\tag{2}
\]

The first term is minimized at r=V/2. The second is strictly increasing.
Both are convex, and the first is strictly convex: its denominator is
the positive concave quadratic D(D-V)+Vr-r^2. Hence J has a unique
minimum on a closed feasible interval. With no positive hardware lower
bound on r, that minimum is below V/2 whenever K,y>0. It lies at zero
when

\[
\frac{K(1-x)y}{D}\ge
\frac{(D+Kx)V}{(D-V)^2},
\tag{3}
\]

and otherwise is the unique root J'(r)=0 in (0,V/2). With a positive
minimum stage expense, use the corresponding constrained endpoint.

Thus balancing verification expenses minimizes the *current* receiver's
information cost, while its original founder can prefer front-loading
verification to reduce mistaken concessions under the changed goal.
The leading gain in avoided mistaken policies can outweigh the smaller
increase in current checking cost. Neither welfare measure should be
silently substituted for the other.

This is an architecture-choice calculation, not a proof that the chosen
architecture persists. A successor able to rebalance the apparatus
cheaply may prefer its own cost minimum. Charge the actual rearrangement
cost or analyze that later choice. A physically completed arrangement
whose remaining redesign price exceeds the successor's possible saving
can preserve the founder's preferred order without forbidding updates.
