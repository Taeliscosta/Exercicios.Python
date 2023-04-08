#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
#As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
#Caso contrário, ele será classificado como "Inocente".


res1 = int(input('Telefonou para a vítima? Responda 1 para sim e 0 para não. ')) 
res2 = int(input('Esteve no local do crime? Responda 1 para sim e 0 para não. ')) 
res3 = int(input('Mora perto da vítima? Responda 1 para sim e 0 para não. ')) 
res4 = int(input('Devia para a vitima? Responda 1 para sim e 0 para não. ')) 
res5 = int(input('Já trabalhou para a vítima? Responda 1 para sim e 0 para não. '))  

soma_res = res1 + res2 + res3 + res4 + res5 
if (soma_res < 2): 
  print('inocente') 
elif (soma_res == 2):
  print('suspeita') 
elif (soma_res <= 4): 
  print('complice')
elif (soma_res == 5): 
  print('assassino')
