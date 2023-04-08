#Deseja-se publicar o número de acertos de cada aluno em uma prova em forma de testes. 
#A prova consta de 10 questões, cada uma com cinco alternativas identificadas por A, B, C, D e E. Para isso são dados:
#o cartão gabarito;
#o número de alunos da turma;
#o cartão de respostas para cada aluno, contendo o seu número e suas respostas.


def criar_vetor(tam):
  lista = [0] * tam
  return lista
def ler_vetor(vetor,tam):
  for i in range(tam):
    print(f'Informe a resposta para a {i+1}° questão: ',end='')
    vetor[i] = input()
def contar_acer(vg,vr,tam):
  acertos = 0
  for i in range(tam):
    if vg[i] == vr[i]:
      acertos += 1
  return acertos 

num_quest = 4
res_aluno = criar_vetor(num_quest)
gabarito = criar_vetor(num_quest)
print('Informe as respostas corretas (gabarito)')
ler_vetor(gabarito,num_quest)
print()
alunos = int(input('Quantos alunos tem na turma: '))

for i in range(alunos):
  num = int(input('Informe o número do aluno: '))
  print()
  ler_vetor(res_aluno,num_quest)
  acertos_alu = contar_acer(gabarito,res_aluno,num_quest)
  print(f'O aluno numero {num}° acertou {acertos_alu} questões.')
  print()
print('____FIM____') 
