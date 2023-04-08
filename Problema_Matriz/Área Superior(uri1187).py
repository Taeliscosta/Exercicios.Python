#Uri 1187
#Lê um caractere maiúsculo que indica uma operação que será realizada em um array M [12][12]. 
#Em seguida, calcule e imprima a soma ou média considerando apenas os números que estão incluídos na área verde desta matriz, conforme mostrado na figura a seguir.
#Entrada
#A primeira linha da entrada contém um único caractere maiúsculo O ('S' ou 'M')
#indicando a operação Soma ou Média (Média em português) a ser realizada com os elementos do array. Siga 144 números duplos da matriz.
#Saída
#Imprima o resultado calculado (soma ou média), com um dígito após a vírgula.


m = []
a = input()

for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x) 
s = 0
cont = 0
inf = 1
sup = 11

for i in range(0,5):
    for j in range(inf,sup):
        s += m[i][j]
        cont += 1
    inf += 1 
    sup -= 1
    
med = s / cont

if a == 'S':
    print('{:.1f}'.format(s))
else:
    print('{:.1f}'.format(s))
