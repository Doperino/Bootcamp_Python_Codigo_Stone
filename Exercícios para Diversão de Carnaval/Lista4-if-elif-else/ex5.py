"""
Escreva um programa que receba uma string e diga se ela tem o formato de uma placa veicular brasileira (no formato antigo) com três letras, um traço e quatro números. Exemplos: 
•	Dada a entrada ABT-1234 o programa deveria exibir True
•	Dada a entrada JKL9999 o programa deveria exibir False
•	Qualquer outra entrada que fuja do padrão de 3 letras, um traço e quatro números, o programa deverá exibir False 

"""
import string #Importa a biblioteca string

alfabeto = []
alfabeto = list(string.ascii_uppercase) #List cria uma list dos elementos iteráveis dentro do parênteses. 
                                        #string.ascii_uppercase retorna uma string das letras de todo o alfabeto em maiúsculo

naturais = [num for num in range(10)]

def valida_placa():
    placa = str(input('>'))
    while len(placa) < 8 | len(placa) > 8:
        print("Quantidade de caracteres inválida, digite novamente:")
        placa = str(input('>'))
    return placa

#print("Digite a placa do seu veículo:")
placa = valida_placa()

if '-' in placa:
    placa = placa.split('-')
    if len(placa[0]) == 3 and len(placa[1]) == 4:
        if placa[0].isalpha() and placa[1].isnumeric():
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)