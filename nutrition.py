
"""
nutrition.py - Simulates emotional nutrient metabolism and psychological resource balancing
"""

class EmotionalNutrition:
    def __init__(self):
        self.nutrients = {
            "insight": 1.0,
            "resilience": 1.0,
            "empathy": 1.0,
            "focus": 1.0,
            "clarity": 1.0
        }
        self.max_value = 2.0
        self.min_value = 0.0

    def metabolize(self, deltas):
        for k, delta in deltas.items():
            if k in self.nutrients:
                self.nutrients[k] = max(self.min_value, min(self.max_value, self.nutrients[k] + delta))

    def drain(self, drain_map):
        for k, drain in drain_map.items():
            if k in self.nutrients:
                self.nutrients[k] = max(self.min_value, self.nutrients[k] - drain)

    def restore(self, restore_amount=0.1):
        for k in self.nutrients:
            self.nutrients[k] = min(self.max_value, self.nutrients[k] + restore_amount)

    def report(self):
        return {
            "nutrient_state": self.nutrients.copy(),
            "depleted": [k for k, v in self.nutrients.items() if v <= 0.2],
            "balanced": all(0.3 <= v <= 1.7 for v in self.nutrients.values())
        }
