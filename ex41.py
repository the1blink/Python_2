from colorama import Fore

idade = int(input("Digite sua idade: "))

mirim = idade <= 9
infantil = 9 < idade <= 14
junior = 14 < idade <= 19
senior = idade == 20
master = idade > 20

if idade <= 9:
    print(f"Atleta {Fore.LIGHTBLUE_EX}MIRIM{Fore.WHITE}")
elif 9 < idade <= 14:
    print(f"Atleta {Fore.LIGHTGREEN_EX}INFANTIL{Fore.WHITE}")
elif 14 < idade <= 19:
    print(f"Atleta {Fore.LIGHTYELLOW_EX}JUNIOR{Fore.WHITE}")
elif idade == 20:
    print(f"Atleta {Fore.LIGHTMAGENTA_EX}SENIOR{Fore.WHITE}")
elif idade > 20:
    print(f"Atleta {Fore.RED}MASTER{Fore.WHITE}")