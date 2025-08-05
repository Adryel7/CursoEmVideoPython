#Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas dos pares
s=0
for c in range (0,6):
    n=int(input('Insira o {} número: ' .format(c+1)))
    if n % 2 == 0:
        s=s+n

print('soma= {}'.format(s))
