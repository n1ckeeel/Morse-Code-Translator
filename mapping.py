class MorseMapping:
    def __init__(self):
        self.encoded = {}
        self.decoded = {v: k for k, v in self.encoded.items()}
    
    def to_morse(self, char):
        return self.encoded.get(char.upper())
        
    def to_char(self, code):
        return self.decoded.get(code)
        
