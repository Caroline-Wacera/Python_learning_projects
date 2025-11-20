#Exercises for Day 2
#Ask the user for two numbers and print their sum
number_1 = int(input("Enter a number:"))
number_2 = int(input("Enter another number:"))
sum = number_1 + number_2
print(f"The sum of the two numbers is {sum}")
#Ask the user for two numbers and print their difference.
difference = number_1 - number_2
print(f"The difference between the two numbers is {difference}")
#Multiply two numbers from user input and print the result.
multiple = number_1 * number_2
print(f"When you multiply the two numbers the answer is {multiple}")
#Divide two numbers from user input and print the result.
division = number_1 / number_2
print(f"When you divide the two numbers the answer is {division}")
#Ask for two numbers, calculate average, and print it.
average = (number_1 + number_2) / 2 
print(f"The average of the two numbers is {average}")
#Ask for radius, calculate area of circle (area = 3.14 * r**2).
radius = float(input("Enter the radius:"))
area = 3.14 * radius ** 2
print(f"The area of a circle is {area}")
#Ask for length and width, calculate area of rectangle.
length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
area = length * width
print(f"The area of a rectangle is {area}")
#Ask for base and height, calculate area of triangle.
base = float(input("Enter the base of a triangle:"))
height = float(input("Enter the height:"))
area = 1/2 * base * height
print(f"The area of a triangle is {area}")
#Ask user for number of hours and hourly rate, calculate total pay.
hours = float(input("Enter the hours:"))
rate = float(input("Enter the hourly rate:"))
total_pay = hours * rate
print(f"The total pay is {total_pay} ")
#Ask for a number, print whether it is even or odd.
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")