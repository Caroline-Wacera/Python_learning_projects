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

