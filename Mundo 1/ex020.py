#um professor quer sortear a ordem de apresentação para um trabalho com 4 alunos. Faça um programa que leia
#o nome dos launos e imprima a ordem de apresentação

from random import sample

a=input('Escreva o nome do primeiro aluno: ')
b=input('Escreva o nome do segundo aluno: ')
c=input('Escreva o nome do terceiro aluno: ')
d=input('Escreva o nome do quarto aluno: ')

print(sample([a,b,c,d],k=4))
