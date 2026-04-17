numero = int(input("Informe um número: "))

if numero >= 0 and numero % 2 == 0:
    print(f"{numero} é um número par.")
elif numero >=0 and numero % 2 != 0:
    print(f"{numero} é um número ímpar.")
elif numero < 0:
    print("O valor absoluto/módulo de", numero, "é", numero * (-1) )
