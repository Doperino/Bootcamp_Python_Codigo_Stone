"""
Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). 
No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
"""

listaNum = list()

while True:
    num = int(input("Digite um número:\n>"))
    if num != 0:
        listaNum.append(num)
    else:
        break

soma = sum(listaNum)
mediaArit = soma / len(listaNum)

print(f"Quantidade de Números ----> {len(listaNum)}\nSoma ----> {soma}\nMédia ----> {mediaArit:.2f}")