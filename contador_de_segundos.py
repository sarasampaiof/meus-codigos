horas = int(input("Informe a quantidade de horas: ")) #horas * 3600 = segundos
minutos = int(input("Informe a quantidade de minutos: ")) #minutos * 60 = segundos
segundos = int(input("Informe a quantidade de segundos: "))


total_de_segundos = (horas * 3600) + (minutos * 60) + segundos

print("O total de segundos é ", total_de_segundos)
