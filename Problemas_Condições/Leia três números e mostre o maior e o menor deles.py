#Faça um Programa que leia três números e mostre o maior e o menor deles.


a = int(input('Informe um valor: ')) 
b = int(input('Informe um valor: ')) 
c = int(input('Informe um  valor: ')) 
if a > b and a > c: 
  maior = a 
if b > a and b > c: 
  maior = b 
if c > a and c > b: 
  maior = c 
if a < c and a< b:
  menor = a
if b < c and b < a: 
  menor = b 
if c < b and c < a: 
  menor = c 
print(f"O menor número digitado é: ",menor) 
print(f'O maior número digitado é: ',maior)
