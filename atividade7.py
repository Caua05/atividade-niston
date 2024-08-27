while True:
    try:
        valor_maximo = int(input("Digite um valor máximo para a sequência de Fibonacci: "))
        if valor_maximo < 0:
            print("Por favor, insira um valor positivo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")


a, b = 0, 1

print("Sequência de Fibonacci até", valor_maximo, ":")

while a <= valor_maximo:
    print(a, end=" ")
    a, b = b, a + b

print()