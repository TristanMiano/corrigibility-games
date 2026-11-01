"""Separate finite LP calculations checking r0002's contract derivations.

The LP includes every binary-output contingent expected allocation with finite
collateral and optional destruction, rather than only the displayed contracts.
Exact vertices check proposal optima and the ordinary punishment comparison.
This is supporting computation, not an independent or machine-checked proof.
"""
from fractions import Fraction as F
from itertools import combinations
import unittest


def solve_square(rows):
    """Solve the selected affine equalities by exact Gaussian elimination."""
    n = len(rows)
    a = [[F(x) for x in row] for row in rows]
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        divisor = a[col][col]
        a[col] = [x / divisor for x in a[col]]
        for i in range(n):
            if i != col:
                multiple = a[i][col]
                a[i] = [x - multiple * y for x, y in zip(a[i], a[col])]
    return tuple(row[-1] for row in a)


def vertices(constraints, dimension=4):
    points = set()
    for active in combinations(constraints, dimension):
        point = solve_square(active)
        if point is not None and all(
            sum(coef * value for coef, value in zip(row[:-1], point)) <= row[-1]
            for row in constraints
        ):
            points.add(point)
    return points


def contract_polytope(lam, mu, reservation, *, ca=F(8, 5), cb=F(8, 5),
                      a=F(1, 10), b=F(2, 5), output=F(10), reserve=F(3)):
    # Variables: g_A^0, g_A^1, g_B^0, g_B^1. All rows are <=.
    delta = b - a
    rows = [
        (1, 0, 1, 0, 0),                 # Failure transfers, including waste.
        (0, 1, 0, 1, output),            # Success material budget.
        (-1, 0, 0, 0, reserve - ca),
        (0, -1, 0, 0, reserve - ca),
        (0, 0, -1, 0, reserve - cb),
        (0, 0, 0, -1, reserve - cb),
        (delta, -delta, delta * lam, -delta * lam, -ca),
        (delta * mu, -delta * mu, delta, -delta, -cb),
        (-(1-b), -b, -lam*(1-b), -lam*b,
         -reservation-ca-lam*cb),
    ]
    return [[F(x) for x in row] for row in rows]


def outcomes(point, *, ca=F(8, 5), cb=F(8, 5), b=F(2, 5)):
    a0, a1, b0, b1 = point
    return (1-b)*a0+b*a1-ca, (1-b)*b0+b*b1-cb


class ProductiveContractCertificates(unittest.TestCase):
    def test_original_goals_and_all_contingent_waste_contracts(self):
        points = vertices(contract_polytope(F(0), F(0), F(0)))
        self.assertTrue(points)
        self.assertEqual(max(outcomes(p)[1] for p in points), F(2, 5))
        self.assertEqual(max(sum(outcomes(p)) for p in points), F(2, 5))
        # Exact budget balance makes the mutual-effort polytope empty.
        balanced = contract_polytope(F(0), F(0), F(0))
        balanced += [[F(-1), 0, F(-1), 0, 0], [0, F(-1), 0, F(-1), F(-10)]]
        self.assertEqual(vertices(balanced), set())

    def test_low_goal_branch_against_complete_contract_lp(self):
        for lam in [F(0), F(1, 20), F(1, 10), F(3, 20)]:
            with self.subTest(lam=lam):
                mu = F(1, 5)
                points = vertices(contract_polytope(lam, mu, F(0)))
                predicted_b = F(4, 5)/(1-lam)
                self.assertEqual(max(outcomes(p)[1] for p in points), predicted_b)
                self.assertEqual(
                    max(outcomes(p)[1]+mu*outcomes(p)[0] for p in points),
                    (1-mu*lam)*predicted_b,
                )
                z = lam*F(4, 5)/(1-lam)
                witness = (-F(3, 5)-z, F(49, 10)-z,
                           F(3, 5)+z, F(51, 10)+z)
                self.assertTrue(all(
                    sum(c*x for c, x in zip(row[:-1], witness)) <= row[-1]
                    for row in contract_polytope(lam, mu, F(0))
                ))
                self.assertEqual(outcomes(witness), (-z, predicted_b))

    def test_efficient_default_protects_founder_for_varied_goals(self):
        for lam in [F(9, 50), F(1, 5), F(1, 2), F(4, 5)]:
            for mu in [F(0), F(1, 5), F(3, 5)]:
                with self.subTest(lam=lam, mu=mu):
                    reservation = F(1, 5)+lam*F(3, 5)
                    points = vertices(contract_polytope(lam, mu, reservation))
                    self.assertTrue(points)
                    self.assertGreaterEqual(min(outcomes(p)[0] for p in points), F(1, 5))
                    self.assertEqual(max(outcomes(p)[1] for p in points), F(3, 5))
                    self.assertEqual(
                        max(outcomes(p)[1]+mu*outcomes(p)[0] for p in points),
                        F(3, 5)+mu*F(1, 5),
                    )

    def test_loss_of_fallback_efficiency_has_exact_extraction_cost(self):
        lam, mu, surplus = F(1, 5), F(1, 5), F(4, 5)
        for rho in [F(0), F(1, 4), F(1, 2), F(3, 4), F(1)]:
            reservation = rho*(F(1, 5)+lam*F(3, 5))
            points = vertices(contract_polytope(lam, mu, reservation))
            predicted_a = rho*F(1, 5)-lam*(1-rho)*surplus/(1-lam)
            self.assertEqual(min(outcomes(p)[0] for p in points), predicted_a)
            self.assertEqual(max(outcomes(p)[1] for p in points), surplus-predicted_a)

    def test_ordinary_waste_bound_with_asymmetric_costs(self):
        for ca, cb in [(F(8, 5), F(8, 5)), (F(17, 10), F(17, 10)),
                       (F(11, 5), F(6, 5))]:
            with self.subTest(ca=ca, cb=cb):
                # A very low participation threshold tests the total-surplus bound,
                # including cases where productive ordinary contracts are not IR.
                points = vertices(contract_polytope(F(0), F(0), F(-10), ca=ca, cb=cb))
                predicted = F(10)-(1-F(1, 10))*(ca+cb)/(F(2, 5)-F(1, 10))
                self.assertEqual(max(sum(outcomes(p, ca=ca, cb=cb)) for p in points), predicted)


if __name__ == '__main__':
    unittest.main()
