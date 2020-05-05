from string import ascii_lowercase
 
alphabet = ascii_lowercase
bitlength = 7
alphabet_size = len(alphabet)
alphabet_upper = alphabet.upper()
 
 
class CaesarEncoderAndDecoder:
    def __init__(self, shift):
        self.shift = int(shift) % alphabet_size

    def getneword(self, ord, shift):
        new_ord = (ord + shift) % alphabet_size
        return new_ord

    def code(self, char, shift):
        new = char
        if char.isalpha():
            if char.isupper():
                ord = alphabet_upper.find(char)
                new_ord = self.getneword(ord, shift)
                new = alphabet_upper[new_ord]
            elif char.islower():
                ord = alphabet.find(char)
                new_ord = self.getneword(ord, shift)
                new = alphabet[new_ord]
        return new
 
    def encode(self, text: str):
        ans = []
        for char in text:
            new = self.code(char, self.shift)
            ans.append(new)
        return ''.join(ans)
 
    def decode(self, text: str):
        ans = []
        for char in text:
            new = self.code(char, alphabet_size - self.shift)
            ans.append(new)
        return ''.join(ans)
 
 
class VigenereEncoderAndDecoder:
    def __init__(self, shift):
        shift = shift.lower()
        if not shift.isalpha():
            raise SyntaxError('Key must be a single word')
        self.shift = shift

    def codechar(self, char, position, alphabet, de):
        delta = alphabet.find(self.shift[position % len(self.shift)])
        if de:
            delta = alphabet_size - delta
        return alphabet[(alphabet.find(char) + delta) % alphabet_size]

    def countchar(self, char, position, de):
        if char.islower():
            char = self.codechar(char, position, alphabet, de)
        if char.isupper():
            char = self.codechar(char, position, alphabet_upper, de)
        return char

    def code(self, text, de):
        result = []
        position = 0
        for char in text:
            if char.isalpha():
                char = self.countchar(char, position, de)
                position += 1
            result.append(char)
        return result

    def encode(self, text: str):
        result = self.code(text, False)
        return ''.join(result)
 
    def decode(self, text: str):
        result = self.code(text, True)
        return ''.join(result)


class VernamEncoderAndDecoder:
    def __init__(self, key):
        self.key = int(key)

    def encode(self, text: str):
        bintext = []
        for char in text:
            bintext.append(bin(ord(char))[2:])
        return bin(int(''.join(bintext), 2) ^ self.key)[2:]

    def decode(self, text: str):
        bintext = bin(self.key ^ int(text, 2))[2:]
        res = []
        for char in range(0, len(bintext), bitlength):
            res.append(chr(int(bintext[char: char + bitlength], 2)))
        return ''.join(res)
