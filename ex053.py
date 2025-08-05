#Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços
#Apos a sopa, a sacada da casa, a torre da detrrota, o lobo ama o bolo, anotaram a placa da maratona

f=(input('Insira a frase: '))
f=f.lower().split()
f=''.join(f)

if str(f) == str(f)[::-1]:
    print('Palindromo')

else:
    print('Não é um palindromo')
