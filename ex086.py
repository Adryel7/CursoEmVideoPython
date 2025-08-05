#Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.

m= list()
j=l=0

for i in range(0,9):
    m.append(int(input(f'Insira o valor da posição [{j}][{l}]: ')))
    l+=1
    if l==3:
        l=0
        j+=1

print('='*60)
for i in range (0,9):
    print(f'[{m[i]:^7}]', end='')
    if i == 2 or i == 5:
        print()



