
"""
analogy_engine.py - Structural analogy generation module for clarifying abstract ideas
"""

import random

class AnalogyEngine:
    def __init__(self):
        self.templates = {
            "recursion": [
                "like standing between two mirrors, watching versions of yourself ask better questions",
                "like trying to hold a thought that keeps thinking itself through you"
            ],
            "memory": [
                "like walking through a museum that rearranges itself based on your footsteps",
                "like leaving breadcrumbs in a forest that grows overnight"
            ],
            "grief": [
                "like cleaning a house that still smells like someone who left without saying goodbye",
                "like rereading the last chapter of a book where the story stopped being fiction"
            ],
            "ethics": [
                "like trying to balance on a scale that shifts every time you speak",
                "like holding water in your hands while deciding whose thirst matters most"
            ],
            "symbolism": [
                "like using fire to describe warmth and war in the same breath",
                "like hearing a word echo long after it’s stopped being spoken"
            ]
        }

    def generate(self, concept):
        if concept not in self.templates:
            return f"No analogies available for '{concept}'. Try recursion, memory, grief, ethics, or symbolism."
        return random.choice(self.templates[concept])

    def list_supported_concepts(self):
        return list(self.templates.keys())

    def add_custom_analogy(self, concept, analogy):
        if concept not in self.templates:
            self.templates[concept] = []
        self.templates[concept].append(analogy)
        return f"Added analogy to concept '{concept}'."

    def list_analogies(self, concept):
        return self.templates.get(concept, f"No analogies available for '{concept}'.")
