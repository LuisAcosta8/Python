Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> None*None
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    None*None
TypeError: unsupported operand type(s) for *: 'NoneType' and 'NoneType'
>>> 1//2
0
>>> lst = [i for i in range(-1,-2)]
>>> len(lst)
0
>>> a = 1
>>> b = 0
>>> a = a^b
>>> a
1
>>> b = a^b
>>> b
1
>>> a = a^b
>>> print(a, b)
0 1
>>> type(a^b)
<class 'int'>
>>> nums = [1,2,3]
>>> vals = nums
>>> len(vals)
3
>>> len(nums)
3
>>> del vals[:]
>>> vals
[]
>>> nums
[]
>>> foo = (1,2,3)
>>> foo.index(0)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    foo.index(0)
ValueError: tuple.index(x): x not in tuple
>>> x = 3
>>> y = 2
>>> x%y
1
>>> y%x
2
>>> print('a','b','c', sep='sep')
asepbsepc
>>> x = float(2)
>>> y = float(4)
>>> print(y**(1/x))
2.0
>>> mylist = [x*x for x in range(5)]
>>> def fun(lst):
	del lst[lst[2]]
	return lst

>>> print(fun(mylist))
[0, 1, 4, 9]
>>> my_list = [1,2]
>>> for v in range(2):
	my_list.insert(-1, my_list[v])

	
>>> print(my_list)
[1, 1, 1, 2]
>>> x = 1
>>> y = 2
>>> x,y,z = x,x,y
>>> z,y,z = x,y,z
>>> print(x,y,z)
1 1 2
>>> dct = {}
>>> dct['1'] = (1,2)
>>> dct['2'] = (1,2)
>>> for x in dct.keys():
	print(dct[x][1], end="")

	
22
>>> 