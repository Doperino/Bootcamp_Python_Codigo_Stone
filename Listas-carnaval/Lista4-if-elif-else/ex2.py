"""
Escreva um programa que receba dois números e imprima na tela se o primeiro é divisível pelo segundo.
"""

def valida_num():
    while True:
        try:
            num = int(input('>'))
            return num 
        except ValueError:
            print("Digite um número válido:")

print("Digite o primeiro número:")
num1 = valida_num()
print("Digite o segundo número")
num2 = valida_num()

if num1 % num2 == 0:
    print(f"{num1} é divisível por {num2}")
else:
    print(f"{num1} não é divisível por {num2}")