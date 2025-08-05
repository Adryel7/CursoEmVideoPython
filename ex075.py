#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e
#guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares

a=int(input('Insira o primeiro número: '))
b=int(input('Insira o segundo número: '))
c=int(input('Insira o terceiro número: '))
d=int(input('Insira o quarto número: '))

t=(a,b,c,d)

if t.count(9)==0:
    print('O número 9 não aparece.')
elif t.count(9)==1:
    print(f'O número 9 aparece {t.count(9)} vez.')
elif t.count(9)>1:
    print(f'O número 9 aparece {t.count(9)} vezes.')

if t.count(3)!=0:
    print(f'O valor 3 foi digitado pela primeira vez na posição: {t.index(3)}')
else:
    print(f'O valor 3 não foi digitado')

print('Os números pares são: ',end='')
for c in range(0,4):
    if c == 0:
        if t[c] % 2==0:
            print(t[c],end='')
    else:
        if t[c] % 2==0:
            print(', ',end='')
            print(t[c],end='')
print('.')
