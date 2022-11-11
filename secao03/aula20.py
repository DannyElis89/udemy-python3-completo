"""
Introdução a formatação de str

"""

nome = 'Danny Elis'
idade = 33
altura = 1.65
e_maior = idade > 18
peso = 70
imc = peso / altura ** 2

print('nome:', nome, type(nome))
print('idade:', idade, type(idade))
print('altura:', altura, type(altura))
print('e_maior:', e_maior, type(e_maior))
print('imc:', imc, type(imc))

print(nome, 'tem', idade, 'anos e seu imc é', imc)

print(f'{nome} tem {idade} anos e seu imc é {imc:.2f}')
print('{} tem {} anos e seu imc é {:.2f}'.format(nome, idade, imc))
print('{name} tem {age} anos e seu imc é {imC:.2f}'.format(name=nome, age=idade, imC=imc))
print('{1} tem {0} anos e seu imc é {2:.2f}'.format(idade, nome, imc))
