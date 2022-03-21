"""
Escreva um programa que converta uma temperatura digitada
em °C em °F. A fórmula para essa conversão é:

     9 × C
 F = ----- + 32
       5
"""

celsius = float(input("Digite a temperatura em Celius:\n>"))
fahrenheit = (9 * celsius)/5 + 32

print(f"A temperatura respectiva em fahrenheit é de {fahrenheit}ºF")
