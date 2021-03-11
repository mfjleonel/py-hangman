import argparse
import random
import subprocess
import sys
import unidecode

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lenght', default='*', help="Escolhe qual tamanho a palavra deve ter, entre 4-12.")
    parser.add_argument('-w', '--word', help="Especifíca a palavra a ser usada.")

    return parser.parse_args()


def gen_word():
    global args
    choosen_word = random.choice(words)

    if args.lenght != '*':
        try:
            lenght = int(args.lenght)
            if lenght > 12 or lenght < 4:
                raise(ValueError)
            else:
                while len(choosen_word) != lenght:
                    choosen_word = random.choice(words)

        except ValueError:
            print("> Deve-se passar um número entre 4 e 12 como argumento para 'lenght'.")
    return choosen_word.lower()


def show():
    if sys.platform == 'win32':
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

    life_hash = ['#' for l in range(life)]
    print(f"Tentativas restantes: {' '.join(life_hash)} \n")
    print(f"{' '.join(list_word)} \n")


def game():
    global life
    global list_word

    word_alt = word.lower()
    guess = ''
    while ''.join(list_word) != word and life > 0:
        show()
        guess = input("> Digite uma letra, ou mais de uma para tentar advinhar a palavra. Digite 'quit' a qualquer momento, para sair. \n")
        guess = guess.lower()

        if guess == 'quit':
            break
        elif len(guess) > 1 and guess != 'quit':
            if unidecode.unidecode(guess) == unidecode.unidecode(word):
                list_word = [l for l in word]
                break
            else:
                life = 0

        else:
            if guess in word_alt:
                for char in word_alt:
                    if unidecode.unidecode(char) == unidecode.unidecode(guess):
                        list_word[word_alt.index(char)] = char
                        word_alt = word_alt.replace(char, 'X', 1)
            else:
                life -= 1
    
    show()
    if life == 0:
        print("Você perdeu! Boa sorte na próxima.")
    else:
        print("Parabéns, você conseguiu!")


words = ['farinha', 'pássaro', 'igreja', 'maçã', 'banana', 'laranja', 'pera', 'mamão', 'graça', 'Deus', 'amor', 'vídeo','espada', 'livro','paralelo', 'linha', 'tempo', 'vida','triste', 'lírio']
life = 5
args = get_args()
if args.word == None:
    word = gen_word()
else:
    word = args.word
list_word = ['_' for a in word]
game()