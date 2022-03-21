"""
Faça um programa que receba dois números inteiros do usuário, 
A e B e imprima na tela as seguintes operações:

•	A soma de A e B;
•	A diferença quando se subtrai B de A;
•	O produto (multiplicação) entre A e B;
•	O quociente (parte inteira da divisão) quando se divide A por B;
•	O resto da divisão entre A e B;
•	O resultado de log10 de A;
•	O resultado de A elevado a B;

"""
#Importação da biblioteca math
import math

#Função que pede o número do usuário e retorna somente um número válido
def digita_num():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Número inválido, digite um número inteiro")

print("Digite o primeiro número:\n>")
num1 = digita_num()

print("Digite o segundo número:\n>")
num2 = digita_num()

soma = num1 + num2
dif = num1 - num2
prod = num1 * num2
quoc = num1 // num2
rest = num1 % num2
lgrtm = math.log10(num1)
pot = num1 ** num2

print(f"soma = {soma}")
print(f"subtração = {dif}")
print(f"produto = {prod}")
print(f"divisão = {quoc}")
print(f"resto = {rest}")
print(f"log do primeiro número na base 10 = {lgrtm}")
print(f"Primeiro número elevado ao Segundo = {pot}")


