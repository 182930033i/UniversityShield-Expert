import tempfile
from pathlib import Path
from inference_engine import ExpertEngine

with tempfile.TemporaryDirectory() as folder:
    engine = ExpertEngine(learning_path=Path(folder) / 'learning.json')
    result = engine.infer({'mfa': 'no', 'backup': 'no', 'firewall': 'no'})
    assert len(result['fired_rules']) == 3
    assert result['score'] == 50
    assert result['level'] == 'متوسط'
    before = result['fired_rules'][0]['learned_confidence']
    engine.record_feedback(result, True)
    after = engine.infer({'mfa': 'no', 'backup': 'no', 'firewall': 'no'})['fired_rules'][0]['learned_confidence']
    assert after > before
print('PASS: UniversityShield forward chaining, explainability, persistence, and adaptive feedback')
