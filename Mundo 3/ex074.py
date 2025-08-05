#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique
#o menor e o maior valor que estão na tupla.

from random import randint

t=(randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f'Os numeros gerados foram:{t}')
print(f'O maior número gerado foi: {sorted(t)[4]}')
print(f'O menor número gerado foi: {sorted(t)[0]}')

print(f'\nO maior número gerado foi: {max(t)}')
print(f'O menor número gerado foi: {min(t)}')
