# Costed combat information and renegotiated goals

**R0004 derivation and constructive repair; analytical self-check, with
exact arithmetic certificates.** This sharpens the ordinary control and
then repairs the first funded goal package against a substantially stronger
control. The conclusion concerns a finite resource and implementation
class, including initial proposal rights. It does not require that goal
change uniquely outperform a matched protected delegate.

## 1. A small chance of combat can replace an ordinary burn

Use the ordinary mechanism class of 079 with fixed original goals,
state probability p, sender bias b>=1, original receiver offset 0<=a_0<=1,
funded payments t_0,t_1<=B, and policy y in [0,1]. A contest costs the
sender d_S>0 and receiver d_R>0. S wins with probability s, chooses 1
under either state, and R wins otherwise and chooses min(theta+a_0,1).
Only a receiver victory provides protected evidence of the sender's
state to another authority. An independent protected state sensor or
delegate remains a separate technology.

Strength is public and independent of theta in this coupling. For a_0>0,
the specified receiver-win policy law matters: a stronger controller
permitted to punish a captured lie by choosing 0 instead of a_0 needs
the larger policy penalty (1-s)(2b-1). The main adopted-family result
has a_0=0 already, so it grants that full policy punishment.

For the moment there is no further state-dependent destruction. Put

\[
M=(1-s)(1-a_0)(2b-1-a_0).
\]

A low sender imitating the entire high strategy can differ from the high
report's low-evaluated policy payoff only on the receiver-win branch.
With high-report contest probability w_1, the IC expression d in 079
therefore satisfies d>=-M w_1. The actual high sender expense includes
d_S w_1, and the receiver expense includes d_R w_1.

For lambda>0 choose

\[
\eta=\min\left\{p,\frac{p(d_S+\lambda d_R)}{d_S+M}\right\},
\qquad \lambda\ge1+\eta/(1-p).
\tag{1}
\]

Then 079's offset bound remains valid with this stronger eta:

\[
L_S+\lambda L_{R_{a_0}}\ge
K=b^2+(2b-1)\eta+\lambda a_0^2
-\frac{[b(1-p+\eta)+\lambda a_0(1-p)]^2}
       {(1-p)(1+\lambda)+\eta}+(1-\lambda)B.
\tag{2}
\]

The additional proof step is

\[
(p-\eta)C_1+\lambda p V_1+\eta d
\ge[(p-\eta)d_S+\lambda p d_R-\eta M]w_1\ge0.
\]

Here C_1 includes actual sender costs and V_1 the receiver's additional
physical costs. No combat damage is omitted or treated as a transfer.

When lambda*d_R<M and the low minimizer

\[
x=\frac{b(1-p+\eta)+\lambda a_0(1-p)}
         {(1-p)(1+\lambda)+\eta}
\]

lies in [0,1] and the contest probability (3) is at most one, the bound
is attained by a generous binding mechanism:
both reports pay B; the low report gets policy x without combat; the
high report gets policy 1 except for a contest lottery of probability

\[
w=G_x/(d_S+M),\qquad G_x=(1-x)(2b-1-x).
\tag{3}
\]

The payments must actually be funded, and the stipulated destruction
must fit the remaining inventory. On a high state's contest both winners
still choose 1. A low imitator instead risks the receiver choosing a_0.
Low IC binds. High truth is strict for x<1 because
d_S w<=G_x<(1-x)(2b+1-x), its gain from reporting high. There is no
ordinary burn beyond the actual contest
damage. The original losses are

\[
L_S=(1-p)(b-x)^2+p b^2+p d_S G_x/(d_S+M)+B,
\]

\[
L_{R_{a_0}}=(1-p)(x-a_0)^2+p a_0^2+p d_R G_x/(d_S+M)-B.
\tag{4}
\]

The mechanism needs binding policy and launch authority. A receiver who
is free to cancel a costly audit after inferring that a high report is
truthful may cancel it; the attaining control is not asserted to be an
equilibrium of the uncommitted staged game. Giving the control this
authority without a setup charge is deliberately favorable to it.

At the same x an ordinary high-report burn costs G_x. Combat saves the
sender p*M*G_x/(d_S+M), while adding receiver loss p*d_R*G_x/(d_S+M).
The weighted boundary is exactly lambda*d_R=M. Above it, the burn is
preferred on this supporting frontier; at equality, mixtures attain
the same weighted loss. Lambda is a welfare-constraint multiplier, not
an extra term in either agent's actual utility.

For a fixed target x, a greater state-sensitive penalty M reduces the
required contest frequency. A larger d_S also reduces frequency but
increases the sender's expected destruction toward the burn cost. The
choice between mechanisms and the frequency within one mechanism are
different outcomes and can move differently.

## 2. Finite punishment capacity is a real enlargement

Now permit a preinstalled authority to destroy up to P_max additional units
of S's output after a receiver victory reveals a false high report.
Destruction is genuine material loss, including the available recovery;
it is not secretly counted as conserved-energy loss or receiver income.
The ordinary comparison may configure this contingency before the state
is learned. A truthful high report incurs no extra destruction.

The same coupling and proof apply with

\[
M=(1-s)\{(1-a_0)(2b-1-a_0)+P_{max}\}.
\tag{5}
\]

This is a bound over arbitrary finite communication, policy lotteries,
type-independent burns and funded payments in the stated capture law,
not just a search over a few threat templates. A transfer or confiscation
that raises the receiver's own output changes the payment/cost premises
and must be analyzed with its actual conversion and capacity. A sensor
that verifies state without this contest is also a different control.

The enlargement matters. At p=.5,b=1,a_0=0,B=.1899,d_S=5,d_R=.01,s=.05,
consider low policy .44, payments B in both states, and a high-report
contest probability .017. Configure an additional low-state destruction
of 14, and charge positive initial mechanism expenses .005 to S and .001
to R. Low truth is strict: the false-report penalty exceeds its policy
gain by 273/20000. High truth is also strict. The losses are

\[
L_S=4471/5000=.8942,\qquad L_R=-18403/200000=-.092015.
\tag{6}
\]

R accepts relative to 081's actual disagreement value, and this S loss
is smaller than that first package's .918744. Its actual contest rate
is .0085, and the extra false-report destruction occurs only off path.
Thus low actual violence can coexist with a large credible punishment.
The controller's authority and verification of captured state must be
real: an uncommitted receiver with a positive punishment expense would
otherwise prefer to spare those resources.

With 20 units of S's specialized output and at least 5 already lost in
a contest, P_max<=15 is a generous bound on all remaining destruction. The
14-unit construction fits even after the positive setup expense. Work,
fuel, targeting and recovery time must support the added destruction;
the finite horizon can make recovery too late, while a prepared trigger
uses finite available work. Merely assigning a large punishment number
without this inventory would not justify the comparison.

## 3. Renegotiating the goal repairs the displaced package

The successful response is to reconsider the bargain. Pay the full
available B before the state is known and negotiate a larger receiver
offset. The sender then has no residual transferable cash in the field:
this is the chosen use of a real budget, not an omitted trade action.
Disagreement still retains 080's actual late cash bargain.

For p=.5, choose a=.42, T=B=.1899, the same three positive C installments
and request expenses as 081, the same .01 receiver update, and the same
.001 early expense for each party. The staged continuation is peace,
with both agents evaluated at each decision by their actual current
goals. Original losses are

\[
L_S=23270576604997/26767049445000\approx .8693739911,
\]

\[
L_R=-19105241287623040090577/210762144090531330790000
\approx -.0906483532.
\tag{7}
\]

Here and below the ordinary receiver's original offset remains a_0=0;
a is the goal package's newly negotiated successor offset. Both originals
improve on disagreement. With P_max<=15 and lambda=8/5, the bound (2)
implies that every qualifying ordinary mechanism accepted by R leaves
S loss at least .880431786. The revised package therefore beats even
the stronger punishment control. Its advantage is not obtained by
removing that control after it displaced the first example.

The physical interface and non-atomic adoption conditions of 081 still
apply. A complete cheap, unrecognized-controller or unrestricted live-
cash implementation is not supplied by this resource-bound comparison.
Those are the next agreement-design link, not a reason to erase the
proved conditional opportunity.

## 4. A whole prior interval with a negotiated target

There is a uniform family, rather than just another single witness.
Let p range over [.45,.55], keep B=.1899 and total initial receiver
expense J=.011, and put rho=.0001 and ell_0=-.1798. Choose

\[
\boxed{a(p)^2=\ell_0+\frac{B-J-\rho}{1-p},\qquad T=B.}
\tag{8}
\]

Then .38<a(p)<.47. Receiver posteriors remain below a(p), so policy 1
is optimal even on the entire continuous policy interval. All update
costs are below the required current-goal continuation gains. For b=1,
g=D=(1-a)^2 and the sender's high implementation expense is at most
f+sum_i c_i=.021.

The original receiver loss is
(1-p)a^2+m+2a(1-a)F-B+J. Substitution of (8) gives
(1-p)ell_0-rho+m+2a(1-a)F. Uniformly, D>=.2809,
mu_1<=1/2809, and

\[
m\le .55(.0001)\,2809/2808,
\quad
F\le .55\,\frac{1}{2808}\frac{43}{3000(.2809)}.
\]

Consequently m+2a(1-a)F<.000061<rho. Actual disagreement is
(1-p)ell_0+p z_1^0 with z_1^0>0, so R strictly prefers every package
in the family. S's package loss is below .881 throughout the interval,
while its disagreement loss is greater than 1.

For the strong ordinary comparison, set P_max=15 in (5), lambda=8/5 and
eta=p(5+lambda*.01)/20.2. The payment and nonnegative-coefficient
conditions in (1) hold on the whole interval. Use the upper bound

\[
\overline L_S(p)=1+2B+.001-J-\rho+(1-p)\ell_0
-2\sqrt{(1-p)[B-J-\rho+(1-p)\ell_0]}+.021p.
\]

The gap K(p)-overline L_S(p)-lambda L_R^{out}(p) is concave in p:
the negative quadratic-over-linear term in K is concave; the displayed
positive square-root term in the gap is concave; all other terms are
affine. Its minimum on this interval is therefore at an endpoint.
Rational square-root enclosures give endpoint gaps greater than .0109
and .0080 respectively. Hence every p in [.45,.55] has a negotiated
goal package that strictly beats every accepted qualifying ordinary
mechanism, including finite state-dependent destruction up to P_max=15.

Exact irrational targets are unnecessary. Round a(p) down to the nearest
multiple of 10^-5. The receiver participation proof still holds because
its leading original policy loss falls and the same uniform cost bound
applies. The sender's policy loss rises by at most
1.1(10^-5)+.55(10^-5)^2, while the .021 expense bound is unchanged.
The uniform advantage therefore remains greater than .008. This uses a
finite, representable goal menu; the positive early expense includes its
calculation and communication in the specified implementation class.

This quantifier permits agents to change their proposed goal with the
known prior. It does not claim that one frozen goal works equally well
for every prior. Positive strict margins persist under sufficiently
small cost and preference perturbations. Larger seizable or destructible
stocks, stronger state sensors and cheaper delegates need their actual
new bounds; neither this interval nor an adverse example establishes
population prevalence.

## 5. Changing the proposer redistributes the gains

The positive comparison also has a receiver-proposer witness. At p=.5,
retain full payment T=B but choose a=.22. Then

\[
L_S=477630993101191/475030407735000\approx1.0054745661,
\]

\[
L_R=-7634391991072827540595843/49365727306329402625410000
\approx-.1546496407.
\]

S strictly accepts relative to its actual disagreement loss. Using
lambda=16/5 and P_max<=15 in (2), every qualifying ordinary contract
acceptable to S leaves R loss at least -.149686386. R therefore also
has a strict incentive to propose a genuine goal package in this
allocation of proposal rights. A best proposal may use still better
terms; these witnesses establish the existence of a strictly preferred
goal option over the entire stated ordinary comparison class.

Under either proposer, a matched protected delegate can tie genuine
change at equal cost, and a cheaper one can displace it. The positive
conclusion is voluntary, current-goal-optimal accommodation in a
specified agreement class, not unique implementation, universal
cooperation, or long-run evolutionary selection.
