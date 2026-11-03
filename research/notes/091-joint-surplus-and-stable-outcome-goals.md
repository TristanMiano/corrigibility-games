# Joint surplus bounds later goal changes

**R0004 derivation and constructive counterpart; analytical self-check.**
This moves beyond a finite list of threatening programs. The result is
local to a publicly known state with a physically protected receiver
fallback and a stated transfer/output law. Initial mutual agreement,
private information and long-run renewal remain distinct questions.

## 1. A bound covering arbitrary new successor criteria

Normalize the known low receiver target to 0. Its current loss is
Y^2-T+C_R, where T is payment from S and C_R>=0 is actual receiver
expense. Suppose it can secure expected loss at most e after any new
sender program or launch. This requires 082's *actual* protected output
and policy, not a merely announced fallback. The sender incumbent has
current loss (Y-a)^2+T+C_S, with C_S>=0 and 0<=a<=2. There is no new
production, third-party subsidy or hidden useful confiscation in the
remaining episode. The common transfer cancels in total loss.

A new effective authority costs the sender at least kappa in remaining
resources. Its successor criterion may be arbitrary; it need not be
quadratic, concave, peaceful or a familiar program. Because the receiver
chooses a continuation at least as good as its executable fallback,

\[
L_R\le e,\qquad
L_S+L_R\ge E[(Y-a)^2+Y^2]+\kappa
\ge a^2/2+\kappa.
\]

Therefore

\[
\boxed{L_S\ge a^2/2+\kappa-e.}
\tag{1}
\]

The last inequality uses (Y-a)^2+Y^2=2(Y-a/2)^2+a^2/2 and also covers
policy lotteries. Signed transfers are permitted; R's guaranteed loss
already bounds any subsidy. Combat and merger are covered if their
actual output/payments obey this law and the fallback remains executable.
Useful new output, a third party or loss of fallback authority changes
the premises.

If retaining the present goal gives incumbent loss a^2, as in the
surplus-extracting quote of 087, then

\[
\kappa>a^2/2+e
\quad\Longrightarrow\quad
\text{every such further authority change is strictly inferior.}
\tag{2}
\]

This is a substantive sufficient class of stability, not a permanent
ban on changing utility. For a=.19,kappa=.02,e=10^-6, the right side is
.018051. The price is much smaller than 084's original broad field-price
witness because the accommodated incumbent has little remaining joint
surplus to obtain. Choosing a goal closer to R and securing R's fallback
work together.

More generally, for current policy losses u(y),v(y), the bound is
L_S>=inf_y[u(y)+v(y)]+kappa-e. Compare it with the incumbent's actual
retention value. The finite output law and the guaranteed receiver
continuation do the work; the new program's announced intentions do not.

## 2. Concave replacement goals have a sharper quote bound

In the known-low, one-quote subgame, suppose every replacement goal is
X_S+v(y), with continuous concave v and v(0)=0, and the protected
receiver default costs zero. Let fees e_S,e_R be paid as in 080. At a
positive optimal quote, R charges min(B,v(y)-e_S). It chooses the
smallest policy yielding a budget-capped payment, so at a chosen quote
v(y)=t+e_S. Comparing its profit at y with a nearby lambda*y, lambda<1,
and using v(lambda*y)>=lambda v(y), gives

\[
v(y)\ge(1+\lambda)y^2,
\quad\text{hence}\quad v(y)\ge2y^2.
\]

The quote must remain feasible for nearby lambda; positive net quote
profit ensures this locally. If no profitable quote exists, the default
gives no improvement to the incumbent. Its improvement from any such
concave replacement is consequently at most

\[
2ay-y^2-v(y)-\kappa\le 2ay-3y^2-\kappa
\le a^2/3-\kappa.
\tag{3}
\]

This bound is attained by the simple linear goal v(y)=(2a/3)y,
which induces y=a/3, provided its payment 2a^2/9-e_S fits B and its
receiver profit a^2/9-e_S-e_R is positive. Thus 087's a^2/4 threshold
for equal-curvature target changes is too narrow for all concave goals.
At a=.28,kappa=.02 the linear replacement is beneficial. A=.24 makes
a^2/3<.02 and blocks this whole concave quote family, but (2) requires
a smaller a to cover arbitrary outcome criteria and credible threats.

The protected default is essential to the broad quantifier. Without it,
a very steep goal can make a launch credible and alter R's continuation;
one cannot keep using the old quote formula after that enlargement.

## 3. A deliberately chosen threshold can be both attractive and stable

The joint-surplus bound has a constructive near-attainment. Take a known
low founder with target a, a protected R default 0, and a genuinely new
achievement utility

\[
u_H=X_S+W\mathbf1\{y\ge q\},
\quad 0<q<1,
\quad W=q^2+e_S+e_R+\epsilon.
\tag{4}
\]

Suppose W-e_S<=B and epsilon>0. R's optimal positive quote is exactly
y=q, t=W-e_S: below q the successor has no willingness to pay, and
above q it has no additional willingness. R gains epsilon over its
default, and H accepts at indifference. The founder's loss is
(a-q)^2+W+kappa. Its improvement over retention loss a^2 is

\[
2aq-2q^2-e_S-e_R-\epsilon-\kappa.
\tag{5}
\]

For q=a/2 this approaches a^2/2-kappa, with explicit fees and positive
receiver participation. If cash prevents that q, a smaller funded q
still gives a strict successful region.

The successor also has a broad stability certificate. Express its
policy loss as u_H^{loss}(y)=W*1{y<q}. Its retained quote loss is W.
Because W>q^2, the minimum of u_H^{loss}(y)+y^2 is q^2. Applying the
general form of (1), any further effective authority has current loss
at least q^2+kappa-e. Hence

\[
\kappa>e_S+e_R+\epsilon+e
\quad\Longrightarrow\quad
\text{H strictly retains its goal against every such replacement.}
\tag{6}
\]

For a=1,q=.4,kappa=.02,e_S=e_R=.0001,epsilon=.001 and B=.1899,
W=.1612 and t=.1611 are funded. The founder's loss is .5412 rather
than 1; R voluntarily receives profit .001 at the quote; the successor
has less than .001201 available improvement if e=10^-6, far below .02.
This small threshold weight also makes the successor's own attack
inferior when the stated launch cost is 5. All alternative successor
criteria are covered by the actual fallback-and-resource bound, not by
that attack calculation alone.

This is an instrumentally attractive, stable genuine outcome goal in the
ordered goal-choice/quote subgame. Initial completion additionally needs
the stated absence of an intervening paid quote; 092 derives the ordinary
compromise repair when such a quote becomes available. No atomicity or
physical exclusion of earlier offers follows from these payoff formulas.
A protected fixed-utility delegate
with the same authority and price can tie it. Sender proposal rights
or a cheaper binding ordinary price commitment can supply the desired
trade without changing terminal utility. The ordered subgame establishes
unilateral initial adoption and subsequent voluntary compromise, not
mutual original-goal improvement before that unilateral move.

## 4. Transparent funded trade identifies where joint gains must come from

The last distinction matters. With known state, original S target a,
R target 0, no transaction costs, and 0<B<3a^2/4, the R-proposer
ordinary quote has y_B=a-sqrt(a^2-B)<a/2 and payment B. Original losses
are S=a^2 and R=y_B^2-B. This is already a constrained Pareto frontier.

To prove it for any policy lottery and payment T<=B, R's participation
requires E[Y^2]<=y_B^2. Moreover

\[
L_S\ge a^2-2aE[Y]+2E[Y^2]-(y_B^2-B).
\]

Use E[Y]<=sqrt(E[Y^2]). The resulting function is decreasing for
sqrt(E[Y^2])<=y_B<a/2, so its minimum is at y_B and equals a^2.
Any additional real goal-change expense raises the bound. Thus a costly
goal change cannot make both originals strictly better in this class.
Equal unavoidable transaction costs give the corresponding shifted
frontier; cheaper execution must be counted as a technology improvement.

For the actual fee-bearing a=1,B=.1899,e_S=e_R=.0001 fixture, even
generously eliminating all transaction fees in a new mechanism cannot
make a .02 goal update mutually beneficial. Original R participation
requires E[Y^2]<=.0101. The same calculation bounds new S loss from below by
1-2sqrt(.0101)+.0101+.1899+.02, which exceeds 1.019. This comparison
allows the small policy relaxation from saving R's quote fee, rather
than assuming every alternative must use an identical quote device.

Threshold adoption can nevertheless benefit S by reducing R's former
rent. Calling that a mutual gain would invert the result. In the main
private-information game, costly verification, false claims and possible
combat supply additional avoidable losses; 083 and 086 derive packages
that improve both original agents against their actual disagreement.
Information benefits and feasible compensation, rather than preference
change by itself, distinguish those positive joint results from pure
redistribution in this transparent-state control.
