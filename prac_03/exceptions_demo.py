"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Answer to question 1:
# A ValueError will occur if the user enters something that cannot be converted to an integer,
# for example, a string like "abc" instead of a valid number.

# Answer to question 2:
# A ZeroDivisionError will occur if the user enters 0 as the denominator,
# because dividing by zero is undefined in mathematics and results in an error.

# Answer to question 3:
# To avoid the possibility of a ZeroDivisionError, we can check if the denominator is zero before performing the division.
# Here's an updated version of the code to handle that:
