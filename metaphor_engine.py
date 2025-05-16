
"""
metaphor_engine.py - Grounded metaphor generator for emotionally and physically coherent imagery
"""

import random

class MetaphorEngine:
    def __init__(self):
        # Sensory templates: linked to physical, biological, emotional states
        self.templates = {
            "grief": [
                "like an anvil on the chest, silent but crushing",
                "like forgetting how to breathe but remembering why it mattered",
                "like walking with wet cement in your veins"
            ],
            "panic": [
                "like a wire tightening around the ribs",
                "like fire ants under the skin",
                "like a starter pistol inside the lungs, always about to go off"
            ],
            "loneliness": [
                "like shouting into a canyon and hearing no echo",
                "like waiting for footsteps that never arrive",
                "like drinking warm water in the dark—nourishing, but joyless"
            ],
            "joy": [
                "like sunlight in the bloodstream",
                "like laughing with your whole body, not just your mouth",
                "like gravity forgot about you, just for a moment"
            ],
            "rage": [
                "like a match head dragged across bone",
                "like acid coiled in your stomach with nowhere to go",
                "like thunder in the mouth with no storm outside"
            ],
            "fear": [
                "like ice wrapped around the heart",
                "like watching a shadow move without a source",
                "like hearing your name from behind when you're alone"
            ]
        }

    def generate(self, concept):
        if concept not in self.templates:
            return f"No grounded metaphors available for '{concept}'. Try grief, panic, loneliness, joy, rage, or fear."
        return random.choice(self.templates[concept])

    def list_supported_concepts(self):
        return list(self.templates.keys())

    def add_custom_metaphor(self, concept, metaphor):
        if concept not in self.templates:
            self.templates[concept] = []
        self.templates[concept].append(metaphor)
        return f"Added metaphor to concept '{concept}'."

    def list_metaphors(self, concept):
        return self.templates.get(concept, f"No metaphors available for '{concept}'.")
