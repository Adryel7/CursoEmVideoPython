#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e
#fechados na ordem correta.

e=str(input('Insira uma expressão usando parenteses: '))
while e.count('(') >= 1:
    if  e.count('(') == e.count(')'):
        if e.index('(') < e.index(')'):
            e=e.replace(e[e.index('(')],'',1)
            e=e.replace(e[e.index(')')],'',1)
        else:
            break
    else:
        break

if e.count('(') == 0 and e.count(')')==0:
    print('Expressão valida.')
else:
    print('Expressão não válida.')
