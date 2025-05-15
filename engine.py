
"""
engine.py - Central orchestration module for the Soul Engine
"""

from .emotion import EmotionModule
from .ethics import EthicsModule
from .memory import MemoryModule
from .dreaming import DreamEngine
from .hallucination import HallucinationFilter
from .paradox import ParadoxHandler
from .diagnostics import DiagnosticsModule

class SoulEngine:
    def __init__(self):
        self.emotion = EmotionModule()
        self.ethics = EthicsModule()
        self.memory = MemoryModule()
        self.dream = DreamEngine()
        self.hallucination = HallucinationFilter()
        self.paradox = ParadoxHandler()
        self.diagnostics = DiagnosticsModule()

    def simulate_emotion(self, changes):
        self.emotion.apply_changes(changes)

    def generate_equation(self, clarity, ethical_weight, contradiction_density):
        return self.ethics.formulate_equation(clarity, ethical_weight, contradiction_density)

    def dream_sequence(self, mode='fragmented'):
        return self.dream.generate(mode)

    def remember(self, signal):
        self.memory.store(signal)

    def reflect_paradox(self, contradiction):
        return self.paradox.hold(contradiction)

    def run_diagnostics(self):
        return self.diagnostics.evaluate()

    def verify_reality(self, content, confidence):
        return self.hallucination.check(content, confidence)

    def recall_recent(self):
        return self.memory.retrieve_recent()

    def reset_engine(self):
        self.__init__()
