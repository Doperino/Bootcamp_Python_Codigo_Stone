"""
Escreva um programa para calcular a redução do tempo de vida
de um fumante. Pergunte a quantidade de cigarros fumados por dia
e quantos anos ele já fumou. Considere que um fumante perde
10 minutos de vida a cada cigarro, e calcule quantos dias de vida um
fumante perderá. Exiba o total em dias.
"""

qtd_cigarros_dia = int(input("Informe a quantidade de cigarros que você fuma em média por dia:\n>"))
qtd_anos = int(input("Informe a quantidade de anos que você já fuma:\n>"))

qtd_cigarros_total = qtd_cigarros_dia * qtd_anos * (365 + 5/525606)

min_vida_perd = 10 * qtd_cigarros_dia * qtd_anos * (365 + 5/525606)

dias_vida_perd = min_vida_perd / (60 * 24)

print(f"Você perdeu {dias_vida_perd} dias de vida por ter fumado tantos cigarros.")
