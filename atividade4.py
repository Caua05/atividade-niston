def ler_lista():
    lista = []
    while True: 
        entrada = input('Digite um número: ')
        if entrada == "": 
            break
        try: 
            numero = float(entrada)
            lista.append(numero)
        except ValueError:
            print('Invalido, Digite outro número: ')
    return lista
numeros = ler_lista()

if numeros:
    maior = max(numeros)
    menor = min(numeros)
    print(f"O maior valor é: {maior}")
    print(f"O menor valor é: {menor}")
else:
    print("A lista está vazia.")