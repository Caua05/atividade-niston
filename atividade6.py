import math


while True:
    try:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero < 0:
            print("Por favor, insira um número inteiro positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")


fatorial = math.factorial(numero)


print(f"O fatorial de {numero} é: {fatorial}")