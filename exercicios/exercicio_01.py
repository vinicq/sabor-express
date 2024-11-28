#1 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura.\n')
print('--------------------------------------------------------')

#2 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.

nome = input(str('Diite seu nome: '))
idade = input('Digite sua Idade: ')
# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')
# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')
# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))
# Abordagem da % (Formatação de String Antiga - Python 2)
idade = int(idade)
print('Meu nome é %s e tenho %i anos.' % (nome,idade))
print('--------------------------------------------------------')

#3 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
print('A','L','U','R','A',sep='\n\n')
print('--------------------------------------------------------')

for letra in 'ALURA':
    print(letra)
    
print('--------------------------------------------------------')
    
# 4 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. 

pi = 3.1415926

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')
# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))
# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))

