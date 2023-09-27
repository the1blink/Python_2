frase = str(input("Digite uma frase e checarei se é um palíndromo: ")).strip().upper()
fraseSemEspaco = frase.replace(" ", "")
fraseInvertida = fraseSemEspaco[::-1]

if fraseSemEspaco == fraseInvertida:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")

print(fraseSemEspaco)
