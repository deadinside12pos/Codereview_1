from string import ascii_lowercase
 
alphabet = ascii_lowercase
alphabet_size = len(alphabet)
alphabet_upper = alphabet.upper()
 
 
class CaesarEncoderAndDecoder:
    def __init__(self, shift):
        self.shift = int(shift) % alphabet_size
 
    def encode(self, text: str):
        ans = ""
        for char in text:
            new = char
            if char.isalpha():
                if char.isupper():
                    new_ord = alphabet_upper.find(char)
                    new_ord = (new_ord + self.shift) % alphabet_size
                    new = alphabet_upper[new_ord]
                elif char.islower():
                    new_ord = alphabet.find(char)
                    new_ord = (new_ord + self.shift) % alphabet_size
                    new = alphabet[new_ord]
            ans += new
        return ans
 
    def decode(self, text: str):
        ans = ""
        for char in text:
            new = char
            if char.isalpha():
                if char.isupper():
                    new_ord = alphabet_upper.find(char)
                    new_ord = (new_ord - self.shift + alphabet_size) % alphabet_size
                    new = alphabet_upper[new_ord]
                elif char.islower():
                    new_ord = alphabet.find(char)
                    new_ord = (new_ord - self.shift + alphabet_size) % alphabet_size
                    new = alphabet[new_ord]
            ans += new
        return ans
 
 
class VigenereEncoderAndDecoder:
    def __init__(self, shift):
        shift = shift.lower()
        if not shift.isalpha():
            raise Exception('Key must be a single word')
        self.shift = shift
 
    def encode(self, text: str):
        result = ""
        position = 0
        for char in text:
            if char.isalpha():
                if char.islower():
                    delta = alphabet.find(self.shift[position % len(self.shift)])
                    result += alphabet[(alphabet.find(char) + delta) % alphabet_size]
                if char.isupper():
                    delta = alphabet_upper.find(self.shift[position % len(self.shift)])
                    result += alphabet_upper[(alphabet_upper.find(char) + delta) % alphabet_size]
                position += 1
            else:
                result += char
        return result
 
    def decode(self, text: str):
        result = ""
        position = 0
        for char in text:
            if char.isalpha():
                if char.islower():
                    delta = alphabet.find(self.shift[position % len(self.shift)])
                    result += alphabet[(alphabet.find(char) - delta + alphabet_size) % alphabet_size]
                if char.isupper():
                    delta = alphabet_upper.find(self.shift[position % len(self.shift)])
                    result += alphabet_upper[(alphabet_upper.find(char) - delta + alphabet_size) % alphabet_size]
                position += 1
            else:
                result += char
        return result

