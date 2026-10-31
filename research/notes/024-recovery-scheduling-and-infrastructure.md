# R0001 working note: recovery scheduling and damaged production capacity

This audit corrects a physical interpretation in the initial reference models. The six-term formula in note 010 remains an exact solution of its written aggregate LP. It is **not**, in general, the attainable frontier of a literal serial recovery/production line when k is a physical production rate. The missing coupling also affected one E1.0 fixture. The correction below preserves the old mathematical result and states the changed execution model explicitly. Proofs are AI self-checked only.

## 1. The omitted time coupling

Use note 010's usable stock O, dispersed stock D, work reserve B, deadline T, production work c>0 and nominal production time tau>0 per unit, recovery work w>=0 and recovery time rho>=0 per unit. Write rho here to avoid confusing recovery time with other notes' dimensionless W/P ratio. Infrastructure limits production to k units per time.

For a serial line, the actual production duration per unit is

$$a=\max\{\tau,1/k\}\quad(k>0).$$

Recovering x units and producing y units therefore takes rho x+a y time, not merely max(rho x+tau y,y/k). The latter is the time condition implicit in the old aggregate LP.

For O=0,D=1,B=2,T=1,c=tau=w=rho=1,k=1/2, that LP permits x=y=1/2. Literal serial execution takes 1/2+1=3/2 time units. The actual maximum is y=1/3. This is a counterexample to the old *serial-rate interpretation*, not to its LP vertex calculation.

If k>=1/tau, the nominal production time already dominates the capacity limit and no correction is needed. This includes the k=tau=1 physical witnesses used in E2-U and notes 012, 016 and 020. Their stated numerical frontiers do not change from this audit.

## 2. Exact corrected serial frontier

For k=0 define output to be zero. For k>0, choose x,y satisfying

$$0\leq x\leq D,\quad 0\leq y\leq O+x,$$
$$cy+wx\leq B,\qquad ay+\rho x\leq T.$$

The least necessary recovery for a given output is x=(y-O)_+. Nonnegative costs make that choice weakly best. Recover those units first, then produce the output; both operations fit the explicitly additive time budget. Hence

$$\boxed{Y_{\rm serial}=\min\left\{
O+D,\frac Bc,\frac{B+wO}{c+w},\frac Ta,
\frac{T+\rho O}{a+\rho}\right\}.}$$

The proof is the same positive-part decomposition used for the aggregate LP, now with the physically effective production time a. Both the resource inequalities and an actual serial schedule are supplied. Material after the schedule is O+x-y usable, D-x dispersed and y delivered; work withdrawals and elapsed time are separate ledgers.

Relative to the old six-term formula, the missing bound when k<1/tau is

$$y\leq\frac{T+\rho O}{1/k+\rho}.$$

Keeping both old time bounds and adding this one is equivalent to replacing tau by a. Note 010's concavity, dispersion-loss and zero-loss derivations apply to this serial model with beta=rho/(a+rho), not the uncorrected rho/(tau+rho).

## 3. The aggregate overestimate is bounded, but can be substantial

Let Y_agg denote the old LP frontier and Y_serial the corrected one with all other quantities matched. Then

$$Y_{\rm serial}\leq Y_{\rm agg}\leq2Y_{\rm serial}.$$

Only the second inequality needs proof. If a=tau the values coincide. Otherwise an aggregate-feasible pair has ay<=T and rho x+tau y<=T. Thus ay+rho x<=2T. Halving both x and y gives a serial-feasible pair: its material constraint holds because y/2<=O+x/2, its stock bounds and work use shrink, and its serial time is at most T. For positive output and tau>0 the time inequality is strictly below 2T, although the factor two is a sharp supremum over parameters.

For sharpness take O=0, abundant D and work, tau=1, a=n+1, rho=n, T=1. The aggregate and serial outputs are respectively 1/(n+1) and 1/(2n+1). Their ratio tends to two. This bound concerns this one omitted coupling; arbitrary incorrect scheduling abstractions need not have a factor-two guarantee.

## 4. A different physical technology: independent parallel lines

Now give recovery and production independent machines. Production rate is kappa=min(k,1/tau)>0. The recovery line releases usable material at rate nu>0 after a fixed startup/transport latency L>=0, up to its stock D. Recovery and production may overlap, recovered material can be buffered, and processing is divisible with zero per-item handoff delay. The latency is paid only when recovery is used. A positive batch size or an additional processing latency is a different technology.

The production line begins with O usable units. Recover only R=(y-O)_+ units for a desired total y. If R>0, the earliest possible completion time is

$$t_*(y)=\max\{y/\kappa,\ L+R/\min(\kappa,\nu)\}.$$

Necessity follows from total production capacity, recovery supply, and the fact that at most O output can be produced before recovered material becomes available. For sufficiency, start the recovery line immediately and run production whenever material is available. If nu<=kappa, completion is limited by either total production time or the last recovered unit; if nu>=kappa, any initial idle gap lasts at most (L-O/kappa)_+, after which production runs at kappa. These two cases give exactly the displayed maximum. If R=0, recovery is unused and completion takes y/kappa, without a spurious latency charge.

Assume the same work costs cy+wR, with a stored budget available from the start and no extra unmodeled startup cost. The exact parallel frontier is

$$\boxed{Y_{\rm parallel}=\min\left\{
O+D,\ \kappa T,\ O+\min(\kappa,\nu)(T-L)_+,\
\frac Bc,\frac{B+wO}{c+w}\right\}.}$$

The formula handles T<L by permitting only the initial stock. An incapable recovery line is the nu=0 limit, which permits no recovered output; an instantaneous supply after latency is the nu tending to infinity limit. kappa=0 gives zero output. These cases concern production/recovery capability, not combat strength.

For O=0,D=1, ample work, kappa=1,nu=2,L=0,T=1, parallel processing delivers one unit. A serial line with the same per-unit production/recovery durations delivers only 2/3. With L>0, the parallel result becomes min(1,1-L); merely listing per-unit costs would miss this startup loss.

## 5. Two damaged material classes require a joint resource condition

Let two recoverable stocks D_1,D_2 have work costs w_1,w_2 and serial recovery times rho_1,rho_2. Nominal and infrastructure production time combine into a as in section 1. A schedule is feasible exactly when

$$0\leq x_j\leq D_j,\quad y\leq O+x_1+x_2,$$
$$cy+w_1x_1+w_2x_2\leq B,\qquad
ay+\rho_1x_1+\rho_2x_2\leq T.$$

Again choose total recovery R=(y-O)_+. When y<=O, the direct production bounds suffice. For positive R, an optimal material choice may trade work against time: minimizing work and minimizing time separately need not select the same mixture.

Define the single-resource frontier function for base cost q>0, budget H, recovery costs v_1,v_2 and stocks D_1,D_2 by ordering v_l<=v_h and setting

$$\Phi(H,q;v,D)=\min\left\{
\frac Hq,\frac{H+v_l O}{q+v_l},
\frac{H+v_h O+(v_h-v_l)D_l}{q+v_h}\right\}.$$

These are the three linear pieces of minimum recovery cost: no recovery, the cheaper stock, and additional use of the expensive stock. The common total-material bound is imposed separately.

If one stock is weakly cheaper in both work and time, recover it first; the two one-resource feasibility conditions and total stock bound are jointly sufficient. If the rankings cross, relabel so w_1>w_2 and rho_1<rho_2. Put

$$\lambda=\rho_2-\rho_1>0,\qquad
\mu=w_1-w_2>0,\qquad
v=\lambda w_1+\mu\rho_1
=\lambda w_2+\mu\rho_2.$$

Then the exact frontier is

$$\boxed{Y=\min\left\{
O+D_1+D_2,\ \Phi(B,c;w,D),\ \Phi(T,a;\rho,D),
\frac{\lambda B+\mu T+vO}{\lambda c+\mu a+v}
\right\}.}$$

Omit the last term when the rankings do not cross. The weights lambda,mu are dual conversion coefficients with the units needed to add the two constraints; they are not an identification of time with work or utility.

### Constructive proof of the extra condition

For fixed y>O and R=y-O, x_1 must lie in [max(0,R-D_2),min(D_1,R)]. The work constraint supplies the upper bound

$$x_1\leq\frac{B-cy-w_2R}{\mu},$$

and time supplies the lower bound

$$x_1\geq\frac{\rho_2R-T+ay}{\lambda}.$$

Each one-resource frontier says that its bound intersects the stock interval. The only remaining condition is that the time lower bound not exceed the work upper bound. Cross-multiplication yields

$$ (\lambda c+\mu a)y+vR\leq\lambda B+\mu T,$$

which is precisely the added bound. The intersection then supplies an actual recovery mixture, followed by serial production. For y<=O the weighted inequality is implied by cy<=B and ay<=T, so it imposes no false restriction on direct production. Zero cost differences use the noncrossing case and require no division by zero.

## 6. Separate work and time optima can overstate attainable recovery

Take O=0,D_1=D_2=1,c=a=1,B=T=3, with (w_1,rho_1)=(3,1) and (w_2,rho_2)=(1,3). Each separate resource calculation permits y=5/4. But work would require x_1<=1/4, while time would require x_1>=1. The joint schedule is impossible.

The added dual weights are lambda=mu=2 and v=8, yielding Y=1. Recovering 1/2 unit from each stock and producing one unit uses exactly three work units and three time units. This demonstrates a physical interaction between work and delay that is lost by separately optimizing each resource and taking the smaller output.

The distinction is relevant when combat transforms material into different damaged states, not just when it changes the total dispersed amount. It does not identify any of these engineering coordinates with thermodynamic or Shannon entropy.

## 7. Uncertainty must preserve the feasible-state calculation

At fixed cost/rate coefficients, the serial frontiers above are minima of affine functions of material stocks, B and T. They are therefore concave in those state variables. For an uncertain state Z observed before production,

$$E[Y(Z)]\leq Y(E[Z]).$$

Using the expected physical state can overestimate even the expected maximum output. With one usable unit, no recovery needed, sufficient time, c=1 and work B equal to 0 or 2 with equal probabilities, E[Y]=1/2 while Y(E[B])=1. This is uncertainty about actual available work, not a confusion between knowing a stochastic law and its realization.

Do not extend this Jensen statement to arbitrary random rate coefficients or products kT without a new joint-concavity proof. Nor does an expected scalar output suffice for a nonlinear successor objective; its lottery over actual worlds still matters.

## 8. Correcting the E1 execution fixture

E1.0 described recovery and production on one serial line, but allowed (x_D+x_Z+v)/4<=1 together with v<=k. After its first combat, k=3. The documented Work(1,0,3,0) used 1/4+3/3=5/4 hours, so it did not fit its one-hour slot under the literal rate interpretation.

E1.1 uses

$$ (x_D+x_Z)/4+v/k\leq1,$$

where the reachable capacities satisfy 1<=k<=4. The corrected recovery fixture is Work(1,0,2,0): it takes 11/12 hour and leaves (O,D,Z)=(2,5,3), B=18 and deliveries (2,0). The old fixture is retained here as a rejected case. Before damage, k=4 and the action condition is unchanged. Pure-production Execute still requires v<=k.

C01's conservation substitution remains valid for both versions; only the action's time feasibility and the affected trace change. No E1 equilibrium had been claimed. E2's k=tau=1 witnesses are unaffected. The minimal contract still permits aggregate relaxations, serial lines, parallel lines and other physical technologies when their interpretation and attainable schedules are stated accurately.

## 9. Using these frontiers in the strategic model

Each frontier is conditional on fixed control and the declared production technology. Assign communication, verification, installation, combat, infrastructure damage and recovery their own state transitions before substituting route outputs into bargaining or goal-adoption inequalities. A larger static opportunity set does not prove that opponents permit its execution.

During an interrupted recovery/production path, retain already delivered quantities, unfinished material and remaining work/time. State whether delivered projects survive a later attack; do not silently erase them or count them twice. Parallel operations also require a rule for what work is canceled or retained when an attack interrupts both machines. These are dynamic-game parameters, not consequences of the static frontier formula.
