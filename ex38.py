from colorama import Fore

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O primeiro número ({Fore.YELLOW}{num1}{Fore.WHITE}) é maior que o segundo ({Fore.LIGHTBLUE_EX}{num2}{Fore.WHITE}).")
elif num1 < num2:
    print(f"O primeiro número ({Fore.LIGHTBLUE_EX}{num1}{Fore.WHITE}) é menor que o segundo ({Fore.YELLOW}{num2}{Fore.WHITE}).")
elif num1 == num2:
    print(f"{Fore.LIGHTGREEN_EX}Os dois números são iguais.{Fore.WHITE}")