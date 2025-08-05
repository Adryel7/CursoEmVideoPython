# Crie um programa que converta reais em dolares(considere U$1,00=R$ 5,64)

r=float(input('Insira o valor em reais:'))
d=r/5.6358

print('R${:.2f} equivale a U${:.2f}'.format(r,d))
