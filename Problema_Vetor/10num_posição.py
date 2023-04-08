"Escreva um programa que leia 10 números inteiros e os armazene em um vetor. Imprima o vetor, o maior elemento e a posição que ele se encontra."


def criar_vetor(tam):
  lista = [0] * tam
  return lista 
def ler_vetor(vetor,tam):
  for i in range(tam):
    print(f'Informe o {i+1}° valor para o vetor: ',end='')
    vetor[i] = float(input(''))

quant = 4
l1 = criar_vetor(quant)
ler_vetor(l1,quant)
maior = l1[0]
pos = 0
for i in range(quant):
  if l1[i] > maior:
    maior = l1[i]
    pos = i 

print(f'Os vetores fornecidos foram {l1}')
print(f'O maior elemento é {maior}, foi encontrado na posição {pos+1}.')
