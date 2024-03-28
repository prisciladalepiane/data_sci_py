import random as rd
import regex as re
from os import system

system('cls')

def jogo():

    system('cls')
    print("Jogo da Foca:")
    print("Adivinhe a palavra abaixo:\n")

    palavras = ['chocolate', 'morango', 'pastel', 'queijo', 'macarrao']

    palavra = rd.choice(palavras)

    n = len(palavra)

    #List comprehencion
    letras_descobertas = ['_' for letra in palavra]

    chances = 10

    acertos = 0

    letras_erradas = []

    while chances > 0:
        system('cls')
        print(" ".join(letras_descobertas))
        print("Chances restantes:", chances)
        print("Letras erradas:",  " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:


            posicao = [match.start() for match in re.finditer(tentativa, palavra)]
            
            for l in posicao:
                letras_descobertas[l] = tentativa
            
            acertos += len(posicao)
                       
            if acertos >= n:
                print("\n****** FIM DE JOGO*********")
                print("VOCÊ ACERTOU! =D a palavra é:", palavra)
                break

        else:
            letras_erradas.append(tentativa)
            chances -= 1
    else: 
        print("\n****** FIM DE JOGO********")
        print("VOCÊ PERDEU! a palavra era:", palavra)



jogo()









