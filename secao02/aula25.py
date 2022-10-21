"""
Operadores relacionais em Python
== Igual a
!= Diferente de
> Maior que
>= Maior ou igual a
< Menor que
<= Menor ou igual a
"""

print(f'2 == 2? {2 == 2}')
print(f'2 != 2? {2 != 2}')
print(f'2 < 2? {2 < 2}')
print(f'2 <= 2? {2 <= 2}')
print(f'2 > 2? {2 > 2}')
print(f'2 >= 2? {2 >= 2}')

nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))
idade_inferior = 18
idade_superior = 30

if idade >= idade_inferior | idade <= idade_superior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')
