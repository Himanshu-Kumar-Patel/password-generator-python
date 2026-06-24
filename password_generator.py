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

    if not (
        uppercase == "y"
        and lowercase == "y"
        and numbers == "y"
        and symbols == "y"
    ):
        return None

    return characters


def generate_password(length, characters):
    password_chars = []

    # Guarantee all 4 character types
    password_chars.append(random.choice(string.ascii_uppercase))
    password_chars.append(random.choice(string.ascii_lowercase))
    password_chars.append(random.choice(string.digits))
    password_chars.append(random.choice(string.punctuation))

    # Fill remaining characters
    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    random.shuffle(password_chars)

    password = "".join(password_chars)
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
        print("Password length must be at least 8 characters")
        return

    characters = get_character_pool()

    if characters is None:
        print(
            "Error: To use this version, select uppercase, lowercase, numbers, and symbols."
        )
        return

    count = int(input("How many passwords you want to generate? "))
    print()

    saved_passwords = []

    for i in range(count):
        password = generate_password(length, characters)

        print(f"Password {i+1}: {password}")

        strength = check_strength(password)

        print(f"Strength: {strength}")
        print()

        saved_passwords.append(
            f"Password {i+1}: {password}\nStrength: {strength}\n"
        )

    save = input("Save passwords to file? (y/n): ")

    if save.lower() == "y":
        file = open("password.txt", "a")

        file.write("\n")
        file.write("===== New Session =====\n\n")

        for item in saved_passwords:
            file.write(item)
            file.write("\n")

        file.close()

        print("Passwords saved successfully.")


main()