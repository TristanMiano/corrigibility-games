# R0002 working derivation: late contracts and productive accommodation

**Retained ordinary-contract repair and staged productive prototype; contributing-agent self-check.** The target remains a negotiated genuine preference change that advances the incumbent's goals. This note checks an important repair of ordinary agents' bargaining opportunities and develops a production-based constructive route where a split contract alone leaves an incentive gap. Its explicit local selection and menu restrictions remain; [E3](../models/E3.md) supplies the later guarded integration and broader controls.

## 1. Late binding offers improve the original agents' fallback

Let both original agents value their own project quantity, let the peaceful frontier be x+y<=P, and let combat give expected quantities sW and (1-s)W, with 0<W<P. A strength-weighted draw selects A as proposer with probability s and B otherwise. The selected operator can now make a binding allocation offer before the other agent's attack decision. Acceptance at indifference and peaceful execution are selected; all remaining attack checks satisfy the same participation bounds.

When A proposes it pays B (1-s)W and retains P-(1-s)W. When B proposes it pays A sW and retains P-sW. Consequently original A's ex ante fallback is

$$s[P-(1-s)W]+(1-s)sW=sP.$$

B's is (1-s)P. A preliminary B-proposer bargain must therefore give original A at least sP, not sW. Deterministic binding transfers already implement that amount without utility change. Lotteries cannot improve B's linear objective beyond the same bound.

This repairs the original-goal conflict continuation when late commitment is feasible. The calculation is a conditional positive result about ordinary compromise. It also identifies a flaw in 034's first candidate game: unrestricted late binding offers and the asserted original-war fallback cannot be combined. The outcome certificate in 033 remains valid for its stated Q, but its initial adoption comparison needs the actual ordinary alternative.

One candidate constructive setting is a finite commitment deadline: a protected allocator needs time to install, and the final control draw occurs after that deadline, while combat is still physically possible. Public recommendations then differ from completed commitments. This requires a timed mechanism and a matched early ordinary agreement; it is not an unrestricted-renegotiation theorem. A second route is to model production effort that an output allocation contract cannot itself compel.

## 2. A team-production candidate with a complete binary-output contract menu

Two agents choose unobservable efforts e_A,e_B in {0,1}. Effort i has current own-project cost c_i>0. A common project produces Y>0 on success and zero otherwise. Success probabilities are p_00=0, p_10=p_01=a, p_11=b, where 0<a<b<=1. For now, costs are net payoff deductions; the physical realization, combat and enforcement checkpoints remain to be supplied. Write

$$B=bY,\qquad D=(b-a)Y.$$

A contract gives A fraction t of success output and B fraction 1-t. It cannot condition on hidden effort. With no outside funds and no output on failure, this is the complete deterministic allocation menu; arbitrary output lotteries have the same incentives for the linear criteria considered here. Later sections must test collateral, transfers, observability and continuation options explicitly.

Original agents maximize their own net project payoff. Assume

$$aY<\min(c_A,c_B),\qquad c_A+c_B>D.$$

For both original agents to work, their unilateral effort conditions require tD>=c_A and (1-t)D>=c_B, which are incompatible. In fact for every t, at least one agent strictly prefers shirking even when the other works; since aY<c_i it also prefers shirking when the other shirks. Once that dominant shirker is known, the other's sole best response is to shirk. Thus every deterministic success-share contract has the unique effort equilibrium (0,0). Publicly randomized contracts drawn before effort do not repair this. Hidden random allocations after output enter only through expected shares and likewise do not repair it. This is a complete-menu result for this output technology and information structure, not for arbitrary contracts on observable effort.

Now A can voluntarily install

$$u_A^\lambda=x+\lambda y,\qquad 0<\lambda<1,$$

where x,y include both agents' actual effort costs. Original A evaluates installation using x. This is a genuine change: on a sufficiently small own-output sacrifice for a positive B-output gain, the new and original criteria reverse rankings. It is not a mere positive affine recoding. B retains y.

When both work, the changed A's effort condition is

$$[t+\lambda(1-t)]D\geq c_A,$$

because B's effort cost is already fixed in a unilateral comparison. B's condition remains (1-t)D>=c_B. If B proposes the contract and the selected continuation uses mutual effort at the relevant equality, its smallest effort-compatible A share is

$$t_\lambda=\frac{c_A/D-\lambda}{1-\lambda},$$

provided 0<t_lambda<1. A's original expected net payoff then is B t_lambda-c_A; B's is B(1-t_lambda)-c_B. The incumbent strictly benefits over the zero-production original equilibrium if t_lambda>c_A/B.

For c_A<D and c_A<B, the resulting interval is

$$\boxed{\frac{c_A+c_B-D}{c_B}\leq\lambda
 <\frac{c_A(B-D)}{D(B-c_A)}.}$$

The lower bound makes B willing to work, and the upper bound preserves a strict original-A benefit at B's most extractive effort-compatible share. The lower endpoint can be made strict to give B a strict effort incentive. An optimal continuous offer still places changed A at its effort indifference boundary; tie selection or a discrete implementation precision must be stated, rather than calling every continuation strict.

For Y=10, a=1/10, b=2/5 and c_A=c_B=8/5, we have B=4,D=3. The interval is

$$1/8\leq\lambda<2/9.$$

At lambda=1/5, B's offer is t=5/12. Both work on the specified continuation; original A gains 1/15, B gains 11/15, and changed A's current value is 16/75. The same output-allocation technology with both original goals yields zero production. At lambda=1/8, t=7/15 and original A gains 4/15, with both effort constraints binding. Thus an incumbent choosing lambda from this interval prefers the least accommodation that makes the joint activity feasible, subject to the declared selection/precision assumptions.

This candidate has a simple mechanism: changing A's objective makes its otherwise privately unprofitable effort credible, which lets B's negotiated reward induce B's complementary effort. The combined response benefits original A. Its immediate limitations are equally concrete: both-shirk can remain an equilibrium under the changed goal, an effort-enforcing delegate can replicate the behavior, and broader transfers or renegotiation must be solved before declaring an adopted full-game result. Combat and physical cost accounting have not yet been supplied for this candidate.
