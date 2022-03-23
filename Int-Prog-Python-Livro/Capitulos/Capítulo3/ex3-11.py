"""
Faça um programa que solicite o preço de uma mercadoria e o
percentual de desconto. Exiba o valor do desconto e o preço a pagar.
"""

preco_mercadoria = float(input("Digite o valor da mercadoria:\n>"))
porc_desconto = float(input("Digite a porcentagem de desconto:\n>"))

desconto = (porc_desconto/100) * preco_mercadoria
novo_preco = preco_mercadoria - desconto

print(f"O desconto foi de R${desconto}, resultando preço a pagar de R${novo_preco}.")   
