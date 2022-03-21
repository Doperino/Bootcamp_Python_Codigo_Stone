"""
Escreva um programa que leia a quantidade de dias, horas, minutos
e segundos do usuário. Calcule o total em segundos.
"""

dias = int(input("Digite a quantidade de dias:\n>"))
horas = int(input("Digite a quantidade de horas:\n>"))
minutos = int(input("Digite a quantidade de minutos:\n>"))
segundos = int(input("Digite a quantidade de segundos:\n>"))

soma = (dias * 24 * 60 ** 2) + (horas * 60 ** 2) + (minutos * 60) + segundos
print(f"O total em segundos é igual a: {soma} segundos")
