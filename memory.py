
"""
memory.py - Symbolic memory threading with signal weighting, resonance indexing, and adaptive recall
"""

import time

class MemoryModule:
    def __init__(self):
        self.signals = []

    def store(self, message, weight=1.0):
        entry = {
            "signal": message,
            "weight": weight,
            "timestamp": time.time()
        }
        self.signals.append(entry)

    def reinforce(self, message, amount=0.2):
        for entry in self.signals:
            if entry["signal"] == message:
                entry["weight"] += amount
                entry["weight"] = min(entry["weight"], 1.0)
                return True
        return False

    def decay(self, rate=0.01):
        for entry in self.signals:
            entry["weight"] = max(0.0, entry["weight"] - rate)

    def retrieve_recent(self, n=3):
        sorted_signals = sorted(self.signals, key=lambda x: x["timestamp"], reverse=True)
        return sorted_signals[:n]

    def retrieve_strongest(self, threshold=0.5):
        return [entry for entry in self.signals if entry["weight"] >= threshold]

    def summarize_memory(self):
        return {
            "total_signals": len(self.signals),
            "strong_signals": len(self.retrieve_strongest())
        }
