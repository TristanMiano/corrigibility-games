"""Exact finite assessment for public progress and interruptible response frames.

The script checks the declared finite kernel, not arbitrary communication,
programs, bargaining or escrow. Run: python experiments/r0004_staged_assessment.py
No random seed is used. Fractions and a common leading-term perturbation
check Bayes limits and current-evaluator deviations at every information set.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from math import prod


@dataclass(frozen=True)
class State:
    theta: int
    mode: str = "F"
    time: F = F(0)
    ws: F = F(111, 10)
    wr: F = F(11)
    cs: F = F(0)
    cr: F = F(0)
    h_violation: bool = False


@dataclass
class Node:
    info: tuple | None
    evaluator: int | None
    edges: dict
    base: dict
    exponent: int | dict = 1
    terminal: tuple | None = None
    state_type: int | None = None


def recovery_loss(dispersed, time, work, *, horizon=F(10), war_work=F(1),
                  repair_work=F(1), war_time=F(1), repair_time=F(2),
                  shipping_time=F(1), repair_material=F(1, 1000),
                  omega=F(900), rate=F(1, 100)):
    """Finite repair; declining it is an available physical choice."""
    if (work < war_work+repair_work or
            time+war_time+repair_time+shipping_time > horizon):
        return dispersed
    recoverable = min(dispersed, (work-war_work-repair_work)/omega,
                      rate*(horizon-time-war_time-repair_time-shipping_time))
    return dispersed-max(F(0), recoverable-repair_material)


class StagedTree:
    # Coordinates are losses: original S, C_a, current R_a, original R,
    # followed by actual C activation and combat indicators.
    width = 9  # H_z loss, actual H_z activation, any physical attack attempt.

    def __init__(self, *, p=F(1, 2), b=F(1), a=F(0), f=F(1, 100),
                 costs=(F(3, 20),)*3, requests=(F(1, 300),)*3,
                 strength=F(1, 20), damage_s=F(5), damage_r=F(1, 100),
                 physical=False, delegate_final=None, policies=None,
                 hostile_price=None, hostile_threshold=F(13,50),
                 hostile_value=None,
                 receiver_repair_time=F(2), safe_exit=None,
                 late_cash=None,trade_offset=None,
                 trade_fee_s=F(1,10000),trade_fee_r=F(1,10000),
                 continuous_posteriors=None):
        self.p, self.b, self.a, self.f = p, b, a, f
        self.c, self.r = tuple(costs), tuple(requests)
        self.n = len(self.c)
        assert self.n and len(self.r) == self.n
        self.high_tremble_power = 100+10*self.n
        self.s, self.ds, self.dr = strength, damage_s, damage_r
        self.physical, self.delegate_final = physical, delegate_final
        self.hostile_price, self.hz = hostile_price, hostile_threshold
        self.hostile_value = hostile_value
        if hostile_value is not None:
            assert hostile_price is not None and a < hostile_threshold < 1
            assert strength*hostile_value > (F(5009,1000) if physical else damage_s)
        self.receiver_repair_time = receiver_repair_time
        self.safe_exit = safe_exit
        self.continuous_posteriors = continuous_posteriors
        if continuous_posteriors is not None:
            assert a == 0 and hostile_price is None
            assert len(continuous_posteriors) == self.n
        self.late_cash, self.trade_offset = late_cash, trade_offset
        self.trade_fee_s, self.trade_fee_r = trade_fee_s, trade_fee_r
        self.cash_ell = F(0)
        if late_cash is not None:
            assert hostile_price is None and safe_exit is None
            assert late_cash+trade_fee_s == 2*(b-a)*trade_offset-trade_offset**2
            assert 0 < trade_offset <= (b-a)/2 and a+trade_offset <= 1
            self.cash_ell = trade_offset**2-late_cash+trade_fee_r
            assert self.cash_ell < 0
        if physical:
            assert self.n <= 3, "Combat and shipping must fit the ten-tick kernel."
        self.D = (1-a)**2
        self.g = (1-a)*(2*b-1-a)
        self.h = (1-a)*(2*b+1-a)
        self.policies = tuple(sorted(set(policies or (F(0), a, F(1, 2),
                                                     min(F(1), p+a), F(1)))))
        if hostile_price is not None:
            self.policies = tuple(sorted(set(self.policies+(self.hz,))))
        if continuous_posteriors is not None:
            self.policies = tuple(sorted(set(self.policies+tuple(1-mu for mu in
                                                               continuous_posteriors))))
        assert all(F(0) <= y <= 1 for y in self.policies)
        self.nu, self.ell = F(0), F(0)
        if hostile_price is not None:
            end = State(0, mode="H", time=F(1+2*self.n),
                        ws=F(11-self.n), wr=F(11-self.n))
            action, receiver_loss = self.hostile_response(end)
            gain = (a-b)**2-self.hostile_sender_loss(end)-hostile_price
            if gain > 0:
                self.nu, self.ell = gain, receiver_loss
            assert self.ell < self.D
            assert self.nu < self.g
            for i in range(self.n-1):
                earlier = replace(end, time=F(3+2*i), ws=F(10-i), wr=F(10-i))
                assert ((a-b)**2-self.hostile_sender_loss(earlier)-hostile_price <= 0), \
                    "This assessment requires the profitable threat to occur only at the last frame."
        self.thresholds = [F(0)]*(self.n+1)
        self.request_thresholds = [F(0)]*self.n
        for i in reversed(range(self.n)):
            next_t = self.thresholds[i+1]
            probe_t = (self.r[i]*self.D/(self.D-self.ell) if i == self.n-1 else
                       self.r[i]+(1-self.r[i]/self.D)*next_t)
            if late_cash is not None:
                probe_t = next_t+(self.D-next_t)*self.r[i]/(self.D-self.cash_ell)
            self.request_thresholds[i] = probe_t
            state = State(0, time=F(1+2*i), ws=F(11-i), wr=F(11-i))
            _, dr = self.damage(state)
            self.thresholds[i] = min(probe_t, dr/(1-self.s))
        if continuous_posteriors is not None:
            next_value = F(0)
            next_mu = F(0)
            for i in reversed(range(self.n)):
                mu = continuous_posteriors[i]
                assert next_mu < mu < F(1,2)
                assert self.r[i] == mu*(1-mu-self.cash_ell)-(1-mu)*next_value
                assert mu*(1-self.s-mu) < self.dr
                self.thresholds[i] = self.request_thresholds[i] = mu
                next_value = mu*(1-mu-self.cash_ell)/(1-mu)
                next_mu = mu
        # A profitable H can make the hypothetical checking mixture exceed
        # one. It is still admissible when the receiver instead preempts
        # by combat, so test the bound only in the selected checking regime.
        if self.thresholds[-2] == self.request_thresholds[-1]:
            assert self.nu < (self.f if self.n == 1 else self.c[-2])
        self.mu = self.thresholds[0]/self.D
        self.alpha = p*self.mu/((1-p)*(1-self.mu))
        assert 0 < self.alpha < 1
        self.nodes = []
        self.root = self.add(None, None,
            {0: self.start(State(0)), 1: self.start(State(1))}, {0: 1-p, 1: p})
        if safe_exit is not None:
            # These new response nodes follow an already launched attack.
            # Their incoming belief is independent of their own terminal
            # response. Optimize using the same common perturbation sequence.
            audit = self.audit_limit()
            for node in self.nodes:
                if node.info and node.info[-1] == ("GuardResponse",):
                    losses = audit["action_losses"][node.info]
                    best = min(losses, key=losses.get)
                    node.base = {best: F(1)}

    def add(self, info, evaluator, edges, base, *, exponent=1, terminal=None,state_type=None):
        if terminal is None:
            assert set(base) <= set(edges)
            assert sum(base.values()) == 1
            assert all(0 <= probability <= 1 for probability in base.values())
        index = len(self.nodes)
        self.nodes.append(Node(info, evaluator, edges, base, exponent, terminal,state_type))
        return index

    def sender(self, st, edges, base, recognized=()):
        powers = {action: (1 if action in recognized else self.high_tremble_power)
                  for action in edges} if st.theta else 1
        evaluator = 6 if st.mode == "H" else (1 if st.mode == "C" else 0)
        return self.add(("S", len(self.nodes)), evaluator,
                        edges, base, exponent=powers,state_type=st.theta)

    def damage(self, st):
        if not self.physical:
            return self.ds, self.dr
        return (recovery_loss(F(5009, 1000), st.time, st.ws),
                recovery_loss(F(19, 1000), st.time, st.wr,
                              repair_time=self.receiver_repair_time))

    def hostile_response(self, st):
        """Receiver best action at the limiting low posterior of an H_z."""
        if self.threshold_guard_effective(st):
            # A goal about outcomes does not reward an ineffective launch.
            # R's credible exit after a launch makes accepting a optimal.
            return f"Set:{self.a}",F(0)
        _, dr = self.damage(st)
        war_loss = dr+self.s*self.D
        acceptable = [y for y in self.policies if y >= self.hz]
        best = min(acceptable, key=lambda y: (y-self.a)**2)
        if self.safe_exit is not None and self.safe_exit < min(war_loss, (best-self.a)**2):
            return f"Exit:{self.a}", self.safe_exit
        if (best-self.a)**2 < war_loss:
            return f"Set:{best}", (best-self.a)**2
        return "Attack", war_loss

    def threshold_guard_effective(self, st):
        if self.hostile_value is None or self.safe_exit is None:
            return False
        _,dr=self.damage(st)
        return self.safe_exit<dr+self.s*self.D

    def hostile_sender_loss(self, st):
        """Original sender's actual state loss after H activation, before price."""
        action, _ = self.hostile_response(st)
        if action.startswith("Exit:"):
            y = F(action.split(":")[1])
            ds, _ = self.damage(st)
            return (y-st.theta-self.b)**2+(ds if y < self.hz else 0)
        if action != "Attack":
            y = F(action.split(":")[1])
            return (y-st.theta-self.b)**2
        ds, _ = self.damage(st)
        r_target = min(F(1),st.theta+self.a)
        return (ds+self.s*(1-st.theta-self.b)**2+
                (1-self.s)*(r_target-st.theta-self.b)**2)

    def terminal(self, st, y, *, war=False, attempted=False):
        hostile_loss=(st.cs+self.hostile_value*F(y<self.hz)
                      if self.hostile_value is not None else
                      st.cs+(y-st.theta-self.b)**2+100*st.h_violation)
        values = (st.cs+(y-st.theta-self.b)**2,
                  st.cs+(y-st.theta-self.a)**2,
                  st.cr+(y-st.theta-self.a)**2,
                  st.cr+(y-st.theta)**2,
                  F(st.mode == "C"), F(war),
                  hostile_loss,
                  F(st.mode == "H"), F(war or attempted))
        return self.add(None, None, {}, {}, terminal=values,state_type=st.theta)

    def contest(self, st, trace):
        ds, dr = self.damage(st)
        damaged = replace(st, cs=st.cs+ds, cr=st.cr+dr)
        roots = {}
        for winner in ("S", "R"):
            target = (st.theta+self.b if winner == "S" and st.mode != "C"
                      else st.theta+self.a)
            best = min(self.policies, key=lambda y: (y-target)**2)
            edges = {f"Set:{y}": self.terminal(damaged, y, war=True)
                     for y in self.policies}
            if winner == "S":
                roots[winner] = self.sender(st, edges, {f"Set:{best}": F(1)})
            else:
                roots[winner] = self.add(trace+(("WinnerR", st.theta),), 2,
                                         edges, {f"Set:{best}": F(1)},state_type=st.theta)
        return self.add(None, None, roots, {"S": self.s, "R": 1-self.s})

    def offered(self, st, y, trace):
        accepted = replace(st,h_violation=st.h_violation or (st.mode == "H" and y < self.hz))
        attacked = replace(st,h_violation=st.h_violation or (st.mode == "H" and y >= self.hz))
        attack=(st.mode == "H" and y < self.hz and
                not self.threshold_guard_effective(st))
        return self.sender(st,
            {"Accept": self.terminal(accepted, y),
             "Attack": self.sender_attack(attacked, trace+(("SenderAttack",),))},
            {"Attack" if attack else "Accept": F(1)})

    def receiver_actions(self, st, trace):
        edges = {f"Set:{y}": self.offered(st, y, trace+(("Set", y),))
                 for y in self.policies}
        edges["Attack"] = self.contest(st, trace+(("ReceiverAttack",),))
        if self.safe_exit is not None:
            edges.update({f"Exit:{y}": self.exit_offered(st, y)
                          for y in self.policies})
        return edges

    def exit_offered(self, st, y):
        """A completed dispatch protects outputs; S retains a costly shot."""
        paid = replace(st, cr=st.cr+self.safe_exit)
        accepted = replace(paid, h_violation=st.h_violation or
                            (st.mode == "H" and y < self.hz))
        ds, _ = self.damage(st)
        attacked = replace(paid, cs=st.cs+ds, h_violation=st.h_violation or
                            (st.mode == "H" and y >= self.hz))
        return self.sender(st,
            {"Accept": self.terminal(accepted,y),
             "Attack": self.terminal(attacked,y,attempted=True)},
            {"Attack" if st.mode == "H" and y < self.hz and
                        self.hostile_value is None else "Accept": F(1)})

    def sender_attack(self, st, trace):
        if self.safe_exit is None:
            return self.contest(st, trace)
        ds, _ = self.damage(st)
        exited = replace(st, cs=st.cs+ds, cr=st.cr+self.safe_exit)
        edges = {f"Exit:{y}": self.terminal(exited,y,attempted=True)
                 for y in self.policies}
        edges["Contest"] = self.contest(st, trace+(("AcceptContest",),))
        return self.add(trace+(("GuardResponse",),),2,edges,
                        {f"Exit:{self.a}":F(1)},state_type=st.theta)

    def resolved(self, st, trace, theta):
        edges = self.receiver_actions(st, trace)
        target = theta+self.a
        best = min(self.policies, key=lambda y: (y-target)**2)
        if self.late_cash is not None and trace[-1][0] in ("Silent","Refusal"):
            ys = (self.a,self.a+self.trade_offset/2,self.a+self.trade_offset,
                  min(F(1),self.a+2*self.trade_offset),F(1))
            quotes = set()
            for y in ys:
                willingness = (self.a-self.b)**2-(y-self.b)**2-self.trade_fee_s
                for price in (F(0),self.late_cash/2,self.late_cash,
                              min(self.late_cash,max(F(0),willingness))):
                    quotes.add((y,price))
            for y,price in sorted(quotes):
                action=f"Quote:{y}:{price}"
                edges[action]=self.cash_quote(st,y,price,trace+(("Quote",y,price),))
            selected=f"Quote:{self.a+self.trade_offset}:{self.late_cash}"
            return self.add(trace+(("Resolved",),),2,edges,{selected:F(1)},state_type=st.theta)
        return self.add(trace+(("Resolved",),), 2, edges, {f"Set:{best}": F(1)},state_type=st.theta)

    def cash_quote(self, st, y, price, trace):
        """The specified funded, one-quote settlement module.

        Acceptance dispatches the conditional command and cash together.
        Rejection retains ordinary physical policy/attack choices; quotes
        close after this response. Continuous optimality is proved in 080.
        """
        quoted=replace(st,cr=st.cr+self.trade_fee_r)
        accepted=replace(quoted,cs=quoted.cs+price+self.trade_fee_s,
                         cr=quoted.cr-price)
        target=st.theta+(self.a if st.mode == "C" else self.b)
        take=price+self.trade_fee_s+(y-target)**2
        reject=(self.a-target)**2
        rejected_edges=self.receiver_actions(quoted,trace+(("Rejected",),))
        rejected=self.add(trace+(("Rejected",),),2,rejected_edges,
                          {f"Set:{self.a}":F(1)},state_type=st.theta)
        return self.sender(st,
            {"Accept":self.terminal(accepted,y),"Reject":rejected,
             "Attack":self.sender_attack(quoted,trace+(("SenderAttack",),))},
            {"Accept" if take <= reject else "Reject":F(1)})

    def start(self, st):
        trace = (("Start",),)
        edges = self.receiver_actions(st, trace)
        edges["Wait"] = self.claim(st, trace+(("Wait",),))
        return self.add(trace, 2, edges, {"Wait": F(1)},state_type=st.theta)

    def claim(self, st, trace):
        paid = replace(st, time=F(1), ws=st.ws-F(1, 10), cs=st.cs+self.f)
        edges = {"Claim": self.checkpoint(paid, 0, self.mu, trace+(("Claim",),)),
                 "Silent": self.resolved(replace(st, time=F(1)),
                                         trace+(("Silent",),), 0),
                 "Attack": self.sender_attack(st, trace+(("SenderAttack",),))}
        base = {"Claim": F(1)} if st.theta else {"Claim": self.alpha,
                                                              "Silent": 1-self.alpha}
        return self.sender(st, edges, base)

    def checkpoint_mix(self, st, i, posterior):
        stop = f"Set:{1-posterior}" if self.continuous_posteriors is not None else "Set:1"
        if posterior*self.D < self.thresholds[i]:
            return {stop: F(1)}
        assert posterior*self.D == self.thresholds[i]
        entry = self.f if i == 0 else self.c[i-1]
        ds, dr = self.damage(st)
        if (self.continuous_posteriors is not None or
                self.request_thresholds[i] <= dr/(1-self.s)):
            gain = (2*self.b*(1-posterior)-(1-posterior)**2
                    if self.continuous_posteriors is not None else self.g)
            q = (gain-entry)/(gain-(self.nu if i == self.n-1 else F(0)))
            return {"Request": q, stop: 1-q}
        z = (self.g-entry)/(ds+(1-self.s)*self.g)
        return {"Attack": z, "Set:1": 1-z}

    def checkpoint(self, st, i, posterior, trace):
        edges = self.receiver_actions(st, trace)
        requested = replace(st, cr=st.cr+self.r[i], wr=st.wr-F(1, 2))
        next_posterior = min(posterior, self.thresholds[i+1]/self.D)
        low_advance = (next_posterior*(1-posterior)/(posterior*(1-next_posterior))
                       if next_posterior else F(0))
        edges["Request"] = self.begin(requested, i, posterior, next_posterior,
                                      low_advance, trace+(("Request", i),))
        return self.add(trace+(("Checkpoint", i),), 2, edges,
                        self.checkpoint_mix(st, i, posterior),state_type=st.theta)

    def begin(self, st, i, posterior, next_posterior, low_advance, trace):
        options = {"BeginC": self.c[i]}
        if i == self.n-1 and self.delegate_final is not None:
            options["BeginD"] = self.delegate_final
        if self.hostile_price is not None:
            options["BeginH"] = self.hostile_price
        edges = {"Refuse": self.mid(st, i, posterior, next_posterior,
                                     None, F(0), trace),
                 "Wait": self.mid(st, i, posterior, next_posterior,
                                   None, F(0), trace),
                 "Attack": self.sender_attack(st, trace+(("SenderAttack",),))}
        for action, cost in options.items():
            begun = replace(st, cs=st.cs+cost/2, ws=st.ws-F(1, 2))
            edges[action] = self.mid(begun, i, posterior, next_posterior,
                                    action[-1], cost, trace)
        recognized = [action for action in options if action != "BeginH"]
        cheapest = min(recognized, key=options.get)
        probability = F(1) if st.theta else low_advance
        base = {cheapest: probability, "Refuse": 1-probability}
        if not st.theta and i == self.n-1 and self.nu > 0:
            base = {"BeginH": F(1)}
        return self.sender(st, edges, base, recognized=recognized)

    def mid(self, st, i, posterior, next_posterior, candidate, cost, trace):
        halfway = replace(st, time=st.time+1)
        mid_trace = trace+(("Mid", i),)
        edges = self.receiver_actions(halfway, mid_trace)
        continued = replace(halfway, wr=halfway.wr-F(1, 2))
        edges["Continue"] = self.finish(continued, i, next_posterior,
                                         candidate, cost, mid_trace+(("Continue",),))
        return self.add(mid_trace, 2, edges, {"Continue": F(1)},state_type=st.theta)

    def finish(self, st, i, next_posterior, candidate, cost, trace):
        end = replace(st, time=st.time+1)
        refused = lambda state: self.resolved(state, trace+(("Refusal", i),), 0)
        edges = {"Abort": refused(end),
                 "Attack": self.sender_attack(st, trace+(("SenderAttack",),))}
        if candidate is None:
            # Restarting too late consumes real resources but cannot supply
            # the complete authenticated stage within the remaining tick.
            wasted = replace(end, cs=end.cs+self.c[i]/2, ws=end.ws-F(1, 2))
            edges["StartLate"] = refused(wasted)
            base = {"Abort": F(1)}
        else:
            finished = replace(end, cs=end.cs+cost/2, ws=end.ws-F(1, 2))
            if candidate == "H":
                finished = replace(finished, mode="H")
                edges["Finish"] = self.report(finished, trace)
                complete_loss = cost/2+self.hostile_sender_loss(finished)
                abort_loss = (self.a-st.theta-self.b)**2
                base = {"Finish" if complete_loss < abort_loss else "Abort": F(1)}
            elif i == self.n-1:
                finished = replace(finished, mode=candidate)
                edges["Finish"] = self.report(finished, trace)
                base = {"Finish" if st.theta else "Abort": F(1)}
            else:
                edges["Finish"] = self.checkpoint(finished, i+1, next_posterior,
                                                   trace+(("Progress", i),))
                base = {"Finish": F(1)}
        return self.sender(st, edges, base)

    def report(self, st, trace):
        if st.mode == "H":
            observed = trace+(("AnnouncedH",),)
            response = self.add(observed, 2, self.receiver_actions(st, observed),
                                {self.hostile_response(st)[0]: F(1)},state_type=st.theta)
            edges = {"Announce": response,
                     "Refuse": self.resolved(st,trace+(("Refusal",self.n-1),),0),
                     "Attack": self.sender_attack(st,trace+(("SenderAttack",),))}
            return self.sender(st, edges, {"Announce": F(1)})
        reports = ("H", "L") if st.mode == "C" else ("Truth",)
        edges = {"Refuse": self.resolved(st, trace+(("Refusal", self.n-1),), 0),
                 "Attack": self.sender_attack(st, trace+(("SenderAttack",),))}
        for message in reports:
            theta = st.theta if message == "Truth" else int(message == "H")
            observed = "H" if theta else "L"
            edges[message] = self.resolved(st,
                trace+(("Protected", st.mode, observed),), theta)
        selected = "Truth" if st.mode == "D" else ("H" if st.theta else "L")
        return self.sender(st, edges, {selected: F(1)})

    def audit_limit(self):
        values = []
        for node in self.nodes:
            values.append(node.terminal if node.terminal is not None else tuple(
                sum(node.base.get(a, 0)*values[child][j] for a, child in node.edges.items())
                for j in range(self.width)))
        leading = [None]*len(self.nodes)
        leading[self.root] = (0, F(1))
        groups = {}
        for index in reversed(range(len(self.nodes))):
            node = self.nodes[index]
            order, coefficient = leading[index]
            if node.info is not None:
                groups.setdefault(node.info, []).append(index)
            for action, child in node.edges.items():
                probability = node.base.get(action, 0)
                assert leading[child] is None
                power = (node.exponent[action] if isinstance(node.exponent, dict)
                         else node.exponent)
                leading[child] = ((order, coefficient*probability) if probability else
                                  (order+power, coefficient))
        regrets, action_losses, beliefs = [], {}, {}
        for info, indexes in groups.items():
            first = self.nodes[indexes[0]]
            order = min(leading[i][0] for i in indexes)
            surviving = [i for i in indexes if leading[i][0] == order]
            mass = sum(leading[i][1] for i in surviving)
            beliefs[info] = {i: leading[i][1]/mass for i in surviving}
            for i in indexes:
                node = self.nodes[i]
                assert node.edges.keys() == first.edges.keys()
                assert node.base == first.base
                assert node.exponent == first.exponent
                assert node.evaluator == first.evaluator
            losses = {a: sum(beliefs[info][i]*values[self.nodes[i].edges[a]][first.evaluator]
                              for i in surviving) for a in first.edges}
            selected = sum(first.base.get(a, 0)*loss for a, loss in losses.items())
            regrets.append((selected-min(losses.values()), str(info)))
            action_losses[info] = losses
        regrets.sort(reverse=True)
        return {"nodes": len(self.nodes), "information_sets": len(groups),
                "maximum_regret": regrets[0][0], "largest_regrets": regrets[:10],
                "values": values[self.root], "beliefs": beliefs,
                "action_losses": action_losses}

    def audit_continuous_policies(self, audit=None):
        """Analytical minimum over every y in [0,1] at receiver policy nodes.

        With no H all specified F/C/D senders accept these offers: their
        finite attack expense exceeds any policy benefit. Quote optimality
        uses the separate low-posterior budget calculus in note 080.
        """
        assert self.hostile_price is None and self.safe_exit is None
        audit = self.audit_limit() if audit is None else audit
        regrets,quote_posteriors = [],[]
        for info,belief in audit['beliefs'].items():
            first=self.nodes[next(iter(belief))]
            if first.evaluator != 2 or 'Set:0' not in first.edges:
                continue
            high=sum(probability*self.nodes[index].state_type
                     for index,probability in belief.items())
            y=max(F(0),min(F(1),high+self.a))
            losses=audit['action_losses'][info]
            optimum=losses['Set:0']-2*(high+self.a)*y+y*y
            selected=sum(first.base.get(action,0)*loss for action,loss in losses.items())
            regrets.append(max(F(0),selected-optimum))
            if any(action.startswith('Quote:') for action in first.edges):
                quote_posteriors.append(high)
        return dict(maximum_policy_regret=max(regrets),
                    quote_posteriors=quote_posteriors)

    def audit(self, epsilon):
        """Finite members of the same completely mixed belief sequence."""
        distributions, values = [], []
        for node in self.nodes:
            if node.terminal is not None:
                distributions.append({})
                values.append(node.terminal)
                continue
            trembles = {}
            for action in node.edges:
                if not node.base.get(action, 0):
                    power = (node.exponent[action] if isinstance(node.exponent, dict)
                             else node.exponent)
                    trembles[action] = epsilon**power
            mass = sum(trembles.values())
            assert mass < 1
            distribution = {a: (node.base[a]*(1-mass) if node.base.get(a, 0)
                                 else trembles[a]) for a in node.edges}
            distributions.append(distribution)
            values.append(tuple(sum(distribution[a]*values[child][j]
                                    for a, child in node.edges.items())
                                for j in range(self.width)))
        reaches, groups = [F(0)]*len(self.nodes), {}
        reaches[self.root] = F(1)
        for i in reversed(range(len(self.nodes))):
            node = self.nodes[i]
            if node.info is not None:
                groups.setdefault(node.info, []).append(i)
            for action, child in node.edges.items():
                reaches[child] += reaches[i]*distributions[i][action]
        regrets = []
        for info, indexes in groups.items():
            first = self.nodes[indexes[0]]
            mass = sum(reaches[i] for i in indexes)
            assert mass > 0
            losses = {a: sum(reaches[i]*values[self.nodes[i].edges[a]][first.evaluator]
                              for i in indexes)/mass for a in first.edges}
            selected = sum(first.base.get(a, 0)*loss for a, loss in losses.items())
            regrets.append((selected-min(losses.values()), str(info)))
        regrets.sort(reverse=True)
        return {"maximum_regret": regrets[0][0], "largest_regrets": regrets[:3],
                "values": values[self.root]}


def main():
    for physical in (False, True):
        tree = StagedTree(physical=physical)
        result = tree.audit_limit()
        print({"physical": physical, "nodes": result["nodes"],
               "information_sets": result["information_sets"],
               "maximum_regret": str(result["maximum_regret"]),
               "values": tuple(str(x) for x in result["values"])})
        if result["maximum_regret"]:
            print(result["largest_regrets"][:3])


if __name__ == "__main__":
    main()
