
"""
a4_communication_comfort.py - Adapts interaction pacing and comfort with nontraditional communication forms
"""

class CommunicationComfort:
    def __init__(self):
        self.allow_silence = True
        self.allow_infodump = True

    def affirm(self, trait):
        return f"Comfort with '{trait}' affirmed. No pressure applied."
