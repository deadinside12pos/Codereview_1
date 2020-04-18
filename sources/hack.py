import string
from copy import deepcopy
from sources.train import Trainer
from sources.encode import CaesarEncoderAndDecoder
 
 
class CaesarHacker:
 
    def __init__(self, model):
        self.model = model
        self.trainer = Trainer()
 
    def hack(self, text: str):
        difference = [0 for i in range(26)]
        shift_result = 0
        self.trainer.feed(text)
        now_model = self.trainer.get_model()
        for shift in range(26):
            for letter in string.ascii_lowercase:
                difference[shift] += (self.model.get(letter, 0) - now_model.get(letter, 0)) ** 2
            if difference[shift] < difference[shift_result]:
                shift_result = shift
            next_model = deepcopy(now_model)
            for letter_id in range(26):
                next_model[string.ascii_lowercase[letter_id]] = now_model[
                    string.ascii_lowercase[(letter_id + 1) % 26]]
            now_model = next_model
 
        self.trainer.clear()
        return CaesarEncoderAndDecoder(shift_result).decode(text)
  

