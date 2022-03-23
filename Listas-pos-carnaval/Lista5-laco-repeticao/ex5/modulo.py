from copy import deepcopy

def registra_notas(qtd_candidatos: int, qtd_jurados: int, notas_candidatos: dict) -> dict:
    for i in range(qtd_candidatos):
        nome = input(f"Nome do {i + 1}º candidato: ")
        notas_candidatos[nome] = []
        for j in range(qtd_jurados):
            nota = float(input(f"Nota do {j + 1}º jurado: "))
            notas_candidatos[nome].append(nota)
        print('')
    return notas_candidatos

def filtra_notas(notas_candidatos: dict) -> dict:
    notas_candidatos_filtradas = deepcopy(notas_candidatos)
    for nome in notas_candidatos_filtradas.keys():
        maior_nota = max(notas_candidatos_filtradas[nome])
        menor_nota = min(notas_candidatos_filtradas[nome])
        
        notas_candidatos_filtradas[nome].remove(maior_nota)
        notas_candidatos_filtradas[nome].remove(menor_nota)
    
    return notas_candidatos_filtradas
            
def calcula_media(notas_candidatos_filtradas: dict) -> dict:
    media_candidatos = dict()
    for nome in notas_candidatos_filtradas.keys():
        media_candidatos[nome] = round(sum(notas_candidatos_filtradas[nome]) / len(notas_candidatos_filtradas[nome]), 2)
    return media_candidatos

def apresenta_resultado(notas_candidatos: dict, media_candidatos: dict) -> None:
    for nome in notas_candidatos.keys():
        jurado = 0
        print(f"Atleta: {nome}")
        for nota in notas_candidatos[nome]:
            print(f"Nota do {jurado + 1}º ---> {nota} ")
            jurado += 1
        print('') #Espaço duplo

        print("Resultado final:")
        print(f"Melhor nota: {max(notas_candidatos[nome])}")
        print(f"Pior nota: {min(notas_candidatos[nome])}")
        print(f"Média filtrada: {media_candidatos[nome]}")
        print('') #Espaço