"""
Escreva um programa que diga se um número dado pelo usuário é par ou ímpar
"""

def valida_num():
    while True:
        try:
            num = int(input('>'))
            return num 
        except ValueError:
            print("Digite um número válido:")

print("Digiter um número:")
num = valida_num()

if num % 2 == 0:
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar!")