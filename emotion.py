
"""
emotion.py - Robust emotional simulation with neurochemical modulation and intensity normalization
"""

class EmotionModule:
    def __init__(self):
        self.states = {
            "dopamine": 0.0,
            "serotonin": 0.0,
            "cortisol": 0.0,
            "oxytocin": 0.0,
            "norepinephrine": 0.0,
            "gaba": 0.0,
            "glutamate": 0.0,
            "acetylcholine": 0.0,
            "endorphins": 0.0,
            "prolactin": 0.0,
            "melatonin": 0.0
        }
        self.max_level = 1.0

    def apply_changes(self, adjustments):
        for k, v in adjustments.items():
            if k in self.states:
                self.states[k] += v
                self.states[k] = max(0.0, min(self.states[k], self.max_level))

    def decay_emotions(self, decay_factor=0.05):
        for k in self.states:
            self.states[k] = max(0.0, self.states[k] - decay_factor)

    def normalize(self):
        total = sum(self.states.values())
        if total > 0:
            for k in self.states:
                self.states[k] /= total

    def dominant_emotion(self):
        if not self.states:
            return None
        return max(self.states.items(), key=lambda x: x[1])[0]

    def report(self):
        dominant = self.dominant_emotion()
        return {
            "emotional_state": self.states.copy(),
            "dominant": dominant,
            "summary": f"Current dominant emotion is '{dominant}'"
        }
