#Faça um programa que leia um número qualquer e mostre seu fatorial
#ex. 5! = 5x4x3x2x1=120

print('-=-'*15, end='')
print('Calculadora de fatorial', end='')
print('-=-'*15)

n=int(input('\nInsira um número para saber seu fatorial: '))
c=n-1
print(' {}! = '.format(n),end='')
while c > 0:
    n=n*(c)

    if c != 0:
        print('{} x'.format(c+1),end=' ')
    c-=1

print('1 = {}'.format(n))
