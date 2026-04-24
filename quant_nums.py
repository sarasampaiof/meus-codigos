num = int(input("Informe um número: "))
quantidade_nums = 0

for i in range(1, num):
    if i % 2 == 0:
        print(i)
        quantidade_nums += 1
print(f"Quantidade de números: {quantidade_nums}")
