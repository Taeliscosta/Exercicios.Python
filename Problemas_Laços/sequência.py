"Dado um número n, considere a seguinte sequência: 01223334444"
"Sua tarefa é fazer um programa que, dado um número n, tenha como resposta a quantidade total de números dessa sequência e logo abaixo a sequencia completa, nessa ordem."


x = 1 
for i in range(x):
  a = int(input('Digite um número: '))
  n = 0
  for i in range(a + 1):
    n += i

  if n == 1:
    print(f'A quantidade é {n} números')
  else:
    print(f'A quantidade é {n} números')

  if a == 0:
    print(0)

  for i in range(a+1):
    for j in range(i):
      if i == a and j == a - 1:
        print(i)
      else:
        print(i,end=' ')

  print('')
  x+=1
