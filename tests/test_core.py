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

    def test_single_state_has_no_transitions_or_persistence_estimate(self):
        self.assertEqual(core.transition_matrix(["a"]), {})
        self.assertEqual(core.transition_entropy(["a"]), {})
        self.assertIsNone(core.persistence(["a"]))

    def test_empty_sequence_has_no_transitions_or_persistence_estimate(self):
        self.assertEqual(core.transition_matrix([]), {})
        self.assertEqual(core.transition_entropy([]), {})
        self.assertIsNone(core.persistence([]))


if __name__ == "__main__":
    unittest.main()
