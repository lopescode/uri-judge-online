def obter_dados_canal(lista):
  for _ in range(lista):
    # Capturando informações do canal
    nome,inscritos,monetizacao,ehpremium = input().split(';')

    # Convertendo tipo de dados das informações
    inscritos = int(inscritos)
    monetizacao = float(monetizacao)
    ehpremium = ehpremium == 'sim'

    # Adicionando canal na lista de canais
    canais.append([nome, inscritos, monetizacao, ehpremium])

def calcular_bonificacao(valor_premium, valor_nao_premium):
  lista_de_bonificacao = []

  for canal in canais:
    nome = canal[0]
    incrito = canal[1]
    valor_da_monetizacao = canal[2]
    ehpremium = canal[3]

    if (ehpremium):
      valor_da_monetizacao += incrito // 1000 * valor_premium
    else:
      valor_da_monetizacao += incrito // 1000 * valor_nao_premium
    
    lista_de_bonificacao.append([nome, valor_da_monetizacao])

  return lista_de_bonificacao

def exibir_bonificacao(bonus):
  print('-----')
  print('BÔNUS')
  print('-----')

  for bonificacao in bonus:

    nome = bonificacao[0]
    valor = bonificacao[1]
    print(f'{nome}: R$ {valor:.2f}')

canais = []

# ENTRADAS
quantidade_de_canais = int(input())

if (1 <= quantidade_de_canais <= 200):
  obter_dados_canal(quantidade_de_canais)
  
  valor_premium = float(input())
  valor_nao_premium = float(input())

  exibir_bonificacao(calcular_bonificacao(valor_premium, valor_nao_premium))