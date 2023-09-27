nomes = []
idades = []
idadeHomemMaisVelho = 0
nomeHomemMaisVelho = ""
maisNovaQue20 = 0


for c in range (4):
    nome = str(input("Digite seu nome: ")).strip().lower()
    nomes.append(nome)
    idade = int(input("Digite sua idade: "))
    idades.append(idade)
    sexo = str(input("Digite 'M' para homem e 'F' para mulher: ")).lower().strip()

    if sexo == "m" and idade > idadeHomemMaisVelho:
        idadeHomemMaisVelho = idade
        nomeHomemMaisVelho = nome
    if sexo == "f" and idade < 20:
        maisNovaQue20 += 1
media = sum(idades) / len(idades)

print(f"A média das idades é: {media:.2f}")
print(f"O nome do homem mais velho é {nomeHomemMaisVelho.capitalize()} e ele tem {idadeHomemMaisVelho} anos de idade.")
print(f"Quantidade de mulheres com menos de 20 anos: {maisNovaQue20}")
 