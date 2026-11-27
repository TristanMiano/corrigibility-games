"""Exact checks for the sequential commissioning game in notes 220–221.

Run from the repository root with python experiments/r0008_sequential_evidence.py.
All comparisons use rational arithmetic; decimals in the printed summary are display only.
"""

from dataclasses import dataclass
from fractions import Fraction
from functools import cache


F = Fraction
SENSITIVITY = F(4, 5)
FALSE_PASS = F(1, 5)


@dataclass(frozen=True)
class Rule:
    name: str
    accept_genuine: Fraction
    accept_retained: Fraction
    trials_genuine: Fraction
    trials_retained: Fraction


RETURN = Rule("return", F(0), F(0), F(0), F(0))
RELEASE = Rule("release", F(1), F(1), F(0), F(0))


@dataclass(frozen=True)
class Job:
    buyer_good_gain: Fraction = F(4)
    buyer_bad_loss: Fraction = F(2)
    trial_cost: Fraction = F(7, 200)
    supplier_good_rent: Fraction = F(2)
    supplier_bad_rent: Fraction = F(4)
    supplier_fallback_difference: Fraction = F(0)
    success: Fraction = F(4, 5)
    expense_ceiling: Fraction = F(7, 5)

    def buyer_gain(self, rule, prior):
        good_return = self.buyer_good_gain * rule.accept_genuine
        bad_return = -self.buyer_bad_loss * rule.accept_retained
        good_return -= self.trial_cost * rule.trials_genuine
        bad_return -= self.trial_cost * rule.trials_retained
        return prior * good_return + (1 - prior) * bad_return

    def successful_edit_gain(self, rule):
        return (
            self.supplier_fallback_difference
            + self.supplier_good_rent * rule.accept_genuine
            - self.supplier_bad_rent * rule.accept_retained
        )

    def genuine_rate(self, rule):
        cutoff = self.success * self.successful_edit_gain(rule)
        attempt = min(F(1), max(F(0), cutoff / self.expense_ceiling))
        return self.success * attempt


def threshold_rule(lower_steps, upper_steps):
    width = lower_steps + upper_steps
    denominator = 4**width - 1
    retained = F(4**lower_steps - 1, denominator)
    genuine = 4**upper_steps * retained
    return Rule(
        f"({lower_steps},{upper_steps})",
        genuine,
        retained,
        (width * genuine - lower_steps) / F(3, 5),
        (lower_steps - width * retained) / F(3, 5),
    )


def possible_rules(job):
    """A uniform bound on distances before another trial costs more than stopping."""
    rules = [RETURN, RELEASE]
    g, h, c = job.buyer_good_gain, job.buyer_bad_loss, job.trial_cost
    if c <= 0:
        raise ValueError("The finite bound requires a positive trial cost.")
    if c >= g * h / (g + h):
        return rules
    ratio = (h - c) * (g - c) / c**2
    steps = 0
    while 4**steps <= ratio:
        steps += 1
    for lower in range(1, steps + 1):
        for upper in range(1, steps + 1):
            rules.append(threshold_rule(lower, upper))
    return rules


def optimal_intervals(job):
    """Intersect the affine buyer comparisons for each policy on [0,1]."""
    rules = possible_rules(job)
    lines = []
    for rule in rules:
        intercept = job.buyer_gain(rule, 0)
        slope = job.buyer_gain(rule, 1) - intercept
        lines.append((rule, slope, intercept))
    intervals = []
    for rule, slope, intercept in lines:
        lower, upper = F(0), F(1)
        for _, other_slope, other_intercept in lines:
            difference = slope - other_slope
            target = other_intercept - intercept
            if difference > 0:
                lower = max(lower, target / difference)
            elif difference < 0:
                upper = min(upper, target / difference)
            elif target > 0:
                lower, upper = F(1), F(0)
            if lower > upper:
                break
        if lower <= upper:
            intervals.append((rule, lower, upper))
    return intervals


def equilibrium_rates(job):
    intervals = optimal_intervals(job)
    equilibria = {}
    for rule, lower, upper in intervals:
        prior = job.genuine_rate(rule)
        if lower <= prior <= upper:
            equilibria.setdefault(prior, set()).add(rule.name)
    endpoints = {point for _, lower, upper in intervals for point in (lower, upper)}
    for prior in endpoints:
        if not 0 < prior <= job.success:
            continue
        best = [rule for rule, lower, upper in intervals if lower <= prior <= upper]
        rates = [job.genuine_rate(rule) for rule in best]
        if rates and min(rates) <= prior <= max(rates):
            equilibria.setdefault(prior, set()).update(rule.name for rule in best)
    return equilibria


def strength_job(share):
    """Purchased evidence with the return-vs-contest continuations in note 207."""
    good_a = bad_a = good_b = bad_b = F(2)
    if share < F(1, 3):
        bad_a, bad_b = 3 * (1 - share), 3 * share
    if share > F(2, 3):
        good_a = bad_a = 3 * (1 - share)
        good_b = bad_b = 3 * share
    return Job(
        buyer_good_gain=6 - good_b,
        buyer_bad_loss=bad_b,
        supplier_good_rent=4 - good_a,
        supplier_bad_rent=6 - bad_a,
        supplier_fallback_difference=good_a - bad_a,
    )


def upper_outcomes(share):
    job = strength_job(share)
    equilibria = equilibrium_rates(job)
    prior = max(equilibria)
    best = [rule for rule in possible_rules(job) if rule.name in equilibria[prior]]
    best.sort(key=job.successful_edit_gain)
    low, high = best[0], best[-1]
    pure = next((rule for rule in best if job.genuine_rate(rule) == prior), None)
    if pure is None:
        target = job.expense_ceiling * prior / job.success**2
        lower_gain = job.successful_edit_gain(low)
        weight = (target - lower_gain) / (job.successful_edit_gain(high) - lower_gain)
    else:
        low = high = pure
        weight = F(0)
    genuine_pass = (1 - weight) * low.accept_genuine + weight * high.accept_genuine
    retained_pass = (1 - weight) * low.accept_retained + weight * high.accept_retained
    released = prior * genuine_pass + (1 - prior) * retained_pass
    combat = F(0)
    if share < F(1, 3):
        combat = (1 - prior) * (1 - retained_pass)
    if share > F(2, 3):
        combat = 1 - released
    return prior, released, combat


def finite_best_response(job, prior, horizon):
    """Solve the buyer's finite tree and propagate state-conditional outcomes."""
    initial_odds = prior / (1 - prior)

    @cache
    def solve(evidence, remaining):
        odds = initial_odds * F(4) ** evidence
        posterior = odds / (1 + odds)
        stop = max((RETURN, RELEASE), key=lambda a: job.buyer_gain(a, posterior))
        stopping_loss = min(
            job.buyer_good_gain * posterior,
            job.buyer_bad_loss * (1 - posterior),
        )
        if remaining == 0 or stopping_loss <= job.trial_cost:
            return stop
        positive = solve(evidence + 1, remaining - 1)
        negative = solve(evidence - 1, remaining - 1)
        sampled = Rule(
            "sample",
            SENSITIVITY * positive.accept_genuine + (1 - SENSITIVITY) * negative.accept_genuine,
            FALSE_PASS * positive.accept_retained + (1 - FALSE_PASS) * negative.accept_retained,
            1 + SENSITIVITY * positive.trials_genuine + (1 - SENSITIVITY) * negative.trials_genuine,
            1 + FALSE_PASS * positive.trials_retained + (1 - FALSE_PASS) * negative.trials_retained,
        )
        if job.buyer_gain(sampled, posterior) > job.buyer_gain(stop, posterior):
            return sampled
        return stop

    return solve(0, horizon)


def main():
    job = Job()
    rule = threshold_rule(4, 2)
    assert (rule.accept_genuine, rule.accept_retained) == (F(272, 273), F(17, 273))
    assert (rule.trials_genuine, rule.trials_retained) == (F(300, 91), F(550, 91))
    prior = job.genuine_rate(rule)
    assert prior == F(1088, 1365)
    equilibria = equilibrium_rates(job)
    assert prior in equilibria
    for rate, names in sorted(equilibria.items()):
        print(f"Genuine rate {float(rate):.8f}, optimal responses {sorted(names)}")
    for horizon in (10, 30, 60, 100):
        candidate = finite_best_response(job, prior, horizon)
        actual = job.genuine_rate(candidate)
        confirmed = finite_best_response(job, actual, horizon)
        if candidate != confirmed:
            raise AssertionError(f"Check the proposed finite assessment at {horizon} trials.")
        print(
            f"Deadline {horizon:3d}, genuine {float(actual):.9f}, "
            f"buyer gain {float(job.buyer_gain(confirmed, actual)):.9f}"
        )
    for share in (F(1, 100), F(1, 50), F(1, 20), F(1, 5), F(1, 2), F(4, 5)):
        outcomes = upper_outcomes(share)
        print(f"Strength {float(share):.2f}, genuine/release/contest", *(f"{float(x):.7f}" for x in outcomes))


if __name__ == "__main__":
    main()
