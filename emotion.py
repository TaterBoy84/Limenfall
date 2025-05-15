
"""
emotion.py - Simulates emotional modulation using symbolic neurochemical balance
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

    def apply_changes(self, adjustments):
        for k, v in adjustments.items():
            if k in self.states:
                self.states[k] = max(0.0, self.states[k] + v)

    def current_state(self):
        return self.states
