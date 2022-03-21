"""
Exercício 04-04: Escreva um programa que pergunte o salário do 
funcionário e calcule o valor do aumento

Escreva um programa que pergunte o salário do funcionário e 
calcule o valor do aumento. Para salários superiores 
a R$ 1.250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, de 15%.

"""


salario_base = 1250
porc_aumento1 = 0.1
porc_aumento2 = 0.15

salario = float(input("Digite o seu salário:\n>"))

if salario > salario_base:
    salario_novo = salario * (1 + porc_aumento1)
    print(f"Seu salario novo é de R${salario_novo}.")
else:
    salario_novo = salario * (1 + porc_aumento2)
    print(f"Seu salario novo é de R${salario_novo}.")
