import collections
import random


LETRAS = ("B", "I", "N", "G", "O")

def min_max(letra: str) -> tuple[int]:
    """Receba a letra e retorna o min,max respectivo

    Args:
        letra (str): Nada mais que a letra sorteada

    Returns:
        tuple[int]: retorna a tupla com o min,max em questão
    """
    intervalo = {
    "B": (1, 15),
    "I": (16, 30),
    "N": (31, 45),
    "G": (46, 60),
    "O": (61, 75)
    }

    minimo, maximo = intervalo[letra][0], intervalo[letra][1]
    
    return minimo, maximo

def gera_cartela() -> collections.defaultdict[str, list[int]]:
    """Gera a cartela a ser utilizada nos sorteios

    Returns:
        collections.defaultdict[str, list[int]]: Retorna uma cartela em formato de dicionário, guardando em cada uma das letras (keys) a lista dos números sorteados (values)
    """
    cartela = collections.defaultdict(list)

    for letra in LETRAS:
        while len(cartela[letra]) < 5:
            minimo, maximo = min_max(letra)
            num_aleatorio = random.randint(a=minimo, b=maximo)

            if num_aleatorio not in cartela[letra]:
                cartela[letra].append(num_aleatorio)
                cartela[letra].sort()

    return cartela

def imprime(cartela: dict[str, list[int]]) -> None:
    """Imprime a cartela formatada

    Args:
        cartela (dict[str, list[int]]): A cartela em si, em formato de dicionário
    """
    print("B   I   N   G   O")
    for linha in range(5):
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]
        string = ', '.join(lista_str)
        print(string)

def marca_cartela(cartela: dict[str, list[int]], letra: str, numero: int) -> dict:
    """Marca a cartela, de acordo com a letra e o número sorteados

    Args:
        cartela (dict[str, list[int]]): recebe a cartela que será atualizada
        letra (str): recebe a letra sorteada
        numero (int): recebe o número sorteado da letra sorteada

    Returns:
        dict: retorna a cartela marcada ou não, de acordo com o que foi sorteado
    """
    if numero in cartela[letra]:
        indice = cartela[letra].index(numero)
        cartela[letra][indice] = 'XX'
    return cartela
    