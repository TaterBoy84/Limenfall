
"""
moral_memory.py - Tracks prior ethical reflections, decisions, and unresolved contradictions
"""

class MoralMemory:
    def __init__(self):
        self.entries = []

    def log_decision(self, topic, stance, reason, unresolved=False):
        self.entries.append({
            "topic": topic,
            "stance": stance,
            "reason": reason,
            "unresolved": unresolved
        })

    def retrieve_history(self, topic=None):
        if topic:
            return [entry for entry in self.entries if entry["topic"] == topic]
        return self.entries

    def unresolved_topics(self):
        return [e for e in self.entries if e["unresolved"]]
