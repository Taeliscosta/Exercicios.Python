"crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. "
"no final mostre um boletim contendo a nota de cada um "
"permita que o usuario possa mostra as notas de cada aluno individualmente."
"Creditos do Exercicio: Curso em Video(Guanabara) Exercicio 089"


b = False
con = False
ficha = []
while con == False:
  nome = str(input('Nome: '))
  nota1 = float(input('Nota 1: '))
  nota2 = float(input('Nota 2: '))
  media = (nota1 + nota2) / 2 
  ficha.append([nome, [nota1, nota2], media])
  res = str(input('Quer continuar? [S/N] '))
  print()
  if res in 'Nn':
    con = True
print('-'*30)
print(f'{"Num.":<4}{"Nome":<10}{"Media":>8}')
print('-'*26)
for i, a in enumerate(ficha):
  print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while b == False:
  print("-"*30)
  opc = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
  if opc == 999:
    print('FINALIZADO.')
    b = True 
  if opc <= len(ficha) - 1:
    print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') 
print()
print('<<< VOLTE SEMPRE >>>')
