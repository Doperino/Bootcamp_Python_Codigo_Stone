"""
Dada a lista de strings [“1”, “7”, “99”, “15”] construa um programa que converte todos os elementos desta lista para inteiro.

Faça também o inverso, dada a mesma lista só que agora de elementos inteiros, converta todos os elementos para int.

"""

lst = ["1", "7", "99", "15"]

for i in range(len(lst)):
    lst[i] = int(lst[i]) #conversão explicita para int

for i in range(len(lst)):
    lst[i] = str(lst[i]) #conversão explícita para str

