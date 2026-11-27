# 275 — Can the parties show which goal is installed without exposing a physical weakness?

An applicant can want its partner to know the promised goal is genuine and want to keep the state of its recovery machinery private. [231](231-when-proving-a-goal-also-reveals-who-would-win.md) prices a narrow and a broad inspection. This note asks whether a narrow report can actually be constructed from a given instrument, how much useful evidence survives, and why two founders might pay to receive it.

## The evidence a finite instrument can keep private

Fix the true evaluator g∈{G,N} and physical condition s∈{V,H}, with V a supplier vulnerable in a contest and H harder for the buyer to displace. A known row K_gs lists the probabilities of the instrument's raw readings. A custodian sees x and issues a pass with probability r_x∈[0,1]. The raw result is inaccessible to the buyer until after the job. Require the distribution of the pass to be identical across the two physical conditions *at each fixed goal*. Put d_G=K_GV−K_GH, d_N=K_NV−K_NH, v=K_GH−K_NH. Then the requirements are

    d_G·r=d_N·r=0,            t−e=v·r.

Let D have rows d_G,d_N. An informative protected result exists precisely when v lies outside the row span of D. If v is inside it every feasible difference vanishes. Otherwise choose a direction in its null space with positive v product, then add a small multiple of it to the constant .5 certificate. This keeps every entry between zero and one. The exact maximum attainable discrimination is

    max_{0≤r≤1, Dr=0} v·r
       = min_λ (1/2) ||v−Dᵀλ||₁.                                  (275.1)

For a fixed multiplier λ the maximum over the box is the sum of the positive entries of v−Dᵀλ. The entries sum to zero. Finite linear-program duality gives equality since the feasible box contains the constant rule and the objective is bounded. Larger output alphabets can be tested one recommendation at a time. If their distribution varies with the goal, some event in it supplies an informative binary certificate. The existence result has a direct geometric interpretation. What distinguishes the goals must contain a component that the two strength effects cannot reproduce. How large the surviving difference must be is determined by the actual participants' payoffs.

In a binary instrument with raw pass probabilities (.95,.55,.45,.05) for (GV,GH,NV,NH), the strength effect on every processed pass is .4(r₊−r₋) while the goal effect within either condition is .5(r₊−r₋). Requiring a goal difference of .40 necessarily exposes a strength difference of .32. An additional independent reference, less damaging timing of disclosure, physical separation of the two systems, or payment for a peaceful settlement can change what is feasible. Removing some fields from a readout is sufficient only if its remaining distribution has the required property.

## A custodian that actually wins the job

Use 231's outputs: returning gives Red 5.5 and Blue two; a genuine delivery gives (6,4) and retention gives (8,0). A destructive contest yields expected blue recovery 5.4 against V and .6 against H, with the complementary red share of six recovered units. The target x+.75y strictly delivers, and both possible red controllers prefer an offered peaceful return to initiating a dispute. At enrollment neither side yet knows whether Red is vulnerable (probability .20). This condition is independent of an attempted edit's success (probability .80). A real attempt costs .10 red units. Signing precedes both draws. Four possible meter marks have these laws:

| State | First mark | Second | Third | Fourth |
| --- | ---: | ---: | ---: | ---: |
| G, vulnerable | .85 | .05 | .09 | .01 |
| G, hard to displace | .05 | .85 | .01 | .09 |
| N, vulnerable | .09 | .01 | .85 | .05 |
| N, hard to displace | .01 | .09 | .05 | .85 |

Here Dr=0 requires r₁=r₂ and r₃=r₄. Thus the largest protected goal difference is .8; passing the first two marks achieves t=.9 and e=.1. The pre-change founder's gain before its private edit expense is .8[.9(.5)−.1(2.5)]=.16, so it strictly tries. The buyer's chance of vulnerability remains .20 after either coarsened result. Its contest is worth 1.56 against a peaceful return of two. It releases a pass and returns a failure, giving 3.40 before hardware cost, greater than 3.20 for untested trust. Red receives 5.81 net even after its expense, versus 5.50 for refusing. Blue can pay .10 for independently held filtering and still prefer it. Eight in ten actual goals change. Each party retains the physical capability to contest, and all refusals in this arrangement are peaceful.

With a compulsory raw display, marks one and three instead make Blue choose the contest for every possible signer prior p∈[0,.8]. To verify, multiply its gain over release or return by the probability of the mark. The gains are affine in p. At p=0 and .8 each is strictly positive. On mark four the return strictly beats either action at both endpoints. Giving Red the most favorable possible reply of release on mark two therefore bounds its earnings under *any* such enrollment prior. If it tries, those earnings are at most 4.787 after expense; if it skips, at most 4.759. Red prefers its pre-draw refusal of 5.5. At p=.8 hypothetical raw enrollment would give the first mark about 97% genuine probability and 81% vulnerability. Blue wants to fight even though it is almost certain the promise was kept. With a raw bill of .05 its gross 3.6464 on this proposed all-attempt path cannot finance Red's minimum .713 participation shortfall and still match the 3.30 it gets from the protected report. A purchased stand-down bond or more extensive strength-contingent settlement has separate capacity requirements. [A funded settlement on disclosed strength](231-when-proving-a-goal-also-reveals-who-would-win.md)

## Which physical correlations can a certificate hide?

If strength and goal are independently distributed *among enrollees*, hiding strength at fixed g also keeps the receiver's strength belief unchanged. When the two underlying facts are correlated, such a report updates the buyer to Pr(V|report)=u_N+(u_G−u_N)Pr(G|report), where u_g=Pr(V|g) in that applicant pool. For example, if every successful installation has spent its backup reserve and every retained line still has it, V and G coincide. Any evidence that strongly establishes G also establishes V. If the two recovery values are .6 and 5.4, the expected contest then yields .6+4.8p, higher than a release worth 4p. A positive proving the goal cannot itself guarantee a peaceful handover. Replenishing the reserve before disclosure, placing the lot beyond seizure, or paying a credible settlement can change those payoffs. One must recheck who would fund the change and whether applicants enroll before or after learning their type.

A physical commissioning record can contain diagnostics about both the local controller and the equipment that hosts it. A separate custodian needs authority to withhold the raw marks, unforgeable sample identity and a real fee below the participation gains. A supplier that can choose which sample to submit, or a buyer that can cheaply buy the raw read on the side, changes the laws and the later choices. A cheap ordinary router delivering the same goods while disclosing less collateral information can displace an edit; one exposing the same maintenance marks faces the same problem. The conditional-distribution constraint is mathematically akin to equalized odds for a predictor with an auxiliary group label. Here the auxiliary trait determines physical dispute payoffs, the installed group is endogenous, and the parties choose whether the instrument is funded.
