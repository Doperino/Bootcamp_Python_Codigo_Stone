from modulo import *

notas_candidatos = dict()
media_candidatos = dict()
notas_candidatos_filtradas = dict()

qtd_candidatos = int(input("Número de candidatos avaliados: "))
qtd_jurados = int(input("Quantidade de jurados: "))
print('')

notas_candidatos = registra_notas(qtd_candidatos, qtd_jurados, notas_candidatos)
notas_candidatos_filtradas = filtra_notas(notas_candidatos)
media_candidatos = calcula_media(notas_candidatos_filtradas)

apresenta_resultado(notas_candidatos, media_candidatos)

    
