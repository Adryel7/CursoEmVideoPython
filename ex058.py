#Melhore o jogo do desafio 28 onde o computador escolhe um número entre 0 e 10. Só que agora
#o jogador vai tentar até acertar. mostrando no final quantos palpites foram necessarios.

from random import randint
from time import sleep

print('-=-'*20,end='')
print('Adivinhe o número',end='')
print('-=-'*20)
sleep(1)

print('\n\nVou pensar em um número de 1 a 10, tente adivinhar.')
a = randint(1,10)
sleep(1)
print('.',end='')
sleep(1)
print('.',end='')
sleep(1)
print('.')

print('\nTente adivinhar o número que eu pensei:')
u=int(input())
c=1

while u != a:
    u=int(input('Você errou, tente de novo.\n'))
    c+=1

print('Parabens! Você acertou!')
if c == 1:
    print('Você tentou {} vez'.format(c))
else:
    print('Você tentou {} vezes'.format(c))
