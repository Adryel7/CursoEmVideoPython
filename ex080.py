#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

v=[]

for c in range(0,5):
    n=int(input(f'Insira o {c+1}º valor: '))
    if c == 0 or n>v[-1]:
        v.append(n)
    else:
        for d in range(0,len(v)):
            if v[d] >= n:
                v.insert(d,n)
                break

print(v)
