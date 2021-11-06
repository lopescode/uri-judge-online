lista_alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                  'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
N = int(input())


def exibe_letras_alfabeto(contador):
    posicao_letra = lista_alfabeto[contador - 1]

    i = 1

    while i <= contador:
        letras_alfabeto = posicao_letra * contador
        i += 1

    print(letras_alfabeto)


if (1 <= N <= 26):

    i = 1

    while i <= N:
        exibe_letras_alfabeto(i)
        i += 1
