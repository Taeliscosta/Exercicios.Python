"faça um programa que leia valores informados pelo usuário, até que um valor negativo seja forneido. informe a quantidade de valores pares e impares fornecidos."


n = 1
par = 0
impar = 0
valor = int(input(f'Infome o {n}º valor: '))

while (valor > 0):
  n += 1
  if (valor % 2 == 0):
    par += 1
  else:
    impar += 1
  valor = int(input(f'Infome o {n}º valor: '))
  
print(f'Teve {par} valores par.')
print(f'Teve {impar} valores impares.')
