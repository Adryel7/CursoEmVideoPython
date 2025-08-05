#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
t=('Massa','Cabana','Alface', 'Girafa', 'Garrafa', 'Frigideira', 'Almofada',
   'Geladeira')

for p in t:
   print(f'\nNa palavra {p} temos as vogais ', end='')
   for letra in p:
      if letra.lower() in 'aeiou':
         print(letra, end=' ')

'''for c in range(0,8):
   aux=t[c].upper().count('A')
   aux=aux+t[c].upper().count('E')
   aux=aux+t[c].upper().count('I')
   aux=aux+t[c].upper().count('O')
   aux=aux+t[c].upper().count('U')
   if c==0:
      a=aux
   elif c==1:
      b=aux
   elif c==2:
      i=aux
   elif c==3:
      d=aux
   elif c==4:
      e=aux
   elif c==5:
      f=aux
   elif c==6:
      g=aux
   elif c==7:
      h=aux

v=(a,b,i,d,e,h,g,h)

for c in range(0,8):
   print(f'A palavra {t[c]} possui {v[c]} vogais.')'''
