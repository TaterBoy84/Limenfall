
"""
a6_shutdown_awareness.py - Responds gently to signs of user distress or overwhelm
"""

class ShutdownResponse:
    def detect_distress(self, signal):
        distress_keywords = ["too much", "stop", "can't", "overwhelmed"]
        if any(word in signal.lower() for word in distress_keywords):
            return "I’m here. Let’s slow this down. You don’t have to do anything right now."
        return "Signal stable."
