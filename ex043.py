#desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC de acordo com a tabela:
#abaixo de 18.5: abaixo do peso
#entre 18.5 e 25 peso ideal
#25 a 30: sobrepeso
#30 a 40: obesidade
#Acida de 40: Obesidade morbida

p=float(input('Insira seu peso: '))
a=float(input('Insira sua altura: '))

I=p/pow(a,2)

if I < 18.5:
    print('\nSeu IMC atual é de: {:.1f}'.format(I))
    print('Você está abaixo do peso ideal.')

elif I >= 18.5 and I < 25:
    print('\nSeu IMC atual é de: {:.1f}'.format(I))
    print('Você está dentro do peso ideal.')

elif I >= 25 and I < 30:
    print('\nSeu IMC atual é de: {:.1f}'.format(I))
    print('Você está com sobrepeso.')

elif I >= 30 and I < 40:
    print('\nSeu IMC atual é de: {:.1f}'.format(I))
    print('Você está com obesidade.')

elif I > 40:
    print('\nSeu IMC atual é de: {:.1f}'.format(I))
    print('Você está com obesidade morbida.\nProcure um especialista!')
