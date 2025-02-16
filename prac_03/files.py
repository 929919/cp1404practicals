#1
name = input("Digite seu nome: ")
with open('name.txt', 'w') as file:
    file.write(name)

#2
with open('name.txt', 'r') as file:
    name = file.read().strip()
print(f"Olá, {name}!")

#3
with open('numbers.txt', 'r') as file:
num1 = int(file.readline().strip())
num2 = int(file.readline().strip())
result = num1 + num2
print(f"A soma dos dois primeiros números é: {result}")

#4

total = 0

with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line.strip())
print(f"A soma de todos os números é: {total}")
