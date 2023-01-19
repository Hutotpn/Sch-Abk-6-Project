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
