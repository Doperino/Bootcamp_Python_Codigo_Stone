"""
Exercício 04-02: Escreva um programa que pergunte a velocidade do carro 
de um usuário e diga se este foi ou não multado

Escreva um programa que pergunte a velocidade do carro de um usuário. 
Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi 
multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km 
acima de 80 km/h.
"""

"""
#Solução que aceita valores fracionários
velocidade_km_por_h = float(input("Digite a velocilidade atingida em km/h:\n>"))

if velocidade_km_por_h > 80:
    multa = (velocidade_km_por_h - 80) * 5 
    print(f"Você foi multado em R${multa}.")
else:
    print("Você não foi multado")

"""
"""

#Solução que aceita somente valores inteiros usando math
import math


velocidade_km_por_h = float(input("Digite a velocilidade atingida em km/h:\n>"))
velocidade_km_por_h = math.floor(velocidade_km_por_h)
if velocidade_km_por_h > 80:
    multa = (round(velocidade_km_por_h) - 80) * 5 
    print(f"Você foi multado em R${multa}.")
else:
    print("Você não foi multado")

"""

#Solução sem math
velocidade_km_por_h = float(input("Digite a velocilidade atingida em km/h:\n>"))
velocidade_km_por_h = int(velocidade_km_por_h)
if velocidade_km_por_h > 80:
    multa = (velocidade_km_por_h - 80) * 5 
    print(f"Você foi multado em R${multa}.")
else:
    print("Você não foi multado")