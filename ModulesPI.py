#Modules PI
from random import randint

for i in range(10):
    print(randint(1, 10), end="," )

lis = [100,28,56,8,9,78,45,1]
a = randint(1,len(lis)-1)
print(lis.pop(a))
print(lis)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


#You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?
import sys

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()

#When package or module is stored in a diferent place
    import sys

# note the double backslashes!
sys.path.append("D:\\Python\\Project\\Modules")
