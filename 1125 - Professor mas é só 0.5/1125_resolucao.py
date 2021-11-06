# ENTRADAS
nota_de_trabalhos = float(input())
nota_da_prova_regular = float(input())

# LOGICA
media_final = (nota_de_trabalhos + nota_da_prova_regular) / 2

# SAIDAS
if media_final >= 6:
    print('aprovado')
elif (media_final < 6 and nota_de_trabalhos >= 2.00):
    print('talvez com a sub')
else:  
    print('reprovado')

