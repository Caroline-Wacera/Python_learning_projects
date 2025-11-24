#Print numbers 1 to 20 using a while loop.
number = 1
while number <= 20:
    print(number)
    number += 1

#Print all multiples of 3 between 3 and 30.
number = 3
while number <= 30:
    print(number)
    number += 3

#Ask the user for a number and print whether it’s positive or negative, until they enter 0.
number = int(input("Enter a number:"))
while number != 0:  
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    number = int(input("Enter a number: "))

#Print the sum of numbers from 1 to 50
number = 1 
total_sum = 0
while number <= 50:
    total_sum += number
    number += 1
print(f"The total sum of number from 1 to 50 is {total_sum}")

#Ask the user for input repeatedly until they type "exit" (case-insensitive).
user_input = input("Enter the input until you type exit:").strip().lower()
while user_input != "exit":
    print(user_input)
    user_input = input("Enter the input until you type exit:").strip().lower()

#Print each character of the string "Yellow" one by one.
colour = "Yellow"
index = 0
while index < len(colour):
    print(colour[index])
    index += 1

#Print a multiplication table of 7 using a while loop.
number = 1
while number <= 10:
    result = 7 * number
    print(f"7 x {number} = {result}")
    number += 1

#Ask the user for a number and print whether it is even or odd repeatedly until they enter 0.
number = int(input("Enter a number:"))
while number != 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    number = int(input("Enter a number:"))
print("End of loop")

#Reverse the string "WACERA" using a while loop (no slicing).
name = "WACERA"
reversed_name = ""
index = len(name) - 1
while index >= 0:
    reversed_name += name[index]
    index -= 1
print(reversed_name)

#Print all items in the list ["apple", "banana", "mango", "orange"] one by one.
fruits = ["apple", "banana", "mango", "orange"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
