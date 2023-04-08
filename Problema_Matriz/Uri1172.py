"Leia uma matriz X[10]. Depois, substitua cada número nulo ou negativo de X por 1. Imprima todos os números armazenados na matriz X."
"A entrada contém 10 números inteiros. Esses números podem ser positivos ou negativos."
"Resultado: Para cada posição do array, imprima "X [i] = x", onde i é a posição do array e x é o número armazenado naquela posição."

x = []
for i in range(10):
  valor = int(input('Digite um número: '))
  if valor <= 0:
    valor = 1
    x.insert(i,valor)
  else:
    x.insert(i,valor)
for i in range(10):
  print('x [{0}] = {1}'.format(i,x[i]))
