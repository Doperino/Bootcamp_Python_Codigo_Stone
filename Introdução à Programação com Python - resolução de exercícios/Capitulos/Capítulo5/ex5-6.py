"""
Altere o programa anterior para exibir os resultados no mesmo formato de 
uma tabuada: 2x1 = 2, 2x2 = 4,
"""

num = int(input(("Tabuada de: ")))
for i in range(10):
    print(f'{num} x {i} = ', num*i)

