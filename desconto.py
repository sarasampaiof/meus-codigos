produto = input("Escreva o nome do produto: ")
preço = float(input("Informe o preço do produto: "))
com_desconto = 0.9 * preço

print(f"Você comprou um produto {produto} por R${preço:.2f} e acaba de ganhar um desconto de 10%. Assim, você vai pagar apenas R${com_desconto:.2f} pelo seu produto. Volte sempre!")
