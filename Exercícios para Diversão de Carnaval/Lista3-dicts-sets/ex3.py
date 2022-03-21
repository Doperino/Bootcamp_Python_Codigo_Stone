"""
Faça um programa que ordene um dicionário por seus valores. 
Exemplo: dado o dicionário
>>> {“matemática”: 81, “física”: 83, “química”: 87} 
a saída deve ser 
>>> {“química”: 87, “física”: 83, matemática”: 81}

notas = {"matemática": 81, "física": 83, "química": 87}
#print(notas.items())


print(sortedByVal)



lista = []

for i in range(10):
    lista.append(i ** 2)

print(lista)


lista = list(map(lambda x: x**2, range(10)))
print(lista)


lista = [x**2 for x in range(10)]
print(lista)


"""
notas = {"matemática": 81, "física": 83, "química": 87}
print(notas)


#sortedByVal = {k: v for k, v in sorted(notas.items(), key= lambda v: v[1] , reverse= True)}
notas_sort = {k: v for k, v in sorted(notas.items(), key= lambda v:v[1], reverse = True)}
print(notas_sort)

#Acima utilizamos uma compreensão de um dicionário
#Em uma linha só, fazemos um iterável para criar os elementos do dicionário
#Os elementos do dicionário são criados de forma que eles são organizados de acordo com o sorted()
#dento de sorted() temos o iterável notas.items(), que irá iterar sobre os items do dicionário (key:value)
#key é a função que define como o dicionário será organizado (chave de comparação)
#lambda v:v[1] é uma função anônima que complementa key, de forma que a organização será feita por v, sendo v pertencente ao dicionário v[1] seu item.
#reverse é utilizado para colocar em ordem decrescente caso True



