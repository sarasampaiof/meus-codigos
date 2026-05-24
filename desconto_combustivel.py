litros_abastecidos = int(input("Informe a quantidade de litros abastecidos: "))
tipo_combustivel = int(input("Digite o código do tipo de combustível usado, sendo 1 para álcool e 2 para gasolina: "))
preco_combustivel = float(input("Informe o preço do litro do combustível: "))

if tipo_combustivel == 1 and litros_abastecidos <= 20:
    valor_final = 0.97 * litros_abastecidos * preco_combustivel
    print(f"Valor a ser pago: R${valor_final:.2f}. ")

elif tipo_combustivel == 1 and litros_abastecidos > 20:
    valor_final = 0.95 * litros_abastecidos * preco_combustivel
    print(f"Valor a ser pago: R${valor_final:.2f}. ")
    
elif tipo_combustivel == 2 and litros_abastecidos <= 20:
    valor_final = 0.965 * litros_abastecidos * preco_combustivel
    print(f"Valor a ser pago: R${valor_final:.2f}. ")
        
elif tipo_combustivel == 2 and litros_abastecidos > 20:
    valor_final = 0.94 * litros_abastecidos * preco_combustivel
    print(f"Valor a ser pago: R${valor_final:.2f}. ")
