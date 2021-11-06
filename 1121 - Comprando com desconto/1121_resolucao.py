# ENTRADAS
preco_da_mercadoria = float(input()) 
quantidade_comparada_da_mercadoria = int(input()) 

# LOGICA
preco_da_compra_sem_desconto = preco_da_mercadoria * quantidade_comparada_da_mercadoria 
desconto_de_dez_por_cento_fixo = 0.1 
desconto_de_um_por_cento_por_item = quantidade_comparada_da_mercadoria * 0.01
total_descontos = preco_da_compra_sem_desconto * (desconto_de_dez_por_cento_fixo + desconto_de_um_por_cento_por_item) 
preco_da_compra_com_desconto = preco_da_compra_sem_desconto - total_descontos

# SAIDAS
print(f'{preco_da_compra_sem_desconto:.2f}')
print(f'{preco_da_compra_com_desconto:.2f}')