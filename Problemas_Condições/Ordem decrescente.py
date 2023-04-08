#Faça um Programa que leia três números e mostre-os em ordem decrescente.


a = float(input('Digite um número: ')) 
b = float(input('Digite um número: ')) 
c = float(input('Digite um número: ')) 

if a > b and a > c and b > c:
  print('A ordem decrescente é ', a, b, 'e', c) 
if a > b and a > c and c > b: 
  print('A ordem decrescente é ', a, c, 'e', b) 
if b > a and b > c and a > c:
  print('A ordem dscrescente é ', b, a, 'e', c) 
if b > a and b > c and c > a: 
  print('A ordem descrescente é ', b, c, 'e', a)
if c > a and c > b and a > b: 
  print('A ordem decrescente é ', c, a, 'e', b)
if c > a and c > b and b > a: 
  print('A ordem decrescente é ', c, b, 'e', a)
