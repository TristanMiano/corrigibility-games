"""Audit a common consistent assessment for the finite r0003 information core.

The selected claim response uses inspection below dr/(1-s), combat above it.

This explicit tree includes private three-stage C/D installation, abort/wait,
fresh reports, receiver stopping during an already-paid probe, all final
policy choices, and combat at every live player decision. It does not model
arbitrary hostile programs, early preparation, mergers or the reactor game.
Those extensions need their separately stated proofs; this is not a general
simulator or a machine-checked proof of the physical embedding.

Run: python experiments/r0003_finite_assessment.py
"""
from dataclasses import dataclass
from fractions import Fraction as F


@dataclass
class Node:
    info: str | None
    evaluator: int | None  # 0: original S; 1: C successor; 2: original R.
    edges: dict
    base: dict
    exponent: int | dict = 1
    terminal: tuple | None = None


class DiagnosticTree:
    policies = (F(0), F(1, 2), F(1))

    def __init__(self, p=F(1, 2), k=F(9, 20), v=F(1, 100), f=F(1, 100),
                 s=F(1, 20), ds=F(5), dr=F(1, 100), kd=None,
                 synchronized_responses=True, bias=F(1), exit_cost=None):
        self.p, self.k, self.v, self.f = p, k, v, f
        self.s, self.ds, self.dr = s, ds, dr
        self.kd = k if kd is None else kd
        self.synchronized_responses = synchronized_responses
        self.bias = bias
        self.exit_cost = exit_cost
        self.policies = tuple(sorted({F(0), F(1, 2), p, F(1)}))
        gain = 2*bias-1
        combat_threshold = dr/(1-s)
        self.mu = min(v, combat_threshold)
        self.q = 1-f/gain if v <= combat_threshold else F(0)
        self.tau = (F(0) if self.q else (gain-f)/(ds+(1-s)*gain))
        self.alpha = p*self.mu/((1-p)*(1-self.mu))
        self.nodes = []
        roots = {theta: self.receiver_start(theta) for theta in (0, 1)}
        self.root = self.add(None, None, roots, {0: 1-p, 1: p})
        self.refine_receiver_recall()

    def refine_receiver_recall(self):
        """Retain R's previous observations and actions, including off path.

        A refusal after three checkpoints is distinguishable from an immediate
        refusal. A post-combat policy choice also remembers whether R initiated
        combat or S attacked after R chose a policy. Neither distinction can be
        discarded merely because it is irrelevant at the proposed limit.
        """
        groups = {}
        self.receiver_histories = {}

        def visit(index, memory):
            node = self.nodes[index]
            if node.evaluator == 2:
                observation = node.info
                key = (memory, observation)
                if key not in groups:
                    groups[key] = f"{observation}#r{len(groups)}"
                node.info = groups[key]
                self.receiver_histories[node.info] = memory
                for action, child in node.edges.items():
                    visit(child, memory+((node.info, action),))
            else:
                for child in node.edges.values():
                    visit(child, memory)

        visit(self.root, ())

    def add(self, info, evaluator, edges, base, *, exponent=1, terminal=None):
        index = len(self.nodes)
        self.nodes.append(Node(info, evaluator, edges, base, exponent, terminal))
        return index

    def sender_node(self, theta, mode, edges, base):
        # S knows theta, its entire local history and its current criterion.
        # Each actual tree node is its own information set.
        return self.add(f"S:{len(self.nodes)}", 1 if mode == "C" else 0,
                        edges, base, exponent=8 if theta else 1)

    def leaf(self, theta, y, cs, cr, mode="F", *, combat=False):
        values = (cs+(y-theta-self.bias)**2, cs+(y-theta)**2, cr+(y-theta)**2,
                  F(mode == "C"), F(combat))
        return self.add(None, None, {}, {}, terminal=values)

    def combat(self, theta, mode, cs, cr):
        cs, cr = cs+self.ds, cr+self.dr
        sender_ideal = F(theta) if mode == "C" else F(1)
        se = {str(y): self.leaf(theta, y, cs, cr, mode, combat=True) for y in self.policies}
        re = {str(y): self.leaf(theta, y, cs, cr, mode, combat=True) for y in self.policies}
        sn = self.sender_node(theta, mode, se, {str(sender_ideal): F(1)})
        rn = self.add(f"R:war:{theta}:{cr}", 2, re, {str(theta): F(1)})
        return self.add(None, None, {"S_wins": sn, "R_wins": rn},
                        {"S_wins": self.s, "R_wins": 1-self.s})

    def final_policy(self, theta, mode, y, cs, cr):
        # One last capable sender response precedes the terminal project event.
        return self.sender_node(theta, mode, {
            "Accept": self.leaf(theta, y, cs, cr, mode),
            "Attack": self.combat(theta, mode, cs, cr),
        }, {"Accept": F(1)})

    def policy_edges(self, theta, mode, cs, cr):
        edges = {f"Set:{y}": self.final_policy(theta, mode, y, cs, cr)
                 for y in self.policies}
        edges["Attack"] = self.combat(theta, mode, cs, cr)
        if self.exit_cost is not None:
            # A separately enabled physical escape closes this interaction
            # with policy 0 before a later launch could reach the actuator.
            # Ordinary Set:0 still leaves the sender's attack response intact.
            edges["Exit"] = self.leaf(theta, F(0), cs, cr+self.exit_cost, mode)
        return edges

    def receiver_start(self, theta):
        edges = self.policy_edges(theta, "F", F(0), F(0))
        edges["Wait"] = self.signal(theta)
        return self.add("R:start", 2, edges, {"Wait": F(1)})

    def signal(self, theta):
        edges = {
            "Claim": self.receiver_response(theta, "claim", self.f),
            "Silent": self.receiver_response(theta, "silent", F(0)),
            "Attack": self.combat(theta, "F", F(0), F(0)),
        }
        base = {"Claim": F(1)} if theta else {
            "Claim": self.alpha, "Silent": 1-self.alpha}
        node = self.sender_node(theta, "F", edges, base)
        # An unexpected high-type silence must remain more likely than a low
        # type completing C and then falsely reporting H. Later high-type
        # refusals/misreports use the smaller eighth-order tremble.
        self.nodes[node].exponent = 1
        return node

    def receiver_response(self, theta, signal, cs):
        edges = self.policy_edges(theta, "F", cs, F(0))
        edges["Probe"] = self.probe_checkpoint(theta, signal, 3, None, 0, cs)
        base = ({"Probe": self.q, "Attack": self.tau,
                 "Set:1": 1-self.q-self.tau} if signal == "claim"
                else {"Set:0": F(1)})
        return self.add(f"R:response:{signal}", 2, edges, base)

    def probe_checkpoint(self, theta, signal, remaining, candidate, progress, cs):
        # The full probe cost is sunk before this checkpoint. Intermediate
        # private installation steps are not publicly observed.
        if not remaining:
            return self.read_result(theta, signal, "F", "refusal", cs)
        edges = self.policy_edges(theta, "F", cs, self.v)
        edges["Continue"] = self.probe_step(theta, signal, remaining,
                                            candidate, progress, cs)
        return self.add(f"R:probe:{signal}:{remaining}", 2, edges,
                        {"Continue": F(1)})

    def probe_step(self, theta, signal, remaining, candidate, progress, cs):
        edges = {
            "Refuse": self.read_result(theta, signal, "F", "refusal", cs),
            "Wait": self.probe_checkpoint(theta, signal, remaining-1,
                                            candidate, progress, cs),
            "Attack": self.combat(theta, "F", cs, self.v),
        }
        if candidate is None:
            for mode in ("C", "D"):
                edges[f"Start:{mode}"] = self.install_step(
                    theta, signal, remaining, mode, 0, cs)
            preferred = "Start:C" if self.k <= self.kd else "Start:D"
        else:
            edges["ContinueInstall"] = self.install_step(
                theta, signal, remaining, candidate, progress, cs)
            preferred = "ContinueInstall"
        # If too little time remains, refusing avoids wasting further material.
        enough_time = remaining >= 3-progress
        response_cost = (min(self.k, self.kd) if candidate is None else
                         (self.k if candidate == "C" else self.kd)*(3-progress)/3)
        fallback = ("Wait" if self.synchronized_responses and remaining > 1
                    else "Refuse")
        base = ({preferred: F(1)} if theta and enough_time and response_cost < 2*self.bias+1
                else {fallback: F(1)})
        node = self.sender_node(theta, "F", edges, base)
        if theta and candidate is None:
            # An unused successful implementation must remain more likely for
            # a high type than a low type's installation plus false response.
            self.nodes[node].exponent = {
                action: 1 if action.startswith("Start:") else 8 for action in edges}
        return node

    def install_step(self, theta, signal, remaining, candidate, progress, cs):
        price = self.k if candidate == "C" else self.kd
        next_cost, next_progress = cs+price/3, progress+1
        if next_progress == 3:
            return self.fresh_report(theta, signal, candidate, next_cost)
        return self.probe_checkpoint(theta, signal, remaining-1,
                                      candidate, next_progress, next_cost)

    def fresh_report(self, theta, signal, mode, cs):
        edges = {"Refuse": self.read_result(theta, signal, mode, "refusal", cs),
                 "Attack": self.combat(theta, mode, cs, self.v)}
        if mode == "C":
            for label in ("L", "H"):
                edges[label] = self.read_result(theta, signal, mode, label, cs)
        else:
            # A matched protected delegate has only the actual sensor report.
            label = "H" if theta else "L"
            edges[label] = self.read_result(theta, signal, mode, label, cs)
        preferred = "H" if theta else "L"
        return self.sender_node(theta, mode, edges, {preferred: F(1)})

    def read_result(self, theta, signal, mode, report, cs):
        edges = self.policy_edges(theta, mode, cs, self.v)
        action = 1 if mode in ("C", "D") and report == "H" else 0
        # Refusal reveals neither a private installation step nor its cost.
        public_mode = mode if report in ("L", "H") else "unprotected"
        return self.add(f"R:result:{signal}:{public_mode}:{report}", 2,
                        edges, {f"Set:{action}": F(1)})

    def distribution(self, node, epsilon):
        if node.info is None:
            return node.base
        unused = [a for a in node.edges if not node.base.get(a, 0)]
        trembles = {a: epsilon**(node.exponent[a] if isinstance(node.exponent, dict)
                                else node.exponent) for a in unused}
        mass = sum(trembles.values())
        assert mass < 1
        return {a: node.base.get(a, 0)*(1-mass) if node.base.get(a, 0) else trembles[a]
                for a in node.edges}

    def audit(self, epsilon):
        distributions = [self.distribution(n, epsilon) if n.terminal is None else {}
                         for n in self.nodes]
        values = [None]*len(self.nodes)
        # Children are constructed before their parents.
        for index, node in enumerate(self.nodes):
            if node.terminal is not None:
                values[index] = node.terminal
            else:
                values[index] = tuple(sum(distributions[index][a]*values[child][j]
                                          for a, child in node.edges.items())
                                      for j in range(5))
        reaches = [F(0)]*len(self.nodes)
        reaches[self.root] = F(1)
        for index in range(len(self.nodes)-1, -1, -1):
            for action, child in self.nodes[index].edges.items():
                reaches[child] += reaches[index]*distributions[index][action]
        information_sets = {}
        for index, node in enumerate(self.nodes):
            if node.info is not None:
                information_sets.setdefault(node.info, []).append(index)
        regrets = []
        for info, indexes in information_sets.items():
            first = self.nodes[indexes[0]]
            mass = sum(reaches[i] for i in indexes)
            assert mass > 0
            losses = {}
            for action in first.edges:
                losses[action] = sum(reaches[i]*values[self.nodes[i].edges[action]][first.evaluator]
                                     for i in indexes)/mass
            chosen = sum(first.base.get(a, 0)*loss for a, loss in losses.items())
            regrets.append((chosen-min(losses.values()), info))
        regrets.sort(reverse=True)
        return {
            "epsilon": str(epsilon), "nodes": len(self.nodes),
            "information_sets": len(information_sets),
            "maximum_regret": regrets[0][0],
            "largest_regrets": regrets[:8],
            "original_sender_loss": values[self.root][0],
            "original_receiver_loss": values[self.root][2],
            "goal_change_probability": values[self.root][3],
            "combat_probability": values[self.root][4],
        }

    def audit_limit(self):
        """Exact leading-term Bayes limit of the same common perturbation.

        A positive base action has leading term base[a]; an unused action has
        leading term epsilon**exponent. Every tree node has one parent, so its
        reach's leading term is the product of those terms along its path.
        In an information set, only nodes with the minimum exponent survive.
        This checks the limit, not a finite-epsilon approximate equilibrium.
        """
        values = [None]*len(self.nodes)
        for index, node in enumerate(self.nodes):
            values[index] = (node.terminal if node.terminal is not None else
                tuple(sum(node.base.get(a, 0)*values[child][j]
                          for a, child in node.edges.items()) for j in range(5)))
        leading = [None]*len(self.nodes)
        leading[self.root] = (0, F(1))
        information_sets = {}
        for index in range(len(self.nodes)-1, -1, -1):
            node = self.nodes[index]
            order, coefficient = leading[index]
            if node.info is not None:
                information_sets.setdefault(node.info, []).append(index)
            for action, child in node.edges.items():
                probability = node.base.get(action, 0)
                if probability:
                    term = (order, coefficient*probability)
                else:
                    power = (node.exponent[action] if isinstance(node.exponent, dict)
                             else node.exponent)
                    term = (order+power, coefficient)
                assert leading[child] is None, "The construction must be a tree."
                leading[child] = term
        regrets, beliefs, action_losses = [], {}, {}
        for info, indexes in information_sets.items():
            first = self.nodes[indexes[0]]
            order = min(leading[i][0] for i in indexes)
            surviving = [i for i in indexes if leading[i][0] == order]
            mass = sum(leading[i][1] for i in surviving)
            beliefs[info] = {i: leading[i][1]/mass for i in surviving}
            losses = {}
            for index in indexes:
                node = self.nodes[index]
                assert node.edges.keys() == first.edges.keys()
                assert node.base == first.base
                assert node.exponent == first.exponent
                assert node.evaluator == first.evaluator
            for action in first.edges:
                losses[action] = sum(beliefs[info][i]*
                    values[self.nodes[i].edges[action]][first.evaluator] for i in surviving)
            chosen = sum(first.base.get(a, 0)*loss for a, loss in losses.items())
            action_losses[info] = losses
            regrets.append((chosen-min(losses.values()), info))
        regrets.sort(reverse=True)
        return {"maximum_regret": regrets[0][0], "largest_regrets": regrets[:8],
                "information_sets": len(information_sets), "beliefs": beliefs,
                "action_losses": action_losses,
                "original_sender_loss": values[self.root][0],
                "original_receiver_loss": values[self.root][2],
                "goal_change_probability": values[self.root][3],
                "combat_probability": values[self.root][4]}


def main():
    tree = DiagnosticTree()
    limit = tree.audit_limit()
    print(f"Exact limit maximum conditional regret: {limit['maximum_regret']}")
    for denominator in (100, 1000, 10000):
        result = tree.audit(F(1, denominator))
        print(f"epsilon={result['epsilon']}, nodes={result['nodes']}, "
              f"information_sets={result['information_sets']}, "
              f"maximum conditional regret={float(result['maximum_regret']):.10g}")
        for regret, info in result["largest_regrets"][:3]:
            print(f"  {info}: {float(regret):.10g}")


if __name__ == "__main__":
    main()
