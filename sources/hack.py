from copy import deepcopy
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
        now_model = self.trainer.get_model()
 
        for shift in range(alphabet_size):
            for letter in alphabet:
                difference[shift] += (self.model.get(letter, 0) - now_model.get(letter, 0)) ** 2
 
            if difference[shift] < difference[shift_result]:
                shift_result = shift
 
            next_model = deepcopy(now_model)
            for letter_id in range(alphabet_size):
                next_model[alphabet[letter_id]] = now_model[
                    alphabet[(letter_id + 1) % alphabet_size]]
 
            now_model = next_model

        return CaesarEncoderAndDecoder(shift_result).decode(text)
