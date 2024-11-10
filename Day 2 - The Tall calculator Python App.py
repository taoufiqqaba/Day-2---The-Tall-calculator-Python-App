import os
os.system('cls' if os.name == 'nt' else 'clear')

#  Day 2

print("Welcome to the Tall calculator! ")
height = int(input("What is Your Height in ? " ))
if height >= 120:
    print("You Can Ride! ")
else: 
    print("You cannot! ")

hhh = float(input("Enter a Number: "))
if hhh % 2 == 0:
    print("The Number is Even")
else:
    print("Odd")

age = int(input("Input Your Age Here:" ))
if age == 20:
    print("You Will Pay $10 ")
elif age == 25:
    print("You Will Pay $30 ")
elif age == 40:
    print("You Will Pay $70 ")
else:
    print("Fuck You ")
