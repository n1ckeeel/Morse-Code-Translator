class MorseEncoder:
    def __init__(self, mapping):
        self.mapping = mapping
        
    def encode(self, text):
        return " ".join(self.mapping.to_morse(c) for c in text)
      
