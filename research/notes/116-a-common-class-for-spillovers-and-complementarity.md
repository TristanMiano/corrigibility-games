# A common class for knowledge spillovers and productive responses

R0006 derivation consolidating notes 113–114. This is a defensible smooth
two-factory class, not a claim that all process overlap has one scalar
meaning. It allows helpful knowledge, complementary integration and
congestion/substitution while keeping original final goals disjoint.

## 1. Definitions and the feasible parameter region

Let

`q_i=Q+a x_i+rho a x_j+b x_i x_j-(c/2)x_i^2-K_i`,          (1)

where `a,c>0`, `s=b/c in (-1/2,1/2)`, `rho in [0,1]`, and outputs are
physical own-color counts. The energy/material realization is as in note
115; negative b additionally represents interference in harvesting or use
of shared equipment. For s<0, choose the effort bound
`E=t(1+rho)` with `t=a/c`; then `a+b x_j>0` throughout the effort set, so
the recoverable-work increment remains nonnegative. For s>=0 choose
`E>=t(1+rho)/(1-2s)`. Supply finite initial work, raw material and throughput
for those ranges. A binding cap is a different piece of the model.

Public successor weights are `H_i=q_i+beta_i q_j`, `0<=beta_i<=1`.
Originals choose these using q_i. Put

`k_i=1+beta_i`, `u_i=1+rho beta_i`,
`A=a^2/c`, `ell=rho(1-s)+s`.

Post-installation effort responses and their unique solution are

`x_i=t u_i+s k_i x_j`,
`x_i=t(u_i+s k_i u_j)/(1-s^2 k_i k_j)`.                   (2)

The response-map contraction constant is at most `2|s|<1`. Positivity of
the numerator follows at the four beta-menu corners and hence everywhere
(it is bilinear). The stated caps include every response/equilibrium in
this menu. This supplies a full effort continuation for every goal profile.

The scalar ell is the net production externality at the original effort
equilibrium. It is not the fraction of common process steps. In fact

`x_F=t/(1-s)`,
`q_i,j at (x_F,x_F)=a ell/(1-s)`.                         (3)

Positive ell means the other's extra effort helps one's output; negative
ell means interference dominates the knowledge benefit. The sign of s
separately determines whether one's extra effort raises or lowers the
other's best-response effort. These are different causal questions.

## 2. Exact independent-adoption classification

At an arbitrary goal profile, direct differentiation of (2) gives

`d x_i/d beta_i = t ell(1+s k_j)/(1-s^2 k_i k_j)^2`,
`q_j,i = a ell(1+s k_j)/(1-s^2 k_i k_j)`,
`q_i,j = a ell(1+s k_i)/(1-s^2 k_i k_j)`.                 (4)

Since original output satisfies

`d q_i/d beta_i = [-beta_i q_j,i+s k_j q_i,j]`
`                  * d x_i/d beta_i`,                   (5)

its sign, when ell is nonzero, is the sign of

`N(beta_i)=s k_j(1+s)-beta_i[1+s k_j(1-s)]`.              (6)

All omitted factors in this sign comparison are positive; in particular
the two factors ell multiply to ell squared. This also checks the local
implicit-function result in note 113.

For `0<s<1/2`, the best weight is precisely

`h(beta_j)=s k_j(1+s)/[1+s k_j(1-s)]`.                    (7)

It lies in (0,1). Remarkably, rho cancels: additive spillovers change the
benefit of the response, but not this family's best strategic weight.
The contraction argument from note 113 gives the unique zero-cost goal
equilibrium `beta_*=s/(1-s)`.

For `-1/2<s<0`, N is strictly negative on the whole interval [0,1]. To see
this even when its slope changes sign, inspect its endpoints:

`N(0)=s k_j(1+s)<0`, `N(1)=2s^2 k_j-1<0`.

Linearity gives the interior result. Thus every original strictly prefers
retaining beta_i=0 against every partner weight, when ell is nonzero and
adoption costs are nonnegative. For s=0, (6) is -beta_i, giving the same
strict preference over every positive weight when rho>0. When ell=0 the
goal weights do not change the equilibrium efforts or original output;
positive installation expense selects retention, while zero expense permits
indifference. These are restricted independent-choice conclusions, with a
successful reciprocal-agreement counterpart in the next section.

No intrinsic concern for the other color is assumed in any original. The
same disjoint final objectives produce different adoption incentives because
of the other factory's productive response.

## 3. Reciprocal common goals improve the joint productive continuation

The original symmetric continuation and the common total-count maximum are

`x_F=t/(1-s)`, `x_eff=t(1+rho)/(1-2s)`.

The total-count objective is strictly concave in the two effort coordinates:
its Hessian has eigenvalues `-c+2b` and `-c-2b`, both negative in this class.
Thus its unique joint maximum is the stated symmetric effort. Each original
has the same per-agent gain, before costs,

`Delta_eff=A ell^2/[2(1-2s)(1-s)^2]`.                    (8)

Proof: along symmetric efforts, own output is
`Q+a(1+rho)x-c(1/2-s)x^2`, whose unique maximum is x_eff.
The gain equals `c(1/2-s)(x_eff-x_F)^2`; substituting
`x_eff-x_F=t ell/[(1-2s)(1-s)]` proves (8).

Consequently a reciprocal common-goal package with each actual expense
below (8) improves both founders whenever ell is nonzero. For ell>0 it
raises productive effort; for ell<0 it reduces mutually costly interference.
At ell=0 the original effort is already the joint optimum. Installation,
proposal, certificate and current-goal continuation obligations are those
in notes 114–115, not consequences of the opportunity inequality alone.
An actual enforceable ordinary effort agreement attains the same improvement.

For s>0 the independently chosen goals give

`x_*=t(1-s+rho s)/(1-2s)`
`   = x_F+s(x_eff-x_F)`,
`Delta_*=s(2-s) Delta_eff`.                              (9)

Thus independent preference changes close exactly a fraction s of the
effort gap to the common optimum in this family. Reciprocal agreement can
improve beyond them. For s<=0, reciprocal agreement can realize (8) even
though independent positive goal choices retain the original objectives.
This is an integrated comparison of implementation environments, not a
count of disconnected positive and negative examples.

## 4. Update costs and the scope of the comparative statics

For s>0, the gross benefit of the best individual update against partner k
is

`g(k)=A k^2 s^2(1+s)^2 ell^2`
`     /[2(1-2ks^2)(1-ks^2)^2]`.                          (10)

One way to verify this is to write original output, after substituting the
partner's response, as a strictly concave quadratic in x_i. Its maximizer
differs from the effort induced by retention by

`t k s(1+s)ell/[(1-2ks^2)(1-ks^2)]`.

Completing the square gives (10). Therefore the fixed-cost classification
of note 113 carries over with

`g_0=A s^2 ell^2/[2(1-2s^2)(1-s)^2]`,
`g_*=A(1-s^2)s^2 ell^2`
`     /[2(1-2s)(1-s-s^2)^2]`.                            (11)

There is unique pure mutual adoption below g_0, coexistence of mutual
adoption and mutual retention between g_0 and g_*, and unique pure mutual
retention above g_*. Boundary ties and mixed strategies retain the scope
specified in note 113. Conditional adoption uses (7). With s>0 and rho>=0,
raising rho increases ell, (8) and both thresholds. Raising s also raises
them on this positive domain: ell increases since `d ell/ds=1-rho>=0`,
and each other positive factor in the unsimplified formula (10), evaluated
at k=1 or k=1/(1-s), increases as the positive denominators shrink.

For s<0, raising rho can first reduce the common-goal gain by offsetting
congestion, reaching zero at `rho=-s/(1-s)`, and then increase it by creating
a positive spillover. Ordinary output can improve while the extra benefit
from modifying goals shrinks. Outcome measures must therefore separate
absolute paperclip production, the gain from agreement, and adoption of a
particular goal-changing mechanism.

The class leaves several parameters free rather than identifying overlap
with s or rho. A path adding a compatible interface may raise s and cost
resources; publicizing a design may raise rho for competitors as well as
partners; sharing a single machine may make s negative through congestion.
Feasible, chosen interventions require their actual actor, cost, timing,
information, alternatives and responses. Naturalness or population frequency
cannot be read off the size of a sampled parameter region.
