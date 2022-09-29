"""
########################
print("Hello Python!")
print("Luis")
#print(Luis)
#print "Luis"
print('Luis')
print("The itsy bitsy spider climbed up the waterspout.")
print()
print("Down came the rain and washed the spider out.")
########################
#\ backslash
print("The itsy bitsy spider\nclimbed up the waterspout.")
print()
print("Down came the rain \ and washed the spider out.")
print("\a hola")
print("")
print("\\")
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")
print("My name is", "Python.")
print("Monty Python.")
print("My name is", "Python.", end=" ")
print("Monty Python.")
print("My name is ", end="")
print("Monty Python.")
print("My", "name", "is", "Monty", "Python.", sep="-")
print("My", "name", "is", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print("Programming","Essentials","in")
print("Python")
print("Programming","Essentials","in")
print("Python")
print("Programming","Essentials","in", end = "@")
print("Python")
print("Programming","Essentials","in")
print("Python", end = "@")
print("Programming","Essentials","in", sep = "|")
print("Python")
print("Programming","Essentials","in")
print("Python", sep = "|")
print("Programming","Essentials","in", end = "°", sep = "|")
print("Python")
print("Programming","Essentials","in", sep = "***", end = "...")
print("Python")
########################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print("    *"*2, "   * *"*2, "  *   *"*2, " *     *"*2, "***   ***"*2, "  *   *"*2, "  *   *"*2, "  *****"*2, sep= "\n")
print("2")
print(2)
print(-11_111_111)
#Octal numbers
print(0o123)
#Hexadecimal numbers
print(0xF)
print(0x123)
#Scientific notation
print(3E8, "m/s")
print(-9E3)
print(6.62607E-34)
print(0.0000000000000000000001)
print(True > False)
print(True < False)
print('\"I\'m\"','\""learning\""','\"""Python\"""', sep = "\n")
print(2+2)
#Arithmetic operators
#(+,*,*,/, //,**,%)
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
print(6 // 4)
print(6. // 4)
print(-6 // 4)
print(6. // -4)
print(12 % 4.5)
print(-4 + 4)
print(-4. + 8)
print(-4 - 4)
print(4. - 8)
print(-1.1)
print(+2)
print(2 ** 2 ** 3)
print(2 * 3 % 5)
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#Variables
#Reserved_Keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
jhon = 3
mari = 5
adam = 6
print(jhon,mari,adam)
total_apples = jhon + mari + adam
print(total_apples)
print("Total number of apples:", total_apples)

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")


#
x =  -1# hardcode your test data here
x = float(x)
y = (3*x**3)-(2*x**2)+(3*x)-1
print("y =", y)

#this program computes the number of seconds in a given number of hours

a = 2
seconds = 3600 

print("Hours: ", a) #printing the number of hours
print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
print("Goodbye")

anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is", (leg_a**2 + leg_b**2) ** .5)

fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


a = float(input("Enter your variable a:"))
b = float(input("Enter your variable b:"))

print("Adition:", a+b)
print("Substract:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)

print("\nThat's all, folks!")

x = float(input("Enter value for x: "))

y = 1/(x+(1/(x+(1/(x+(1/x))))))
print("y =", y)

n = int(input("Set a number: "))
print(f"{n} < 100",n < 100)
print(f"{n} > 100",n > 100)
"""
"""
a = input()
if a == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif a == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print(f"Spathiphyllum! Not " + a +"!")

year = int(input("Enter a year: "))

#
if year < 1582:
    print("Not within Gregorian calendar period")
elif year % 4 != 0:
    print("It's a common year")
elif year % 100 != 0:
    print("It's a leap year")
elif year % 400 != 0:
    print("It's a commmon year")
else:
    print("It's a leap year")
#	
while True:
    print("I'm stuck inside a loop.")

counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

secret_number = 777
a = int(input("Enter a num: "))
while a != secret_number:
    print("Ha ha! You're stuck in my loop!")
    a = int(input("Enter a num: "))
    
print("Well done, muggle! You are free now.")

import time

# Write a for loop that counts to five.
for i in range(1,6):
    
    print(i, "Mississippi")
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)
    time.sleep(1)
# Write a print function with the final message.
print("Ready or not, here I come!")


# break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


while True:
    a = input("Enter a secret word: ")
    if a == "chupacabra":
        break
print("You've successfully left the loop")


# Prompt the user to enter a word
a = input("Enter a word: ")
# and assign it to the user_word variable.
user_word = a.upper()
for letter in user_word:
    # Complete the body of the for loop.
    if "A" == letter:
        continue
    elif "E" == letter:
        continue
    elif "I" == letter:
        continue
    elif "O" == letter:
        continue
    elif "U" == letter:
        continue
    else:
        print(letter)



word_without_vowels = ""
user_word = input("Enter a word: ")
# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = user_word.upper()
for letter in user_word:
    # Complete the body of the loop.
    if "A" == letter:
        continue
    elif "E" == letter:
        continue
    elif "I" == letter:
        continue
    elif "O" == letter:
        continue
    elif "U" == letter:
        continue
    else:
         word_without_vowels = word_without_vowels + letter
# Print the word assigned to word_without_vowels.
print(word_without_vowels)

#Lothar Collatz Hypothesis
c0 = int(input("Enter a num: "))
n = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 / 2
        n +=1
        print(c0)
    elif c0 % 2 != 0:
        c0 = 3 * c0 + 1
        n +=1
        print(c0)
    else:
        n +=1
        print(c0)
print("Steps = ", n)

for i in range(1,11):
    if i % 2 == 0:
        continue
    else:
        print(i)

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x+=1
"""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end = "")

print("\n")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")



hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
print(hat_list[round(len(hat_list)/2)])
# Step 2: write a line of code that removes the last element from the list.
del(hat_list[-1])
print(hat_list)
# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))
print(hat_list)
#APPEND
#list.append(value)
#INSERT
#list.insert(location, value)
#To change the variable values
"""
variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary
"""
#
"""
variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
"""
a = 5
b = 8
print("a",a)
print("b",b)
a, b = b, a
print("New a",a)
print("New b",b)

#For a list when you don't know the lenght of the list
my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)


# step 
beatles = []
print("Step 1:", beatles)


# step 2
beatles.append("Jhon Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 3
print("Step 3:", beatles)
beatles.append("Stu Sutcliffe")
beatles.append("Pete Best")
# step 4
print("Step 4:", beatles)
del(beatles[-2])
del(beatles[-1])
# step 5
print("Step 5:", beatles)
beatles.insert(0,"Ringo Starr")
print(beatles)
# testing list legth
print("The Fab", len(beatles))

#burble sort list.sort()
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

#list.reverse() change list order from last element to first element


####to avoid the .copy() method you can make a slicing when you copy list1 in list2
# Copying the entire list.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


###
my_list = [10, 8, 6, 4, 2]
list1 = my_list[:]
print(my_list)
print(list1)
my_list[2] = 4
list1[0] = 111
print(my_list)
print(list1)


#
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list:
    if i > largest:
        largest = i

print(largest)
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
print(my_list)
list_elements = []
for i in my_list:
    if i not in list_elements:
        list_elements.append(i)
my_list = list_elements[:]
#
print("The list with unique elements only:")
print(my_list)



#Three dimension array
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

#Cube
# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'

#Digit of life

a = input("Enter you birthday date(YYYYMMDD): ")
r = 0
for i in a:
    r = r + int(i)
    print(r)

#Reading ints safely

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print("Error: wrong input")
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max) + ")")
    return value;


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)