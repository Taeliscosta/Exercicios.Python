"Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)"
"3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita)."
"O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês." 
"Desconto do IR:"
"Salário Bruto até 900 (inclusive) - isento"
"Salário Bruto até 1500 (inclusive) - desconto de 5%"
"Salário Bruto até 2500 (inclusive) - desconto de 10%"
"Salário Bruto acima de 2500 - desconto de 20%"


valor_hora = float(input('informe o valor da hora: '))
qntd_hora = float(input('informe as horas trabalhadas: '))

print()
salario_bruto = valor_hora * qntd_hora 
print('salario bruto: (',valor_hora, '*',qntd_hora,'): R$',  salario_bruto,sep='') 

if salario_bruto <= 900:
  taxa = 0
elif salario_bruto <= 1500:
  taxa = 5
elif salario_bruto <= 2500:
  taxa = 10 
else: 
  taxa = 20 

ir =  (salario_bruto * taxa) / 100
print('(-) IR (',taxa,'%): R$',ir,sep='')
sindicato = salario_bruto * 0.03 
print('(-) Sindicato (3%): R$',sindicato,sep='') 
fgts = salario_bruto * 0.11
print('FGTS (11%): R$',fgts,sep='') 
total_des = ir + sindicato 
print('Total de descontos: R$',total_des,sep='')
salario_l = salario_bruto - total_des 
print('Salario líquedo: R$',salario_l,sep='')
