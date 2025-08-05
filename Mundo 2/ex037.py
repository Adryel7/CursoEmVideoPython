#escreva um programa que leia um número inteiro qualquer e peça ao usuario escolher a base de conversão

#1 - binario
#2- octal
#3- hexadecimal
print('-=-'*10, end='')
print('Sistema de conversão de números decimais',end='')
print('-=-'*10)
n=int(input(('\nInsira um numero: ')))

c=int(input('''
Insira a conversão que deseja para esse núemro:
1- Binario
2- Octal
3-Hexadecimal
'''))
if c == 1:
    b=format(n,'b')
    print('O numero decimal {} convertido para Binario é: {}' .format(n,b))

elif c == 2:
    o=format(n,'o')
    print('O numero decimal {} convertido para Octal é: {}' .format(n,o))

elif c == 3:
    h=format(n,'X')
    print('O numero decimal {} convertido para Hexadecimal é: {}' .format(n,h))

else:
    print('Opção invalida.')
