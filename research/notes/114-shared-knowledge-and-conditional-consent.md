# Shared knowledge, reciprocal changes and conditional consent

R0006 working proof note. Originals maximize only their own final color.
This note compares a substitutable/additive knowledge benefit with note 113's
complementary investment response. It also constructs a staged launch under
an explicit, demanding public-certificate technology. The certificate and
offer protocol are assumptions to assess, not consequences of self-knowledge.

## 1. Additive spillovers create a reciprocal opportunity

Let efforts satisfy a sufficiently large finite bound and let physical final
counts be

`q_i = Q + a x_i + rho a x_j - (c/2)x_i^2 - K_i`,           (1)

where `a,c>0`, `0<=rho<=1`, and the initial work/material budgets keep every
specified output nonnegative. Research work and installation consume useful
work that could otherwise make clips; the shared knowledge increases work
recoverable/usable in production. The exact physical-accounting realization
and output bounds are supplied in note 115. Counts, work, energy and utility
are not identified merely because their numerical units are normalized.

Set `t=a/c`, `A=a^2/c`. Original-goal effort is `x_i=t`. A public genuine
goal `H_i=q_i+beta_i q_j`, with `beta_i>=0`, chooses

`x_i=t(1+rho beta_i)`.

Therefore the founder's output is

`q_i = q_F + A rho^2(beta_j-beta_i^2/2)-K_i`,
`q_F = Q+A(1/2+rho)`.                                    (2)

For `rho>0`, holding the partner's weight fixed, each original strictly
maximizes (2) by retaining beta_i=0 when installation expense is nonnegative.
The other agent's effort response to one's *effort* is zero in this family.
Thus independent public goal choices select retention. A sequential game in
which Blue chooses an unconditional weight and then original Red chooses its
own also selects retention by backward induction. This restriction has a
constructive repair below; it is not an obstruction to negotiated change.

If both instead install the same positive weight beta, each founder gains

`A rho^2(beta-beta^2/2)-K_i`.                              (3)

Before costs this is strictly positive for `0<beta<2`, uniquely maximal at
beta=1, and equal to `A rho^2/2` there. A rising shared-knowledge coefficient
rho increases this reciprocal opportunity quadratically. It does not create
the absent unilateral response in the preceding independent-choice game.
An enforceable effort agreement can realize the same physical improvement.

## 2. Negotiate a common goal, including asymmetric bargains

Let the agreed common criterion be

`W_z(q_B,q_R)=q_B+z q_R`, `z>0`.                           (4)

Blue expresses it with beta_B=z and Red with beta_R=1/z; these are positive
rescalings of the same *new* ordering. Both differ genuinely from their
original own-color preferences. With sufficiently large effort caps, its
unique physical maximum over the effort set occurs at

`x_B=t(1+rho z)`, `x_R=t(1+rho/z)`.                        (5)

Strict concavity of the weighted sum in both effort coordinates proves the
claim. With the specified private finishing lines, no extra allocation or
recoloring choice is hidden outside this effort set. If finishing control is
enlarged, the maximum must be recomputed.

The founders' net gains over the original continuation are

`D_B(z)=A rho^2(1/z-z^2/2)-K_B`,
`D_R(z)=A rho^2(z-1/(2z^2))-K_R`.                         (6)

At zero costs both strictly consent exactly when

`2^(-1/3) < z < 2^(1/3)`.                                (7)

Positive costs replace the two endpoints by the roots of the corresponding
equalities in (6). The Blue expression decreases strictly with z; the Red
expression increases strictly. Thus a nonempty interval of mutually
beneficial terms is an exact opportunity criterion. The effort caps and raw
material limits may further restrict this interval and must be intersected
with it. For equal expense K, the balanced choice z=1 works strictly iff
`K < A rho^2/2`; it maximizes the smaller of the two gross improvements.

If Blue has the offer right, Red's only responses are accept or reject, and
Red accepts at indifference, the best accepted z is the smallest feasible
root of `D_R(z)=0`, provided Blue's gain is positive. At zero costs this is
z=2^(-1/3); Blue obtains `3*2^(-5/3) A rho^2`, while Red ties its outside
continuation. Interior terms give both strict gains. Requiring strict
acceptance with a continuum of terms can leave only a supremum, rather than
a maximizing offer; a finite grid or an explicit tie rule resolves a
different, specified game. The division depends on bargaining rights, not
on a change in the originals' exclusive final values.

## 3. A sequential conditional-goal construction

Consider the following finite launch interface, with explicit offers and
accurate public semantic certificates for a specified installed goal:

1. Blue chooses terms z and pays its declared installation work. It installs
   a history-dependent criterion C_z. Red can inspect the actual criterion,
   rather than relying on Blue's promise about a private program.
2. Original Red can reject and take the specified original-goal continuation,
   or pay its work expense and install W_z. A valid certificate records that
   installation in publicly available history. A counterfeit or a different
   goal does not create that event.
3. After that event, each current agent chooses production and any later
   permitted revisions using its installed criterion. Attack remains a
   separate physical action and requires the continuation comparison below.

The first criterion is

`C_z(H) = W_z(q(H))` if the agreed valid Red certificate occurred,
`C_z(H) = q_B(H)` otherwise.                              (8)

This is a fixed utility function over terminal histories. The certificate's
occurrence changes which branch applies; no simultaneous rewrite of both
agents is required. It is nevertheless more expressive than an output-only
goal and requires secure, available historical evidence. Installing (8) is
a genuine change of the ordering over histories/lotteries, not merely a
different policy. Once the event has occurred, it stays in the history;
retaining the same code is not itself a terminal requirement.

**Conditional launch implication.** Suppose the offer/response protocol above
is the actual game; the installed goals are reliably recognized; (5) is a
feasible common maximum over the post-activation physical continuation,
including attack and revision outcomes; and (6) meets the originals'
participation conditions using their actual rejection continuations and all
costs. Then acceptance and execution of the common optimum is a sequentially
rational continuation. Blue chooses an accepted offer when it improves on
its best rejection/alternative option; Red consents using its original q_R.

After the certificate, both criteria order continuations by W_z. Its global
maximum rules out profitable rollback or changes of production policy within
that feasible set. Before the certificate, the original Red compares actual
q_R. Blue's current C_z values the proposed activation at W_z(q*), at least
q_B(q*) because q_R>=0. If the rejection continuation yields q_B no larger
than the accepted q_B(q*), Blue also prefers proceeding. These comparisons
prove the stated finite protocol; they do not assume the successor continues
to maximize the founder's q_B.

The opportunity calculation (6) used q_F as the rejection continuation. If
Blue has already sunk its installation cost on rejection, its actual
rejection output is lower and the root chosen by Red's participation still
uses Red's actual unaffected continuation. Compute Blue's initial decision
before paying that cost. No expense is refunded by verbal rejection.

There is a real scope limit. A richer response menu can allow Red to demand
new terms after Blue has installed (8); a protocol with such renegotiation
needs its own continuation analysis. Conditional-goal expressiveness does
not establish commitment to the original offer or free protection against
hold-up. Likewise, installing a false certificate or learning how to modify
oneself is not reliable semantic verification. These are candidate repair
technologies and unresolved implementation costs, not universal obstructions.

## 4. Ordinary alternatives and the physical peace condition

A fixed-utility pair with an actual conditional execution/effort controller
can implement (5). Give it the same communication, verification, energy,
execution and response opportunities as the goal-change route. At equal
cost, both can be optimal; a cheaper available controller displaces the
more expensive route. A revocable promise alone does not supply this control.
The benefit of genuine change in this construction is that, once activated,
executing the joint optimum serves each current preference even when later
revision is allowed within the same physical opportunity set.

Combat is not removed. To conclude peace, check the current criterion against
the actual stochastic recovery outputs at every nonterminal decision. A
strictly smaller attainable W_z after a destructive fight than at (5) is
sufficient after activation; the originals' earlier attack values must also
be below their offered own-color counts. Note 115 provides an explicit
finite-work, finite-recovery embedding. An increase in captureability or
better repair can change those bounds and the initial participation interval.

The physical overlap creates the productive opportunity in (3). The chosen
conditional goal and public inspection arrange the reciprocal response in
(8). This distinguishes a parameter effect from an available intervention
and from actual adoption under the finite offer protocol. Publicly certified
conditional preference installation is demanding. Additive shared knowledge
and positive production/communication expenses have simpler independent
motivations. Neither observation supports a population prevalence claim.
