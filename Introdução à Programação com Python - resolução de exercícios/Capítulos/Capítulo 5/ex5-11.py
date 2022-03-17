"""
Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses. 
Escreva o total ganho com juros no período.
"""

depoInicial = float(input("Bem vindo ao Banco do Igor! Informe o depósito inicial para simulação:\n>"))
tempo = int(input("Por quanto tempo você manterá a aplicação?\n>"))
juros = float(input("Qual a porcentagem da taxa de juros?:\n>"))

saldo = depoInicial

for i in range(tempo):
    acompSaldo = saldo
    ganho = round(saldo * juros / 100, 2)
    saldo += ganho 
    print(f"{repr(i + 1).rjust(2)}º mês ---> Saldo: R${acompSaldo:.2f} -- Ganho: R${ganho:.2f} -- Total: R${saldo:.2f}")


