"""
Entrada de dados do usuário
"""

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))

print(f'O usuário {nome} tem {idade} anos de idade.')
print(type(idade))

# Calculadora
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {(num1 / num2):.2f}')
