def valida_triangulo(lados: list) -> bool:
    maior = max(lados)
    menor = min(lados)
    if maior > (sum(lados) - maior - menor):
        if maior < (sum(lados) - maior):
            return True
    else:
        return False

def converte_str(lados: str) -> list:
    lados = list(lados.split(','))
    lados = [int(x) for x in lados]
    return lados

while True:
    ladosTriangulo = input("Informe os lados do triângulo separados por vírgula (,):\n>")
    ladosTriangulo = converte_str(ladosTriangulo)
    while len(ladosTriangulo) > 3:
        ladosTriangulo = input("Informe somente três lados:\n>")
        ladosTriangulo = converte_str(ladosTriangulo)
    break

if valida_triangulo(ladosTriangulo):
    print("Triângulo válido!")
else:
    print("Triângulo inválido")
