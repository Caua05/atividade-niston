entrada = input("Digite uma lista de números separados por espaço: ")


numeros = list(map(int, entrada.split()))


pares = [num for num in numeros if num % 2 == 0]


if pares:
    media_pares = sum(pares) / len(pares)
    print(f"A média dos números pares é: {media_pares:.2f}")
else:
    print("Não há números pares na lista para calcular a média.")