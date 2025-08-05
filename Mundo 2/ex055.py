#Mostre um programa que leia o peso de 5 pessoas e mostre o maior e o menor pesos lidos
a=0
b=0
for c in range(0,5):
    p=float(input('Insira o peso da {}ª pessoa:'.format(c+1)))
    
    if c == 1:
        a=p
        b=p
        
    elif p > a:
        a=p
        
    elif p < b:
        b=p

print('O maior peso lido foi {:.1f} e o menor foi {:.1f}'.format(a,b))
