"""
Crie uma variável do tipo lista com 5 elementos (você escolhe quais serão).
Imprima na tela o elemento e sua respectiva posição na lista. 
Exemplo: para a lista [1, 3, 6, “H”, [7,7,7]] a saída deve ser:

>>> Elemento 1 na posição 0
>>> Elemento 3 na posição 1
>>> Elemento 6 na posição 2
>>> Elemento “H” na posição 3

"""

lista = []

for i in range(5):
    item = input(">")
    lista.append(item)

for i in range(5):
    print(f"Elemento {lista[i]} na posição {i}")