# Early accommodation improves the sender's bargaining position

**R0004 constructive enlargement; analytical self-check.** This tests a
specific restriction in 084: only the agreed pair has cheap early goal
recognition. Give the sender one cheap, publicly recognized pre-state
choice from a whole quadratic accommodation family instead. Derive the
new disagreement, then renegotiate the joint package against it. This
does not solve unrestricted two-sided goal choice or repeated cheap
reconfiguration; 087 tests the latter directly.

## 1. A unilateral early option with genuine preferences

The sender's original target is theta+1, the receiver's is theta,
theta is binary with high probability p, and y lies in [0,1]. Before
theta is drawn, S may spend k=.02 plus early setup .001 to install
U_z=X_S-(y-theta-z)^2, where 0<=z<=1/2. This is a genuine change of
lottery preferences. State messages after installation are cheap, and
the receiver observes the installed goal but not theta. The receiver
can offer a binding current-policy/cash exchange after a message.
The remaining sender budget is B=.1899; each successful quote has
expenses e_S=e_R=.0001. Attacks retain the stated finite damages.

In the truthful assessment, a low report gives R a known-low bargaining
problem. For z>.02 it offers

\[
y=z/2,\qquad t=3z^2/4-e_S.
\tag{1}
\]

The price is below B throughout this goal interval. S's installed
utility is indifferent between accepting and rejecting into policy 0:
(y-z)^2+t+e_S=z^2. R's profit is z^2/2-e_S-e_R>0. This quote globally
maximizes its profit: at any y, the largest accepted payment is
2zy-y^2-e_S, so net profit is 2zy-2y^2-e_S-e_R. The physical interval
and budget do not bind at y=z/2. For smaller z, foregoing the quote
is optimal when its net benefit is nonpositive.

After a truthful high report, policy 1 is already both parties' best
feasible policy, so there is no profitable positive-price concession.
A low sender comparing the two reports has current losses z^2 and
(1-z)^2. Truth is strict for z<1/2 and weak at z=1/2. A high sender
strictly prefers its truthful policy 1 to the low quote. A common
completely mixed sequence supplies the truthful limiting beliefs;
acceptance of the surplus-extracting quote is the stated tie-breaking
choice. Every attack is more costly than the available policy gain.

Crucially, the original sender's low-state loss at (1) is

\[
(1-z/2)^2+3z^2/4=1-z+z^2.
\]

The original sender therefore strictly prefers larger z on [0,1/2),
and chooses z=1/2 in this family. Its new disagreement loss and R's are

\[
S_{early}=1-(1-p)/4+.021,\qquad
R_{early}=-(1-p)(1/8-.0002)=-(1-p).1248.
\tag{2}
\]

S strictly improves on 080's old disagreement throughout p in [.45,.55].
The mechanism is a voluntary reduction in willingness to pay: R must
offer a larger policy concession to extract the installed successor's
smaller trade surplus. The founder values that concession enough to
pay for changing its preferences. It never needs an intrinsic reward
for corrigibility or violence.

This construction reaches a selected truthful equilibrium. At z=1/2
low truth is indifferent; selecting z just below 1/2 makes it strict
and preserves the substantive margins by continuity. If the finite
available bank has such a largest value, the initial choice is strict
within that bank. Arbitrary goals above this truth-preserving interval,
another receiver goal move, and cheaper future reconfiguration require
their own continuation analysis. They are not ruled out by calling
this equilibrium truthful.

## 2. A revised joint package beats stronger ordinary controls again

Use (2), not 080's former reservation values. Let h=1-p,
L=.1248, J=.011, rho=.0001, and retain B=.1899. Negotiate the
full-budget staged target

\[
a(p)^2=-L+\frac{B-J-\rho}{h},\qquad T=B.
\tag{3}
\]

On [.45,.55], .44<a<.53. The original R leading loss is
-hL-rho; its remaining information and mistaken-policy cost is less
than .000064. To verify that bound, use D> .2209,
mu_1<1/2209, m<=.55(.0001)2209/2208 and
F<=.55(1/2208)43/[3000(.2209)]. The multiplier 2a(1-a) is at most 1/2.
Thus R strictly accepts; S's loss is below its new early-change option.
The old-current utility distinction and non-atomic installation remain
those of 084 on the accepted branch.

Against ordinary controls allow every contest strength and P_max<=15,
so M<=16. Put beta=5/21, gamma=.01/21 and choose the valid multiplier

\[
\lambda(p)=\frac{h+p\beta}{h-p\gamma}.
\]

The supporting bound (4) of 085 gives

\[
S_{ordinary}\ge p+B+
\frac{h+p\beta}{h-p\gamma}\{h(1/2+L)-B\}.
\tag{4}
\]

The goal package has sender loss at most
p+B+h(1-a)^2+.021p+.001. The difference between (4) and this upper
bound is concave in p. To check the only less immediate term, write
q=1/2+L and t=1+gamma. The rational part is

\[
\frac{h+p\beta}{h-p\gamma}(hq-B)
=(hq-B)+(\beta+\gamma)\frac{p(q-B)-qp^2}{1-tp}.
\]

Its second derivative is nonpositive when B>q gamma/(1+gamma), which
holds here: polynomial division leaves a multiple of 1/(1-tp) with
negative numerator q gamma-B(1+gamma). The other nonlinear term is
2 sqrt(h[B-J-rho-hL]), a concave square root of a positive concave
quadratic. All remaining terms are affine. The minimum gap is therefore
at an endpoint. Rational square-root bounds give positive endpoint
margins (approximately .0054 and .0026 before rounding; use the exact
certificate rather than these display values). Rounding a down by at
most 10^-5 increases S's loss by at most .000011000055 and leaves
strict R participation intact. The uniform gap remains greater than
.0025.

There is an explicit strict-truth variant: let the early recognized bank
end at z=.499 instead of .5. Replace L by z^2/2-.0002=.1243005 and
S's early reservation by 1+(1-p)(z^2-z)+.021. The same concavity proof
applies; rational endpoint margins before rounding exceed .0054539
and .0024535. After rounding the uniform gap still exceeds .00244.
This removes the low-report indifference from the early continuation,
while keeping the stated scope of that early goal bank explicit.

At p=.5, the revised a is about .482494. Its original losses are about
.83502 and -.06245, compared with .896 and -.0624 under the unilateral
early-change option. The lower bound on accepted ordinary S loss is
about .84164. This is a second substantive repair: permitting an
attractive early preference change alters the bargaining problem, and
agents can negotiate a different shared target in response.

## 3. What this extension establishes

The positive result permits a continuum of early quadratic targets in
the derivation and a finite representation with strict margins. It
does not require the earlier blanket claim that every cheap unilateral
early update is unattractive. If this early branch is added to the
finite offer game as a priced disagreement continuation, 084's initial
proposal argument applies with the new reservation values and package.

The one-opportunity technology matters: a recognized module can be
configured and activated before the state draw, or reserved for the
agreed field route; further effective authorities retain their actual
remaining prices. A cheap reusable general-purpose compiler or several
cheap modules changes that premise. The next note constructs an actual
beneficial second update rather than presuming the first goal survives.
Two-sided cheap early choices, additional quote windows and continuing
resources remain unresolved. This repair is one larger agreement class,
not a proof covering every feasible innovation.
