#-------------------------------------------------------------|
'                        Unit - 4   (File3)                   |'
'                  "More Control Flow Tools"                  |'
'        (this is file 3 contains notes of pydocs unit-4)     |'
#-------------------------------------------------------------|

# -------------'if statements'-------------------------
'''
num = int(input("enter your age "))
if num<18:
    print('Sorry :( You can not vote')

elif num==18:
    print('Yes :) You can vote')

else:
    print('Give vote :)')    
'''
# --------------'for statements'-------------------------

#Example 1
'''
'measure length of words'
words = ['cat', 'window', 'defenestrate']

for i in words:
    print(i , len(i))

# cat 3
# window 6
# defenestrate 12

'''

#Example 2
'create a sample collection'

users = {'dog':'online',
         'rat':'online',
         'lion':'offline'}

# Strategy : Iterate over a copy
for user,status in users.copy().items():
    if status=='offline':    
        del users[user]      #(passing key in dict for deletion of item)

# Strategy : Create a new collection
active_users = {}
for user , status in users.items():
    if status=='online':
        active_users[user] = status   #(inserting items in new dict)

print(users)         #{'dog': 'online', 'rat': 'online'}
print(active_users)  #{'dog': 'online', 'rat': 'online'}


#---------------the range() function-----------------------

'If you do need to iterate over sequence of numbers'
'the built-in function range() comes very handy'
'It generates arithmetic progressions'

for i in range(6):
    print(i)
''''''
# the range function produces items from => 0 to range-1 
# => 0 to 6-1 
# => 0-5
0
1
2
3
4
5
''''''

'we can also modify the range to start and end at different numbers'
'also we can control the steps or differences'
# --------------------------------------|
#         range(start, end , step)      |
#         note: end is non inclusive    |
# --------------------------------------| 

for i in range(1,5):print(i , end = ',') #1,2,3,4,
print() #for gaping
for i in range(1,10,2):print(i , end = ',')#1,3,5,7,9,
print()
for i in range(-10,0,2):print(i,end=',') #-10,-8,-6,-4,-2,
print()
# --------------------------------------------------------
'to iterate over the indices of a sequence'
'we can combine range() and len() as follows'
'''
list = ['a' , 'b' , 'c' , 'd']
for i in range(len(list)):
    print(i,list[i])

'output'
# 0 a
# 1 b
# 2 c
# 3 d
'''
print(range(5))       #range(0, 5)
print(sum(range(5)))  #10

# note: the sum() takes an iterable object

# ---------------break,continue,and else clauses on loops---------------
'''
# The break statement breaks out of the innermost 
enclosing for or while loop.

# A for or while loop can include and else clause.

# In a for loop , the else clause is executed after the
loop reaches its final iteration

# In a while loop , else clause is executed after the loop's
condition becomes false.

## In either kind of loop,
the else clause is 'not' executed if 
the loop was terminated by a break.  

'''

for i in range(2,10):
    for x in range(2,i):
        if i%x==0:
            print(i,'equals',x,'*',i//x)
            break
    
    else: #loop fell through without finding the factor
        print(i,'is a prime number')

'output'
# 2 is a prime number
# 3 is a prime number
# 4 equals 2 * 2
# 5 is a prime number
# 6 equals 2 * 3
# 7 is a prime number
# 8 equals 2 * 4
# 9 equals 3 * 3

# ------------------------continue-----------------------
'the continue statement, continues with the next itertaion of the loop'
#Example :

for i in range(1,11):
    if i%2==0:
        print(i,'is an even number')
        continue
    print(i,'is odd number')

'output'
# 1 is odd number
# 2 is an even number
# 3 is odd number
# 4 is an even number
# 5 is odd number
# 6 is an even number
# 7 is odd number
# 8 is an even number
# 9 is odd number
# 10 is an even number

#---------------------------pass---------------------
'pass statements'
'''
-The pass statement does nothing.
-It can be used when a statement is required syntactically 
but the program requires no action
'''
#for example:
'''
--------------------------------------------------------|
while True:                                             |
    pass  #busy-wait for keyboard interrupt (ctrl+c)    |
--------------------------------------------------------|    

'''
# ---------------------------------------------------------
# This is commonly used for creating minimal classes:

class MyEmptyClass:
    pass
# ---------------------------------------------------------

# Another place 'pass' can be used is as a place holder
# for a functional or conditional body , when you are working on new code
# allowing you to keep thinking at a more abstract level.
# The pass is silently ignored:

def initlog(*args):
    pass #Remember to implement this!


# --------------------match statements---------------------- 
'''
A match statement takes an expression and compares its value to
successive patterns given as one or more case blocks.

Only the first pattern that matches gets executed and it can 
also extract components(sequence elements or object attributes)
from the value into the variable
'''
#The simplest form compares a subject value against one or more literals:

def http_error(status):
    match status:
        case 400: return "Bad request"
        case 404: return "Not found"
        case 418: return "I am a tea pot"
        case 200|201|202|203 : return "case is under 200 series"
        case _: return "Something wrong with internet"

print(http_error(404))  #Not found
print(http_error(500))  #Something wrong with internet

'''
Note the last block : the variable name _ acts as a wildcard
and never fails to match.
If no case matches,none of the branches is executed.

You can combine serveral literals in a single pattern
using | ("or")

'''
print(http_error(200)) #case is under 200 series
print(http_error(201)) #case is under 200 series
print(http_error(202)) #case is under 200 series
print(http_error(203)) #case is under 200 series

# ---------------------------------------------------
'Patterns can also look like unpacking assignments'
'and can be used to bind variables:'

#example
'''
----------------------------------------|
# note : (f-string is used below)       |
name = 'ram'                            |
print(f'name = {name}')   #name = ram   |
----------------------------------------|
'''
#point is an (x,y) tuple
def pointer(point):
    match point:
        case (0,0): print('origin')
        case (0,y): print(f'y={y}')
        case (x,0): print(f'X={x}')
        case (x,y): print(f'x={x},y={y}')
        case _: raise ValueError('not a point')


pointer((0,0))
pointer((1,0))
pointer((0,2))
pointer((3,5))
# pointer((0))

'output'
# origin
# X=1
# y=2
# x=3,y=5
# ValueError: not a point


# -------------------------------------------
'Defining functions'
# The keyword 'def' introduces a function definition.


'this function will write the fibonacci series from given value'

def fibo(n):
    a,b = 0,1
    while a < n :
        print(a , end = ',')
        a,b = b ,a+b
    print()

fibo(100)    #0,1,1,2,3,5,8,13,21,34,55,89,
fi = fibo  # accessing function using different name 
fi(1000)   #0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,

'''
write a function that returns a list of fibonacci series upto n
'''
def fiboni(n):
    a,b=0,1
    result = []
    while a < n:
        result.append(a)
        a,b = b,a+b
    return result

print(fiboni(100))  #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# -------------------------------------------------------------------
'                     MORE ON DEFINING FUNCTIONS                    '
# -------------------------------------------------------------------

'''
-Is is also possible to define functions with variable number of
arguments.
-There are three forms, which can be combined.

'''
# ------------------------------|
# 1. Default Argument Values    |
# ------------------------------|

def ask_ok(prompt , retries=3 ,reminder='please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y' , 'ye' , 'yes'):
            return True
        if ok in ('n', 'no' ,'nope'):
            return False
        retries = retries -1
        
        if retries<0:
            raise ValueError('invalid user response')
        print(reminder)
        
# ask_ok('do you want to quit ')
# ask_ok('want to quit' , 2)
# ask_ok('want to quit' , 2 , 'only yes or no')

'''NOTE : this example contains "in" keyword.
This tests whether or not a sequence contains a certain value'''

# ---------------------------------|
# !!! IMPORTANT WARNING            |
# ---------------------------------|
'''
-The default value is evaluated only once.
-This makes a difference when the default is a mutable object such
as a list , dictionary or instances of most classes
'''
#For example: The following function accumulates the arguments
#             passed to it on subsequent calls

def f(a,l=[]):
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))

'output'
# [1]
# [1, 2]
# [1, 2, 3] 

#Probelm:
'we wanted a new empty list everytime'
'but we got the same previous list getting appended'

#Solution :
"If you don't want the default to be shared between subsequent calls"
"we can write the above f function like this:"

def f2(a,l=None):
    if l is None:l=[]
    l.append(a)
    return l

print(f2(1))
print(f2(2))
print(f2(3))

'output'
# [1]
# [2]
# [3]

# ----------------------------|
# 2. KEYWORD ARGUMENTS        |
# ----------------------------|
'''
-Functions can also be called using the keyword arguments 
of the form kwargs = value.
'''
def parrot(cost , color = 'red' , age = 12):
    print('this parrot cost is',cost)
    print('this parrot color is',color)
    print('this parrot age is', age)
    
#parrot() 
#TypeError: parrot() missing 1 required positional argument: 'cost'

parrot(200)
# this parrot cost is 200
# this parrot color is red
# this parrot age is 12

parrot('50 bucks' ,color='black')
# this parrot cost is 50 bucks
# this parrot color is black
# this parrot age is 12

parrot(99,age=69,color='grey')
# this parrot cost is 99
# this parrot color is grey
# this parrot age is 69

# ---------------------------------------------------|
'              UNPACKING ARGUMENTS LISTS             |'
# ---------------------------------------------------|
'''
-The situation can occurs when the arguments are already 
in a list or tuple but need to be unpacked for a function call
requiring separate positional arguments.
'''
print(range(3,6))  #range(3, 6)

print(list(range(3,6)))  #[3, 4, 5]

args = [3,6]
print(list(range(*args)))   #[3, 4, 5]

# NOTE: do not define any variable names 'list = ' 
# otheriwse the list(range(3,6)) will give error , that is
# TypeError: 'list' object is not callable

# ---------------------------------------------------------
'''IN THE SAME FASHION , DICTIONARIES CAN DELIVER KEYWORDS ARGUMENTS
WITH THE '**' OPERATOR'''

def cat(name,age,cost):
    print('cat name is',name,'her age is',age,'her cost is',cost)
    
catinfo = {'name':'snowbell' , 'age':12 , 'cost': '50'}

'(wrong way , used * for dictionary )'
cat(*catinfo) #cat name is name her age is age her cost is cost

'right way , used ** for dictionary'
cat(**catinfo) #cat name is snowbell her age is 12 her cost is 50

# --------------------------------------------------------------------
# --------------------------------------|
#             Lambda Expressions        |
# --------------------------------------|
'''
Small anonymous functions can be created using the lambda keyword.
this function returns the sum of its two arguments:
lambda a,b : a+b
'''

def lambda_demo(num):
    return lambda a : a*num

mydoubler = lambda_demo(2)
mytripler = lambda_demo(3)

print(mydoubler(5)) # 10
print(mytripler(4)) # 12

x = lambda a : a*2
print(x(22))   #44

greet = lambda z : 'hello ' + z
print(greet('jack'))  #hello jack

# -----------------------------------------
nums = [4,7,1,3]
nums.sort()
print(nums)  #[1,3,4,7]

nums2 = [1,2,3,4]
nums2.sort(reverse=True)
print(nums2)   #[4, 3, 2, 1]

# -----------------------------------------------------|
'     Here is an example of multi-line docstring:      |'
#------------------------------------------------------|
def dummy():
    '''
    This function does nothing.
    only contains pass
    '''
    pass

print(dummy.__doc__)
'output'
# this function does nothing
#     only contains pass

#-----------------------------------------------|
'             Function Annotations              |'
#-----------------------------------------------|

# Function annotations are completely optional 
# metadata information about the types used by user-defined functions 

# Annotations are stored in the __annotations__ attribute 
# of the function as a dictionary and have no effect on any 
# other part of the function.

# Parameter annotations are defined by a colon 
# after the parameter name, followed by an expression 
# evaluating to the value of the annotation. 

# Return annotations are defined by a literal ->, 
# followed by an expression, between the parameter 
# list and the colon denoting the end of the def statement. 

# The following example has a required argument, 
# an optional argument, and the return value annotated:

def anno_func(cat:str , age:int = 32) -> str:
    print('annotations are ' , anno_func.__annotations__)
    print('arguments' , cat , age)
    return 'this '+cat+'is '+str(age)+ 'years old.'
    
print(anno_func('snowbell'))

'output'
# annotations are  {'cat': <class 'str'>, 'age': <class 'int'>, 'return': <class 'str'>}
# arguments snowbell 32
# this snowbellis 32years old.