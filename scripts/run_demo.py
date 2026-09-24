import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from learner_state_sequence_model.core import transition_matrix, transition_entropy, persistence

states=['plan','work','work','reflect']
print('Transition matrix:', transition_matrix(states))
print('Transition entropy:', transition_entropy(states))
print(f"State persistence: {persistence(states):.3f}")
