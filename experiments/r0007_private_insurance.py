"""Rational primal and dual welfare certificates for the three-tier case in note 160.

Run with: python experiments/r0007_private_insurance.py
"""

from fractions import Fraction as F
from itertools import product
from math import prod


MASS = {1: F(1, 2), 2: F(1, 8), 3: F(3, 8)}
CURVATURE = F(1, 16)
STOCK = 3
SITES = 3
MULTIPLIER = {(2, 1): F(2646, 100000), (3, 2): F(1135, 100000)}
ROBUST_MULTIPLIER = {(2, 1): F(3294, 100000), (3, 2): F(1398, 100000)}


def utility(income):
    return income - CURVATURE * income**2 / 2


def coefficients(report, multipliers):
    """Coefficients of f(income), served*income and served in the upper bound."""
    weight = F(1)
    slope = F(0)
    constant = F(0)
    for (actual, mimicked), multiplier in multipliers.items():
        if report == actual:
            weight += multiplier
        if report == mimicked:
            scaled = multiplier * MASS[actual] / MASS[mimicked]
            extra = actual - mimicked
            weight -= scaled
            slope += scaled * CURVATURE * extra
            constant -= scaled * utility(extra)
    return weight, slope, constant


def optimal_settlement(reports, winner, multipliers):
    """Maximize the concave dual score for one served site or an idle slot."""
    weights, slopes, constants = [], [], []
    for site, report in enumerate(reports):
        weight, slope, constant = coefficients(report, multipliers)
        assert weight > 0
        weights.append(weight)
        slopes.append(slope if site == winner else F(0))
        constants.append(constant if site == winner else F(0))
    output = reports[winner] if winner is not None else 0
    marginal = max(F(0), (sum(1 + b/w for b, w in zip(slopes, weights)) - CURVATURE*output)
                   / sum(1/w for w in weights))
    incomes = tuple((w+b-marginal)/(CURVATURE*w) for w, b in zip(weights, slopes))
    assert sum(incomes) <= output
    score = sum(w*utility(y) + b*y + c
                for w, b, c, y in zip(weights, slopes, constants, incomes))
    return score, incomes


def certificate(multipliers, check_mass=MASS):
    policies = {}
    lower = upper = insured = F(0)
    for reports in product(MASS, repeat=SITES):
        probability = prod(MASS[report] for report in reports)
        candidates = {winner: optimal_settlement(reports, winner, multipliers)
                      for winner in (None, *range(SITES))}
        best = max(score for score, _ in candidates.values())
        maximizing = [(winner, incomes) for winner, (score, incomes) in candidates.items()
                      if score == best]
        policies[reports] = maximizing
        upper += probability * best
        insured += probability * SITES * utility(F(max(reports), SITES))
        for winner, incomes in maximizing:
            assert winner is not None and reports[winner] == max(reports)
            transfers = [y-(report if i == winner else 0)
                         for i, (y, report) in enumerate(zip(incomes, reports))]
            assert sum(transfers) == 0 and min(transfers) >= -STOCK
            lower += probability * sum(map(utility, incomes)) / len(maximizing)

    # Symmetric tie-breaking. Check every deviation by every site, including
    # deviations across two levels. Transfer is held fixed, true service changes.
    margins = []
    radii = []
    for site, actual, lie in product(range(SITES), MASS, MASS):
        if actual == lie:
            continue
        advantage = {}
        for others in product(MASS, repeat=SITES-1):
            profile = list(others)
            profile.insert(site, actual)
            true_choices = policies[tuple(profile)]
            profile[site] = lie
            false_choices = policies[tuple(profile)]
            true = sum(utility(y[site]) for _, y in true_choices)/len(true_choices)
            false = sum(utility(y[site]+(actual-lie if i == site else 0))
                        for i, y in false_choices)/len(false_choices)
            advantage[others] = true-false
        margin = sum(prod(check_mass[t] for t in others)*gain
                     for others, gain in advantage.items())
        spread = max(advantage.values())-min(advantage.values())
        margins.append(margin)
        if spread:
            radii.append(margin/((SITES-1)*spread))
    # Welfare quantities are all at the design prior. The optional check
    # prior changes only the interim reporting incentives.
    return lower, upper, insured, min(margins), min(radii)


if __name__ == "__main__":
    ordinary_lower, ordinary_upper, full, margin, radius = certificate(MULTIPLIER)
    assert ordinary_lower <= ordinary_upper < full and margin > 0
    print(f"Feasible ordinary welfare     {float(ordinary_lower):.10f}")
    print(f"Upper bound on ordinary welfare {float(ordinary_upper):.10f}")
    print(f"Full insurance welfare        {float(full):.10f}")
    print(f"Smallest truthful-report gain {float(margin):.10f}")
    print(f"Certified prior TV radius     {float(radius):.10f}")
    robust_lower, _, _, robust_margin, robust_radius = certificate(ROBUST_MULTIPLIER)
    assert robust_margin > 0 and robust_radius > F(28, 1000)
    print(f"Robust ordinary welfare       {float(robust_lower):.10f}")
    print(f"Robust prior TV radius        {float(robust_radius):.10f}")
    shifted = {1: MASS[1]+F(1, 1000), 2: MASS[2]-F(1, 1000), 3: MASS[3]}
    assert certificate(MULTIPLIER, shifted)[3] < 0
