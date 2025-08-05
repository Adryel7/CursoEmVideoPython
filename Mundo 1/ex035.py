#desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem formar um triangulo

a=float(input('Insira o comprimento da primeira reta: '))
b=float(input('Insira o comprimento da segunta reta: '))
c=float(input('Insira o comprimento da terceira reta: '))

if a + b > c and a + c > b and b + c > a:
    print('\nAs retas \033[1;34mpodem\033[m formar um triangulo.')

else:
    print('\nAs retas \033[1;34mnão\033[m podem formar um triangulo.')
