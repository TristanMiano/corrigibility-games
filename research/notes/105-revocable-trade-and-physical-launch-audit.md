# Revocable trade and a physical launch audit

**R0005 proof and implementation audit.** The first result covers a broad
finite class of ordinary post-entry actions. The later sections identify
additional requirements for connecting it to initial choice and renewal.
Those requirements are not silently supplied by a local incentive proof.

## 1. A finite ordinary-trade bound after workshop entry

Consider a completed-entry state with fixed total cash at most R-h, two
preloaded nontransferable combat consumables, and no new material arrivals
before the cycle ends. Only the supplier can provide the service. Providing
any positive service costs it positive cash/work; the resulting customer
benefit is a dated achievement, not cash the supplier can later seize.
There is no supplier investment technology that turns these remaining
inputs into additional own output during this cycle.

Both agents retain their original linear own-output preferences. Allow any
finite sequence of communication, stopping, divisible voluntary transfers,
partial service, own-material disposal and physically available combat.
There is no action atomically exchanging payment for service or enforcing
a later transfer: such a device is a separately priced ordinary control.
Promised transfers remain freely revisable. No later reputation payoff or
external arrival is attached to the terminal history in this subgame.

Let C be an upper bound on the supplier's expected cash from any combat
continuation. Suppose the customer's expected combat cash is always below
its retained preloaded holding a_j. The convenient physical bounds are

    C=p_i(R-h-a_i-a_j),
    (1-p_i)(R-h-a_i-a_j)<a_j.                        (1)

Let u denote the supplier's current unencumbered cash, after any unavoidable
expenses. Every subgame-perfect continuation in this class gives the
supplier at most

    max(u,C).                                        (2)

Moreover, if u>C, its continuation payoff is u, no positive service is
performed and the customer makes no positive transfer. This stronger
statement is needed for the induction, rather than assuming that an
unmodified promise is ineffective.

**Proof by backward induction on the finite remaining actions.** At a
terminal node the statements hold. At a supplier decision, attack gives
at most C, stopping gives u, and a positive service, outgoing transfer or
disposal reduces u without raising the bound C. The induction hypothesis
then bounds the resulting payoff by max(u-cost,C), strictly below u if
u>C. Messages or delay cannot improve the bound. At a customer decision,
an attack gives the supplier at most C; disposal or a zero transfer leaves
u unchanged. Consider a positive transfer r with u+r>max(u,C). The
following state is in the rich region, where the induction hypothesis
implies no future service or profitable attack and payoff u+r to the
supplier. If u>C, replacing r by zero yields that same peaceful future
and saves the customer r. If u<=C, a smaller transfer r' satisfying
C<u+r'<u+r yields the same peaceful, service-free future and saves
r-r'. Divisibility supplies r'. Thus such a transfer is not optimal.
The remaining transfers keep the supplier below the claimed bound.
The rich-region conclusion follows at the same induction step. QED.

Histories may carry messages or promised prices, but those labels cannot
physically require an otherwise irrational later action. If a payment
activates enforceable execution, creates additional own productive capacity,
or transfers a new binding right, that is a different physical action and
must be included as a control rather than hidden in the transfer symbol.
Continuous transfer choice is material to the proof: a coarse indivisible
payment can leave a strictly positive excess above a coercive threshold.
Finite payment-grid experiments are not exact proofs of (2).

## 2. Arbitrary prepayment does not evade this particular bound

Suppose the parties can choose an entry advance, with total entry expenses
h paid before service is technologically available. Let u be the resulting
supplier cash. If u<=C, (2) bounds its later payoff by C. If u>C,
the rich-region result supplies no service and the parties divide at most
R-h in cash. Initial customer participation at reservation d_j then
bounds the supplier by R-h-d_j. Therefore every initially acceptable
ordinary arrangement in this class has supplier payoff at most

    max{C,R-h-d_j}.                                  (3)

In 100's physical data, C=117/40 and R-h-d_j=22/5. Both are below
the supplier's original duel holding 9/2. A genuine contractual goal can
instead select partial service at the physical opportunity frontier, while
a binding funded bond or delegate can implement the same outcome at its
actual cost. This establishes a meaningful ordinary-policy comparison;
it does not cover every conceivable workshop or execution technology.

## 3. Setup should not silently weaken the other party's reservation

The original fixture pays setup from capturable workshop stock. A supplier
that later makes the best continuous take-it-or-leave-it offer can then
exploit the decrease in the customer's combat alternative. Anticipating
this, the customer may prefer to attack before setup. A strict-interior
agreed quote avoids the payoff problem only if its prior terms survive
the actual activation procedure. Note 101 therefore left launch conditional.

A physical repair is to pay setup from dedicated controller work which
could have produced the supplier's own dated output but is not capturable
by the customer's workshop within this cycle. This is an explicit separate
stock/location, not erased energy or a universal assumption of protected
resources. The off-site controller is already distinct from the workshop
actuator in 098. Its battery expends useful work as heat during setup and
the supplier loses the corresponding original project achievement.

Setup may have multiple positive-time stages and interruption checkpoints.
Give the workshop enough deadline slack that these stages do not change
the work-limited combat prize Y. For the numerical recovery problem,
recovering two units takes two time units while the initial deadline is
three; setup duration strictly below the remaining slack preserves Y=6.
The dedicated battery is not part of the combat recovery-work budget.

Now setup reduces the supplier's own original welfare by K but preserves
the customer's entry guarantee d_j. If the implemented service frontier
gives supplier r_0, then r_0-K>d_i makes starting the update worthwhile.
At an intermediate stage with smaller remaining cost, completing it is
also preferable to its original duel, with the already spent cost common
to both choices. The customer can wait for a quote giving at least d_j;
a strict quote gives strict preference to waiting, and a reservation quote
requires an explicit acceptance/waiting tie. This repairs one source of
preemption rather than proving every staged implementation automatically.

With the displayed data, the continuous optimum has e*=1/8 and
r_0=191/40. Thus K<11/40 makes installation preferable to the original
duel. K=1/10 gives 187/40, as before. Local workshop cash differs from
the earlier setup-funded fixture, because the setup stock is separate;
post-entry attack bounds must use the larger remaining workshop stock.
The generous bound (1), which did not subtract setup, already covers it.

## 4. Funded acceptance, withdrawal and deliberate resource loss

A useful launch implementation must distinguish a real funded acceptance
from a cheap utterance that binds only the supplier. If a mere acceptance
activates an unconditional customer floor, the customer can accept, refuse
payment and exploit the supplier's concern about its outcome. Conversely,
activating the floor only after fees have irreversibly been spent can leave
an interval for supplier repricing. Both are actual failed candidate timings.

One candidate physical interface is a funded, irrevocable dispatch under
the publicly recorded offer. The full payment is committed to a one-way
route before the customer's carriage expense is consumed; the supplier's
accepted-outcome rule recognizes that funded event. Transit has positive
duration, can be interrupted by combat and consumes the stated resources.
The customer cannot quietly withdraw the payment after consuming fees;
an actual raid is evaluated with the same combat kernel. The promise
refers to the accepted offer even if the supplier later rewrites its goal.
This requires a real irreversible payment route and sound finite-template
recognition. It is not arbitrary semantic verification or a costless
commitment supplied only to the goal-change option.

There is also a consequential ordinary repair to test: the customer can
deliberately destroy or move loot before buying off the supplier. If that
operation completes before attack is possible, it can lower the supplier's
reservation enough to make ordinary peace attractive. For example, removing
18/5 from the available cash leaves a fully recoverable prize at most
22/5. Under the actual half-dispersion, two-unit recovery limit, the
prize is at most 21/5. After also paying the supplier's 1/2 entry expense,
a transfer of 9/5 leaves the supplier 33/10 and the customer 13/5.
Both exceed their reduced-state duel values, at most 63/20 and 21/20.
This is a changed disagreement state, not the original 9/2,3/2.

If disposal has an observable positive-duration preparation stage and the
supplier can attack before capturable stock is consumed, the supplier can
preempt an attempted reduction below its original profitable duel. The
customer then cannot treat the completed burn as a guaranteed outside
option. Which timing is physically available is decisive. A hidden fast
burn, a remote safe transfer or a binding destructive controller requires
its own comparison; a public slow burn with an attack checkpoint supplies
the constructive preemption boundary. The present model does not declare
every disposal technology slow by definition of rationality.

## 5. What the renewal comparison can now use

When these entry/continuation conditions hold independently each cycle,
the original duel gives d_i per cycle and the implemented productive
frontier gives r_0. A reusable genuine goal with setup K_G and recurring
expense mu_G has value A_n(r_0-mu_G)-K_G. A reusable ordinary device m
has value A_n(r_0-mu_m)-K_m. Compare these with A_n d_i and every actual
alternative partner or method. In the equal-recurring-cost specialization,
genuine adoption beats combat and all such devices when

    K_G < A_n(r_0-d_i),       K_G < min_m K_m.         (4)

Equality with an otherwise equivalent device permits optimal genuine
adoption. A cheaper device diverts the cooperative gain to ordinary
execution. A higher combat or ordinary outside option narrows the first
comparison. This is a conditional integrated result with an explicitly
larger ordinary action class, not a proof over unrestricted physical
programs or arbitrary multi-agent threats.

History-dependent reputation, investments linking successive resource
stocks, future goal installations, customer threat goals and new partner
entry can alter the no-update continuation value. Use the actual Bellman
comparison in 103 when its common-state assumptions apply; otherwise those
links require a new dynamic game. Summing the one-cycle bound while
silently excluding such continuations would overstate the result.
