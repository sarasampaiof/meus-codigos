potencia = int(input("Informe a potência do aparelho em watts: "))
horas = int(input("Informe por quantas horas ele fica ligado por dia: "))
dias = int(input("Informe o número de dias de uso no mês: "))

kwh = (potencia * horas * dias) / 1000

print(f"O consumo mensal é de {kwh} kWh.")
