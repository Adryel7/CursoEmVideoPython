#faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
#Se ele ainda vai se alistar ao serviço militar
#Se é hora de ele se alistar
#Se ja passou o tempo do alistamento
#o programa também deve mostrar o tempo que falta ou quanto passou o prazo.

from datetime import date

print('\33[1m-=-'*10,end='')
print('Calculo para informações sobre alistamento militar obrigatório.',end='')
print('-=-\33[m'*10)
i=int(input('\nInsira seu ano de nascimento: '))
h=date.today().year

if i+18 == h:
    print('Esse ano você deve se alistar.')

elif i+18 < h:
    t=h-(i+18)
    if t==1:
        print('Você deveria ter se alistado ano passado.')
    else:
        print('Você deveria ter se alistado a {} anos atras.' .format(t))

elif i+18 > h:
    t=(i+18)-h
    if t == 1:
        print('Você deve se alistar no próximo ano.')
    else:
        print('Você deve se alistar daqui a {} anos.'.format(t))
