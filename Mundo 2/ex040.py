#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final
#de acordo com a média atingida

#media abaixo de 5 reprovado
#media entre 5 e 6.9 recuperação
#media 7 ou superior Aprovado

print('='*20,end='')
print('Sistema de calculo de medias',end='')
print('='*20)
a=float(input('\nInsira a primeira nota: '))
b=float(input('\nInsira a segunda nota: '))

m=(a+b)/2

if m < 5:
    print('\n\33[1;31m=',end='')
    print('='*9,end='')
    print('Reprovado',end='')
    print('='*9,end='')
    print('=\33[m')

elif m >= 5 and m<= 6.9:
    print('\n\33[7m=',end='')
    print('='*9,end='')
    print('Recuperação',end='')
    print('='*9,end='')
    print('=\33[m')

else:
    print('\n\33[1;34m=',end='')
    print('='*9,end='')
    print('Aprovado',end='')
    print('='*9,end='')
    print('=\33[m')
