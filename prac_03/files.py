#1
name = input("Digite seu nome: ")
with open('name.txt', 'w') as file:
    file.write(name)

#2
with open('name.txt', 'r') as file:
    name = file.read().strip()
print(f"Olá, {name}!")
