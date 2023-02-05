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
