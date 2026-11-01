# R0002 working derivation: insurance protects a risk-averse founder

**Insured certificate and local bargaining prototype; contributing-agent self-check.** This extends the efficient-fallback idea from a linear founder to a broad class of original project preferences. The key constructive repair is to combine a chosen productive goal with insurance. The limiting question is whether the insurance is feasible and whether its installation and bargaining terms are actually chosen. Note 042 proves the strict ordinary gap suggested below; 048/049/056 supply the final guarded extension registered as R206. The two-round protocol here retains its explicit unfinished implementation obligations.

## 1. Founder utility plus physical total output

Let original A have a continuous, strictly increasing, concave utility f(X) over its own final project output. B values Y linearly. Let T=X+Y be actual total project output, distinct from energy and utility. A can install

$$U_\eta(X,Y)=f(X)+\eta T,\qquad \eta>0.$$

This is a genuine preference change: original A is indifferent to B output at fixed X, while the successor strictly prefers more B output. At a fixed total it still ranks outcomes by original f(X). A current pre-change self evaluates installing U_eta using f; later decisions use U_eta.

If all feasible continuations obey E T<=S and a credible fallback Q has X=q surely and E_Q T=S, then every continuation accepted by this current successor satisfies

$$E U_\eta\geq f(q)+\eta S
\quad\Longrightarrow\quad
\boxed{E f(X)\geq f(q).}$$

This protects original expected utility, not merely expected material quantity. It covers all accepted lotteries and transfers within the actual surplus bound. With fallback efficiency gap g and current decision error epsilon, the lower bound becomes f(q)-eta g-epsilon. The parameter eta is a current-utility weight in declared units, and transforms with a positive affine rescaling of f.

## 2. An insured productive default

Use the hidden-effort technology with project stocks R_A,R_B, costs c_A,c_B, success probabilities 0,a,a,b and output Y_0. To avoid confusing B with output, write V=bY_0, D=(b-a)Y_0 and C=V-c_A-c_B. Assume

$$aY_0<\min(c_A,c_B),\quad c_A<D,\quad c_B<D,\quad C>0.$$

Choose a desired original-A gain r in (0,C) and q=R_A+r. A conditional allocator pays A the same transfer

$$k=c_A+r$$

in both success and failure states after the agreed installation is certified. B receives the remaining common output and pays k. If A works, its final X=q with certainty. If it shirks, it keeps the effort material and gets X=q+c_A. The contract therefore cannot by itself motivate original A to work. Its activation must be tied to an actual goal change or an equally credible effort commitment.

Finite collateral suffices if

$$R_B\geq c_B+c_A+r.$$

Then B can pay k even after contributing and seeing failure. No outside subsidy or unlimited wealth is assumed. Both agents still retain attack at the declared nonterminal checkpoints.

When B works, changed A's work-versus-shirk gain is

$$f(q)-f(q+c_A)+\eta(D-c_A).$$

B's own work-versus-shirk gain when A works is D-c_B>0. Thus sufficiently large finite eta induces mutual effort. Moreover, both current agents prefer mutual effort to the mutual-shirk continuation if

$$\boxed{\eta>\frac{f(q+c_A)-f(q)}{C}.}$$

This is stronger than A's unilateral effort condition because C<D-c_A when aY_0<c_B. B's improvement over mutual shirking is V-c_B>0. Mutual shirking can still remain an equilibrium, so the productive continuation is a specified Pareto-superior selection, not a unique-equilibrium result.

Mutual effort gives expected final outputs q and R_B+C-r and maximizes expected total output R_A+R_B+C over the declared physical production routes. Therefore section 1 protects original A's utility f(q) across every accepted renegotiation with that fallback. Concavity implies E X>=q whenever E f(X)>=f(q); consequently B cannot increase its expected Y above R_B+C-r by an accepted rearrangement. The insured default itself attains that bound.

## 3. Proposal incentives through a two-round bargaining game

An agreed beneficial contract is not yet an optimal proposal. Consider a finite alternating-offer implementation with genuine physical delay: the first round can attain net productive surplus C, while rejecting its offer leaves a second-round frontier C' with 0<C'<C. Both rounds satisfy the effort and collateral conditions above. A is first proposer, B second. Rejection of the final offer gives the original stocks. Attacks remain available throughout and must be inferior to the relevant offered or stock continuations in the physical instance.

In round two, original B can offer A insurance at q=R_A, conditioned on A voluntarily installing a suitable U_eta. Original A is indifferent to its stock outside option and accepts under the stated tie selection. The installed goal makes effort strict when eta is chosen above the current bound. B gets net C'. This is optimal over all accepted physical contracts: original A's concavity and participation imply E X>=R_A, and total expected output is at most R_A+R_B+C'. Hence B cannot obtain more than R_B+C'.

In round one, B's current reservation is therefore R_B+C'. A offers an insured goal-change arrangement with

$$q=R_A+C-C',\qquad E Y=R_B+C'.$$

B accepts at indifference to waiting. Original A strictly prefers the change because C-C'>0. It is an optimal first-round proposal: any accepted continuation gives B at least R_B+C', so E X<=R_A+C-C'; Jensen then bounds original A's expected utility by f(R_A+C-C'), which the insured arrangement attains.

Thus the same argument connects a physically larger early surplus to an optimal negotiated, voluntary genuine change for any increasing concave f, subject to collateral, feasible installation, current-self continuation and the declared selection. The construction does not assume that the original agent values change or insurance intrinsically. It chooses insurance and a productive successor because together they advance f.

The contract must activate only upon verification of the promised goal; otherwise A could accept its insurance payment and retain the original incentive to shirk. At each pre-activation choice, incumbent A prefers its promised f(q) to cancellation; after activation the current U_eta prefers productive execution. B's conditional payment obligation and its acceptance/withdrawal opportunities need an explicit physical state table. This remains to be supplied before claiming a complete extensive-form theorem.

## 4. Ordinary controls and remaining checks

An ordinary fixed-utility output contract cannot give A the same certain q under both effort choices and induce its contribution: shirking increases its certain own output by c_A. A binding effort delegate can reproduce the insured mechanism while preserving the principal's utility and must be included if available. Observable sequential effort or effort verification may also change the implementable insurance set. Equal-cost replication is a tied successful alternative; cheaper implementations can displace direct goal modification.

For strictly concave f, achieving A's first-round upper bound requires full insurance, because equality in Jensen requires constant X. Without a binding effort device, the just-described output contract has a strict shirking deviation. This suggests a strict ordinary-contract gap under a compact implementation class; the existence/compactness and all randomization details still require proof. For affine f, the earlier summed incentive constraints supply the ordinary budget-balanced effort obstruction when c_A+c_B>D. These are separate arguments and should not be conflated.

Further unilateral goal changes, changed proposer rights, counterparties, limited collateral, delays that alter combat returns and unsound verification are consequential variations. A chosen guard of the kind in 040 may preserve the productive fallback, but its adoption and costs cannot simply be assumed. The present note establishes the certificate, effort inequalities and candidate optimal-offer calculation; integration and robustness checks continue.
