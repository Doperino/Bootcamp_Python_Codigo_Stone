"""
How Bootcamps - Stone - /código[s]
Data: 31/03/2022
Autor: Henrique Junqueira Branco
Enunciado: Construa um jogo da forca!
A palavra secreta é representada por uma linha de traços em cada letra da palavra. 
Esta pode vir de uma variável ou arquivo, como achar melhor.
Se o jogador que adivinha sugerir uma letra que ocorre na palavra, o programa a escreve em todas as posições corretas. 
Se a letra sugerida for incorreta, o programa deve mostrar isso de alguma forma (desenho, mensagem, etc.).
As tentativas (acertos e erros) são definidas em variáveis.
Quando se esgotarem as tentativas, o programa finaliza dizendo que o jogador perdeu e mostra a palavra correta.
Algumas funções, importações e variáveis foram pré-definidas para auxiliá-los!
"""

# from random import ?
import random
from utilities import STATUS, WORDS
import copy
from string import ascii_uppercase

def get_secret_word():
    """Devolve uma palavra aleatória de uma lista."""
    palavra = random.choice(WORDS).upper()
    return palavra
    ...


def print_game_board(error: int, attempts: int, correct_letters: list, secret_word: str, status: list) -> None:
    """Imprime a situação atual do jogo."""
    encoded_word = ''
    for letter in secret_word:
        if letter not in correct_letters:
            encoded_word += '_ '
        else:
            encoded_word += letter + ' '

    print(STATUS[error])
    print(encoded_word)
    return None
    


def read_input_player() -> str:
    """Lê uma letra do usuário."""
    while True:
        letter = str(input('Digite uma letra: ')).upper()
        while letter not in ascii_uppercase or len(letter) != 1:
            letter = str(input('Valores diferentes de letras ou palavras não são aceitos. Digite somente uma letra: ')).upper()
        return letter

        


def guess_letter(typped_letter: str, secret_word: str, correct_letters: list, missed_letters: list) -> bool:
    """Verifica se uma letra está na palavra secreta ou já foi jogada, seja certa ou errada."""
    while typped_letter in missed_letters or typped_letter in correct_letters:
        print('Essa letra já foi jogada, digite uma nova letra.')
        typped_letter = read_input_player()
    if typped_letter in secret_word:
        return True
    else:
        return False


def game_continue(error: int, attempts: int, correct_letters: list, secret_word: str, status: list) -> bool:
    """Função que decide se jogo já encerrou ou não."""
    if set(correct_letters) == set(secret_word):
        print("Você é um vencedor!")
        return False
    elif error == attempts:
        print(status[error])
        print(f"A palavra secreta é {secret_word}")
        return False
    else:
        return True



correct_letters = []  # variável que armazena as letras corretas já jogadas
missed_letters = []  # variável que armazena as letras incorretas já jogadas
error = 0  # erro inicial
attempts = 6  # tentativas

secret_word = get_secret_word()

while game_continue(error, attempts, correct_letters, secret_word, STATUS):
    print_game_board(error, attempts, correct_letters, secret_word, STATUS)
    typed_letter = read_input_player()
    if not guess_letter(typed_letter, secret_word, correct_letters, missed_letters):
        error += 1
        missed_letters.append(typed_letter)
    else:
        correct_letters.append(typed_letter)

    
