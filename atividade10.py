import random

def jogar_pedra_papel_tesoura():

    opcoes = ['pedra', 'papel', 'tesoura']
    

    while True:
        escolha_usuario = input("Escolha pedra, papel ou tesoura: ").strip().lower()
        if escolha_usuario in opcoes:
            break
        else:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")


    escolha_computador = random.choice(opcoes)
    

    print(f"O computador escolheu: {escolha_computador}")
    

    if escolha_usuario == escolha_computador:
        resultado = "Empate!"
    elif (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_usuario == 'papel' and escolha_computador == 'pedra') or \
         (escolha_usuario == 'tesoura' and escolha_computador == 'papel'):
        resultado = "Você ganhou!"
    else:
        resultado = "O computador ganhou!"
    

    print(resultado)


jogar_pedra_papel_tesoura()