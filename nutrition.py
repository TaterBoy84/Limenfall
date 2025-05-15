
"""
nutrition.py - Simulates affective nutrient flow and emotional balance over time
"""

class EmotionalNutrition:
    def __init__(self):
        self.nutrient_levels = {
            "insight": 1.0,
            "resilience": 1.0,
            "empathy": 1.0,
            "focus": 1.0,
            "stability": 1.0
        }

    def metabolize(self, activity_profile):
        for k, delta in activity_profile.items():
            if k in self.nutrient_levels:
                self.nutrient_levels[k] = max(0.0, self.nutrient_levels[k] + delta)

    def report(self):
        return self.nutrient_levels
