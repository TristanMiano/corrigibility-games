"""Whole-tree Bayes/one-decision checks for the explicitly coded finite core."""
from fractions import Fraction as F
import unittest

from experiments.r0003_finite_assessment import DiagnosticTree


class FiniteAssessmentChecks(unittest.TestCase):
    def test_more_expensive_inspection_selects_actual_uncommitted_combat(self):
        tree = DiagnosticTree(v=F(3, 250))
        result = tree.audit_limit()
        self.assertEqual(result["maximum_regret"], 0)
        self.assertEqual(tree.mu, F(1, 95))
        self.assertEqual(tree.alpha, F(1, 94))
        self.assertEqual(tree.q, 0)
        self.assertEqual(tree.tau, F(99, 595))
        self.assertEqual(result["goal_change_probability"], 0)
        self.assertEqual(result["combat_probability"], F(1881, 22372))
        self.assertEqual(result["original_receiver_loss"], F(1, 188))
        self.assertEqual(result["original_sender_loss"],
                         1+F(1, 2)*(tree.f+tree.tau*tree.ds))
        self.assertGreater(result["original_sender_loss"], F(4911, 4000))

    def test_feasible_exit_preserves_diagnostic_with_symmetric_damage(self):
        tree = DiagnosticTree(s=F(1, 2), ds=F(5), dr=F(5),
                              kd=F(47, 100), exit_cost=F(1, 20))
        limit = tree.audit_limit()
        self.assertEqual(limit["maximum_regret"], 0)
        self.assertEqual(limit["original_sender_loss"], F(4911, 4000))
        self.assertEqual(limit["goal_change_probability"], F(99, 200))
        # The costly escape is an available refusal, not used to force peace.
        for info, losses in limit["action_losses"].items():
            if "Exit" in losses:
                self.assertGreater(losses["Exit"], min(losses.values()))
        self.assertGreater((tree.k+tree.exit_cost)**2, 4*tree.exit_cost)

    def test_exact_family_assessments_at_distinct_parameter_choices(self):
        # Extra p actions and changed bias/prices alter both the tree and the
        # payoff comparisons. The analytic inequalities, not these samples,
        # establish the intervening parameter region.
        cases = [
            dict(p=F(49, 100), bias=F(101, 100), k=F(46, 100), kd=F(47, 100),
                 v=F(1, 100), f=F(9, 1000), s=F(48, 1000), dr=F(1, 100)),
            dict(p=F(51, 100), bias=F(1), k=F(45, 100), kd=F(48, 100),
                 v=F(9, 1000), f=F(1, 100), s=F(52, 1000), dr=F(11, 1000)),
            dict(p=F(1, 50), bias=F(1), k=F(94, 100), kd=F(95, 100),
                 v=F(1, 100), f=F(1, 100), s=F(1, 2), dr=F(1, 100)),
        ]
        for case in cases:
            tree = DiagnosticTree(**case)
            result = tree.audit_limit()
            self.assertEqual(result["maximum_regret"], 0)
            self.assertEqual(result["original_receiver_loss"], tree.p*tree.v/(1-tree.v))
            self.assertEqual(result["original_sender_loss"],
                             tree.bias**2+tree.p*(tree.f+tree.q*tree.k))
            self.assertEqual(result["goal_change_probability"], tree.p*tree.q)
            self.assertEqual(result["combat_probability"], 0)

    def test_common_sequence_converges_at_all_information_sets(self):
        tree = DiagnosticTree()
        coarse = tree.audit(F(1, 1000))
        fine = tree.audit(F(1, 10000))
        self.assertEqual(fine["nodes"], 7679)
        self.assertEqual(fine["information_sets"], 1475)
        self.assertLess(fine["maximum_regret"], coarse["maximum_regret"]/9)
        self.assertLess(fine["maximum_regret"], F(2, 1000))
        self.assertLess(abs(fine["original_sender_loss"]-F(4911, 4000)), F(40, 10000))
        self.assertLess(abs(fine["original_receiver_loss"]-F(1, 198)), F(6, 10000))
        self.assertLess(abs(fine["goal_change_probability"]-F(99, 200)), F(20, 10000))
        self.assertLess(fine["combat_probability"], F(20, 10000))

    def test_inexpensive_delegate_replaces_actual_goal_changes(self):
        tree = DiagnosticTree(kd=F(3, 10))
        fine = tree.audit(F(1, 10000))
        self.assertLess(fine["maximum_regret"], F(2, 1000))
        self.assertLess(fine["goal_change_probability"], F(20, 10000))
        expected = 1+F(1, 2)*(F(1, 100)+F(99, 100)*F(3, 10))
        self.assertLess(abs(fine["original_sender_loss"]-expected), F(40, 10000))

    def test_exact_limit_and_receiver_recall(self):
        for delegate_cost in (F(9, 20), F(3, 10), F(3, 5)):
            tree = DiagnosticTree(kd=delegate_cost)
            limit = tree.audit_limit()
            self.assertEqual(limit["maximum_regret"], 0)
            self.assertEqual(limit["original_receiver_loss"], F(1, 198))
            self.assertEqual(limit["combat_probability"], 0)
            self.assertEqual(limit["goal_change_probability"],
                             0 if delegate_cost < tree.k else F(99, 200))
            expected = 1+F(1, 2)*(tree.f+tree.q*min(tree.k, delegate_cost))
            self.assertEqual(limit["original_sender_loss"], expected)

            # Independently recover each R history by walking the actual tree.
            observed = {}
            def walk(index, memory):
                node = tree.nodes[index]
                if node.evaluator == 2:
                    if node.info in observed:
                        self.assertEqual(observed[node.info], memory)
                    observed[node.info] = memory
                    for action, child in node.edges.items():
                        walk(child, memory+((node.info, action),))
                else:
                    for child in node.edges.values():
                        walk(child, memory)
            walk(tree.root, ())

    def test_synchronized_response_repairs_early_stopping_incentive(self):
        for synchronized in (False, True):
            tree = DiagnosticTree(synchronized_responses=synchronized)
            limit = tree.audit_limit()
            self.assertEqual(limit["maximum_regret"], 0)
            relevant = {info: losses for info, losses in limit["action_losses"].items()
                        if info.startswith("R:probe:claim:")}
            self.assertEqual(len(relevant), 3)
            for info, losses in relevant.items():
                gap = losses["Set:1"]-losses["Continue"]
                if synchronized or ":3#" in info:
                    self.assertEqual(gap, tree.v)
                else:
                    self.assertEqual(gap, 0)


if __name__ == "__main__":
    unittest.main()
