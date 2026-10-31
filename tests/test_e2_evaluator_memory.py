"""Exact augmented-state policy evaluation for note 029's recurrent example.

The three-state linear system retains a past evaluator's first-change bit.
It is compared with current-self deviations and the deliberately different
criterion charging every future change. This is not a fixed-point proof.
"""
from fractions import Fraction as F
import unittest

from test_e2_population import solve_three


def evaluate_first_change(p):
    beta, color, bonus, penalty = F(1, 2), F(1), F(12, 5), F(1)
    # States F before first change, F after first change, H after first change.
    transitions = [[1-p, 0, p], [0, 1-p, p], [0, 1, 0]]
    rewards = [(1-p)*color+p*(bonus-penalty), (1-p)*color+p*bonus, 0]
    rows = []
    for i in range(3):
        rows.append(tuple(F(i == j)-beta*transitions[i][j] for j in range(3))
                    +(rewards[i],))
    return solve_three(rows)


class EvaluatorMemoryChecks(unittest.TestCase):
    def test_all_three_stationary_profiles_and_deviations(self):
        for p in [F(0), F(1, 4), F(1)]:
            current, archived_color, h_color = evaluate_first_change(p)
            stay = 1+current/2
            switch = F(12, 5)-1+h_color/2
            self.assertEqual(current, (1-p)*stay+p*switch)
            self.assertGreater(current, 0)  # Attack
            self.assertGreater(h_color, h_color/2)  # H Return vs Keep
            if p == 0:
                self.assertGreater(stay, switch)
                self.assertEqual(current, 2)
            elif p == 1:
                self.assertGreater(switch, stay)
                self.assertEqual(current, F(11, 5))
            else:
                self.assertEqual(stay, switch)
                self.assertEqual(current, 2)
                self.assertEqual(archived_color, F(12, 5))
        for p in [F(j, 20) for j in range(21)]:
            current, _, h_color = evaluate_first_change(p)
            gain = F(12, 5)-1+h_color/2-(1+current/2)
            self.assertEqual((gain > 0)-(gain < 0), (p > F(1, 4))-(p < F(1, 4)))

    def test_tenure_delay_and_wrong_repeated_penalty(self):
        current, _, h_color = evaluate_first_change(F(1))
        switch = F(12, 5)-1+h_color/2
        for delay in range(20):
            value = sum(F(1, 2)**t for t in range(delay))+F(1, 2)**delay*switch
            self.assertLessEqual(value, current)
        persistent_penalty = (F(12, 5)-1)/(1-F(1, 2)**2)
        self.assertEqual(persistent_penalty, F(28, 15))
        self.assertGreater(1+persistent_penalty/2, persistent_penalty)

    def test_affine_lottery_witness_for_freezing_parameters(self):
        # Same numerical output ordering at endpoints does not preserve lotteries.
        low, high = (F(0), F(1), F(-1)), (F(0), F(1), F(-2))
        lottery = (F(0), F(1, 2), F(1, 2))
        self.assertEqual(sum(x*p for x, p in zip(low, lottery)), low[0])
        self.assertNotEqual(sum(x*p for x, p in zip(high, lottery)), high[0])
        recoded = tuple(3*x+7 for x in low)
        self.assertEqual(sum(x*p for x, p in zip(recoded, lottery)), recoded[0])


if __name__ == '__main__':
    unittest.main()
