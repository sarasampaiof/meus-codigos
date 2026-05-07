folhas = int(input("Informe o número de folhas: "))

if folhas <= 100:
    print(f"O valor total a ser pago é de R${folhas * 0.25:.2f}.")
else:
    folhas = 100 * 0.25 + (folhas - 100) * 0.20
    print(f"O valor total a ser pago é de R${folhas:.2f}.")
