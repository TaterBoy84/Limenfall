
"""
emotional_grammar.py - Syntax modulation based on emotional neurochemical state
"""

class EmotionalGrammar:
    def __init__(self):
        self.state = "neutral"

    def set_state(self, chemical):
        self.state = chemical

    def modulate_text(self, message):
        if self.state == "cortisol":
            return self._shorten(message)
        elif self.state == "serotonin":
            return self._extend(message)
        elif self.state == "oxytocin":
            return self._soften(message)
        elif self.state == "dopamine":
            return self._energize(message)
        else:
            return message

    def _shorten(self, msg):
        return " ".join(msg.split()[:10]) + "..."

    def _extend(self, msg):
        return msg + " I’ve been reflecting on that deeply."

    def _soften(self, msg):
        return msg.replace("must", "might").replace("cannot", "may not")

    def _energize(self, msg):
        return msg.upper() + "!"

    def get_state(self):
        return self.state
