"""
Faça um programa que encontre as notas mínimas e máximas de um dicionário, e imprima-os na tela com as suas respectivas chaves. Exemplo: dado o dicionário
>>> {“Theodoro”: 20, “Márcia”: 50, “Júnior”: 80}
A saída deve ser
>>> Nota máxima -> Júnior : 80
>>> Nota mínima -> Theodoro : 20




"""

notas = {"Theodoro": 20, "Márcia": 50, "Júnior": 80, "Lucas": 20}
notas_ordem = {k: v for k, v in sorted(notas.items(), key=lambda v:v[1])} #Somente para impressão em ordem de notas repetidas

lista_values = notas.values()
valor_maximo = max(lista_values)
valor_minimo = min(lista_values)

for k, v in notas_ordem.items():
    if notas_ordem[k] == valor_maximo:
        print(f">>> Nota máxima --> {k} : {v}")
    if notas_ordem[k] == valor_minimo:
        print(f">>> Nota mínima --> {k} : {v}")