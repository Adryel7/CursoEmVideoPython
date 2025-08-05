#Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte
#ao usuario qual o valor a ser sacado e o programa vai informar quantas cedulas de cada valor serão entregues.
#considere notas de 50, 20, 10, 5 e 1.

v=int(input('Informe o valor a ser sacado: R$'))
c50=v//50
rc50=v%50
c20=rc50//20
rc20=rc50%20
c10=rc20//10
rc10=rc20%10
c5=rc10//5
rc5=rc10%5
c1=rc5//1

if
print(f'Total de {c50} cedulas de R$50,00')
print(f'Total de {c20} cedulas de R$20,00')
print(f'Total de {c10} cedulas de R$10,00')
print(f'Total de {c5} cedulas de R$5,00')
print(f'Total de {c1} cedulas de R$1,00')
