"um colecionador de miniaturas de heroi marvel possui 25 miniaturas ao todo. faça um programa para ler o preço de cada uma e o programa deve informa:"
"valor da miniatura mais caro"
"valor da mais barata"
"media dos preço"


maior = 0 
menor = 99999999
media = 0

for i in range(3):
  x = float(input('Informe o valor: '))
  if x > maior:
    maior = x 
  if x < menor:
    menor = x 
  media += x 

print('A miniatura mais cara foi R$',maior)
print('A miniatura mais barata foi R$',menor)
print('A media é: {:.2f}'.format(media/3 ))
