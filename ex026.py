#fAÇA UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece na primeira vez
#Em que posição ela aparece na ultima vez

frase=input('Escreva uma frase: ').strip()
print('''
A letra "A" aparece {} vezes.
Ela aparece pela primeira vez na posição {}
e na ultima vez na opsição {}.'''.format(frase.count('A'), frase.find('A'), frase.rfind('A')))

