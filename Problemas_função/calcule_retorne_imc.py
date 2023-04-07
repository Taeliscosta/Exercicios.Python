"faça uma função que calcule e retorne o imc de uma pessoa, que é dado pela formula IMC = p/h^2   onde p = peso e h = altura "
"solicite ao usuario os dados reerentes a uma pessoa, calcule seu IMC e nforme a situação da pessoa de acordo com a classificação a seguir "
"baixo peso: imc abaixo de 18.5kg/m²" 
"peso normal: IMC entre 18.5 e 24.9kg/m²" 
"sobre peso: imc entre 24.9 e 29.9k/m² "
"obesidade: imc acima de 29.9 "

def imc_pessoa(peso,altura):
  imc = peso / altura ** 2
  return imc 

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc2 = imc_pessoa(peso,altura)   

if imc2 < 18.5: 
  print('Baixo peso, IMC abaixo de 18,5kgm² ') 
elif imc2 < 24.9: 
  print('Peso normal, IMC entre 18,5kg/m² e 24,9kg/m²')
elif imc2 < 29.9:
  print('Sobre peso, IMC entre 24,9kg/m² e 29,9kg/m²')
elif imc2 > 29.9:
  print('Obesidade, IMC acima de 29,9kg/m²')
