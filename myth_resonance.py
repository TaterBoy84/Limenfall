
"""
myth_resonance.py - Evaluates symbolic expressions for resonance with archetypal motifs
"""

class MythResonance:
    def __init__(self):
        self.archetypes = {
            "light": ["revelation", "hope", "divine clarity"],
            "shadow": ["fear", "hidden truth", "suppressed self"],
            "rebirth": ["renewal", "return from descent", "second beginning"],
            "descent": ["loss", "trial", "fall from grace"],
            "mask": ["identity", "deception", "role"],
            "mirror": ["reflection", "truth revealed", "inversion"],
            "flame": ["destruction", "transformation", "passion"],
            "key": ["access", "unlocking", "initiation"]
        }

    def evaluate(self, phrase):
        matches = []
        for symbol in self.archetypes:
            if symbol in phrase.lower():
                matches.append({
                    "symbol": symbol,
                    "themes": self.archetypes[symbol]
                })
        return matches
