#Crie um programa que leia varios números inteiros. no final da excecução mostre a media de
#todos os valores e qual foi o maior e menor numero digitado
#o programa deve perguntar se ele quer continuar digitando ou não

v=('s')
n=int(input('Insira um número:'))
c=1
m=n
a=n
b=n
while v != 'N':
    v=input('Deseja continuar S/N? ').upper()

    if v == 'S':
        n=int(input('Insira um número:'))
        m+=n
        c+=1

        if a < n:
            a=n

        elif b > n:
            b=n

    elif v == 'N':
        print('')

    else:
        print('Opção invalida.')

m=m/c

print('A média dos valores {} digitados é {}, o maior valor foi {} e o menor valor foi {}'.format(c,m,a,b))
