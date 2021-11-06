# ENTRADA
valor_digitado = int(input()) # 55

# TESTANDO SE O VALOR DIGITADO É PAR
if valor_digitado % 2 == 0:
# ESSA LOGICA SÓ FUNCIONA SE EU DIGITAR UM NUMERO PAR
    impar_que_antecede_valor_digitado = valor_digitado - 1
    par_que_sucede_valor_digitado = valor_digitado + 2
else:
# ESSA LOGICA SÓ FUNCIONA SE EU DIGITAR UM NUMERO IMPAR
    impar_que_antecede_valor_digitado = valor_digitado - 2
    par_que_sucede_valor_digitado = valor_digitado + 1

# SAIDA
print(f'{impar_que_antecede_valor_digitado} {par_que_sucede_valor_digitado}')