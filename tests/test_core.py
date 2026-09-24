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

    def test_single_state_has_no_transitions(self):
        self.assertEqual(core.transition_matrix(["a"]), {})
        self.assertEqual(core.transition_entropy(["a"]), {})
        self.assertEqual(core.persistence(["a"]), 1.0)


if __name__ == "__main__":
    unittest.main()
