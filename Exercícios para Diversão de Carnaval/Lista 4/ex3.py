"""
A tabela a seguir lista os níveis sonoros em decibéis para alguns barulhos comuns

Barulho	Nível sonoro (dB)
Britadeira	130
Cortador de grama	106
Despertador	70
Cômodo em silêncio	40


Escreva um programa que leia um valor de nível sonoro do usuário em decibéis. Se o valor for um dos que estão na tabela, o programa deve retornar aquele barulho. 
Caso o número esteja entre algum dos valores da tabela, o programa deve dizer entre quais barulhos o valor digitado está. 
Seu programa deve informar também quando o valor for menor que o ruído mínimo da tabela e maior que ruído máximo. 

"""

britadeira = 130
cortador_de_grama = 106
despertador = 70
silencio = 40

#Cria uma lista das chaves e valores, a partir do dict dos barulhos
barulhos = {'britadeira': 130, 'cortador_de_grama': 106, 'despertador': 70, 'silencio': 40}
barulhos_keys = list(barulhos)
barulhos_values = list(barulhos.values())

#Validador do número, aproximando para o inteiro mais próximo
def valida_num():
    while True:
        try:
            num = float(input('>'))
            return round(num) 
        except ValueError:
            print("Digite um número válido:")

print("Digite o nível sonoro em decibéis (parte fracionária será arredondada):")
qtd_db = valida_num()

#Se qtd_db estiver nos valores dos barulhos, ele retornará o responsável pelo barulho
if qtd_db in barulhos_values:
    for barulho, decibeis in barulhos.items():
        if qtd_db == barulhos[barulho]:
            print(f"Responsável pelo barulho: {barulho}")
#Caso contrário, serão analisados os intervalos
else:
        if qtd_db > 130:
            print("O barulho é maior que o limte máximo.")
        elif qtd_db > 106 and qtd_db < 130:
            print(f"O barulho está entre {barulhos_keys[0]} e {barulhos_keys[1]}")
        elif qtd_db > 70 and qtd_db < 106:
            print(f"O barulho está entre {barulhos_keys[1]} e {barulhos_keys[2]}")
        elif qtd_db > 40 and qtd_db < 70:
            print(f"O barulho está entre {barulhos_keys[2]} e {barulhos_keys[3]}")
        else:
            print("O barulho está abaxo do limite mínimo.")