"""Checks for note 019 sections 7/8 using the original encounter birth table.

Fixed-point roots are compared with that independently assembled transmission
map. Iterations and small-innovation limits are numerical support, not proofs
of global convergence or asymptotic order.
"""
from math import sqrt
import unittest

from test_e2_population import next_generation


def innovate(population, rho, epsilon, nu):
    selected = next_generation(population, rho)
    return {kind: (1-epsilon)*selected[kind]+epsilon*nu[kind] for kind in 'RKG'}


def fixed_point(rho, epsilon, nu):
    if epsilon == 1:
        return dict(nu)
    c, d = 50-123*rho, 73*(1-rho)
    def drift(k):
        h = 100-73*rho*k-d*k*k
        return (1-epsilon)*k*(1-k)*(c-d*k)+epsilon*(nu['K']-k)*h
    low, high = 0., 1.
    for _ in range(80):
        middle = (low+high)/2
        if drift(middle) > 0:
            low = middle
        else:
            high = middle
    k = (low+high)/2
    z = .5-73/200*(rho*k+(1-rho)*k*k)
    a = (1-epsilon)*(3/8*rho+3/4*(1-rho)*(1-k))/z
    b = (1-epsilon)*3/8*(1-rho)/z
    if b == 0:
        r = epsilon*nu['R']/(1-a)
    elif a <= 1:
        r = 2*epsilon*nu['R']/(1-a+sqrt((1-a)**2+4*b*epsilon*nu['R']))
    else:
        r = (a-1+sqrt((1-a)**2+4*b*epsilon*nu['R']))/(2*b)
    return {'R': r, 'K': k, 'G': 1-k-r}


class InnovationChecks(unittest.TestCase):
    def test_roots_match_transmission_and_attract_boundary_populations(self):
        for rho in [0., 18/91, .3, 50/123, 2/3, 1.]:
            for epsilon in [.01, .2, .8]:
                for nu in [dict(R=.2, K=.3, G=.5), dict(R=.7, K=.2, G=.1)]:
                    target = fixed_point(rho, epsilon, nu)
                    mapped = innovate(target, rho, epsilon, nu)
                    for kind in 'RKG':
                        self.assertAlmostEqual(target[kind], mapped[kind], places=12)
                        self.assertGreaterEqual(target[kind]+1e-15, epsilon*nu[kind])
                    for initial in 'RKG':
                        state = {kind: float(kind == initial) for kind in 'RKG'}
                        for _ in range(800):
                            state = innovate(state, rho, epsilon, nu)
                        for kind in 'RKG':
                            self.assertAlmostEqual(state[kind], target[kind], places=10)

    def test_random_matching_small_innovation_coefficients(self):
        nu, epsilon = dict(R=.2, K=.3, G=.5), 1e-7
        target = fixed_point(0., epsilon, nu)
        self.assertAlmostEqual(target['R']/epsilon, 32*nu['R']/9, places=5)
        self.assertAlmostEqual((target['K']-50/73)/epsilon,
                               96/23*(nu['K']-50/73), places=5)

    def test_critical_square_root_and_noncritical_linear_scales(self):
        nu, epsilon = dict(R=.2, K=.3, G=.5), 1e-10
        cases = [(18/91, 'R', 10*sqrt(nu['R']/73)),
                 (50/123, 'K', 10*sqrt(123*nu['K'])/73),
                 (2/3, 'R', 2*sqrt(nu['R']))]
        for rho, kind, coefficient in cases:
            actual = fixed_point(rho, epsilon, nu)[kind]/sqrt(epsilon)
            self.assertAlmostEqual(actual, coefficient, delta=3e-5)
        target = fixed_point(.9, epsilon, nu)
        self.assertAlmostEqual(target['K']/epsilon, 100*nu['K']/(123*.9-50), places=7)
        self.assertAlmostEqual(target['R']/epsilon, 4*nu['R']/(3*.9-2), places=7)

    def test_complete_innovation_is_exact_replacement(self):
        nu = dict(R=.2, K=.3, G=.5)
        for rho in [0., .5, 1.]:
            state = innovate(dict(R=1., K=0., G=0.), rho, 1., nu)
            self.assertEqual(state, nu)


if __name__ == '__main__':
    unittest.main()
