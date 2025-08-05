#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

m=[[],[],[]]
s = sc = sl = 0

for i in range(0,3):
    for j in range(0,3):
        m[i].append(int(input(f'Insira o valor da posição [{i}][{j}]: ')))

print('='*60)

for i in range(0,3):
    for j in range(0,3):
        print(f'[{m[i][j]:^7}]', end='')
        if m[i][j] % 2 == 0:
            s+=m[i][j]
        if j == 2:
            sc+=m[i][j]
            print()

print(f'A soma dos valores da matriz é: {s}')
print(f'A soma dos valores da terceira coluna é: {sc}')
print(f'O maior valor da segunda linha é: {max(m[1])}')
