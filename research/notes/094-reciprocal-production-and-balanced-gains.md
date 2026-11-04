# Reciprocal production and a chosen preference for balanced gains

**R0005 local analytical construction.** The statements below are
local mathematical results; full initial negotiation, physical execution,
partner choice and the ordinary-control comparison require separate results.
The final [E6 account](../models/E6.md) maps the subsequent repairs and
remaining obligations; the last section records this note's intermediate agenda.
The candidate moves from private-state reporting to renewable reciprocal
production. No independent review or novelty claim is made. Fehr–Schmidt's
1999 model, pp. 821–824, was inspected: its standard alpha>=beta>=0,
beta<1 restriction is narrower than the full goal family used here. The
formula is conventional; later theorem proofs in that paper were not audited.

## 1. A finite reciprocal exchange

In one episode, two specialized producers can each supply b units of useful
output to the other at an own-project opportunity cost c, with b>c>0.
These are net project quantities, not conserved energy. The physical inputs,
conversion and available-work mechanism must be specified when implementing
this payoff subgame. Let v=b-c. In order, the first producer chooses C or D,
the second observes it and chooses C or D. The episode's net increments are

| First, second action | First producer | Second producer |
| --- | ---: | ---: |
| C,C | v | v |
| C,D | -c | b |
| D,C | b | -c |
| D,D | 0 | 0 |

Original preference F_i is own net project output. A proposed successor has
criterion

\[
G_i(x_i,x_j)=x_i-\alpha_i(x_j-x_i)_+
                 -\beta_i(x_i-x_j)_+,
\quad \alpha_i\ge0,\quad 0<\beta_i<1.
\tag{1}
\]

The first penalty is for being worse off in this collaboration, the second
for being better off. The subclass alpha_i>=beta_i is available; the local
proofs do not need that ordering. Outcomes and coefficients are defined in
the declared physical project-output scale. They are not sums of arbitrary
unnormalized representations of different agents' utilities.

**Proposition 1.** If beta_i>c/(b+c), a G second mover strictly reciprocates C
and strictly declines to supply after D. Against that second mover an F or G
first mover strictly chooses C. An F second mover strictly chooses D; an F
or G first mover then strictly chooses D.

**Proof.** After C, the G second mover's difference between C and D is

\[
v-[b-\beta_i(b+c)]=\beta_i(b+c)-c>0.
\]

After D, supplying gives -c-alpha_i(b+c)<0 against zero from D. Anticipating
reciprocation, either first mover receives v>0 from C and zero from D.
Against an F second mover, the first mover's C gives -c (F) or
-c-alpha_i(b+c) (G), whereas D gives zero. These strict comparisons determine
the unique backward-induction outcome in this action subgame. QED.

Thus a single genuinely changed second mover can enable a mutually beneficial
exchange, while two F agents have the D,D outcome in this subgame. The change
is genuine: the original second mover prefers (b,-c) to (v,v), whereas the
stated G ranks them oppositely. It is not a positive affine recoding or only
a different policy with the original preferences retained.

At equality beta_i=c/(b+c), reciprocation is an indifference selection.
Below it, this successor does not solve the last-move incentive. These are
preference thresholds, not facts about how frequently such agents occur.

The raw exchange has no binding transfer/delegation facility. Giving one to
the parties changes the comparison and must be priced rather than ignored.
In particular a credible performance bond of at least c can change the F
second mover's incentives. The availability, holding cost and finite funding
of that control are open implementation choices here.

## 2. Renewable episodes and the meaning of the goal

For finite episodes t=1,...,N, discount factor delta in (0,1], and realized
partner j(t), an initial candidate is the history criterion

\[
G_i(H)=W_i(H)-\sum_{t=1}^N\delta^{t-1}
\{\alpha_i[x_{j(t),t}-x_{it}]_+
 +\beta_i[x_{it}-x_{j(t),t}]_+\}.
\tag{2}
\]

W_i is actual discounted own-project welfare, including implementation and
other real expenses. The x's are the net gains of the declared physical
collaboration episode, including its within-episode transfers and expenses.
An episode with no collaboration has no pair-inequality term. This is a
preference concerning *collaborative gains*, not automatically a preference
for equality of lifetime wealth or of every person's holdings. Actual project
and partner identity must be recorded by the physical mechanism; merely
renaming a delivery cannot change the old evaluator's interpretation.

Installations are chosen under the incumbent criterion; after activation the
successor uses (2). A subsequent update does not erase an earlier evaluator's
dated interpretation of past episodes. A new partner changes the relevant
pair through the actual future matching process, not through an invisible
instruction to maximize the founder's welfare. Original W_i is separately
reported. The concrete timing and fee attribution of an implemented instance
must be explicit; (2) does not supply a costless semantic verifier.

If each episode is balanced and gives v, the continuation values of F and G
coincide at A_N v, where A_N=sum_{t=0}^{N-1}delta^t. A durable update cost can
therefore be amortized across genuine future production. This arithmetic
does not yet establish who will select that partner, whether others also
change, or whether a cheaper ordinary route replaces the update.

## 3. A protected original-welfare floor without a change penalty

The useful general form is G(H)=a W(H)-P(H), where a>0 and P>=0.
Let Q be a feasible continuation under the other parties' actual strategies.
At the current information set, subtract any common sunk contribution to P
and W. If the remaining P is nonnegative, E_Q P=0, and a deviation law L is
accepted under the current G, then

\[
a E_L W-E_L P\ge a E_Q W
\quad\Longrightarrow\quad E_L W\ge E_Q W.
\tag{3}
\]

This covers a proposed utility change by evaluating its *actual successor
continuation* with the old G. It does not force that successor to use W.
There is no penalty for changing code or preferences in this lemma.

If Q instead has expected remaining penalty e>=0, and current choice can
fall short by epsilon>=0 in G units, the bound is

\[
E_L W\ge E_Q W-(e+\epsilon)/a.
\tag{4}
\]

For (2), an executable continuation with balanced episode gains has zero
remaining penalty and yields (3). Unlike a cap on the other agent's possible
output, the pointwise inequality G<=W continues to hold when new productive
opportunities appear. The *availability and balance of Q* still need checking
after shocks, revised partners, entry fees or changed resource rights.

If Q also attains the largest achievable E W under the given opponent
strategies and feasible actions, then it maximizes current G. A positive-cost
replacement that cannot raise that maximum is strictly worse. Without this
extra maximality premise, the result is a welfare floor, not universal
retention or renegotiation-proofness. A better original-welfare opportunity
can support another consensual change.

## 4. Wealth-based fairness has a separate repair boundary

Suppose instead that (1) evaluates final stocks. Before the exchange let
d be the second mover's stock minus the first mover's stock, and put
phi(d)=alpha*(-d)_++beta*d_+. After the first mover supplies C, the second
mover's C-versus-D difference is

\[
\phi(d+b+c)-\phi(d)-c.
\tag{5}
\]

When beta(b+c)>c and alpha+beta>0, strictly supplying after C is equivalent to

\[
d>d_*:=\frac{c-\beta(b+c)}{\alpha+\beta}.
\tag{6}
\]

Indeed, for d>=0 the difference is beta(b+c)-c>0; for
d<=-(b+c) it is -alpha(b+c)-c<0; between them it is
(alpha+beta)d+beta(b+c)-c. The root d_* lies strictly between -(b+c) and 0.

A pre-exchange transfer z from the first mover to the second raises d by 2z.
There is also an upper boundary. After a first-mover D, supplying gives
the second mover the difference phi(d)-phi(d-b-c)-c over D. It is positive
exactly when

\[
d>d^*:=\frac{c+\alpha(b+c)}{\alpha+\beta}.
\tag{7}
\]

Thus the strict reciprocal response (supply after C, decline after D) holds
on the band d_*<d<d^*, whose width is exactly b+c. A sufficiently rich
second mover instead supplies even after D. An F first mover then chooses
D to obtain b without paying c. Checking only the response after C would
miss this exploitation of the wealth-sensitive goal.

The transfer repairs strict reciprocity when
(d_*-d)/2<z<(d^*-d)/2, subject to funding and full participation. It must
not overshoot into unconditional giving. If equal initial stocks
are followed by a second-mover installation expense kappa, compensation
z=kappa/2 restores equality of stocks after the expense. This is a candidate
cost-sharing repair, with strict original participation requiring the
future productive gains to cover each party's share and other expenses.
Transfer commitment, non-atomic installation and alternative contracts
must be checked before asserting actual adoption.

Equations (2) and (5) are distinct preference domains. A result for balanced
episode gains must not be attributed to absolute-wealth fairness. Both
give constructive regions and specific limiting conditions. Choosing the
goal's domain, changing the role assignment, or funding an equalizing
transfer are different possible repairs with different real requirements.

## 5. Integrated next obligations

Give renewal a physical resource law, keep finite combat actions at live
histories, and compare those returns with the balanced continuation. Add
voluntary partner choice and transfers, derive why a party would create
access or finance a genuine change, and test current-self revision. Compare
ordinary policies, priced bonds/escrow and matched delegates. Preserve the
positive reciprocation and floor results while seeking the resource,
matching and bargaining conditions that favor ordinary cooperation,
retention or combat instead. No population or full initial-game result
is claimed by this note alone.
