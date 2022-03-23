"""
Escreva um programa que leia do usuário um número de 4 dígitos e 
imprima a soma destes dígitos. Exemplo, se o usuário digitar 3141 
seu programa deverá imprimir na tela 3+1+4+1=9.
"""

def teste_num():
    while True:
        try:
            num = int(input('>'))
            if num < 0:
                num = num * -1
            while (num < 1000 or num > 9999):
                num = int(input("Valor inválido, digite um número inteiro de 4 dígitos:\n>"))
            return num
        except ValueError:
            print("Valor inválido, digite um número inteiro:")

def separa_num(num):
    list_num = []
    for i in range(4):
        list_num.append(num % 10)
        num //= 10
    return list_num

list_num = []

print("Digite um número qualquer de 4 dígitos")
num = teste_num()
list_num = separa_num(num)
soma = sum(list_num)

print(f"A soma dos dígitos desse número é igual a {soma}.")



