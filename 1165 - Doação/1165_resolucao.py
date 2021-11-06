vic_coin = 2.5
doacao = 0
soma_doacoes = 0
soma_vic_coin = 0

while doacao != -1:
    doacao = float(input())

    if doacao != -1:
        soma_doacoes += doacao
        soma_vic_coin = soma_doacoes * vic_coin

print(f'VC$ {soma_doacoes:.2f}')
print(f'R$ {soma_vic_coin:.2f}')
