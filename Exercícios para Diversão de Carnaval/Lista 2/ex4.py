"""
Faça um programa que receba a temperatura média de cada mês do ano e 
armazene-as em uma lista. Em seguida, calcule a média anual das 
temperaturas e mostre a média calculada juntamente com todas as 
temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: Exemplo de saída:

>>> Meses com temperatura acima da média anual de 35,5°:
>>> 1 – janeiro
>>> 3 – março
>>> 6 – junho

"""

def valida_num():
    while True:
        try:
            num = int(input())
            return num
        except ValueError:
            print("Valor inválido, digite um número inteiro")


lista_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
lista_temp = []

print("Digite a temperatura média dos seguintes meses:")

for i in lista_meses:
    print(f"{i}: ", end='')
    lista_temp.append(valida_num())

media_temp_anual = sum(lista_temp) / len(lista_temp)
media_temp_anual = round(media_temp_anual, 2)

print(f"A temperatura média anual foi de {media_temp_anual}ºC")
print("Os meses que tiveram temperatura acima da média foram:")

for i in range(len(lista_temp)):
    if lista_temp[i] > media_temp_anual:
        print(f">>>> {i} -- {lista_meses[i]}")
     
