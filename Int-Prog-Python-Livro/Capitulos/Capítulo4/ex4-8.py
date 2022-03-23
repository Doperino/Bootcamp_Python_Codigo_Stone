"""
Exercício 04-08: Escreva um programa que leia dois números e que 
pergunte qual operação você deseja realizar

Escreva um programa que leia dois números e que pergunte qual 
operação você deseja realizar. Você deve poder calcular soma (+), 
subtração (-), multiplicação (*) e divisão (/). 
Exiba o resultado da operação solicitada.
"""
def operacoes():
    while True:   
        operacao = input("Digite a operação:\n>")

        while operacao not in lista_operacoes:
            operacao = input("Digite uma operação válida:\n>")

        num1 = float(input("Digite o primeiro número:\n>"))
        num2 = float(input("Digite o segundo número:\n>"))
        match operacao:
            case '+':
                resultado = num1 + num2
            case '-':
                resultado = num1 - num2
            case '*':
                resultado = num1 * num2
            case '/':
                resultado = num1 / num2

        print(f"Resultado da operação: {resultado}.")
        resposta = input("Deseja realizar uma nova operação?\n>")
        while resposta not in lista_respostas: 
            resposta = input("Digite uma resposta válida (sim ou não):\n>")

        if resposta in respostas_nao:
            break


#Solução com match (switch em C)
lista_operacoes = ['+', '-', '*', '/']
respostas_nao = ['n','na','nao','nã','não']
respostas_sim = ['s','si','sim']
lista_respostas = ['s','si','sim','n','na','nao','nã','não']

print("Digite a operação que você deseja realizar de acordo", end=' ')
print("com o guia logo abaixo:")
print("""\
 ----------------------------  
|           /guia/           |
| -------------------------- |
|      soma      --->   +    |
|    subtração   --->   -    |
|  multiplicação --->   *    |
|     divisão    --->   /    |
|                            |
 ----------------------------
""")

operacoes()
