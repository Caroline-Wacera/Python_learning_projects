#1: Print each item in a list using a while loop
fruits = ["apple", "banana", "mango", "orange"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

#Exercise 2: Count how many numbers in the list are even
numbers = [12, 5, 8, 19, 4, 21, 6]

index = 0
even_count = 0
while index < len(numbers):
    if numbers[index] % 2 == 0:
        even_count += 1
    index += 1
print(f"Total even numbers: {even_count}")

#Basic counting
# Print numbers 1 to 10
number = 1
while number <= 10:
    print(number)
    number += 1

#User input repetition
# Keep asking user for a number until they type 0
number = int(input("Enter a number: "))
while number != 0:
    print(f"You entered {number}")
    number = int(input("Enter a number: "))

#Even/Odd check with repetition
number = int(input("Enter a number: "))
while number != 0:
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
    number = int(input("Enter a number: "))

#Looping through a string
word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index += 1

#Looping through a list
fruits = ["apple", "banana", "mango"]
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1
