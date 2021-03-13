import argparse
import random
import subprocess
import sys
import unidecode
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lenght', default='*', help="Escolhe qual tamanho a palavra deve ter.")
    parser.add_argument('-w', '--word', help="Especifíca a palavra a ser usada.")
    parser.add_argument('-i', '--inputlist', help="Determina um arquivo listando as palavras a serem sorteadas, uma em cada linha.")
    return parser.parse_args()


def gen_word(input_list):
    global args
    words = ['farinha', 'pássaro', 'igreja', 'maçã', 'banana', 'laranja', 'pera', 'mamão', 'graça', 'Deus', 'amor', 'vídeo','espada', 'livro','paralelo', 'linha', 'tempo', 'vida','triste', 'lírio']
    choosen_word = ''
    if input_list:
        try:
            with open(args.inputlist) as ilist:
                data = ilist.read()
                words = [w for w in data.replace(' ','').splitlines() if w != '']
        except (IsADirectoryError, FileNotFoundError):
            wait = input("Não foi possível acessar arquivo ou diretório. Por favor, confira o caminho indicado e se você tem as permissões necessárias para acessá-lo.\n> Pressione enter para sortear entre as palavras padrões ou digite 'quit' para sair...\n")
            if wait == 'quit':
                exit()
        except:
            print("Alguma coisa aconteceu, mas não consigo determinar a fonte do erro. Abortando o programa!")
            exit()

    if args.lenght != '*':
        try:
            possible = False
            lenght = int(args.lenght)
            for w in words:
                if len(w) == lenght:
                    possible = True
            if possible == False:
                raise(ValueError)
            else:
                while len(choosen_word) != lenght:
                    choosen_word = random.choice(words)

        except ValueError:
            print(f'Não foi possível achar uma palavra com {lenght} letras na lista.')
            wait = input(f"> Pressione enter para escolher uma palavra de qualquer tamanho, ou 'quit' para sair...\n")
            if wait == 'quit':
                exit()
            choosen_word = random.choice(words)
            
    else:
        choosen_word = random.choice(words)

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
        print(f'Você perdeu! Boa sorte na próxima. A palavra era: {word}')
    else:
        print('Parabéns, você conseguiu!')


life = 5
args = get_args()

if not args.word:
    input_list = False
    if args.inputlist:
        input_list = True
    word = gen_word(input_list)
else:
    word = args.word
        
list_word = ['_' for a in word]
game()