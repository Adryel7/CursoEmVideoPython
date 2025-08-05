#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas= list()
dados= list()

dados.append(str(input('Insira o nome: ')))
dados.append(float(input('Insira o peso: ')))
pessoas.append(dados[:])
dados.clear()
while (True):
    op=str(input('Deseja continuar?S/N '))
    if op in 'Nn':
        break
    elif op in 'Ss':
        dados.append(str(input('Insira o nome: ')))
        dados.append(float(input('Insira o peso: ')))
        pessoas.append(dados[:])
        dados.clear()

    else:
        print('Comando invalido.')

for c in range (0,len(pessoas)):
    if c==0:
        max = min = pessoas[0][1]
    elif max < pessoas[c][1]:
        max=pessoas[c][1]
    elif min > pessoas[c][1]:
        min=pessoas[c][1]

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas são: ',end='')
for c in range (0,len(pessoas)):
    if pessoas[c][1]==max:
        print(pessoas[c][0],end=' ')

print('\nAs pessoas mais leves são:',end=' ')
for c in range (0,len(pessoas)):
    if pessoas[c][1]==min:
        print(pessoas[c][0],end=' ')

