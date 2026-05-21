class MorseDecoder:
    def __init__(self, mapping):
        self.mapping = mapping
        
    def decode(self, code):
        return "".join(self.mapping.to_char(s) for s in code.split())
      
