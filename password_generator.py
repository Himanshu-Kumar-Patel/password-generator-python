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

    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    random.shuffle(password_chars)

    return "".join(password_chars)


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


def generate_passwords():

    length = int(input("Enter password length: "))

    if length < 8:
        print("Password length must be at least 8 characters")
        return

    characters = get_character_pool()

    if characters is None:
        print(
            "Error: Select uppercase, lowercase, numbers and symbols."
        )
        return

    count = int(input("How many passwords do you want to generate? "))
    print()

    saved_passwords = []

    for i in range(count):

        password = generate_password(length, characters)

        strength = check_strength(password)

        print(f"Password {i+1}: {password}")
        print(f"Strength: {strength}")
        print()

        saved_passwords.append(
            f"Password {i+1}: {password}\nStrength: {strength}\n"
        )

    save = input("Save passwords to file? (y/n): ")

    if save.lower() == "y":

        with open("password.txt", "a") as file:

            file.write("\n")
            file.write("===== New Session =====\n\n")

            for item in saved_passwords:
                file.write(item)
                file.write("\n")

        print("Passwords saved successfully.")


def view_password_history():

    try:

        with open("password.txt", "r") as file:

            print("\n===== PASSWORD HISTORY =====\n")

            print(file.read())

    except FileNotFoundError:

        print("No saved passwords found.")


def delete_password_history():

    confirm = input(
        "Are you sure you want to delete all saved passwords? (y/n): "
    )

    if confirm.lower() == "y":

        with open("password.txt", "w") as file:
            pass

        print("Password history deleted successfully.")

    else:
        print("Deletion cancelled.")




def main():

    while True:

        print("\n===== PASSWORD GENERATOR =====")
        print("1. Generate Passwords")
        print("2. View Saved Password History")
        print("3. Delete Password History")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_passwords()

        elif choice == "2":
            view_password_history()

        elif choice == "3":
            delete_password_history()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
