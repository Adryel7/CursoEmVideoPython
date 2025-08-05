#escreva um programa que leia um salario e calcule o aumento
#Para salarios superiores a 1250 calcula 10% de aumento
#para salarios inferiores calcule 15%

s=float(input('Insira o salario: '))

if s <= 1250:
    a=s*0.15
    print('\nSeu novo salario é \033[7;30mR${:.2f}\033[m'.format(s+a))

else:
    a=s*0.1
    print('Seu novo salario é \033[7;30mR${:.2f}\033[m'.format(s+a))

