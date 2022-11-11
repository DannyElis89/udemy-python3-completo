# Comando print()
print('Hello World!', 123456, 'Danny Elis Simioni')  # Saída: Hello World! 123456 Danny Elis Simioni
print('Danny', 'Elis', 'Simioni', sep='-')  # Saída: Danny-Elis-Simioni

print('Danny', 'Elis', sep='-', end='')
print('Simioni', sep='-')  # Saída: Danny-ElisSimioni

"""
imprimir CPF fictício com formatação usando parametros da função print
"""
print('Resolução 01', end=': ')
print('123', end='.')
print('456', end='.')
print('789', end='-')
print('00')

print('Resolução 02', end=': ')
print('123', '456', '789', sep='.', end='-')
print('00')
