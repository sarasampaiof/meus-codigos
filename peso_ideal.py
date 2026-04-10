altura = float(input("Informe a altura: "))
genero = input("Informe o gênero (M / F): ")

if genero == "M" or genero == "m": #apenas digitações diferentes
    print(f"Seu peso ideal é {72.7 * altura - 58:.2f}")

elif genero == "F" or genero == "f":
    print(f"Seu peso ideal é {62.1 * altura - 44.7:.2f}")
