#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
#listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
#respectivamente. Ao final, mostre o conteúdo das três listas geradas.

l=[]
p=[]
i=[]
aux=int(input('Insira um valor: '))
l.append(aux)

while(True):
    op=input('Deseja continuar? S/N ')
    if op in 'Nn':
        break
    elif op in 'Ss':
        aux=int(input('Insira um valor: '))
        l.append(aux)
    else:
        print('Comando invalido.')
for c in l:
    if c % 2 ==0:
        p.append(c)
    else:
        i.append(c)

print(l)
print(p)
print(i)
