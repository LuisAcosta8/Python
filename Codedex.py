#Write and show in screen
from cmath import sqrt
import random

print("Hello world")
print("       1\n     2 3\n   4 5 6\n7 8 9 10")
print("L       A")
print("L      AAA")
print("L     A   A")
print("L     AAAAA")
print("L     A   A")
print("L     A   A")
print("LLLLL A   A")
print("\n")
print("August 8th 2022")
print("Dear future me")
print("I'm looking for a job, I want to cry because I haven't had locky for get my fisrt job, I hope you will having a great salary. I'm going to do the possible for you will have a good jobs and I will learn English for that.")
print("During this course I want to reinforce my knowledge and maybe learn new thing about python. I know that I'm bad with OOP and I want to change that.")
print("This is for you past me; I know is difficult have a concentration with all your problems but your life won't finish you have to be a good worker and you can do it, you will be the best.")
print("With love, Past Luis Acosta")
print("This letter will to open and read for the letter sender in 3 months")
#DataTypes
print("Variable \n variable_name = value")
print("Int \n variable_name = 8")
print("8 is ", type(8))
print("Float \n variable_name = 8.1235")
print("8.1235 is ", type(8.1235))
print("String \n variable_name = 'Hello'")
print("Hello is ", type("Hello"))
print("Boolean \n variable_name = True")
print("True is ", type(True))

#Operators
"""
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulo (returns the remainder)
"""
#Temperature.py
f = 100
c = (f-32)/1.8
print(str(f) + " °F = " + str(c) + " °C")

#Exponents
""" 
Exponent**
"""
#BMI.py
mass = 189
height = 15
bmi = mass/(height**2)
print("Your BMI is equal to", bmi)

#Input
"""
Allows the user interact with the program
"""
#Quadratic.py
print("Quadratic Equation")
print("aX^2 + bX + c = 0")
a = int(input("Enter de 'a' value: "))
b = int(input("Enter de 'b' value: "))
c = int(input("Enter de 'c' value: "))

x1 = (-b + sqrt(b**2 - 4*a*c ))/2*a
x2 = (-b - sqrt(b**2 - 4*a*c ))/2*a
#Currency.py
yuan = float(input("What do you have left in yuan? "))
yen  = float(input("What do you have left in yen? "))
won  = float(input("What do you have left in won? "))
yUSD = yuan * 0.15
yeUSD = yen * 0.0074
wUSD = won * 0.00077
print(yuan, "yuan =", yUSD, " USD")
print(yen, "yen =", yeUSD, " USD")
print(won, "won =", wUSD, " USD")

#Control Flow

num = random.randint(0, 1)   # RNGesus will give us a random number between 0 and 1

if num > 0.5:
  print("Heads")
else:
  print("Tails")

  #grades.py
num = random.randint(0, 100)
if num >= 55:
    print("You passed")
else:
    print("You failed")

"""
One or more elif statements (short for "else if") can be optionally added in between the if and else to provide additional condition(s) to check. Sometimes two is simply not enough.
"""

#Relational operators
"""
== equal to
!= not equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""

#IF

#if condition:
    #instructions
#else:
    #instructions

#if condition:
    #instructions
#elif condition2:
    #instructions2
#else:
    #instructions


#ph_levels.py
ph = random.randint(0, 14)
if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")


#Magic 8 Ball
question = input("Question: ")

random_int = random.randint(1,9)

if random_int == 1:
    print("Your question: ", question)
    print("Your answer: Yes - definitely.")
if random_int == 2:
    print("Your question: ", question)
    print("Your answer: It is decidedly so.")
if random_int == 3:
    print("Your question: ", question)
    print("Your answer: Without a doubt.")
if random_int == 4:
    print("Your question: ", question)
    print("Your answer: Reply hazy, try again.")
if random_int == 5:
    print("Your question: ", question)
    print("Your answer: Ask again later.")
if random_int == 6:
    print("Your question: ", question)
    print("Your answer: Better not tell you now.")
if random_int == 7:
    print("Your question: ", question)
    print("Your answer: My sources say no.")
if random_int == 8:
    print("Your question: ", question)
    print("Your answer: Outlook not so good.")
if random_int == 9:
    print("Your question: ", question)
    print("Your answer: Very doubtful")


#SortingHat.py

print("Sorting Hat".center(50, "*"))

Gryffindor = 0
Ravenclaw = 0
Hufflepuf = 0
Slytherin = 0
print("Do you like Dawn or Dusk?")
option = input("1)Dawn \n 2)Dusk\n")
if option == 1:
    Gryffindor = Gryffindor + 1
    Ravenclaw = Ravenclaw + 1
elif option == 2:
    Hufflepuf = Hufflepuf + 1
    Slytherin = Slytherin + 1
else:
    print("Wrong input")

option = input("When I´m dead, i want people to remember me as: \n1)The Good\n2)The Great\n3)The Wise\n4)The Bold\n")
if option == 1:
    Hufflepuf = Hufflepuf + 1
elif option == 2:
    Slytherin = Slytherin + 1
elif option == 3:
    Ravenclaw = Ravenclaw + 1
elif option == 4:
    Gryffindor = Gryffindor + 1
else:
    print("Wrong input")

option = input("Wich kind of instrument most pleases your ear? \n1)The violin\n2)The trumpet\n3)The piano\n4)The drum\n")
if option == 1:
    Slytherin = Slytherin + 1
elif option == 2:
    Hufflepuf = Hufflepuf + 1
elif option == 3:
    Ravenclaw = Ravenclaw + 1
elif option == 4:
    Gryffindor = Gryffindor + 1
else:
    print("Wrong input")

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print("🦁 Gryffindor!")
elif ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print("🦅 Ravenclaw!")
elif hufflepuff >= slytherin:
  print("🦡 Hufflepuff!")
else:
  print("🐍 Slytherin!")

#while condition        
    #instructions

#enter_pin.py
print("BANK OF CODÉDEX")

pin = int(input("Enter your PIN: "))

while pin != 1234:
  pin = input("Incorrect PIN. Enter your PIN again: ")

  if pin == 1234:
    print("PIN accepted!")
 
 #Logical operators
 """
 *and
 *or
 *not
 """


 #Guess.py
 guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number:  "))
  tries = tries + 1

if tries == 5:
  print("You ran out of tries.")
else:
  print("You got it!")


#for in range
for i in range(1,101,1):
    print(i, ")", "I will not use Snapchat in class")

#String concatenation
for i in range(5):
    print("The square of " + str(i) + " is " + str(i*i))

#String Interpolation
for i in range(5):
    print(f"The square of {i} is {i*i}")


#99Bottlesofbeer
for i in range(99, 0, -1):
  print(f"{i} bottles of beer on the wall")
  print(f"{i} bottles of beer")
  print("take one down pass it around")
  print(f"{i-1} bottles of beer on the wall")


#fizz_buzz.py
for i in range (1,101, 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:print(i)

