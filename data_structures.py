#----------------------------------------------------------|
#                   Unit - 5  | File4                      |
#                     "Data Structures"                    |
#     (This is file 4 containing notes of pydocs unit-5)   |
#----------------------------------------------------------|

'1.' 'list.append(x) : adds items at the end of the list'
numbers = [1,2,3,4,5]
numbers.append(33)
print(numbers)  # [1, 2, 3, 4, 5, 33]


'2.' 'list.extend(interable) : add new list to end of old list'
# numbers.extend(3)  # TypeError: 'int' object is not iterable
numbers.extend([3])
print(numbers)  #[1, 2, 3, 4, 5, 33, 3]


'3.' 'list.insert(index,value)'
numbers.insert(3,44)
print(numbers)  #[1, 2, 3, 44, 4, 5, 33, 3]


'4.' 'list.remove(value)'
numbers.remove(33)
print(numbers)   #[1, 2, 3, 44, 4, 5, 3]
'NOTE : error occurs if no such item is present'
# numbers.remove(99)  #ValueError: list.remove(x): x not in list


'5.' 'list.pop(index) : removes and returns item from a specific index'
'if left empty it removes item from the last'

print(numbers.pop())  #3
print(numbers.pop(1)) #2
print(numbers)   #[1, 3, 44, 4, 5]


'6.' 'list.clear() : removes all items from the list'

print(numbers)  #[1, 3, 44, 4, 5]
numbers.clear()
# print(numbers.clear())  #None
print(numbers)  #[]


numbers = [1,2,3,4,5]

'7.' 'list.index(value) : finds value by 0-based indexing in the'
print(numbers.index(3))   #2
print(numbers.index(5))   #4
# print(numbers.index(99))  #ValueError: 99 is not in list


'8. list.count(value) : counts the occurence of a value'
nums = [1,2,2,3,3,4,4,4]
print(nums.count(77))  #0
print(nums.count(3))   #2


'9. list.sort(* , key=None , reverse=False)'
'sort the items of the list in place'

num = [4,3,2,1]
num.sort()
# print(num.sort())  #None
print(num)  #[1, 2, 3, 4]


'10. list.reverse() : reverse the list elements in place'

x = [3,5,1,2]
x.reverse()
# print(x.reverse())  #None

print(x)  #[2, 1, 5, 3]


'11. list.copy() : returns a shallow copy of the list'
keys1 = [1,2,3,4]
keys2 = keys1.copy()

keys1[0] = 99   #'changing keys1 item'

print(keys2)  #[1, 2, 3, 4]  
'this is a shallow copy as changing keys does not affected keys2 values'

print(keys1)  #[99, 2, 3, 4]

# ---------------------------------------------
# Using lists a stacks
#----------------------------------------------

'-The lists makes it very easy to use a list as a "STACK"'
'where the last element added is the first element retrieved'
'last-in-first-out'

'-To add an item on the top of the stack use append()'
'-To retrieve an item from top of the stack use pop(),' 
'without an explicit index'

#For example :

stack = [3,4,5,6,7]
stack.append(99)
# print(stack.append(44))   #None
print(stack)   # [3, 4, 5, 6, 7, 99]

print(stack.pop())   #99
print(stack)
#[3, 4, 5, 6, 7]


#append() will add item from the last
#pop() will remove the last added item
# so this way the list works as a last-in-first-out model or Stack

# ----------------------------------------------
# Using lists as Queues  (use collection.deque)
# from collections import deque
# queue = deque([iterables])
# ----------------------------------------------

'''
- Queues are made from first-in-first-out principal
- Lists can also be used as Queues but,
  lists are no efficient for this purpose'
  Because append and pop from the end of the list are fast
  but doing inserts or pops from the beginning of a list is slow'
# (Because all the other elements have to be shifted one by one)
'''

#To implement a queue, use collections.deque which was designed to have 
#fast appends and pops from both ends.
'For example'

from collections import deque

queue = deque([11,22,33,44])

# print(queue.append('new item'))  #None
queue.append('new item')
print(queue)
#deque([11, 22, 33, 44, 'new item'])

print(queue.popleft())   #11
print(queue)
# deque([22, 33, 44, 'new item'])

'append() is used to add item in queue(which is a deque)'
'popleft() is used to remove item from the start of the queue'
'hence this works as a first-in-first-out or queue'


# -----------------------------------------------
'    List Comprehensions  '
# newlist = [expression for item in iterable if condition == True]
# -----------------------------------------------

'List comprehension provides a concise way to create lists'
'Common applications are to make new lists where each element is'
'the result of some operations applied to each member of another'
'sequence or iterable'
'or , to create a subsequence of those elements that satisfy'
'a certain condition'

#For example , assume we want to create a list of squares
sqaure = []
for i in range(10):
    sqaure.append(i**2)
    
print(sqaure) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ------- but we can do this by following method also---
sqaure2 = list(map(lambda x : x**2 , range(10)))
print(sqaure2) 
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#-----method3 for square counting---------

square3 = [x**2 for x in range(10)]
print(square3)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# ----
'''
- A list comprehension consists of brackets containing an expression
followed by a for clause, then zero or more for or if clauses.

- The result will be a new list resulting from evaluating the
expression in the context of the for and if clauses which follow it.
'''
# For example , this listcomp combines the elements of two list 
# if they are not equal

listcomp = [(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]
print(listcomp)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

'the above is equivalent to'
comb = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            comb.append((x,y))
            
print(comb)  #[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
print(type(comb))  #<class 'list'>

'Note how the order of for and if statements' 
'is the same in both these snippets'

"If the expression is a tuple(e.g (x,y)), it must be parenthesized"

# ------------Example-------

vec = [-4,-2,0,2,4]

'task1 : create a new list with the values doubled'
# task1 = [vec*2]
# print(task1) 
# # [[-4, -2, 0, 2, 4, -4, -2, 0, 2, 4]]

task1 = [x*2 for x in vec]
print(task1)  
# [-8, -4, 0, 4, 8]


'task2 : filter the vec list and exclude negative numbers'
pos = [x for x in vec if x>=0]
print(pos)
# [0, 2, 4]

print([x for x in vec if x>=0])
[0, 2, 4]

'task3 : apply a function to all the elements'
print([abs(x) for x in vec])
# [4, 2, 0, 2, 4]


'task4 : call a method on each element'
fruits = ['apple ', '  mango','grapes']

print([x.strip() for x in fruits])
# ['apple', 'mango', 'grapes']

print([x.upper() for x in fruits])
# ['APPLE', 'MANGO', 'GRAPES']

print(fruits)
# ['apple', 'mango', 'grapes']

'task5 : create a list of 2 tuples like (number,square)'
print([(x,x**2) for x in vec])
# [(-4, 16), (-2, 4), (0, 0), (2, 4), (4, 16)]
'NOTE: tuple must be parenthesized () , otherwise it gives an error'


'task6 : flatten a list using listcomp using two for'
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
'Normal way'
flatten_list = []
for row in matrix:
    flatten_list.extend(row)

print(flatten_list)   #[1, 2, 3, 4, 5, 6, 7, 8, 9]

'my trial and error way'
# print((x,y) for x in vecs for y in vecs)
# <generator object <genexpr> at 0x104f09a50>

'using list comprehension'
print([item for row in matrix for item in row])
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# ---------------
"List comprehension can also contain complex expressions and nested functions"

from math import pi
# print(pi)   #3.141592653589793

print([round(pi,i) for i in range(1,6)])
# [3.1, 3.14, 3.142, 3.1416, 3.14159]

# ------------------------------------
'      Nested list Comprehensions     '
# ------------------------------------

'''
The initial expression in a list comprehension can be any 
arbitary expression , including another list comprehension
'''
#Given a matrix of 3*3
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

'TASK : we want to transpose this matrix'
'transpose means chnage row items into columns and column items into row'
''' something like below:
[1,4,7],
[2,5,8],
[3,6,9]
'''

'way1 : using numpy'
import numpy as np

transpose =  np.transpose(matrix)
print(transpose)        
'''output
[
 [1 4 7]
 [2 5 8]
 [3 6 9]
 ]
'''
print(np.transpose(matrix))
'''output
[
 [1 4 7]
 [2 5 8]
 [3 6 9]
]
'''
# --------------------------------
'way2 : '
transpose = []
for i in range(3):
    transpose.append([row[i] for row in matrix])

print(transpose)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


'way3 : '
transpose = []
for i in range(3):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transpose.append(transposed_row)

print(transpose)  #[[1, 4, 7], [2, 5, 8], [3, 6, 9]]


'way4 : using list comprehension'
x  = [[row[i] for row in matrix] for i in range(3)]
print(x)
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

print([[row[i] for row in matrix] for i in range(3)])
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# --------------------------------
'''
zip(*iterables, strict=False)

Iterate over several iterables in parallel, 
producing tuples with an item from each one.

'''
# ----------------------------------
'zip makes tuples , so convert them in list as per use case'

# print(list(zip(matrix)))
# [([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9],)]

print(list(zip(*matrix)))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

#---------------------------------------
'  The del keyword  :'
'There is a way to remove an item from a list given its index'
'instead of its value: the del statement'

'This differs from pop() method which returns a value'

'The del statement can also be used to remove slices from a list'
'or to remove an entire list'

items = [55,66,77,88,99,00]
print(items) #[55, 66, 77, 88, 99, 0]

'deleting first index using del'
del items[0]
print(items) # [66, 77, 88, 99, 0]

'deleting a slice from items'
del items[2:]
print(items)  #[66, 77]

'deleting the whole list'
del items
# print(items)  NameError: name 'items' is not defined.

# ----------------------------------------------
'        Tuples and Sequences           '
# ----------------------------------------------

'A tuple consists of a number of values seperated by comma'
'Tuples are immutable'

tup = 1,2,3,4
print(tup)  # (1, 2, 3, 4)
print(type(tup)) # <class 'tuple'>

tup2 = (1,2,3)
print(tup2)  #(1, 2, 3)
print(type (tup2))  # <class 'tuple'>

'''-----"tuples are immutable"-----
tup[0] = 33
print(tup)
TypeError: 'tuple' object does not support item assignment
'''

#Tuples are immutable objects but , they can contain mutable items
tup = ([1,2,3],[4,5,6])
print(tup)  #([1, 2, 3], [4, 5, 6])

'Nesting tuples'
combining_two_tuple_items = tup,99
print(combining_two_tuple_items)
# (([1, 2, 3], [4, 5, 6]), 99)

trying_tup = 99,
print(trying_tup)  #(99,)
print(type(trying_tup))  #<class 'tuple'>

# -------------------------------------------

tup = 44,55,66
#Tuple unpacking
x,y,z = tup
print(x,y,z)   #44 55 66

#--------------------------------------------
'empty tuple is made using only parentheses()'
tup = ()
print(tup,len(tup),type(tup))
#     ()     0      <class 'tuple'>


'single tuple is made using a single value with comma'
tup = 44,
print(tup,len(tup),type(tup))

#    (44,)    1    <class 'tuple'>

# -------------------------------------------
'                  SETS                     '
# -------------------------------------------

'Python also includes a datatype for sets'
'A set is an unordered collection with no duplicate elements'

'Basic uses include membership testing and eliminating duplicate entries'

'Set objects also support mathematical operations such as'
'union'
'difference'
'intersection'
'symmetric difference'

'Curly braces {} or the set() function can be used to create sets.'
myset = {1,2,3,4}
print(myset,len(myset),type(myset))
# {1, 2, 3, 4} 4 <class 'set'>

'NOTE: to create an empty set , use set() , not simply this {}'
'because simply {} will create an empty dictionary'

myset = set()
print(myset,len(myset),type(myset))
# set() 0 <class 'set'>

# -----------set demonstartions-------

nums = {1,2,3,4,5,1,2,3,6}
print(nums) 
#{1, 2, 3, 4, 5 ,6}   //all duplicates has been removed

'fast membership testing'
print(2 in nums)  #True
print(33 in nums)  #False
print(33 not in nums)  #True


'set operations on unique letters'

'below set_a use only print one word string , not expanding list'
# set_a = {'aabbc'}  
# print(set_a,type(set_a))
# # {'aabbc'} <class 'set'>


'this set() method prints expanding list'
set_a = set('abcddee')
print(set_a) 
# {'a', 'd', 'b', 'e', 'c'}
# (only unique letters are printed)

set_b = set('abdscc')
print(set_b)
# {'c', 's', 'b', 'a', 'd'}
# (only unique letters are printed)

'print differences in a and b sets  (a-b) or (b-a)'
'means letters which are in set_a but not in set_b '
print(set_a - set_b)  #{e}

'letters which are in set_b but not in set_a'
print(set_b - set_a)  #{s}


'letters in a or b both (a|b) // prints all letters of both sets'
print(set_a | set_b) #{'c', 'e', 'b', 'd', 'a', 's'}

'print common letters of both sets // use &'
print(set_a & set_b)  #{'c', 'a', 'b', 'd'}


'letters in set a or b but not in both'
print(set_a ^ set_b)  #{'e', 's'}

# ----------------------------------------------------------------------
# Similar to list comprehensions , set comprehensions are also supported
# ----------------------------------------------------------------------


a = {x for x in 'helloworld' if x not in 'o'}
print(a)
# {'d', 'r', 'e', 'h', 'w', 'l'}



# ----------------------------------
'          Dictionaries             '
# ----------------------------------

'Another useful built-in data type in python is dictionaries'

'Dictionary is a set of key:value  pairs'
'with the requirement that each key is unique'

'A pair of curly braces {} creates an empty dictionary'
d = {}
print(d,type(d))  #{} <class 'dict'>

'deleting a dictionary using del keyword'
del d
# print(d)  NameError: name 'd' is not defined.

'If we again use already existing key'
'then old value associated with that key will be forgotten'

d = {1:'one',2:'two'}
print(d[1])  #one

'but if we assign again value for key 1 , we get another value'
d = {1:'one',2:'two',1:'three'}
print(d[1])
# three

# ---------------------
'if we try to use a non existent key'
'it will throw a KeyError'
# print(d[44])   KeyError: 44

# ------------------------
'using list(dict_name) will give '
'list of all the keys used in the dictionary , in the insertion order'

d = {99:22,22:33,33:33,11:44}
print(list(d))
# [99, 22, 33, 11]   (list of keys same as insertion order)

'if we want list of keys in sorted order'
'we can use sorted(dict_name)'

print(sorted(d))
# [11, 22, 33, 99]

d = {'c':3 , 'b':2 , 'a':1}
print(list(d))  #['c', 'b', 'a']
print(sorted(d)) #['a', 'b', 'c']


'to check a single key is present in dictionary use'
'in keyword'

print('a' in d)  #True
print('z' in d)  #False
print('d' not in d) #True

'deleting a single key-value'
del d['a']
print(d)   #{'c': 3, 'b': 2}

# -------------------------------------------
'''
The dict() constructor builds dictionaries directly from
sequences of key-value pairs:
'''

d = dict([(1,'eat'),(2,'code'),(3,'sleep')])
print(d) ## {1: 'eat', 2: 'code', 3: 'sleep'}

'directly assign key=values if the keys are normal strings'
d = dict(eat=1,code=2,sleep=3)
print(d) #{'eat': 1, 'code': 2, 'sleep': 3}

d = dict(name='somu',clas='4th',age=77)
print(d)  #{'name': 'somu', 'clas': '4th', 'age': 77}

# ---------------------------------------------

'dict comprehensions can also be used to create dictionaries'
'from arbitrary key and value expressions'

d = {x:x**2 for x in range(5)}
print(d)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

d = {x:y for x in (1,2,3,4) for y in (11,22,33,44)}
print(d)
#{1: 44, 2: 44, 3: 44, 4: 44}

'when the keys are simple strings'
'we can also specify pairs using keyword arguments'

d = dict(ram=33,kam=44,pam=55)
print(d)  #{'ram': 33, 'kam': 44, 'pam': 55}

# -----------------------------------------------------
#              Looping Techniques
#------------------------------------------------------
'''
1. When looping through dictionaries , the key and its value
   can be retrieved at the same time using the items() method.
# items() : Return a new view of the dictionary's items ((key, value) pairs)
'''

d = dict(name='hacker' , age = 99 , ransom = 1_00_000)
for key,value in d.items():
    print(key,value)
    
'output'    
# name hacker
# age 99
# ransom 100000

# ----------------------------------------------
'''
2 . When looping through a sequence we can get both "index" and "value"
at the same time , using enumerate() function
'''

for index,value in enumerate((11,22,33)):
    print(index,value)
    
'output'
# 0 11
# 1 22
# 2 33
    
# enumerate(iterable, start=0)
demo1 = ['jan','feb','march','april']

'if we want to get a list of months with corresponding index'
'we can do like this'
print(list(enumerate(demo1)))
# [(0, 'jan'), (1, 'feb'), (2, 'march'), (3, 'april')]

'if we want the index to start from some other number'
'we can specify that too'

print(list(enumerate(demo1,start=1)))
# [(1, 'jan'), (2, 'feb'), (3, 'march'), (4, 'april')]

print(list(enumerate(demo1,start=-4)))
# [(-4, 'jan'), (-3, 'feb'), (-2, 'march'), (-1, 'april')]


# -------------------------------------
# Enumerate() method adds a counter to an iterable and 
# returns it in a form of enumerating object. 
# This enumerated object can then be used 
# directly for loops or converted into a list of 
# tuples using the list() function.

l1 = [11,22,33,44]
print(list(enumerate(l1)))
# [(0, 11), (1, 22), (2, 33), (3, 44)]

l2 = 'abcde'
print(list(enumerate(l2)))
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# ----------------------------------------
'''
3. To loop over two or more sequences at the same time
the entries can be paired with the zip() function
'''
testcases = ['t1','t2','t3','t4']
answers = [22,33,44,55]

'using indexes as placeholders for format() method'
for tcase,ans in zip(testcases,answers):
    print('test case number {0} ,ans is {1}'.format(tcase,ans))

'output'
# test case number t1 ,ans is 22
# test case number t2 ,ans is 33
# test case number t3 ,ans is 44
# test case number t4 ,ans is 55

'using empty curly braces as placeholders for format method'
for tcase,ans in zip(testcases,answers):
    print('test case number {} ,ans is {}'.format(tcase,ans))
    
'output'    
# test case number t1 ,ans is 22
# test case number t2 ,ans is 33
# test case number t3 ,ans is 44
# test case number t4 ,ans is 55

'''
4. To loop over a sequence in reverse we,
first specify the sequence in a forward direction
and then call the reversed() function
'''

for i in reversed(range(1,10,2)):
    print(i)
 
'output'    
9
7
5
3
1

'''
5. To loop over a sequence in sorted order use "sorted()" function,
which returns a new sorted list
while leaving the source unaltered
'''

nums = [7,6,5,4,3,2,1]
for i in sorted(nums):
    print(i)

'output'    
1
2
3
4
5
6
7
print(nums)  #[7, 6, 5, 4, 3, 2, 1]

'''
6. Using set() over a sequence , removes duplicate items

'''

chars = 'aabbccdd'
print(set(chars))  #{'b', 'd', 'c', 'a'}

nums = [11,22,33,11,22,11]
print(set(nums))   #{33, 11, 22}

'if we want to remove duplicates + iterate over sorted sequence at same time'
'we can use both sorted() and set()'

nums = [99,44,11,33,11,22]
for i in sorted(set(nums)):
    print(i)
    
'output'
11
22
33
44
99

'''
7. Sometimes it is not suitable to change a list while iterating over it.
so its safer we create a new list
'''

#NOTE: float('nan') represents NaN (not a number)

import math

raw_data = [12,13,float('nan'),10,float('nan'),22]
filtered_data = []

for i in raw_data:
    if not math.isnan(i):
        filtered_data.append(i)
        
print(filtered_data)  #[12, 13, 10, 22]