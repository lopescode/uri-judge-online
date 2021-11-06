divida = int(input())
pagamento_mensal = int(input())
contador = 0

while divida != 0:
    contador += 1

    if divida >= pagamento_mensal:
        antes = divida
        divida = divida - pagamento_mensal
        depois = divida
    else:
        antes = divida
        divida = divida - divida
        depois = divida

    print(f'pagamento: {contador}')
    print(f'antes = {antes}')
    print(f'depois = {depois}')
    print('-----')
