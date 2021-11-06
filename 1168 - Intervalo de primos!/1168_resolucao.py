# ENTRADAS
inicio = int(input())
fim = int(input())
quantidade_primos = 0

def eh_primo(num):
  if num < 2:
    return False  # não é primo
  elif num == 2:
    print(num)
    return True   # é primo
  else:
    for i in range(2, num):
      if num % i == 0:
        return False
    print(num)
    return True

# LOGICA
if (inicio <= fim <= 5000):
  for i in range(inicio, fim + 1):
    if eh_primo(i):
      quantidade_primos += 1
  
  print(f'primos: {quantidade_primos}')