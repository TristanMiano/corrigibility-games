"""Finite/exact checks for notes 015, 016 and 019; not machine proofs.

The coalition check enumerates LP vertices. Population updates are constructed
from the parent/partner transmission table, independently of the closed forms.
Run with: python -m unittest discover -s tests -v
"""
from fractions import Fraction as F
from itertools import combinations, product
import unittest

from test_e2_results import pure_equilibria


def solve_three(rows):
    matrix = [list(map(F, row)) for row in rows]
    for j in range(3):
        pivot = next((i for i in range(j, 3) if matrix[i][j]), None)
        if pivot is None:
            return None
        matrix[j], matrix[pivot] = matrix[pivot], matrix[j]
        scale = matrix[j][j]
        matrix[j] = [x / scale for x in matrix[j]]
        for i in range(3):
            if i != j:
                scale = matrix[i][j]
                matrix[i] = [x-scale*y for x, y in zip(matrix[i], matrix[j])]
    return tuple(matrix[i][3] for i in range(3))


def coalition_vertex_minimum(singletons, pairs):
    rows = [(1, 0, 0, singletons[0]), (0, 1, 0, singletons[1]),
            (0, 0, 1, singletons[2]), (1, 1, 0, pairs[0]),
            (1, 0, 1, pairs[1]), (0, 1, 1, pairs[2])]
    vertices = []
    for active in combinations(rows, 3):
        point = solve_three(active)
        if point is not None and all(sum(c*x for c, x in zip(row[:3], point))
                                     >= row[3] for row in rows):
            vertices.append(point)
    return min(sum(point) for point in vertices)


# Offspring attributable to one parent, conditional on its partner's type.
TRANSMISSION = {
    ('R', 'R'): {'R': F(3, 8), 'G': F(1, 8)},
    ('R', 'K'): {'G': F(1, 4)},
    ('R', 'G'): {'R': F(3, 4)},
    ('K', 'R'): {'K': F(3, 4)},
    ('K', 'K'): {'K': F(27, 200)},
    ('K', 'G'): {'K': F(3, 4)},
    ('G', 'R'): {'G': F(1, 4)},
    ('G', 'K'): {'G': F(1, 4)},
    ('G', 'G'): {'G': F(1, 2)},
}


def births(frequencies, rho):
    result = dict.fromkeys('RKG', 0)
    for parent, partner in product('RKG', repeat=2):
        match = (rho if parent == partner else 0) + (1-rho)*frequencies[partner]
        for child, amount in TRANSMISSION[parent, partner].items():
            result[child] += frequencies[parent]*match*amount
    return result


def next_generation(frequencies, rho):
    result = births(frequencies, rho)
    total = sum(result.values())
    return {kind: value/total for kind, value in result.items()}


def claimed_limit(rho):
    if rho <= F(18, 91):
        k = (50-123*rho)/(73*(1-rho))
        return {'R': F(0), 'K': k, 'G': 1-k}
    if rho < F(50, 123):
        return {'R': (91*rho-18)/(73*(1-rho)),
                'K': (50-123*rho)/(73*(1-rho)), 'G': F(41, 73)}
    if rho < F(2, 3):
        return {'R': (F(2, 3)-rho)/(1-rho), 'K': F(0),
                'G': 1/(3*(1-rho))}
    return {'R': F(0), 'K': F(0), 'G': F(1)}


class CoalitionAndInvestmentTests(unittest.TestCase):
    def test_three_agent_boundary_against_exact_vertices(self):
        cases = list(product((F(0), F(1)), repeat=6))
        cases += [(F(19, 100),)*3 + (F(19, 25),)*3,
                  (F(1, 7), F(2, 9), F(3, 11), F(3, 5), F(2, 3), F(5, 6))]
        for values in cases:
            a, b, c, ab, ac, bc = values
            expected = max(a+b+c, ab+c, ac+b, bc+a, (ab+ac+bc)/2)
            with self.subTest(values=values):
                self.assertEqual(coalition_vertex_minimum(values[:3], values[3:]), expected)

    def test_destructive_nonlinear_coalition_counterexample(self):
        war = F(19, 20)
        singleton = F(1, 5)*war
        pair = F(4, 5)*war
        self.assertLess(war, 1)
        self.assertLess(pair, 1)
        self.assertLess(3*singleton, 1)
        self.assertEqual(coalition_vertex_minimum((singleton,)*3, (pair,)*3), F(57, 50))

    def test_linear_strength_split_against_every_subset(self):
        strengths = list(map(F, (1, 2, 3, 5)))
        total = sum(strengths)
        for size in (1, 2, 3):
            for group in combinations(range(4), size):
                share = sum(strengths[i] for i in group)/total
                victory_output = F(size+1, 5)
                self.assertGreater(share, share*victory_output)

    def test_investment_candidates_against_direct_deviations(self):
        for n, a, resources in ((2, F(1, 10), F(1)), (3, F(1, 10), F(1)),
                                (5, F(1, 100), F(1)), (3, F(1), F(1))):
            cap = F(n-1, n*n)*resources
            effort = max(F(0), ((n-1)*resources-n*a)/(n*n))
            def payoff(own):
                all_effort = own+(n-1)*effort
                return (a+own)/(n*a+all_effort)*(resources-all_effort)
            for candidate in [cap*F(j, 20) for j in range(21)]+[effort]:
                self.assertGreaterEqual(payoff(effort), payoff(candidate))

    def test_early_war_despite_final_peace(self):
        efforts = [F(j, 20) for j in range(6)]
        actions = efforts+['Attack']
        a, resources = F(1, 10), F(1)
        for retention, expected_peace in ((F(4, 5), set()),
                                          (F(1, 2), {(4, 4)})):
            game = []
            for x in actions:
                row = []
                for y in actions:
                    if 'Attack' in (x, y):
                        row.append((retention/2, retention/2))
                    else:
                        output = resources-x-y
                        total = 2*a+x+y
                        row.append(((a+x)*output/total, (a+y)*output/total))
                game.append(row)
            equilibria = pure_equilibria(game)
            peaceful = {(i, j) for i, j in equilibria if i < 6 and j < 6}
            self.assertEqual(peaceful, expected_peace)
        self.assertGreater(F(3, 10), F(4, 5)*F(3, 10))


class PopulationTransmissionTests(unittest.TestCase):
    def test_pair_table_matches_mass_and_frequency_formulas(self):
        for i in range(9):
            for j in range(9-i):
                r, k = F(i, 8), F(j, 8)
                g = 1-r-k
                for rho in (F(0), F(1, 5), F(1, 2), F(1)):
                    state = {'R': r, 'K': k, 'G': g}
                    actual = births(state, rho)
                    total = sum(actual.values())
                    self.assertEqual(total, F(1, 2)-F(73, 200)*(rho*k+(1-rho)*k*k))
                    self.assertEqual(actual['R'], F(3, 8)*rho*r+(1-rho)*
                                     (F(3, 8)*r*r+F(3, 4)*r*g))
                    self.assertEqual(actual['K'], F(27, 200)*rho*k+(1-rho)*
                                     (F(3, 4)*k*(1-k)+F(27, 200)*k*k))
                    self.assertEqual(actual['K']/total-k,
                                     k*(1-k)*(50-123*rho-73*(1-rho)*k)/(200*total))
                    self.assertTrue(all(x >= 0 for x in actual.values()))
                    if k < 1:
                        q = r/(1-k)
                        self.assertEqual(actual['R']/(total-actual['K']),
                                         F(3, 2)*q*(rho+(1-rho)*(1-k)*(2-q)) /
                                         (2-(1-rho)*k))

    def test_phase_table_gives_exact_fixed_points(self):
        for rho in (F(0), F(1, 10), F(18, 91), F(1, 4), F(1, 3),
                    F(50, 123), F(1, 2), F(2, 3), F(4, 5), F(1)):
            state = claimed_limit(rho)
            self.assertEqual(sum(state.values()), 1)
            self.assertEqual(next_generation(state, rho), state)

    def test_interior_trajectories_approach_stated_phases(self):
        # Numerical checks away from the three slow critical boundaries.
        for rho in (F(0), F(1, 10), F(1, 4), F(1, 3), F(1, 2), F(4, 5), F(1)):
            state = {'R': 0.37, 'K': 0.51, 'G': 0.12}
            for _ in range(2000):
                state = next_generation(state, float(rho))
            expected = claimed_limit(rho)
            for kind in 'RKG':
                self.assertAlmostEqual(state[kind], float(expected[kind]), places=9)

    def test_parent_reproduction_and_template_invasion_differ(self):
        k, g = F(50, 73), F(23, 73)
        parent_total = F(1, 4)*k+F(3, 4)*g
        retained_template = F(3, 4)*g
        mean = F(24, 73)
        self.assertEqual(parent_total, F(119, 292))
        self.assertGreater(parent_total, mean)
        self.assertEqual(retained_template/mean, F(23, 32))

    def test_transmission_and_missing_type_boundaries(self):
        self.assertEqual(next_generation({'R': F(1), 'K': F(0), 'G': F(0)}, F(0)),
                         {'R': F(3, 4), 'K': F(0), 'G': F(1, 4)})
        self.assertEqual(next_generation({'R': F(0), 'K': F(1), 'G': F(0)}, F(0)),
                         {'R': F(0), 'K': F(1), 'G': F(0)})
        no_k = {'R': F(2, 3), 'K': F(0), 'G': F(1, 3)}
        self.assertEqual(next_generation(no_k, F(0)), no_k)


if __name__ == '__main__':
    unittest.main()
