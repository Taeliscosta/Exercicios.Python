"faça um programa que leia nomes para serem inseridos em uma lista, até que o usuario digite a palavra fim, que não deve ser inserida na lista."
"Na sequencia imprima a lista de traz para frente:"


l1 = []
def inserir(lista):
  n = 0
  while True:
    n += 1
    name = str(input(f'Digite o {n}° nome/ (fim) para encerrar:  '))
    if 'fim' in name:
      return lista
    else: 
      lista.append(name)
  
a = inserir(l1)
a.reverse()
print(a)
