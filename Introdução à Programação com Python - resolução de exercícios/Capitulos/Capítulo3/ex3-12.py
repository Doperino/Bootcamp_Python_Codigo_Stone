"""
Escreva um programa que calcule o tempo de uma viagem de carro.
Pergunte a distância a percorrer e a velocidade média esperada
para a viagem.
"""

distancia = float(input("Digite a distância a ser percorrida em Km:\n>"))
velocidade_media = float(input("Digite a provável velocidade média em Km/h:\n>"))

while distancia == 0 or velocidade_media == 0:
    distancia = float(input("Digite um valor maior que zero para a distância a ser percorrida em Km:\n>"))
    velocidade_media = float(input("Digite um valor maior que zero para a provável velocidade média em Km/h:\n>"))

tempo = distancia / velocidade_media

if tempo >= 24:
    tempo /= 24
    print(f"O tempo percorrido será de {tempo} dias")

elif tempo >= 1 and tempo < 24:
    print(f"O tempo percorrido será de {tempo} horas")

elif tempo > 0 and tempo < 1:
    tempo *= 60
    print(f"O tempo percorrido será de {tempo} minutos")
