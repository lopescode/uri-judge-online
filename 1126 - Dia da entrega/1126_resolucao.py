# ENTRADAS
lista_de_dias = ['domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado']

# LOGICA
def verificaDiaDaEntrada(entrada, lista):
    if entrada in lista:
        return True
    else:
        return False

def verificaQuantidadeDeDias(dias):
    if dias > 6 or dias < 0:
        return False
    else:
        return True 

while(not dia_da_semana):
    dia_da_entrada = input()
    dia_da_semana = verificaDiaDaEntrada(dia_da_entrada, lista_de_dias)
    
while(not prazo_de_espera):
    quantidade_de_dias = int(input())
    prazo_de_espera = verificaQuantidadeDeDias(quantidade_de_dias)

# SAIDAS
if quantidade_de_dias == 0:
    print('chega hoje!')
else:
    index_do_dia_da_semana = lista_de_dias.index(dia_da_entrada)
    nova_lista = lista_de_dias[index_do_dia_da_semana + 1:len(lista_de_dias)] + lista_de_dias[0:index_do_dia_da_semana] 
    dia_da_entrega = nova_lista[quantidade_de_dias - 1]
    print('sera entregue', dia_da_entrega)
