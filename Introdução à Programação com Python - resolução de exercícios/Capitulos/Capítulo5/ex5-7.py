"""
Modifique o programa anterior de forma que o usuário também digite o 
início e o fim da tabuada, em vez de começar com 1 e 10.
"""

num = int(input(("Tabuada de: ")))
inicio = int(input(("De: ")))
lim = int(input(("Até: ")))

for i in range(inicio, lim + 1):
    print(f"{num} x {i} =", num * i)