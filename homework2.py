# 1. The Calculator App
# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.
response=input("add, subtract, multiply, or divide")
num1=float(input("enter first number"))
num2=float(input("enter a second number"))

if response == "add":
    result = num1 + num2
    print(result)
elif response == "subtract":
    result = num1 - num2
    print(result)
elif response == "multiply":
    result =num1 * num2
    print(result)
elif response == "divide":
    if num2 == 0:
        print("cant divide by zero lol")
    else:
        result = num1 / num2
        print(result)
else:
    print("invalid input")















# 2. The Shopping List Maker
# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

grocery_list = []
while True:
    item = input("Enter a item or type 'stop' to finish: ")
    if item == 'stop':
        break
    grocery_list.append(item)
remove_item = input("Do you want to remove an item? (y/n): ")
if remove_item == 'y':
    item_to_remove = input("Enter the item you want to remove: ")
    if item_to_remove in grocery_list:
        grocery_list.remove(item_to_remove)
    else:
        print("Item not found in the grocery list.")
print("Your grocery list:")
for item in grocery_list:
    print("- " + item)
