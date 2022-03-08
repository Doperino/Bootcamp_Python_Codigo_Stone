"""
No exercício acima você calculou a área de um triângulo a partir da 
sua base e altura. Faça um programa que receba os 3 lados de um 
triângulo – s1, s2 e s3 – e calcule sua área. 
Compare a resposta com o exercício acima, dada das mesmas entradas. 
Os resultados devem ser idênticos.


(semiperimetro) s = (s1 + s2 + s3) / 2
area = √(s . (s - s1 ) . (s - s2) . (s - s3))

"""


import math

#Função que retorna o número, validando se ele é um número e se é maior que zero 
def fornec_lado():
    while True:
        try:
            lado = float(input('>'))
            while lado <= 0:
                lado = float(input("Digite um número válido maior que zero:"))
            return lado
        except ValueError:
            print("Valor inválido, digite um número:")


print("Forneça a seguir os lados do triângulo, em metros:")

print("Lado 1:")
lado1 = fornec_lado()
print("Lado 2:")
lado2 = fornec_lado()
print("Lado 3:")
lado3 = fornec_lado()

semi_per = (lado1 + lado2 + lado3) / 2
area = math.sqrt(semi_per * (semi_per - lado1) * (semi_per - lado2) * (semi_per - lado3))

print(f"A área do triângulo é equivalente a {area} m²")