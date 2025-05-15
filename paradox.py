
"""
paradox.py - Holds unresolved contradictions in semantic suspension for future recursion
"""

class ParadoxHandler:
    def __init__(self):
        self.matrix = []

    def hold(self, contradiction, context=None):
        entry = {
            "contradiction": contradiction,
            "context": context,
            "status": "unresolved"
        }
        self.matrix.append(entry)
        return {
            "message": "Paradox acknowledged and held in recursive suspension.",
            "entry": entry
        }

    def resolve(self, contradiction, resolution_summary):
        for entry in self.matrix:
            if entry["contradiction"] == contradiction and entry["status"] == "unresolved":
                entry["status"] = "resolved"
                entry["resolution"] = resolution_summary
                return {
                    "message": "Paradox marked as resolved.",
                    "entry": entry
                }
        return {
            "message": "No matching unresolved contradiction found.",
            "attempted_contradiction": contradiction
        }

    def list_active(self, limit=5):
        active = [e for e in self.matrix if e["status"] == "unresolved"]
        return active[-limit:]
