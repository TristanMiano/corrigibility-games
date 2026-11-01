# R0002 extension: coalition incentives and chosen work reserves

**Working extension; module assumptions remain explicit.** The two-agent guarded certificate has a simple coalition analogue. This note tests both the extra demand created by coordinated combat and a physical repair that agents can choose before threats arrive. It is a conditional module result, not a theorem about arbitrary coalition formation.

## 1. A coalition certificate

Let n original agents value their own final project quantities. A compatible productive continuation has mean allocation q, total T=sum(q_i), and is physically efficient after its implementation costs. Each compatible current controller preserves the same productive continuation and accepts only alternatives maintaining its own original-output floor. For example, the saturated reward certificate supports a goal

\[
G_i=(1-\lambda_i)X_i+\lambda_i\sum_jX_j+\beta_i e_i-K_iI_i,
\quad 0\le\lambda_i<1,
\]

when the continuation maximizes expected total output and attains e_i=1. The finite unsafe-approval penalty and implementation qualifications are those in 046.

For each proper coalition S, assume that an incompatible coalition facing the remaining compatible controllers receives no voluntary productive participation, concessions or authority. Let R_S be its retained finished stock, p_S its maximum probability of winning a joint contest against the complement, and W_S the total output recoverable after that contest. Suppose its original summed payoff under every such deviation is at most

\[
v(S)=\max\{R_S,p_SW_S\}.
\]

This bound must include solitary production, resource destruction, internal transfers, alternate attack plans and mixed deviations; it is an assumption until a physical instance supplies it. Internal transfers can help distribute the coalition's payoff but cannot exceed this sum.

If q(S)>=v(S) for every proper coalition, no such coalition can give every member a strict original-goal improvement by becoming incompatible. A compatible deviation cannot do so either: outsiders keep their protected shares, and the assumed total cap over those deviations leaves the coalition at most q(S). This proves the proper-coalition result under the module. At equality the sum argument also excludes weak improvement for all with strict improvement for one; indifference requires separate selection. Grand-coalition initial choice needs a separate cap over all jointly available implementations and their actual costs. Efficiency after paying the displayed guard costs alone does not establish that cap: a cheaper jointly chosen mechanism may improve every founder. No grand-coalition conclusion is asserted here without that additional premise.

This is stronger than an individual best-response comparison and weaker than a complete dynamic coalition-formation theory. It does not identify which coalition forms or eliminate every other initial equilibrium. Approval by already installed guarded selves is a different comparison from coordinated initial choices made under original goals.

## 2. A three-agent threshold

For three symmetric stocks and combat opportunities, write v_1 for each singleton's value and v_2 for each pair's value. An allocation of total T meets every proper-coalition lower bound exactly when

\[
T\ge\max\{3v_1,\tfrac32v_2\}.
\]

Necessity follows by adding the three singleton inequalities and, separately, the three pair inequalities. Sufficiency follows from the equal allocation T/3. This elementary feasibility statement needs no general core-existence theorem.

If coalition win probability is additive in members' individual probabilities and the recovery bound is common, individual combat constraints imply the coalition combat constraints. Complementary military strength can instead make the pair inequalities strictly stronger. That is a specified environment parameter, not an inference about natural coalitions in general.

## 3. A candidate physical instance

Each original stock is 1. Each contribution consumes 3/10 finished units; each installation consumes 1/100. Common feedstock yields 2 units on success, with probabilities 0,1/100,2/100,1/2 for zero through three contributors. The expected net production gains, before installation, are 0,-7/25,-14/25,1/10. The unique total-maximizing profile is full contribution, giving

\[
T=307/100,\qquad q_i=307/300.
\]

Private effort remains available. A contribution reward beta_i=1 makes contribution strict at every other-agent effort profile, even with zero concern for other projects. Suitable positive concern below one preserves the same original-output certificate. Proper coalitions cannot profitably use this reactor alone even when awarded all of its output.

Let initial useful work be B=27/4, with combat leaving 4/5 of that work. Recovery requires two work units per finished unit, so the work-limited recovery frontier is W=(2/5)B=27/10, below the initial finished stock 3. The reactor is damaged beyond the finite episode's repair time, as in 049; the common feedstock cannot be repurposed after combat. Sufficient recovery time is required for equality. The strength kernel for a coordinated coalition of k agents against 3-k is

\[
p_k=\frac{k^2}{k^2+(3-k)^2}.
\]

Thus individual combat value is 27/50<1, whereas pair combat value is 54/25=2.16. Equal productive pair output is 307/150, about 2.047. With a credible internal split and negligible enough coalition-formation costs, both pair members can improve by attacking. Moreover, 3v_2/2=81/25=3.24>T, so no allocation of this productive total meets all pair combat bounds. This is a limit of this unchanged recovery environment; it is not a claim that every renegotiated environment produces combat.

## 4. A repair that preserves useful production

Suppose each participant can dissipate delta of its own excess work during its local preparation, before new remote actions arrive. Dissipation converts useful work to heat; it does not remove conserved energy or the military charge. This is an unconditional physical preparation, not an incredible promise to damage one's own postwar payoff after an attack has become irrevocable.

Against a deviating pair, the remaining guarded participant has already dissipated delta. The pair may avoid its own disposal, so the correct recovery upper bound is (2/5)(B-delta), rather than the lower all-participants-dispose bound. Coalition security requires

\[
\frac45\frac25(B-\delta)\le\frac{2T}{3},
\qquad\text{equivalently}\quad\delta\ge\frac{17}{48}.
\]

Choose delta=2/5. Pair combat value is then at most 254/125=2.032, strictly below 307/150. A singleton facing two compatible agents has an even smaller combat bound. If productive reaction requires 5 work units and all installation, communication, calibration and routing require at most 3/10 additional units, all three disposals leave B-3delta=111/20=5.55, exceeding 5.3. Thus the same productive allocation remains feasible while the coalition combat constraints become strictly satisfied.

This is an open interval of feasible disposal choices, not an equality: the sufficient production bound allows delta<29/60, while coalition deterrence requires delta>17/48. Charge any additional material cost against T before applying the inequalities. A cheaper passive device that prevents combat recovery from using the same excess work is an alternative control if physically available.

The repair requires a certificate of the actual reduced work state, staged preparation completing before incoming attacks, and a complete multi-party collision/authority specification. A full implementation must also check information arriving after solitary production and attacks after successful production. Until those are supplied this numerical extension is a conditional construction, not an audited three-agent equilibrium. Its useful result is the joint threshold: **recoverable work can be reduced enough to remove a coalition's combat gain while retaining the work needed for the cooperative surplus.** Testing that window is a constructive response to the coalition boundary.

## 5. What this adds to the central mechanism

Individual gains from accommodation and coalition security impose different inequalities. Negotiated shares can meet the latter when the total surplus is large enough; chosen physical preparation can lower the required total by changing war recovery without eliminating Attack. Increasing unrestricted useful work can raise war spoils after productive capacity has saturated. Increasing work that is usable for production but unavailable to combat recovery can instead preserve the cooperative margin. These comparisons concern explicitly different physical capabilities.

The original agents choose any disposal and guarded preference package by its original output consequences. Successors then use their current goals. The local guard lemma, coalition sum bound and three-agent feasibility threshold are mathematical results conditional on their displayed modules. The unfinished multi-party implementation remains visible alongside the successful two-agent implementation work, rather than being promoted to long-run population stability.
