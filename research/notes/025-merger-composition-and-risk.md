# R0001 working note: merger composition and lottery preferences

Note 010 gives an additive constituent-goal construction. This note checks what must survive repeated merging, gives a different associative construction, and shows why applying a concave repair recursively is not the same operation. The aggregation algebra is conventional; no novelty claim is made. Proofs are AI self-checked only.

## 1. Physical strength and constitutional weights are different records

Let the founding project coordinates be x_i>=0, with fixed positive weights a_i and A_S=sum_{i in S} a_i for a coalition S. Initially the a_i may equal combat strengths. After damage, deployment, or organizational synergy, the current controller's physical strength need not remain A_S. The model must record that transition rather than silently rewrite an installed utility's weights.

If current physical strengths really add and ordinary control is strength weighted, replacing a group's controllers by one controller with their summed strength and their weighted conditional policy preserves the outside outcome law (note 010, section 2). That representation theorem does not make the new controller choose the weighted policy, nor does it determine its utility aggregation rule.

All constructions below keep their founding coordinates and calibration fixed while grouping them. New negotiations may change those data, but that is a genuine additional objective-design choice whose current-utility incentives need checking.

## 2. Additive constituent accounting is associative

For a fixed increasing strictly concave function phi, define

$$G_S(x)=\sum_{i\in S}a_i\phi(x_i/a_i).$$

Then G_(S union T)=G_S+G_T for disjoint groups. Repeated addition gives the same function in any order, and the unique optimum on sum_i x_i<=Y remains x_i=a_iY/A_(S union T). This is the construction already used in note 010, now made explicit as a composition rule.

If a supplied group representative is u_S=alpha_S G_S/A_S+beta_S with alpha_S>0, the calibrated merger is

$$\frac{A_S(u_S-\beta_S)/\alpha_S+
A_T(u_T-\beta_T)/\alpha_T}{A_S+A_T}.$$

It equals the combined G divided by total weight. Thus arbitrary positive affine recoding does not change the merged preference **when the calibration is adjusted with it**. Dropping the alpha/beta metadata and merely averaging the displayed numbers need not preserve it. Self-knowledge, public verification of those data, and binding installation remain distinct capabilities.

The data may be represented by an expression tree rather than a literal vector, but their functional meaning cannot be discarded. This rule sums the already defined constituent transforms; it does not apply phi again to an already aggregated utility.

## 3. Reapplying the same concave rule changes the allocation

Consider three equal-strength founders with dimensionless own-color utilities u_i=x_i and sum_i x_i<=1. Define a seemingly natural recursive rule for groups of weights a,b:

$$N_{a,b}(u,v)=\frac{a\sqrt u+b\sqrt v}{a+b}.$$

Use the rule's stated numerical output as the next group's canonical input; there is no accidental change of representation in this example. If A and B merge first and that group then merges with C, the final objective is proportional to

$$\sqrt{2(\sqrt{x_A}+\sqrt{x_B})}+\sqrt{x_C}.$$

For a fixed A/B total z, it uniquely splits that total equally. The remaining maximization is

$$2^{3/4}z^{1/4}+\sqrt{1-z},\qquad 0\leq z\leq1.$$

Its strictly decreasing derivative vanishes at z=1/2; equivalently, 1-z=sqrt(2) z^(3/2). Therefore the final allocation is (1/4,1/4,1/2). Merging B/C first instead gives (1/2,1/4,1/4). The controller strengths are still 2 and 1 at the final merge; they do not repair this path dependence by themselves.

The failure concerns this recursive rule, not all concave successor objectives. Adding the constituent terms once would instead give sqrt(x_A)+sqrt(x_B)+sqrt(x_C), uniquely producing (1/3,1/3,1/3).

## 4. A different associative rule: power means

Fix 0<rho<1. For group S define the per-weight goal and its quantity-equivalent multiple by

$$H_S(x)=\left[\sum_{i\in S}\frac{a_i}{A_S}
(x_i/a_i)^\rho\right]^{1/\rho},\qquad Q_S=A_S H_S.$$

The calibrated group-composition rule is

$$H_{S\cup T}=\left[
\frac{A_S H_S^\rho+A_T H_T^\rho}{A_S+A_T}
\right]^{1/\rho}.$$

Substitution cancels each internal power and reproduces the flat expression over all founding coordinates. It is associative in any grouping with the same weights. H and Q for one fixed group differ by a positive constant, so they represent the same lottery preferences. The input to a later merger must consistently be H, or decode Q/A first.

The power-mean goal is increasing and concave, and it uniquely produces the strength-proportional allocation at a fixed positive total budget. A direct curvature check avoids treating a nonlinear transform as automatically concavity preserving. Put z_i=x_i/a_i, w_i=a_i/A_S and S=sum_i w_i z_i^rho. For an interior perturbation v,

$$v^T\nabla^2H_S v=(1-\rho)S^{1/\rho-2}
\left[\left(\sum_iw_i z_i^{\rho-1}v_i\right)^2
-S\sum_iw_i z_i^{\rho-2}v_i^2\right]\leq0$$

by Cauchy-Schwarz. Equality requires v proportional to z. On a fixed total-resource tangent sum_i a_i v_i=0, that means v=0. Continuity extends concavity to the boundary, and Jensen gives the unique proportional optimum. Global strict concavity is not claimed: Q is homogeneous of degree one and is linear along each ray.

For a group with total budget Y, its optimal value is Q_S=Y. This explains the term quantity-equivalent; Q is still a utility function, not conserved energy or a physical resource stock.

## 5. The two associative designs have different lottery preferences

For phi(t)=t^rho, the additive goal G_S and power-mean goal Q_S have the same deterministic maximizers because Q_S=A_S(G_S/A_S)^(1/rho). For rho!=1 this is generally **not** a positive affine transformation, so it is a genuine expected-utility preference difference.

With two equal weights and rho=1/2, compare a certain balanced output of total 1/2 with a lottery giving balanced total one or zero, each with probability 1/2. G gives the certain outcome value one and the lottery value 1/sqrt(2), so it strictly prefers certainty. Q gives both expected value 1/2 and is indifferent. A difference in indifference rules out positive affine equivalence.

Thus one cannot replace an additive goal by its power-mean transform while claiming only to have changed its representation. Conversely, either goal is a legitimate optional installed criterion when adoption is evaluated by the predecessor's actual preference.

## 6. The difference changes incumbent merger participation

Consider two currently independent groups S,T with strength share s=A_S/(A_S+A_T), and suppose each values only its own founding coordinates. If one wins, it maximizes its own current goal over total output W; the other group gets zero. A protected deterministic split or merged controller supplies respective group totals sP and (1-s)P, each allocated proportionally within the group. All processing and integration costs are already reflected in P,W. Keep combat available until the actual fusion removes separate agency.

If the current group criteria are the quantity-equivalent Q goals, their deterministic values are their group totals. Both strictly prefer the split to war iff P>W.

If their current criteria instead are additive power goals G with the same rho, a group's value from total Y is A_S^(1-rho)Y^rho. The common factor cancels from its participation test. The two conditions become

$$P/W>s^{1/\rho-1},\qquad
P/W>(1-s)^{1/\rho-1}.$$

For interior s and rho<1, both right sides are below one. These already risk-averse incumbents can accept a deterministic compromise that produces less than combat would conditional on victory. For example, s=1/2,rho=1/2,P/W=9/10 passes both G conditions but fails both Q conditions.

This does not make a linear original founder approve installing risk aversion for its own sake. It compares **current** group preferences, which may have been installed earlier under a separately justified adoption decision. The original founders' physical welfare must still be reported. An equally enforceable fixed-utility split gives the same deterministic outputs without a new change, so this local risk-sharing comparison does not establish that merger is necessary.

## 7. Algebraic consistency is not strategic stability

Associativity holds only while the constituent weights, calibration and aggregation rule are held fixed. It does not imply that agents agree to each step, that a current merged agent refuses a later reweighting, or that its founders retain decision authority. Note 012 supplies a concrete founder/current-successor conflict even when each later proposal is consensual.

Changing physical strength, initial freezing preferences, heterogeneous risk curvature, synergy and private calibration are further choices. A mechanism that recomputes constitutional weights from present combat strength may be coherent, but it can change the objective and make the path matter. The correct record is an explicit preference/physical transition, not a claim that goal averaging automatically preserves the essay's strength-relative allocation intuition.

## 8. Preserving every original lottery indifference prevents this repair

There is a stronger demand one might mistakenly impose on a “faithful” merger: whenever all original linear color agents are indifferent between two lotteries, the merged criterion must also be indifferent. This is not the same as their consent to one specific merger outcome.

Suppose the physical domain is the convex resource simplex and the successor has vNM utility U. For any two worlds x,y and t in [0,1], each original color utility is indifferent between the deterministic mean tx+(1-t)y and the lottery assigning probabilities t,1-t to x,y. Preserving all those indifferences requires

$$U(tx+(1-t)y)=tU(x)+(1-t)U(y).$$

Thus U is affine on the simplex. For example, express each point as a mixture of the origin and the resource-simplex vertices; the equality directly gives a fixed affine combination of its coordinates. An affine utility cannot uniquely maximize at an interior allocation: unequal coordinate coefficients favor a face or vertex, while equal coefficients leave all full-output allocations tied.

This is a direct specialization of familiar expected-utility aggregation reasoning. Harsanyi (1955), section III, pp. 312–314, states individual/social expected-utility and unanimous-indifference premises and derives weighted linear aggregation; those pages and the proof were inspected in the [original article](https://davidmccarthy.org/wp-content/uploads/2018/09/harsanyi1955.pdf). L20 records the scope. The present simplex proof does not claim a new aggregation theorem or infer positive weights from indifference alone.

Consequently the full lottery menu, universal preservation of the originals' lottery indifferences, and unique interior production by the successor cannot all hold. The nonlinear goals in this project intentionally relax the second requirement; their risk preferences are part of an actual utility change. A protected allocation policy or a restricted physical lottery kernel is another possible repair, with different implementation assumptions. Local incumbent consent and safe improvement relative to a specified baseline outcome do not require preserving every unanimous indifference over all conceivable lotteries.
