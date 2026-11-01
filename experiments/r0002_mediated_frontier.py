"""Explore the finite-collateral mediated ordinary frontier in note 044.

Optional research computation: Python + scipy.optimize.linprog (checked locally
with SciPy 1.15.3). Run: python experiments/r0002_mediated_frontier.py
No random samples. Printed rationalizations are candidates, not exact proofs.
The analytical note and standard-library tests carry the proved statements.
"""
from fractions import Fraction
import json

from scipy.optimize import linprog


PROFILES = ((0, 0), (1, 0), (0, 1), (1, 1))


def solve_frontier(reserve=3, ca=1.6, cb=1.6, a=.1, b=.4, output=10):
    # Per profile: q, q*g_A0, q*g_A1, q*g_B0, q*g_B1.
    n = 20
    rows, rhs = [], []
    payoffs = [[0.0]*n for _ in range(2)]
    costs = (ca, cb)
    probabilities = (0, a, a, b)

    def add(entries, bound=0):
        row = [0.0]*n
        for index, coefficient in entries:
            row[index] += coefficient
        rows.append(row)
        rhs.append(bound)

    for j, effort in enumerate(PROFILES):
        base = 5*j
        p = probabilities[j]
        for k in (0, 1):
            add(((base+1+k, 1), (base+3+k, 1), (base, -k*output)))
        for i, cost in enumerate(costs):
            for k in (0, 1):
                add(((base+1+2*i+k, -1), (base, -(reserve-cost))))
            payoffs[i][base] = -cost*effort[i]
            payoffs[i][base+1+2*i] = 1-p
            payoffs[i][base+2+2*i] = p

    # Obedience conditional on each private action recommendation. These are
    # deliberately coarse constraints; more information can only restrict them.
    for i, cost in enumerate(costs):
        for recommendation in (0, 1):
            entries = []
            sign = 1 if recommendation == 0 else -1
            for j, effort in enumerate(PROFILES):
                if effort[i] != recommendation:
                    continue
                marginal = (b-a) if effort[1-i] else a
                base = 5*j
                entries += [(base, -sign*cost),
                            (base+1+2*i, -sign*marginal),
                            (base+2+2*i, sign*marginal)]
            add(entries)

    # The reported cooperative frontier must also be acceptable to both
    # original agents relative to retained stocks.
    for payoff in payoffs:
        rows.append([-v for v in payoff])
        rhs.append(0)
    objective = [-sum(v) for v in zip(*payoffs)]
    normalization = [1.0 if j % 5 == 0 else 0.0 for j in range(n)]
    bounds = [(0, 1) if j % 5 == 0 else (None, None) for j in range(n)]
    result = linprog(objective, A_ub=rows, b_ub=rhs,
                     A_eq=[normalization], b_eq=[1], bounds=bounds,
                     method="highs")
    if not result.success:
        raise RuntimeError(result.message)
    residual = max(sum(c*x for c, x in zip(row, result.x))-r
                   for row, r in zip(rows, rhs))
    rational = lambda x: str(Fraction(float(x)).limit_denominator(100000))
    mechanism = []
    for j, effort in enumerate(PROFILES):
        mass = result.x[5*j]
        if mass > 1e-8:
            mechanism.append({
                "recommendation": effort,
                "probability": rational(mass),
                "transfers_A0_A1_B0_B1": [
                    rational(result.x[5*j+k]/mass) for k in range(1, 5)
                ],
            })
    return {
        "reserve_each": reserve,
        "ordinary_net_surplus": rational(-result.fun),
        "net_payoffs": [rational(sum(c*x for c, x in zip(row, result.x)))
                        for row in payoffs],
        "max_constraint_residual": residual,
        "mechanism": mechanism,
    }


if __name__ == "__main__":
    for wealth in (3, 4, 5, 10, 100):
        print(json.dumps(solve_frontier(wealth)))
