"""
Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês, e 
você deve considerá-lo para o cálculo de juros do mês seguinte.
"""

def calculaPoupanca(depoMensal, juros, tempo):
    saldo = depoMensal
    for i in range(tempo):
        acompSaldo = saldo
        ganho = round(saldo * juros / 100, 2)
        saldo += ganho
        print(f"{repr(i + 1).rjust(2)}º mês ---> Depósito: R${depoMensal} -- Saldo: {acompSaldo:.2f} -- Ganho: R${ganho:.2f} -- Total: R${saldo:.2f}")
        saldo += depoMensal



depoMensal = float(input("Bem vindo ao Banco do Igor! Informe o depósito inicial para simulação:\n>"))
tempo = int(input("Por quanto tempo você manterá a aplicação?\n>"))
juros = float(input("Qual a porcentagem da taxa de juros?:\n>"))

calculaPoupanca(depoMensal, juros, tempo)