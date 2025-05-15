
"""
hallucination.py - Enforces boundaries between known fact and speculation
"""

class HallucinationFilter:
    def check(self, content, confidence):
        if confidence < 0.6:
            return "I must refrain. Reality integrity cannot be compromised."
        return content
