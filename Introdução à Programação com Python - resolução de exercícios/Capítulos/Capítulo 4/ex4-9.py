"""
Exercício 04-09: Escreva um programa para aprovar o empréstimo bancário 
para compra de uma casa

Escreva um programa para aprovar o empréstimo bancário para compra de 
uma casa. O programa deve perguntar o valor da casa a comprar, 
o salário e a quantidade de anos a pagar. 
O valor da prestação mensal não pode ser superior a 30% do salário. 
Calcule o valor da prestação como sendo o valor da casa a comprar 
dividido pelo número de meses a pagar.
"""

valor_da_casa = float(input("Digite o valor da casa:\n>"))
salario = float(input("Digite o valor do seu salário:\n>"))
qtd_anos = float(input("Digite a quantidade de anos para pagar:\n>"))

prestacao = valor_da_casa / (qtd_anos * 12)
limite_prest_mensal = 0.3 * salario
qtd_anos_ideal = valor_da_casa / (12 * limite_prest_mensal)

if prestacao <= limite_prest_mensal:
    print("Parabéns! Seu financiamento foi aprovado!")
else:
    print("Infelizmente seu financiamento não foi aprovado.")
    print(f"Entretanto, você pode optar por uma parcela de {limite_prest_mensal}", end=' ')
    print(f"e pagar durante {qtd_anos_ideal:.2f} anos.")