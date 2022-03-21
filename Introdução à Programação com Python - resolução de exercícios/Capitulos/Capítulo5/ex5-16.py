"""
Sistema de troco
Nota max = 200 reais
Nota min = 2 reais
Moeda max = 50 cents
Moeda min = 5 cents
"""

#Função que valida o número, a partir da parte fracionária
def valida_num():
    #listaIntFra = []
    
    valor = float(input())
    
    while True:
        parteInt = int(valor)
        parteFra = round((valor - parteInt) * 100)

        if parteFra % 5 != 0:
            print("Digite um valor válido (terminado em 0 ou 5): ", end='')
            valor = float(input())
        
        else:
            #listaIntFra.append(parteInt)
            #listaIntFra.append(parteFra)
            return valor

#Essa função recebe a lista das notas/centavos existentes e cria uma lista para acrescentar a ela a quantidade de notas/centavos utilizados, retornando ela
def notas(lista_notas, num):

    lista_qtd_notas = list()

    for nota in lista_notas:
        notas = 0

        while num >= nota:
            notas += 1
            num = round(num - nota, 2)
            
        lista_qtd_notas.append(notas)
    
    return lista_qtd_notas
    
#Lista das notas/moedas existentes
lista_notas = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]

print("Digite o valor para a contagem de notas/moedas: ", end='')

#listaIntFra = valida_num()
num = valida_num()

#Int = listaIntFra[0]
#Fra = listaIntFra[1]

#lista_qtd_notas = notas(lista_notas, Int)
lista_qtd_notas = notas(lista_notas, num)

index = 0
for qtd in lista_qtd_notas:

    if qtd == 0:
        index += 1

    elif lista_notas[index] > 1:
        print(f"{qtd} cédulas de  {repr(lista_notas[index]).rjust(3)}")
        index +=1

    elif lista_notas[index] == 1:
        print(f"{qtd} cédulas de    {lista_notas[index]:.0f}")
        index +=1

    else:
        print(f"{qtd} moedas  de {lista_notas[index]:.2f}")
        index += 1

