# Using f-string formatting to produce the required output
name = "Gibson L-5 CES"
year = 1922
cost = 16036
print(f"{year} {name} for about ${cost:,}!")

# Using a for loop with f-string formatting to generate the required output
for i in range(11):
    print(f"2 ^ {i:2} is {2 ** i:4}")