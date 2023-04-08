"faça uma função que receba três valores: um valor inicial, um valor final e um terceiro valor. "
"A função deve retomar um booleando que indique se o terceiro valor está dentro do intervalo comprendidos pelos valores inicial e final(estes inclusos), ou não."


def valores(pr,seg,ter):
    if pr > seg:
      if pr >= ter and seg <= ter:
        return True
      else:
        return False
    else:
      if seg >= ter and pr <= ter:
        return True
      else:
         return False

pr = int(input())
seg = int(input())
ter = int(input())

print(valores(pr,seg,ter))
