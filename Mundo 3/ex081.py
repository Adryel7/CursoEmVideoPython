#Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
v=[]
v.append(int(input('Insira um valor:')))
while(True):
    op=input('Deseja Continuar? S/N ')
    if op in'Nn':
        break
    if op in 'Ss':
        v.append(int(input('Insira um valor:')))
    else:
        print('Comando invalido')
print()
print('-=-'*30)

print(f'\nVocê digitou {len(v)} valores.')
v.sort(reverse=True)
print(v)
if 5 in v:
    print('O número 5 está na lista.')
else:
    print('O número 5 não aparece na lista.')
