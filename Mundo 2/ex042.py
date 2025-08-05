#faça o desafio 35 dos triangulos, acrescentando o tipo de triangulo que será formado
#Equilatero(todos os lados iguais)
#isóceles(dois lados iguais)
#Escaleno(todos os lados diferentes)
#35 - desenvolva um programa que leia o comprimento de 3 retas e diga se elas podem formar um triangulo

a=float(input('Insira o comprimento da primeira reta: '))
b=float(input('Insira o comprimento da segunta reta: '))
c=float(input('Insira o comprimento da terceira reta: '))

if a + b > c and b + c > a and c + a > b:
    if a == b and b == c:
        print('\nAs retas formam um triangulo Equilatero.')

    elif a == b or b == c or a == c:
        print('\nAs retas formam um triangulo Isóceles.')

    elif a != b and a != c and b != c:
        print('\nAs retas formam um triangulo Escaleno.')
else:
    print('\nAs retas não podem formar um triangulo.')
