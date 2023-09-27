for c in range (10, 0, -2): # Ao pôr o terceiro parâmetro "-" alguma coisa, ele repete de trás pra frente no range.
    print(c)
print("FIM")

n = int(input("Digite um número: "))

for c in range (0, n+1): # Esse n+1 é só para que o contador termine de contar até o de fato número inputado, ao invés de cortar o último.
    print(c)
print("FIM")

inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("De quanto em quanto: "))

for c in range(inicio, fim, passo): # É possível fazer isso com variáveis inputaveis, o que torna o programa dinâmico.
    print(c)
print("FIM")
