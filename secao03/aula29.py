"""
Pass eEllipsis como placeholders
"""

valor = True

if valor:
    print('Olá!')
else:
    print('Tchau')

if valor:
    pass
else:
    print('Tchau')

if valor:
    ...
else:
    print('Tchau')
