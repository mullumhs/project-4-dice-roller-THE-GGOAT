"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                Dice Roller
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

def welcome():
     print("Welcome to Python dice roller")
     

def print_divider():
    print()
    print("-"*100)
    print()

def Dice():
    total = 0   
    for i in range(roll_amount()):  
     
        spinvalue = random.randint(1, jcole)
        print(f"Spin {i+1}: {spinvalue}")    
        total = total + spinvalue
    print(f"Your total is {total}")
    print(f"You rolled {i + 1} times")

def roll_amount():
    while True:
        roll_amount = input("How many times would you like to roll: ")
        try: 
            int(roll_amount)
            is_dig = True
            return int(roll_amount)
        except ValueError:
            is_dig = False
            roll_amount = input("Invalid input. Enter a whole number: ")
    
def get_number():
   while True:
    num = input("How many sides would you like to roll?: ")
    try: 
       int(num)
       is_dig = True
       return int(num)
    except ValueError:
      is_dig = False
      num = input("Invalid input. Enter a whole number: ")


print_divider()
welcome()
print_divider()
jcole = get_number()
print_divider()
Dice()
print_divider()

