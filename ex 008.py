# Escreva um programa que leia um valor em metros e converta para centrimetros e milimetros.

m=float(input('Insira o valor a ser convertido(em metros): '))
c=m*100
mm=m*1000

print('{} metros é igual a {} centrimetros e {} milimetros' .format(m,c,mm))
