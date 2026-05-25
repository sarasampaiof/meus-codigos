vel_maxima = int(input("Informe a velocidade máxima, em km/h, permitida na avenida: "))
vel_motorista = int(input("Informe a velocidade, em km/h, com que o motorista estava dirigindo na avenida: "))

if vel_motorista > vel_maxima:
    multa = (vel_motorista - vel_maxima) * 5
    print(f"O motorista receberá uma multa de R${multa:.2f} por ultrapassar a velocidade máxima permitida na avenida.")
else:
    print("O motorista está livre de multa.")
