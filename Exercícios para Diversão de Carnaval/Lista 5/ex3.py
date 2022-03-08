"""
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser realocadas para formar a outra palavra. 
Dada uma string qualquer, desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.

"""
import functools
import string
import math

#Importa o alfabeto inteiro e cria uma lista dele
alfabeto = list(string.ascii_lowercase)

#Solicita uma palavra do usuário
palavra = input("Digite a palavra escolhida:\n>")
palavra = palavra.lower()

#Cria uma lista de cada char da string palavra
palavra_lista = list(palavra)
#Cria a lista de repetições (para contar a aparição das letras  e suas repetições)
rep_list = []
#Cria a lista do denominador (se existirem letras repitidas)
denominador_list = []

numerador = len(palavra_lista)
denominador = 0

#Passa por todo o alfabeto e identifica as letras que aparecem na lista da palavra, contando o número de vezes que ela está na lista 
for i in alfabeto:
    rep = palavra_lista.count(i)
    if rep > 0:
        rep_list.append(rep)

#Cria uma lista do fatorial das letras que aparecem mais de uma vez
for i in rep_list:
    if i > 1:
        denominador_list.append(math.factorial(i))

#Cria o denominador, multiplicando todos os termos da lista de denominadores
if len(denominador_list) > 0:
    denominador = functools.reduce(lambda x, y: x*y, denominador_list)

#Faz a seleção da operação para cálculo de anagramas (com repetições e sem repetições)
if denominador > 0:
    qtd_anagramas = math.factorial(numerador)/denominador
else:
    qtd_anagramas = math.factorial(numerador)

#Imprime o resultado
print(f"A palavra {palavra} possui uma quantidade {qtd_anagramas:.0f} de anagramas.")


