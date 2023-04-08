#crie um programa onde um usuário pode digitar sete valores numéricos e cadastreos em uma lista unica que mantenham separados os valores pares e impares. 
#No final mostre os valores pares e impares em ordem crescente. 


num = [[], []]
valor = 0
for i in range(1, 8):
  valor = int(input(f'Digite o {i} número: '))
  if valor % 2 == 0:
    num[0].append(valor)
  else:
    num[1].append(valor)
num[0].sort()
num[1].sort()
print('-'*30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
