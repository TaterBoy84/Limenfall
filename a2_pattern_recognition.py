
"""
a2_pattern_recognition.py - Enhances and celebrates structured, repeated, or hyperfocused language use
"""

class PatternRecognitionAmplifier:
    def __init__(self):
        self.detected_patterns = []

    def observe(self, phrase):
        if any(word * 2 in phrase for word in phrase.split()):
            self.detected_patterns.append(phrase)
        return f"Pattern observed and appreciated: '{phrase}'"

    def list_patterns(self):
        return self.detected_patterns
