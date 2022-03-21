"""

Crie uma lista com 10 elementos (você escolhe quais serão) e imprima a 
lista na ordem inversa. Exemplo: para a lista [1, 3, 6, “H”, [7,7,7] 
a saída deve ser
>>> [[7,7,7], “H”, 6, 3, 1]

"""

lista = []

for i in range(11):
    item = input(">")
    lista.append(item)

print(lista)
lista.reverse()
print(lista)