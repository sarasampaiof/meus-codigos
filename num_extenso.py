numero = int(input("Insira um número inteiro (de 0 a 9): "))

match numero:
    case 0:
        print("O número digitado é ZERO.")
    case 1:
        print("O número digitado é UM.")
    case 2:
        print("O número digitado é DOIS.")
    case 3:
        print("O número digitado é TRÊS.")
    case 4:
        print("O número digitado é QUATRO.")
    case 5:
        print("O número digitado é CINCO.")
    case 6:
        print("O número digitado é SEIS.")
    case 7:
        print("O número digitado é SETE.")
    case 8:
        print("O número digitado é OITO.")
    case 9:
        print("O número digitado é NOVE.")
    case _: # _ = else no padrão match case
        print("Valor inválido")
