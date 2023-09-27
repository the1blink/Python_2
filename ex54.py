menores = []
maiores = []

for c in range (0, 7):
    ano = int(input("Digite um ano de nascimento: "))
    if 2023 - ano < 18:
        print("Menor de idade.")
        menores.append(c)
    else:
        print("Maior de idade.")
        maiores.append(c)
print(f"Nesse lista, {len(menores)} são menores de idade, enquanto {len(maiores)} são maiores de idade.")
