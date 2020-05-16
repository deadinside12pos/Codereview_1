from collections import defaultdict
from sources.train import Trainer
from sources.encode import CaesarEncoderAndDecoder, alphabet, alphabet_size
 
 
class CaesarHacker:
 
    def __init__(self, model):
        self.model = model
        self.trainer = Trainer()
 
    def hack(self, text: str):
        difference = defaultdict(int)
        shift_result = 0
 
        self.trainer.feed(text)
        current_model = self.trainer.get_model()
 
        for shift in range(alphabet_size):
            for letter in alphabet:
                encrypted_letter = CaesarEncoderAndDecoder(0).getnewchar(letter, shift, alphabet)
                difference[shift] += (self.model[letter] - current_model[encrypted_letter]) ** 2
 
            if difference[shift] < difference[shift_result]:
                shift_result = shift

        return CaesarEncoderAndDecoder(shift_result).encode(text, True)
