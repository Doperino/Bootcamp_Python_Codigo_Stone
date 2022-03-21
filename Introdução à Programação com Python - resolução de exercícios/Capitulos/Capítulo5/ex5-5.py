"""
Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
"""

list_mult = list()
i = 0
while len(list_mult) != 10:
    list_mult.append(3*i)
    i += 1

print(list_mult)

for i in list_mult:
    print(i, end=' ')