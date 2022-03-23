"""
Crie uma lista com 6 números inteiros. Imprima o maior, o menor e suas 
respectivas posições. 
Exemplo: para a lista [5,4,6,8,3,4] a saída deve ser

>>> O maior elemento é 8 e está na posição 3
>>> O menor elemento é 3 e está na posição 4

Obs: caso o maior ou o menor número sejam repetidos, trazer a menor posição.

"""

def valida_num():
    while True:
        try:
            num = int(input('>'))
            return num
        except ValueError:
            print("Valor inválido, digite um número inteiro")


lista = []

for i in range(7):
    item = valida_num()
    lista.append(item)

#maior = lista[0]
#menor = lista[0]

lista_copia = lista.copy()
lista_copia.sort()

menor = lista_copia[0]
maior = lista_copia[len(lista_copia) - 1]

"""
for i in range(len(lista)):
    if maior <= lista[i]:
        maior = lista[i]
    if menor >= lista[i]:
        menor = lista[i]
"""

print(lista)
index_maior = lista.index(maior)
index_menor = lista.index(menor)

print(f"O maior elemento é o {maior} e possui index {index_maior}")
print(f"O menor elemento é o {menor} e possui index {index_menor}")