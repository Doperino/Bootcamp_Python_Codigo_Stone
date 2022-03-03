"""
Exercício 04-10: Escreva um programa que calcule o preço a pagar 
pelo fornecimento de energia elétrica

Escreva um programa que calcule o preço a pagar pelo fornecimento 
de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: 
R para residências, I para indústrias e C para comércios. 
Calcule o preço a pagar de acordo com a tabela a seguir.

+---------------------------------------+
|   Preço por tipo e faixa de consumo   |
+---------------------------------------+
| Tipo        | Faixa (kWh)   | Preço   |
+=======================================+
| Residencial | Até 500       | R$ 0,40 |
|             | Acima de 500  | R$ 0,65 |
+---------------------------------------+
| Comercial   | Até 1000      | R$ 0,55 |
|             | Acima de 1000 | R$ 0,60 |
+---------------------------------------+
| Industrial  | Até 5000      | R$ 0,55 |
|             | Acima de 5000 | R$ 0,60 |
+---------------------------------------+
"""
def calcula_preco(instalacao, qtd_kwh, dicionario_inst):
    match instalacao:
        case 'R':
            if qtd_kwh <= 500:
                preco_consumo = qtd_kwh * 0.40
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")
            else:
                preco_consumo = qtd_kwh * 0.65
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")
        case 'C':
            if qtd_kwh <= 1000:
                preco_consumo = qtd_kwh * 0.55
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")
            else:
                preco_consumo = qtd_kwh * 0.60
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")
        case 'I':
            if qtd_kwh <= 5000:
                preco_consumo = qtd_kwh * 0.55
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")
            else:
                preco_consumo = qtd_kwh * 0.60
                print(f"Tipo de instalação: {dicionario_inst.get(instalacao)}")
                print(f"Preço de consumo: {preco_consumo}")


tipo_inst = ['R', 'I', 'C']
dicionario_inst = {'R': 'Residencial', 'I': 'Industrial', 'C': 'Comercial'}

print("Digite o seu tipo de instalação:")
instalacao = input("R: residencial, I: Industrial e C: Comercial.\n>")

while instalacao not in tipo_inst:
    instalacao = input("Digite um termo válido:\n>")

qtd_kwh = float(input("digite a quantidade de kWh consumida:\n>"))

while qtd_kwh <= 0:
    qtd_kwh = input("Digite uma quantidade válida:\n>")

calcula_preco(instalacao, qtd_kwh, dicionario_inst)


