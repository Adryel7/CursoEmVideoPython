#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
l=[]

for c in range(0,10):
    l.append(int(input('Insira um número:')))

    if c == 0:
        e=l[c]
        a=l[c]

    else:
        if l[c] > a:
            a=l[c]
        elif l[c] < e:
            e=l[c]

print(f'O maior valor digitado foi {a} nas posições ', end='')
for i, v in enumerate(l):
    if v == a:
        print(i,end='...')
print()

print(f'O menor valor digitado foi {e} nas posições ', end='')
for i, v in enumerate(l):
    if v == e:
        print(i,end='...')
