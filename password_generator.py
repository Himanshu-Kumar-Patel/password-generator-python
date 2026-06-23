import random
import string


def get_character_pool():
    characters = ""

    uppercase = input("Include uppercase letters? (y/n): ")
    lowercase = input("Include lowercase letters? (y/n): ")
    numbers = input("Include numbers? (y/n): ")
    symbols = input("Include symbols? (y/n): ")

    if uppercase == "y":
        characters += string.ascii_uppercase

    if lowercase == "y":
        characters += string.ascii_lowercase

    if numbers == "y":
        characters += string.digits

    if symbols == "y":
        characters += string.punctuation

    return characters


def generate_password(length, characters):
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"

    elif score <= 4:
        return "Medium"

    else:
        return "Strong"


def main():
    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length must be greater than or equal to 8")
        return

    characters = get_character_pool()

    if characters == "":
        print("Error: Select at least one character type.")
        return

    password = generate_password(length, characters)

    print("Generated Password:", password)
    strength = check_strength(password)
    print("Strength of password: ",strength)



main()