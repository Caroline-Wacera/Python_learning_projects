# 1. Print numbers from 1 to 10 using a while loop
number = 1
while number <= 10:
    print(number)
    number += 1

# 2. Print all even numbers between 2 and 20 using while
number = 2
while number <= 20:
    print(number)
    number += 2

# 3. Ask the user for a number and print whether it’s positive or negative until they enter 0
user_number = int(input("Enter a number (0 to quit): "))
while user_number != 0:
    if user_number > 0:
        print("The number is positive")
    else:
        print("The number is negative")
    user_number = int(input("Enter a number (0 to quit): "))

# 4. Sum numbers from 1 to 50 using while
sum_total = 0
number = 1
while number <= 50:
    sum_total += number
    number += 1
print(f"The sum of numbers from 1 to 50 is {sum_total}")

# 5. Ask user for input repeatedly until they type "exit"
user_input = input("Enter an input (type 'exit' to quit): ").strip().lower()
while user_input != "exit":
    print("The input is not 'exit'")
    user_input = input("Enter an input (type 'exit' to quit): ").strip().lower()

# 6. Check if a number is even or odd repeatedly until 0
user_number = int(input("Enter a number (0 to quit): "))
while user_number != 0:
    if user_number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    user_number = int(input("Enter a number (0 to quit): "))

# 7. Print each character of a string using a while loop
word = "Yellow"
index = 0
while index < len(word):
    print(word[index])
    index += 1

# 8. Print multiplication table of 7 using while
number = 7
multiplier = 1
while multiplier <= 10:
    print(f"{number} x {multiplier} = {number * multiplier}")
    multiplier += 1

# 9. Reverse a string using while loop
string_to_reverse = "Wacera"
reversed_string = ""
index = len(string_to_reverse) - 1
while index >= 0:
    reversed_string += string_to_reverse[index]
    index -= 1
print(f"The reversed string is: {reversed_string}")

# 10. Ask user for input repeatedly until they type "exit" (alternative version for practice)
user_input = input("Enter input (type 'exit' to quit): ").strip().lower()
while user_input != "exit":
    print(f"You entered: {user_input}")
    user_input = input("Enter input (type 'exit' to quit): ").strip().lower()
