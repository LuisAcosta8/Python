#BASICS I
### Print
print("Hello Word")

### Comments
#This is a comment

### Variables
x = 3
y = 2
print(y)

### Mathematical Operators
#addition
print(10+2)

#substraction
print(4-1)

#multiplication
print(10*7)

#division
print(50/10)

#modulus
print(10%2)

### Comparison Operators
# == equals to
print(1==2)
print("hello"=="hello")

# != not equal or different
print(2!=2)

# > more than
print(2>2)

#> more than or equals to
print(2>=2)

# < less than
print(1<2)

# <= less than or equals to
print(3<=2)

### Logical Operators
# and
print(False and False)

# or
print(False or False)

#not
print(not(False))

### Data types
# string
print("Hello World")

# integer
print(1)

# float
print(1.23)

# boolean
print(True)

# use the type function
print(type("Hello World"))
print(type(1))
print(type(1.23))
print(type(True))

### Type conversion
print("1")
print(1)
#print("1"+1) #Error

#type conversion
print(int("1") + 1)
print(type(int("1")))
print(int(10.00))
print(int(10.12))
print(float(10))
print(type(str(1000)))

###Control flow
is_raining = False
is_sunny = False

if is_raining:
	print("Let's grab an umbrella")

elif is_sunny:
	print("Let's go a grab an umbrella")

else:
	print("No need to bring an umbrella")


is_raining = False
is_sunny = False
if is_raining or is_sunny:
    print("Let's grab an umbrella")
else:
    print("No need an umbrella")

### Functions
def hello_world():
    return "Hello World"

print(hello_world())

def hello(sentence):
    return "Hello" + " " + sentence

print(hello("my name is Luis"))

def add_two(a,b):
    return a+b
print(add_two(100,200))


#BASICS II

### Intro to lists
first = "a"
secod = "b"
third = "c"

list_of_letters = ["a","b","c","d","e"]
print(list_of_letters)
list_of_ints = [1,2,3,4,5]
list_of_floats = [1.0,2.0,3.0]
list_of_bools = [True, True, False]

print(list_of_ints)
print(list_of_floats)
print(list_of_bools)

### Getting a list item

letters = ["a","b","c","d","e"]
print(letters)

#Counting starts from 0 in Python

# ["a","b","c","d","e"]
# 0,1,2,3,4
# -5,-4,-3,-2,-1

print(letters[5])
#print(letters[-6]) #Error
print(letters[-2])

### Subsetting and slicing lists

letters = ["a","b","c","d","e"]
print(letters)
print(letters[1])

# ["a","b","c","d","e"]
# 0,1,2,3,4
# -5,-4,-3,-2,-1

# We want to get "a" and "b"
print(letters[:3])

# namelist[start_index:end_index+1]

# We want to get "c" and "d"
print(letters[2:4])

# We want to get "b" and everithing else
print(letters[1:])

print(letters[-4:])

### List Manipulation

letters = ["a","b","c","d","e"]

# len() to count number of items in list
print(len(letters))

# append() to add new items into the list
# name_list.apppend("new_item")

print(letters)
letters.append("f")
letters.append("g")
print(letters)


# pop() to remove items from back of list
letters.pop()
print(letters)

# you can store items popped out of list
popped_item = letters.pop()
print(popped_item)

# name_list.pop(index)
letters.pop(0)
print(letters)

### Loop control I

letters = ["a","b","c","d","e"]
print(letters)
print(letters[0])
print(letters[1:4])

for letter in letters[1:4]:
	print(letter)

# range() gives you a range of numbers
numbers = [0, 1, 2, 3, 4]
print(numbers)
numbers = range(9) # starts from 0, ends at 8
print(numbers)

for number in range(9):
print("hello")


### Loop control II

numbers = range(9)

for number in numbers:
	if number == 5:
		#break 	  (end the loop)
		#pass
		#continue (skip number 5)
		print("The above let the code pass")
	else:
		print(number)

### While loop

#while True:
	#code will continuously run
    
test = 0

while test < 9:
    print("Hello")
    test += 1 #adds 1 to test

### Tuples
#Inmutable = cannot be changed

example_tuple = ("a","b","c","d","e")
print(example_tuple)

print(example_tuple + ("f","g","h"))
print(example_tuple[2])
      
example_list = [1,2,3,4,5]
print(tuple(example_list))
      
print(example_tuple[1:4])


### Dictionaries
# {key:value}

john = {"name": "John Smith", "age":18}
print(john)

john["Country"] = "Singapore"
print(john)

# We can retriebe the valeu using the key
print(john["name"])

#print(john["gender"])	#Error

print(john.keys())
print(john.values())

john["Has kids"] = True
john["fav colors"] = ["Black","White","Red"]
print(john)

### Sets
example_set = {"a", "b", "a"}
print(example_set)

example_list = [1, 2, 3, 3, 3, 4, 5]
print(set(example_list))
print(len(example_set))
example_set.add("f")
example_set.remove("a")
print(example_set)

example_set_2 = {"c","d","a"}
print(example_set_2)

print(example_set_2 - example_set)