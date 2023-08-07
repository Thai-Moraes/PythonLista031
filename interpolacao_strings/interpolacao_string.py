nome = input("Digite o seu primeiro nome: ")
idade = int(input("Digite sua idade: "))

# print("Olá, ", nome, "!")
# print("Tudo bem com você?")
# print("Caramba", nome, "! Você tem", idade, "anos? Nem parece")

print("Olá, {}!" .format(nome))
print("Tudo bem com você?")
print("Caramba, {}! Você tem {} anos? Nem parece" .format(nome, idade))
print(f"Caramba, {nome}! Você tem {idade} anos? Nem parece")