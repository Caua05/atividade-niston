entrada = input("Digite uma lista de nomes separados por vírgula: ")


nomes = [nome.strip() for nome in entrada.split(',')]

nomes_com_a = [nome for nome in nomes if nome.startswith('A') or nome.startswith('a')]


print("Nomes que começam com a letra 'A':")
print(nomes_com_a)