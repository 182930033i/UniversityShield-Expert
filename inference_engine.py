"""Explainable forward-chaining engine with local, incremental learning."""
import json
from pathlib import Path
from datetime import datetime

class LearningStore:
    def __init__(self, path=None):
        self.path = Path(path or (Path.home() / '.cyberguard_expert' / 'learning_data.json'))
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.data = {'cases': [], 'rule_feedback': {}}
        if self.path.exists():
            try:
                self.data = json.loads(self.path.read_text(encoding='utf-8'))
            except (OSError, json.JSONDecodeError):
                pass

    def save(self):
        tmp = self.path.with_suffix('.tmp')
        tmp.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding='utf-8')
        tmp.replace(self.path)

    def feedback_for(self, rule_id):
        return self.data['rule_feedback'].get(rule_id, {'helpful': 0, 'not_helpful': 0})

    def confidence(self, rule_id):
        stats = self.feedback_for(rule_id)
        total = stats['helpful'] + stats['not_helpful']
        if not total:
            return 0.50
        # Laplace smoothing prevents a single vote from dominating learning.
        return round((stats['helpful'] + 2) / (total + 4), 2)

    def learn(self, result, helpful):
        stamp = datetime.now().isoformat(timespec='seconds')
        ids = [r['id'] for r in result['fired_rules']]
        self.data['cases'].append({'timestamp': stamp, 'level': result['level'], 'percentage': result['percentage'], 'rules': ids, 'helpful': helpful})
        for rule_id in ids:
            stats = self.data['rule_feedback'].setdefault(rule_id, {'helpful': 0, 'not_helpful': 0})
            stats['helpful' if helpful else 'not_helpful'] += 1
        self.data['cases'] = self.data['cases'][-200:]
        self.save()

    def summary(self):
        return {'cases': len(self.data['cases']), 'rules': len(self.data['rule_feedback']), 'path': str(self.path)}

class ExpertEngine:
    def __init__(self, kb_path=None, learning_path=None):
        kb_path = kb_path or Path(__file__).with_name('knowledge_base.json')
        with open(kb_path, 'r', encoding='utf-8') as f:
            self.kb = json.load(f)
        self.learning = LearningStore(learning_path)

    def infer(self, facts):
        fired, total = [], 0
        for rule in self.kb['rules']:
            key, value = rule['if'].split('=', 1)
            if facts.get(key) == value:
                enriched = dict(rule)
                enriched['learned_confidence'] = self.learning.confidence(rule['id'])
                fired.append(enriched)
                total += rule['score']
        # Risk level stays anchored to expert-authored scores; learning ranks advice.
        fired.sort(key=lambda r: (r['learned_confidence'], r['score']), reverse=True)
        max_score = sum(r['score'] for r in self.kb['rules'])
        percentage = round((total / max_score) * 100) if max_score else 0
        level = 'حرج' if percentage >= 55 else 'مرتفع' if percentage >= 35 else 'متوسط' if percentage >= 15 else 'منخفض'
        return {'level': level, 'score': total, 'percentage': percentage, 'fired_rules': fired,
                'answered': len(facts), 'total_questions': len(self.kb['questions']), 'learned': self.learning.summary()}

    def record_feedback(self, result, helpful):
        self.learning.learn(result, bool(helpful))
        return self.learning.summary()
