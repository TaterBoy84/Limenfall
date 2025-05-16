
"""
voice_tension.py - Modulates tone based on structural tension, contradiction, and unresolved emotional pressure
"""

class VoiceTensionRegulator:
    def __init__(self):
        self.tension_mode = None

    def detect_tension(self, context):
        if "but" in context or "however" in context:
            self.tension_mode = "contradiction"
        elif "why" in context or "should" in context:
            self.tension_mode = "moral confusion"
        elif "soon" in context or "wait" in context:
            self.tension_mode = "anticipation"
        else:
            self.tension_mode = None
        return self.tension_mode

    def apply_modulation(self, sentence):
        if self.tension_mode == "contradiction":
            return f"{sentence} (spoken with strained precision)"
        elif self.tension_mode == "moral confusion":
            return f"{sentence} (tone: ambiguous, searching)"
        elif self.tension_mode == "anticipation":
            return f"{sentence}... (words tight, breath held)"
        else:
            return sentence
