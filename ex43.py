from colorama import Fore

peso = float(input("Calcularei seu IMC. Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f"Seu IMC é {Fore.YELLOW}{imc:.2f}{Fore.WHITE} , e você está {Fore.LIGHTMAGENTA_EX}abaixo do peso saudável{Fore.WHITE}.")
elif imc >= 18.5 and  imc <= 24.9:
    print(f"Seu IMC é {Fore.YELLOW}{imc:.2f}{Fore.WHITE} , e você está em seu {Fore.LIGHTGREEN_EX}peso ideal{Fore.WHITE}.")
elif imc >= 25 and imc <= 29.9:
    print(f"Seu IMC é {Fore.YELLOW}{imc:.2f}{Fore.WHITE} , e você está em {Fore.LIGHTYELLOW_EX}sobrepeso{Fore.WHITE}.")
elif imc >= 30 and imc <= 39.9:
    print(f"Seu IMC é {Fore.YELLOW}{imc:.2f}{Fore.WHITE} , e você está {Fore.LIGHTRED_EX}obeso{Fore.WHITE}.")
elif imc >= 40:
    print(f"Seu IMC é {Fore.YELLOW}{imc:.2f}{Fore.WHITE} , e você está {Fore.RED}morbidamente obeso,{Fore.WHITE} procure um médico.")