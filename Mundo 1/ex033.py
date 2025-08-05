#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor

a=float(input('Insira o primeiro número: '))
b=float(input('Insira o segundo número: '))
c=float(input('Insira o terceiro número: '))

if a > b and a > c:
    print('\nO maior número é {}' .format(a))
else:
    if b > c:
        print('\nO maior número é {}'.format(b))
    else:
        print('\nO maior número é {}'.format(c))

if a < b and a < c:
    print('\nO menor número é {}' .format(a))
else:
    if b < c:
        print('\nO menor número é {}'.format(b))
    else:
        print('\nO menor número é {}'.format(c))
