"""Backward finite execution checks for note 032, without a game library.

At each checkpoint enumerate vertices of both constrained behavior simplexes
and verify both players' best responses. These numerical finite witnesses
support the analytical limit proof; they do not prove a continuous-game or
normal-form refinement theorem. Outcome vectors retain both founder criteria,
the current balanced criterion, and the probability of combat.
"""
from functools import lru_cache
from math import sqrt
import unittest


def mean(vectors, weights):
    return tuple(sum(w*v[k] for v, w in zip(vectors, weights))
                 for k in range(len(vectors[0])))


def vertex(n, chosen, eta):
    return tuple(1-(n-1)*eta if j == chosen else eta for j in range(n))


def constrained_stage(matrix, row_criterion, column_criterion, eta):
    nr, nc = len(matrix), len(matrix[0])
    rows = [vertex(nr, i, eta) for i in range(nr)]
    cols = [vertex(nc, j, eta) for j in range(nc)]
    values = [[mean([mean(matrix[i], col) for i in range(nr)], row)
               for col in cols] for row in rows]
    equilibria = []
    for i in range(nr):
        for j in range(nc):
            if (values[i][j][row_criterion] >= max(values[k][j][row_criterion] for k in range(nr))-1e-13
                    and values[i][j][column_criterion] >= max(values[i][k][column_criterion] for k in range(nc))-1e-13):
                equilibria.append((values[i][j], i, j))
    if not equilibria:
        raise AssertionError('No pure constrained-vertex equilibrium in this test fixture')
    # The mathematical proof classifies all limits; this independent check
    # retains every pure vertex equilibrium, including indifferent actions.
    return equilibria


def finite_game(eta, p_a=1., p_b=1., k_a=0., k_b=0.):
    menu = ((0., 0.), (1., 0.), (0., 1.), (.5, .5), (.25, .75))
    def terminal(x, y, changed, war):
        return (x-k_a*changed[0], y-k_b*changed[1],
                (sqrt(x)+sqrt(y))/sqrt(2), float(war))
    def criterion(agent, changed):
        return 2 if changed[agent] else agent

    @lru_cache(None)
    def combat(w, changed):
        branches = []
        for winner in (0, 1):
            values = [terminal(w*x, w*y, changed, True) for x, y in menu]
            best = max(range(len(menu)), key=lambda j: values[j][criterion(winner, changed)])
            branches.append(mean(values, vertex(len(menu), best, eta)))
        return mean(branches, (.5, .5))

    @lru_cache(None)
    def production(changed):
        fight = combat(.25, changed)
        branches = []
        for operator in (0, 1):
            matrix = [[terminal(x, y, changed, False), fight] for x, y in menu]
            matrix.append([fight, fight])
            equilibria = constrained_stage(matrix, criterion(operator, changed),
                                           criterion(1-operator, changed), eta)
            if len(equilibria) != 1:
                raise AssertionError('Expected unique last-checkpoint vertex equilibrium')
            branches.append(equilibria[0][0])
        return mean(branches, (.5, .5))

    @lru_cache(None)
    def second(changed):
        fight = combat(.26, changed)
        installed = (changed[0], True)
        attempt = mean([production(installed), production(changed)], (p_b, 1-p_b))
        matrix = [[production(changed), fight], [attempt, fight], [fight, fight]]
        return constrained_stage(matrix, criterion(1, changed), criterion(0, changed), eta)[0][0]

    changed = (False, False)
    fight = combat(.27, changed)
    attempt = mean([second((True, False)), second(changed)], (p_a, 1-p_a))
    initial = [[second(changed), fight], [attempt, fight], [fight, fight]]
    return constrained_stage(initial, 0, 1, eta), production


class BehavioralPerturbationTests(unittest.TestCase):
    def test_last_checkpoint_and_reliable_backward_selection(self):
        for eta in (1e-3, 1e-4, 1e-5):
            initial, production = finite_game(eta)
            self.assertEqual(len(initial), 1)
            result, row, column = initial[0]
            self.assertEqual((row, column), (0, 0))
            self.assertAlmostEqual(result[0], .75, delta=30*eta)
            self.assertAlmostEqual(result[1], .25, delta=30*eta)
            self.assertLess(result[3], 30*eta)
            self.assertGreater(production((False, False))[3], 1-5*eta)
            for flags in ((True, False), (False, True), (True, True)):
                self.assertLess(production(flags)[3], 5*eta)

    def test_nonmonotone_reliability_survives_the_refinement(self):
        outcomes = []
        for p, expected_row, expected_war in ((.19, 1, .81**2), (.21, 0, .79)):
            initial, _ = finite_game(1e-5, p, p)
            self.assertEqual(len(initial), 1)
            result, row, column = initial[0]
            self.assertEqual((row, column), (expected_row, 0))
            self.assertAlmostEqual(result[3], expected_war, delta=.002)
            outcomes.append(result[3])
        self.assertGreater(outcomes[1], outcomes[0])

    def test_finite_freezing_and_preemption_strict_regions(self):
        for k_b, expected_actions, expected_war in ((.119, (0, 1), 1.), (.121, (1, 0), 0.)):
            initial, _ = finite_game(1e-5, k_b=k_b)
            self.assertEqual(len(initial), 1)
            result, row, column = initial[0]
            self.assertEqual((row, column), expected_actions)
            self.assertAlmostEqual(result[3], expected_war, delta=.002)
        initial, _ = finite_game(1e-5, .02, .02)
        for result, _, _ in initial:
            self.assertGreater(result[3], .998)


if __name__ == '__main__':
    unittest.main()
