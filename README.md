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
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    # Ask for operation
    time.sleep(1)
    choice = input("Enter choice(1/2/3/4): ")

    # Ask for number
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Calculate
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid input")

    # Try again?
    time.sleep(1)
    print("Do you want to try again?(y/n): ")
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
```
#### Explain this code
This is a Python program that converts temperature between Celsius and Fahrenheit.

It starts by importing the *time* module and displaying a welcome message to the user. Then it enters an infinite loop using `while True` and prompts the user to select an option for the conversion using `input()` function. The program presents two options: **1** for converting **Celsius to Fahrenheit** and **2** for **converting Fahrenheit to Celsius**.

Based on the user's choice, it prompts the user to enter a temperature value in the selected unit and uses the corresponding formula for the conversion. The result is then displayed to the user using **print()** statement.

If the user enters an invalid choice, the program will print "**Invalid option**"

Finally, after the operation is done, the program asks the user if they want to try again by entering '**y**' or '**n**' using `input()` function. If the user enters '**y**', the program reloads and the loop starts again. If the user enters '**n**', the program exits and displays a goodbye message. The `time.sleep()` function is used to delay the execution of certain parts of the code, making the program more user-friendly and readable.
