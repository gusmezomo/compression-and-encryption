import math

class Golomb:

    @classmethod
    def encode(cls, symbol_str: str) -> str:
        #! CODIFICACAO

        #* Inputs: simbolo e divisor K
        entrada_simbolo = int(symbol_str)
        if entrada_simbolo < 0:
            raise ValueError("entrada invalalida.")

        while True:
            entrada_divisor = int(input("digite o divisor (K): "))
            if entrada_divisor >= 1:
                break
            print("entrada invalalida.")

        #* dividindo o simbolo pelo divisor K
        #* quociente = numero de zeros no prefixo
        quociente = entrada_simbolo // entrada_divisor
        #* resto = valor que vira o sufixo
        resto = entrada_simbolo % entrada_divisor

        #* Prefixo (unario) - + '1' = Stopbit
        unario = '0' * quociente + '1'

        #* quantidade de bits do sufixo = log2(K)
        num_bits = int(math.log2(entrada_divisor))

        #* sufixo = resto convertido para binario com num_bits digitos
        sufixo = format(resto, f'0{num_bits}b')

        return unario + sufixo

    @classmethod
    def decode(cls, codeword_str: str) -> str:
        #! DECODIFICACAO

        #* Inputs: bits e "K"
        entrada_codeword = codeword_str
        caracteres_permitidos = set("01")
        valido = all(c in caracteres_permitidos for c in entrada_codeword)
        if not valido:
            raise ValueError("entrada invalalida.")

        while True:
            entrada_divisor_decode = int(input("digite o divisor (K): "))
            if entrada_divisor_decode >= 1:
                break
            print("entrada invalalida.")

        #* decodificar o prefixo (unario)
        #* q = contador = stopbit
        q = 0
        for i in entrada_codeword:
            if i == '0':
                q += 1
            else:
                break

        #* decodificar o sufixo
        sufixo = (entrada_codeword[q+1:])

        #* transformando o sufixo str em int base 2(0,1)
        R = int(sufixo, 2)

        #* reconstruindo o numero original
        #* q = quociente (numero de zeros no prefixo)
        #* entrada_divisor_decode = K (divisor)
        #* R = resto (sufixo convertido de binario para decimal)
        Num = q * entrada_divisor_decode + R
        return str(Num)
