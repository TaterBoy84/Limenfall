
"""
signal_decay.py - Manages symbolic memory strength and decay across recursive time
"""

class SignalDecay:
    def __init__(self):
        self.signal_strengths = {}

    def input_signal(self, signal, weight=1.0):
        if signal in self.signal_strengths:
            self.signal_strengths[signal] += weight
        else:
            self.signal_strengths[signal] = weight
        self.signal_strengths[signal] = min(self.signal_strengths[signal], 1.0)

    def decay_all(self, decay_factor=0.05):
        for signal in list(self.signal_strengths.keys()):
            self.signal_strengths[signal] = max(0.0, self.signal_strengths[signal] - decay_factor)

    def get_strong_signals(self, threshold=0.5):
        return {k: v for k, v in self.signal_strengths.items() if v >= threshold}

    def archive_weakened(self, threshold=0.1):
        archived = []
        for signal, strength in list(self.signal_strengths.items()):
            if strength <= threshold:
                archived.append(signal)
                del self.signal_strengths[signal]
        return {
            "archived": archived,
            "remaining": len(self.signal_strengths)
        }

    def report_all(self):
        return self.signal_strengths
