# Jogo da Forca
# Programação Orientada a Objetos

# Importar pacotes
import random as rd
from os import system

# Board (tabuleiro)
board = ['''

>>>>>>>>>> Jogo da Forca <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

palavras = ['chocolate', 'morango', 'pastel', 'queijo', 'macarrao']

# Classe
class JogoForca:

	# Construtor
    def __init__(self, palavra):
       self.palavra = palavra
       self.letras_descobertas = []
       self.letras_erradas = []

    def adivinharPalavra(self, letra):

        if letra in self.palavra and letra not in self.letras_erradas:
            self.letras_descobertas.append(letra)
        elif letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        

    def palavraDescoberta(self):
        palavra_descoberta = ''

        for letra in self.palavra:
            if letra not in self.letras_descobertas:
                palavra_descoberta += '_'
            else:
                palavra_descoberta += letra
        return palavra_descoberta
                
    def fimJogo(self):
        return not self.ganhouJogo() and not self.perdeuJogo()

    def ganhouJogo(self):
       if '_' not in self.palavraDescoberta():
           return True
       return False
    
    def perdeuJogo(self):
        return len(self.letras_erradas) == 6 
        

	# Método para checar o status do game e imprimir o board na tela
    def statusJogo(self):
        if self.ganhouJogo():
            print("Você ganhou o jogo, a palavra é: ", self.palavra)
        elif self.perdeuJogo: 
            print("Você perdeu o jogo, a palavra era: ", self.palavra)

jogo = JogoForca(rd.choice(palavras))


while jogo.fimJogo():

    system('cls')
    print("Jogo da Foca:")
    print("Adivinhe a palavra abaixo:\n")
    print(board[len(jogo.letras_erradas)])
    print(jogo.palavraDescoberta())
    print("Letras erradas:", jogo.letras_erradas)
    tentativa = input("\nDigite uma letra: ").lower()
    jogo.adivinharPalavra(tentativa)

else:
    print(board[len(jogo.letras_erradas)])
    print("Fim de jogo")
    jogo.statusJogo()
    

