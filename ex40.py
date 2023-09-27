from colorama import Fore
from math import floor, ceil


nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = ((nota1 + nota2) / 2)

print(f"MÉDIA: {media}")

if media < 5.0:
    print(f"{Fore.RED}REPROVADO{Fore.WHITE}")
elif  5.0 <= media <= 6.99:
    print(f"{Fore.YELLOW}RECUPERAÇÃO{Fore.WHITE}")
else:
    print(f"{Fore.LIGHTGREEN_EX}APROVADO{Fore.WHITE}")