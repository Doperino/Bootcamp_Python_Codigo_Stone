"""
Calcule o resultado da expressão A > B and C or D,
utilizando os valores da tabela a seguir.

A  B C     D      Resultado
1  2 True  False
10 3 False False
5  1 True  True
"""

A, B, C, D = 1, 2, True, False

result = (A > B) & (C | D)
print(result)

A, B, C, D = 10, 3, False, False

result = (A > B) & (C | D)
print(result)

A, B, C, D = 5, 1, True, True

result = (A > B) & (C | D)
print(result)
