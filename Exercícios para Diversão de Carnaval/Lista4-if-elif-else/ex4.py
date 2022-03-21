"""
Faça um programa que imprima na tela se um dado ano é bissexto ou não de acordo com as regras na ordem abaixo:

1.	Um ano que é divisível por 400 é bissexto.
2.	Dos anos que não entram na regra 1, se o ano for divisível por 100 então ele não é bissexto.
3.	Dos anos que não entram na regra 2, se o ano for divisível por 4 então ele é um ano bissexto.
4.	Todos os outros anos não são bissextos

"""

#Validador do número
def valida_num():
    while True:
        try:
            num = int(input('>'))
            return num 
        except ValueError:
            print("Digite um ano válido:")

print("Digite o ano desejado:")
ano = valida_num()

if ano % 400 == 0 | (ano % 100 != 0 and ano % 4 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")

