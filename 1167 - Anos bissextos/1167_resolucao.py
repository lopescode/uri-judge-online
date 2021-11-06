# ENTRADAS
inicio = int(input())
fim = int(input())
quantidade_bissexto = 0

# LOGICA
if (0 <= inicio <= fim <= 9999):
  while inicio <= fim:
    if (inicio % 4 == 0 and inicio % 100 != 0 or inicio % 400 == 0):
      print(inicio)
      quantidade_bissexto += 1
    
    inicio += 1
  
  print(f'bissextos: {quantidade_bissexto}')
