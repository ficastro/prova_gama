num = input("Insira um número inteiro: ")
while str(num).isnumeric() != True:
    num = input("\nEntrada inválida. Insira um número inteiro: ")
num = int(num)


print("\n")
if num < 10:
    print("O número é menor que 10.")

if (num % 2) == 0:
    print("O número é par.")

if num > 8 and num < 16:
    print("O número está entre 8 e 16.")

if num == 51 or num == 80:
    print("O número é 51 ou 80")