# Outcome thresholds can make threats credible without valuing combat

**R0004 derivation; analytical self-check.** This supplies a simpler
outcome-based utility for the threatening-controller construction. The
earlier history-penalty controller is retained as one explicit mechanism,
but a preference for violence itself is unnecessary in this class.

## 1. Which outcomes make combat attractive?

At a known low state let a receiver victory implement a, a sender victory
implement 1, and the sender win with probability s. Write the sender's
current utility as X_S+V(y), and let effective combat destruction be d_S.
Against a sure offer y, the exact condition for preferring combat is

\[
sV(1)+(1-s)V(a)-V(y)>d_S.
\tag{1}
\]

The reverse weak inequality makes the sure offer at least as attractive.
It compares valued outcomes, strength and recoverable physical expense;
it includes no separate reward for violence.

For increasing concave V, an offer at or above the contest's mean policy
mu=s+(1-s)a is strictly preferable to combat with d_S>0. Jensen's
inequality gives V(y)>=V(mu)>=sV(1)+(1-s)V(a). For the original quadratic
V(y)=-(y-b)^2, b>=1, combat is preferred precisely when

\[
(\mu-y)(2b-\mu-y)>d_S+s(1-s)(1-a)^2.
\tag{2}
\]

The last term is the cost of policy risk for this concave goal. A larger
b favors combat when the offered policy is below the contest mean;
offers above that mean remain preferable. These are conditional value
comparisons, not claims about the frequency of war after bargaining.

Now use the simple achievement preference

\[
V_z(y)=W\,\mathbf1\{y\ge z\},\qquad a<z<1.
\]

If sW>d_S, the sender strictly attacks every effective offer below z
and strictly accepts every offer at least z. It values completion of
a threshold project sufficiently strongly relative to its own material
loss. Above the threshold it is indifferent among policies, so choosing
1 after winning is optimal. This is a nonconcave outcome goal, not a
history-dependent penalty for failing to shoot.

## 2. An original quadratic agent can choose this goal instrumentally

In 082's one-frame example, a=.3,s=.05,d_S=5,z=.48. Choose W=120.
Then sW-d_S=1>0. The current threshold successor therefore supplies
exactly the effective threat used in the unprotected construction.
R's concession loss is (.48-.3)^2=.0324, below contest loss .0345.
The original low quadratic sender pays .025 for the genuine update
because the induced concession improves its old loss by .1946 net.

The preference change is genuine over physical lotteries: the original
sender prefers accepting a to a contest costing 5, whereas the threshold
successor strictly prefers that contest to an effective offer a. Its
decision is evaluated by the original criterion before activation and
by the achievement criterion afterwards. A sender can therefore value
an ordinary smooth policy objective now and choose a sharp successor
objective to influence another agent's later choice.

The unprotected backward induction is unchanged: admitting this cheap
late threat makes the receiver prefer preemptive contest screening,
with the same actual war frequency approximately .0457173. The new
goal is off path in that selected assessment; its credible continuation
changes the earlier incentive to check. A costly protected commitment
to the same response could have the same effect if actually available.

## 3. A causal safeguard changes the outcome incentive itself

If 082's prepared exit secures policy a and the valued stock before a
launched attack can affect them, attacking after a subthreshold dispatch
can no longer achieve the threshold. It only consumes sender resources.
The achievement successor therefore accepts even that unfavorable
completed exit. Unlike the earlier history-penalty goal, it has no
reason to fire an ineffective shot.

At an ordinary offer a, a subsequent launch would induce R's cheaper
exit rather than a contest. Thus R can offer a, the threshold successor
accepts, and the original sender declines to pay .025 for a goal that
would obtain no concession. The peaceful staged C continuation returns.
The same initial private safeguard-purchase bound in 082 applies because
the on-path original welfare before and after protection is unchanged.
Actual attack choices remain in the game, including the response after
a launch; the changed incentives explain their nonuse.

The guard kernel charges a finite sender launch expense even when R
escapes. This must be actual consumed/dispersed output, not damage
silently attributed to an opponent who never fought. It is a separate
conditional physical law from 076's clash-recovery calibration. Any
positive unavoidable launch expense suffices for the strict refusal
to fire an ineffective shot; the numerical checker retains 5.

The achievement preference is easy to describe, but its weight W=120,
threshold z and reliable recognition are still chosen model parameters.
This gives a concrete value class and an incentive boundary. It does
not establish how common such priorities or such hardware are among
capable agents.
