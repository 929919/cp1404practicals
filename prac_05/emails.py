"""
Emails
Estimate: 20 minutes
Actual: 25 minutes
"""
def extract_name(email):
    """Extract a formatted name from the email address."""
    name_part = email.split('@')[0]
    name = " ".join(name_part.split('.')).title()
    return name


def main():
    """Store emails and names in a dictionary and display them."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email:
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm and confirm != 'y':
            name = input("Name: ").strip().title()
        email_to_name[email] = name
        email = input("Email: ").strip()

    print("\nStored email addresses and names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
