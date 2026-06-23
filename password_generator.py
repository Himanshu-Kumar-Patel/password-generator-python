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


main()