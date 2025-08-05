#Faça um programa que mostre a tabuada de varios números para cada valor digitado pelo usuario
#o programa para quando digitar um valor negativo

print('-'*30,end='')
print('Calculadora de tabuadas',end='')
print('-'*30)

while True:
    n=int(input('\nInsria um número para ver a tabuada: '))

    if n >= 0:
        for c in range(1,11):
            print(f'{n} x {c} = {n*c}')

        print('-'*20)

    else:
        print('Programa encerrado.')
        break
