import modulos

lista_idades = list()
perfis = [('bebês', 0 ), ('crianças', 0 ), ('adultos', 0), ('idosos', 0)]
perfis = dict(perfis)

print("Forneça a idade de cada um dos participantes:")

while True:
    idade = modulos.valida_idade(lista_idades)
    if idade == '':
        break
    lista_idades.append(idade)

perfis = modulos.conta_perfil(lista_idades, perfis)
modulos.calcula_total(perfis)
