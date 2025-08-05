#Crie um programa que leia varios numeros inteiros pelo teclado. O programa para quando o usuario
#digitar 9999. no final mostre quantos números foram digitados e qual foi a soma deles(desconsiderando o 9999)
s=0
n=0
c=0
print('-=-'*15,end='')
print('Somador de números',end='')
print('-=-')
print('\nInsira números inteiros para serem somados, digite 9999 para sair.')

while n != 9999:

    if c == 0:
        n=int(input('Insira um número: '))
    else:
        n=int(input('Insira outro número: '))

    if n != 9999:
        c+=1
        s=s+n

if c == 1:
    print('Apenas um número foi digitado')
else:
    print('A soma dos {} números digitados é {}.'.format(c,s))
