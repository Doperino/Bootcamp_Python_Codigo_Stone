
lista_idades = list()

print("Forneça a idade de cada um dos participantes:")

while True:
    idade = input('>')
    
    while idade == '' and len(lista_idades) == 0:
        idade = input('Nenhuma pessoa foi adicionada, adicione a idade de pelo menos uma pessoa: ')
    
    if idade == '':
        break    
    
    else:
        lista_idades.append(int(idade))

preco_pagar = 0
perfis = [('bebês', 0 ), ('crianças', 0 ), ('adultos', 0), ('idosos', 0)]
perfis = dict(perfis)

for i in lista_idades:
    if i <= 2:
        perfis['bebês'] += 1
    elif i >= 3 and i <= 12:
        perfis['crianças'] += 1
    elif i >= 65:
        perfis['idosos'] += 1
    else:
        perfis['adultos'] += 1

for k, v in perfis.items():
    if k == 'bebês':
        print(f"quantidade de {k}: {v} ---> R${v*0}")
    elif k == 'crianças':
        preco_pagar += v * 14
        print(f"quantidade de {k}: {v} ---> R${v*14}")
    elif k == 'adultos':
        preco_pagar += v * 23
        print(f"quantidade de {k}: {v} ---> R${v*23}")
    else:
        preco_pagar += v * 18
        print(f"quantidade de {k}: {v} ---> R${v*18}")

qtd_pessoas = sum(list(perfis.values()))
print(f"quantidade de pessoas: {qtd_pessoas} ---> Total a pagar: R${preco_pagar}")

