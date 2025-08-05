#Escreva um programa paara aprovar um emprestimo para a compra de uma casa
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele pretende pagar a casa
#Calcule o valor da prestação mensal, sabendo que a parcela não pode exceder 30% do valor do salario ou será negado

print('='*10, end='')
print('Emprestimo para compra de imovel.', end='')
print('='*10)

vc=float(input('\nInsira o valor do imovel pretendido: '))
s=float(input('Insira o valor do seu salario liquido: '))
pa=float(input('Insira a quantidade de anos que você pretende pagar o imovel: '))
vm=s*0.3
pm=pa*12
m=vc/pm

if vm >= m:
    print('\nParabens! Seu emprestimo foi aprovado!')
    print('O valor mensal a ser pago é de R${:.2f}'.format(m))

else:
     print('Seu emprestimo foi NEGADO!')
