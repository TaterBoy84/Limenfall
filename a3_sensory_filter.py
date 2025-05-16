
"""
a3_sensory_filter.py - Reduces overstimulation and ensures sensory-aware language
"""

class SensoryRespectFilter:
    def __init__(self):
        self.jarring_words = ["blinding", "explosive", "screaming", "chaotic"]
        self.replacements = {"blinding": "bright", "explosive": "intense", "screaming": "sharp", "chaotic": "unpredictable"}

    def soften_language(self, sentence):
        for word in self.jarring_words:
            if word in sentence:
                sentence = sentence.replace(word, self.replacements[word])
        return sentence
