"""
Escreva um programa que leia dois números. Imprima o resultado da 
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de 
soma e subtração para calcular o resultado. Lembre-se de que podemos 
entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4 * 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
"""

num_1 = int(input("Digite o primeiro número:\n>"))
num_2 = int(input("Digite o segundo número:\n>"))
resultado = 0
for i in range(num_2):
    resultado += num_1

print(f"Resultado de {num_1} x {num_2} = {resultado}")