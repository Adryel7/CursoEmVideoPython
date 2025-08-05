#Faça um programa que leia um número inteiro e diga se ele é primo ou não

n=int(input('Insira o número: '))

if n == 1:
    print('O número não é primo')

if n == 2:
    print('O número é primo')

for c in range(2,n):

    if n % c == 0:
        print('O número não é primo.')
        break

    if n-1 == c:
        print('O número é primo')
