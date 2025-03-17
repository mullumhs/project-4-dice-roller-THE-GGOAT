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

# pick a dice
def choose_dice():
   print("0. Roll D6")
   print("1. Roll D12") 
   print("2. Roll D20")    
def D6():
    return(random.randint(1, 6)) 

def D12():
   return(random.randint(1, 12))

def D20():
   return(random.randint(1, 20))

def list(index):
    
    list = [D6, D12, D20]
    try:
        for i in range(roll_amount()):  
            print(f"Spin {i+1}: {list[index]()}")     
    except IndexError:
        ("NOT IN RANGE")

# how many rolls 
   # add counter  
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
    
    

# Each Roll & Total
    # print counter
    #print sum of rolls
def get_number():
   while True:
    num = input("Enter a number: ")
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
choose_dice()



list(get_number())