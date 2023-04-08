#crie um programa que crie uma matrix de dimensão 3x3 e prencha com valores lidos pelo teclado. No final mostre a matrix na tela com a formatação correta. 


matrix = [[0, 0, 0],[0, 0 , 0],[0 , 0, 0]] 
for l in range(0, 3):
  for c in range(0, 3):
    matrix[l][c] = int(input(f'Digite um valor para {[l],[c]}: '))
print('-'*30)
for l in range(0, 3):
  for c in range(0, 3):
    print(f'[{matrix[l][c]:^5}]',end='')
  print()
