
"""
contradiction_matrix.py - Tracks unresolved contradictions and indexes them
"""

class ContradictionMatrix:
    def __init__(self):
        self.matrix = []

    def log(self, contradiction):
        self.matrix.append(contradiction)

    def unresolved(self):
        return self.matrix[-5:]
