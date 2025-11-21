#Write a program that asks the user for their name and age, then prints a greeting message.
name = input("Enter your name:")
age = int(input("Enter your age:"))
print(f"Hey! My name is {name}, and i am {age} years old.")

#Ask the user for a number and print whether it is even or odd. Keep asking until the user enters 0.
number = int(input("Enter a number:"))
while number != 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    number = int(input("Enter a number:"))

#Print the numbers from 1 to 20 using a while loop.
number = 1
while number <= 20:
    print(number)
    number += 1

#Print all the multiples of 5 from 5 to 50 using a while loop.
number = 5
while number <= 50:
    print(number)
    number += 5

#Ask the user for 5 numbers and store them in a list. After the inputs, print the list.
numbers = []
for _ in range (5):
    num = int(input("Enter a number:"))
    numbers.append(num)
print("The numbers you entered are:", numbers)

#Sum all numbers from 1 to 100 using a while loop.
number = 1
total_sum = 0
while number <= 100:
    total_sum += number
    number += 1
print(f"The sum of all numbers is {total_sum}")

#Reverse the string "WACERA" using a while loop.(no slicing allowed)
string_to_reverse = "WACERA"
reversed_string = ""
index = len(string_to_reverse) - 1
while index >= 0:
    reversed_string += string_to_reverse[index]
    index -= 1
print(f"The reversed string is: {reversed_string}")

#Given the list [3, 7, 1, 9, 4], find the largest number using a while loop.
given_list = [3, 7, 1, 9, 4]

largest_number = given_list[0]  # Start with the first element
index = 1  # We already considered index 0

while index < len(given_list):
    if given_list[index] > largest_number:
        largest_number = given_list[index]
    index += 1

print(f"The largest number in the list is: {largest_number}")

#Ask the user for input repeatedly until they type "exit" (case-insensitive). Print the input each time.
string = input("Enter a word until exit is typed:").strip().lower()
while string != "exit":
    print(string)
    string = input("Enter a word until exit is typed:").strip().lower()

#Print each character in the word "Python" using a while loop.
word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index += 1
