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
