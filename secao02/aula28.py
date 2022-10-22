"""
Documentação e funções built-in úteis
Funções de checagem de tipos numéricos:
    isnumeric: somente números inteiros e positivos
    isdigit
    isdecimal
"""

num2 = input('Digite outro número: ')
num1 = input('Digite um número: ')

if num1.isnumeric() and num2.isnumeric():
    num1 = int(num1)
    num2 = int(num2)
    print(f'{num1} + {num2} = {num1 + num2}')
