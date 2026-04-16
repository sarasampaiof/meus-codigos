numero = int(input("Informe um número inteiro: "))

if numero % 2 == 0 and numero % 3 == 0:
    print(f"{numero} é divisível por 2 e por 3")
else:
    print(f"{numero} não é divisível por 2 e por 3")
    
#ou:
#if numero % 6 == 0:
    #print(f"{numero} é divisível tanto por 6 quanto por 2 e por 3, uma vez que todo número divisível por 6, também é divisível por 2 e por 3")
#else:
    #print(f"{numero} não é divisível por 6")
