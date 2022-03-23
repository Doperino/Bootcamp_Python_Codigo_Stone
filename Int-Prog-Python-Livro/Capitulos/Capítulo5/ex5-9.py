"""
Escreva um programa que leia dois números. Imprima a divisão inteira do 
primeiro pelo segundo, assim como o resto da divisão. Utilize apenas os 
operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números 
como a quantidade de vezes que podemos retirar o divisor do dividendo. 
Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20.
"""

num_1 = int(input("Digite o primeiro número:\n>"))
num_2 = int(input("Digite o segundo número:\n>"))

maior = num_1

if maior > num_2:
    menor = num_2
else:
    maior = num_2
    menor = num_1

quociente = 0
resto = 0

while maior >= menor:
    maior -= menor
    quociente += 1

resto = maior

print(f"A divisão de {num_1} por {num_2} possui quociente igual a {quociente} e resto {resto}")