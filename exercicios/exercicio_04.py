# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'Rio de Janeiro'}

""""
2 - Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.

"""

print(pessoa)    
pessoa['idade'] = 31
print(pessoa)
pessoa['profissao'] = 'Desenvolvedor'
print(pessoa)
del pessoa['cidade']
print(pessoa)
pessoa['cidade'] = 'Rio de Janeiro'
print(pessoa)

# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

pessoa = {'nome': 'Amanda', 'idade': 19, 'cidade': 'São Luís'}
if 'nome' in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.

frase = 'O rato roeu a roupa do rei de Roma'
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)