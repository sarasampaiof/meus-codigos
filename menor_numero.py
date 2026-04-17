numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))
numero3 = int(input("Informe o terceiro número: "))

if numero1 < numero2 and numero1 < numero3:
    print(f"O menor número é {numero1}.")
elif numero2 < numero1 and numero2 < numero3:
    print(f"O menor número é {numero2}.")
else:
    print(f"O menor número é {numero3}.")
