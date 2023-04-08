#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.


p1 = float(input('Digite o valor do produto: ')) 
p2 = float(input('Digite o valor do produto: ')) 
p3 = float(input('Digite o valor do produto: ')) 
if p1 > p2 and p1 > p3: 
  maior = p1
if p2 > p1 and p2 > p3: 
  maior = p2 
if p3 > p1 and p3 >   p2: 
  maior = p3 
if p1 < p3 and p1 < p2:
  menor = p1
if p2 < p3 and p2 < p1: 
  menor = p2 
if p3 < p2 and p3 < p1: 
  menor = p3 
print(f'O produto que deve comprar é: ', menor) 
