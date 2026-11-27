# Which risks can the signers share?

A partner can reasonably doubt an installation and still want the deal. One way to decide is to value *all* the resulting stocks under the incumbent preferences, then ask what insurance the parties can actually fund. The boundary below covers imperfect inspection, honest execution failures, uncertain physical yields and differing beliefs in the same calculation. It applies to a proposed continuation whose incentives have already been checked.

## A bilateral consent test

There are finitely many states s, including the installation, readings, private actions, weather and output as appropriate. Founder i has full-support beliefs P_i and exponential utility with tolerance T_i>0. X_i(s) is its founder-valued private stock after all expenses and actions in the proposed deal. A unit of reservable common input can become a unit of either party's stock. The parties can move c_y units from B to A upon a publicly verifiable reading y. States with the same y must receive the same transfer. Access to the input is reserved by consent before the reading arrives. Define

    A_y = sum over s in y of P_A(s) exp(−X_A(s)/T_A),
    B_y = sum over s in y of P_B(s) exp(−X_B(s)/T_B),
    T = T_A + T_B,   α = T_A/T.

Let r_i be the certainty equivalent of i's available disagreement continuation, including safe production or an advantageous contest. If several feasible joint outside contracts compete, each one requires its own selection comparison. With unrestricted funded transfers and a transferable signing payment, the founders can both strictly beat their respective r_i **if and only if**

    J(Y) = −T log sum_y A_y^α B_y^(1−α) > r_A + r_B.              (216.1)

Equality permits joint indifference. To prove this, let a=Σ A_y exp(−c_y/T_A) and b=Σ B_y exp(c_y/T_B). The sum of the two certainty equivalents is −T log(a^α b^(1−α)). Hölder bounds the quantity inside the log below by Σ A_y^α B_y^(1−α) because the transfer factors cancel. Equality is attained by

    c_y = (T_A T_B/T) log(A_y/B_y) + C.

The free constant C moves a certainty-equivalent unit from B to A one for one. This proves attainability and both directions of the claim. With common beliefs and every state verifiable, (216.1) becomes the representative certainty equivalent −T log E exp(−(X_A+X_B)/T). With different beliefs each founder also values bets on which state occurs. These are *subjective* participation gains; physical output and welfare under a common reference distribution require their own accounting.

Refining a public reading weakly increases J. Within every old cell, another application of Hölder gives the weak inequality, strict precisely when the positive A/B ratios of its newly distinguished subcells differ. An accurate diagnostic that separates states bearing identical ratios has zero extra insurance value in this calculation. A measurement of production risk can be worth buying even if it leaves the probability of the agreed goal exactly where it was. If a proposed extra measurement costs d_A,d_B units of certain stock, both can strictly fund it with transferable unrestricted side payments when the increase in J exceeds d_A+d_B and it beats the existing options. An *optional* reading can always be ignored under these assumptions.

## Limited deposits and an exact physical example

Real transfers may have to stay inside an interval [l_y,u_y] in each public state. Write a(c), b(c) as above and R_A=exp(−r_A/T_A). If a(u)>R_A, even B's largest permitted payments cannot give A its outside value. If a(l)≤R_A, c=l maximizes B's return while satisfying A. Otherwise choose λ>0 so that a(c)=R_A with

    c_y = clip( (T_A T_B/T) log(λ T_B A_y/(T_A B_y)), l_y, u_y ).

This minimizes b(c) subject to a(c)≤R_A. Each cell minimizes its strictly convex term of b+λa, and a along this family is continuous and nonincreasing between the endpoints. At a(u)=R_A one can directly take c=u. Joint weak consent requires b(c)≤exp(−r_B/T_B); for joint strict consent apply the same check with a common positive increment to the two outside values. This covers physically binding wealth as well as a cap on pledged input.

For example, suppose the proposed batch leaves stocks (3,7) or (7,3) with equal probability, and each founder has utility −2^(−stock) and a safe alternative of 4.5. A binary public meter picks out the low plant with accuracy a≥1/2 in either state. It can release up to two reserved units in the indicated direction. Symmetry makes the best equal division a transfer of

    f* = (1/2) log₂[(1+15a)/(16−15a)]

to the indicated low plant. To see the threshold, factor out the low baseline of three units. The conditional disutility factors for the indicated low and high sites are L=(1+15a)/16 and H=(16−15a)/16. The equal-division expected factor is (L 2^(−f)+H 2^f)/2, minimized at sqrt(LH). Thus both strictly sign exactly when 16+225a(1−a)<32, or **a>(15+sqrt(161))/30 ≈ .923**. If the meter can reserve only one unit, f* hits the cap at a=.84. Above it the expected factor is (65−45a)/64 and strict participation instead requires **a>(65−16 sqrt(2))/45 ≈ .942**. At 93% accuracy, two units of reservable stock are enough and one unit leads the same founders to keep their safe options. Any founding meter expense is deductible before repeating the test.

Even an erroneous two-unit release leaves one unit for the short plant. For example, damage and a finishing deadline can cap the winner's recoverable contest output at half a unit at every live stage, with victory probabilistic in relative strength. Both parties then strictly take their peaceful continuations, including after the reading, until final conversion. Better unilateral recovery can raise r_i or create a later deviation; a signature theorem alone would not settle that game.

**Naturality and reach.** Physical batch indices and separately escrowed common inputs can support the public partition and funding cap. Separate projects with substitute inputs can arrange insurance before either knows who will be short. Transfer tolerances measure diminishing marginal value of each party's own stocks. They and the numerical example are model assumptions. The result applies equally to the genuine edits in [215](215-who-signs-when-even-a-correct-goal-has-an-uncertain-yield.md) and to an available ordinary contract. If the parties' hidden actions or disclosures would change with the insurance rule, X and its law must be resolved at the proposed rule. The independent weather meter in 215 passes this check. A sibling contract uses a physical deposit when the entire state remains private. The broader question asks what can be shared while preserving both the incentive to perform and the freedom to decline the bargain.
