from asyncio.proactor_events import _ProactorBaseWritePipeTransport


def taximetro(distancia: float, tarifa :float = 4, precoDist :float = 0.25/140) -> float:
    """Recebe a distância percorrida, faz o cálculo do preço da corrida e retorna"""
    return distancia * precoDist + tarifa    
    ...


print("Cálculo automático de viagem")
distancia = float(input("Digite a distância percorrida em metros:\n>"))

preco = taximetro(distancia)
print(f"Valor da corrida: R${preco}")
