"""
Escreva uma expressão que será utilizada para decidir se um aluno
foi ou não aprovado. Para ser aprovado, todas as médias do aluno
devem ser maiores que 7. Considere que o aluno cursa apenas
três matérias, e que a nota de cada uma está armazenada nas seguintes
variáveis: matéria1, matéria2 e matéria3.
"""

matéria1 = float(input("Digite a nota da 1º matéria:\n>"))
matéria2 = float(input("Digite a nota da 2º matéria:\n>"))
matéria3 = float(input("Digite a nota da 3º matéria:\n>"))

média = (matéria1 + matéria2 + matéria3)/3

print(f"Sua média foi de: {média} pontos")

if média >= 7:
    print("Parabéns! Você foi aprovado.")
else:
    print("Que pena! Você não foi aprovado")
