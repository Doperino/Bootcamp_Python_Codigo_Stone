"""
Faça um programa que remova strings vazias de uma lista de strings. 
Exemplo: dada a lista [“Olá”, “”, “meu”, “nome”, “”, “é”, “facilitador”, “”] a saída deve ser
>>> [“Olá”, “meu”, “nome”, “é”, “facilitador”]

"""

#Forma 1 de fazer
"""
lst = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]
lst_sem_espacos = []

for i in range(len(lst)):
    if lst[i] != "":
        lst_sem_espacos.append(lst[i])

print(lst)
print(lst_sem_espacos)
"""

#Forma 2 de fazer iterando sobre uma cópia rasa
lst = ["Olá", "", "meu", "nome", "", "é", "facilitador", ""]

"""
for i in lst.copy():
    if i == "":
        lst.remove(i)
"""     
#Formma 3 de fazer iterando sobre a cópia rasa e utilizando pop e index, 
#para retirar o elemento de acordo com seu index
for i in lst.copy():
    if i == "":
        lst.pop(lst.index(i))

print(lst)
