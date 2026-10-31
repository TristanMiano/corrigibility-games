"""Independent finite-offer and stopping-policy checks for notes 021 and 022.

Exact rational path enumeration checks the information examples. Enumerating
all stationary acceptance sets checks the finite stopping problem; midpoint
quadrature and a threshold grid check the continuous uniform formulas. These
are reproducible checks, not machine proofs of the general claims.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import unittest


def offer_outcome(types, probabilities, peace, war, offer):
    a = b = fighting = F(0)
    for q, probability in zip(types, probabilities):
        if offer >= q*war:  # declared acceptance-at-indifference convention
            a += probability*offer
            b += probability*(peace-offer)
        else:
            a += probability*q*war
            b += probability*(1-q)*war
            fighting += probability
    return a, b, fighting


def optimal_offer(types, probabilities, peace, war):
    candidates = [offer_outcome(types, probabilities, peace, war, q*war)
                  for q, probability in zip(types, probabilities) if probability]
    # On proposer ties select the less violent offer; strict examples do not tie.
    return max(candidates, key=lambda result: (result[1], -result[2]))


def binary_test(prior, low_label_if_low, low_label_if_high, peace, war):
    total = [F(0)]*3
    for ll, lh in [(low_label_if_low, low_label_if_high),
                   (1-low_label_if_low, 1-low_label_if_high)]:
        mass = (1-prior)*ll+prior*lh
        if mass:
            p = prior*lh/mass
            outcome = optimal_offer([F(1, 4), F(3, 4)], [1-p, p], peace, war)
            total = [old+mass*new for old, new in zip(total, outcome)]
    return tuple(total)


def stationary_stopping(marks, probabilities, eta, delta, penalty, accept):
    hazard = eta*sum(p for p, take in zip(probabilities, accept) if take)
    numerator = eta*sum(p*(g-penalty) for g, p, take
                        in zip(marks, probabilities, accept) if take)
    return numerator/(1-delta*(1-hazard)), hazard


def uniform_stopping(maximum, penalty, eta, delta):
    if penalty >= maximum:
        return 0., maximum, 0., 0.
    gap = maximum-penalty
    alpha = delta*eta/(2*maximum*(1-delta))
    z = 2*gap/(1+sqrt(1+4*alpha*gap))
    hazard = eta*z/maximum
    value = eta*z*z/(2*maximum*(1-delta))
    discounted_arrival = hazard/(1-delta*(1-hazard))
    return value, maximum-z, hazard, discounted_arrival


class InformationChecks(unittest.TestCase):
    def test_peace_exists_but_proposer_screens(self):
        p, w = F(11, 10), F(4, 5)
        low = offer_outcome([F(1, 4), F(3, 4)], [F(1, 2)]*2, p, w, F(1, 5))
        high = offer_outcome([F(1, 4), F(3, 4)], [F(1, 2)]*2, p, w, F(3, 5))
        self.assertEqual(low, (F(2, 5), F(11, 20), F(1, 2)))
        self.assertEqual(high, (F(3, 5), F(1, 2), 0))
        self.assertGreater(high[1], F(2, 5))
        self.assertGreater(low[1], high[1])

    def test_discrete_cdf_identity_and_best_offer(self):
        types = [F(1, 5), F(1, 2), F(4, 5)]
        probabilities = [F(1, 4), F(1, 2), F(1, 4)]
        w = F(3, 4)
        mean = sum(q*p for q, p in zip(types, probabilities))
        for p in [F(4, 5), F(1), F(3, 2)]:
            for i, q in enumerate(types):
                cdf = sum(probabilities[:i+1])
                integral = sum(sum(probabilities[:j+1])*(types[j+1]-types[j])
                               for j in range(i))
                b = w*(1-mean)+(p-w)*cdf-w*integral
                self.assertEqual(b, offer_outcome(types, probabilities, p, w, q*w)[1])
            candidate = optimal_offer(types, probabilities, p, w)[1]
            # A larger finite offer menu must not improve the support-point optimum.
            grid_best = max(offer_outcome(types, probabilities, p, w, F(j, 100)*p)[1]
                            for j in range(101))
            self.assertLessEqual(grid_best, candidate)

    def test_fallible_information_introduces_war(self):
        p, w, prior = F(11, 10), F(4, 5), F(4, 5)
        initial = optimal_offer([F(1, 4), F(3, 4)], [1-prior, prior], p, w)
        tested = binary_test(prior, F(9, 10), F(1, 10), p, w)
        self.assertEqual(initial, (F(3, 5), F(1, 2), 0))
        self.assertEqual(tested, (F(66, 125), F(137, 250), F(2, 25)))
        self.assertEqual(sum(tested[:2]), p-(p-w)*tested[2])
        self.assertEqual(binary_test(prior, F(1), F(0), p, w)[2], 0)

    def test_information_structure_war_bound(self):
        p, w = F(11, 10), F(4, 5)
        for prior in [F(1, 10), F(3, 10), F(4, 5)]:
            bound = min(prior, (1-prior)*w*F(1, 2)/(p-w))
            initial_b = optimal_offer([F(1, 4), F(3, 4)], [1-prior, prior], p, w)[1]
            for i, j in product(range(11), repeat=2):
                outcome = binary_test(prior, F(i, 10), F(j, 10), p, w)
                self.assertLessEqual(outcome[2], bound)
                self.assertGreaterEqual(outcome[1], initial_b)

    def test_strength_signal_score_and_checkpoint_payoffs(self):
        l, h, w, p = F(1, 4), F(3, 4), F(4, 5), F(3, 2)
        eta, shift = F(1, 10), F(7, 10)
        for actual in [l, h]:
            means = {}
            for report in [l, h]:
                outputs = [shift+eta*(2*report*z-report**2) for z in [0, 1]]
                means[report] = (1-actual)*outputs[0]+actual*outputs[1]
                for output in outputs:
                    self.assertGreater(output, h*w)
                    self.assertGreater(p-output, (1-l)*w)
            other = h if actual == l else l
            self.assertEqual(means[actual]-means[other], eta*(h-l)**2)


class StoppingChecks(unittest.TestCase):
    def test_all_finite_acceptance_sets_against_backward_induction(self):
        marks, probabilities = [F(0), F(1), F(2)], [F(1, 4), F(1, 2), F(1, 4)]
        eta, delta = F(3, 5), F(4, 5)
        for penalty in [F(0), F(1, 2), F(3, 2), F(5, 2)]:
            possibilities = [stationary_stopping(marks, probabilities, eta, delta,
                             penalty, take)[0] for take in product([False, True], repeat=3)]
            optimum = max(possibilities)
            value = 0.
            for _ in range(200):
                value = (1-float(eta))*float(delta)*value+float(eta)*sum(
                    float(prob)*max(float(g-penalty), float(delta)*value)
                    for g, prob in zip(marks, probabilities))
            self.assertAlmostEqual(value, float(optimum), places=12)

    def test_uniform_formula_against_quadrature_and_threshold_grid(self):
        n = 4000
        marks = [(j+.5)/n for j in range(n)]
        for eta, delta, penalty in product([.2, 1.], [.5, .9, .99], [0., .2, .8]):
            value, threshold, hazard, discount = uniform_stopping(1., penalty, eta, delta)
            rhs = (1-eta)*delta*value+eta*sum(max(g-penalty, delta*value)
                                                           for g in marks)/n
            self.assertLess(abs(rhs-value), 2e-8)
            best = 0.
            tail = sum(marks)
            for j in range(n):
                h = eta*(n-j)/n
                policy_value = eta*(tail-penalty*(n-j))/n/(1-delta*(1-h))
                best = max(best, policy_value)
                tail -= marks[j]
            self.assertLess(abs(value-best), 2e-6)
            gross = discount*(1+threshold)/2
            self.assertAlmostEqual(value, gross-penalty*discount, places=11)

    def test_finite_freeze_can_be_optimal_for_color_only_designer(self):
        delta, eta, premium = .9, 1., .2
        def designer(kappa):
            value, _, _, discount = uniform_stopping(1., kappa, eta, delta)
            return premium*kappa/(1-delta)+value+kappa*discount
        values = [designer(j/1000) for j in range(1001)]
        best_index = max(range(1001), key=values.__getitem__)
        self.assertGreater(best_index, 0)
        self.assertLess(best_index, 1000)
        self.assertGreater(values[best_index], max(values[0], values[-1]))
        self.assertTrue(all(values[j+1]-2*values[j]+values[j-1] < 1e-10
                            for j in range(1, 1000)))

    def test_early_relaxation_imitation_bound(self):
        for eta, delta in product([.2, 1.], [.5, .9, .99]):
            v0, _, _, d0 = uniform_stopping(1., 0., eta, delta)
            for penalty in [.1, .5, .9, 1.1]:
                value = uniform_stopping(1., penalty, eta, delta)[0]
                self.assertGreaterEqual(value+1e-12, v0-penalty*d0)
                self.assertGreaterEqual(v0-penalty*d0+1e-12, v0-penalty)


if __name__ == '__main__':
    unittest.main()
