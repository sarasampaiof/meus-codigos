nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media_ponderada = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10 #soma das notas multiplicadas por seus pesos, dividido pela soma dos pesos

print(f"A média das notas é {media_ponderada}")
