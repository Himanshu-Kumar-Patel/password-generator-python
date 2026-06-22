import random
import string

length = int(input("Enter password length: "))

if length<8:
	print("Disclaimer: Password length must be greater than or equal to 8")
	exit()

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

if characters=="":
	print("Error: Select at least one character type")
	exit()
 

password = ""

for i in range(length):
    password += random.choice(characters)

print("Generated Password:", password)