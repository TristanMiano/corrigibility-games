"""Exact rational interval checks for r0002's logarithmic examples.

Run with Python's standard library: python experiments/r0002_welfare_checks.py
Log bounds use the positive atanh series with an explicit remainder bound.
These verify specified finite inequalities; they are not a formal proof checker.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import comb


@lru_cache(maxsize=None)
def log_bounds(x, terms=80):
    """Return rational lower/upper bounds on log(x), for rational x >= 1."""
    x = F(x)
    if x < 1:
        lower, upper = log_bounds(1/x, terms)
        return -upper, -lower
    t = (x-1)/(x+1)
    lower = 2*sum((t**(2*j+1)/F(2*j+1) for j in range(terms)), F(0))
    tail = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return lower, lower+tail


def binomial(n, probability):
    return {j: F(comb(n, j))*probability**j*(1-probability)**(n-j)
            for j in range(n+1)}


def success_law(full, solo, rho=F(1, 10)):
    """Mixture: independent Bernoulli signals or one common uniform shock."""
    law = {}
    for j, pj in binomial(full, F(2, 5)).items():
        for k, pk in binomial(solo, F(1, 10)).items():
            law[j+k] = law.get(j+k, F(0))+(1-rho)*pj*pk
    for count, probability in ((full+solo, F(1, 10)),
                               (full, F(3, 10)), (0, F(3, 5))):
        law[count] = law.get(count, F(0))+rho*probability
    assert sum(law.values()) == 1
    return law


def expected_log(law):
    lower = upper = F(0)
    for argument, probability in law.items():
        lo, hi = log_bounds(argument)
        lower += probability*lo
        upper += probability*hi
    return lower, upper


def welfare_bound(n, full, solo, *, reserve=F(3), setup=F(1, 20),
                  partition_cost=F(1, 100), rho=F(1, 10)):
    """Half of maximal original log welfare, allowing equal ex-post division.

    Even an effort-unobservable allocator is granted this statewise optimal
    division for the upper bound. Full effort actually attains it.
    """
    z0 = (1+reserve-setup-partition_cost*(n-1)
          -F(8, 5)*(2*full+solo)/(2*n))
    law = {z0+F(5*j, n): p for j, p in success_law(full, solo, rho).items()}
    return expected_log(law)


def one_shirk_log(n=3, rho=F(1, 10)):
    # Other modules retain both contributions; one module has only the peer's.
    # Transfers remain those of full-effort equal output division. The shirker
    # privately saves c/n of its own stock; it is not charged half that saving.
    z0 = F(4)-F(1, 20)-F(n-1, 100)-F(8, 5)+F(8, 5*n)
    law = {z0+F(5*j, n): p for j, p in success_law(n-1, 1, rho).items()}
    return expected_log(law)


def audit_three_partition_witness():
    full_lo, full_hi = welfare_bound(3, 3, 0)
    stock_lo, stock_hi = log_bounds(F(4))
    assert full_lo-stock_hi > F(1, 100)
    competitors = []
    for n in range(1, 4):
        for full in range(n+1):
            for solo in range(n-full+1):
                if (n, full, solo) == (3, 3, 0):
                    continue
                lo, hi = welfare_bound(n, full, solo)
                assert full_lo > hi, (n, full, solo)
                competitors.append((hi, n, full, solo))
    shirk_lo, shirk_hi = one_shirk_log()
    assert shirk_lo > full_hi
    return {
        "adoption_gain_lower": float(full_lo-stock_hi),
        "adoption_gain_upper": float(full_hi-stock_lo),
        "best_other_profile_n_full_solo": max(competitors)[1:],
        "gap_over_other_profiles_lower": float(full_lo-max(competitors)[0]),
        "ordinary_one_shirk_gain_lower": float(shirk_lo-full_hi),
    }


if __name__ == '__main__':
    print(audit_three_partition_witness())
