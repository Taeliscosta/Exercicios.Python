#Faça um programa que receba duas lista. gere uma terceira lista contendo os elementos das duas lista recebidas, em ordem crescente e sem repetição. imprima as 3 listas


def criar_lista(tam):
  lista = [0] * tam
  return lista

def ler_lista(lista,tam):
  for i in range(tam):
    print(f'Digite o {i+1} da lista: ',end=' ')
    lista[i] = int(input())
  print()

def lista3(lista,lista2,tam):
  l3 = criar_lista(tam)
  l3 = lista + lista2
  return list(set(l3))
  
def imprimir(lista):
  for i in range(0,len(lista)):
    print(lista[i],end=' ')
  print()

tam = int(input('Digite o tamanho das listas: '))
l1 = criar_lista(tam)
l2 = criar_lista(tam)
print('Digite os valores da primeira lista:')
ler_lista(l1,tam)
print('Digite os valores da segunda lista:')
ler_lista(l2,tam)
l3 = lista3(l1,l2,tam)
imprimir(l1)
imprimir(l2)
imprimir(l3)
