votos_brancos = int(input("Informe o número de votos brancos: "))
votos_nulos = int(input("Informe o número de votos nulos: "))
votos_validos = int(input("Informe o número de votos válidos: "))

total = votos_brancos + votos_nulos + votos_validos

percentual_brancos = (votos_brancos / total) * 100
percentual_nulos = (votos_nulos / total) * 100
percentual_validos = (votos_validos / total) * 100

print(f"Os percentuais de votos brancos, nulos e válidos em relação ao total de eleitores do município, respectivamente, são: {percentual_brancos:.2f}%, {percentual_nulos:.2f}% e {percentual_validos:.2f}%")
