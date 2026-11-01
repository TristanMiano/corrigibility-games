# R0002 extension: coordination beliefs, costs and negotiated shares

**Exact reduced-game calculation, conditional on the stated continuation module.** The guarded construction establishes an equilibrium with voluntary preference change. This note asks when agents prefer entering that arrangement before knowing whether a partner will enter. It also identifies how ordinary peaceful improvements affect that choice. It is a belief/choice comparison, not a population-frequency theorem.

## 1. Two available modes and their payoffs

Subtract each agent's retained initial stock. Let G mean installing the compatible productive arrangement; its best available implementation can be a genuine goal change or a matched delegate. Let O mean an incompatible ordinary output-contract mode. The conditional module is:

| Choices | Agent i's original payoff above stock |
| --- | --- |
| Both G | r_i-k_i |
| i chooses G, other chooses O | -k_i |
| i chooses O, other chooses G | 0 |
| Both O | o_i |

Here r_A+r_B=C is the full productive surplus before installation, k_i>=0 is the actual installation cost, and o_i>=0 is the payoff of the selected available ordinary peaceful contract. In the small-collateral fixture, o_A+o_B can be 2/5, whereas C=4/5. When just one installs, both retain their remaining stocks because the guarded party makes no outgoing concession to an incompatible party and combat is unattractive in that branch.

This module deliberately states what a complete strategic selection model would have to supply: a chosen ordinary continuation, its selection when effort is weakly optimal, a rule for failed coordination, and an actual implementation-cost comparison. O does not mean every agent retaining its terminal utility. A compatible binding delegate belongs to G. If a new ordinary technology can obtain the compatible certificate, include it in G at its true cost instead of forcing it into the failure branch. Threats or unilateral options improving either off-diagonal payoff require recalculation.

## 2. A belief threshold for entering the arrangement

If i assigns probability p to the other choosing G, its original-utility advantage from G is

\[
p(r_i-k_i)+(1-p)(-k_i-o_i)
=p(r_i+o_i)-(k_i+o_i).
\]

For r_i>k_i, G is strictly preferred exactly when

\[
\boxed{p>p_i^*=\frac{k_i+o_i}{r_i+o_i}.}
\]

Lower installation cost lowers this threshold. A larger negotiated productive share lowers it. A better ordinary continuation raises it, since d p_i^*/d o_i=(r_i-k_i)/(r_i+o_i)^2>0. The last comparison describes displacement toward another peaceful option, not an increase in combat. Genuine modification is selected within G when it is a least-cost available compatible implementation; equal-cost delegation creates an implementation tie.

For symmetric r_i=2/5, k_i=1/20, o_i=1/5, the threshold is 5/12. At equal probability of the two partner modes, entering G is strictly preferred. More generally that equal-belief comparison holds exactly when r_i-o_i>2k_i. If symmetric installation cost reaches 1/10, the fixture is at equality; above it, the ordinary mode is preferred at that belief even while a profitable mutually guarded equilibrium can still exist.

This identifies distinct claims: r_i>k_i makes mutual guarded adoption a best-response outcome; the stronger inequality r_i-o_i>2k_i makes it individually attractive at the specified uncertain-coordination belief. Neither condition determines actual population frequencies without a process generating beliefs and choices.

## 3. Negotiating the shares improves the common threshold

Put K=k_A+k_B and O=o_A+o_B. Suppose shares r_i can be negotiated subject to r_A+r_B=C and there is no extra share restriction. The smallest common p sufficient for both agents is

\[
\boxed{p_{\min}=\frac{K+O}{C+O},\qquad C>K.}
\]

To prove the lower bound, both requirements p(r_i+o_i)>=k_i+o_i sum to p(C+O)>=K+O. Equality is attained by choosing

\[
r_i=\frac{(k_i+o_i)(C+O)}{K+O}-o_i
\]

when K+O>0. These shares obey r_i-k_i=(k_i+o_i)(C-K)/(K+O)>=0, with strictness whenever k_i+o_i>0. A zero component can be given an arbitrarily small positive share, giving the same infimum where strict gains are required. When K+O=0, any positive split has zero threshold.

Thus a negotiated allocation can make both agents favor the arrangement at a common belief p=1/2 precisely when

\[
2K+O<C
\]

with the strict-share qualifications just stated. In the fixture K=1/10, O=2/5, C=4/5, p_min=5/12 regardless of how the ordinary surplus is split, provided the productive shares can adjust. If all ordinary surplus goes to A, the threshold-equalizing productive gains are (17/25,3/25), corresponding to output shares (57/100,43/100). The contribution rewards retain strict effort incentives at that split; final failure holdings are unchanged.

## 4. Capability comparisons and scope

Holding the physical surplus and ordinary alternative fixed, lower total installation cost lowers the negotiated coordination threshold with derivative 1/(C+O). Holding installation costs fixed, a larger productive surplus lowers it. Better ordinary monitoring can instead raise O and shift choices toward unchanged-goal cooperation. If that monitoring implements the same compatible arrangement more cheaply, it lowers G's effective cost and changes its internal implementation choice; these are different comparisons and should not be conflated.

The thresholds are algebraic statements about current original goals and explicit beliefs. No reproductive fitness, inherited type distribution or learning law has been supplied. A future repeated-choice model can use this module, while retaining both a constructive question about selection of accommodation and a limiting question about failed coordination or superior peaceful alternatives. The established voluntary-adoption equilibrium in 046 is not contingent on solving that further population question.
