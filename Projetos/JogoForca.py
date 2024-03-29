import random as rd
import regex as re
from os import system

system('cls')

def jogo(palavras):

    # Variaveis
    palavra = rd.choice(palavras)
    letras_descobertas = ['_' for letra in palavra]
    chances = 10
    acertos = 0
    letras_erradas = []

    system('cls')
    print("Jogo da Foca:")
    print("Adivinhe a palavra abaixo:\n")


    while chances > 0:
        system('cls')
        print(" ".join(letras_descobertas))
        print("Chances restantes:", chances)
        print("Letras erradas:",  " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:

            posicao = [match.start() for match in re.finditer(tentativa, palavra)]
            
            if tentativa not in letras_descobertas:
              acertos += len(posicao)

            for l in posicao:
              letras_descobertas[l] = tentativa
                       
            if acertos >= len(palavra):
                print("\n****** FIM DE JOGO*********")
                print("VOCÊ ACERTOU! =D a palavra é:", palavra)
                break

        elif tentativa not in letras_erradas:
            letras_erradas.append(tentativa)
            chances -= 1
    else: 
        print("\n****** FIM DE JOGO********")
        print("VOCÊ PERDEU! a palavra era:", palavra)



palavras = ['chocolate', 'morango', 'pastel', 'queijo', 'macarrao']

jogo(palavras)









