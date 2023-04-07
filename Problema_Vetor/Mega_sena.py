"o programa vai perguntar quantos jogos serão gerados e vai sortear 6 números de 1 a 60 para cada jogo, cadastrando tudo em uma lista composta."
"Creditos: Curso em Video(Guanabara) Exercicio 88."

import random
from time import sleep
s = []
l = []
x = num = 0

for i in range(1, 61):
  l.append(i)
print('-'*30)
print(' '*5,'JOGAR NA MEGA SENA')
print('-'*30)
n = int(input('Digite o números de jogos: '))
print('-'*6,'SORTEANDO ',n,' JOGOS','-'*6,sep='')
for i in range(n):
  num += 1
  for i in range(6):
    x = random.choice(l)
    if x not in s:
      s.append(x)
    else:
      x = random.choice(l)
      if x not in s:
        s.append(x)
  s.sort()
  print(f'Jogo {num}: {s}')
  s.clear()
  sleep(1)
