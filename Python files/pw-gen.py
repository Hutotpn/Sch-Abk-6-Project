import random
import string
import time

def generate_password(length, use_uppercase=True, use_numbers=True, use_special_characters=True):
    # Create a list of characters to use in the password
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation
    
    # Use the random module to shuffle the characters
    password = ''.join(random.sample(characters, length))
    return password

# Welcome message
print("Welcome to the Random Password Generator!")

time.sleep(1)

while True:
    # Prompt the user for the password length
    length = int(input("How many characters would you like your password to have? "))

    # Prompt the user for the type of characters to use
    use_uppercase = input("Use uppercase letters? (y/n) ") == 'y'
    use_numbers = input("Use numbers? (y/n) ") == 'y'
    use_special_characters = input("Use special characters? (y/n) ") == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_characters)
    time.sleep(2)
    print("Your generated password is: " + password)

    try_again = input("Do you want to generate another password? (y/n) ")
    if try_again.lower() != 'y':
        print("Thank you for using the Random Password Generator. Goodbye!")
        break
