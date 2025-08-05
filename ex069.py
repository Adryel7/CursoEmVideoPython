#crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada o
#programa deve perguntar se o usuario quer continuar ou não ao final do programa deve mostrar:
#quantas pessoas tem mais de 18 anos quantos homens e quantas mulheres com menos de 20 anos
mais_18=0
h=0
m_menos_20=0
while True:
    n=input('Insira o nome: ')
    s=input('Insira o sexo(F/M): ').upper()
    i=int(input('Insira a idade: '))

    if i > 18:
        mais_18+=1

    if s == 'M':
        h+=1

    if s == 'F' and i < 20:
        m_menos_20+=1

    c=input('Deseja continuar(S/N?) ').upper()

    if c == 'N':
        break
    elif c != 'S':
        c=input('Deseja continuar(S/N?) ').upper()

print(f'Foram cadastradas {mais_18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {h} homens.')
print(f'Foram cadastradas {m_menos_20} mulheres com menos de 20 anos.')
