#------------------------------------------------------|
#                     Unit-3                           |
#        An informal introduction to python            |
#     (This file contains pydocs Unit-3 notes )        | 
#------------------------------------------------------| 


the_world_is_flat = True

if the_world_is_flat:
    print("Be careful not to fall off!!!")

# ---------------------------------------------

#this is a comment
spam = 1   #this is second comment
           #this is third..
text = "# this is not a comment because its inside quotes"

# ---------------------------------------------
'''
+ add 
- subtract
/ divison [will return float value]
// floor division [will return integer value only (no decimals)]
% modulo [will return remainder]
** power [2**3]= 2*2*2
'''
print(2+3)
print(2-3)
print(3/2)
print(3//2)
print(10%7)
print(3**3)

# ---------------------------------------------
s = 'C:\desktop\name'
print(s)

#the output of above print is :
'''
C:\desktop
ame
'''
#because \n is new line character

'''
If you not want characters prefaced by \ to be interpreted as special
characters , you can use raw strings 
by using adding r before the first quote.
'''
print(r'c:\desktop\name')

# ---------------------------------------------
# String can be concatenated with + operator and repeated with *
print(3*'ab' + 'is')  #abababis

# Two or more string literals next to each other 
# are automatically concatenated
print('rr' 'vv') #rrvv

# ---------------------------------------------
word = 'python'
print(word[0])
print(word[-1])
print(word[5])

# ---------------------------------------------
# slicing allows you to obtain substring

print(word[0:3]) #pyt  (index 3 is not included)
print(word[:3])  #pyt  (omitting first index defaults to 0)
print(word[3:])  #hon  (omitting second index defaults to last index)
print(word[-6:])

'print(word[55])'  # this will give error of index out of bound

"But out of range slice indexes are handled gracefully when used for slicing"
print(word[4:55]) #on  (this does not throw error of index out of bound)
print(word[99:])  # ''  (this gives empty string)

# -------------------------------------------------

#NOTE: Python strings are immutable 
#So assigning to an indexed position in the strings results in an error

'''
word[0] = 'r'     (gives type error as below)
word[2:] = 'abc'   (gives type error as below )
''' 
#TypeError: 'str' object does not support item assignment

# ----------------------------------------------
'If you need a different string, you should create a new one'
print('hi ' + word[0:])    #hi python

'The built in function len() returns the length of the string'
print(len('joker'))   #5


# ----------------------------------------------

'Lists can contain items of different types'
'But usually the items all have the same type'

mylist = [1,2,3,4,5]
print(mylist)   #[1, 2, 3, 4, 5]

'Lists can also be sliced and indexed'

print(mylist[3])   #4
print(mylist[2:])  #[3,4,5]

'''all slice operations returns a new list 
containing containing the requested elements.
This means that the following slice returns a shallow copy of the string '''

print(mylist[:])  #[1, 2, 3, 4, 5]

'Lists are mutable'
mylist[0]  = 99
print(mylist)  #[99, 2, 3, 4, 5]

'Lists support opeartions like concatenation'
print(mylist + [99,89,79])  #[99, 2, 3, 4, 5, 99, 89, 79]

# ----------------------------------------------
'append() method'
'''we can add new items at the end of the list,
 using the append() method'''

mylist.append('new item')
print(mylist)  #[99, 2, 3, 4, 5, 'new item']

# ----------------------------------------------
'Assignment to slices is also possible'
'this can change the size of the list or clear it entirely'

letter = ['a','b','c','d']
print(letter) #'a', 'b', 'c', 'd']

letter[2:] = [3,4,5]
print(letter)  #['a', 'b', 3, 4, 5]

letter = []
print(letter)   #[]

# ----------------------------------------------
'len() function can also be used for lists'
list = [3,4,5,6]
print(len(list))  #4

# ----------------------------------------------
'It is possible to nest lists(creating list inside list)'
'for example'
list1 = [1,2,3]
list2 = ['red','blue','green']
list3 = [list1,list2]
print(list3)  #[[1, 2, 3], ['red', 'blue', 'green']]

print(list3[0])     #[1, 2, 3]
print(list3[1])     #['red', 'blue', 'green']
print(list3[0][2])  #3
print(list3[1][0])  #red

#------------------------------------------------|
#      First Step Towards Programming            |
#------------------------------------------------|

'Fibonacci Series'
"the sum of first two elements defines the next"

a,b = 0,1
while a < 10:
    print(a,end = ',')
    a,b = b,a+b
print()
'output'
#0,1,1,2,3,5,8,

'the first line contains multiple assignments'
'the variables a and b simultaneously gets the new values 0 and 1'

#------------------------------------------------
'Using print()'
state = 'stop'
print('the red signal indicates to', state)
#the red signal indicates to stop

#------------------------------------------------
'Note: ** has higher precedence than -'
'so , -3**2 will be interpreted as -(3**2), which results to -9'
'to avoid this and get 9 you can use (-3)**2'

print(-3**2)    #-9
print((-3)**2)  #9

##------------------------------------------------
'''
Unlike other languages, 
special characters such as \n has the same meaning with both 
single('...') and double("...") quotes.

The only difference between the two is that within the single quotes,
we don't need to escape the double quote (") 
but we have to escpae (\') single quotes 
and vice-versa .
'''

print('can use double quotes " freely inside single quotes')
# can use double quotes " freely inside single quotes

print('But use \'back slash\' to use single quotes inside single quotes')
# But use 'back slash' to use single quotes inside single quotes

print("can use 'single quotes' freely inside double quotes")
# can use 'single quotes' freely inside double quotes

print("But use \"backslash\" to use double quotes inside doube quotes")
# But use "backslash" to use double quotes inside doube quotes