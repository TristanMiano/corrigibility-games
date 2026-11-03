# Further accommodation and the price of preserving a bargain

**R0004 local derivation and repair test; analytical self-check.** This
tests whether 086's early successor would preserve its goal when another
cheap recognized update is available. It also derives how allocating
cash between initial payment and later trade changes the best bargain.
The results below do not supply a complete two-sided repeated-goal game.

## 1. A second accommodation can serve the successor's current goals

At a publicly known low state, let the sender's *current* quadratic
target be a, with 0<a<=1/2. R retains target 0 and the known-low
quote technology of 086. If S retains a, R extracts its entire trade
surplus and leaves it current loss a^2. Suppose S can instead spend
kappa>0 to install a publicly recognized target z, after which R
quotes y=z/2 and t=3z^2/4-e_S. Require the quote to be profitable,+funded and within the physical policy interval, as in 086.

Evaluated by the incumbent a, this change has loss

\[
(a-z/2)^2+3z^2/4+\kappa=a^2-az+z^2+\kappa.
\]

Its gain is az-z^2-kappa, maximized at z=a/2. Consequently

\[
\boxed{a^2>4\kappa\quad\Longrightarrow\quad
\text{a strictly beneficial further preference change to }a/2.}
\tag{1}
\]

When a^2<4kappa, every one-step update in this quote family is strictly
inferior. At equality the best update ties. These are statements about
the current successor, not an instruction to retain the founder's goal.
The mechanism again uses a smaller willingness to pay to obtain better
terms from the receiver. A matched delegate with the same public
authority and expense can reproduce it.

For a=.5,kappa=.02, the optimal z=.25 gives a strict current gain .0425.
The new .25 successor then has maximum further one-step gain
.25^2/4-.02<0, so this particular two-step path terminates voluntarily
within the same family. A truthful high sender already receives policy
1 and cannot gain from paying for a goal change. The low-only public
update can therefore consistently reveal the low state; it need not
assume that utility attestation itself reveals private information.

The founder's welfare changes differently. With z=.25 its low policy
and payment give original target-1 loss .8125, plus the new .02 expense,
whereas preserving .5 would give .75. The successor's beneficial update
therefore costs this founder .0825 at that history. This is an actual
failure of a particular preservation claim, coupled to an explicit
constructive preference change by the successor.

A founder can respond by choosing a more stable goal initially. For
example a=.28 has a^2/4=.0196<.02. Its known-low original loss is
1-.28+.28^2=.7984, and its quoted receiver loss is -.039. The same
one-step menu then gives every successor update a strict disadvantage.
Initial preference choice and later protection are joint design
variables. This establishes stability only against the specified
one-step quote/update family; new threats, altered material weights,
state-contingent goals or additional counterparties remain separate.

## 2. Dividing cash between initial agreement and later trade

The full-budget choice T=B is useful but can cease to be the best goal
package under a changed disagreement payoff. Let the receiver's installed
target be a and retain residual sender cash delta=B-T. In a known-low
quote define final policy q=a+x and assume the budget binds:

\[
\delta+e_S=2(1-a)x-x^2=(1-a)^2-(1-q)^2.
\tag{2}
\]

Let h=1-p, J the receiver's initial update/setup expense, and m+H_F its
remaining information/original-policy loss, where
H_F=2a(1-a-x)F. Original receiver loss is

\[
L_R=hq^2+p\delta-B+he_R+J+m+H_F.
\tag{3}
\]

The original sender's loss is
h(1-a)^2+p+B-delta+pE+e_S^{early}. Combining (2)--(3) gives the exact
total-loss identity

\[
\boxed{L_S+L_R=
1+J+e_S^{early}+h(e_S+e_R)
 +2h(q^2-q)+pE+m+H_F.}
\tag{4}
\]

No transfer disappears mysteriously: initial and late payments cancel
in the total, and both transaction expenses remain. The founder-optimal
low policy in the physical quadratic part is q=1/2. Holding the residual
information costs fixed, any feasible redistribution of initial and late
cash that moves q toward 1/2 reduces total original loss by
2h times the decrease in (q-1/2)^2. Actual choice must also account for
the induced changes in E,m,F and the current agents' continuation IC.

For a proposed reservation r and neglected *display-only* small
information terms, q=1/2 suggests
delta=[B-J+r-h(e_R+1/4)]/p and
a=1-sqrt(1/4+delta+e_S). These are candidate terms, not a proof of
participation after dropping the costs. Use (3) with the actual costs
to certify a proposal. Feasibility requires 0<=delta<=B, a<=q,
x<= (1-a)/2 and a valid staged assessment.

## 3. The open integrated question after these repairs

There are three supported constructive facts: a founder can choose a
genuine early accommodation to improve bargaining; a successor can
choose another genuine accommodation for its own current benefit; and
the founder can choose a target that resists that particular later move.
There is also a supported limitation: the one-opportunity payoff in
086 is not the payoff of a cheap reusable update technology.

The unresolved next link is to solve the joint initial offer and
continuation with a priced reusable goal/safeguard menu and actual cash
circulation. Search for mutually attractive stable packages and for
obstructions that persist after changing targets, payments, delegates
and safeguards. Neither the profitable second update nor the stable
.28 target alone decides that larger game, and neither establishes a
population frequency of accommodation or freezing.
