"Faça uma função que receba uma matriz quadrada e sua ordem. essa função deve retornar true ou false, informando se ela é uma matriz identidade ou não."
"A matriz identidade possui o valor 1 em toda sua diagonal principal, e 0 em todas as demais posições."


def criar_matriz(lin,col):
  m = []
  for i in range(lin):
    m.append([0] * col)
  return m

def ler_matriz(m,lin,col):
  for i in range(lin):
    for j in range(col):
      print('m[',i+1,',',j+1,']:',sep='',end=' ')
      m[i][j] = int(input())

def imprimir_matriz(m,lin,col):
  for i in range(lin):
    for j in range(col):
      print(m[i][j],end=' ')
    print()
    
def m_qua(m,ordem):
  for i in range(ordem):
      if m[i][i] == 1:
        if m[i][i+1] == 0 and m[i][i-1] == 0:
          return True
        return False
      else:
        return False
      
ordem = int(input('Digite a ordem da matriz: '))
m = criar_matriz(ordem,ordem)
ler_matriz(m,ordem,ordem)
imprimir_matriz(m,ordem,ordem)
print(m_qua(m,ordem))
