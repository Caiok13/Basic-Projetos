 ### CÁLCULO DE MÉDIA FINAL  ###

p1 = int(input('Digite um número:'))
p2 = int(input('Digite um número:'))
p3 = int(input('Digite um número:'))
p4 = int(input('Digite um número:'))

constante = 4
calculo = ((p1+p2+p3+p4)/constante)


def media_final ():
  if calculo >= 5:
    print (f'Sua Média Final é igual a {calculo} e você está APROVADO')
  else:
    print(f' Sua Média Final é igual a {calculo} e você está REPROVADO')
  
  
media_final()

ll


