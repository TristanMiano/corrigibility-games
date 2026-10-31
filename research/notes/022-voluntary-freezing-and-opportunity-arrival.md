# R0001 working note: voluntary freezing over an indefinite horizon

This note supplies a separate individual-choice analysis alongside note 019's population process. Its optimal-stopping machinery is conventional; the contribution is the explicit current-utility, implementation, and resource interpretation. Proofs are AI self-checked only. Neither survival of a population type nor adoption at one date implies a voluntary long-run theorem.

## 1. What the incumbent evaluates

Until its first genuine preference change, the incumbent uses an expected-utility criterion F_kappa. It values its original color stream with discount delta in (0,1) and subtracts a finite penalty kappa>=0 at the date of that first change. Positive affine recoding, belief revision, and ordinary policy adjustment do not trigger the penalty. The event and the history flag that records it are explicit. Later criteria are those actually installed; the founder's F_kappa evaluation is retained only for welfare reporting.

There is a fixed-utility peaceful baseline giving flow b per period. An available combat route gives no larger incumbent continuation value under the specified physical transition; for example, it gives current flow d<b, consumes additional work, and supplies no better next-state distribution. It remains physically available. This comparison does not infer combat from keeping a utility. In applications where combat improves the continuation distribution, it must enter the Bellman equation rather than be dominated by assumption.

With probability eta in (0,1] each period, an opportunity arrives, independently over periods. Its observed mark G>=0 is the *actual old-utility gain* of its specified successor continuation over the baseline lifetime value b/(1-delta), before the change penalty. Marks are independent and identically distributed with E[G]<infinity. The update is evaluated by G-kappa under F_kappa, not by the successor's numerical approval of its new criterion.

This continuation-value input is conditional on implementation. One witness is a protected merger whose successor persistently allocates an additional physical flow g to the original color, so G=g/(1-delta), under a separately verified current-goal and agency model. Another is immediate delivery of a bounded physical bonus followed by an already specified continuation. The present note does not derive the availability, credibility, or payoff of every such offer from self-knowledge. Costs and failure must already be reflected in G and the next-state law. A stronger fixed-utility delegate that produces the same gain without a change penalty weakly dominates this modification route for the incumbent; its availability must not be suppressed in an application.

The process after the first accepted update is absorbing **for this stopping problem**, not a claim that the universe or successor stops acting. Later choices are already incorporated in the mark's continuation value. The result concerns the time to the first change, not convergence of all future utilities.

## 2. The incumbent's Bellman equation

Subtract the baseline lifetime value. Let v be the optimal excess value before the period's opportunity draw. Keeping the utility and continuing gives delta v. An available update gives G-kappa. Thus

$$v=(1-\eta)\delta v+\eta E[\max\{G-\kappa,\delta v\}].$$

The right side is a delta contraction in v: the maximum is 1-Lipschitz in its second argument, and the two weighted continuation terms have total Lipschitz coefficient at most delta. It maps finite values to finite values because E[G]<infinity. Its unique fixed point is nonnegative, bounded by eta E[G]/(1-delta), and attained by the stationary threshold rule.

Writing t=kappa+delta v gives the equivalent equations

$$ (1-\delta)v=\eta E[(G-t)_+],\qquad
t-\kappa=\frac{\delta\eta}{1-\delta}E[(G-t)_+]. $$

The left side of the second equation strictly increases in t and the right side weakly decreases. Hence t is unique. Choose the update when G>t, keep when G<t, and state a tie convention at atoms. With an atomless mark distribution, ties have zero probability. The Bellman inequality bounds every history-dependent stopping strategy; truncating a strategy and letting the discounted integrable tail vanish verifies optimality. In particular, the current criterion is constant up to the stopping event, so no hidden founder control of a later goal is used.

## 3. Finite freezing can persist forever, or eventually be relaxed

If G<=M almost surely and kappa>M, every update has negative excess value, v=0, and keeping is strictly optimal at every opportunity. The agent continues ordinary peace with its original goal. At kappa=M the same value holds; a zero-gain top atom permits indifferent changes, so universal nonchange requires an explicit tie rule or the strict inequality.

If kappa<M:=ess sup G and delta<1, then Pr(G>kappa)>0, v>0, and t<M. The latter follows because E[(G-t)_+]=0 for t>=M while t-kappa>0. Consequently

$$h=\eta\Pr(G>t)>0$$

is a constant probability of accepting at each still-unmodified period. The first-change time tau, indexed from 0, satisfies

$$\Pr(\tau=n)=(1-h)^n h,\quad
E[\tau]=(1-h)/h,\quad
E[\delta^\tau]=\frac{h}{1-\delta(1-h)}.$$

Thus it changes eventually with probability one in this stationary renewal model, despite a positive finite freezing penalty. The same conclusion holds for every finite kappa when G has unbounded support and finite mean: the threshold is finite and the upper tail remains positive. An unbounded supply of such opportunities is a substantive physical/environmental assumption. It is not supplied by the word “universe.”

These two branches refute both unqualified claims: that finite freezing must disappear given enough calendar time, and that a positive finite penalty necessarily prevents all future change. The relevant boundary is the attainable old-utility gain and the ongoing arrival process.

## 4. An exact bounded example

Let G be uniform on [0,M] and 0<=kappa<M. Put A=M-kappa and

$$\alpha=\frac{\delta\eta}{2M(1-\delta)},\qquad z=M-t.$$

Since E[(G-t)_+]=z^2/(2M), the threshold equation is A-z=alpha z^2. Its positive solution, written without subtracting nearly equal square roots, is

$$z=\frac{2A}{1+\sqrt{1+4\alpha A}},\quad
t=M-z,\quad h=\eta z/M,\quad
v=\frac{\eta z^2}{2M(1-\delta)}.$$

The preceding geometric formulas give exact adoption-time and discounted-adoption distributions. Expected gross old-color gain, before the penalty, is

$$J_{\rm gain}=E[\delta^\tau G_\tau]
=\frac{h}{1-\delta(1-h)}(M-z/2).$$

The equality v=J_gain-kappa E[delta^tau] is an independent accounting check. It separates the welfare of a founder who values color alone from that of the incumbent who also values preserving its criterion.

As delta tends to 1 with M,kappa,eta fixed,

$$h\sim\sqrt{\frac{2\eta(1-\delta)(M-\kappa)}{M}},$$

so the expected waiting time diverges, although eventual change has probability one for every delta<1. The incumbent becomes more selective. Long delay is not a hard inability to modify.

At delta=1, continuous bounded marks supply an existence warning. The supremum of undiscounted excess gain is M-kappa, approached by accepting G>M-epsilon. It is not attained by any almost-surely finite stopping time because G_tau<M almost surely. Never changing gives zero, below that supremum when kappa<M. Thus an optimal stopping rule need not exist at this undiscounted boundary; one must not take the discounted policy's limit and declare it an attained equilibrium.

## 5. Positive opportunities at every date do not suffice

For any process, define h_n=Pr(first change at n | no earlier change), whenever the conditioning event has positive probability. The chain rule, without an independence assumption, gives

$$\Pr(\tau=\infty)=\prod_{n\geq0}(1-h_n).$$

If any h_n=1, eventual change is certain. Otherwise, when all h_n<1, the product is zero exactly when sum_n h_n diverges. To prove the nontrivial direction, if the sum is finite then h_n tends to zero, and for sufficiently large n, -log(1-h_n)<=2h_n; the finite prefix has positive product. If the sum diverges, log(1-h_n)<=-h_n forces zero product.

For example, h_n=2^(-n-2) is positive at every date but has finite sum, leaving positive probability of permanent nonchange. These hazards could result from a declining supply of feasible opportunities; they are not asserted to be the optimal policy for an unspecified physical process. A stationary positive hazard in section 3 is doing real work.

## 6. Resource limits are distinct from voluntary freezing

If a closed modeled system starts with available work B_0, has no replenishment, and every completed genuine goal change irreversibly consumes at least e_min>0 work, then the number N of such changes is at most floor(B_0/e_min). This is a direct resource bound, including all installation attempts that consume the same minimum if applicable. A finite time horizon T_0 and minimum sequential installation duration ell_min>0 independently give N<=floor(T_0/ell_min).

Neither bound proves a preference for freezing: the last agent may simply be unable to execute another change. They also require uniform positive lower bounds. Summable positive work costs alone allow infinitely many changes on an infinite time horizon; a renewable work source invalidates the closed-stock bound. A thermodynamic argument for a uniform e_min would need an actual hardware, temperature, error and logical-operation model; it is not inferred from Shannon entropy.

Similarly, if every feasible successor continuation improves a bounded incumbent physical utility over its best unchanged-utility control by at most B, then a current first-change penalty kappa>B strictly prevents voluntary change. This is an inequality over the whole feasible continuation set, not a parameter sampled from favorable examples. Enlarging the set, changing the old utility, or adding unbounded renewed resources can invalidate the bound.

## 7. Voluntarily choosing a finite future freeze: a conditional menu result

To isolate the founder/successor distinction, consider a designer whose present criterion values only its color stream. It can install one of the future criteria F_kappa, kappa in [0,M]. Suppose the declared counterpart/contract menu supplies the successor's ordinary-peace flow

$$b(\kappa)=b_0+c\kappa,$$

and the same uniform opportunities of section 4, with all setup costs matched. The premium c kappa is a **specified response to public goal type**, not derived from arbitrary opponents. Note 012 gives a separate finite game where a commitment premium is endogenous; the present result only analyzes this reduced menu. A common bounded production capacity at least b_0+cM and the specified bonus-flow capacity is required. It is not a free resource created by preference change.

The offer's gain is measured over that candidate's **entire** baseline continuation. A concrete menu must therefore preserve the already allocated baseline stream after an accepted opportunity, or compensate any loss within G. For example, the initial contract can allocate a protected baseline production asset and the opportunity can add a separate bonus asset. If changing the goal instead forfeits the premium, G depends on kappa and the following formulas must be changed. Renewed material/work supplies sustain these indefinite flows; they are not a closed finite-resource universe.

The designer does not itself charge the successor's future freezing penalty. Its actual value is

$$J(\kappa)=\frac{b_0+c\kappa}{1-\delta}+v_\kappa+\kappa D_\kappa,
\qquad D_\kappa=E[\delta^\tau].$$

For 0<=kappa<M, write a=1-delta, B=delta eta/M and z as above. Then

$$D_\kappa=\frac{\eta z}{M(a+Bz)},\quad
\frac{dz}{d\kappa}=-\frac{a}{a+Bz},\quad
\frac{dD_\kappa}{d\kappa}=-\frac{\eta a^2}{M(a+Bz)^3}.$$

Differentiating the fixed-point expression gives dv_kappa/dkappa=-D_kappa. Therefore

$$J'(\kappa)=\frac{c}{a}-
\frac{\kappa\eta a^2}{M(a+Bz)^3}.$$

As kappa increases, z decreases, so the second term increases strictly. Thus J is strictly concave on [0,M). Its right derivative at 0 is c/a, and its left derivative at M is (c-eta)/a. If 0<c<eta, it has a unique maximizer strictly between 0 and M. The present color-only designer voluntarily chooses a positive finite future freezing penalty, while that successor still eventually changes with probability one under the stationary opportunities. At c=0 the optimum is kappa=0; at c>=eta the endpoint kappa=M maximizes the specified menu, subject to the tie convention at the zero-probability top mark.

This is an exact conditional incentive tradeoff, not a claim that all environments pay a linear commitment premium. If a fixed-utility commitment supplies the same premium and execution while preserving the same future deviations, compare its actual founder value; modification has no automatic advantage. A small genuine initial installation cost preserves a strict interior preference only when it is below the derived gain over the unchanged alternative.

## 8. Early relaxation is a different action and must be checked

Editing F_kappa to F_0 is itself a genuine preference change and incurs the old criterion's penalty. It cannot be treated as a free preparatory operation. Under an unchanged opportunity law and with no increased baseline after relaxation, this early edit cannot improve F_kappa's value over its optimal stopping policy.

Indeed let the relaxed F_0 policy accept at tau_0. Its gross gain is v_0 and D_0=E[delta^tau_0]<=1. F_kappa could use that same stopping rule while keeping its criterion until the actual opportunity, obtaining v_0-kappa D_0, at least v_0-kappa. Its own optimal value v_kappa is at least that much. Early editing instead pays kappa immediately and obtains at most v_0-kappa, with any lost commitment premium making it worse. The argument compares feasible policies and then uses the incumbent's time-consistent Bellman optimum; it does not assume that an inactive founder commands F_0.

This removal test relies on matched future feasible policies and opportunity laws. If removing a freeze changes others' offers, enables a new physical operation, or alters information, the imitation argument fails and the early edit must be evaluated in that enlarged game. Nor does this argument identify different expected-utility preferences merely because their realized policies happen to agree in one state.

## 9. What remains open

The result gives conditional long-run individual behavior, distinct from reproductive transmission. It does not prove that all future preferences converge, that descendants preserve founder welfare, or that the linear commitment premium arises generically. Deriving the opportunity law and premium together from an interruptible repeated bargaining game with endogenous strength and verification remains open. The first-change analysis is useful precisely because its assumptions expose where a claimed inevitable thaw would need additional evidence.
