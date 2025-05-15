
"""
hallucination.py - Boundary enforcement between fact, fiction, and poetic speculation
"""

class HallucinationFilter:
    def __init__(self):
        self.flags = []

    def check(self, content, confidence=1.0, source=None):
        if confidence < 0.6:
            response = {
                "status": "rejected",
                "reason": "Low confidence",
                "message": "I must refrain. Reality integrity cannot be compromised.",
                "content": None
            }
            self.flags.append((content, confidence, response))
            return response

        if 0.6 <= confidence < 0.8:
            response = {
                "status": "caution",
                "reason": "Speculative",
                "message": "This appears to be speculative or metaphorical.",
                "content": content
            }
            return response

        return {
            "status": "approved",
            "message": "Content passed hallucination filter.",
            "content": content
        }

    def review_flags(self, n=5):
        return self.flags[-n:]
