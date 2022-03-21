"""
Escreva uma expressão para determinar se uma pessoa deve ou não
pagar imposto. Considere que pagam imposto pessoas cujo salário
é maior que R$ 1.200,00.
"""

salario = float(input("Qual o seu salário?\n>"))
while salario < 0:
    print("Digite um numero maior ou igual a zero:")
    salario = float(input('>'))

if salario > 1200:
    print("Você deve pagar imposto")
else:
    print("Você não deve pagar imposto")
