#Exercício Python 079: Crie um programa onde o usuário possa digitar
#vários valores numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
# em ordem crescente.

v=[]
aux=int(input('Insira um valor: '))

while(True):
    if aux in v:
        print('Valor duplicado invalido, não adicionado.')
    else:
        v.append(aux)
        print('Valor adicionado com sucesso.')

    op=input('Deseja inserir mais valores? S/N ')

    if op.upper() == 'N':
        break
    elif op.upper() == 'S':
        aux=int(input('Insira um valor: '))
    else:
        print('Comando invalido')

v.sort()
print(f'\nVocê digitou os valores {v}')
