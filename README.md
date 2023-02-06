# Python Project (Aksep 19 6)
## Explain the code
### Calculator
#### Code
``` python
# Import & Settings
import time


# Operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Welcome Message
print("Welcome to the Calculator!")
time.sleep(1)
while True:
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Ask for operation
    time.sleep(1)
    choice = input("Enter the number of your choice (1, 2, 3, or 4): ")

    # Check if input is valid
    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        continue

    # Ask for numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate
    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    else:
        result = divide(num1, num2)
        operation = '/'

    # Display result
    time.sleep(1)
    print(f"{num1} {operation} {num2} = {result}")

    # Ask to try again
    time.sleep(1)
    try_again = input("Do you want to perform another calculation? (y/n): ")

    if try_again.lower() != 'y':
        print("Goodbye!")
        time.sleep(1)
        break
```
#### Explain this code
It starts by importing the *time* module, which is used later in the program to delay the execution of certain parts of the code.

It then defines four functions: add, subtract, multiply, and divide, which take in two arguments (x and y) and perform the corresponding mathematical operation on them.

After that, the program displays a welcome message and then enters a while loop that continues until the user decides to exit the program. The loop starts by displaying a menu of operations (add, subtract, multiply, and divide), and then prompts the user to select one of the options by entering a number (**1**, **2**, **3**, or **4**).

Once the user makes a selection, the program prompts the user to enter two numbers. It then uses an `if-elif` statement to check the user's choice and perform the corresponding operation using the two numbers entered by the user. The result is then printed to the screen.

If the user enters an invalid choice, the program will print "**Invalid input**".

Finally, after the operation is done, the program asks the user if they want to try again by entering '**y**' or '**n**'. If the user enters '**y**', the program reloads and the loop starts again. If the user enters '**n**', the program exits and displays a goodbye message.

The `time.sleep()` function is used to delay the execution of certain parts of the code, making the program more user-friendly and readable.

---
### Number Generator
#### Code
``` python
import random
from time import sleep

def grn():
  # Prompt the user to enter the lower and upper bounds of the range
  low = int(input("Enter the lower bound of the range: "))
  high = int(input("Enter the upper bound of the range: "))

  # Generate a random integer between low and high (inclusive)
  return random.randint(low, high)

# Welcome & Generate a random number within the user-specified range
print("Welcome to the Number Generator!")

sleep(1)

while True:
  print(grn())
  
  # Try again?
  sleep(1)
  print("Do you want to try again?: ")
  # Ask for input
  tryagain = input("Enter y/n: ")
  # If yes, do it again
  if tryagain == 'y':
    print("Reloading!")
    sleep(0.5)
    print("Reloaded!")
 
# If no, exit
else:
  print("Goodbye!")
  sleep(3)
  break
```
#### Explain this code
This is a Python program that generates random numbers within a range specified by the user.

It starts by importing the *random module* and *sleep* (from *time*) function from the time module.

The `grn()` function is defined which prompts the user to enter the lower and upper bounds of the range. It then uses the `random.randint()` function to generate a random integer between the specified bounds and returns the result.

The program then displays a welcome message and enters an infinite loop using `while True`. Within the loop, it calls the `grn()` function and prints the returned random number.

After that, the program asks the user if they want to try again by entering '**y**' or '**n**' using `input()` function. If the user enters '**y**', the program reloads and the loop starts again. If the user enters '**n**', the program exits and displays a goodbye message and break the infinite loop. The `sleep()` function is used to delay the execution of certain parts of the code, making the program more user-friendly and readable.

---
### Temperature Calculator
#### Code
``` python
# Import
import time

# Welcome
print("Welcome to the Temperature calculator.")

while True:
    # Ask
    time.sleep(1)
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    time.sleep(1)
    wtw = input("Enter choice(1 or 2): ")
    # Calculate
    if wtw == "1":
        askfah = int((input("Enter temperature in Fahrenheit: ")))
        fah = (askfah * 1.8) + 32
        print("The temperature in Fahrenheit is: " + str(fah))
    elif wtw == "2":
        askcel = int((input("Enter temperature in Celsius: ")))
        cel = (askcel - 32) * 5 / 9
        print("The temperature in Celsius is: " + str(cel))
    else:
        print("Invalid option")
    # Try again?
    time.sleep(1)
    print("Do you want to try again?: ")
    # Ask for input
    tryagain = input("Enter y/n: ")
    # If yes, do it again
    if tryagain == 'y':
        print("Reloading!")
        time.sleep(0.5)
        print("Reloaded!")

    # If no, exit
    else:
        print("Goodbye!")
        time.sleep(3)
        break
```
#### Explain this code
This is a Python program that converts temperature between Celsius and Fahrenheit.

It starts by importing the *time* module and displaying a welcome message to the user. Then it enters an infinite loop using `while True` and prompts the user to select an option for the conversion using `input()` function. The program presents two options: **1** for converting **Celsius to Fahrenheit** and **2** for **converting Fahrenheit to Celsius**.

Based on the user's choice, it prompts the user to enter a temperature value in the selected unit and uses the corresponding formula for the conversion. The result is then displayed to the user using **print()** statement.

If the user enters an invalid choice, the program will print "**Invalid option**"

Finally, after the operation is done, the program asks the user if they want to try again by entering '**y**' or '**n**' using `input()` function. If the user enters '**y**', the program reloads and the loop starts again. If the user enters '**n**', the program exits and displays a goodbye message. The `time.sleep()` function is used to delay the execution of certain parts of the code, making the program more user-friendly and readable.

---
### Password Generator
#### Code
``` python
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
```
#### Explain this code
This is a Python program that generates random passwords by using the `random` and `string` modules. The program starts by importing the `random` and `string` modules and the `time` module that will be used to add a delay to the program.

It defines a function `generate_password` that takes in four parameters:

`length`: the length of the password to generate
`use_uppercase`: a Boolean indicating whether to include uppercase letters in the password (defaults to **True**)
`use_numbers`: a Boolean indicating whether to include numbers in the password (defaults to **True**)
`use_special_characters`: a Boolean indicating whether to include special characters in the password (defaults to **True**)
It then creates a list of characters to use in the password by concatenating different sets of characters based on the parameters passed in. The `string` module is used to get the set of lowercase letters, uppercase letters, digits and special characters.

Then the function uses the ``random.sample()`` function to shuffle the characters and join them to form a password. The function then returns the generated password.

The program then displays a welcome message and enters an infinite loop using `while True` where it prompts the user for the password length and the type of characters to use. It then generates the password and displays it to the user after a 2 second delay by using the `time.sleep(2)`. Finally, the program asks the user if they want to generate another password by using `input()` function. If the user enters '**y**', the program reloads and the loop starts again. If the user enters '**n**', the program exits and displays a goodbye message.
