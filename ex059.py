#Crie um programa que leia dois valores e mostre um menu na tela
'''
1 - soma
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa
'''
op=0
n1=int(input('Insria um numero: '))
n2=int(input('Insria outro numero: '))

while op != 5:
    print('''O que deseja fazer com esses números?
    1 - Somar
    2 - Multiplicar
    3 - Saber qual é o maior
    4 - Digitar novos números
    5 - Sair do programa''')
    op=int((input('')))

    if op == 1:
        s=n1+n2
        print('\nA soma dos números digitados é {}'.format(s))
        print('\n')

    elif op == 2:
        m=n1*n2
        print('\nO produto dos números digitados é {}'.format(m))
        print('\n')

    elif op == 3:
        if n1 > n2:
            print('\nO número {} é maior que {}'.format(n1,n2))
            print('\n')
        elif n2 > n1:
            print('\nO número {} é maior que {}'.format(n2,n1))
            print('\n')
        else:
            print('\nOs números são iguais.')
            print('\n')

    elif op == 4:
        n1=int(input('Insria um numero: '))
        n2=int(input('Insria outro numero: '))
