import json
import string
from collections import defaultdict


class Trainer:
 
    def __init__(self):
        self.count = defaultdict(int)
        self.letter_count = 0

    def feed(self, text: str):
        for char in text.lower():
            if char.isalpha():
                self.count[char] += 1
                self.letter_count += 1
 
    def get_model(self):
        result = defaultdict(float)
        for letter in string.ascii_lowercase:
            if self.letter_count != 0:
                result[letter] = self.count[letter] / self.letter_count
        return result
 
    def get_json_model(self):
        return json.dumps(self.get_model())

