# Who checks the person selling the inspection?

A future sale gives an inspector a reason to issue a favorable report. Two things can discipline that incentive. Someone can reserve a sample which will settle how accurate the report was, and the customer can hire a tester whose income is independent of the sale. Both cost resources. Even a highly accurate tester can prefer to skip the test when genuine installations are common.

## What a paid inspector has to gain by looking

Use the [commissioning game](206-when-a-truthful-attempt-can-fail.md). A owns the processing window, B owns the batch and C can read a local instrument before release. Its signal has sensitivity t and false-positive probability e. A's genuine installation rate π is determined by its private choice. C earns a fixed fee w and b units of actual margin on a consumable used whenever B releases a batch. B's stated production payoffs are net of that consumable. The meter costs C an additional c per use. It can instead report without taking a reading. The contract claims that the reported sign is the reading of the meter.

An independent reference becomes available *after* release or return, with probability α, including on rejected orders. It identifies the active state at handover with symmetric accuracy ℓ>1/2, independently of the first error conditional on that state. When the reports disagree, C forfeits a funded deposit F to B. A unit of forfeited stock has constant value to each party. C's deposit is in custody beyond the control of the contest over the batch. At signing B can choose the service for this batch before A invests. Suppose B releases on a positive and declines on a negative. At genuine probability p the inspector gains b+D(2p−1) by reporting positive instead of negative, where D=αF(2ℓ−1). Write P₊=πt+(1−π)e and P₋=1−P₊. A paid reading and truthful report of both signs strictly maximize C's return precisely when

    c < min{ bP₊ + D[πt−(1−π)e],
             D[(1−π)(1−e)−π(1−t)] − bP₋ }.                         (237.1)

The first term is the improvement over always reporting negative. The second is the improvement over always reporting positive. Their strict positivity also makes reporting each observed sign optimal after the expense is sunk. Interchanging the signs cannot improve on these policies because t>e. At equality C may mix. The reference has to survive a rejection. An outcome measured only for shipped batches would give C a different set of incentives.

## A stronger buyer can induce more honest installations than its inspector will check

Let (t,e,q,K)=(.9,.1,.8,1.4) as before. Set α=.25, ℓ=.9, F=5, b=.5, c=.05 and w=.08. The stand locks .1 of C's working resources. B pays .3 to use an available reference, after it has received C's report. In all three outcomes below any posterior puts the mismatch probability at least .1, so the recoverable fine is worth at least .5. B strictly takes every available reference. Inspections are feasible even on a contested return because a contemporaneous reading has already been reserved separately. A and B retain the finite-cost contest over the actual goods.

With equal recovery strength and π=.64, C's advantage from reading over always reporting positive before the .05 cost is .26−.5×.388=.066. It buys the reading. Original A's cost cutoff is 1.12, giving the stated π. B wants a positive batch and returns a negative. C's net income is .011 and B gains 2.302 per offer over return, including expected fine revenue. B buys the service. Risk-neutral founders consent, and installers with k<1.12 pay for the real change.

Now give B an .8 chance of recovering the contested line as in [207](207-who-can-walk-away-from-a-doubtful-installation.md). B will contest a declined batch. With a genuine readout under B's own control every supplier would try; π=.8. At that prior a financially interested inspector saves expense and earns more on sales by routinely reporting positive. The candidate in which it always checks fails at C's own decision.

There is an assessment in which C actually checks with probability x and otherwise claims a positive reading. C's gross gain from checking over always passing is .45−.6π. Setting this equal to .05 gives π=2/3; the other term in (237.1) strictly exceeds .05. For A, a genuine installation rather than a retained controller gains 2.52 under checking and loses 2 under untested release. The uniform cost distribution then gives

    x = [Kπ/q² + 2]/[2.52+2] = 2075/2712.

Conditional on genuine and retained controllers respectively, B receives a positive with probabilities 1−.1x and 1−.9x. Its posteriors are 10018/11707 after a positive and 2/11 after a negative. Its release threshold is .4. This checks its two sequential choices. All applicants sign. Five in six attempt the change, two in three succeed, one in six fails honestly and one in six deliberately skips. C reports a reading that it never took on about 23.5% of all orders, including many genuinely changed ones. The event that an inspector invented a reading differs from the event that the installer lied.

| Selected service at strength .8 | Genuine per offer | Combat per offer | B's gain | Original A's mean gain | Inspector's net gain |
| --- | ---: | ---: | ---: | ---: | ---: |
| Tester also supplies the consumable | 2/3 | 4565/16272 | 2.0921 | 2.1676 | .0217 |
| Independent tester, commissioned in advance | .8 | .26 | 2.2140 | 1.8560 | .0050 |

The independent tester has b=0, the same meter and deposit, a .38 fee, and B must also pay .10 to commission the separate stand. At π=.8 its gross benefit over always passing is .10, enough to pay .05. B therefore buys this option if it has the procurement right before A invests and the displayed positive equilibria are selected. A still earns more than refusal but some suppliers would pay to retain the old arrangement. If B could cancel its independent testing contract after A invests and recover the prepaid expenses, the procurement incentive would have to be checked again.

For the table, with a test probability x and induced π put T=1−.1x, E=1−.9x, and j=π(1−T)+(1−π)E. The expected fine is αF[(1−ℓ)+(2ℓ−1)j]. B's gain is πTg−(1−π)Eh plus the fine, less w, .3α and any commissioning cost. C earns w+b[πT+(1−π)E] less cx, the locking cost and the fine. Original A's gain is E(a+d−A_N) plus the expected positive part of its attempt premium over its private cost. This also checks who actually gains when B separates testing from sales.

**Why these roles could arise.** The equipment vendor may be the party with the cheapest access to a plant, and can earn a real margin from further production. Independent inspection, paid backchecks and accuracy-dependent compensation have an institutional precedent in the Gujarat environmental-audit experiment, whose researchers funded a bundled reform. Its measurements concerned pollution. E9 assumes substantially more about the link from two physical readings to a terminal goal. A poor inspector may be unable to post F; an interested buyer with discretion to manufacture discrepancies could also undermine participation. Mutual control of a contemporaneous sample or a second independent custodian are priced repairs to investigate. A supplier able to pay the inspector privately poses a different question, taken up in the next note. [Primary comparison L98](../LITERATURE.md)
