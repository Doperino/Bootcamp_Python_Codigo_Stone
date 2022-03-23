def valida_num(lista_valores: list) -> float:
    """Essa função valida o número a ser digitado""" 
    num = float(input(f'> '))  
    if len(lista_valores) == 0:
        while num == 0:
            num = float(input(f'Valor inválido. Digite novamente: '))
        return num

    else:
        return num

    ...

def calcula_media(valores: list) -> None:
    """ Essa função calcula a soma e imprime na tela"""
    media = sum(valores)/len(valores)
    print(f'média aritmética ---> {round(media, 2)}')


valores = list()

print("\nDigite a quantidade de números que quiser para cálculo da média.")
print("Obs: o 1º valor não pode ser igual a 0. A partir do 2º, o valor 0 retornará a média aritmética dos números.")


while True:
    num = valida_num(valores)
    if num == 0:
        break
    else:
        valores.append(num)

calcula_media(valores)