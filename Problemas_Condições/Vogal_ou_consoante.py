"Faça um Programa que verifique se uma letra digitada é vogal ou consoante"


a = input('Informe uma letra: ') 
a = a.lower()
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
  print('É uma vogal') 

else:
  print('É uma cosoante')
