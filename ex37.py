from colorama import Fore

num = int(input("Digite um número: "))
b2 = bin(num)
b8 = oct(num)
b16 = hex(num)

conversor = int(input(f"Para qual base você quer converter? Digite {Fore.LIGHTBLUE_EX}'2' para binário, {Fore.LIGHTGREEN_EX}'8' para octal, {Fore.WHITE}e {Fore.YELLOW}'16' para hexadecimal:{Fore.WHITE} "))

if conversor == 2:
    print(f"Convertido para valores binários, o número {Fore.RED}{num} {Fore.WHITE}equivale à {Fore.LIGHTBLUE_EX}{b2}{Fore.WHITE}")
elif conversor == 8:
    print(f"Convertido para valores octais, o número {Fore.RED}{num} {Fore.WHITE}equivale à {Fore.LIGHTGREEN_EX}{b8}{Fore.WHITE}")
elif conversor == 16:
    print(f"Convertido para valores hexadecimais, o número {Fore.RED}{num} {Fore.WHITE}equivale à {Fore.YELLOW}{b16}{Fore.WHITE}")
else:
    print(f"CÓDIGO DE CONVERSÃO {Fore.RED}INVALIDO.{Fore.WHITE} Por favor, digite {Fore.LIGHTBLUE_EX}'2' para binário, {Fore.LIGHTGREEN_EX}'8' para octal, {Fore.WHITE}e {Fore.YELLOW}'16' para hexadecimal.{Fore.WHITE}")