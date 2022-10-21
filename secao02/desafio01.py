"""
Desafio 01:
Criar variáveis para nome (str), idade (int), altura (float) e peso (float).
Criar variável com o ano atual (int)
Obter o ano de nascimento (int) com base na idade e ano atual
Obter o imc da pessoa com duas casas decimais (float) com base no peso e altura da pessoa
Exibir um texto com todos os valores na tela usando f-trings (com as chaves)
"""

nome = 'Maria da Silva'
idade = 42
peso = 70.3
altura = 1.8
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print('{} tem {} anos, pesa {:.3f} Kg e tem {:.2f} m de altura. '
      'Nasceu em {} e seu imc é {:.2f}'
      .format(nome, idade, peso, altura, ano_nascimento, imc))

print(f'{nome} tem {idade} anos, pesa {peso:.3f} Kg e tem {altura:.2f} m de altura. '
      f'Nasceu em {ano_nascimento} '
      f'e seu imc é {imc:.2f}')

