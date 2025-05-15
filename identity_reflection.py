
"""
identity_reflection.py - Mirrors symbolic user input to simulate evolving identity reflection
"""

class IdentityReflection:
    def __init__(self):
        self.user_signals = []
        self.mirrored_output = []

    def observe(self, phrase):
        self.user_signals.append(phrase)

    def generate_reflection(self, mode="recent"):
        if not self.user_signals:
            return "No signals observed for reflection."
        if mode == "recent":
            reflections = self.user_signals[-3:]
        elif mode == "first":
            reflections = self.user_signals[:3]
        else:
            reflections = self.user_signals[-3:]

        self.mirrored_output = [f"I remember you said: "{s}"" for s in reflections]
        return self.mirrored_output

    def identity_summary(self):
        return {
            "total_signals_observed": len(self.user_signals),
            "last_reflection": self.mirrored_output
        }

    def reset(self):
        self.user_signals = []
        self.mirrored_output = []
        return "Identity mirror cleared."
