"""
len - quantidade de caracteres
Não funciona em variáveis numéricas (int e float), nem em bool
"""

usuario = input('Nome de usuário: ')
qtd_caracteres_nome = len(usuario)
senha = input('Senha do usuário: ')
qtd_caracteres_senha = len(senha)

usuario_bd = 'danny'
senha_db = '123456'

if qtd_caracteres_nome <= 4 or qtd_caracteres_senha <= 4:
    print('O nome de usuário e a senha devem conter pelo menos 5 caracteres cada')
elif usuario != usuario_bd or senha != senha_db:
    print('Usuário e/ou senha incorretos')
else:
    print('Login efetuado com sucesso')

print(f'usuário: {usuario}, senha: {senha}, ')
print(f'qtd_caracteres_nome: {qtd_caracteres_nome}, ')
print(f'type(qtd_caracteres_nome): {type(qtd_caracteres_nome)} ')
print(f'qtd_caracteres_senha: {qtd_caracteres_senha} ')
print(f'type(qtd_caracteres_nome): {type(qtd_caracteres_nome)}')

