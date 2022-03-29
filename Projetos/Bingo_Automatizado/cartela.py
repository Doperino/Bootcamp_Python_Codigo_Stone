import collections
import random

LETRAS = ("B", "I", "N", "G", "O")

def min_max(letra: str) -> tuple[int]:

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
    print("B   I   N   G   O")
    for linha in range(5):
        lista_str = [str(lista[linha]).zfill(2) for lista in cartela.values()]
        string = ', '.join(lista_str)
        print(string)

def marca_cartela(cartela: dict[str, list[int]], letra: str, numero: int) -> dict:
    if numero in cartela[letra]:
        indice = cartela[letra].index(numero)
        cartela[letra][indice] = 'XX'
    return cartela
    