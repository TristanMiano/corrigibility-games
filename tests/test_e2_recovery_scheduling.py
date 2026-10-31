"""Independent LP and time-discretization checks for note 024.

Exact vertices check the two-stock work/time formula. Upper/lower fluid queue
discretizations check the parallel frontier, with an explicit finite-mesh
bracket. These do not establish the continuous proofs or calibrate physics.
"""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random
import unittest

from test_e2_population import solve_three
from test_e2_results import frontier as aggregate_frontier


def serial_frontier(o, d, work, time, c, tau, w, recovery_time, capacity):
    if capacity == 0:
        return F(0)
    a = max(tau, 1/capacity)
    return min(o+d, work/c, (work+w*o)/(c+w), time/a,
               (time+recovery_time*o)/(a+recovery_time))


def one_resource(o, budget, base, costs, stocks):
    (low, stock_low), (high, _) = sorted(zip(costs, stocks))
    return min(budget/base, (budget+low*o)/(base+low),
               (budget+high*o+(high-low)*stock_low)/(base+high))


def two_stock_formula(o, stocks, work, time, c, a, costs, delays):
    bounds = [o+sum(stocks), one_resource(o, work, c, costs, stocks),
              one_resource(o, time, a, delays, stocks)]
    if (costs[0]-costs[1])*(delays[0]-delays[1]) < 0:
        expensive = 0 if costs[0] > costs[1] else 1
        cheap = 1-expensive
        lam = delays[cheap]-delays[expensive]
        mu = costs[expensive]-costs[cheap]
        v = lam*costs[expensive]+mu*delays[expensive]
        bounds.append((lam*work+mu*time+v*o)/(lam*c+mu*a+v))
    return min(bounds)


def two_stock_vertices(o, stocks, work, time, c, a, costs, delays):
    constraints = [(-1, 0, 0, 0), (1, 0, 0, stocks[0]),
                   (0, -1, 0, 0), (0, 1, 0, stocks[1]),
                   (0, 0, -1, 0), (-1, -1, 1, o),
                   (*costs, c, work), (*delays, a, time)]
    result = []
    for active in combinations(constraints, 3):
        point = solve_three(active)
        if point is not None and all(sum(x*y for x, y in zip(row[:3], point)) <= row[3]
                                     for row in constraints):
            result.append(point)
    return result


def fluid_queue(o, d, production_rate, recovery_rate, latency, time, steps, upper):
    # Arrivals released at a mesh interval's start/end bracket continuous supply.
    dt = time/steps
    inventory, output, released = o, 0., 0.
    for j in range(steps):
        available_recovery = min(d, recovery_rate*max(0., (j+1)*dt-latency))
        arrival = available_recovery-released
        if upper:
            inventory += arrival
        produced = min(inventory, production_rate*dt)
        inventory -= produced
        output += produced
        if not upper:
            inventory += arrival
        released = available_recovery
    return output


class RecoverySchedulingChecks(unittest.TestCase):
    def test_aggregate_serial_counterexample(self):
        args = tuple(map(F, (0, 1, 2, 1, 1, 1, 1, 1)))+(F(1, 2),)
        self.assertEqual(aggregate_frontier(*args), F(1, 2))
        self.assertEqual(serial_frontier(*args), F(1, 3))
        self.assertEqual(F(1, 2)+F(1, 2)/F(1, 2), F(3, 2))

    def test_factor_two_and_unchanged_fast_capacity_cases(self):
        rng = Random(2401)
        for _ in range(100):
            o, d, work, time = [F(rng.randrange(5)) for _ in range(4)]
            c, tau = F(rng.randrange(1, 4)), F(rng.randrange(1, 4))
            w, recovery = F(rng.randrange(4)), F(rng.randrange(4))
            capacity = F(rng.randrange(1, 6), 3)
            args = (o, d, work, time, c, tau, w, recovery, capacity)
            old, actual = aggregate_frontier(*args), serial_frontier(*args)
            self.assertLessEqual(actual, old)
            self.assertLessEqual(old, 2*actual)
            if capacity*tau >= 1:
                self.assertEqual(actual, old)
        for n in [1, 3, 10, 100]:
            args = (F(0), F(1), F(2), F(1), F(1), F(1), F(1), F(n), F(1, n+1))
            self.assertEqual(aggregate_frontier(*args)/serial_frontier(*args), F(2*n+1, n+1))

    def test_two_stock_formula_against_exact_vertices(self):
        cases = []
        for costs_delays in product([F(0), F(1), F(3)], repeat=4):
            cases.append((F(1, 3), (F(2), F(1)), F(5), F(4), F(1), F(3, 2),
                          costs_delays[:2], costs_delays[2:]))
        rng = Random(2402)
        for _ in range(35):
            cases.append((F(rng.randrange(4)), (F(rng.randrange(4)), F(rng.randrange(4))),
                          F(rng.randrange(7)), F(rng.randrange(7)),
                          F(rng.randrange(1, 4)), F(rng.randrange(1, 4)),
                          (F(rng.randrange(4)), F(rng.randrange(4))),
                          (F(rng.randrange(4)), F(rng.randrange(4)))))
        for case in cases:
            self.assertEqual(two_stock_formula(*case), max(p[2] for p in two_stock_vertices(*case)))

    def test_joint_resource_condition_is_necessary(self):
        o, stocks, work, time, c, a = F(0), (F(1), F(1)), F(3), F(3), F(1), F(1)
        costs, delays = (F(3), F(1)), (F(1), F(3))
        self.assertEqual(one_resource(o, work, c, costs, stocks), F(5, 4))
        self.assertEqual(one_resource(o, time, a, delays, stocks), F(5, 4))
        self.assertEqual(two_stock_formula(o, stocks, work, time, c, a, costs, delays), F(1))
        self.assertIn((F(1, 2), F(1, 2), F(1)),
                      two_stock_vertices(o, stocks, work, time, c, a, costs, delays))

    def test_parallel_frontier_between_independent_queue_meshes(self):
        for o, d, kappa, nu, latency, time in product([0., .3], [1., 2.],
                [.5, 2.], [.7, 3.], [0., .25, 2.], [1., 1.5]):
            exact = min(o+d, kappa*time, o+min(kappa, nu)*max(time-latency, 0.))
            lower = fluid_queue(o, d, kappa, nu, latency, time, 400, False)
            upper = fluid_queue(o, d, kappa, nu, latency, time, 400, True)
            self.assertLessEqual(lower, exact+1e-11)
            self.assertGreaterEqual(upper+1e-11, exact)
            self.assertLessEqual(upper-lower, kappa*time/400+1e-10)


if __name__ == '__main__':
    unittest.main()
