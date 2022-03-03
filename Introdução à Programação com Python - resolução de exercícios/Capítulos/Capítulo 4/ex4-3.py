"""
Exercício 04-03: Escreva um programa que leia três números e que 
imprima o maior e o menor

Escreva um programa que leia três números e que imprima o maior 
e o menor.

"""


"""
#solução 1

def maior_menor(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            if num2 > num3:
                print(f"O maior número é o {num1} e o menor {num3}")
            else:
                print(f"O maior número é o {num1} e o menor {num2}")
        else:
            if num1 > num2:
                print(f"O maior número é o {num3} e o menor {num2}")
            else:
                print(f"O maior número é o {num3} e o menor {num1}")
    else:
        if num2 > num3:
            if num1 > num3:
                print(f"O maior número é o {num2} e o menor {num3}")
            else:
                print(f"O maior número é o {num2} e o menor {num1}")
        else:
            if num2 > num1:
                print(f"O maior número é o {num3} e o menor {num1}")
            else:
                print(f"O maior número é o {num3} e o menor {num2}")  


num1 = float(input("Digite o primeiro número:\n>"))
num2 = float(input("Digite o segundo número:\n>"))
num3 = float(input("Digite o terceiro número:\n>"))

maior_menor(num1, num2, num3)

"""

#solução 2

lista_num = []

lista_num.append(float(input("Digite o primeiro número:\n>")))
lista_num.append(float(input("Digite o segundo número:\n>")))
lista_num.append(float(input("Digite o terceiro número:\n>")))

menor = lista_num[0]
maior = lista_num[len(lista_num) - 1]

print(f"O maior número é o {maior} e o menor {menor}")