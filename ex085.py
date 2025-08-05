#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
#em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
v = list()
a = p = b = 0

for i in range(0,7):
    aux=int(input(f'Insira o {i+1}º valor: '))
    if aux % 2 == 0:
        v.insert(0,aux)

    else:
        if len(v)==1:
            v.append(aux)

        else:
            v.insert(-1,aux)

for i in v:
    if i % 2 != 0:
        a=i
        b+=1
        break
p=v.index(a)
if a == 0:
    print('='*120)
    print(f'Os valores digitados foram: {v}')
    print(f'Você não digitou valores impares')
    print(f'Os valores pares em ordem crescente são: {sorted(v[:p])}')
elif b == 1:
    print('='*60)
    print(f'Os valores digitados fora: {v}')
    print(f'Os valores impares em ordem crescente são: {sorted(v[p:])}')
    print(f'Você não digitou valores pares.')
else:
    print('='*60)
    print(f'Os valores digitados fora: {v}')
    print(f'Os valores impares em ordem crescente são: {sorted(v[p:])}')
    print(f'Os valores pares em ordem crescente são: {sorted(v[:p])}')

'''solução proposta
v=[[], []]
for i in range(0,7)
    aux=int(input('Insira um número: '))
    if aux % 2 == 0:
        v[0].append(aux)'''
