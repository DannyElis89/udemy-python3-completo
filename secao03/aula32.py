"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUM) - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QTDD)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num1 = 26
num2 = 2
num3 = 13
divisao = num1 / num2

print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome = 'Danny Elis'
idade = 33
print(f'{nome:s}')
print('Seu nome é %s e sua idade é %d anos' % (nome, idade))

print(f'{num1:0>10}')
print(f'{num2:0>10}')
print(f'{num3:0^10}')
print(f'{num3:0>10.2f}')

print(f'{nome:#^50}')

nome_formatado = '{:*>30}'.format(nome)
print(nome_formatado)
