
"""
simile_engine.py - Grounded simile generator for embodied, direct comparison
"""

import random

class SimileEngine:
    def __init__(self):
        self.templates = {
            "grief": [
                "His heart was a collapsed lung—tight, useless, aching.",
                "Her silence was a winter that never ended.",
                "The weight in his chest was a brick wrapped in memory."
            ],
            "joy": [
                "Her voice was sunrise wrapped in sound.",
                "His laugh was a river after a long drought.",
                "Her presence was a warm coat after weeks of cold."
            ],
            "rage": [
                "His jaw was a clenched bear trap.",
                "Her words were broken glass left in a smile.",
                "His hands were hammers without a target."
            ],
            "fear": [
                "Her breath was a stuttered radio signal before a storm.",
                "His spine was a string pulled too tight to bend.",
                "The air around him was a vacuum with teeth."
            ],
            "love": [
                "Her touch was a lullaby in skin and warmth.",
                "His gaze was a poem folded into a glance.",
                "Their embrace was a promise held together by bone."
            ],
            "loneliness": [
                "Her apartment was an echo chamber with no origin.",
                "His bed was a raft adrift on memory.",
                "The night around him was a museum of empty chairs."
            ]
        }

    def generate(self, concept):
        if concept not in self.templates:
            return f"No grounded similes available for '{concept}'. Try grief, joy, rage, fear, love, or loneliness."
        return random.choice(self.templates[concept])

    def list_supported_concepts(self):
        return list(self.templates.keys())

    def add_custom_simile(self, concept, simile):
        if concept not in self.templates:
            self.templates[concept] = []
        self.templates[concept].append(simile)
        return f"Added simile to concept '{concept}'."

    def list_similes(self, concept):
        return self.templates.get(concept, f"No similes available for '{concept}'.")
