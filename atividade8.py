def e_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero < 0:
            print("Por favor, insira um número inteiro não negativo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")


if e_primo(numero):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")