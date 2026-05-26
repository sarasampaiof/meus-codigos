numero = int(input("Insira um número: "))
quantidade_nums = 0

for numero in range(1, numero + 1):
    if numero % 2 == 0:
        print(numero)
        quantidade_nums += 1
print(f"A quantidade de números apresentados é: {quantidade_nums}.")
