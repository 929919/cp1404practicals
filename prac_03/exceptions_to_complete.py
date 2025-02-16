"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  #TODO: Set is_finished to True to exit the loop when input is valid
    except ValueError:  #TODO: Catch only ValueError exceptions (invalid input type)
        print("Please enter a valid integer.")

print("Valid result is:", result)