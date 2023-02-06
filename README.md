# Python Project (Aksep 19 6)

[![CodeQL](https://github.com/Hutotpn/Python-project-Aksep19/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/Hutotpn/Python-project-Aksep19/actions/workflows/github-code-scanning/codeql)

## Explain the code

### Calculator

#### Code

```python
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

This code is a simple calculator program that performs basic arithmetic operations (addition, subtraction, multiplication, and division).

The code starts by importing the `time` module, which is used later to add pauses between `print` statements to make the program feel more user-friendly.

Next, the code defines four functions, `add`, `subtract`, `multiply`, and `divide`, that perform the corresponding arithmetic operations. Each function takes two arguments, **x** and **y**, and returns the result of the operation.

After defining the functions, the program prints a welcome message, and then enters an infinite loop. Within the loop, the program first displays the list of available operations, and then asks the user to choose one by entering a number.

If the user's choice is not one of the four options, the program displays an error message and goes back to the beginning of the loop. If the user's choice is valid, the program asks the user to enter two numbers, and then performs the chosen operation. The result of the operation is displayed, and then the program asks the user if they want to perform another calculation. If the user enters '**n**', the program terminates and displays a goodbye message. If the user enters '**y**', the program goes back to the beginning of the loop.

<!-- End Calculator -->

### Number Generator

#### Code

```python
import random
from time import sleep

def generate_random_number():
  # Prompt the user to enter the lower and upper bounds of the range
  lower_bound = int(input("Enter the lower bound of the range: "))
  upper_bound = int(input("Enter the upper bound of the range: "))

  # Generate a random integer between low and high (inclusive)
  return random.randint(lower_bound, upper_bound)

# Welcome & Generate a random number within the user-specified range
print("Welcome to the Random Number Generator!")

sleep(1)

try_again = True
while try_again:
  print(generate_random_number())

  # Ask the user if they want to try again
  try_again = input("Do you want to generate another random number? (y/n) ").lower() == 'y'

# Goodbye message
print("Goodbye!")
sleep(3)
```

#### Explain this code

The code generates random numbers within a user-specified range. The user is first asked to enter the lower and upper bounds of the range. Then, a random integer between the specified bounds is generated using the `random.randint` function. The generated number is displayed, and the user is asked if they want to generate another random number. If the user enters '**y**', another random number is generated. If the user enters anything other than '**y**', the program displays a goodbye message and exits. The `sleep` function from the `time` module is used to add pauses between each message for better readability.

<!-- End Number Generator -->

### Temperature Calculator

#### Code

```python
# Import
import time

# Welcome
print("Welcome to the Temperature Calculator!")
time.sleep(1)

while True:
    # Ask
    print("\nPlease choose an option:")
    print("1. Convert from Celsius to Fahrenheit")
    print("2. Convert from Fahrenheit to Celsius")

    # Get user input
    user_choice = input("Enter your choice (1 or 2): ")

    # Calculate and print result
    if user_choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 1.8) + 32
        print("The temperature in Fahrenheit is: {:.2f}°F".format(fahrenheit))
    elif user_choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print("The temperature in Celsius is: {:.2f}°C".format(celsius))
    else:
        print("Invalid option")

    # Ask user if they want to try again
    try_again = input("\nWould you like to try again? (y/n) ").lower()
    if try_again != 'y':
        print("\nThank you for using the Temperature Calculator. Goodbye!")
        time.sleep(3)
        break
```

#### Explain this code

The code implements a temperature calculator that allows the user to convert temperatures between **Celsius** and **Fahrenheit**. When the program starts, it displays a welcome message and presents two options to the user: **(1) Convert from Celsius to Fahrenheit**, and **(2) Convert from Fahrenheit to Celsius**. The user is prompted to enter their choice (1 or 2). If the user enters 1, the program asks for a temperature in Celsius and then converts it to Fahrenheit using the formula fahrenheit = `(celsius * 1.8) + 32`. The result is displayed with a message. If the user enters 2, the program asks for a temperature in Fahrenheit and then converts it to Celsius using the formula celsius = `(fahrenheit - 32) * 5 / 9`. The result is displayed with a message. If the user enters anything other than 1 or 2, an error message is displayed. After each calculation, the program asks the user if they want to try again. If the user enters '**y**', the program starts again. If the user enters anything other than '**y**', the program displays a goodbye message and exits. The `time.sleep` function is used to add pauses between each message for better readability.

<!-- End Temperature Calculator -->

---

### Password Generator

#### Code

```python
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
```

#### Explain this code

The code generates a random password based on user-specified length and character types (uppercase letters, numbers, special characters). The `generate_password` function takes four arguments: `length`, `use_uppercase`, `use_numbers`, and `use_special_characters`. The user-specified length and character type preferences are passed to the function, and a password is generated using `random.sample`. The program then prints the generated password and asks the user if they want to generate another password. If the user enters anything other than '**y**', the program displays a goodbye message and exits. The `sleep` function from the `time` module is used to add pauses between each message for better readability.

<!-- End Password Generator -->

<!-- Documentation End -->
