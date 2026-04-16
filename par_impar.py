numero = int(input("Informe um número: "))

if numero >= 0 and numero % 2 == 0:
    print(f"{numero} é um número PAR.")
elif numero >=0 and numero % 2 != 0:
    print(f"{numero} é um número ÍMPAR.")
