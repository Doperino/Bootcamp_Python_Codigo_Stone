"""
Exercício 04-06: Escreva um programa que pergunte a distância 
que um passageiro deseja percorrer em km

Escreva um programa que pergunte a distância que um passageiro 
deseja percorrer em km. Calcule o preço da passagem, 
cobrando R$ 0,50 por km para viagens de até de 200 km, 
e R$ 0,45 para viagens mais longas.

"""

qtd_km = float(input("Digite a quantidade de km do trajeto:\n>"))

while(qtd_km <= 0):
    qtd_km = float(input("Digite uma quantidade de km válida, maior que zero:\n>"))

if qtd_km <= 200:
    preco_km = 0.50 * qtd_km
    print(f"Sua passagem custará R${preco_km}")

else:
    preco_km = 0.45 * qtd_km
    print(f"Sua passagem custará R${preco_km}")