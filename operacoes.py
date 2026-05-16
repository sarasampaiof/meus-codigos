num1 = int(input("Insira um número: "))
num2 = int(input("Insira um número: "))
operacao = input("Insira a operação que deseja realizar entre esses números (+, -, *, /): ")

match operacao:
    case "adição" | "+": # | = or no padrão match case
        print(f"O resultado da operação é {num1 + num2}.")
    case "subtração" | "-":
        print(f"O resultado da operação é {num1 - num2}.")
    case "multiplicação" | "*":
        print(f"O resultado da operação é {num1 * num2}.")
    case "divisão" | "/":
        print(f"O resultado da operação é {num1 / num2}.")
