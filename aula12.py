from colorama import Fore

nome = str(input(Fore.WHITE + "Digite seu nome: ")).capitalize()

if nome == "Matheus":
    print(f"Que nome bacana, {Fore.RED + nome}.{Fore.WHITE} Prazer em te conhecer.")
elif nome == "Larissa":
    print(f"{Fore.MAGENTA + nome} {Fore.WHITE}é nome de mulher bonita.")
else:
    print(f"{Fore.RED + nome}?{Fore.WHITE} Seu nome podia ser mais legal, mas serve. Prazer em te conhecer!")
