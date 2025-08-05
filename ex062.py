#Melhore o desafio 51, perguntando ao usuario se ele quer mostrar mais termos
#o programa encerra quando ele digitar 0

p=int(input('Insira o primeiro termo da P.A.: '))
r=int(input('Insira a razão da P.A.: '))
t=10

while t !=0:
    for c in range (0,t):
        print(p,end=' ')
        p=p+r
    print('''\nDeseja mostrar mais termos?''')
    t=int(input('Digite a quantidade de termos que deseja mostrar(Digite 0 para sair): '))
