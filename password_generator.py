import random
import string

length = int(input("Enter password length: "))

characters = ""

uppercase = input("Include uppercase letters? (y/n): ")
lowercase = input("Include lowercase letters? (y/n): ")
numbers = input("Include numbers? (y/n): ")
symbols = input("Include symbols? (y/n): ")

if uppercase=="y":
	characters+=string.ascii_uppercase


if lowercase=="y":
	characters+=string.ascii_lowercase


if numbers=="y":
	characters+=string.digits


if symbols=="y":
	characters+=string.punctuation
 

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)