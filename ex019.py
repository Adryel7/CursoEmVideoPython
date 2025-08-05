#um professor que sortear um dos seus 4 alunos para apagar o quadro. escreva um programa que auxilie ele,
#escrevedno na tela o nome do escolhido.

from random import choice

a=input('Escreva o nome do primeiro aluno: ')
b=input('Escreva o nome do segundo aluno: ')
c=input('Escreva o nome do terceiro aluno: ')
d=input('Escreva o nome do quarto aluno: ')

print(choice([a,b,c,d]))


