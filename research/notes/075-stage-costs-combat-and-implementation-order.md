# Stage costs, combat thresholds and implementation order

**R0004 continuation of 073; analytical self-check.** This note derives the
combat regime and the effects of changing implementation costs. It concerns
the specified staged interface; its causal kernel and complete assessment
are audited separately.

## 1. Backward screening threshold with combat retained

Use 073's D,g,h, costs c_i,r_i, entry prices e_0=f,e_i=c_i, and goals.
Let

\[
w=\frac{d_R}{1-s},\qquad A=d_S+(1-s)g.
\]

Assume 0<w<D, 0<r_i<D, 0<e_i<g and c_N<h. Define backwards

\[
T_{N+1}=0,\qquad
T_i=\min\{w,\ r_i+(1-r_i/D)T_{i+1}\},\qquad \mu_i=T_i/D.
\tag{1}
\]

The entry and progress probabilities are still Bayes' formulas (3) in 073.
When T_i=T_{i+1}, low advancement is one; when T_i>T_{i+1}, it is strictly
between zero and one. At N low refuses. At checkpoint i choose:

- if the second term of (1) is below w: request with q_i=1-e_{i-1}/g,
  otherwise select 1;
- if it is above w: contest with z_i=(g-e_{i-1})/A, otherwise select 1;
- at equality: any q_i,z_i>=0 satisfying q_i g+z_i A=g-e_{i-1}, with the
  remaining probability assigned to 1.

These mixtures are feasible because A>g when d_S>2b+1. The receiver's
excess loss from selecting 1 is T_i. A contest costs d_R+s T_i and ties
it exactly at T_i=w. A request followed by the Bayes-updated continuation
has excess loss

\[
r_i+\frac{1-\mu_i}{1-\mu_{i+1}}T_{i+1}.
\]

It ties T_i precisely when the second term of (1) is selected. Otherwise
it is more expensive. This proves the receiver comparisons at every stage,
including stages reached only after an off-path request in the combat regime.

The low sender's value at checkpoint i is

\[
(1-q_i-z_i)g+z_i(sg-d_S)
 =g-q_i g-z_i A=e_{i-1}.
\tag{2}
\]

A requested partial stage therefore ties refusal at its specified low
mixing probability. A requested final goal change is strictly worse for
low S than refusal. High continuation remains strict as proved next.

## 2. A weaker and more useful high-adoption condition

073 used sum c_i<h as a simple sufficient condition. It can be replaced
by c_N<h and 0<c_i<g for i<N. Let F_i be the high sender's expected expense
from carrying out a requested stage i, including the subsequent selected
continuation. At the last stage F_N=c_N<h. If stage i+1 uses a peaceful
mixture, then

\[
F_i=c_i+(1-c_i/g)F_{i+1}
    =(c_i/g)g+(1-c_i/g)F_{i+1}<h.
\]

If it uses combat screening, F_i=c_i+z_{i+1}d_S<g<h. For a boundary
mixture, substituting its indifference equation gives

\[
F_i=g+q_{i+1}(F_{i+1}-g)-z_{i+1}(1-s)g<h.
\]

Backward induction proves every requested high continuation worthwhile.
The same calculation with c_0=f proves high claiming worthwhile. This is
a current-self calculation of **remaining** expenses. A large accumulated
sunk cost is not a reason to quit an otherwise advantageous final update.

If the final cost reaches h, this strict-completion proof ends. That is a
boundary of this goal template, not a proof that every peaceful repair
fails: a different goal, truthful delegate or ordinary costly signal must
receive its actual price comparison.

## 3. Peace and combat on the selected path

Let

\[
V_{\rm eff}=D\left[1-\prod_{i=1}^N(1-r_i/D)\right].
\tag{3}
\]

If V_eff<w, every selected checkpoint is peaceful. If V_eff>w, the first
checkpoint strictly prefers combat screening to requesting the first stage,
so no stage is requested on path. This follows because any earlier positive
r_i propagates a capped suffix strictly above the cap before the minimum
is taken. At V_eff=w the first stage can mix checking and combat; later
stages have uncapped peaceful thresholds when all r_i>0.

Provided the initial wait and unchecked-policy conditions hold, the combat
regime has

\[
\mu_1=w/D,\quad z_1=(g-f)/A,\quad
L_S=(1-p)(b-a)^2+pb^2+p(f+z_1d_S),
\]

\[
L_{R_a}=pa^2+\frac{pw}{1-w/D},\qquad
P(W)=\frac{p z_1}{1-w/D},\qquad P(C_a)=0.
\tag{4}
\]

Here P(C_a) counts sender activation in this continuation. If a>0 was
installed in R earlier, that earlier change must still be reported.

For arbitrary boundary mixtures, set Q_0=1,Q_i=product_{j<=i}q_j. Then

\[
P(C_a)=p Q_N,\quad
P(W)=\sum_i\frac{p Q_{i-1}z_i}{1-\mu_i},\quad
E=f+\sum_i Q_{i-1}(q_i c_i+z_i d_S).
\tag{5}
\]

Low indifference supplies the same original-sender baseline plus pE.
Boundary selection is a genuine multiplicity, not a unique predicted jump.

## 4. Splitting costs and changing capability

Splitting one receiver request x+y into two positive requests x,y changes
its effective expense from x+y to x+y-xy/D. With the other stages fixed,
V_eff falls strictly. Subject to all the same policy, prior and physical
conditions, a split that crosses w replaces selected combat by peaceful
screening. This comparative change assumes no new per-stage overhead.

For a fixed number of stages and fixed total request expense, equal r_i
maximize product(1-r_i/D), hence minimize V_eff and the receiver's selected
loss. If each extra frame costs h_R>0, the equal-stage expression instead
uses r_i=V/N+h_R; indefinitely adding frames then drives V_eff toward D
and can restore combat or invalidate the mixed-entry region. Actual extra
communication and setup costs must therefore be charged.

Holding all request costs fixed, raising d_R or raising sender strength s
raises w and can turn combat screening into peaceful screening. Within
the strict combat region, however, each raises its selected combat rate:
raising d_R increases the false-claim posterior w/D, while raising s also
reduces A and increases the required contest probability z_1. Thus these
are conditional comparisons on either side of the boundary, not a single
monotone slogan about strength or damage.

Holding d_R,s fixed, increasing d_S leaves the boundary unchanged and
reduces z_1 and the combat rate, but raises z_1 d_S. Fewer clashes can thus
coexist with greater original high-sender expected damage. Report event
frequency and welfare separately.

## 5. Sender costs and the order of genuine completion

In the peaceful regime suppose all c_i<g. Telescoping (4) in 073 gives

\[
E=g-(g-f)\prod_{i=1}^N(1-c_i/g).
\tag{6}
\]

For fixed total sender implementation expense and fixed N, equal stages
minimize E by the arithmetic-geometric mean inequality. Reordering those
same expenses leaves E unchanged. Yet completion probability is

\[
P(C_a)=p(1-f/g)\prod_{i=1}^{N-1}(1-c_i/g),
\tag{7}
\]

so putting the largest expense last maximizes genuine completion, and
putting the smallest last minimizes it. With a=0 the original receiver
loss and sender loss are unchanged by this reordering, provided the
receiver request prices and all conditions are retained. For a>0, archived
receiver welfare additionally depends on false-positive frequency (074),
so invariance of its *current* loss must not be relabeled invariance of its
original welfare.

For b=1,a=0,p=.5,f=.01 and sender stages (.1,.35) or (.35,.1), both have
E=.42085. Their goal-change frequencies are respectively .4455 and .32175.
Both selected continuations are peaceful. Frequency of literal preference
change is therefore a distinct outcome from peaceful play and welfare.

An ordinary final burn with observable cost g can separate the types at
the last request: low is indifferent and can refuse, while high strictly
prefers burning to policy a. Replacing c_N by g makes (6) equal g exactly,
regardless of the preceding stages. If the genuine final update costs less
than g, it strictly lowers the high sender's cost in this matched control;
if it costs more, the available ordinary burn is cheaper. The burn and its
observation must really be available at those prices. Arbitrary richer
ordinary mechanisms receive the separate frontier audit in 074.

## 6. Completion obligations

Equations (1)-(7) supply local best-response and Bayes calculations. The
common completely mixed sequence and off-path audit are in 077, the
physical kernel in 076, and the priced agreement/control enlargements in
078–093. The broader reusable-goal and live-renegotiation game remains
open, preserving both achieved goal completion and ordinary/combat regions.
