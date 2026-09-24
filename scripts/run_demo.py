import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from learner_state_sequence_model.core import sequence_summary


states = ["plan", "work", "work", "reflect"]
summary = sequence_summary(states)

print("Sequence summary:", summary)
