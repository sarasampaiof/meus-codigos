capacidade = float(input("Informe a capacidade em litros do tanque: "))
litros_abastecidos = float(input("Informe a quantidade de litros abastecidos: "))
km_rodados = float(input("Informe a quantidade de quilômetros rodados desde o último abastecimento total do tanque: "))

consumo_medio = km_rodados / litros_abastecidos #unidade km/L
autonomia_veiculo = consumo_medio * capacidade #é a distância máxima em km que um veículo pode percorrer com o tanque cheio

print(f"O consumo médio do veículo é {consumo_medio} e sua autonomia é {autonomia_veiculo}")
