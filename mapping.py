import json
import os

class MorseMapping:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "character_set.json")
        with open(path, "r") as f:
            self.encoded = json.load(f)

        self.decoded = {v: k for k, v in self.encoded.items()}

    def to_morse(self, char):
        return self.encoded.get(char.upper(), "")

    def to_char(self, code):
        return self.decoded.get(code, "")
