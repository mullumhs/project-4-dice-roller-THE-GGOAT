"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.
def welcome_message():
    print('Welcome to the program')



# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.
def print_divider():
    print("'"*100)


# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.
def get_number():
   while True:
    num = input("Enter a number: ")
    try: 
       int(num)
       is_dig = True
       return int(num)
    except ValueError:
      is_dig = False
      num = input("Enter a whole number: ")


# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.
import random
def get_random_colour():
    x = random.randint(1, 5)
    colours = "red", "Green", "blue", "yellow", "transparent"
    return colours[x]
 

# Call all of your functions to demonstrate that they work
welcome_message()
print_divider()
get_number()
print_divider()
print(get_random_colour())