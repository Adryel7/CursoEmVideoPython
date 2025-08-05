# Faça um algoritmo que leia um preço e mostre o novo preço com  5% de desconto.
p=float(input('Insira o valor:'))
d=p-(p*0.05)
print('O valor com desconto é R${:.2f}' .format(d))
