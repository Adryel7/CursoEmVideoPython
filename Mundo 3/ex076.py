#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
#e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando
#os dados em forma tabular.

print('-'*45)
print(f'{"Loja preço melhor Eletronica":^45}')
print('-'*45)
print('')
p=('Monitor', 250.99, 'TV', 1579.99, 'Geladeira', 2599.99, 'Ar-Condicionado', 2799.99,
   'Notebook', 3500, )

for c in range (0,len(p)):

   if c== 0 or c % 2 ==0:
      print(f'{p[c]:.<30}',end='')
#      print(p[c],end='')

#      if len(p[c]) < 30:
#         print('.'*(30-len(p[c])),end='')
#      else:
#         print('')

   else:
      print('R$',end='')
      print('{:>10.2f}'.format(p[c]))
