#refaça o exercicio do desafio 9 mostrando a tabuada de um número que o usuario escolher
#ultilizando o for

n=int(input('Insira o número para gerar a tabuada: '))

for c in range (1,11):
    print('{} x {} = {}'.format(n, c,c*n))
