#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$7,00por cada km acima do limite.

v=int(input('Insira a velocidade do carro: '))

if v > 80:
    m=(v-80)*7
    print('Você foi multado em R${:.2f}'.format(m))
