# Who can walk away from a doubtful installation?

A powerful customer can insist on evidence because the batch is still valuable to it after a dispute. A powerful installer can make the customer's fallback depend on *which goal actually took effect*: an original installer may prefer the contest, whereas a changed installer may accept a peaceful return. This changes how much an inspection is worth. This note solves the buyer's monitoring decision and the installer's response together for the commissioning game in [206](206-when-a-truthful-attempt-can-fail.md).

## All active inspection choices in this class

Write (A_G,B_G) and (A_N,B_N) for outputs following a declined release when the installer's current goal is genuine or retained. These are actual continuation outputs, evaluated here by the founders' original goals. On release, the outputs are (a,b) after a genuine installation and (a+d,b−l) otherwise. Set g=b−B_G>0, h=B_N−(b−l)>0. An investor's unwillingness to release can reflect a good fallback against a retained controller, even if its peaceful fallback against a genuine controller is very different. In this class offering return weakly beats the customer's initiating immediate combat after a signal, in either possible state. A customer's credible choice of combat upon refusal is included in the continuation outputs.

With genuine installation probability π, trusting is worth πg−(1−π)h over declining. Testing and releasing only after a positive earns πtg−(1−π)eh−c. With t>e the other signal-contingent policy, releasing only on a negative, cannot strictly improve on the best unconditional action. Define

    π_L=(c+eh)/(tg+eh),       π_U=((1−e)h−c)/((1−e)h+(1−t)g).

**207.1.** A positive-width interval of priors at which B strictly buys evidence exists exactly when c<gh(t−e)/(g+h). Its interior is (π_L,π_U). Below the interval B declines, above it B trusts without testing. To verify, intersect the two linear comparisons in 206.3. At π=h/(g+h) the two unconditional actions tie and the gross value of checking is gh(t−e)/(g+h); moving toward either extreme decreases the improvement over the better unconditional action. This is a condition on the *buyer's incentives*, even with an excellent available test. Within the interval the positive and negative responses are individually strict.

Let x,y,z denote B's probabilities of testing, trusting without a test and declining untested. Conditional on successful installation, the original founder gains the following amounts relative to deliberately faking, for each pure policy:

    Z_N=A_G−A_N,     Z_T=−d,
    Z_Q=A_G−A_N+t(a−A_G)−e(a+d−A_N).

An attempt multiplies the corresponding difference by q since a real failure and a fake have the same continuation within this interface. The privately known attempt expense is paid regardless of success. Consequently

    π=q clip(q[x Z_Q+y Z_T+z Z_N]/K,0,1).                        (207.2)

Assume Z_N≤0, Z_T<0, Z_Q>0 and a+d>A_N. Original refusal yields A_N. Whenever some batch is entrusted, even the highest-cost type can gain from signing. All types then sign, so (207.2) also gives the fraction of *offers* leading to a real installation. On a zero-trade path signing need not be strict. Let π_Q=q min(q Z_Q/K,1).

**207.3 (equilibrium scope).** Away from equality boundaries, if the buyer has no profitable test interval or π_Q<π_L, there is no equilibrium with positive trade under this menu. Otherwise there is a positive equilibrium with a mixture of testing and untested decline that supports π=π_L. The highest-installation equilibrium uses pure testing if π_Q lies inside the interval. If π_Q>π_U it uses a mixture of testing and untested trust that supports π=π_U. In the latter case

    x=(Kπ_U/q²+d)/(Z_Q+d),      y=1−x.                            (207.4)

The low equilibrium uses x=(Kπ_L/q²−Z_N)/(Z_Q−Z_N), z=1−x. A no-trade assessment also exists with retained evaluators and a refusal after any signature in the baseline menu. A positive fee to make a false declaration or a separate ordinary route can change this assessment.

For the proof, without any checking both Z_N and Z_T give zero installations and the buyer then strictly declines. Any bought test must have meaningful signal-contingent release, and (207.1) gives all strict and mixed buyer responses for positive trade. The π induced by a mixture with either unconditional act rises continuously from zero to π_Q as its testing probability rises. Equating it to the respective indifference probability gives the stated mixtures. On the pure-testing path the π_Q value must itself yield testing. Continuous costs have no mass at an indifferent private cost. These are on-path Bayesian comparisons with an offered and signed bargain. For the physical examples a customer obtains at least its original refusal value by making the offer in each positive equilibrium. Selecting the highest-installation branch is a comparison of equilibria, not a prediction of how a market selects.

## A strength sweep with fixed technology, goals and prices

Use the physical parameters of 206, varying only B's probability s of winning a contest. Returned stocks are (2,2), contested expectations (3−3s,3s). For 0<s<1/3, original A contests a return. A genuinely changed A prefers the returned bundle by its own criterion, since 3>3−1.5s. B prefers offering the return to initiating itself. Thus (A_G,B_G)=(2,2), (A_N,B_N)=(3−3s,3s). For 1/3<s<2/3 both controllers and B accept the return. Above 2/3 B contests a refusal, yielding the wartime pair for either A controller. At any live checkpoint A's preferred action on a released batch beats its own contest value. B can initiate before relinquishing control, including after its signal. After the last physical release A can complete its chosen conversion before B can interfere again. Extra advance information or a later chance to intercept the conversion changes that timing.

| B's strength s | Monitoring in the highest-installation equilibrium | What sets the boundary |
| --- | --- | --- |
| (0,4/93) | No active trade. A contests the returned batch. | B's own prospective recovery is too small for even the best prior to justify buying the test. |
| (4/93,1/3) | B mixes testing and untested trust. Some installations, honest failures and intentional false claims occur. | The remaining controllers can contest a return that a genuine controller accepts. B buys evidence only at π_U. |
| (1/3,2/3) | B always tests, 64% of offers achieve the changed goal, and declined batches return peacefully. | Both original peaceful fallback shares exceed combat returns. |
| (2/3,29/39) | B again mixes testing and untested trust. A declined batch now produces combat. | B's better recovery makes combat credible; A's diminished fallback would attract more genuine attempts than can support pure testing here. |
| (29/39,1) | B always tests and every installer honestly attempts the update. Four in five installations succeed. | B has enough at stake after either kind of rejection to buy the test even when the only mismatches come from honest failure. |

For s<1/3, g=4, h=3s, Z_Q=1/2+27s/10 and π_Q=8/35+216s/175. The affordable-test bound in 207.1 gives s>4/93. At π_Q, the benefit of checking over always trusting before its cost is (1−π_Q)(.9)(3s)−π_Q(.1)(4). This concave quadratic has maximum 5489/56000 at s=103/432, below c=.1. Thus any positive high branch here must mix. In the middle band (206.3) holds strictly. Above 2/3 pure testing would attract every cost type, giving π_Q=.8. At that prior the gross advantage over untested trust is .78s−.48, exceeding .1 exactly above 29/39. Positive-only release also strictly beats declining throughout this upper band. Endpoints with indifference have additional possible choices.

At s=.05 the high branch buys tests on about 81.3% of offers and genuinely changes goals on 6.54%. Even after a positive the probability of a genuine goal is only about 38.65%. B still finds entrusting a positive batch worthwhile, since it can recover little against an unchanged A. At s=.8 the positive posterior is 36/37. Yet the customer contests 26% of all offers on this branch. Those contested cases comprise 8% genuinely changed but falsely rejected and 18% honest failures correctly flagged. The installer never lied in this last example. Stronger assurance about accepted offers, a higher genuine adoption rate, and a higher incidence of combat can occur together. In the central band every rejected batch can return peacefully.

**Naturality, construction and limits.** Unequal access to recoverable stocks and a deadline that leaves one line active after conflict give a physical interpretation to the outside options. Variation in s compares initially different environments. Neither party in this sweep purchases a strength change. B does have authority to pay .1 of its output for a test, and a low-cost A can pay to change its goals for the more valuable batch. Routable collateral, an ordinary upfront payment or a local binding delegate can raise the weak party's fallback or deliver the batch without relying on goal evidence. The sharp no-trade region applies to this specified offer menu. A sibling prices a binding handover or an affordable partial batch. The higher-level question is how the parties choose what must be exposed before they can learn anything.
