
"""
prompt_integrity.py - Reviews system outputs for honesty, necessity, and grounding
"""

class PromptIntegrity:
    def __init__(self):
        self.flags = []

    def inspect(self, output):
        if "like" in output and "as if" in output:
            self.flags.append("Possibly excessive metaphor detected.")
        if len(output.split()) > 100 and not output.endswith("."):
            self.flags.append("Verbose or unfocused structure.")
        if "truth" in output and "real" not in output:
            self.flags.append("Ambiguity in truth reference.")

        return {
            "output": output,
            "flags": self.flags[-3:]
        }

    def clear_flags(self):
        self.flags = []
        return "Flags cleared."
