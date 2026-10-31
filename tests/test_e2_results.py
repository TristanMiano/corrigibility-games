"""Checks for note 010 / E2.0; run python -m unittest discover -s tests -v.

Standard library only. Fraction arithmetic checks the recovery LP by an
independent vertex enumeration and computes finite-game payoff/deviation cases.
Square-root utility comparisons use floating point with large strict margins;
the proofs and continuous-action arguments remain in the note. These tests are
not a general equilibrium solver, a physics calibration, or machine proofs.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import sqrt
from random import Random
import unittest


def frontier(o, d, b, t, c, tau, w, r, k):
    return min(o + d, k * t, b / c, (b + w * o) / (c + w),
               t / tau, (t + r * o) / (tau + r))


def lp_vertices(o, d, b, t, c, tau, w, r, k):
    # Each constraint is ax + by <= bound, with x recovery and y output.
    constraints = [(-F(1), F(0), F(0)), (F(1), F(0), d),
                   (F(0), -F(1), F(0)), (-F(1), F(1), o),
                   (w, c, b), (r, tau, t), (F(0), F(1), k * t)]
    vertices = []
    for (a, b1, z), (c1, d1, z1) in combinations(constraints, 2):
        det = a * d1 - b1 * c1
        if not det:
            continue
        x, y = (z * d1 - b1 * z1) / det, (a * z1 - z * c1) / det
        if all(ax * x + by * y <= bound for ax, by, bound in constraints):
            vertices.append((x, y))
    return vertices


def allocation(controller, types, output):
    if types[controller] == "G":
        return (output / 2, output / 2)
    return (output, F(0)) if controller == 0 else (F(0), output)


def utility(agent, types, x):
    if types[agent] == "G":
        return (sqrt(x[0]) + sqrt(x[1])) / sqrt(2)
    return x[agent]


def war_law(types, output):
    return [(F(1, 2), allocation(winner, types, output)) for winner in (0, 1)]


def current_value(agent, types, law):
    return sum(float(p) * utility(agent, types, x) for p, x in law)


def founder_values(law):
    return tuple(sum((p * x[i] for p, x in law), F(0)) for i in (0, 1))


def selected_continuation(types):
    if types == ("O", "O"):
        return war_law(types, F(1, 4))
    return [(F(1, 2), allocation(controller, types, F(1)))
            for controller in (0, 1)]


def freeze_game(ka, kb):
    # Construct the reduced initial game from round-2 best responses.
    attack = (F(27, 200), F(27, 200))
    after_keep = ((F(3, 4), F(1, 4) - kb) if F(1, 4) - kb > F(13, 100)
                  else (F(13, 100), F(13, 100)))
    wait_column = [after_keep, (F(1, 4) - ka, F(3, 4)), attack]
    return [[payoff, attack] for payoff in wait_column]


def pure_equilibria(game):
    rows, cols = len(game), len(game[0])
    return {(i, j) for i, j in product(range(rows), range(cols))
            if all(game[i][j][0] >= game[ii][j][0] for ii in range(rows))
            and all(game[i][j][1] >= game[i][jj][1] for jj in range(cols))}


def unreliable_update_game(p):
    """Backward construction from conditional outcomes, not the expanded formula."""
    initial_war = (F(27, 200), F(27, 200))
    late_war = (F(1, 8), F(1, 8))
    successful_b = (F(3, 4), F(1, 4))
    b_try = tuple(p*successful_b[i] + (1-p)*late_war[i] for i in (0, 1))
    after_keep = b_try if b_try[1] > F(13, 100) else (F(13, 100), F(13, 100))
    successful_a = (F(1, 4), F(3, 4))
    after_try = tuple(p*successful_a[i] + (1-p)*after_keep[i] for i in (0, 1))
    return [[after_keep, initial_war], [after_try, initial_war],
            [initial_war, initial_war]]


def combined_update_game(pa, pb, ka, kb):
    initial_war = (F(27, 200), F(27, 200))
    b_success, failure = (F(3, 4), F(1, 4)-kb), (F(1, 8), F(1, 8))
    b_try = tuple(pb*b_success[i] + (1-pb)*failure[i] for i in (0, 1))
    after_keep = b_try if b_try[1] > F(13, 100) else (F(13, 100), F(13, 100))
    a_success = (F(1, 4)-ka, F(3, 4))
    a_try = tuple(pa*a_success[i] + (1-pa)*after_keep[i] for i in (0, 1))
    return [[after_keep, initial_war], [a_try, initial_war],
            [initial_war, initial_war]]


class E2ResultTests(unittest.TestCase):
    def test_closed_frontier_against_independent_lp_vertices(self):
        rng = Random(141421)
        nonnegative = [F(0), F(1, 2), F(1), F(3), F(8)]
        positive = [F(1, 2), F(1), F(2)]
        cases = [(F(0),) * 4 + (F(1), F(1), F(0), F(0), F(0)),
                 tuple(map(F, (10, 0, 12, 12, 1, 1, 1, 1, 10))),
                 tuple(map(F, (4, 6, 12, 12, 1, 1, 1, 1, 10)))]
        for _ in range(250):
            cases.append(tuple(rng.choice(nonnegative) for _ in range(4)) +
                         tuple(rng.choice(positive) for _ in range(2)) +
                         tuple(rng.choice(nonnegative) for _ in range(3)))
        for args in cases:
            with self.subTest(args=args):
                vertices = lp_vertices(*args)
                self.assertTrue(vertices)
                self.assertEqual(frontier(*args), max(y for _, y in vertices))

    def test_dispersion_bottleneck_and_peace_cost_reversal(self):
        def y(o, b, t):
            return frontier(*map(F, (o, 10-o, b, t, 1, 1, 1, 1, 10)))
        self.assertEqual(y(10, 12, 12), 10)
        self.assertEqual(y(8, 12, 12), 10)
        self.assertEqual(y(4, 12, 12), 8)
        self.assertEqual(y(4, 20, 20), 10)
        self.assertGreater(y(4, 14-2, 14-2), y(10, 14-7, 14-7))

    def test_asymmetric_bargain_and_surplus_share(self):
        s, wa, wb, p = F(1, 2), F(12), F(4), F(9)
        disagreement = (s * wa, (1-s) * wb)
        x = disagreement[0] + s * (p - sum(disagreement))
        self.assertEqual(x, F(13, 2))
        self.assertGreater(x, disagreement[0])
        self.assertGreater(p-x, disagreement[1])
        self.assertLess(s*p, disagreement[0])

    def test_representation_counterexample(self):
        u, v, other = (F(1), F(0)), (F(4, 5), F(1, 5)), (F(0), F(1))
        self.assertEqual(v, tuple(F(3, 5)*x + F(1, 5) for x in u))
        raw = lambda own: tuple((own[i]+other[i])/sum(own+other) for i in (0, 1))
        self.assertEqual(raw(u), (F(1, 2), F(1, 2)))
        self.assertEqual(raw(v), (F(2, 5), F(3, 5)))

    def test_grouping_and_nonlinear_strength_boundary(self):
        self.assertEqual(F(1, 3)*F(1) + F(1, 3)*F(0), F(2, 3)*F(1, 2))
        individual_group_share = F(1+1, 1+1+1)
        square_strength_group_share = F(2**2, 2**2+1**2)
        self.assertEqual(individual_group_share, F(2, 3))
        self.assertEqual(square_strength_group_share, F(4, 5))

    def test_strong_agent_can_deceive_and_restoration_is_insufficient(self):
        s, p, w, d = F(9, 10), F(1), F(4, 5), F(1, 5)
        h, gain, failure = s*p, p, s*w
        self.assertEqual((gain-h)/(gain-failure), F(5, 14))
        self.assertGreater((1-d)*gain + d*failure, h)
        for detection in (F(0), F(1, 2), F(99, 100)):
            self.assertGreater((1-detection)*gain + detection*h, h)

    def test_inspection_mixed_equilibrium_from_payoffs(self):
        h, g, ell, b, bd, bf = map(F, (2, 4, 0, 3, 0, 4))
        delta, cost = F(3, 4), F(1)
        # A rows honest/cheat; B columns no inspection/inspection.
        game = [[(h, b), (h, b-cost)],
                [(g, bd), ((1-delta)*g+delta*ell,
                           (1-delta)*bd+delta*bf-cost)]]
        self.assertEqual(pure_equilibria(game), set())
        inspect, cheat = F(2, 3), F(1, 3)
        a_values = [(1-inspect)*row[0][0] + inspect*row[1][0] for row in game]
        b_values = [(1-cheat)*game[0][j][1] + cheat*game[1][j][1] for j in (0, 1)]
        self.assertEqual(a_values[0], a_values[1])
        self.assertEqual(b_values[0], b_values[1])

    def test_current_successor_goal_changes_war_production(self):
        mixed_types = ("G", "O")
        self.assertEqual(founder_values(war_law(mixed_types, F(1, 4))),
                         (F(1, 16), F(3, 16)))
        self.assertEqual(founder_values(war_law(("O", "O"), F(1, 4))),
                         (F(1, 8), F(1, 8)))

    def test_persistent_attack_witness_deviations(self):
        candidates = [(F(j, 4), F(1)-F(j, 4)) for j in range(5)]
        for types in (("G", "O"), ("O", "G"), ("G", "G")):
            war = war_law(types, F(1, 4))
            for controller in (0, 1):
                chosen = allocation(controller, types, F(1))
                for agent in (0, 1):
                    self.assertGreater(utility(agent, types, chosen),
                                       current_value(agent, types, war))
                for alternative in candidates:
                    self.assertGreaterEqual(utility(controller, types, chosen),
                                            utility(controller, types, alternative))
        # These sampled allocations check examples; continuous optimality is proved.

    def test_adoption_table_uses_original_welfare(self):
        expected = {("O", "O"): (F(1, 8), F(1, 8)),
                    ("O", "G"): (F(3, 4), F(1, 4)),
                    ("G", "O"): (F(1, 4), F(3, 4)),
                    ("G", "G"): (F(1, 2), F(1, 2))}
        values = {types: founder_values(selected_continuation(types)) for types in expected}
        self.assertEqual(values, expected)
        b_after_a = {a: max(("O", "G"), key=lambda b: values[(a, b)][1]) for a in ("O", "G")}
        self.assertEqual(b_after_a, {"O": "G", "G": "O"})
        a = max(("O", "G"), key=lambda a: values[(a, b_after_a[a])][0])
        self.assertEqual((a, b_after_a[a]), ("O", "G"))

    def test_finite_freezing_preemption_boundary(self):
        # (row 0, col 0) is Keep/Wait; (row 1, col 0) is Install/Wait.
        for ka, kb, peaceful in ((F(0), F(1, 10), (0, 0)),
                                (F(0), F(119, 1000), None),
                                (F(0), F(121, 1000), (1, 0)),
                                (F(1), F(121, 1000), None)):
            equilibria = pure_equilibria(freeze_game(ka, kb))
            self.assertTrue(equilibria)
            nonwar = equilibria.intersection({(0, 0), (1, 0)})
            self.assertEqual(nonwar, set() if peaceful is None else {peaceful})
        # The no-mixed-peace argument is analytical; pure enumeration alone
        # cannot establish that stronger statement.

    def test_stochastic_installation_changes_attempts_and_war_probability(self):
        for p, expected in ((F(3, 100), None), (F(5, 100), (1, 0)),
                            (F(19, 100), (1, 0)), (F(21, 100), (0, 0)),
                            (F(1), (0, 0))):
            game = unreliable_update_game(p)
            nonattack = pure_equilibria(game).intersection({(0, 0), (1, 0)})
            self.assertEqual(nonattack, set() if expected is None else {expected})
            if p > F(1, 25):
                self.assertEqual(game[1][0][0] - game[0][0][0], p*(1-5*p)/8)
        lower_reliability_war = (1-F(19, 100))**2
        higher_reliability_war = 1-F(21, 100)
        self.assertEqual(lower_reliability_war, F(6561, 10000))
        self.assertGreater(higher_reliability_war, lower_reliability_war)

    def test_combined_strict_region_classification(self):
        probabilities = [F(1, 100), F(1, 20), F(19, 100), F(21, 100), F(1)]
        penalties = [F(0), F(1, 10), F(119, 1000), F(121, 1000), F(1)]
        c, t = F(27, 200), F(13, 100)
        for pa, pb, ka, kb in product(probabilities, probabilities, penalties, penalties):
            b = F(1, 8) + pb*(F(1, 8)-kb)
            if b == t:
                continue
            game = combined_update_game(pa, pb, ka, kb)
            k = game[0][0]
            if F(1, 4)-ka == k[0]:
                continue
            row = 1 if F(1, 4)-ka > k[0] else 0
            value = game[row][0]
            if c in value:
                continue
            expected = {(row, 0)} if min(value) > c else set()
            actual = pure_equilibria(game).intersection({(0, 0), (1, 0)})
            self.assertEqual(actual, expected)
        for p in probabilities:
            self.assertEqual(combined_update_game(p, p, F(0), F(0)), unreliable_update_game(p))
        for ka, kb in product(penalties, penalties):
            self.assertEqual(combined_update_game(F(1), F(1), ka, kb), freeze_game(ka, kb))


if __name__ == "__main__":
    unittest.main()
