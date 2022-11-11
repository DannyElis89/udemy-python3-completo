"""
Operadores lógicos + IF/ELIF/ELSE
and (comparação1 E comparação2):
    Se as duas comparações forem verdadeiras, retorna True;
    Se as duas ou uma das comparações forem falsas, retorna False;

or (comparação1 OU comparação2):
    Se pelo menos uma das comparações forem verdadeiras, retorna True;
    Se as duas comparações forem falsas, retorna False;

not (nega o resultado de uma comparação):
    3 > 2 = True
    3 < 2 = False
    if not 3 < 2 = True

in (Verifica a existência de algum caracter dentro de uma string ou
    de um valor dentro de uma lista/conjunto)

not in (Verifica a inexistência de algum caracter dentro de uma string ou
    de um valor dentro de uma lista/conjunto)

"""

a = 2
b = 2
c = 3

print(f'(a == b) = {a == b}')
print(f'(a != b) = {a != b}')

print(f'(b < c) = {b < c}')
print(f'(b > c) = {b > c}')

print(f'(a == b) and (b < c) = {a == b and b < c}')
print(f'(a == b) and (b > c) = {a == b and b > c}')
print(f'(a != b) and (b > c) = {a != b and b > c}')

print(f'(a == b) or (b < c) = {a == b or b < c}')
print(f'(a == b) or (b > c) = {a == b or b > c}')
print(f'(a != b) or (b > c) = {a != b or b > c}')

name = ''
if not name:
    print('Por favor, preencha o seu nome abaixo:')
    name = input('Nome completo: ')

if 'y' in name:
    print('Possui a letra y')
else:
    print('Não possui a letra y')

if 'r' not in name:
    print('O nome não possui a letra r')
else:
    print('O nome possui a letra r')

print(name)

usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'danny'
senha_db = '123456'

if usuario == usuario_bd and senha == senha_db:
    print('Login efetuado com sucesso')
else:
    print('Usuário e/ou senha incorretos')
