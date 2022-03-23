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