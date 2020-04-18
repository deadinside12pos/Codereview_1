class CaesarEncoderAndDecoder:
    def __init__(self, shift):
        self.shift = int(shift) % 26
 
    def encode(self, text: str):
        ans = ""
        for char in text:
            new_ord = ord(char)
            if char.isalpha():
                if char.isupper():
                    new_ord = ord('A') + (ord(char) - ord('A') + self.shift) % 26
                elif char.islower():
                    new_ord = ord('a') + (ord(char) - ord('a') + self.shift) % 26
            ans += chr(new_ord)
        return ans
 
    def decode(self, text: str):
        ans = ""
        for char in text:
            new_ord = ord(char)
            if char.isalpha():
                if char.isupper():
                    new_ord = ord('A') + (ord(char) - ord('A') + 26 - self.shift) % 26
                elif char.islower():
                    new_ord = ord('a') + (ord(char) - ord('a') + 26 - self.shift) % 26
            ans += chr(new_ord)
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
                start = ord('A') if char.isupper() else ord('a')
                delta = ord(self.shift[position % len(self.shift)]) - ord('a')
                result += chr(start + (ord(char) - start + delta) % 26)
                position += 1
            else:
                result += char
        return result
 
    def decode(self, text: str):
        result = ""
        position = 0
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                delta = ord(self.shift[position % len(self.shift)]) - ord('a')
                result += chr(start + (ord(char) - start - delta + 26) % 26)
                position += 1
            else:
                result += char
        return result

