"""Enumerate the buyer's complete strategies in E9's optional second-test game.

Run python experiments/r0008_receipt_game.py --price .20. The solver uses the
finite game tree directly. It does not use the price branches derived in note 264.
Costs, probabilities, best-response regions and equilibrium rates are rational.
"""

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import product

Q = F(4, 5)
COST_CEILING = 3

# Within each state: process pass / goal pass, pass / fail, fail / pass, fail / fail.
SIGN_LAWS = (
    (81, 9, 9, 1),  # Agreed goal installed
    (9, 81, 1, 9),  # Honest attempt failed
    (1, 9, 9, 81),  # Claimed attempt deliberately skipped
)


@dataclass(frozen=True)
class Reply:
    name: str
    read: bool
    release_good: bool
    release_bad: bool


REPLIES = (
    Reply("return", False, False, False),
    Reply("release", False, True, True),
    Reply("read and use positive", True, True, False),
    Reply("read and use negative", True, False, True),
    Reply("read and return", True, False, False),
    Reply("read and release", True, True, True),
)


@dataclass(frozen=True)
class Plan:
    replies: tuple
    incentive: F
    buyer_if_skipped: F
    buyer_slope: F

    def buyer_value(self, attempted):
        return self.buyer_if_skipped + self.buyer_slope * attempted


def measured_probabilities(replies, law):
    """Find the probabilities of release and of buying the second reading."""
    released = 0
    reads = 0
    for index, weight in enumerate(law):
        process_result, goal_result = divmod(index, 2)
        decision = replies[process_result]
        reads += weight * decision.read
        release = decision.release_good if goal_result == 0 else decision.release_bad
        released += weight * release
    return F(released, 100), F(reads, 100)


def complete_plans(price, process_bonus=F(0)):
    if price < 0 or process_bonus < 0:
        raise ValueError("The reading price and the process bonus must be nonnegative.")
    plans = []
    for replies in product(REPLIES, repeat=2):
        history_returns = []
        for index, law in enumerate(SIGN_LAWS):
            release, read = measured_probabilities(replies, law)
            paid = process_bonus * F(law[0] + law[1], 100)
            supplier = (2 if index == 0 else 4) * release + paid
            buyer = (4 if index == 0 else -2) * release - price * read - paid
            history_returns.append((supplier, buyer))
        genuine, failed, skipped = history_returns
        incentive = Q * genuine[0] + (1 - Q) * failed[0] - skipped[0]
        slope = Q * genuine[1] + (1 - Q) * failed[1] - skipped[1]
        plans.append(Plan(replies, incentive, skipped[1], slope))
    return plans


def best_response_region(plan, plans):
    """Intersect the original buyer payoff comparisons over priors in [0,1]."""
    low, high = F(0), F(1)
    for other in plans:
        intercept = plan.buyer_if_skipped - other.buyer_if_skipped
        slope = plan.buyer_slope - other.buyer_slope
        if slope > 0:
            low = max(low, -intercept / slope)
        elif slope < 0:
            high = min(high, -intercept / slope)
        elif intercept < 0:
            return None
        if high < low:
            return None
    return low, high


def equilibrium_intervals(price, process_bonus=F(0)):
    """Return all attempt-rate intervals allowing best replies by both sides."""
    plans = complete_plans(price, process_bonus)
    regions = []
    endpoints = {F(0), F(1)}
    for plan in plans:
        region = best_response_region(plan, plans)
        if region is not None:
            regions.append((*region, plan))
            endpoints.update(region)
    knots = sorted(endpoints)
    cells = [(k, k) for k in knots] + list(zip(knots, knots[1:]))
    solutions = []
    for left, right in cells:
        middle = (left + right) / 2
        incentives = [plan.incentive for lo, hi, plan in regions if lo <= middle <= hi]
        # The founder can face any mixture of the buyer's maximizing plans.
        f_low = max(F(0), min(F(1), min(incentives) / COST_CEILING))
        f_high = max(F(0), min(F(1), max(incentives) / COST_CEILING))
        lower, upper = max(left, f_low), min(right, f_high)
        if lower <= upper:
            solutions.append((lower, upper))
    merged = []
    for lower, upper in sorted(solutions):
        if merged and lower <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(upper, merged[-1][1]))
        else:
            merged.append((lower, upper))
    return merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--price", type=F, default=F(1, 5))
    parser.add_argument("--process-bonus", type=F, default=F(0))
    args = parser.parse_args()
    plans = complete_plans(args.price, args.process_bonus)
    for lower, upper in equilibrium_intervals(args.price, args.process_bonus):
        if lower != upper:
            print(f"Attempt interval [{lower}, {upper}], genuine interval [{Q*lower}, {Q*upper}]")
            continue
        value = max(plan.buyer_value(lower) for plan in plans)
        print(f"Attempts {lower}, genuine changes {Q*lower}, buyer gain {value} ({float(value):.4f})")


if __name__ == "__main__":
    main()
