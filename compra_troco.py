nome_produto = input("Escreva o nome do produto: ")
preço = float(input("Informe o preço do produto: "))
valor_entregue = float(input("Informe o valor em dinheiro entregue ao vendedor: "))
troco = valor_entregue - preço

print(f"Você comprou um produto {nome_produto} por R${preço:.2f} e entregou ao vendedor R${valor_entregue:.2f} em dinheiro. Você vai receber R${troco:.2f} de troco. Volte sempre!")
