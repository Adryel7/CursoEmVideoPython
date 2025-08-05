#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
#cadastrando tudo em uma lista composta.
from random import sample
cartela= []
quant=int(input('Insira a quantidade de jogos que deseja gerar: '))

for i in range (0,quant):
    cartela.append(sample(range(1,61),6))

print('='*60)
print('Os jogos gerados foram:')

for i in range(0,quant):
    print(f'Jogo {i+1}:{sorted(cartela[i])}')
