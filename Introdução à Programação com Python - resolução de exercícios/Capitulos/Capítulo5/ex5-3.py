"""
Faça um programa para escrever a contagem regressiva do lançamento de 
um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e Fogo! na tela.

"""

print("Contagem regressiva para o lançamento:")

for i in reversed(range(0, 11)):
    print(i, end= '...')

print("Fogo!")
