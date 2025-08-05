

nome=input('Escreva seu nome: ')

print(nome.upper())
print(nome.lower())
a=(len(nome))
e=(nome.count(' '))
print('O nome {}, possui {} caracteres'.format(nome, a-e))
d=nome.split()
print('O primeiro nome é {} possui {} caracteres'.format(d[0], len(d[0])))
