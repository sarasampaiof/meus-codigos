numero = int(input("Informe um número: "))

if numero % 2 == 0 or numero % 7 == 0:
    print(f"{numero} é divisível por 2 ou por 7")
else:
    print(f"{numero} não é divisível por 2 e nem por 7")
