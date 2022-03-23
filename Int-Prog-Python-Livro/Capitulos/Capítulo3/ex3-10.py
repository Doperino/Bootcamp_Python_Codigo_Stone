"""
Faça um programa que calcule o aumento de um salário.
Ele deve solicitar o valor do salário e a porcentagem do aumento.
Exiba o valor do aumento e do novo salário.
"""

salario = float(input("Digite o valor do seu salário:\n>"))
porc_aumento = float(input("Digite a porcentagem de aumento:\n>"))

aumento = (porc_aumento/100) * salario
novo_salario = salario + aumento

print(f"O aumento foi de R${aumento}, resultando em um salário novo de R${novo_salario}.")   
