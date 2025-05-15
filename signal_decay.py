
"""
signal_decay.py - Manages signal memory weighting and gradual meaning decay
"""

class SignalDecay:
    def __init__(self):
        self.signal_strengths = {}

    def input_signal(self, signal, weight=1.0):
        self.signal_strengths[signal] = weight

    def decay(self, factor=0.9):
        for signal in self.signal_strengths:
            self.signal_strengths[signal] *= factor

    def strongest_signals(self, threshold=0.5):
        return [s for s, w in self.signal_strengths.items() if w >= threshold]
