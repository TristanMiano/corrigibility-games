"""Reproduce the one-inspection power/capability comparisons in E9, notes 207, 250 and 251.

    python experiments/r0008_verification_boundaries.py
    python experiments/r0008_verification_boundaries.py --figure research/reports/r0008-power.png

The selected equilibrium has the highest installation rate away from ties. At
a physical recovery tie both parties return the batch. At a test-price tie
with no strictly profitable interval we display the no-trade equilibrium.
Input fractions and all equilibrium outcomes, before plotting, are exact.
"""

from argparse import ArgumentParser
from dataclasses import dataclass
from fractions import Fraction as F
from functools import cache

SENSITIVITY = F(9, 10)
FALSE_POSITIVE = F(1, 10)
COST_CEILING = F(7, 5)
TEST_PRICE = F(1, 10)


@dataclass(frozen=True)
class Refusal:
    red: F
    blue: F
    combat: bool


@dataclass(frozen=True)
class Market:
    changed: Refusal
    retained: Refusal
    blue_gain: F
    blue_loss: F
    red_edit_premium: F
    lower_prior: F
    upper_prior: F
    active_interval: bool


@cache
def market(power, price=TEST_PRICE):
    """Choose fallback actions using each controller's own preferences."""
    if not 0 < power < 1 or price < 0:
        raise ValueError("Expected interior recovery probability and nonnegative test price.")
    recovered_red, recovered_blue = 3 * (1 - power), 3 * power
    contest = Refusal(recovered_red, recovered_blue, True)
    returned = Refusal(F(2), F(2), False)
    retained = contest if recovered_blue > 2 or recovered_red > 2 else returned
    changed = contest if recovered_blue > 2 or recovered_red + recovered_blue / 2 > 3 else returned

    gain = 6 - changed.blue
    loss = retained.blue
    premium = changed.red - retained.red
    premium += SENSITIVITY * (4 - changed.red) - FALSE_POSITIVE * (6 - retained.red)
    lower = (price + FALSE_POSITIVE * loss) / (SENSITIVITY * gain + FALSE_POSITIVE * loss)
    upper = ((1 - FALSE_POSITIVE) * loss - price) / (
        (1 - FALSE_POSITIVE) * loss + (1 - SENSITIVITY) * gain
    )
    return Market(changed, retained, gain, loss, premium, lower, upper, lower < upper)


@dataclass(frozen=True)
class Outcome:
    policy: str
    attempt: F
    changed: F
    deliberate: F
    test: F
    release: F
    genuine_service: F
    combat: F

    @property
    def confidence(self):
        """Genuine among all released suppliers, including uninspected ones."""
        return self.genuine_service / self.release if self.release else None


def outcome(power, reliability, price=TEST_PRICE):
    if not 0 <= reliability <= 1:
        raise ValueError("Reliability must be a probability.")
    m = market(power, price)
    pure_prior = reliability * min(F(1), reliability * m.red_edit_premium / COST_CEILING)
    if not m.active_interval or pure_prior < m.lower_prior:
        return Outcome("no trade", F(0), F(0), F(0), F(0), F(0), F(0), F(m.retained.combat))

    if pure_prior <= m.upper_prior:
        policy, prior, test = "test", pure_prior, F(1)
    else:
        policy, prior = "test or trust", m.upper_prior
        test = (COST_CEILING * prior / reliability**2 + 2) / (m.red_edit_premium + 2)

    attempt = prior / reliability
    refuse_genuine = test * (1 - SENSITIVITY)
    refuse_retained = test * (1 - FALSE_POSITIVE)
    service = prior * (1 - refuse_genuine)
    release = service + (1 - prior) * (1 - refuse_retained)
    combat = prior * refuse_genuine * m.changed.combat + (1 - prior) * refuse_retained * m.retained.combat
    return Outcome(policy, attempt, prior, 1 - attempt, test, release, service, combat)


def make_figure(path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import Normalize
    from matplotlib.ticker import PercentFormatter

    width, height = 216, 144
    powers = [F(2 * i + 1, 2 * width) for i in range(width)]
    reliabilities = [F(2 * i + 1, 2 * height) for i in range(height)]
    values = np.empty((3, height, width))
    for i, power in enumerate(powers):
        for j, reliability in enumerate(reliabilities):
            state = outcome(power, reliability)
            values[:, j, i] = (
                float(state.changed),
                float(state.combat),
                float(state.confidence) if state.confidence is not None else np.nan,
            )

    cmap = plt.colormaps["viridis"].copy()
    cmap.set_bad("#e4e5e4")
    fig, axes = plt.subplots(1, 3, figsize=(11.7, 3.8), sharey=True, layout="constrained")
    titles = ("Suppliers acquiring the agreed goal", "Batches ending in combat", "Genuine among released batches")
    for ax, title, field in zip(axes, titles, values):
        raster = ax.imshow(
            field, origin="lower", extent=(0, 1, 0, 1), norm=Normalize(0, 1),
            cmap=cmap, aspect="auto", interpolation="nearest",
        )
        ax.set_title(title, fontsize=11, loc="left", pad=9)
        for boundary in (1 / 3, 2 / 3):
            ax.axvline(boundary, color="white", linewidth=0.85, linestyle=(0, (3, 3)), alpha=.8)
        ax.set_xticks([0, 1 / 3, 2 / 3, 1], ["0", "⅓", "⅔", "1"])
        ax.set_yticks([0, .25, .5, .75, 1])
        ax.tick_params(length=3)
    axes[0].set_ylabel("Chance a real installation attempt succeeds")
    fig.supxlabel("Buyer’s chance of recovering the batch in combat", fontsize=11)
    cb = fig.colorbar(raster, ax=axes, fraction=.027, pad=.015)
    cb.formatter = PercentFormatter(1)
    cb.update_ticks()
    fig.savefig(path, dpi=165, facecolor="white")
    plt.close(fig)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--figure", help="Save the probability maps as a PNG.")
    args = parser.parse_args()
    examples = [(F(1, 20), F(4, 5)), (F(1, 2), F(4, 5)), (F(4, 5), F(4, 5)),
                (F(4, 5), F(17, 20)), (F(4, 5), F(1))]
    for power, reliability in examples:
        state = outcome(power, reliability)
        print(f"s={power}, q={reliability}: {state.policy}, genuine={state.changed}, "
              f"combat={float(state.combat):.5f}, released confidence={float(state.confidence):.5f}")
    if args.figure:
        make_figure(args.figure)


if __name__ == "__main__":
    main()
