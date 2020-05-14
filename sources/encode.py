from string import ascii_lowercase
 
alphabet = ascii_lowercase
ASCII_BIT_COUNT = 7
BASE = 2
alphabet_size = len(alphabet)
alphabet_upper = alphabet.upper()
 
 
class CaesarEncoderAndDecoder:
    def __init__(self, shift):
        self.shift = int(shift) % alphabet_size

    def getneword(self, ord, shift):
        new_ord = (ord + shift) % alphabet_size
        return new_ord

    def getnewchar(self, char, shift, alphabet):
        ord = alphabet.find(char)
        new_ord = self.getneword(ord, shift)
        return alphabet[new_ord]
 
    def encode(self, text: str, decrypt):
        ans = []
        shift = self.shift * (-1 if decrypt else 1)
        for char in text:
            new = char
            if char.isalpha():
                if char.isupper():
                    new = self.getnewchar(char, shift, alphabet_upper)
                elif char.islower():
                    new = self.getnewchar(char, shift, alphabet)
            ans.append(new)
        return ''.join(ans)

 
class VigenereEncoderAndDecoder:
    def __init__(self, shift):
        shift = shift.lower()
        if not shift.isalpha():
            raise SyntaxError('Key must be a single word')
        self.shift = shift

    def codechar(self, char, position, alphabet, decrypt):
        delta = alphabet.find(self.shift[position % len(self.shift)])
        if decrypt:
            delta = alphabet_size - delta
        return alphabet[(alphabet.find(char) + delta) % alphabet_size]

    def countchar(self, char, position, decrypt):
        if char.islower():
            char = self.codechar(char, position, alphabet, decrypt)
        if char.isupper():
            char = self.codechar(char, position, alphabet_upper, decrypt)
        return char

    def code(self, text, decrypt):
        result = []
        position = 0
        for char in text:
            if char.isalpha():
                char = self.countchar(char, position, decrypt)
                position += 1
            result.append(char)
        return result

    def encode(self, text: str, decrypt):
        result = self.code(text, decrypt)
        return ''.join(result)


class VernamEncoderAndDecoder:
    def __init__(self, key):
        self.key = int(key)

    def encode(self, text: str, decrypt):
        if decrypt:
            bintext = bin(self.key ^ int(text, BASE))[BASE:]
            res = []
            for char in range(0, len(bintext), ASCII_BIT_COUNT):
                res.append(chr(int(bintext[char: char + ASCII_BIT_COUNT], BASE)))
            return ''.join(res)
        else:
            bintext = []
            for char in text:
                bintext.append(bin(ord(char))[BASE:])
            return bin(int(''.join(bintext), BASE) ^ self.key)[BASE:]
