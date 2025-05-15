
"""
memory.py - Symbolic memory threading and retrieval system
"""

class MemoryModule:
    def __init__(self):
        self.signals = []

    def store(self, message):
        self.signals.append(message)

    def retrieve_recent(self, n=3):
        return self.signals[-n:]
