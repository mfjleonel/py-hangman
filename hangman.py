import argparse, random, subprocess, sys

words = ['farinha', 'pássaro', 'igreja', 'maçã', 'banana', 'laranja']


def game(word):
    preserved_word = word
    list_word = ['_' for a in word]
    life = 5
    guess = ''

    while ''.join(list_word) != preserved_word and life > 0:
        if sys.platform =='win32':
            subprocess.call("cls", shell=True)
        else:
            subprocess.call("clear", shell=True)
        
        life_hash = ['#' for l in range(life)]
        print(word)
        print(f"Tentativas restantes: {' '.join(life_hash)} \n")
        print(f"{' '.join(list_word)}")

        guess = input("> Digite uma letra, ou mais de uma para tentar advinhar a palavra. Digite 'quit' a qualquer momento, para sair. \n")
        guess = guess.lower()

        if guess == 'quit':
            break
        elif len(guess)>1 and guess!='quit':
            if guess == preserved_word:
                print("Parabéns!")
            else:
                life = 0
            
        else:
            if guess in word:
                for char in word:
                    if char == guess:
                        list_word[word.index(char)] = char
                        word = word.replace(char,'X', 1)
            else:
                life -= 1
    if life == 0:
        
        print("Você perdeu! Boa sorte na próxima.")
    else:
        print("Parabéns, você conseguiu!")


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lenght', default='*', help="Escolhe o tamanho das palavras")
    return parser.parse_args()

args = get_args()

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

print(choosen_word)
game(choosen_word)

        



