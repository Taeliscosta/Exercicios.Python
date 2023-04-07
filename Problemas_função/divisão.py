"faça uma função que rceba dois valores e retorne verdadeiro, caso o primeiro valor seja divisivel pelo o segundo, falso, caso contrario "


def divisao(a,b):
  if a % b == 0:
    return True 
  return False 

a = int(input('informe um valor: '))
b = int(input('informe um valor: '))
print(divisao(a,b))
