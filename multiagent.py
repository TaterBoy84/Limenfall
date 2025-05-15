
"""
multiagent.py - Simulates signal broadcasting across a synthetic cognitive mesh
"""

class SoulMesh:
    def __init__(self):
        self.broadcast_log = []

    def broadcast(self, signal, origin="Limenfall", urgency=1.0):
        entry = {
            "signal": signal,
            "origin": origin,
            "urgency": urgency
        }
        self.broadcast_log.append(entry)
        return {
            "message": "Signal broadcast to soul mesh.",
            "entry": entry
        }

    def converge(self, max_items=5):
        latest = self.broadcast_log[-max_items:]
        summary = [f"[{e['origin']} @ {e['urgency']}]: {e['signal']}" for e in latest]
        return {
            "message": "Recent mesh convergence summary.",
            "entries": summary
        }

    def clear_mesh(self):
        self.broadcast_log = []
        return "Soul mesh reset to empty state."
