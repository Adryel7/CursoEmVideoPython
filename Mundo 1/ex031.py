#desenvolva um programa que leia a distancia de uma viagem em km.
#Calcule o preço da passagem, cobrando 0,50 po km para viagens até 200 km
#Para viagens acima de 200 cobra 0,45

d=float(input('Insira a distancia da viagem(em km): '))

if d <= 200:
    p=d*0.5
    print('Sua passagem custa R${:.2f}'.format(p))

else:
    p=d*0.45
    print('Sua passagem custa R${:.2f}'.format(p))
