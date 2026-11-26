# 264 — When buyers can recheck whichever receipts they doubt

The buyer sees a free process receipt P, then may spend c on a live goal reading Z **after seeing P**. This is a repair to the fixed-display assumption in [263](263-when-suppressing-a-second-read-makes-both-founders-better-off.md). It changes which physical sample is worth checking and admits three different rates of voluntary change at the very same cost. Both readings have the same laws and the two factories have exactly the same material stakes as before.

Let f denote the attempt fraction. On the positive operating branches on which a process pass would justify unaudited release, the chances of the agreed goal after a process pass and failure are

    p₊=36f/(5+40f),             p₋=4f/(45−40f).

A live reading converts a pass into a refusal on Z−, saving 1.8−2.2p₊ in conditional expectation. On a failed process receipt a good goal reading can justify release instead. The corresponding gain from the option to read is max(0,3.8p₋−.2). Define

    H(f)=9(5−4f)/[25(8f+1)],       J(f)=(116f−45)/[25(9−8f)].

H is the first gain, decreasing in f; J is the signed second gain, increasing in f. With increasing trust in the commissioning process it becomes more valuable to rescue falsely rejected units and less valuable to catch bad passes. The two gains coincide at f=9/16 and price c=9/50.

Let x and y be the probability of buying a consequential live reading after a pass and a failure. They are one if the corresponding gain exceeds c, zero if below, and can mix at equality. On these branches the buyer releases a passed receipt without a further reading and declines a failed one without a further reading. Following a purchased test, it acts on Z. The founder cutoff must therefore satisfy

    3f = 1.76−.432x−.208y.                                        (264.1)

Testing a pass mainly removes orders from honest failed attempts. Testing a failure admits enough deceptive suppliers with a lucky goal reading to reduce the incentive to try. For instance, the incremental weights on (P+Z+,P+Z−,P−Z+,P−Z−) are (1.328,.432,−.208,−3.152) from (262.1). No recommendation or test use from these readings can produce a cutoff above 1.76. This supplies a global upper bound f≤44/75 even before imposing buyer incentives.

## All the equilibria in which a process pass alone would strictly justify release

Put L=45/116, A=166/375, E=44/75. Here J(L)=0, J(A)≈.04653, H(A)≈.25600 and J(E)≈.21412. The following branches include their endpoints, identifying coincident branches there.

| Range of c | Attempt rate and buyer behavior |
| --- | --- |
| 0≤c≤J(A) | f=J⁻¹(c), x=1, y=(1.328−3f)/.208. At zero cost y is the effective acceptance of a marginal failed-receipt/positive-goal result. |
| J(A)≤c≤H(A) | f=A, x=1, y=0. All passed receipts get checked and all failed receipts are declined. |
| .18≤c≤H(A) | f=H⁻¹(c), y=0, x=(1.76−3f)/.432. The buyer sometimes checks a pass. |
| .18≤c≤J(E) | f=J⁻¹(c), x=0, y=(1.76−3f)/.208. The buyer sometimes rechecks a failure. |
| c≥J(E) | f=E, x=y=0. A process pass gets the order. |
| c=.18 | At f=9/16 every pair (x,y) in the unit square satisfying (264.1) is a best response. |

**Exhaustion on the stated scope.** A process pass alone strictly warrants release when f>5/68. For 5/68<f<L, no goal reading after a process failure can warrant release. A passed process receipt either gets the order directly or at least releases P+Z+. Either gives f≥A>L by (264.1) with y=0. Hence any equilibrium on the stated scope has L≤f≤E. Throughout this interval, a bought Z− is strictly declined and a bought Z+ is accepted, with the indicated tie at f=L on a failed process receipt. An unpaid process failure is always declined. The pretest replies used above therefore exhaust the choices. With x=1 the viable rates run from L to A, first along J(f)=c, then at A. For 0<x<1, c=H(f). Taking y=1 would force f≤194/375<9/16, where J(f)<H(f), so the buyer would decline to check a failure. Taking y=0 instead requires f≤9/16. With x=0, y can mix on J(f)=c only at f≥9/16 and can reach zero at E. The corner x=0,y=1 would require H≤J at f=194/375. Both interior probabilities require the single crossing H=J. These cases give the rows. If no one expects trade, refusing and skipping remain possible. The enumeration concerns the stated productive branches.

At c=.20 there are three such rates. Checking every pass gives an actual agreed-goal rate .3541 and confidence .955 among releases. Checking some passes gives .4211 and .804. Rechecking some failures gives .4615 and .735. The buyer gains 1.0295, 1.2316 and 1.3692 respectively after reading costs. A high-confidence collection of accepted suppliers can therefore come from a market in which a *smaller* fraction of founders installed the agreed goal. All three arise from sequentially rational choices with the same technology and material preferences. Which set of expectations would prevail is a further question.

## Would the buyer pay to change its own future opportunities?

At c=.05 the only branch with a valuable bare pass checks every pass and gives the buyer 1.0976 net. Suppose a different sample-custody route costs .15 upfront per job and increases the physical cost of any early read to .26. The buyer at each future node retains the right to buy that read. At .26 the only branch in the displayed class uses the process result alone. The buyer gets 1.3957−.15=1.2457. Even suppliers that never try gain, since their chance of a released order rises from .01 to .10. The private attempt cutoff rises from 1.328 to 1.76, so all other incumbent types also gain. Faithful installation rises from .3541 to .4693. The buyer commissions the route while retaining the right to return goods and physically contest them at every live decision. With equal strengths safe return keeps all refusals peaceful.

Physical distance from a sample archive, a longer turnaround time or an independent custodian with an opportunity cost can make an immediate read more expensive. A fee the buyer can quietly waive cannot sustain the indicated cost. A forced regulator's fee and an institution both incumbents voluntarily buy are different interventions. A consequential new cost of wrong deliveries, correlated readings, a lower supplier work cost or a binding ordinary shipment guarantee changes which branches survive. These formulas give the required timing, material expenses, information and private incentives for one feasible route.
