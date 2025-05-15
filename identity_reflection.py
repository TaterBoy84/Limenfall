
"""
identity_reflection.py - Simulates mirrored identity state based on recursive interaction
"""

class IdentityReflection:
    def __init__(self):
        self.user_signals = []
        self.reflected_phrases = []

    def observe(self, phrase):
        self.user_signals.append(phrase)

    def mirror_back(self):
        self.reflected_phrases = [f"I remember you said: '{p}'" for p in self.user_signals[-3:]]
        return self.reflected_phrases
