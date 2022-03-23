
notas_candidatos = dict()
media_candidatos = dict()
notas_candidatos_filtradas = dict()

qtd_candidatos = int(input("Número de candidatos avaliados: "))
qtd_jurados = int(input("Quantidade de jurados: "))

#Registra o nome dos candidatos e a nota dos seus saltos
for i in range(qtd_candidatos):
    nome = input(f"Nome do {i + 1}º candidato: ")
    notas_candidatos[nome] = []
    for j in range(qtd_jurados):
        nota = float(input(f"Nota do {j + 1}º jurado: "))
        notas_candidatos[nome].append(nota)
    print('')
    
    #encontra a maior e a menor nota
    maior_nota = max(notas_candidatos[nome])
    menor_nota = min(notas_candidatos[nome])
    
    #Cria uma cópia da lista e remove a maior e a menor nota da lista filtrada 
    notas_candidatos_filtradas[nome] = notas_candidatos[nome].copy()
    notas_candidatos_filtradas[nome].remove(maior_nota)
    notas_candidatos_filtradas[nome].remove(menor_nota)

    #Realiza a média da lista filtrada
    media_candidatos[nome] = round(sum(notas_candidatos_filtradas[nome]) / len(notas_candidatos_filtradas[nome]), 2)

print('') #espaço

for nome in notas_candidatos.keys():
    jurado = 0
    print(f"Atleta: {nome}")
    for nota in notas_candidatos[nome]:
        print(f"Nota do {jurado + 1}º ---> {nota} ")
        jurado += 1
    print('\n') #Espaço duplo

    print("Resultado final:")
    print(f"Melhor nota: {max(notas_candidatos[nome])}")
    print(f"Pior nota: {min(notas_candidatos[nome])}")
    print(f"Média filtrada: {media_candidatos[nome]}")
    print('') #Espaço


    
