# Who signs when even a correct goal has an uncertain yield?

Two founders can strictly prefer a deal while assigning only a 9-in-16 chance to both promised changes actually happening. In the same deal, even a partner with exactly the agreed goal delivers an uncertain quantity. What makes signature attractive here is the combination of valuable work, a check that favors actual updates, and insurance against a different source of loss. These conditions have separate, measurable thresholds.

## Three physical risks

Two plants care only about their own final stock. Each founder evaluates lotteries by the incumbent criterion `−2^(−own stock)`. Its certainty equivalent in units of stock is `−log₂ E[2^(−stock)]`. Each can keep a safe four units using its seasonal equipment alone. Both signatures reserve that equipment for the joint season and pay a metering fee m=.05 each. The parties can jointly specify an automatic weather transfer f between zero and two units beforehand. In either of two equiprobable weather states the equipment otherwise produces baseline stocks (2,6) or (6,2). The plant in the good location delivers f to the other from the public harvest. An agreed meter can reserve that much fungible input at source. Weather and both installations are independent.

Privately, each founder can pay k=.25 to attempt the agreed update or falsely declare readiness for free. An attempt succeeds with q=3/4. Success installs the criterion `−2^(−(own stock + partner stock / 2))`. A failed attempt leaves the original criterion. The installed criterion reverses the founder's strict ranking of, for example, (4,1) and (3,5) in own/partner order. The readout always passes a correct installation and passes a remaining original with probability 1/4. These are independent readings conditional on the installations. Two passes release both sites' equipment for a last opportunity to help. At each site, sending costs one unit of own stock and independently produces two or four units for the *other* plant with equal chances. Keeping produces zero extra units for the other. The yield is realized after the donor chooses. The agreed goal favors sending since the change in the underlying weighted stock is zero or +1 with equal chances. The original strictly favors keeping. This is uncertainty *after* a fully successful update as well as uncertainty about implementation.

Metering the common harvest and commissioning the two sites do not reveal their private downstream effort. The physical reservation of public stock is binding once signed. An original founder can keep its old goal and exploit a mistaken opening. Until final conversion, either party can contest the remaining equipment, with a strength-dependent chance of winning. After disruption, recovery and finishing use up all but at most half a unit of usable final stock for the winner and give zero to the other. Even the least favorable continuation under the proposed hedge or at f=0 retains at least 2−1−.25−.05=.70 for each, and a successful editor also values the partner's preserved stock. Combat is available and strictly worse at these live histories. Conversion ends agency over this batch. A richer salvage technology or a valuable unilateral use of the reserved season changes the participation comparison.

## Pay for the edit, falsely sign, or keep the safe four?

Let H be a paid sincere attempt and D a false declaration. Because the exponential criterion factorizes over independent stock increments, first calculate the expected factor from sending and receiving conditional on the chosen pair of declarations. Receiving a gift multiplies expected disutility by b=(2⁻²+2⁻⁴)/2=5/32. Giving costs one, a factor of two. When both attempt, both send with probability 9/16. Only the founder sends with probability 3/64 and only its partner sends with probability 3/64. When a false signer faces an attempter, it receives with probability 3/16 and always keeps. Thus

    M_HH = 1 + (9/16)(2b−1) + (3/64)(2−1) + (3/64)(b−1) = 1271/2048,
    M_DH = 1 + (3/16)(b−1) = 431/512.

The incumbent strictly pays for the attempt if k < log₂(M_DH/M_HH), about **.440 units**. The common weather factor and already paid meter cancel from this comparison. With the stipulated .25 cost, mutual sincere attempts are a strict continuation equilibrium. Mutual false declarations also support a no-work continuation, where an isolated attempt risks a costly gift. The construction establishes a coordinated adoption outcome.

For equal contracts the certainty equivalent of signing and mutually attempting is

    CE(f) = 4 − log₂ cosh((2−f) ln 2) − log₂ M_HH − k − m.         (215.1)

The first deduction prices the remaining weather exposure. The second term values the uncertain downstream gifts under the original preferences, counting both favorable and mistaken openings. For the choices above, each signs over the safe four exactly when

    f > 2 − acosh(2^(−k−m)/M_HH)/ln 2 ≈ .894

for strict preference, with indifference on the boundary. Zero insurance gives CE=3.301. Full insurance gives **4.388** and is each founder's strict favorite at the common fee before it learns its weather. Each can fund the arrangement out of the high-state stock and has a current-goal reason to authorize the meter. A winner asked to transfer voluntarily *after* the weather is known would keep the stock. At the full hedge, the founders sign even though both actual goals change with probability .5625 and the chance of joint genuine change given admission is 144/169, about .852. The outcome of the private work remains risky after admission. Neither number is a universal confidence requirement.

## Available ordinary contracts and the reach of the example

Weather insurance alone equalizes the baseline at four less the fee and elicits no hidden gifts from two unchanged donors in the last batch. A local delegate implementing the same hidden-effort rule with identical commissioning, failure rates and costs gives the same original welfare. An ordinary router capable of binding *both* gifts for certain would give M=2b=5/16. With the common full weather hedge it displaces the proposed updates if its additional price per plant is less than k+log₂(M_HH/(5/16)), about **1.240**. A transfer for unobserved private effort requires a feasible way to meter or bind that effort. The founders' choice depends on which instruments they can actually buy.

**Naturality and reach.** Geographically separated plants can experience opposite yield shocks while sharing a cheap, independently readable weather or bulk-output index. Specialized local processing and the recipient's private use can still obscure the amount of help a donor provided. The perfect sensitivity, independent fair shocks, exponential valuations and prices here are illustrative. Less insurance capacity or a better safe harvest can move the same parties to the separate option. A sibling can buy a small first batch when there is no weather meter. The broader question is how much jointly verifiable payoff risk the partners must be able to reallocate for the remaining uncertainty to be worth accepting.
