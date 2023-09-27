pesos = []

for c in range (0, 5):
    peso = int(input("Digite seu peso: "))
    pesos.append(peso)
print(f"Dentre esses pesos, o menor é {min(pesos)}kg, e o maior é {max(pesos)}kg.")

