#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso,
#de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

num=('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
   'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:

    n=int(input('Insira um número entre 0 e 20: '))

    if n >= 0 and n<=20:
        print(f'Você inseriu o número {num[n]}')
        cont=input('\nDeseja continuar (S/N)? ').upper()

        if cont == 'N':
            break


