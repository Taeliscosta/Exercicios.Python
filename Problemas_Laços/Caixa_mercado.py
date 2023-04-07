"Caixa de mercado ou loja, Nesse codigo o usuario decide quando para. creditos do exercicio: Curso em Video(Guanabara)"

def clear():
  print('/n' * 40)

while True:
  print('_ _ _ _ _Lojas Tabajara_ _ _ _ _')
  n = 1
  total = 0
  while True:
    preco = float(input('Produto {}: R$ '.format(n)))
    total += preco
    n += 1
    if preco == 0:
      break 

  print('_ _ _ _ _ _ _ _ _ _ ')

  print('Total: R$',total)
  dinheiro = float(input('Digite o valor do troco: '))
  troco = dinheiro - total
  print('Dinheiro: R$',dinheiro)
  print('Troco: R${:.2f}'.format(troco))
  
  print('_ _ _ _ _ _ _ _ _ _')

  reset = input('Digite (2) para o programa seguir ou (1) para encerrar: ')
  print('')
  if reset == '2':
    continue
  else:
    print('Programa encerrado')
    break
