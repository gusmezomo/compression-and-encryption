# transform char into decimal in ASCII table
def text_to_decimals(text: str) -> list[int]:
    return [ord(char) for char in text]


def fibonacci_encode(decimal: int) -> list[int]:
    fibonacci_reverse = [233, 144, 89, 55, 34, 21, 13, 8, 5, 3, 2, 1]
    bits = []

    # the logic to put 1 and 0 in the correct places
    for fibo in fibonacci_reverse:
        if decimal >= fibo:
            bits.append(1)
            decimal -= fibo
        else:
            bits.append(0)

    bits.reverse()  # reverse in place, then return separately
    bits.append(1)
        
    return ''.join(str(bit) for bit in bits)

text = input("Choose something: ")
decimal_text = text_to_decimals(text)
print(f"Decimals: {decimal_text}")

encodes = []

# join every encode bit
for decimal in decimal_text:
    bits = fibonacci_encode(decimal)
    encodes.append(bits)  
    
final_encode = ''.join(str(encode) for encode in encodes)

print(f"Encode -> {final_encode}")