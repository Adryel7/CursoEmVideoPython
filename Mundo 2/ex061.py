#Refaça o desafio 51 , lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros
# Termos usando while

p=int(input('Insira o primeiro termo da P.A.: '))
r=int(input('Insira a razão da P.A.: '))
c=0

while c < 10:
    print(p,end=' ')
    p=p+r
    c+=1
