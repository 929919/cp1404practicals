#1
name = input("Digite seu nome: ")
with open('name.txt', 'w') as file:
    # Escreve o nome no arquivo
    file.write(name)
