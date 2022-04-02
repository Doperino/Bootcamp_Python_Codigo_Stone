import random
import cartela

def sorteia() -> tuple[str, int]:
    """Sorteia a letra e o número

    Returns:
        tuple[str, int]: Retorna uma tupla com a letra e o número sorteados
    """
    letra_sorteada = random.choice(cartela.LETRAS)
    minimo, maximo = cartela.min_max(letra_sorteada)
    numero_sorteado = random.randint(minimo, maximo)
    return letra_sorteada, numero_sorteado

def sorteia_cartelas(cart: dict) -> tuple[dict, int]:
    """com o número e a letra sorteados, faz o sorteio dos números até que o ganhador seja identificado

    Args:
        cart (dict): recebe a cartela gerada

    Returns:
        tuple[dict, int]: retorna um tuple com a cartela e o número de sorteios que foram realizados para identificar o ganhador
    """
    sorteios = list()
    contagem_sorteios = 0
    while not verifica_ganhador(cart):
        letra_sorteada, numero_sorteado = sorteia()
        while (letra_sorteada, numero_sorteado) in sorteios:
            letra_sorteada, numero_sorteado = sorteia()

        sorteios.append((letra_sorteada, numero_sorteado))
        cart = cartela.marca_cartela(cart, letra_sorteada, numero_sorteado)
        contagem_sorteios += 1
        
    return cart, contagem_sorteios

def verifica_ganhador(cartela: dict) -> bool:
    """Verifica se alguma das colunas ou linhas foram sorteadas por completo

    Args:
        cartela (dict): recebe a cartela para verificar se há ganhador

    Returns:
        bool: retorna False ou True de acordo com a identificação do ganhador.
    """
    for coluna in cartela.values():
        if coluna.count('XX') == len(coluna):
            #print("Ganhador!")
            return True
    for linha in range(5):
        lista = [lista[linha] for lista in cartela.values()]
        if lista.count('XX') == len(lista):
            #print("Ganhador!")
            return True
    return False