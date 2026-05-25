salario = float(input("Informe o valor do seu salário em reais: "))
if salario < 0:
    print("Valor inválido")
elif salario < 1500:
    print(f"Categoria: Baixa renda \nSalário com bônus: R${salario * 1.2:.2f}")
elif salario <= 5000:
    print(f"Categoria: Classe média \nSalário com bônus: R${salario * 1.1:.2f}")
elif salario > 5000: #ou simplesmente else
    print(f"Categoria: Alta renda \nSalário com bônus: R${salario * 1.05:.2f}")
