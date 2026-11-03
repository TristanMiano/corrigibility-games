# Observable progress supports staged screening and genuine completion

**R0004 working mathematical note; contributing-agent self-check.** The
conditional game below replaces E4's three private installation steps with
observable, costly progress. It first solves the continuation. Initial
agreement over a changed receiver goal, the physical realization and enlarged
controller/transfer menus are separate obligations, not assumed consequences.

## 1. Goals and the finite interface

The original sender has utility X_S-(y-theta-b)^2, b>=1. The receiver's
current goal is X_R-(y-theta-a)^2, 0<=a<1. The case a=0 keeps the original
receiver goal of E4. A positive a describes an already adopted compromise;
its original-goal adoption must be checked separately. Nature's binary state
has P(theta=1)=p and is privately known to S. Policies include a and 1.

The sender can complete C_a, whose actual current utility is
X_S-(y-theta-a)^2. Its pre-change evaluator remains the original sender
until the final activation. Define

\[
D=(1-a)^2,\quad
g=(1-a)(2b-1-a),\quad h=(1-a)(2b+1-a).
\]

Here g is the low original sender's gain from policy 1 instead of a, and
h is the high original sender's corresponding gain. C_a strictly prefers
truth: its low-state loss from an H report is D, and its high-state gain
from H instead of L is 1-a^2. Refusal gives the low policy a.

There are N requested stages. A claim costs f. At receiver checkpoint i,
R can choose a policy, attack, or request stage i at actual output cost r_i.
Following a request, S can refuse, attack, or execute the next stage at
cost c_i. Before N this produces authenticated *progress*, not a claim that
the new goal is active. At N it activates C_a, which freely chooses a fresh
authenticated report, refusal or attack. A completed C_a report H leads
to 1 and L to a. Refusal ends the diagnostic and leads to a. Costs already
spent remain sunk. A wait that misses the frame supplies no progress.

R observes each completed frame, including progress or refusal. Within a
frame the response cannot be observed before its physical release time.
This last condition needs a causal communication mechanism: it is not
implied by private utility knowledge or a convention to ignore early signals.
In particular, exposing activation before a fresh report is a different
interface. Positive stage costs and public progress are allowed here;
free intermediate mimicry and synchronized costless low-type waiting across
all stages are unnecessary.

Combat is available at live decisions. It consumes the contest apparatus,
costs useful output d_S,d_R, and gives S control with probability s in (0,1).
The winner learns theta. An original S winner selects 1; a receiver or C_a
winner selects a when low and 1 when high. Take d_S>2b+1 to make voluntary
sender attacks inferior to every available peaceful policy, including after
activation. These are finite losses; a physical embedding must derive them.

Let e_0=f and e_i=c_i for 1<=i<N. Assume

\[
0<e_i<g,\qquad c_i>0,\qquad \sum_{i=1}^N c_i<h,
\qquad 0<r_i<D.
\tag{1}
\]

A matched truthful delegate can replace the final activation if it really
has the same protected state/report authority. Its final incremental cost
is compared with c_N; equal cost gives a tie, cheaper cost displaces C_a,
and dearer cost preserves strict final C_a adoption. Earlier shared work
must actually be reusable by that delegate for this particular comparison.

## 2. Peaceful staged assessment

Define, backwards,

\[
\mu_{N+1}=0,\qquad
\mu_i=\mu_{i+1}+(1-\mu_{i+1})r_i/D
      =1-\prod_{j=i}^N(1-r_j/D),
\tag{2}
\]

and let

\[
q_i=1-e_{i-1}/g,\quad
\alpha_0=\frac{p\mu_1}{(1-p)(1-\mu_1)},\quad
\alpha_i=\frac{\mu_{i+1}(1-\mu_i)}
 {\mu_i(1-\mu_{i+1})}\quad(1\le i<N).
\tag{3}
\]

Require mu_1<1-p. High S claims and completes each requested stage. Low S
claims with probability alpha_0; after request i<N it advances with
probability alpha_i and otherwise refuses. It refuses the last request.
R requests i with probability q_i and otherwise selects 1. A refusal is
low in the limiting assessment. Progress leads to the next checkpoint.

The unchecked policy 1 must be optimal at each mu_i. For a finite grid this
requires 1+a-mu_i >= (1+y_-)/2, where y_- is its largest element below 1.
For the entire policy interval it suffices that mu_1<=a. At a=0 this is the
finite-grid version; the continuous a=0 version needs the varying unchecked
policy analysis, not a substitution of 1 for its interior optimum.

Subtract the receiver's statewise unavoidable high loss a^2. At checkpoint
i, choosing 1 has excess loss mu_i D. Requesting the next stage costs r_i
and reaches the next checkpoint with probability

\[
P_i=1-\mu_i+\mu_i\alpha_i
   =\frac{1-\mu_i}{1-\mu_{i+1}}.
\]

Its excess loss is r_i+P_i mu_{i+1}D. Equation (2) makes this exactly
mu_i D. This proves receiver indifference *with the information actually
revealed by progress and refusal*. A partly paid, unobserved frame has a
smaller remaining request cost, so completing it weakly improves this
comparison, strictly when a positive part of r_i has already been spent.

The low sender's value at checkpoint i, relative to a, is
(1-q_i)g=e_{i-1}. After request i<N, advancing pays c_i=e_i to reach value
e_i and hence ties refusal. At the last request, completing a truthful
controller pays c_N and still produces a, so refusal is strictly better.
The initial low claim similarly pays f to reach value f. High S prefers
each requested continuation: its total remaining implementation expense is
at most sum c_i<h, while refusal sacrifices h. Its full conditional claim
expense is

\[
E=f+\sum_{i=1}^N c_i Q_i,\qquad Q_i=\prod_{j=1}^i q_j.
\tag{4}
\]

Since sum c_i<h and f=(1-q_1)g with g<h,
E <= (1-q_1)g+q_1 sum c_i<h. Thus high claiming is strict.
The active successor chooses truth under its own goal; the original sender
only evaluates the earlier adoption and its archived welfare.

At checkpoint i, combat has excess loss d_R+s mu_i D. Consequently all
checkpoints prefer the displayed peaceful mixture to combat whenever

\[
\boxed{D\left[1-\prod_{i=1}^N(1-r_i/D)\right]
       < \frac{d_R}{1-s}.}
\tag{5}
\]

This is a sufficient regime, subject to the initial choice and policy
conditions. The strongest combat comparison is at the first checkpoint.
Sender attacks remain available and are ruled out by their actual finite
loss. Initial R waiting must also beat its best uninformed policy and
immediate combat; see the excess-loss comparisons below.

All used progress and refusal information sets have Bayes beliefs fixed by
(3). A consistent finite assessment can make high false reports and other
high departures vanish faster than low off-path completion. In particular,
a low C_a completion followed by truthful L must dominate a high C_a's
trembling false L in the limiting L posterior. Merely saying "truthful
reports are believed" is insufficient. The complete tree and common-sequence audit are supplied in 077; the
continuous-policy and paid-quote enlargement is in 080. The larger
initial program interface is conditional on 084.

## 3. Welfare, initial choice and genuine preference change

The original sender's expected loss is

\[
L_S=(1-p)(b-a)^2+p b^2+p E.
\tag{6}
\]

Low indifference accounts for its costly false claims and partial progress;
those expenditures are not omitted. The current receiver's loss is

\[
L_{R_a}=p a^2+\frac{p D\mu_1}{1-\mu_1}.
\tag{7}
\]

Actual C_a adoption has probability p Q_N, and combat probability is zero
in this assessment. Early acceptance is peaceful without a goal change.
These are equilibrium frequencies in one game, not population prevalence.

For initial R waiting, subtract p a^2. Its best uninformed excess loss is

\[
B_0=\begin{cases}
p(1-p-a^2),&p+a\le1,\\
(1-p)D,&p+a\ge1.
\end{cases}
\]

Immediate combat has excess loss d_R+s(1-p)D. Require the excess term in
(7) to be smaller than both. A usable safe exit securing a at expense e
would instead cost e+p(1-a^2), and must also be compared.

C_a is a genuine expected-utility preference change when a<b. In the high
state take T=1+(a+b)/2, and compare sure y=1/2 with a lottery giving 1 with
probability (T-1/4)/(2T-1), otherwise 0. The new quadratic target 1+a
prefers the sure policy, while the old target 1+b prefers the lottery.
This is a preference reversal over a common lottery domain, not a change
of beliefs, code identity, or affine representation.

The original receiver's welfare when a>0 is **not** (7). It must be
computed from actual theta,y and expenditures using its archived target
theta. Agreement over a therefore needs the separate original-welfare
calculation; this continuation alone supplies no adoption claim for R_a.

## 4. Equal stages: a useful exact comparison

For a=0, let total sender implementation cost k<g and total receiver
request cost V<1 be split into N equal pieces. Then

\[
\mu_1=1-(1-V/N)^N,\quad
E_N=g-(g-f)(1-k/(Ng))^N,
\]

\[
P(C)=p(1-f/g)(1-k/(Ng))^{N-1},\quad
L_R=p\{(1-V/N)^{-N}-1\}.
\tag{8}
\]

Splitting an existing request into positive pieces reduces the effective
receiver expense in (5): x+y is replaced by x+y-xy/D. This can move a
near-boundary example from combat screening into peaceful staged screening.
For fixed k and feasible N, the high sender expense decreases as N grows,
since (1-k/(Ng))^N increases. This is the standard elementary monotonicity
of (1-K/N)^N for N>K, not a claim about arbitrary capability changes.

With b=1,a=0,p=1/2,f=.01,k=.45,V=.01,N=3,
q=(.99,.85,.85), E=.39201625 and P(C)=.3576375. The one-stage comparison
has E=.4555 and P(C)=.495. Public progress permits earlier compromise and
saves implementation expense while genuine completion remains positive.
The mathematical improvement assumes dividing the work adds no new setup
overhead; a physical implementation must charge such overhead explicitly.

## 5. Obligations carried forward

The full finite assessment is in 077, its combat regime and boundary
mixtures in 075, and the conditional funded initial wrapper in 084. The
physical instance in 076 supplies resource costs and observation timing;
074/079/083 test ordinary signals and capture, 080 actual cash, and 086
early preparation. Live reusable goal/safeguard choice and funded
renegotiation remain open in 088/092. Preserve the positive completion
region and equally identify the costs, information leaks or alternatives
that favor earlier fixed-goal compromise, retention or combat. None of the
displayed formulas establishes robustness to an unspecified physical
agreement space.
