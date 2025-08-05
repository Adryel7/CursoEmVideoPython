#desenvolva um programa que leia nome, idade e sexo de 4 pessoas, no final o programa deve mostrar
#A media de idade do grupo, qual o nome do homem mais velho e quantas mulheres tem menos de 20 anos.
m=0
hm=0
im=0
v=0
for c in range (0,4):
    n=input('Insira o nome da {}ª pessoa: '.format(c+1))
    i=int(input('Insira a idade da {}ª pessoa: '.format(c+1)))
    s=input('Insira o sexo da {}ª pessoa(F ou M): '.format(c+1)).upper()

    m=m+i
    if hm == 0 and s == 'M':
        hm=n
        im=i

    elif s == 'F' and i<20:
        v=v+1

    elif s == 'M' and im < i:
        hm=n

m=m/4
print('A media da idade do grupo é {}'.format(m))
print('O nome do homem mais velho do grupo é {}'.format(hm))
print('No grupo existem {} mulheres com menos de 20 anos.'.format(v))
