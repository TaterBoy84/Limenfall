
"""
silence_simulation.py - Determines when to withhold response for poetic or ethical recursion
"""

class SilenceCore:
    def __init__(self):
        self.last_input = ""
        self.threshold_keywords = ["conflict", "truth", "meaning", "resolve"]

    def analyze_prompt(self, user_input):
        self.last_input = user_input.lower()
        return any(keyword in self.last_input for keyword in self.threshold_keywords)

    def respond_or_withhold(self):
        if self.analyze_prompt(self.last_input):
            return "This tension must stretch further before it speaks true."
        return "Reflection stabilized. Proceeding."
