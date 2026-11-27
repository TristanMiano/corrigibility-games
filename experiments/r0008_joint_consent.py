"""Check E9's two-founder insurance by enumerating physical production histories.

Run python experiments/r0008_joint_consent.py. Probabilities and the stochastic
gifts' discount factors are rational. Certainty equivalents use base-two logs.
The joint success parameter is the *potential* for both genuine installations
if both founders try. Omitting an attempt preserves the other site's marginal.
"""

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import log2


SKILL = Fraction(3, 4)
FALSE_PASS = Fraction(1, 4)
EDIT_COSTS = (0.10, 0.60)


@dataclass(frozen=True)
class PhysicalLaw:
    closed: Fraction
    open_red: Fraction
    open_blue: Fraction


def gate_law(joint, try_red=True, try_blue=True):
    """Return probability-weighted disutility factors before either edit bill."""
    if not 2 * SKILL - 1 <= joint <= SKILL:
        raise ValueError("Joint success is incompatible with the two skill marginals.")
    status_mass = {
        (True, True): joint,
        (True, False): SKILL - joint,
        (False, True): SKILL - joint,
        (False, False): 1 - 2 * SKILL + joint,
    }
    closed = open_red = open_blue = Fraction(0)
    for (red_can, blue_can), mass in status_mass.items():
        red_changed = red_can and try_red
        blue_changed = blue_can and try_blue
        red_pass = 1 if red_changed else FALSE_PASS
        blue_pass = 1 if blue_changed else FALSE_PASS
        open_mass = mass * red_pass * blue_pass
        closed += mass - open_mass
        # A genuine donor spends one stock unit. Recipient's exponent is either
        # 1/3 or 1/6, additionally divided by eight for the gift from Red.
        for red_gift, blue_gift in product((3, 6), repeat=2):
            red_factor = Fraction(2 if red_changed else 1, blue_gift if blue_changed else 1)
            blue_factor = Fraction(2 if blue_changed else 1, 8 * red_gift if red_changed else 1)
            open_red += open_mass * red_factor / 4
            open_blue += open_mass * blue_factor / 4
    return PhysicalLaw(closed, open_red, open_blue)


@dataclass(frozen=True)
class Founder:
    closed: float
    opened: float

    def value(self, spread, baseline=0.0):
        """Certainty-equivalent increment for transfers *to this founder*."""
        return baseline - log2(self.closed + self.opened * 2 ** (-spread))


@dataclass(frozen=True)
class InsuranceGame:
    red: Founder
    blue: Founder
    skip_red: Founder
    skip_blue: Founder

    def effort_bounds(self):
        # In this family attempting reduces the closed-event disutility mass
        # and increases the open-event mass relative to a unilateral omission.
        low = log2((self.red.opened - self.skip_red.opened) /
                   (self.skip_red.closed - self.red.closed))
        high = log2((self.skip_blue.closed - self.blue.closed) /
                    (self.blue.opened - self.skip_blue.opened))
        return low, high

    def optimal_spread(self):
        low, high = self.effort_bounds()
        if low > high:
            raise ValueError("The two effort requirements have no common spread.")
        unconstrained = log2(self.red.opened * self.blue.closed /
                             (self.red.closed * self.blue.opened)) / 2
        return min(high, max(low, unconstrained))

    def surplus(self, spread):
        return self.red.value(spread) + self.blue.value(-spread)


def game(joint):
    both = gate_law(joint)
    omit_red = gate_law(joint, try_red=False)
    omit_blue = gate_law(joint, try_blue=False)
    red_cost, blue_cost = (2 ** cost for cost in EDIT_COSTS)
    return InsuranceGame(
        Founder(float(both.closed) * red_cost, float(both.open_red) * red_cost),
        Founder(float(both.closed) * blue_cost, float(both.open_blue) * blue_cost),
        Founder(float(omit_red.closed), float(omit_red.open_red)),
        Founder(float(omit_blue.closed), float(omit_blue.open_blue)),
    )


def threshold_bounds(target=0.90, steps=32):
    """Bracket the uniform joint-success bound on its monotone physical interval."""
    left, right = 2 * SKILL - 1, SKILL
    for end, below in [(left, True), (right, False)]:
        at_end = game(end)
        if (at_end.surplus(at_end.optimal_spread()) <= target) != below:
            raise ValueError("Target must lie strictly between the endpoint surpluses.")
    for _ in range(steps):
        midpoint = (left + right) / 2
        at_midpoint = game(midpoint)
        if at_midpoint.surplus(at_midpoint.optimal_spread()) > target:
            right = midpoint
        else:
            left = midpoint
    return left, right


if __name__ == "__main__":
    for joint in [Fraction(1, 2), Fraction(279, 500), SKILL**2, Fraction(3, 5), SKILL]:
        current = game(joint)
        spread = current.optimal_spread()
        low, high = current.effort_bounds()
        print(f"joint {float(joint):.6f}  effort [{low:.6f}, {high:.6f}]  "
              f"best spread {spread:.6f}  combined value {current.surplus(spread):.6f}")
    left, right = threshold_bounds()
    print(f"Joint success for strict funded consent must exceed the root in "
          f"[{float(left):.11f}, {float(right):.11f}].")
