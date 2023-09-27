from colorama import Fore

idade = int(input("Digite sua idade: "))
jovem = 18 - idade
velho = idade - 18

if idade < 18:
    print(f"{Fore.LIGHTBLUE_EX}Você é muito novo para se alistar.{Fore.WHITE} Lembre-se que daqui {Fore.LIGHTRED_EX}{jovem}{Fore.WHITE} anos você terá de se apresentar no quartel.")
elif idade == 18:
    print(f"{Fore.LIGHTGREEN_EX}Você tem 18 anos, está na hora de se alistar.{Fore.WHITE}")
else:
    print(f"{Fore.YELLOW}Você já passou da idade de alistamento obrigatório.{Fore.WHITE} Já se passaram {Fore.YELLOW}{velho} {Fore.WHITE}anos desde seu ano de alistamento.")