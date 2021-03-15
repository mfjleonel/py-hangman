# py-hangman

Esse é um dos meus primeiros projetos em python, e mira, não só em me ajudar através do processo de aprendizado, mas em entregar um jogo da forca simples, como o nome já sugere.  
No momento, todo texto e UI está em português, mas planejo acrescentar a possibilidade do jogador escolher a linguagem que quer.  
Para jogar, você precisará do python3 instalado, e basta usar "python3 hangman.py", mas você também pode passar alguns argumentos:  

### --length, -l
Length significa "tamanho", logo, com esse argumento você pode indicar para o programa o tamanho da palavra que quer.

### --word, -w
Passando esse argumento você pode especificar a exata palavra a ser usada, o programa, então, pula direto para o jogo. É útil, quando se está jogando com outra pessoa, por exemplo.

### --inputlist, -i
Usa uma lista externa para obter e sortear as palavras. O arquivo de texto deve ter uma palavra por linha.

### --help, -h
Mostra a mensagem de ajuda padrão gerada pelo argparse do python.

### Exemplos:
python3 hangman.py -w exemplo      
python3 hangman.py --word guarda-chuva  
python3 hangman.py -i './palavras.txt'  
python3 hangman.py -i '/home/usuario/palavras.txt' -l 6  
