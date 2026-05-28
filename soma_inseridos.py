soma = 0

while True:
    numero = int(input("Insira número ('0' para parar): "))
    soma += numero
    
    if numero == 0:
        break

print(f"A soma dos números inseridos é: {soma}.")
