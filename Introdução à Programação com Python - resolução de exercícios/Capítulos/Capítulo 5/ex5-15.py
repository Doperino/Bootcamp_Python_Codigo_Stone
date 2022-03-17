"""
Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
Utilize a tabela de códigos a seguir para obter o preço de cada produto:

Código Preço
1      0,50
2      1,00 
3      4,00
5      7,00
9      8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0.
Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
"""

lista_compra = dict()

cod_produtos = {'1': 0.5, '2': 1.0, '3': 4.0, '5': 7.0, '9': 8.0}

valorCompra = 0

while True:
    prod = str(input("Código do produto: "))
    
    if prod == '0':
        break

    elif prod not in cod_produtos.keys():
        print("Código inválido!")

    else:
        qtd = int(input("Quantidade do produto: "))
        
        if prod in lista_compra.keys():
            qtd += lista_compra[prod]
            lista_compra[prod] = qtd

        else:
            lista_compra[prod] = qtd

for prodCompra, qtd in lista_compra.items():
    for prod, valor in cod_produtos.items():
        if prodCompra == prod:
            valorCompra += qtd * valor

print(f"Valor total da compra: R${valorCompra}")
