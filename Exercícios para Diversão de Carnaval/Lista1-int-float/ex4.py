"""
Faça um programa que receba do usuário seu peso em kg e altura 
em metros e imprima o Índice de Massa Corporal (IMC) do usuário.

IMC = peso /〖altura〗^2 

"""


def valida_num():
    while True:
        try:
            num = float(input('>'))
            while num <= 0:
                num = float(input("O número deve ser maior que zero:\n>"))
            return num
        except ValueError:
            print("Valor inválido, digite um número")


print("Digite o seu peso:")
peso = valida_num()

print("Digite sua altura:")
altura = valida_num()

imc = peso / altura ** 2

print(f"Seu IMC é igual a {imc:.2f}.")