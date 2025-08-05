#escreva um programa que leia dois números inteiros e compare-os mostrando a seguinte mensagem:
#O primeiro valor é maior
#o segundo valor é maior
# não existe valor maior, os dois são iguais
print('\033[1;31;40m-=-'*10, end='')
print('Sistema comparador de números', end='')
print('-=-'*10,'\033[m')
a=float(input('\n\033[34mInsira o primeiro valor: '))
b=float(input('Insira o segundo valor valor: '))

if a > b:
    print('O \033[4mPRIMEIRO\033[0;34m valor é maior que o segundo.\033[m')
elif a < b:
    print('O \033[4mSEGUNDO\033[0;34m valor é maior que o primeiro.\033[m')
else:
    print('\033[4mOs valores são iguais.')
