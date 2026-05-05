saque = int(input("Informe o valor do saque (retire um valor múltiplo de 5): "))

cedulas_100 = saque // 100
saque %= 100 #atualiza a variável c/ esse valor, que é o que sobra p/ calcular o resto

cedulas_50 = saque // 50
saque %= 50

cedulas_20 = saque // 20
saque %= 20

cedulas_10 = saque // 10
saque %= 10

cedulas_5 = saque // 5
saque %= 5

print(f"Você receberá {cedulas_100} cédulas de 100 reais, {cedulas_50} cédulas de 50 reais, {cedulas_20} cédulas de 20 reais, {cedulas_10} cédulas de 10 reais e {cedulas_5} cédulas de 5 reais.")
