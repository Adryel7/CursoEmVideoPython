# Escreva um programa que faça o computador escolher um número aleatório entre 0 5 e peça para o
# usuario tentar acertar. O programa deve avisar se o usuario acertou ou errou.
import random

n = random.randint(0, 5)

nu = int(input('Tente acertar o número escolido pela maquina(entre 0 e 5): '))

if n == nu:
    print('Parabéns! Você Acertou!')
else:
    print('Mais sorte na próxima.')
