lata_350ml = int(input("Informe a quantidade de latas de 350ml compradas: "))
garrafa_600ml = int(input("Informe a quantidade de garrafas de 600ml compradas: "))
garrafa_2L = int(input("Informe a quantidade de garrafas de 2 litros compradas: "))

total_de_litros = (lata_350ml * 350 + garrafa_600ml * 600 + garrafa_2L * 2000) / 1000 #calculado em mls para passar para litros ao dividir por mil

print("O total de litros comprados é: ", total_de_litros)
