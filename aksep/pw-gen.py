import random
import string
import time

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_characters=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation
    password = ''.join(random.sample(characters, length))
    return password

print("Welcome to the Random Password Generator!")
time.sleep(1)

while True:
    length = int(input("Enter the desired length of your password (minimum 6 characters): "))
    if length < 6:
        print("For your safety, password length must be at least 6 characters. Please try again.")
        continue

    print("Choose the types of characters to include in your password:")
    time.sleep(1)
    use_uppercase = input("Include uppercase letters? (y/n) ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n) ").lower() == 'y'
    use_special_characters = input("Include special characters? (y/n) ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_numbers, use_special_characters)
    print(f"Your generated password is: {password}")

    try_again = input("Do you want to generate another password? (y/n) ").lower()
    if try_again != 'y':
        print("Thank you for using the Random Password Generator. Goodbye!")
        time.sleep(3)
        break