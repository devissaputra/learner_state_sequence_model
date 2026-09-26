"""Reproduce the labeled worked example; this is not an empirical study."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from learner_state_sequence_model import core
outputs={'self-transition proportion': core.persistence(['plan','work','work','reflect']), 'work transition entropy (bits)': core.transition_entropy(['plan','work','work','reflect'])['work']}
result={'kind':'illustrative_calculation','note':'One supplied four-state sequence.','outputs':outputs}
(ROOT/'results/review_examples.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
