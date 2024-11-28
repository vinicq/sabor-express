# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

import os

numero = int(input('Digite um numero: '))

# if numero == 0:
#     print('O numero digitado eh par')
# else:
#     if numero % 2 == 0:
#         print('O numero digitado eh par')
#     else:
#         print('O numero digitado eh impar')

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
        
        
"""
3 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
""" 

os.system('cls')

idade = int(input('Digite sua idade: '))

if idade < 13:
    print('Voce eh crianca')
elif idade < 19:
    print('Voce eh adolescente')
else:
    print('Voce eh adulto')
    
"""
4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""


coordenada_x = float(input('Digite a coordenada x: '))
coordenada_y = float(input('Digite a coordenada y: '))

if coordenada_x > 0 and coordenada_y > 0:
    print('O ponto se encontra no primeiro quadrante')
elif coordenada_x < 0 and coordenada_y > 0:
    print('O ponto se encontra no segundo quadrante')    
elif coordenada_x < 0 and coordenada_y < 0:
    print('O ponto se encontra no terceiro quadrante')
elif coordenada_x > 0 and coordenada_y < 0:
    print('O ponto se encontra no quarto quadrante')
else:
    print('O ponto se encontra no eixo ou origem')
    
# 5 - fazer uma condicional que poderá verificar os valores de usuário e senha

usuario_correto = "teste"
senha_correta = "teste123"

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")