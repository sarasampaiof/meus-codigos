distancia = float(input("Informe a distância total percorrida em quilômetros: "))
combustivel = float(input("Informe a quantidade de combustível gasta em litros: "))
preco_combustivel = float(input("Informe o preço do litro do combustível: "))

consumo_medio = distancia / combustivel
custo_total = combustivel * preco_combustivel

print(f"O consumo médio do veículo é {consumo_medio} km/L e o custo total da viagem é de R${custo_total:.2f}.")
