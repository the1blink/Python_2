valorOriginal = float(input("Digite o valor do produto: R$"))
formaDePagamento = int(input("""Você pode escolher a forma de pagamento, cada uma tem suas condições.
                              Se deseja pagar a vista ou no cheque com 10% de desconto, digite 1.
                                Se quiser pagar a vista no cartão com 5% de desconto, digite 2.
                                  Se quiser pagar em até 2x no cartão sem juros, digite 3.
                                    Se quiser pagar em 3x ou mais vezes no cartão com 20% de juros, digite 4: """))

chequeVista = valorOriginal - ((valorOriginal * 10) / 100)
cartaoVista = valorOriginal - ((valorOriginal *  5) / 100)
cartao2X = valorOriginal / 2


if formaDePagamento == 1:
    print(f"Pagando a vista ou no cheque, o preço final fica em R${chequeVista:.2f}")
elif formaDePagamento == 2:
    print(f"Pagando a vista no cartão, o preço final fica em R${cartaoVista:.2f}")
elif formaDePagamento == 3:
    print(f"Pagando em 2x no cartão sem juros, cada parcela fica em R${cartao2X:.2f}")
elif formaDePagamento == 4:
    vezes = int(input("Digite em quantas vezes quer pagar: "))
    cartao3xMais = (valorOriginal + ((valorOriginal * 20) / 100)) / vezes
    cartao3xMaisTotal = (valorOriginal + ((valorOriginal * 20) / 100))
    print(f"Pagando em {vezes}x com 20% de juros, cada parcela fica em R${cartao3xMais} e o preço final aumenta para R${cartao3xMaisTotal}")

