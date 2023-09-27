from colorama import Fore

a = int(input("Verificarei se um triângulo é possível e, se é, qual o seu tipo. Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

triangulo = [a, b, c]

if a + b > c and b + c > a and a + c > b and a - b < c and b - c < a and a - c < b:
    triangulo = True
else:
    triangulo = False


if triangulo == False:
    print(f"Esse triângulo é matematicamente {Fore.RED}IMPOSSÍVEL.{Fore.WHITE}")
elif triangulo == True and a != b != c and a != c:
    print(f"Esse triângulo é {Fore.YELLOW}ESCALENO.{Fore.WHITE}")
elif triangulo == True and (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
    print(f"Esse triângulo é {Fore.YELLOW}ISÓSCELES.{Fore.WHITE}")
elif triangulo == True and a == b == c and a == c:
    print(f"Esse triangulo é {Fore.YELLOW}EQUILÁTERO.{Fore.WHITE}")
