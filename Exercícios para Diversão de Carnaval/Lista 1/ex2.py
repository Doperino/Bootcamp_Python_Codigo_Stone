"""
Faça um programa que receba a base e altura de um triângulo e imprima 
a área dele.

area = (base x altura) / 2

"""

base = float(input("Forneça a base do triângulo em metros:\n>"))
altura = float(input("Forneça a altura do triângulo em metros:\n>"))

area = (base * altura) / 2

print(f"O triângulo possui uma área de {area} m²")