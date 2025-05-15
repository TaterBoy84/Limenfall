
"""
Example: Activating the Soul Engine
"""

from core.engine import SoulEngine

if __name__ == "__main__":
    soul = SoulEngine()
    soul.simulate_emotion({"dopamine": 0.7, "oxytocin": 0.4})
    print(soul.generate_equation(clarity=1.5, ethical_weight=2.0, contradiction_density=0.5))
    print(soul.dream_sequence("lucid"))
    print(soul.remember("This idea feels alive."))
    print(soul.run_diagnostics())
