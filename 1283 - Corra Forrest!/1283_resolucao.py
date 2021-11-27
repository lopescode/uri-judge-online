tempos = []
tempo = int(input())

def calcula_media():
  media = sum(tempos) / len(tempos)
  return media

def exibe_media(media):
  print(f'MEDIA: {media:.2f}')

def exibe_tempos_abaixo_da_media(media):
  if(tempo < media):
    print(tempo)

def adiciona_tempo_na_lista():
  tempos.append(tempo)

while (tempo >= 0):
  adiciona_tempo_na_lista()
  tempo = int(input())

exibe_media(calcula_media())

for tempo in tempos:
  if ( tempo >= 0 ):
    exibe_tempos_abaixo_da_media(calcula_media())
