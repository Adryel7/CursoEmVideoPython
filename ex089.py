#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
#notas de cada aluno individualmente.

notas = list()
dados = list()
c=0
dados.append(c)
dados.append(str(input('Nome: ')))
dados.append(float(input('Nota 1: ')))
dados.append(float(input('Nota 2: ')))
dados.append((dados[2]+dados[3])/2)
notas.append(dados[:])
dados.clear()

while(True):

    op=str(input('Deseja continuar? S/N '))

    if op in 'Nn':
        break

    elif op in 'Ss':
        c+=1
        dados.append(c)
        dados.append(str(input('Nome: ')))
        dados.append(float(input('Nota 1: ')))
        dados.append(float(input('Nota 2: ')))
        dados.append((dados[2]+dados[3])/2)
        notas.append(dados[:])
        dados.clear()

    else:
        print('Opção invalida.')
print()
print('='*60)
print('Lista de média dos alunos:')
print('='*60)

print(f'Mat   Nome       Média')
for i in range(0,len(notas)):
    print(f'{notas[i][0]:<5}',end=' ')
    print(f'{notas[i][1]:<10}',end=' ')
    print(f'{notas[i][4]:<5}')
while(True):
    print('='*60)
    print('Para exibir as notas individuais digite a "Mat" do aluno.(digite 999 para sair)',end='')
    op=int(input())
    print('='*60)
    if op == 999:
        break
    elif op > len(notas)-1:
        print('Opção invalida.')
    else:
        print(f'Nome      Nota 1   Nota 2')

        for c in range(0,len(notas)):
            if op == notas[c][0]:
                print(f'{notas[c][1]:<10}', end='')
                print(f'{notas[c][2]:<5}', end='')
                print(f'{notas[c][3]:>7}')
