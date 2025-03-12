"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name, count):
 print(f'Hello {name}' * count)

# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
def triple(number):
 print(number * 3)
# Write a function called add that takes two numbers as parameters and returns their sum. 
def add(num1, num2):
 print(num1 + num2)

# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.
def draw_line(length):
 print("*" * length)

# Call your functions, printing out the return result where appropriate
say_hello("Linc", 10)
triple(4)
add(6, 5)
draw_line(50)