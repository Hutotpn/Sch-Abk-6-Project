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

print(grn())
