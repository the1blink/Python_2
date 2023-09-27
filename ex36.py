from colorama import Fore

valor_casa = float(input("Digite o valor da casa 🏠: "))
salario_comprador = float(input("Digite seu salário 💸: "))
tempo_de_pagamento = int(input("Digite em quantos anos você pretende pagar essa casa ⌛: "))

meses = tempo_de_pagamento * 12
prestacoes = valor_casa / meses
limite30 = salario_comprador * 30 / 100

if prestacoes > limite30:
    print(f"Seu empréstimo foi {Fore.RED}NEGADO {Fore.WHITE}pois o valor das prestações (R${prestacoes:.2f}) ultrapassam 30% do seu salário.")
else:
    print(f"Seu empréstimo foi {Fore.BLUE}APROVADO. {Fore.WHITE}O valor das prestações ficará em {Fore.GREEN}R${prestacoes:.2f}\n{Fore.WHITE} por {meses} meses, ou {meses / 12} anos e {meses % 12} meses.")
