"""
Escreva um programa que pergunte a quantidade de
km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia
e R$ 0,15 por km rodado.
"""

qtd_km_percorrido = float(input("Digite a quantidade de km percorrida:\n>"))
qtd_dias_alugado = float(input("Digite a quantidade de dias que o carro ficou alugado:\n>"))

preco_a_pagar = qtd_dias_alugado * 60 + qtd_km_percorrido * 0.15

print(f"Você pagará um total de R${preco_a_pagar} pelo aluguel do veículo")
