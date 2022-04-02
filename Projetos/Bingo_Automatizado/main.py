"""
Uma cartela de BINGO consiste em 5 colunas de 5 números que são rotulados com as letras B, I, N, G e O.
Atenção: Google it, para quem nunca viu uma cartela dessas!

Existem 15 números que podem aparecer sob cada letra respeitando a regra abaixo.
- B -> números variando de 1 a 15  (inclusos)
- I -> números variando de 16 a 30 (inclusos)
- N -> números variando de 31 a 45 (inclusos)
- ... e assim por diante

Passo número 0:
- Escreva uma função que crie uma cartela de BINGO aleatória. Dica(podemos usar um dicionário!). 
- As chaves serão as letras B, I, N, G e O. 
- Os valores serão as listas de cinco números aleatórios respeitando a regra dos intervalos de cada letra. 

Passo número 1: 
- Escreva uma segunda função que exiba a cartela de BINGO com as colunas rotuladas apropriadamente
- Formate a saída no terminal para que a cartela seja impressa em forma de colunas (letras e seus valores abaixo)

Passo número 2: 
- Sorteie uma letra e número aleatório (respeitando a regra) e veja se a cartela contém aquele número.

Passo número 3:
- Sorteie 50 (letras e) números e verifique se a cartela é vencedora ou não.
- Uma cartela é vencedora quando preencher uma linha ou coluna inteira com números sorteados.

Passo número desafio:
- Simule 1.000 jogos que sorteiam TODOS os números até que uma mesma cartela seja preenchida e contabilize:
    * O número mínimo de sorteio para que a carteja seja vencedora (não necessariamente preencher toda a cartela!)
    * A média do número de sorteios para que a carteja seja vencedora
    * O número máximo de sorteios para que a cartela seja vencedora
"""
import cartela
import sorteio

#Simula 1000 jogos e appenda em uma lista a quantidade de sorteios, necessária para identificador o ganhador, em cada uma das ocasiões
lista_sorteios = list()
numero_sorteios = int(input("Digite a quantidade de sorteios desejada:\n>"))

while len(lista_sorteios) < numero_sorteios:
    #Gera cartela
    cartela_gerada = cartela.gera_cartela()
    
    #Atribuição dinâmica. recebe a cartela_1 atualizada ganhadora e a contagem de sorteios necessários para tal
    cartela_gerada, contagem_sorteios = sorteio.sorteia_cartelas(cartela_gerada)
    
    #Appenda a lista a quantidade de sorteios, para ser utilizado posteriormente na identificação do mínimo, máximo e para a média
    lista_sorteios.append(contagem_sorteios)
    

#Localiza o número mínimo, máximo e realizad a média de sorteios por jogo
minimo_sorteios = min(lista_sorteios)
maximo_sorteios = max(lista_sorteios)
media_sorteios = sum(lista_sorteios) / len(lista_sorteios)

#Print simples dos números adquiridos
print(f"Quantidade de cartelas sorteadas: {numero_sorteios}")
print(f"Quantidade mínima de sorteios para identificar um ganhador: {minimo_sorteios}")
print(f"Quantidade máxima de sorteios para identificar um ganhador: {maximo_sorteios}")
print(f"Média de sorteios por jogos: {media_sorteios}") 
