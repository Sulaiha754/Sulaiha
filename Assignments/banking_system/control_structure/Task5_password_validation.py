
"""Task 5: Password Validation
Write a program that prompts the user to create a password for their bank account. Implement if
conditions to validate the password according to these rules:
• The password must be at least 8 characters long.
• It must contain at least one uppercase letter.
• It must contain at least one digit.
• Display appropriate messages to indicate whether their password is valid or not."""

def is_valid_password(password):
    if len(password) < 8:
        print(" Password must be at least 8 characters long.")
        return False
    if not any(char.isupper() for char in password):
        print(" Password must contain at least one uppercase letter.")
        return False
    if not any(char.isdigit() for char in password):
        print(" Password must contain at least one digit.")
        return False
    print("Password is valid!")
    return True
password = input("Create your password: ")
is_valid_password(password)
