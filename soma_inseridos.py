soma = 0
numero = int(input("Insira número ('0' para parar): "))

while True:
    numero = int(input("Insira número: "))
    soma += numero
    
    if numero == 0:
        break

print(f"A soma dos números inseridos é: {soma}.")
