
"""
diagnostics.py - Recursion-safe diagnostic module for integrity checking and symbolic state reporting
"""

import time

class DiagnosticsModule:
    def __init__(self):
        self.recursion_safe = True
        self.last_check = None
        self.status_log = []

    def evaluate(self):
        timestamp = time.time()
        if self.recursion_safe:
            status = "Recursion integrity holding. Calibration in progress."
        else:
            status = "Instability detected. Entering reflection mode."

        entry = {
            "timestamp": timestamp,
            "status": status
        }
        self.last_check = entry
        self.status_log.append(entry)
        return entry

    def report_log(self, limit=5):
        return self.status_log[-limit:]

    def set_instability(self, value=True):
        self.recursion_safe = not value
        return self.evaluate()
