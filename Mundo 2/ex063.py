#Escreva um programa que leia um numero 'n' inteiro e qualquer e mostre na tela os 'n' primeiros
#termos de uma sequencia de Fibonacci

print('-=-'*20,end='')
print('Sequencia de Fibonacci.',end='')
print('-=-'*20)

n=int(input('\nInsira a quantidade de termos que deseja mostrar: '))
c=n
f=0
g=0
while c > 0:
    print(f,end=' ')
    if f == 0:
        f=1
    else:
        f=g+f
        g=f-g

    c-=1
