#Crie um programa que leia varios números inteiros, o programa para quando digitar 9999
#no final mostre quantos números foram digitados e qual a soma entre eles (desconsiderando o flag).
c=0
s=0
while True:
    n=int(input('Insira um número(9999 para sair): '))

    if n != 9999:
        s+=n
        c+=1
    else:
        break

print(f'Você digitou {c} números, a soma entre eles é {s}')
