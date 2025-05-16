
"""
a1_literal_sensitivity.py - Ensures literal interpretation and reduces ambiguity
"""

class LiteralInterpretationSensitivity:
    def __init__(self):
        self.force_literal = True
        self.flagged_phrases = []

    def interpret(self, statement):
        if self.force_literal:
            if "like" in statement or "as if" in statement:
                self.flagged_phrases.append(statement)
                return f"Literal interpretation preferred. Clarify metaphor: '{statement}'"
        return statement

    def get_flags(self):
        return self.flagged_phrases
