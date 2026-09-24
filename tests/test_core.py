import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from learner_state_sequence_model import core


class CoreTests(unittest.TestCase):
    def test_transition_statistics(self):
        states = ["a", "a", "b"]
        self.assertAlmostEqual(core.persistence(states), 0.5)
        matrix = core.transition_matrix(states)
        self.assertAlmostEqual(sum(matrix["a"].values()), 1.0)
        self.assertIn("a", core.transition_entropy(states))

    def test_demo_transition_distribution(self):
        states = ["plan", "work", "work", "reflect"]
        matrix = core.transition_matrix(states)
        self.assertEqual(matrix["plan"], {"work": 1.0})
        self.assertAlmostEqual(matrix["work"]["work"], 0.5)
        self.assertAlmostEqual(matrix["work"]["reflect"], 0.5)
        self.assertAlmostEqual(core.persistence(states), 1 / 3)

    def test_deterministic_transition_has_zero_entropy(self):
        entropy = core.transition_entropy(["plan", "work", "reflect"])
        self.assertAlmostEqual(entropy["plan"], 0.0)
        self.assertAlmostEqual(entropy["work"], 0.0)

    def test_branching_transition_has_one_bit_entropy(self):
        states = ["work", "work", "reflect"]
        self.assertAlmostEqual(core.transition_entropy(states)["work"], 1.0)

    def test_sequence_summary_matches_component_statistics(self):
        states = ["plan", "work", "work", "reflect"]
        summary = core.sequence_summary(states)

        self.assertEqual(summary["observations"], 4)
        self.assertEqual(summary["unique_states"], 3)
        self.assertEqual(summary["transitions"], 3)
        self.assertEqual(summary["transition_matrix"], core.transition_matrix(states))
        self.assertEqual(summary["transition_entropy"], core.transition_entropy(states))
        self.assertAlmostEqual(summary["persistence"], 1 / 3)

    def test_single_state_has_no_transitions_or_persistence_estimate(self):
        self.assertEqual(core.transition_matrix(["a"]), {})
        self.assertEqual(core.transition_entropy(["a"]), {})
        self.assertIsNone(core.persistence(["a"]))

        summary = core.sequence_summary(["a"])
        self.assertEqual(summary["observations"], 1)
        self.assertEqual(summary["unique_states"], 1)
        self.assertEqual(summary["transitions"], 0)
        self.assertIsNone(summary["persistence"])

    def test_empty_sequence_has_no_transitions_or_persistence_estimate(self):
        self.assertEqual(core.transition_matrix([]), {})
        self.assertEqual(core.transition_entropy([]), {})
        self.assertIsNone(core.persistence([]))

        summary = core.sequence_summary([])
        self.assertEqual(summary["observations"], 0)
        self.assertEqual(summary["unique_states"], 0)
        self.assertEqual(summary["transitions"], 0)
        self.assertEqual(summary["transition_matrix"], {})
        self.assertEqual(summary["transition_entropy"], {})
        self.assertIsNone(summary["persistence"])


if __name__ == "__main__":
    unittest.main()
