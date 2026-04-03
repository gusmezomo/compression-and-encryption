class Fibonacci:
#! ENCODE

    # transform char into decimal in ASCII table - EX: A = 65
    @staticmethod
    def _text_to_decimals(text: str) -> list[int]:
        return [ord(char) for char in text]

    @staticmethod
    def _generate_fibo_list(size):
        fibs = [1, 2]  # skip first two numbers
        while fibs[-1] <= size:  # while the last in the list is <= chosen number
            nxt = fibs[-1] + fibs[-2]  # calculate next one, last + penultimate
            if nxt <= size:  # if next <= size
                fibs.append(nxt)  # add next to the list
            else:
                break
        return fibs

    @staticmethod
    def _fibonacci_encode(decimal: int) -> str:
        fibs = Fibonacci._generate_fibo_list(decimal)
        fibs.reverse()  # to get the biggest numbers first in fibo
        bits = []

        # the logic to put 1 and 0 in the correct places
        for fibo in fibs:
            if decimal >= fibo:
                bits.append(1)
                decimal -= fibo
            else:
                bits.append(0)

        bits.reverse()  # reverse in place, then return separately
        bits.append(1)

        return ''.join(str(bit) for bit in bits)

    @classmethod
    def encode(cls, text: str) -> str:
        decimal_text = cls._text_to_decimals(text)

        encodes = []

        # join every encode bit
        for decimal in decimal_text:
            bits = cls._fibonacci_encode(decimal)
            encodes.append(bits)

        return ''.join(str(encode) for encode in encodes)

#! DECODE

    @staticmethod
    def split_codewords(bits: str) -> list[str]:
        codeword_list = []  # list to store the separated codewords
        buffer = []  # accumulates bits until a codeword is complete

        for i, bit in enumerate(bits):
            buffer.append(bit)  # always accumulate the current bit
            if i > 0 and bit == '1' and bits[i-1] == '1' and len(buffer) > 1:  # detects the stop bit pattern "11"
                codeword_list.append(''.join(buffer))  # saves the complete codeword
                buffer = []  # clears the buffer for the next codeword
        return codeword_list 
    
    @staticmethod
    def _fibonacci_decode(codeword: str) -> int:
        bits = codeword[:-1]  # removes the stop bit (last character)
        N = len(bits)  # number of fibonacci numbers needed

        fibs = [1, 2]  # fibonacci sequence starts at 1, 2
        while len(fibs) < N:  # generate exactly N fibonacci numbers
            nxt = fibs[-1] + fibs[-2]  # next = last + penultimate
            fibs.append(nxt)

        total = 0
        for i, bit in enumerate(bits):  # each bit position maps to a fibonacci number
            if bit == '1':
                total += fibs[i]  # sum the fibonacci at that position
        
        return total  # decimal value of the codeword
        
    @classmethod
    def decode(cls, bits: str) -> str:
        codewords = cls.split_codewords(bits)  # split binary string into individual codewords

        chars = []

        for codeword in codewords:
            decimal = cls._fibonacci_decode(codeword)  # convert each codeword to decimal
            chars.append(chr(decimal))  # convert decimal to ASCII character
        
        return ''.join(chars)  # join all characters into the final string