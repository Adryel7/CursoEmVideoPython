#Faça um programa que faça o computador jogar JoKenPô com você.

from random import randint
from time import sleep

print('\33[7;37m-_'*20, end='')
print('-',end='')
print('\33[7;31mJo\33[7;33mKen\33[7;34mPô\33[7;37m', end='')
print('-_'*20, end='')
print('-\33[m')

print('\nVamos jogar o famoso jogo \33[7;31mJo\33[7;33mKen\33[7;34mPô\33[m. Ou \33[7;31mPedra\33[m, \33[7;33mPapel\33[m e \33[7;34mTesoura\33[m.')

c=randint(1,3)

u=int(input('''\nEscolha a opção:
1 - \33[7;31mPedra\33[m
2 - \33[7;33mPapel\33[m
3 - \33[7;34mTesoura\33[m
'''))

print('\33[7;31mJo',end='')
sleep(1)
print('\33[7;33mKen',end='')
sleep(1)
print('\33[7;34mPô\33[m')
sleep(0.3)

if c == 1:
    if u == 1:
        print('Computador: \33[7;31mPedra\33[m')
        print('Usuario: \33[7;31mPedra\33[m')
        print('\33[1;37mJogo empatado.\33[m')
    if u == 2:
        print('Computador: \33[7;31mPedra\33[m')
        print('Usuario: \33[7;33mPapel\33[m')
        print('\33[1;34mParabens, você ganhou!\33[m')
    if u == 3:
        print('Computador: \33[7;31mPedra\33[m')
        print('Usuario: \33[7;34mTesoura\33[m')
        print('\33[1;31mVocê perdeu, mais sorte na proxima.\33[m')

elif c==2:
    if u == 1:
        print('Computador: \33[7;33mPapel\33[m')
        print('Usuario: \33[7;31mPedra\33[m')
        print('\33[1;31mVocê perdeu, mais sorte na proxima.\33[m')

    if u == 2:
        print('Computador: \33[7;33mPapel\33[m')
        print('Usuario: \33[7;33mPapel\33[m')
        print('\33[1;37mJogo empatado.\33[m')

    if u == 3:
        print('Computador: \33[7;33mPapel\33[m')
        print('Usuario: \33[7;34mTesoura\33[m')
        print('\33[1;34mParabens, você ganhou!\33[m')

elif c == 3:
    if u == 1:
        print('Computador: \33[7;34mTesoura\33[m')
        print('Usuario: \33[7;31mPedra\33[m')
        print('\33[1;34mParabens, você ganhou!\33[m')

    if u == 2:
        print('Computador: \33[7;34mTesoura\33[m')
        print('Usuario: \33[7;33mPapel\33[m')
        print('\33[1;31mVocê perdeu, mais sorte na proxima.\33[m')
    if u == 3:
        print('Computador: \33[7;34mTesoura\33[m')
        print('Usuario: \33[7;34mTesoura\33[m')
        print('\33[1;37mJogo empatado.\33[m')
