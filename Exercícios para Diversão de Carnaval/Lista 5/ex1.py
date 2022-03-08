"""
Implemente um jogo em que o usuário tenha que adivinhar um número sorteado pelo computador.

1.	O jogo deve sortear um número entre 1 e 100.
2.	O usuário deve informar um número. O número informado pelo usuário deve ser validado: não pode ser inferior a 1 ou superior a 100. 
Enquanto o usuário informar um número inválido, o jogo deve solicitar a entrada de um novo número.
3.	O número do usuário deve ser analisado:
a.	Caso o usuário informe um número inferior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é maior.”.
b.	Caso o usuário informe um número superior ao número sorteado, o jogo deve apresentar a mensagem “O número sorteado é menor.”.
c.	Caso o usuário informe um número igual ao número sorteado, o jogo deve apresentar a mensagem “Parabéns! Você acertou o número sorteado” e o jogo deve ser finalizado, 
sendo apresentado ao usuário a quantidade de tentativas efetuadas até este momento.
4.	Ao final do jogo, deve-se questionar o usuário se ele deseja jogar novamente. Caso afirmativo, todo o processo deve ser repetido. 
Caso contrário, o jogo deve ser encerrado.

Dica!
Pesquise sobre o módulo buit-in do Python chamado random

"""
import random

resp_sim = ['s', 'si', 'sim', 'y', 'ye', 'yes']

def valida_num():
    while True:
        try:
            num = int(input('>'))
            while num < 1 or num > 100:
                num = int(input('Número inválido, digite novamente:\n>'))
            return num
        except ValueError:
            print("Valor inválido, digite um número inteiro entre 1 e 100:")


def opera_jogo():
    num_premio = random.randrange(1, 100)
    print("Digite o número desejado:")
    num = 0
    tentativas = 0

    while True:
        num = valida_num()
        tentativas += 1
        if num == num_premio:
            print(f"Parabéns! Você acertou o número sorteado com um número de {tentativas} tentativas!")
            resposta = str(input("Deseja jogar novamente? Digite sim para continuar ou não para encerrar o jogo:\n>"))
            return resposta
        elif num > num_premio:
            print("O número digitado é maior que o número sorteado! Tente novamente.")
        elif num < num_premio:
            print("O número digitado é menor que o número sorteado! Tente novamente.")

resposta = 'sim'
while resposta in resp_sim:
    resposta = opera_jogo()

