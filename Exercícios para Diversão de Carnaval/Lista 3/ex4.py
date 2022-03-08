"""
Escreva um programa para encontrar o tamanho do comprimento das strings nos valores de dicionário. Exemplo: dada o dicionário
>>> {1: “vermelho”, 2: “azul”, 3: “marrom”}
A saída deverá ser
>>> {1: 8, 2: 4, 3: 6}

"""

"""
#Forma 1 de fazer
dicio = {1: "vermelho", 2: "azul", 3: "marrom"}
dicio_values = dicio.values()
dicio_values_len = [len(x) for x in dicio_values]

dicio_keys = dicio.keys()

cria_dicio = {k: v for k, v in zip(dicio_keys, dicio_values_len)}

print(cria_dicio)

"""

#Forma 2 de fazer
# Definindo o dicionario
dic = {1: 'vermelho', 2: 'azul', 3: 'marrom', 4: 'roxo', 5: 'lilas', 6: 'alaranjado'}
# Definindo um dicionario vazio
dic_2 = {}

# Varendo todo dic
for k,v in dic.items():
    dic_2[k] = len(v)
 
# Imprimindo o resultado    
print(dic_2)