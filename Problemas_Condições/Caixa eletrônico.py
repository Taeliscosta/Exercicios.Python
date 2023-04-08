#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
#As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
#O programa não deve se preocupar com a quantidade de notas existentes na máquina. 
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1; 
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


x = int(input('Digite um número')) 
aux = x 

n100 = 0 
n50 = 0 
n10 = 0
n5 = 0 

if (x >= 100): 
  n100 = x // 100
  x = x%100 
if (x >= 50): 
  n50 = x // 50 
  x = x%50 
if (x >= 10):
  n10 = x // 10 
  x = x%10 
if (x >= 5): 
  n5 = x // 5 
  x = x%5

print(f'Para sacar a quantia de {aux} reais: {n100} notas de 100, {n50} notas de 50, {n10} notas de 10, {n5} notas de 5 e {x} notas de 1.')
