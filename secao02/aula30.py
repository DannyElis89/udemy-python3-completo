"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

number = input('Por favor, digite um número inteiro: ')

if not (number.isnumeric()):
    print('O valor inserido não é um número.')
elif '.' in number:
    print('O número digitado não é um número inteiro.')
elif int(number) % 2 == 0 and number.isnumeric():
    print('O número digitado é par.')
else:
    print('O número digitado é ímpar.')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada.
"""
hora = input('Por favor, insira a hora atual: ')

if not (hora.isnumeric()):
    print('O valor inserido não é um número.')
elif 0 <= int(hora) <= 11:
    print('Bom dia!')
elif 12 <= int(hora) <= 17:
    print('Boa tarde!')
elif 18 <= int(hora) <= 23:
    print('Boa Noite!')
else:
    print('O valor inserido é inválido.')

"""
Faça um programa que peça o primeiro nome do usuário:
    Se o nome tiver até 4 letras, escreva 'Seu nome é curto';
    Se Tiver entre 5 e 6 letras, escreva: 'Seu nome é normal';
    Se tiver mais que 6 letras, escreva: 'Seu nome é muito grande';
"""

nome = input('Por favor, insira seu primeiro nome: ')
letras = len(nome)

if letras <= 4:
    print('Seu nome é curto')
elif 5 <= letras <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')
