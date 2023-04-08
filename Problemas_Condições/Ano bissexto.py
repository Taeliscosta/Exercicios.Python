#Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.


ano = int(input('Digite um ano: ')) 
if (ano%4 == 0): 
  print('É um ano bissexto!') 
else:
  print('Não é um ano bissexto!') 
