d=int(input('Quantos dias o carro ficou alugado? '))

k=int(input('Quantos quilometros o carro percorreu? '))

v=(d*60)+(k*0.15)

print('O valor a ser pago é R${:.2f}' .format(v))
