import os

os.system('clear')

print('Bem Vindo ao nosso sistema de notas escolares')

qtqNT = int(input('Digite a quantidade de notas que o aluno teve: '))
entrada = input('Digite o nome do aluno responsável pelas notas a seguir: ')

notas = []  # lista para armazenar as notas

for i in range(qtqNT):
    nota = float(input(f'Digite a nota {i+1}: '))
    notas.append(nota)  # adiciona cada nota na lista

# Calcula a média das notas
calculo = sum(notas) / qtqNT

print(f'\nAluno: {entrada}')
print(f'Média das notas: {calculo:.2f}')