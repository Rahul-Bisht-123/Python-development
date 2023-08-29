#----------------------------------------------------------|
#                   Unit - 7  | File 6                     |
#                     "Input/Outpt"                        |
#     (This is file 6 containing notes of pydocs unit-7)   |
#----------------------------------------------------------|


# 1. formatted string literals (using f or F)

user = 'john'
line = f'what are yout doing {user}'
print(line) #what are yout doing john

greet = F'how are you {user}'
print(greet)  #how are you john

# ---------------------------------------
#using str() and repr()

s = 'this is a string'
print(str(s))  #this is a string
print(repr(s)) #'this is a string'

# -------------------------
a = 9/5
b = str(9/5)
print(a, type(a))   #1.8 <class 'float'>
print(b, type(b))   #1.8 <class 'str'>

#-------------------------

x = 10*3.25
y = 200*200

s= 'the value of x = ' +repr(x)+' the value of y = '+repr(y)

print(s) #the value of x = 32.5 the value of y = 40000
print(type(s))  #<class 'str'>

#---------------------------
# the repr() of a string adds string quotes and backslashes:
hello = 'hello ,world\n'
print(hello) #hello ,world

'one line space is also present in above print statement output'

print(repr(hello)) #'hello ,world\n'

# -----------------------------------
# the argument of repr() may be any python object:

# print(repr(x,y,('spam','eggs')))  
# TypeError: repr() takes exactly one argument (3 given)

print(repr((x,y,('spam','eggs'))))
# (32.5, 40000, ('spam', 'eggs'))


# ------------------------------------------
'Formatted string literals'
'also known as f-string'

pi = 3.145555566
print(f'the value of pi is {pi:.3f}')
# the value of pi is 3.146

# --------------------------------------------
# -Passing an integer after the ':' will cause that field to 
#  be a minimum number of characters wide. 
# -This is useful for making columns line up.

table = {'ram': 401, 'shyam':402,'tom':403}

for name,room in table.items():
    print(f'{name:5}={room:5}')
    
# ram  =  401
# shyam=  402
# tom  =  403

# -----------------------------------
# Other modifiers can be used to convert 
# the value before it is formatted. 
# '!a' applies ascii(), 
# '!s' applies str(), and 
# '!r' applies repr():

char = 'b'
print(f'the !a is for ascii()  = {char!a}')
print(f'the !s is for str() = {char!s}')
print(f'the !r is for repr() = {char!r}')

# ---------------------------------
# The = specifier can be used to expand an expression 
# to the text of the expression, an equal sign, then 
# the representation of the evaluated expression:

name = 'snowbell'
age = 35
print(f'hi my {name=} and my {age=}')
# hi my name='snowbell' and my age=35

# --------------------------------------------
# str.format()
print('i am {} and age is {}'.format('fish',34))
# i am fish and age is 34

print('i am {name} and age is {age}'.format(name='ram',age=44))
# i am ram and age is 44

print('i am {0} and my age is {1}'.format('hat',44))
# i am hat and my age is 44

print('i am {0} and my age is {age}'.format('groot',age=999))
# i am groot and my age is 999

# -----------------------------------
users = {'ram':45,'shyam':46}
print('ram : {ram:d} , shyam : {shyam:d}'.format(**users))
# ram : 45 , shyam : 46

print('ram : {0[ram]:d} , shyam : {0[shyam]:d}'.format(users))
# ram : 45 , shyam : 46

# ------------------------------------------
# printing numbers 1to10 , with their squares , with their cubes

for i in range(1,11):
    print('{0:2d} || {1:3d} || {2:4d}'.format(i,i**2,i**3))
    
# 1 ||   1 ||    1
#  2 ||   4 ||    8
#  3 ||   9 ||   27
#  4 ||  16 ||   64
#  5 ||  25 ||  125
#  6 ||  36 ||  216
#  7 ||  49 ||  343
#  8 ||  64 ||  512
#  9 ||  81 ||  729
# 10 || 100 || 1000

# -------------------------------------------
# There is another method, str.zfill(), which pads a 
# numeric string on the left with zeros. 
# It understands about plus and minus signs:

print('12'.zfill(4))  #0012
print('pp'.zfill(4))  #00pp

print('-12'.zfill(4))  #-012


# -----------------------------------------
'Reading and Writing files'
# ------------------------------------------

'''
r = read
w = write
a = append
r+ = read and writing
'''
# file = open('hello.py','r+')

# ------------------------------------------
# If you have an object x, 
# you can view its JSON string representation 
# with a simple line of code:

import json
x = 'this is important data'
print(json.dumps(x))
# "this is important data"