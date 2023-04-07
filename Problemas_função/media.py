"Faça um programa para ler as notas das duas unidades de um aluno."
"Informe se este aluno está aprovado (média maior ou igual a 7), na final (entre 4 e 7) ou reprovado (média abaixo de 4). "


def media_uni(uni1,uni2):
  media = (uni1 + uni2) / 2
  return media 

uni1 = float(input('Informe sua primeira nota: ')) 
uni2 = float(input('informe sua segunda nota: '))

media_f = media_uni(uni1,uni2) 
print('Sua nota é', media_f) 

if media_f >= 7:
  print('Aprovado!') 
elif media_f >= 4:
  print('Final!')
else: 
  print('Reprovado!')
