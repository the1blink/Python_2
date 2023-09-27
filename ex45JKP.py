from time import sleep
import random
from colorama import Fore, Back



jogadasPossiveis = ["pedra", "papel", "tesoura"]
continuarJogando = True

while continuarJogando:
    playerIsready = input("Vamos jogar Jo-ken-po? Digite 's' para sim e 'n' para não: ").lower().strip()
    if playerIsready == 'n':
        print("Catapimbas, fica pra mais tarde então... 😔")
        break
    elif playerIsready == 's':
        while True:
            comecarJogo = int(input("Supimpa! Digite '1' para começar! "))
            escolhaDoBot = random.choice(jogadasPossiveis)

            def escolhaDoJogador():
                escolha = input("Escolha uma jogada: 'Pedra', 'Papel' ou 'Tesoura': ").lower()
                if escolha in jogadasPossiveis:
                    return escolha
                else:
                    print("Escolha inválida, tente novamente")
                    return escolhaDoJogador()

            escolhaDoUsuario = escolhaDoJogador()   

            def disputa():
                print("JO")
                sleep(0.7)
                print("KEN")
                sleep(0.7)
                print("PÔ")
                sleep(0.7)
                if escolhaDoUsuario == escolhaDoBot:
                    print(f"Computador jogou {escolhaDoBot}. EMPATE")
                elif escolhaDoUsuario == "pedra" and escolhaDoBot == "tesoura" or \
                escolhaDoUsuario  == "papel" and escolhaDoBot == "pedra" or \
                escolhaDoUsuario == "tesoura" and escolhaDoBot == "papel":
                    print(f"Computador escolheu {escolhaDoBot}. Jogador vence!")
                else:
                    print(f"Computador escolheu {escolhaDoBot}. CPU vence!")

            disputa()
            
            while True:  
                replay = input("Quer jogar de novo? 'S' para sim e 'N' para Não: ").lower().strip()
                if replay == "n":
                    continuarJogando = False
                    break
                elif replay == "s":
                    break
                else:
                    print("Comando inválido, tente novamente.")
                    
    else:
        print(f"'{playerIsready}' não é um comando válido, tente novamente: ")
