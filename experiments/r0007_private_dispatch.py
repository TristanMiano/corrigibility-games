"""Exact three-site inspection and dispatch checks for E8 notes 195–198.

Run with python experiments/r0007_private_dispatch.py. Pass --plot FILE.png to
render the findings figure with matplotlib (the rational checks need only Python).
"""
import argparse
from fractions import Fraction as F
from itertools import product
from pathlib import Path


X, Q, COST = F(7, 10), F(1, 5), F(1, 25)
D = Q - COST
DAMAGE = X - 3 * Q + COST
CUT = F(1408, 17325)
STRONG_PRICE = F(1, 25)


def fair_fallback(price):
    """Return the three original outside incomes and dispute probability."""
    inspect = F(11, 19)
    early = F(2, 3) * inspect
    later = (D - F(3, 2) * price) / Q
    assert 0 <= later <= 1
    returns = (
        (1-later)*X/3 + later*Q,
        early*Q + (1-early)*(D+later*COST),
        early*Q + (1-early)*D,
    )
    contest = early + (1-early)*later
    assert sum(returns) == X-contest*DAMAGE-price*inspect
    return returns, contest


def dispatch(price):
    """Latent physical destination, privately recommended initiator and joint mass."""
    (_, second, third), _ = fair_fallback(price)
    contest = max(F(0), (D*(second+third)/X-price)/(COST+D*(Q+D)/X))
    early = F(78832, 262257)*max(F(0), 1-price/CUT)
    second_peace = (second-contest*Q+early*COST)/X
    third_peace = (third-contest*D-early*COST)/X
    first_peace = 1-contest-second_peace-third_peace
    cells = [
        (0, None, first_peace), (1, None, second_peace),
        (2, None, third_peace), (2, 1, early), (1, 2, contest-early),
    ]
    assert min(mass for _, _, mass in cells) >= 0
    assert sum(mass for _, _, mass in cells) == 1
    return cells


def material(site, destination, initiator):
    if initiator is None:
        return X * (site == destination)
    return Q - COST * (site == initiator)


def verify_deviations(price):
    """Evaluate pure replacement policies on the joint cells, including full inspection."""
    cells = dispatch(price)
    gains = [
        sum(mass*material(site, dest, called) for dest, called, mass in cells)
        for site in range(3)
    ]
    for inspect in (False, True):
        # A can observe the exact recipient if it pays. It receives no ordinary message.
        for actions in product((False, True), repeat=3 if inspect else 1):
            alternative = -price*inspect
            for dest, called, mass in cells:
                act = actions[dest if inspect else 0]
                first = 0 if act else called
                alternative += mass*material(0, dest, first)
            assert alternative <= gains[0], (price, "A", inspect, actions)
    for site in (1, 2):
        # The signal says whether this site was designated to move. An already
        # completed upstream initiative leaves no later choice at this site.
        for pass_signal, act_signal in product((False, True), repeat=2):
            alternative = F(0)
            for dest, called, mass in cells:
                action = act_signal if called == site else pass_signal
                if called is not None and called < site:
                    first = called
                elif action:
                    first = site
                else:
                    first = called if called is not None and called > site else None
                alternative += mass*material(site, dest, first)
            assert alternative <= gains[site], (price, site, pass_signal, act_signal)
    contest = sum(mass for _, called, mass in cells if called is not None)
    required, _ = fair_fallback(price)
    assert gains[1:] == list(required[1:])
    assert gains[0] >= required[0]
    assert sum(gains) == X-DAMAGE*contest
    assert contest == max(0, (1408-17325*price)/2033)
    return contest, gains


def make_figure(output):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import PercentFormatter

    prices = [F(i, 2000) for i in range(201)]
    ordinary = [verify_deviations(h)[0] for h in prices]
    baseline = [fair_fallback(h)[1] for h in prices]
    switch = (1408-2033*STRONG_PRICE/DAMAGE)/17325
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(8.4, 6.1), sharex=True)
    fig.subplots_adjust(top=0.87, bottom=0.13, left=0.11, right=0.965, hspace=0.31)
    fig.suptitle("When is a goal change worth buying?", x=0.11, ha="left",
                 fontsize=18, weight="bold")
    xs = [float(h) for h in prices]
    top.plot(xs, [float(v) for v in baseline], color="#7e7165", linestyle="--",
             label="Fair lottery with private inspection")
    top.plot(xs, [float(v) for v in ordinary], color="#13566a", linewidth=2.6,
             label="Best ordinary dispatcher")
    top.set_ylabel("Jobs disputed")
    top.yaxis.set_major_formatter(PercentFormatter(1))
    top.set_ylim(-0.035, 1)
    top.legend(loc="upper right", frameon=False, fontsize=9)
    premium = [float(DAMAGE*v) for v in ordinary]
    bottom.plot(xs, premium, color="#13566a", linewidth=2.6, label="Maximum price worth paying")
    bottom.axhline(float(STRONG_PRICE), linestyle="--", color="#9b4c27",
                   label="Offered installation price (0.04)")
    bottom.axvspan(0, float(switch), color="#d8ede4", alpha=0.68, zorder=-3)
    bottom.text(0.003, 0.006, "Genuine change purchased", fontsize=9, color="#22624c")
    bottom.set_ylabel("Units of intact output")
    bottom.set_xlabel("Cost to learn the recipient before release (units of output)")
    bottom.set_ylim(-0.004, 0.11)
    bottom.legend(loc="upper right", frameon=False, fontsize=9)
    for ax in (top, bottom):
        ax.set_xlim(0, 0.1)
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(axis="y", color="#d5d9d9", lw=0.7)
        ax.set_axisbelow(True)
    fig.savefig(output, dpi=180, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plot", type=Path, metavar="FILE.png")
    args = parser.parse_args()
    for price in (F(0), F(1, 100), F(1, 25), F(2, 25), CUT, F(8, 75)):
        dispute, returns = verify_deviations(price)
        print(f"h={price}: ordinary conflict={dispute}, installation premium={DAMAGE*dispute}")
    if args.plot:
        make_figure(args.plot)
