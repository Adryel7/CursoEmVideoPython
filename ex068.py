#Faça um programa que jogue par ou impar com computador. O jogo será interrompido quando
#o jogador perder, mostrando o total de vitorias conquistadas pelo usuario

from random import randint
from time import sleep

print('-'*30,end='')
print('Par ou impar.',end='')
print('-'*30)
v=0
while True:
    c=randint(0,10)
    n=int(input('\nInsira um número: '))
    u=input('Você escolhe par ou impar(P/I)? ').upper()
    s=c+n

    if u == 'P':

        if s % 2 == 0:
            print(f'O computador escolheu {c} e você escolher {n}. {c} + {n} = {s} PAR')
            print('Parabens, você ganhou!')
            v+=1
        else:
            print(f'O computador escolheu {c} e você escolher {n}. {c} + {n} = {s} IMPAR')
            if v == 0:
                print(f'GAME OVER! Você não teve vitorias.')
                break
            elif v == 1:
                print(f'GAME OVER! Você teve {v} vitória')
                break
            else:
                print(f'GAME OVER! Você teve {v} vitórias')
                break

    elif u == 'I':
        if s % 2 != 0:
            print(f'O computador escolheu {c} e você escolher {n}. {c} + {n} = {s} IMPAR')
            print('Parabens, você ganhou!')
            v+=1
        else:
            print(f'O computador escolheu {c} e você escolher {n}. {c} + {n} = {s} PAR')
            if v == 0:
                print(f'GAME OVER! Você não teve vitorias.')
                break
            elif v == 1:
                print(f'GAME OVER! Você teve {v} vitória')
                break
            else:
                print(f'GAME OVER! Você teve {v} vitórias')
                break
    else:
        u=input('Você escolhe par ou impar(P/I)?').upper()
