"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to use exception handling in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a function called get_number(prompt) that returns an integer. 
# Include a while loop and try/except blocks inside the function to handle non-integer inputs.
def get_number(prompt):
        try:
            int(prompt)
            return(int(prompt))
            
        
        except ValueError:
           print("Please enter a vaild integer")
     

# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.
def division(numerator, denominator):
    try:
        answer = get_number(numerator)/ get_number(denominator)
        print(answer)
    
    except ZeroDivisionError:
        print("You cant divide by zero")

# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.
def list(index):
    try:
        X = get_number(index)
        list = "red", "Green", "blue", "yellow", "transparent"
        return list[X]
          
    except IndexError:
        ("NOT IN RANGE")

print(list(3))