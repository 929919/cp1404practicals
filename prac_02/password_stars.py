def get_password():
    """Ask the user for a password and validate its length."""
    min_length = 6
    password = input("Enter a password: ")

    while len(password) < min_length:
        print("Password too short. Try again.")
        password = input("Enter a password: ")

    print("*" * len(password))


get_password()