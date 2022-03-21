"""
Modifique o programa anterior para imprimir de 1 até o número digitado 
pelo usuário, mas, dessa vez, apenas os números ímpares.

"""
lim = int(input("Até que número você deseja que a contagem seja realizada?\n>"))

#forma1
for i in range(1, (lim + 1), 2):
    print(i, end=' ')
print("\n")

#Forma2
for i in range(1, (lim + 1)):
    if i % 2 != 0:
        print(i, end=' ')