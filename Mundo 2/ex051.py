#desenvolva um programa que leia o primeiro termo e a razão de uma PA.No final mostre os 10
#primeiros termos dessa progressão

p=int(input('Insira o primeiro termo da P.A.: '))
r=int(input('Insira a razão da P.A.: '))

for c in range(0,10):
    print(p)
    p=p+r
