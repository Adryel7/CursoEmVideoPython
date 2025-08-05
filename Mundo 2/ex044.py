#Elabore um programa que calcule o valor a ser pago por um produto considerando seu preço normal
#e condição de pagamento:

#a vista(dinheiro ou cheque): 10% de desconto
#a vista no cartão:5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

v=float(input('Insira o valor do produto: '))

op=int(input('''
Insira a opção de pagamento:
1 - A vista (dinheiro ou cheque)
2 - A vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão
'''))

if op == 1:
    d=v*0.1
    print('Você vai pagar R${:.2f} pelo produto.'.format(v-d))

elif op==2:
    d=v*0.05
    print('Você vai pagar R${:.2f} pelo produto.'.format(v-d))

elif op==3:
    print('Você vai pagar duas vezes de R${:.2f} pelo produto.'.format(v/2))

elif op==4:
    j=v*0.2
    print('O valor total do seu produto será R${:.2f}.'.format(v+j))
