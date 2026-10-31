# R0001 working note: preference domains, evaluator memory and reinitialization

Goal code, the preference it denotes, and the current evaluator's memory need not coincide. This note makes that distinction precise for finite libraries and supplies a finite-state existence argument that allows indefinitely many fresh evaluator epochs. It is a local formalization tool, not a universal equilibrium or peace theorem. The proofs are contributing-agent self-checks; the expected-utility uniqueness and fixed-point machinery are conventional.

## 1. A finite preference library can be checked extensionally

Fix a common finite outcome domain Omega={omega_1,...,omega_m} and the full simplex of lotteries over it. A template c denotes a utility vector u_c on that domain. Two templates represent the same expected-utility ordering exactly when u_d=a u_c+b 1 for some a>0,b in R.

Here is a direct finite proof and witness test. If u_c is constant, all lotteries are indifferent, so u_d must also be constant. Otherwise choose indices l,h at its minimum and maximum. Preservation of their strict ordering requires u_d(h)>u_d(l). For any j, outcome omega_j is u_c-indifferent to the lottery putting probability

$$t_j=\frac{u_c(j)-u_c(l)}{u_c(h)-u_c(l)}$$

on omega_h and the rest on omega_l. Preserving that indifference forces

$$u_d(j)=u_d(l)+t_j[u_d(h)-u_d(l)].$$

These equations give exactly the positive affine relation. Conversely a positive affine relation preserves all expected-utility comparisons. If it fails, either a deterministic pair or an outcome-versus-two-point-lottery comparison witnesses the difference.

The declared lottery domain matters. Equal optimal actions in one production problem do not imply equal preferences; even equal rankings of every deterministic outcome permit a nonlinear recoding that changes lottery preferences. If a model uses a smaller feasible lottery menu, behavioral equivalence on that menu is a different relation. A public verifier's ability to establish an arbitrary program's denotation is not supplied by this finite mathematical test.

For example, an outcome domain containing records with (color,change flag) equal to (0,0),(1,0),(0,1) gives the finite-penalty criterion vectors (0,1,-kappa). Different kappa values are not positive affine representations of one another. But changing the code while multiplying the entire criterion by a positive constant is not a genuine preference change. The events in a finite installation library must be checked against its denotations, rather than counted merely because a code string changed.

To avoid circular definitions, a model can start from raw execution records and a candidate library of functions on them, then verify that its designated preference-change events agree with the induced equivalence classes. A self-referential sentence about “my real utility changing” is not a substitute for this consistency check. This requirement does not impose a globally computable classifier for arbitrary future programs.

## 2. Returning to the same code need not restore an old evaluator

Suppose a criterion F_kappa values a discounted color stream and charges kappa at the **first subsequent** genuine change after its activation. After it changes to another goal, its archived evaluation retains that already-incurred penalty. If the same F_kappa code is later installed with its first-change memory reset, the new evaluator again cares about a future first change. It is not the old evaluator with its penalty already sunk.

A terminal illustration uses kappa=2. At a restored-code decision, Keep gives no further color and Change gives one unit. An archived evaluator whose first penalty is already sunk prefers Change. A freshly activated F_2 prefers Keep, because Change is worth 1-2. Adding a physically available zero-output Attack option does not remove the distinction. This is an evaluator-semantics example, not a calibrated combat model.

Note 018's finite-label theorem remains valid when labels are actual fixed criteria on complete histories. It must not be applied by counting only distinct code templates if reinitialization creates new criteria. Its clause allowing the same label to act after restoration applies when the **same complete-history criterion** really returns. A fresh first-change reference time can violate that condition, even with a finite hardware state space.

The next construction avoids assigning infinitely many archived evaluators simultaneous decision authority. It uses finite virtual memory to evaluate a current epoch's continuation, while later epochs use their own initialized memories.

## 3. Finite-memory stationary current-self existence

Assume a finite public physical/implementation state space S, finitely many controller slots and actions, and finitely many evaluator **parameters** g. The active parameter of each controller is part of the state. Combat, installation, failure, loss of agency and restoration are ordinary actions/transitions, with all physical capabilities still declared.

Each current decision maker chooses its entire simultaneous action tuple as one controller. If one evaluator controls several devices, group those choices before applying the product correspondence; identical goal parameters alone do not merge independent controllers' decision authority.

For every g, specify a finite evaluation-memory space M_g, a discount beta_g in (0,1), a bounded reward r_g(s,m,a,s',m'), and a memory transition kernel together with the physical kernel. For an active controller at s, an initialization map iota_i(s) specifies the memory used by its actual current criterion. The resulting discounted evaluation must equal that criterion's ordering of future histories, up to an irrelevant positive affine transformation. This is a representation assumption, not an assertion that arbitrary history preferences have finite memory.

An evaluator epoch is a tenure with one actual criterion. When it ends, the former evaluator can keep evaluating the outcome, but cannot choose later actions. Reinstallation of the same code may begin a fresh epoch. Impose **within-epoch consistency**: while an epoch remains active, the evolved evaluation memory at its later decision states agrees with the initialization used there for that same criterion. Ending an epoch does not reset the archived evaluator's memory. The memory used by its successor is initialized separately.

For the first-change example, each virtual evaluator has a bit recording whether its epoch has ended. The old evaluator charges its penalty on the first 0-to-1 transition and leaves the bit at one forever, including when the physical code returns. A fresh F_kappa evaluator starts a separate calculation with bit zero. Its color rewards continue after losing authority. The two calculations can use the same finite physical states without conflating their criteria.

**Result.** This finite public discounted class has a stationary profile with no profitable one-step deviation by any current evaluator. Under the stated within-epoch consistency, it also has no profitable history-dependent deviation through one evaluator's remaining tenure, holding later distinct evaluators' strategies fixed.

### Fixed-point proof

Let sigma be a stationary mixed policy on the finite product of controller/state action simplexes. For every g, evaluate it on the finite augmented states (s,m):

$$V_g^\sigma(s,m)=E_{a\sim\sigma(s),s',m'}
[r_g(s,m,a,s',m')+\beta_g V_g^\sigma(s',m')].$$

The right side is a beta_g contraction. Its unique bounded fixed point depends continuously on sigma: the transition/reward entries are continuous finite polynomials in the mixed actions, and either the contraction comparison or the uniformly convergent discounted series establishes continuity.

At an active controller i's state s, put g=g_i(s) and compute its one-step deviation value

$$Q_i^\sigma(s,a_i)=E_{a_{-i}\sim\sigma_{-i}(s),s',m'}
[r_g(s,\iota_i(s),a,s',m')+\beta_g V_g^\sigma(s',m')].$$

Return, for every controller/state pair, all mixed actions supported on the maximizing pure actions. Because the action sets are finite and Q is continuous, this correspondence has a closed graph and nonempty compact convex values. Its domain is a compact convex product of simplexes. Kakutani's theorem gives a fixed point sigma*. At that point each current controller's action is optimal for its own current evaluation, taking all later policies as specified. This proves the one-step statement.

For the stronger tenure statement, follow one current evaluator while its epoch remains active. Its one-step Bellman inequalities hold at each later decision because of within-epoch consistency. At states where others decide, use their fixed sigma* policies. After the epoch ends, its archived continuation follows those later evaluators' sigma* policies and retains its own evaluation memory. Iterating the inequalities along any unilateral tenure deviation bounds its value by V_g^{sigma*}; the remaining discounted tail tends to zero because rewards are bounded and beta_g<1. This also handles an epoch that never ends. No old evaluator is allowed to change a successor's strategy merely by calling that a longer unilateral deviation.

This is a finite-memory specialization of standard discounted-policy and fixed-point reasoning, related to the inspected L18 machinery. It does not assert literature priority. Private observations, unbounded memories, arbitrary utility programs, undiscounted criteria or infinitely many policy states need other arguments. Existence says nothing about peaceful selection or convergence of goal parameters.

## 4. A recurrent example where charging every future self's penalty is wrong

Consider public modes F and H, discount beta=1/2 and renewable net color flows. In F, Stay gives color c=1 and remains F; Switch gives color b=12/5 and activates H. The current F criterion charges kappa=1 at its first subsequent change. In H, Return gives no immediate color and installs a fresh F; Keep gives zero and remains H. H values color alone. Attack is available in both modes and terminates with zero further color under the declared local comparison. Positive ongoing flows require a renewal supply and the specified mode-dependent opportunity menu; they are not a closed-stock physical theorem.

H strictly prefers Return whenever F supplies positive future color. There are two strict F continuations:

- If F always stays, its color and current-criterion value is c/(1-beta)=2. A one-step Switch is worth b-kappa+beta^2*2=19/10<2. Thus Stay/Return is a stationary current-self equilibrium.
- If every fresh F switches, the color-only continuation at F is b/(1-beta^2)=16/5. A current F charges its own first penalty once, so its value is 16/5-1=11/5. Delaying one period gives c+beta*(11/5)=21/10<11/5. Thus Switch/Return is another stationary current-self equilibrium. Each newly activated F voluntarily pays its own penalty, while an older archived F does not adopt all later selves' penalties as its own.

Attack is strictly worse at either continuation. The within-epoch argument rules out repeated delays as well as a single delay. The second equilibrium changes goals indefinitely; the first keeps the F goal indefinitely. Neither equilibrium is selected by the existence proof.

There is also a mixed stationary equilibrium: a fresh/unchanged F switches with probability p=1/4 at each F decision. Under a candidate p and H returning, the color-only F value is

$$V_{color}(p)=\frac{1+(7/5)p}{1/2+p/4}.$$

At p=1/4 it is 12/5. The expected discounted first-change indicator is p/[1-(1/2)(1-p)]=2/5, so current F's criterion value is 12/5-2/5=2. Stay and Switch both give that value. More generally their difference has the sign of p-1/4, so the two pure profiles and this mixed profile are the three stationary equilibria in the stated menu. This does not classify arbitrary history-dependent equilibria.

If one instead charges kappa at **every** future F-to-H switch to a single persistent evaluator, the cyclic value is (b-kappa)/(1-beta^2)=28/15. A one-period delay gives 1+(1/2)(28/15)=29/15, so that cyclic policy is no longer optimal. This is a different utility, not an alternative computation of the first-change criterion. Conversely, reusing an archived bit that is already one would omit a fresh evaluator's own penalty. Both shortcuts erase a substantive preference distinction.

The example is a formal decision-self control with explicit renewed payoffs. A full E2 use must give its flows and mode-dependent opportunities physical and strategic foundations and compare fixed-utility commitments. It is not inserted into note 019's one-batch population process or note 022's absorbing first-change problem, whose objective domains and renewal meanings differ.
