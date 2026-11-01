# R0002 repair: diversify production and renegotiate the active plan

**Finite exact construction with rational interval checks.** The small-stock logarithmic case in 052 favors retention because one risky project lowers the maximum sum of original utilities. This note changes the production arrangement itself. Three bounded compartments, positive setup costs and imperfect diversification suffice for a mutually attractive guarded preference change. As common risk increases, negotiating a smaller active plan extends the successful region.

## 1. A costly physical enlargement

Keep original utilities log(1+X_i), stocks R=3, goal-installation cost k=1/20 and total calibration cost c=8/5. A shared batch reactor has capacity for at most three compartments. Choosing N in {1,2,3} costs h(N-1) finished units per participant, with h=1/100, and 1/20 extra work per additional compartment. Each of the N compartments has feedstock 10/N and uses calibration c/N from each contributing agent. The whole batch requires ten work units before any informative output observation, including when fewer compartments receive calibration. This is a shared heating/processing requirement; unused compartments cannot supply an early success signal or an uncharged independent reactor. New plants are outside this finite episode.

Within each compartment the success probabilities are 0,1/10,1/10,2/5 for the four contribution profiles. With probability 1-rho, compartment signals are independent. With probability rho, one common uniform U determines all signals: compartment l succeeds exactly when U is below its contribution-dependent success probability. This specifies the joint kernel under deviations as well as on the cooperative path. It does not silently assume that correlation is unaffected by effort.

For N=3, setup uses at most 1/10 extra work. The schedule in 049 then uses at most 10.502 work, below 11. Installation, input shipment, reaction and output delivery retain their positive durations. Only ten total output units are routed; partitioning does not multiply that quantity. The extra finished material costs are separate from work consumption. Attack and its recovery kernel remain available.

## 2. All contribution profiles have a finite welfare bound

Suppose m compartments receive both contributions, l receive exactly one, and N-m-l receive neither. Grant a hypothetical allocator equal division of total final output in every state. This is an upper bound on the original log welfare for any actual transfers or lotteries. Half of that maximal welfare is

\[
U_{N,m,l}(\rho,h)=E\log\left[
4-k-h(N-1)-\frac{c(2m+l)}{2N}+\frac5N K
\right].
\]

In the independent branch K is the sum of independent Binomial(m,2/5) and Binomial(l,1/10). In the common branch K equals m+l, m and 0 with probabilities 1/10,3/10,3/5, respectively. Thus each U is affine in rho and explicit as a finite sum of logarithms. Allowing all m,l covers every private contribution profile and its public or private mixtures. The equal allocation is actually attained when both agents contribute to the same chosen active compartments.

For the witness rho=1/10, h=1/100, exact rational bounds prove:

- U_(3,3,0)-log4 > 1/100. Each original agent strictly gains.
- U_(3,3,0) exceeds every other U_(N,m,l), N<=3; the smallest gap exceeds 1/200.
- All those upper bounds include allocation lotteries through concavity. Initial retention gives log4 per agent; combat's total welfare is also smaller under the recovery cap.

The actual gain is about 0.0114345 log-utility units per agent, and the nearest competing profile is two active compartments out of three. Exact interval checks also preserve strict adoption and welfare optimality throughout 9/100<=rho<=11/100 and 9/1000<=h<=11/1000: welfare is affine in rho and decreasing in h, so the tested extreme bounds enclose that whole rectangle. These are values and a parameter region for a declared class, not a population frequency.

The reproducible check is `python experiments/r0002_welfare_checks.py`. For any rational z>=1 it bounds the logarithm using

\[
\log z=2\sum_{j=0}^{L-1}\frac{t^{2j+1}}{2j+1}+R_L,
\quad t=\frac{z-1}{z+1},\quad
0\le R_L\le\frac{2t^{2L+1}}{(2L+1)(1-t^2)}.
\]

The tail bound follows by bounding each remaining denominator below by 2L+1 and summing a geometric series. Exact fractions certify the signs; printed decimals are explanatory. This is a reproducible finite mathematical check, not independent review or a proof-assistant certificate.

## 3. From a better production plan to actual goal choice

For the fixed-contract subgame, lambda_i=1/5, beta_i=1 and K_i=6 suffice. Here e_i=1 means actually supplying every calibration in the jointly registered active plan by its performance deadline. It does not require all installed compartments to be active. For the full-three plan, the greatest possible own log loss from paying all calibration costs is at most log[(393/100)/(233/100)]<1. Additional calibration weakly increases every output under the specified common-random-number coupling. Its effect on the other project is nonnegative. The contribution reward therefore makes completing the agreed plan strictly optimal against every peer contribution profile in that subgame, while actual partial effort remains physically available and unpenalized by I_i. The integrated construction uses beta_i in [4,5] and K_i=10: [056](056-contribution-rewards-through-renegotiation.md) proves that these parameters also cover a missed obligation followed by arbitrary renegotiation. Timely amendments remain available; a new plan cannot erase a past miss for its archived evaluator.

The productive plan maximizes the sum of original log utilities, and e_i=1. The welfare certificate preserves each participant's original-utility floor against accepted renegotiations. With lambda=1/5, equal-strength incompatible combat gives at most (1/2)log5<log4. For the broader concern family, a concave winner can allocate output to the defeated project; [055](055-concave-survivors-and-broader-original-goals.md) includes that output and proves the still-sufficient bound (1/2)log15<log4. Solitary production has negative expected material return; no informative signal appears until the work is spent, so a subsequent attack cannot rescue it. Thus both original agents strictly prefer the compatible guarded arrangement to remaining incompatible under 056's complete execution bound. Equally costly matched delegates can tie as implementations.

Before calibration, current productive utility exceeds the combat upper bound. After calibration and before observation, remaining finished stock is 133/100 per participant, and combat has total frontier at most 266/100. Productive expected current base utility is (1+lambda_i)U_(3,3,0)>(1+lambda_i)log4, whereas any combat allocation has base at most (1+lambda_i)log(366/100). The contribution reward has then already been earned and cancels. After the output signal, every holding is at least 133/100, above the entire residual recovery bound 4/11. The single-batch schedule supplies these checks rather than deleting later attacks.

The same attestation, no-earlier-observed-commitment, physical preservation and finite-library premises as 049 apply. Goal change is evaluated with the original logarithmic criterion before activation; current G governs later choices. This gives an integrated constructive case with two risk-averse founders, finite positive costs, a common shock and meaningful retained combat capability.

## 4. Renegotiating the active plan enlarges the correlation region

Write g_m(rho)=U_(3,m,0)(rho,1/100)-log4. The relevant approximate endpoint values are:

| Active compartments | g_m(0), independent signals | g_m(1), common signal |
| --- | ---: | ---: |
| 1 | -0.00380761 | -0.00380761 |
| 2 | 0.00940913 | -0.02549789 |
| 3 | 0.02181427 | -0.08198319 |

Their exact values are the finite log sums above; every curve is affine between its endpoints. Let

\[
\rho_s=\frac{g_3(0)-g_2(0)}{[g_3(0)-g_3(1)]-[g_2(0)-g_2(1)]}
\simeq0.180071,
\quad
\rho_e=\frac{g_2(0)}{g_2(0)-g_2(1)}\simeq0.269548.
\]

The optimal positive-welfare plan uses all three compartments below rho_s and two between rho_s and rho_e. At rho_s they tie. Above rho_e this guarded package's implementation cost and available production plans fail to improve both original utilities over retention; retention is peaceful. The fixed full-three plan alone loses its adoption gain earlier, at about rho=0.210162. Thus adapting the agreement preserves strict original gains over a larger correlation interval.

To check that no omitted profile raises this envelope, first remove solitary contributions. In the independent branch a solitary contribution has negative expected total output and lowers conditional expected log welfare by Jensen. In the common branch its positive output occurs only in the states with the largest output from the other compartments. Concavity bounds its welfare increment by f'(Z) times its material increment L; because f'(Z) is smallest when L is positive, this expectation is at most f'(Z_high)E L<0. Removing the solitary contribution strictly improves the statewise-optimal welfare bound. It remains to compare the finite joint-plan curves for N<=3. All N=1 or N=2 curves, and the single-active N=3 curve, lie below retention at both endpoints; affine dependence keeps them below throughout. The two displayed positive curves then give the asserted envelope until retention takes over. Their pairwise crossings and signs can be bounded by the same rational logarithm routine.

This is a boundary for the stated positive-cost guarded package. Cheaper compatible delegates, lower installation costs, a different partition capacity or additional counterparties can shift it. In particular, reducing installation cost can make even a single small active compartment attractive at every rho, because a one-compartment outcome has no remaining cross-compartment correlation penalty. Those are feasible directions for constructive repair; the interval above is not an impossibility theorem over all richer technologies.

## 5. Ordinary hidden-effort controls and flexibility

The ordinary allocator receives the full vector of compartment signals and may use finite-collateral transfers, private recommendations and lotteries. At the full-three welfare maximum, strict concavity forces equal allocation in every output state and the physical optimum forces every contribution. Secretly omitting one calibration while retaining that transfer rule increases an original agent's log utility by more than 0.0286 in the witness. The exact routine checks the changed signal law and the full saved own calibration cost. Since the independent branch has positive weight, every output vector has positive probability under full effort; there is no unconstrained zero-probability transfer state that repairs this deviation.

Compactness therefore gives a strict ordinary welfare gap at the same dated frontier. Better observation or a binding effort delegate can close the implementation gap and must receive its actual costs. Diversification repairs the risky opportunity; a credible contribution mechanism repairs its hidden-effort incentives. These are separate enabling changes.

The active-plan predicate permits agents to replace three tasks by two without rewriting an archived utility or treating a private claim of compliance as performance. Joint registration and current-goal acceptance remain required. The efficient continuation and protected floor are dated to the actual plan, physical state and information. This is flexibility within a declared implementable language, with future expansions still available for investigation.
