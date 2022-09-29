from cmath import pi, sqrt
from math import pi
# Basic
#  1) Write a program that prompts the user to type their name and greets them by calling their name.
name = input("What's your name?")
print(f"Hi, {name}")
#  2) Write a program that receives as input the radius of a circle and outputs its perimeter and area.
radius = float(input("Enter the radius of the circle: "))
P = 2 * pi * radius
A = pi * radius**2 
print(f"Perimeter: {P}")
print(f"Area: {A}")
#  3) Write a program that calculates the average of 4 marks entered by the user
a = []
for i in range(4):
    q = int(input(f"Enter the number {i+1}: "))
    a.append(q)
mean = a[0] + a[1] + a[2] + a[3] / 4
print(f"Average: {mean}")

#ó
"""
a = int(input("Enter the number 1) "))
b = int(input("Enter the number 2) "))
c = int(input("Enter the number 3) "))
d = int(input("Enter the number 4) "))

mean = (a + b + c + d) / 4

print(f"Average: {mean}")

"""


#  4) Write a program that converts from centimeters to inches. An inch is 2.54 centimeters
cm = float(input("cm: "))
inches = cm / 2.54
print(f"Inches: {inches}")

#  5) Write a program that prompts the user for a three-digit integer and returns the number with the digits in reverse order
a = input("Enter a three-digit integer: ")
print(a[2] + a[1] + a[0])



#  6) Write a program that receives as input the lengths of the two legs a and b of a right triangle, and outputs the length of the hypotenuse c of the triangle, given by the Pythagorean theorem: c^2=a^2+b^2
a = float(input("Enter the side A: "))
b = float(input("Enter the side B: "))
c = sqrt(a**2+b**2)
print(f"Side C: {c}")

#  7) Write a program that asks the user for the current clock time t and an integer number of hours h, indicating what time the clock will show in h hours
t = int(input("Time now: "))
h = int(inút("Hours: "))


#  8) Write a program that returns the decimal part of a real number entered by the user
num = float(input("Enter a decimal number: "))
dec = int(num)
dec = num - dec
print(f"Decimal: {dec}")

#  9) A student wants to know what mark he needs in the third contest to pass a bouquet.
"""    The branch average is calculated using the following formula.

    NC=(C1+C2+C3)/3
    NF=NC⋅0.7+NL⋅0.3
    Where NC is the average of the exam, NL the average of the laboratory and NF the final grade.

    Write a program that asks the user for the marks of the first two quizzes and the laboratory mark, and shows the mark that the student needs to pass the course with a final mark of 60 
    """
