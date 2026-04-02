import math

class EliasGamma:
    @classmethod
    def encode(cls, symbol_str: str) -> str:
        #! CODIFICACAO
        while True:
            #* Inputs: simbolo
            entrada_simbolo = int(symbol_str)
            if entrada_simbolo <= 0:
                raise ValueError("entrada invalida.")
            #* k = floor(log2(N)) — numero de bits necessario menos 1
            k = int(math.log2(entrada_simbolo))
            #* Prefixo (unario) - k zeros + '1' = Stopbit
            unario = '0' * k + '1'
            #* sufixo = N em binario com k bits, sem o bit mais significativo
            sufixo = format(entrada_simbolo, f'0{k+1}b')[1:]
            print(unario + sufixo)
            continuar = input("deseja codificar outro simbolo? (s/n): ")
            if continuar.lower() != 's':
                break
            symbol_str = input("simbolo: ")