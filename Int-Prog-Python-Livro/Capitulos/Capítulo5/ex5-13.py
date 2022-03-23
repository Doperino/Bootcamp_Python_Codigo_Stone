"""
Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. 
Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
"""

dividaIni = float(input("Valor da dívida?\n>"))
percJuros = float(input("Juro mensal:\n>"))
pgmtoMensal = float(input("Valor do Pagamento Mensal:\n>"))

meses = 0
valPago = 0
dividaCorrigida = 0
dividaCorrigida = dividaIni

valJuros = percJuros * dividaIni / 100

while pgmtoMensal < valJuros:
    pgmtoMensal = float(input(f"Com esse pagamento a dívida nunca será paga, escolha um valor acima de {valJuros}:\n>"))

while pgmtoMensal < dividaCorrigida:
    valJuros = percJuros * dividaCorrigida / 100
    dividaCorrigida += valJuros - pgmtoMensal
    meses += 1
    valPago += pgmtoMensal

pgmtoRestante = dividaCorrigida
valPago += pgmtoRestante
totalJuros = valPago - dividaIni

print(f"A dívida será paga em {meses + 1} meses. Você pagará um total de R${valPago:.2f}, dessa valor, R${totalJuros:.2f} foram de juros.  ")
print(f"Relatório: R${meses * pgmtoMensal} por {meses} meses e {pgmtoRestante:.2f} no {meses + 1}º mês")