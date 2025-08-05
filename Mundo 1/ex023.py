#Faça um programa que leia um número de 0 a 9999 e mostre seus digitos separados na tela como
#milhar, centena, dezena e unidade.
n=int(input('Escreva um número entre 0 e 9999: '))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print('Unidade: {}' .format(u))
print('Dezena: {}' .format(d))
print('Centena: {}' .format(c))
print('Milhar: {}' .format(m))
