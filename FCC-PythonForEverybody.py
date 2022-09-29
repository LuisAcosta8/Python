#Scientific Computing with Python
#Book -->   http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
#*Intermediate expressions
#Excercises page 42
#2) Write a program that uses input to prompt a user for their name and then welcomes them
name = input("Enter your name: ")
print(f"Hello {name}")
print("Hello", name)
print("Hello {}".format(name))
#3) Write a program to prompt the user for hours and rate per hour to compute gross pay
hours = input("Hours: ")
rate = input("Rate per hour: ")
print("Gross payment:", int(hours)*int(rate))
#4) Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# For each of the following expressions, write the value of the expression and the type (of the value of the expression)
    #I) width//2
print(width//2)
    #II) width/2.0
print(width/2.0)
    #III) width/3
print(width/3)
    #IV) 1+2*5
print(1+2*5)
#5) Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature
celsius = int(input("Celsius: "))
farenheit = ((9*celsius)/5)+32
print(f"Farenheit: {farenheit}")
#Excercises page 52
#1) Rewrite your pay computation(excercise 3, page 42) to give the employee 1.5 times the hourly rate for hours worked above 40 hours
hours = float(input("Hours: "))
rate = float(input("Rate per hour: "))
pay = hours*rate
if hours > 40:
    et = hours-40
    pay = pay + (et*rate*0.5)
    print("Overtime")
    print("Gross payment:", pay)
else:
    print("Regular")
    print("Gross payment:", pay)
#2)Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program
try:
    hours = float(input("Hours: "))
    rate = float(input("Rate per hour: "))
    pay = hours*rate
    if hours > 40:
        et = hours-40
        pay = pay + (et*rate*0.5)
        print("Overtime")
        print("Gross payment:", pay)
    else:
        print("Regular")
        print("Gross payment:", pay)
except ValueError:
    print("You didn't write a numeric value")
#3)Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table
"""
Score       Grade
>= 0.9        A
>= 0.8        B
>= 0.7        C
>= 0.6        D
<  0.6        F
"""
score = float(input("Enter your score: "))
if score >= 0.9 and score <=1:
    print("A")
elif score >= 0.8 and score < 0.9:
    print("B")
elif score >= 0.7 and score < 0.8:
    print("C")
elif score >= 0.6 and score < 0.7:
    print("D")
if score >= 0 and score < 0.6:
    print("F")
else:
    print("Score is out of range")

#Functions
#1) Excercise page 58
import random
for i in range(10):
    x = random.random()
    print(x)
#random.randint(low, high)
#2)
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
def repeat_lyrics():
    print_lyrics()
    print_lyrics()
repeat_lyrics()

#Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get
#NameError: name 'repeat_lyric' is not defined. Did you mean: 'repeat_lyrics'?

# Excercise page 66
#4)What is the purpose of the “def” keyword in Python?
# d)b and c are both true

#5) What will the following Python program print out?
def fred():
    print("Zap")
def jane():
    print("ABC")
jane()
fred()
jane()

# d) ABC Zap ABC

#6) Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)
def pay(hours, rate):
    pay = hours * rate
    if hours > 40:
        et = hours - 40
        pay = pay + (et*rate*0.5)
    return "Gross payment: ", pay


#7) Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string
"""
Score       Grade
>= 0.9        A
>= 0.8        B
>= 0.7        C
>= 0.6        D
<  0.6        F
"""
def grade(score):
    if score >= 0.9 and score <=1:
        print("A")
    elif score >= 0.8 and score < 0.9:
        print("B")
    elif score >= 0.7 and score < 0.8:
        print("C")
    elif score >= 0.6 and score < 0.7:
        print("D")
    if score >= 0 and score < 0.6:
        print("F")
    else:
        print("Score is out of range")

#Iteration

# Excercises page
#1) Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number
num = 0
tot = 0.0
while True:
    number = input("Enter a number")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invailed Input')
        continue
    num = num+1
    tot = tot + num1
print (tot,num,tot/num)

#2) Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average

