#crie um programa que mostre todos os numeros pares no intervalo entre 1 e 50.

i=int(input('Insira o número inicial: '))
f=int(input('Insira o número final: '))
for c in range(i,f+1):
    if c % 2 == 0:
        print(c)
