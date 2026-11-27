"""Solve the unrestricted four-state disclosure problem in E9 notes 282–285.

Run python experiments/r0008_peaceful_evidence.py --spoilage 3 or add
--peaceful --confidence .95 --objective genuine. Requires scipy. Each LP
variable is a state/action *mass*. Even if an outcome is required to be
peaceful, the receiver remains free to contest every recommendation.
"""

import argparse
from dataclasses import dataclass

from scipy.optimize import linprog


STATES = ("genuine, vulnerable", "genuine, hard", "retained, vulnerable", "retained, hard")
MASSES = (.15, .60, .12, .13)
RELEASE, RETURN, CONTEST = range(3)
ACTIONS = ("release", "return", "contest")


@dataclass(frozen=True)
class Allocation:
    joint: float
    serving_genuine: float
    released: float
    contested: float
    rows: tuple


def solve(spoilage, *, settlement=0, peaceful=False, confidence=0, objective="stock"):
    if spoilage < 0 or settlement < 0 or not 0 <= confidence <= 1:
        raise ValueError("Costs must be nonnegative and confidence a probability.")
    if objective not in ("stock", "genuine"):
        raise ValueError("Unknown disclosure objective.")
    values, stocks, genuine, equalities = [], [], [], []
    for state in range(len(STATES)):
        agreed = state < 2
        vulnerable = state % 2 == 0
        values.append((4 if agreed else -spoilage, 2 + settlement, 5.4 if vulnerable else .6))
        stocks.extend((10 if agreed else 8-spoilage, 7.5, 6))
        genuine.extend((int(agreed), 0, 0))
        equalities.append([int(cell // len(ACTIONS) == state) for cell in range(12)])

    constraints = []
    for recommended in range(len(ACTIONS)):
        for deviation in range(len(ACTIONS)):
            if recommended == deviation:
                continue
            row = [0.0] * 12
            for state, payoff in enumerate(values):
                row[3*state + recommended] = payoff[deviation] - payoff[recommended]
            constraints.append(row)
    constraints.append([confidence - int(cell // 3 < 2) if cell % 3 == RELEASE else 0
                        for cell in range(12)])
    bounds = [(0, 0 if peaceful and cell % 3 == CONTEST else None) for cell in range(12)]
    target = stocks if objective == "stock" else genuine
    solution = linprog([-v for v in target], A_eq=equalities, b_eq=MASSES,
                       A_ub=constraints, b_ub=[0]*len(constraints), bounds=bounds, method="highs")
    if not solution.success:
        raise ValueError(solution.message)
    weights = solution.x
    rows = tuple(tuple(weights[3*s:3*s+3]) for s in range(4))
    return Allocation(
        joint=sum(w*v for w, v in zip(weights, stocks)),
        serving_genuine=sum(w*v for w, v in zip(weights, genuine)),
        released=sum(row[RELEASE] for row in rows),
        contested=sum(row[CONTEST] for row in rows),
        rows=rows,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spoilage", type=float, default=3)
    parser.add_argument("--settlement", type=float, default=0)
    parser.add_argument("--peaceful", action="store_true")
    parser.add_argument("--confidence", type=float, default=0)
    parser.add_argument("--objective", choices=("stock", "genuine"), default="stock")
    args = parser.parse_args()
    result = solve(**vars(args))
    print("State                    release    return   contest")
    for state, row in zip(STATES, result.rows):
        print(f"{state:21s} " + " ".join(f"{mass:9.6f}" for mass in row))
    print(f"Joint stock before bills {result.joint:.6f}. Genuine service {result.serving_genuine:.6f}. "
          f"All releases {result.released:.6f}. Combat {result.contested:.6f}.")
